---
project: Studio-Infrastructure
type: runbook
status: ready
updated: 2026-09-10
tags: [project/studio-infra, ai/tools/runpod]
---

# GPUが空いたら、これをやる

> **このページだけ見れば進められます。** 他のノートを開く必要はありません。
> 準備は全部できています。あとはGPUの空きを待つだけです。

---

## いまの状態（2026-09-10時点）

| | |
|---|---|
| ✅ Network Volume | `minimax_h3_comfyui_volume` / **150GB** / **AP-JP-1** / 月$10.50 |
| ⏳ モデル | まだダウンロードしていない（約50GB） |
| ⏳ GPU | **在庫待ち** |
| ✅ 残高 | 約$56 |

**やり残しは「モデルのダウンロード」だけ**です。それが終われば、以後は2〜3分で生成に入れます。

---

## 今日わかったこと（大事な前提）

### AP-JP-1（日本）には、H100 SXM と H200 SXM しかない

安い48GBのカード（A6000・A40・L40S・RTX 6000 Ada）は**日本には置いていません**。
だから今までH100 SXMを使っていたのは、選んだからではなく**それしか無かったから**です。

### 安いカードはあるが、場所が問題

| GPU | 価格 | ある場所 | ライセンス |
|---|---|---|---|
| A40 48GB | $0.49 | CA-MTL-1 | ✅ カナダはOK。ただし**ボリュームが作れないDC** |
| RTX A6000 48GB | $0.53 | CA-MTL-3 / EU-RO-1 | カナダはOKだが**在庫なし** |
| RTX PRO 4500 32GB | $0.72 | EU-RO-1 / EUR-IS-1 | ⚠️ EUは**ライセンス除外地域** |
| RTX PRO 6000 96GB | $2.09 | EU / US中心 | ⚠️ 除外地域 |
| **H100 SXM 80GB** | **$3.49** | **AP-JP-1** | ✅ **日本。いちばん確実** |

> H3のライセンス適用地域は「米国・EU・英国・韓国**を除く**」。
> クライアント案件では、**日本・カナダ・インド・オーストラリア**を選ぶのが安心。

### 在庫は数分単位で変わる

A40もH100も、目の前で「出たり消えたり」しました。**タイミングの問題**なので、
気長に構えて大丈夫です。焦って高いカードを掴む必要はありません。

---

## 空きを見つけたら ─ 手順

### STEP 1 ─ Podを立てる

**ポッド → 展開する（Deploy）**

| 項目 | 値 |
|---|---|
| テンプレート | ComfyUI - CUDA 12.8 |
| 地域 | **AP-JP-1** |
| **Network volume** | **`minimax_h3_comfyui_volume`** ← 最重要 |
| GPU | 空いているもの（H100 SXM / H200 SXM） |
| コンテナディスク | 50 GB |

> ⚠️ **ストレージ欄に `150 GB` と `AP-JP-1` が出ているか必ず確認。**
> ここが抜けると、ダウンロードしたものがPod削除で全部消えます。

### STEP 2 ─ ターミナルを開く

1. 左メニュー **「ポッド」**
2. Podが **「Running（実行中）」** になるまで1〜2分待つ
3. **Podの行をクリック**
4. **「接続」** ボタン
5. **「Web ターミナルを開始する」** → **「Web ターミナルに接続」**
6. 黒い画面が新しいタブで開く。`root@xxxx:/#` と出ていれば成功

> 貼り付けは **Ctrl+V**（Macは **Cmd+V**）。効かない時は**右クリック → 貼り付け**。

### STEP 3 ─ コマンドを順番に（1つずつ、終わってから次へ）

#### ① 確認 ─ ここで `150G` が見えるか

```bash
cd /workspace && df -h /workspace && ls -la
```

**`150G` が見えなければ、ここで止めてPodを作り直す。**（ボリュームが繋がっていない）

#### ② 準備（3分）

```bash
cd /workspace
git clone https://github.com/comfyanonymous/ComfyUI
cd /workspace/ComfyUI && pip install -r requirements.txt
pip install -U huggingface_hub
```

#### ③ ダウンローダーを作る（ブロック全体を一度に貼る）

```bash
cat > /workspace/fetch-h3.py <<'PYEOF'
import os, shutil, sys
from huggingface_hub import list_repo_files, hf_hub_download
REPO = "Comfy-Org/MiniMax-H3"
MODELS = "/workspace/ComfyUI/models"
PROFILES = {
 "h100":       ("minimax_h3_fl2va_pruned_bf16.safetensors",         "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
 "a40":        ("minimax_h3_fl2va_pruned_int8_convrot.safetensors", "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
 "a6000":      ("minimax_h3_fl2va_pruned_int8_convrot.safetensors", "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
 "l40s":       ("minimax_h3_fl2va_pruned_fp8_scaled.safetensors",   "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
 "rtxpro4500": ("minimax_h3_fl2va_pruned_fp8_scaled.safetensors",   "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"),
}
VAES = ["minimax_h3_video_vae_fp16.safetensors", "minimax_h3_audio_vae_fp32.safetensors"]
p = os.environ.get("H3_PROFILE", "h100")
if p not in PROFILES: sys.exit(f"H3_PROFILE が不正: {p}")
diff, te = PROFILES[p]
wanted = [("diffusion_models", diff), ("text_encoders", te)] + [("vae", v) for v in VAES]
print(f"構成: {p}\nリポジトリのファイル一覧を取得中...")
files = list_repo_files(REPO)
for sub, name in wanted:
    d = os.path.join(MODELS, sub); os.makedirs(d, exist_ok=True)
    dest = os.path.join(d, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"✅ 取得済み: {sub}/{name}"); continue
    m = [f for f in files if f.rsplit("/",1)[-1] == name]
    if not m:
        print("❌ 見つかりません:", name); print("候補:")
        [print("  ", f) for f in files if f.endswith(".safetensors")]; sys.exit(1)
    print(f"⬇️  {m[0]}")
    shutil.copyfile(hf_hub_download(REPO, m[0]), dest)
    print(f"✅ 配置: {sub}/{name}")
print("\n完了:")
for sub in ("diffusion_models","text_encoders","vae"):
    d = os.path.join(MODELS, sub)
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            print(f"  {sub}/{f}  ({os.path.getsize(os.path.join(d,f))/1e9:.1f} GB)")
PYEOF
echo "できました"
```

#### ④ ダウンロード（放置OK・50GB）

```bash
cd /workspace && H3_PROFILE=h100 python3 fetch-h3.py
```

> ⏸ 途中で止まったら、**同じコマンドをもう一度**。続きから再開する。
> 💡 A40やA6000を掴んだ日は `H3_PROFILE=a40` / `a6000` に変えるだけ。

#### ⑤ 速度2倍（料金半分）

```bash
pip install sageattention
```

#### ⑥ 起動

```bash
cd /workspace/ComfyUI && python3 main.py --listen 0.0.0.0 --port 8188 --use-sage-attention
```

**接続 → ポート8188** で ComfyUI。**Video テンプレート**に MiniMax H3 がある。

> エラーで起動しない時は `--use-sage-attention` を消す。速度が2倍にならないだけで動く。

### STEP 4 ─ 終わったら

1. 生成物を手元にダウンロードして `03-generated-videos/` へ
2. **Terminate（削除）** する ← 停止ではなく削除
3. 手元で `python3 scripts/h3log.py pod end`

**モデルはボリュームに残ります。次回は②〜④が不要になり、2〜3分で生成開始できます。**

---

## 記録（忘れずに）

Pod を立てたら手元のPCで：

```bash
python3 scripts/h3log.py pod start --project H3-Video-Series --gpu "H100 SXM" --rate 3.49
```

終わったら：

```bash
python3 scripts/h3log.py pod end
```

これで実測が貯まり、[[04-買うか借りるか-判断シート]] の判定ができるようになります。

---

## 困ったら

| 症状 | 対処 |
|---|---|
| `150G` が出ない | ボリュームが繋がっていない。Podを作り直す |
| ダウンロードが止まる | 同じコマンドをもう一度。続きから再開 |
| 「❌ 見つかりません」 | 候補一覧が出るので、それを見せてもらえれば直します |
| ターミナルの開き方が分からない | STEP 2 を見る。それでも分からなければ接続画面のスクショを |
| 動画が無音 | `minimax_h3_audio_vae_fp32.safetensors` が無い。④を再実行 |

---

## GPUが空かない日が続いたら

**CPUポッドでダウンロードだけ先に済ませる**手もあります（GPUは1%も使わない作業なので）。
CPUはほぼ常に空いていて、1時間数十円です。

やるときは「CPUに切り替える？」で **続く** を押したあと、
**Network volume と 地域を選び直す**のを忘れずに（切り替えでリセットされます）。

---

## 関連

- [[00-結論とロードマップ]] / [[04-買うか借りるか-判断シート]]
- [[MiniMax-H3-運用ガイド]]
