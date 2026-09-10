#!/usr/bin/env python3
"""H3 生成ログ・原価管理ツール

「どの動画を、どのプロンプトで、どのモデルで作ったか」と
「その案件にいくらかかったか」を1つの台帳で管理する。

台帳は2つ:
  生成ログ.csv     … 1生成 = 1行。中身(プロンプト・モデル・判定)の記録
  Pod稼働ログ.csv  … 1セッション = 1行。RunPodに実際に課金された時間

この2つを突き合わせると「払った時間のうち、何%が実際の生成だったか」が出る。
それがローカルPCを買うべきかどうかの判断材料になる。
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

JST = timezone(timedelta(hours=9))
BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = BASE_DIR / "07_System" / "Ledger"

GEN_FILE = "生成ログ.csv"
POD_FILE = "Pod稼働ログ.csv"
STATE_FILE = ".pod-state.json"

GEN_FIELDS = [
    "timestamp", "project", "cut", "version", "mode", "model", "quant",
    "gpu", "rate_usd_hr", "compute_s", "cost_usd", "resolution",
    "duration_s", "steps", "seed", "video", "verdict", "prompt_ref", "note",
]
POD_FIELDS = [
    "start", "end", "project", "gpu", "rate_usd_hr",
    "billed_s", "cost_usd", "note",
]


# ---------------------------------------------------------------- helpers

def now() -> datetime:
    return datetime.now(JST).replace(microsecond=0)


def iso(dt: datetime) -> str:
    return dt.isoformat()


def parse_dt(text: str) -> datetime:
    dt = datetime.fromisoformat(text)
    return dt if dt.tzinfo else dt.replace(tzinfo=JST)


def ensure(path: Path, fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.stat().st_size == 0:
        with path.open("w", newline="", encoding="utf-8") as fh:
            csv.DictWriter(fh, fieldnames=fields).writeheader()


def append(path: Path, fields: list[str], row: dict) -> None:
    ensure(path, fields)
    with path.open("a", newline="", encoding="utf-8") as fh:
        csv.DictWriter(fh, fieldnames=fields).writerow(
            {k: row.get(k, "") for k in fields}
        )


def read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(value: str | float | None, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def cost_of(rate_usd_hr: float, seconds: float) -> float:
    return round(rate_usd_hr * seconds / 3600.0, 4)


def hhmm(seconds: float) -> str:
    total = int(round(seconds))
    return f"{total // 3600}時間{(total % 3600) // 60:02d}分"


def yen(amount: float) -> str:
    return f"¥{amount:,.0f}"


def in_period(row_ts: str, since: datetime | None, until: datetime | None) -> bool:
    if not row_ts:
        return False
    try:
        stamp = parse_dt(row_ts)
    except ValueError:
        return False
    if since and stamp < since:
        return False
    if until and stamp > until:
        return False
    return True


# ------------------------------------------------------------ pod session

def cmd_pod_start(args, ledger: Path) -> int:
    state_path = ledger / STATE_FILE
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        print(
            f"⚠️  Podセッションは既に開始されています "
            f"({state['start']} / {state['gpu']})。\n"
            f"    先に `pod end` で閉じてください。",
            file=sys.stderr,
        )
        return 1
    state = {
        "start": iso(now()),
        "project": args.project,
        "gpu": args.gpu,
        "rate_usd_hr": args.rate,
        "note": args.note or "",
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"▶️  Pod開始: {args.gpu} (${args.rate}/hr) / 案件: {args.project}")
    print(f"   開始時刻: {state['start']}")
    print("   終わったら必ず `python3 scripts/h3log.py pod end` を実行してください。")
    return 0


def cmd_pod_end(args, ledger: Path) -> int:
    state_path = ledger / STATE_FILE
    if not state_path.exists():
        print("⚠️  開始中のPodセッションがありません。", file=sys.stderr)
        return 1
    state = json.loads(state_path.read_text(encoding="utf-8"))
    start = parse_dt(state["start"])
    end = now()
    billed = (end - start).total_seconds()
    rate = num(state["rate_usd_hr"])
    usd = cost_of(rate, billed)
    append(ledger / POD_FILE, POD_FIELDS, {
        "start": iso(start), "end": iso(end), "project": state["project"],
        "gpu": state["gpu"], "rate_usd_hr": rate,
        "billed_s": int(billed), "cost_usd": usd,
        "note": args.note or state.get("note", ""),
    })
    state_path.unlink()
    print(f"⏹  Pod終了: {hhmm(billed)} / ${usd:.2f}")
    return 0


def cmd_pod_add(args, ledger: Path) -> int:
    """過去のセッションを後から手入力する(4日ぶんの実績を遡って入れる用)。"""
    start = parse_dt(args.start)
    billed = args.minutes * 60
    end = start + timedelta(seconds=billed)
    usd = cost_of(args.rate, billed)
    append(ledger / POD_FILE, POD_FIELDS, {
        "start": iso(start), "end": iso(end), "project": args.project,
        "gpu": args.gpu, "rate_usd_hr": args.rate,
        "billed_s": int(billed), "cost_usd": usd, "note": args.note or "",
    })
    print(f"✅ Pod稼働を記録: {hhmm(billed)} / ${usd:.2f}")
    return 0


# ------------------------------------------------------------- generation

def cmd_gen_add(args, ledger: Path) -> int:
    state_path = ledger / STATE_FILE
    gpu, rate = args.gpu, args.rate
    if (not gpu or rate is None) and state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        gpu = gpu or state.get("gpu", "")
        rate = state.get("rate_usd_hr") if rate is None else rate
    rate = num(rate)
    usd = cost_of(rate, args.compute_s) if args.compute_s else ""
    append(ledger / GEN_FILE, GEN_FIELDS, {
        "timestamp": iso(now()), "project": args.project, "cut": args.cut,
        "version": args.version, "mode": args.mode, "model": args.model,
        "quant": args.quant, "gpu": gpu, "rate_usd_hr": rate,
        "compute_s": args.compute_s or "", "cost_usd": usd,
        "resolution": args.resolution, "duration_s": args.duration or "",
        "steps": args.steps or "", "seed": args.seed or "",
        "video": args.video, "verdict": args.verdict,
        "prompt_ref": args.prompt_ref, "note": args.note or "",
    })
    tail = f" / ${usd:.3f}" if usd != "" else ""
    print(f"✅ 生成を記録: {args.project} {args.cut} {args.version} [{args.verdict}]{tail}")
    return 0


# ----------------------------------------------------------------- report

def collect(ledger: Path, project: str | None,
            since: datetime | None, until: datetime | None):
    gens = [r for r in read(ledger / GEN_FILE)
            if (not project or r["project"] == project)
            and in_period(r["timestamp"], since, until)]
    pods = [r for r in read(ledger / POD_FILE)
            if (not project or r["project"] == project)
            and in_period(r["start"], since, until)]
    return gens, pods


def cmd_report(args, ledger: Path) -> int:
    since = parse_dt(args.since) if args.since else None
    until = parse_dt(args.until) if args.until else None
    gens, pods = collect(ledger, args.project, since, until)

    if not gens and not pods:
        print("⚠️  対象期間に記録がありません。", file=sys.stderr)
        return 1

    compute_s = sum(num(r["compute_s"]) for r in gens)
    billed_s = sum(num(r["billed_s"]) for r in pods)
    gpu_usd = sum(num(r["cost_usd"]) for r in pods) or sum(num(r["cost_usd"]) for r in gens)
    gpu_jpy = gpu_usd * args.jpy
    labor_jpy = args.labor_hours * args.labor_rate
    other_jpy = args.other
    total_jpy = gpu_jpy + labor_jpy + other_jpy

    ok = sum(1 for r in gens if r["verdict"].upper() == "OK")
    adopted = ok
    retry_rate = (1 - adopted / len(gens)) * 100 if gens else 0.0
    efficiency = (compute_s / billed_s * 100) if billed_s else 0.0

    period = []
    if since:
        period.append(since.strftime("%Y-%m-%d"))
    if until:
        period.append(until.strftime("%Y-%m-%d"))
    period_text = " 〜 ".join(period) if period else "全期間"

    out = []
    add = out.append
    add(f"# 制作原価レポート: {args.project or '全案件'}")
    add("")
    add(f"- **対象期間**: {period_text}")
    add(f"- **作成日**: {now().strftime('%Y-%m-%d')}")
    add(f"- **為替レート**: 1 USD = {args.jpy:.1f} 円")
    add("")
    add("## 制作ボリューム")
    add("")
    add("| 項目 | 値 |")
    add("|---|---|")
    add(f"| 生成回数(のべ) | {len(gens)} 回 |")
    add(f"| 採用カット数 | {adopted} 本 |")
    add(f"| 作り直し率 | {retry_rate:.0f}% |")
    add(f"| GPU実生成時間 | {hhmm(compute_s)} |")
    add(f"| GPU課金時間 | {hhmm(billed_s)} |")
    add(f"| 稼働効率(生成/課金) | {efficiency:.1f}% |")
    add("")
    add("## 費用内訳")
    add("")
    add("| 項目 | 内容 | 金額 |")
    add("|---|---|---|")
    add(f"| GPU利用料 | {hhmm(billed_s)}のGPUレンタル実費 | {yen(gpu_jpy)} |")
    add(f"| 制作作業費 | {args.labor_hours:.1f}時間 × {yen(args.labor_rate)}/時 | {yen(labor_jpy)} |")
    if other_jpy:
        add(f"| その他 | 素材・ソフト等 | {yen(other_jpy)} |")
    add(f"| **合計** |  | **{yen(total_jpy)}** |")
    add("")

    if gens:
        add("## カット別の内訳")
        add("")
        add("| カット | 版 | モード | モデル | 判定 | 動画ファイル |")
        add("|---|---|---|---|---|---|")
        for r in gens:
            model = "/".join(x for x in (r["model"], r["quant"]) if x)
            add(f"| {r['cut']} | {r['version']} | {r['mode']} | {model} "
                f"| {r['verdict']} | `{r['video']}` |")
        add("")

    add("---")
    add("")
    add("※ GPU利用料は実際のクラウド課金額に基づく実費です。")
    add("※ 各カットのプロンプト全文とモデル設定は制作台帳に保管しており、")
    add("　 ご要望に応じていつでも提示できます。")

    text = "\n".join(out) + "\n"
    if args.out:
        path = Path(args.out)
        if not path.is_absolute():
            path = BASE_DIR / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"✅ レポートを書き出しました: {path.relative_to(BASE_DIR)}")
    else:
        print(text)
    return 0


# ----------------------------------------------------------------- decide

def cmd_decide(args, ledger: Path) -> int:
    since = parse_dt(args.since) if args.since else None
    gens, pods = collect(ledger, None, since, None)
    if not pods:
        print("⚠️  Pod稼働ログがありません。まず `pod start` / `pod end` で"
              "実績を貯めてください(目安: 2〜4週間)。", file=sys.stderr)
        return 1

    stamps = [parse_dt(r["start"]) for r in pods]
    span_days = max((max(stamps) - min(stamps)).days, 1)
    billed_s = sum(num(r["billed_s"]) for r in pods)
    compute_s = sum(num(r["compute_s"]) for r in gens)
    usd = sum(num(r["cost_usd"]) for r in pods)

    billed_h_month = billed_s / 3600 / span_days * 30
    rent_jpy_month = usd / span_days * 30 * args.jpy

    depreciation = args.machine_cost / (args.years * 12)
    power = args.kw * (billed_h_month) * args.kwh_price
    own_jpy_month = depreciation + power

    rate_jpy_hr = (usd / (billed_s / 3600) * args.jpy) if billed_s else 0.0
    breakeven_h = own_jpy_month / rate_jpy_hr if rate_jpy_hr else 0.0

    print(f"# GPU: 借りる vs 買う 判定\n")
    print(f"- 集計期間: {span_days} 日間 / Pod稼働ログ {len(pods)} 件、生成 {len(gens)} 件")
    print(f"- 実測の課金時間: {hhmm(billed_s)}(月換算 {billed_h_month:.1f} 時間)")
    if compute_s:
        print(f"- うち実際の生成時間: {hhmm(compute_s)}"
              f"(稼働効率 {compute_s / billed_s * 100:.1f}%)")
    print(f"- 実効GPU単価: {yen(rate_jpy_hr)}/時\n")
    print("| | 月額 |")
    print("|---|---|")
    print(f"| 借りる(現状ペース) | {yen(rent_jpy_month)} |")
    print(f"| 買う({yen(args.machine_cost)} を{args.years}年で償却 + 電気代) | {yen(own_jpy_month)} |")
    print(f"\n**損益分岐点: 月 {breakeven_h:.0f} 時間**"
          f"(1日あたり約 {breakeven_h / 30:.1f} 時間)\n")

    if billed_h_month > breakeven_h:
        over = billed_h_month / breakeven_h
        print(f"→ 現在の稼働({billed_h_month:.0f}時間/月)は分岐点の {over:.1f} 倍です。")
        print("   **購入が経済的にも有利**。年間で "
              f"{yen((rent_jpy_month - own_jpy_month) * 12)} の差になります。")
    else:
        print(f"→ 現在の稼働({billed_h_month:.0f}時間/月)は分岐点を下回っています。")
        print("   **費用だけで見れば借りる方が安い**。")
        print("   購入する場合は「機密保持」と「使い放題の安心感」に")
        print(f"   月 {yen(max(own_jpy_month - rent_jpy_month, 0))} を払う判断になります。")
    return 0


# ------------------------------------------------------------------- main

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="h3log", description="H3 生成ログ・原価管理ツール",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ledger-dir", default=str(DEFAULT_LEDGER),
                   help="台帳フォルダ(既定: 07_System/Ledger)")
    sub = p.add_subparsers(dest="command", required=True)

    pod = sub.add_parser("pod", help="Podの稼働時間を記録する").add_subparsers(
        dest="pod_command", required=True)

    s = pod.add_parser("start", help="Podを起動したら実行")
    s.add_argument("--project", required=True)
    s.add_argument("--gpu", required=True, help='例: "RTX 5090"')
    s.add_argument("--rate", type=float, required=True, help="1時間あたりのUSD単価")
    s.add_argument("--note")
    s.set_defaults(func=cmd_pod_start)

    e = pod.add_parser("end", help="Podを停止したら実行")
    e.add_argument("--note")
    e.set_defaults(func=cmd_pod_end)

    a = pod.add_parser("add", help="過去の稼働を後から手入力する")
    a.add_argument("--project", required=True)
    a.add_argument("--gpu", required=True)
    a.add_argument("--rate", type=float, required=True)
    a.add_argument("--start", required=True, help="例: 2026-09-06T10:00")
    a.add_argument("--minutes", type=float, required=True)
    a.add_argument("--note")
    a.set_defaults(func=cmd_pod_add)

    gen = sub.add_parser("gen", help="生成した1本を記録する").add_subparsers(
        dest="gen_command", required=True)
    g = gen.add_parser("add", help="生成結果を1行記録する")
    g.add_argument("--project", required=True)
    g.add_argument("--cut", required=True, help="例: C-2d")
    g.add_argument("--version", required=True, help="例: v2")
    g.add_argument("--mode", default="", help="T2VA / I2VA / FL2VA / L2VA / Ref2VA")
    g.add_argument("--model", default="MiniMax-H3")
    g.add_argument("--quant", default="", help="例: bf16 / int8 / nvfp4")
    g.add_argument("--gpu", default="")
    g.add_argument("--rate", type=float, default=None)
    g.add_argument("--compute-s", type=float, default=0.0, help="生成にかかった秒数")
    g.add_argument("--resolution", default="")
    g.add_argument("--duration", type=float, default=None, help="動画の尺(秒)")
    g.add_argument("--steps", type=int, default=None)
    g.add_argument("--seed", default="")
    g.add_argument("--video", default="", help="保存した動画ファイル名")
    g.add_argument("--verdict", default="未検証", help="OK / NG / 未検証")
    g.add_argument("--prompt-ref", default="", help="プロンプトを書いたノートのパス")
    g.add_argument("--note")
    g.set_defaults(func=cmd_gen_add)

    r = sub.add_parser("report", help="案件別の原価レポートを作る")
    r.add_argument("--project")
    r.add_argument("--since")
    r.add_argument("--until")
    r.add_argument("--jpy", type=float, default=155.0, help="USD/JPY レート")
    r.add_argument("--labor-hours", type=float, default=0.0, help="制作にかけた時間")
    r.add_argument("--labor-rate", type=float, default=0.0, help="自分の時間単価(円)")
    r.add_argument("--other", type=float, default=0.0, help="その他実費(円)")
    r.add_argument("--out", help="書き出し先のパス")
    r.set_defaults(func=cmd_report)

    d = sub.add_parser("decide", help="借りる/買う を実測データから判定する")
    d.add_argument("--since")
    d.add_argument("--jpy", type=float, default=155.0)
    d.add_argument("--machine-cost", type=float, default=800000.0, help="PC購入費(円)")
    d.add_argument("--years", type=float, default=4.0, help="償却年数")
    d.add_argument("--kw", type=float, default=0.8, help="システム全体の消費電力(kW)")
    d.add_argument("--kwh-price", type=float, default=31.0, help="電気代(円/kWh)")
    d.set_defaults(func=cmd_decide)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    ledger = Path(args.ledger_dir)
    if not ledger.is_absolute():
        ledger = BASE_DIR / ledger
    return args.func(args, ledger)


if __name__ == "__main__":
    raise SystemExit(main())
