#!/usr/bin/env python3
"""
愛の装置 — H3 一括生成ランナー

h3_manifest.json の27件を上から順に生成し、正しいファイル名で保存します。
生成順ではなくマニフェストのidで名前が決まるので、完了順が前後しても、
途中で失敗しても、出力が取り違わることはありません。

RunPodのGPUは起動中ずっと課金されるため、このスクリプトは
「人が次を投げるまでの待ち時間」をゼロにすることを目的にしています。

  使い方
    python run_h3_batch.py --dry-run          # 何が実行されるか確認（課金なし）
    python run_h3_batch.py                    # 全27本を生成
    python run_h3_batch.py --only C04         # Cut 4 の3本だけ
    python run_h3_batch.py --only C04P2       # 1本だけ
    python run_h3_batch.py --workers 3        # 3本同時（APIが非同期の場合のみ）

  再開
    出力ファイルが既にあるジョブは自動でスキップします。
    Podが落ちてももう一度実行すれば続きから再開でき、生成済みの分に再課金されません。

  ★ 唯一の編集箇所は generate_one() です。
    H3の呼び出し方（RunPodのエンドポイント / ローカルAPI / CLI）に合わせて
    中身を書いてください。それ以外は触る必要がありません。
"""

import argparse
import concurrent.futures
import csv
import json
import os
import sys
import time
import traceback
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "h3_manifest.json")


# ───────────────────────────────────────────────────────────────
# ★ ここだけ書き換えてください
# ───────────────────────────────────────────────────────────────

def generate_one(job, image_path, output_path):
    """1本生成して output_path に保存する。

    job       : マニフェストの1件。job["prompt"] にプロンプト全文、
                job["duration_sec"] に尺（6.0）が入っています。
    image_path: 第1フレーム画像のフルパス
    output_path: ここに .mp4 を保存する（このパスは呼び出し側が決めています）

    成功したら output_path にファイルが存在する状態で return してください。
    失敗は例外を投げてください（自動でリトライされます）。

    以下は書き方の例です。実際のエンドポイントとパラメータ名は
    お使いのRunPod構成に合わせて差し替えてください。
    """
    raise NotImplementedError(
        "generate_one() を実装してください。"
        "run_h3_batch.py の中のコメント例を参照。"
    )

    # ── 例A：RunPod Serverless エンドポイント（同期 runsync）────────
    # import base64, requests
    # endpoint = os.environ["RUNPOD_ENDPOINT_ID"]
    # api_key  = os.environ["RUNPOD_API_KEY"]
    # with open(image_path, "rb") as f:
    #     image_b64 = base64.b64encode(f.read()).decode()
    # r = requests.post(
    #     "https://api.runpod.ai/v2/%s/runsync" % endpoint,
    #     headers={"Authorization": "Bearer " + api_key},
    #     json={"input": {
    #         "prompt": job["prompt"],
    #         "image": image_b64,
    #         "duration": job["duration_sec"],
    #     }},
    #     timeout=1800,
    # )
    # r.raise_for_status()
    # data = r.json()
    # video_b64 = data["output"]["video"]          # ← 実際のキー名に合わせる
    # with open(output_path, "wb") as f:
    #     f.write(base64.b64decode(video_b64))

    # ── 例B：Pod内のローカルAPI（Gradio / FastAPI など）──────────
    # import requests
    # with open(image_path, "rb") as f:
    #     r = requests.post(
    #         "http://127.0.0.1:8000/generate",
    #         data={"prompt": job["prompt"], "duration": job["duration_sec"]},
    #         files={"image": f},
    #         timeout=1800,
    #     )
    # r.raise_for_status()
    # with open(output_path, "wb") as f:
    #     f.write(r.content)

    # ── 例C：コマンドラインツールを叩く ──────────────────────
    # import subprocess
    # subprocess.run([
    #     "python", "inference.py",
    #     "--image", image_path,
    #     "--prompt", job["prompt"],
    #     "--duration", str(job["duration_sec"]),
    #     "--output", output_path,
    # ], check=True)


# ───────────────────────────────────────────────────────────────
# 以下は触らなくて構いません
# ───────────────────────────────────────────────────────────────

def load_jobs():
    with open(MANIFEST, encoding="utf-8") as f:
        return json.load(f)["jobs"]


def run_job(job, args, image_dir, out_dir):
    jid = job["id"]
    image_path = os.path.join(image_dir, job["image"])
    output_path = os.path.join(out_dir, job["output"])

    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        return {"id": jid, "status": "skipped", "seconds": 0.0,
                "output": job["output"], "error": ""}

    if not os.path.exists(image_path):
        return {"id": jid, "status": "no_image", "seconds": 0.0,
                "output": job["output"],
                "error": "画像がありません: " + image_path}

    if args.dry_run:
        return {"id": jid, "status": "dry_run", "seconds": 0.0,
                "output": job["output"], "error": ""}

    tmp_path = output_path + ".part"
    last_error = ""
    for attempt in range(1, args.retries + 1):
        started = time.time()
        try:
            generate_one(job, image_path, tmp_path)
            if not os.path.exists(tmp_path) or os.path.getsize(tmp_path) == 0:
                raise RuntimeError("出力ファイルが作られていません")
            os.replace(tmp_path, output_path)
            return {"id": jid, "status": "ok",
                    "seconds": round(time.time() - started, 1),
                    "output": job["output"], "error": ""}
        except Exception as e:
            last_error = "%s: %s" % (type(e).__name__, e)
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except OSError:
                    pass
            log("  × %s 失敗 (%d/%d) %s" % (jid, attempt, args.retries, last_error))
            if attempt < args.retries:
                time.sleep(min(30, 5 * attempt))

    return {"id": jid, "status": "failed", "seconds": 0.0,
            "output": job["output"], "error": last_error}


def log(msg):
    print("[%s] %s" % (datetime.now().strftime("%H:%M:%S"), msg), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", default=os.path.join(HERE, "keyframes"),
                    help="第1フレーム画像のフォルダ")
    ap.add_argument("--out", default=os.path.join(HERE, "output"),
                    help="動画の保存先フォルダ")
    ap.add_argument("--only", default="",
                    help="C04 や C04P2 のように絞り込む")
    ap.add_argument("--workers", type=int, default=1,
                    help="同時実行数。APIが非同期の場合のみ増やす")
    ap.add_argument("--retries", type=int, default=2,
                    help="失敗時のリトライ回数")
    ap.add_argument("--dry-run", action="store_true",
                    help="実行せず計画だけ表示（課金なし）")
    args = ap.parse_args()

    jobs = load_jobs()
    if args.only:
        key = args.only.upper()
        jobs = [j for j in jobs if j["id"].startswith(key)]
    if not jobs:
        log("該当するジョブがありません: " + args.only)
        return 1

    os.makedirs(args.out, exist_ok=True)

    log("対象 %d 本 / 画像 %s / 出力 %s" % (len(jobs), args.images, args.out))
    if args.dry_run:
        log("--dry-run: 実際の生成は行いません")

    missing = sorted({j["image"] for j in jobs
                      if not os.path.exists(os.path.join(args.images, j["image"]))})
    if missing:
        log("!! 画像が見つかりません（該当ジョブはスキップされます）:")
        for m in missing:
            log("   - " + m)

    started = time.time()
    results = []

    if args.workers > 1:
        log("同時実行 %d 本" % args.workers)
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(run_job, j, args, args.images, args.out): j for j in jobs}
            for fut in concurrent.futures.as_completed(futures):
                r = fut.result()
                results.append(r)
                log("  %-8s %-9s %s" % (r["id"], r["status"], r["output"]))
    else:
        for n, j in enumerate(jobs, 1):
            log("(%d/%d) %s  %s ／ パターン%s %s"
                % (n, len(jobs), j["id"], j["cut_title"], j["pattern"], j["axis"]))
            r = run_job(j, args, args.images, args.out)
            results.append(r)
            log("  %-8s %-9s %s  %ss" % (r["id"], r["status"], r["output"], r["seconds"]))

    results.sort(key=lambda r: r["id"])
    logpath = os.path.join(args.out, "run_log_%s.csv" % datetime.now().strftime("%Y%m%d_%H%M%S"))
    with open(logpath, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "status", "seconds", "output", "error"])
        w.writeheader()
        w.writerows(results)

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    elapsed = time.time() - started
    log("─" * 52)
    log("完了 %d分%d秒" % (int(elapsed // 60), int(elapsed % 60)))
    for k in sorted(counts):
        log("  %-9s %d" % (k, counts[k]))
    log("ログ: " + logpath)

    failed = [r for r in results if r["status"] in ("failed", "no_image")]
    if failed:
        log("!! 未完了 %d 本。直してもう一度実行すれば、この分だけ生成されます:" % len(failed))
        for r in failed:
            log("   - %s  %s" % (r["id"], r["error"]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
