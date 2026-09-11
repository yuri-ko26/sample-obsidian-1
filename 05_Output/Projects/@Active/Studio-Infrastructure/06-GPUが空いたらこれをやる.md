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

## いまの状態（2026-09-11 更新）

| | |
|---|---|
| ✅ Network Volume | `minimax_h3_comfyui_volume` / AP-JP-1 / 月$10.50 |
| ⚠️ **必ず確認** | デプロイ時に **`150 GB`** と表示されているか(下記①参照) |
| ✅ 取得済み | VAE 2つ(5.5GB)、Turbo LoRA(1.9GB) |
| ⏳ 未取得 | テキストエンコーダ・拡散モデル(**計約37GB**) |
| ⏳ GPU | 在庫待ち |

**残りは2ファイルのダウンロードだけ。約20分で完了します。**

---

## 今日わかった大事なこと(ここを読めば同じ失敗をしません)

### ① 【最重要】デプロイ時にボリュームが勝手に新規作成されることがある

9/10の作業では、`minimax_h3_comfyui_volume`(150GB)を選んだつもりが、
**Pod名と同じ `fixed_ivory_gopher_volume`(50GB)が新しく作られて接続**されていました。
そのため48GBで `Disk quota exceeded` になり、原因究明に何時間もかかりました。

**デプロイ画面のストレージ欄で、必ず `150 GB` と目で確認すること。**
`50 GB` や見慣れない名前が出ていたら、**選び直してからデプロイ**する。

Podの中からは、これで確認できます:

```bash
df -h /workspace; du -sh /workspace
```

### ② `hf download` は使えない。**curl を使う**

`hf download` は Xet という「チャンク分割して組み立て直す」方式で、
RunPodのストレージと相性が悪く **`File reconstruction error`** で失敗します。
**curl で直接落とせば問題なく通ります。**

### ③ 使うモデルの組み合わせ

**150GBのボリュームを正しく接続できていれば、容量の制約はありません。**
画質を妥協する必要はないので、H100では下記の推奨構成を使うこと。

| 用途 | ファイル | サイズ |
|---|---|---|
| **拡散モデル** | `diffusion_models/minimax_h3_fl2va_pruned_fp8_scaled` | 20.96GB |
| **テキストエンコーダ** | `text_encoders/qwen3vl_32b_minimax_h3_int8_convrot` | 25.2GB |
| 映像VAE | `vae/minimax_h3_video_vae_fp16` | 5.21GB |
| 音声VAE | `vae/minimax_h3_audio_vae_fp32` | 0.61GB |
| Turbo LoRA | `loras/minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16` | 1.96GB |
| | **合計** | **約54GB**(150GBなら余裕) |

> 💡 **H100はFP8をネイティブ対応**しているので、拡散モデルの `fp8_scaled` は
> bf16より**速く、サイズは約半分**。H100では最も効率の良い選択。
> 画質を最優先するなら `pruned_bf16` も選べる(150GBなら入る)。

**参考: 50GBしか使えない場合の縮小構成**(約45GB)
エンコーダを `qwen3vl_32b_minimax_h3_nvfp4_awq`(15.69GB)に差し替える。
ただしNVFP4はBlackwell世代以外では速度の利点がなく、圧縮も強い。

### ④ 🔥 Turbo LoRA がある

`loras/minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors`(取得済み)
**4ステップで生成できるLoRA**です。通常は20〜50ステップ必要なので、
**生成時間を大幅に短縮できる可能性があります。** 画質と引き換えなので、
`C-2d` で通常版と比較してから採用を決めること。

### ⑤ その他、後日試す価値があるもの

- `embeddings/` に**演出プリセット10種**(bullet_time / spiral_ascent / storm_magic など)
- `model_patches/` に **ControlNet**(キャラクターの一貫性に効く可能性)

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

> ⚠️ **ストレージ欄に `minimax_h3_comfyui_volume` と `150 GB` が出ているか必ず確認。**
> 9/10は、ここでPod名と同じ**50GBのボリュームが勝手に作られて**いたため、
> 48GBで容量不足になりました。**名前とサイズを目で見て確認すること。**

### STEP 2 ─ ターミナルを開く

1. 左メニュー **「ポッド」**
2. Podが **「Running（実行中）」** になるまで1〜2分待つ
3. **Podの行をクリック**
4. **「接続」** ボタン
5. **「Web ターミナルを開始する」** → **「Web ターミナルに接続」**
6. 黒い画面が新しいタブで開く。`root@xxxx:/#` と出ていれば成功

> 貼り付けは **Ctrl+V**（Macは **Cmd+V**）。効かない時は**右クリック → 貼り付け**。

### STEP 3 ─ コマンドを順番に(1つずつ、終わってから次へ)

> ⚠️ **長い文章の貼り付けは途中で切れます。** 下のコマンドは全部短くしてあります。
> 1行ずつコピーして貼ってください。

#### ① 確認

```bash
cd /workspace && df -h /workspace && ls -la && du -sh /workspace
```

`ap-jp-1.runpod.net` が見えればボリュームは繋がっています
(`150G` ではなく `559T` と出ますが、それが正常です)。

#### ② ComfyUIと必要なもの(初回のみ・既にあれば飛ばす)

```bash
cd /workspace && git clone https://github.com/comfyanonymous/ComfyUI
```

```bash
cd /workspace/ComfyUI && pip install -r requirements.txt
```

#### ③ テキストエンコーダ(15.69GB)

```bash
cd /workspace/ComfyUI/models/text_encoders
```
```bash
F=qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
```
```bash
U=https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/$F
```
```bash
nohup curl -L -C - -o $F "$U" > /workspace/c1.log 2>&1 &
```

#### ④ 拡散モデル(20.96GB)

```bash
cd /workspace/ComfyUI/models/diffusion_models
```
```bash
F=minimax_h3_fl2va_pruned_fp8_scaled.safetensors
```
```bash
U=https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/$F
```
```bash
nohup curl -L -C - -o $F "$U" > /workspace/c2.log 2>&1 &
```

> 💡 `nohup` なので**ターミナルが切れても続きます**。
> 💡 `-C -` なので**途中で止まっても同じ4行で続きから再開**します。
> 💡 2つ同時に走らせて問題ありません(curlなら大丈夫です)。

#### ⑤ 進捗確認

```bash
ls -lh /workspace/ComfyUI/models/text_encoders /workspace/ComfyUI/models/diffusion_models; du -sh /workspace
```

**合計45GB前後**で止まれば完成です。

#### ⑥ 速度2倍

```bash
pip install sageattention
```

#### ⑦ 起動

```bash
cd /workspace/ComfyUI && python3 main.py --listen 0.0.0.0 --port 8188 --use-sage-attention
```

**接続 → ポート8188** で ComfyUI。**Video テンプレート**に MiniMax H3 がある。

> ⚠️ `Address already in use` → `--port 8189` に変更
> ⚠️ Sage Attentionでエラー → `--use-sage-attention` を消す(動きます)

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
| **画面が真っ暗になった** | Webターミナルが切れただけ。**処理は壊れていません**。開き直す |
| **貼り付けが途中で切れる** | 長文は切れます。**1行ずつ**貼る。上のコマンドは全部短くしてあります |
| **`Disk quota exceeded`** | **接続中のボリュームが小さい**。`df -h /workspace` と `du -sh /workspace` で確認し、150GBのものを接続してPodを作り直す |
| **curl が `Exit 23`** | 書き込みエラー＝上と同じ原因 |
| `File reconstruction error` | `hf download` の問題。**curlを使う** |
| ダウンロードが止まる | 同じ4行をもう一度。`-C -` で続きから再開 |
| `ap-jp-1.runpod.net` が出ない | ボリュームが繋がっていない。Podを作り直す |
| 動画が無音 | `minimax_h3_audio_vae_fp32.safetensors` が無い |
| ターミナルが開けない | Podが Running か確認 → 接続 → **Web ターミナルを開始する** → 接続 |

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
