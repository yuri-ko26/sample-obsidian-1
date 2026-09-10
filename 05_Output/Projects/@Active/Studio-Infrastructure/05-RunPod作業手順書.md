---
project: Studio-Infrastructure
type: runbook
status: active
updated: 2026-09-10
tags: [project/studio-infra, ai/tools/runpod]
---

# RunPod 作業手順書(このページを見ながら作業してください)

> **所要時間: 操作30分 + ダウンロード待ち(この間は放置でOK)**
> この作業は**最初の1回だけ**です。2回目以降は2分で制作を始められます。
>
> ⚠️ **正直にお伝えします。** このスクリプトは私の環境にGPUがないため、
> **実際のPod上での実行テストができていません。** 構文と手順の確認は済んでいますが、
> 途中で止まる可能性はあります。**止まっても壊れない・途中から再開できる**作りに
> してあるので、詰まったらエラーメッセージをそのまま貼ってください。すぐ直します。

---

## 全体の流れ

```
STEP 1  Network Volume を作る          … RunPodの画面で。10分
STEP 2  L40S の Pod を立てる            … RunPodの画面で。5分
STEP 3  セットアップを流す(1回だけ)     … コマンド1行。待ち時間あり
STEP 4  ComfyUI を開く                  … 5分
STEP 5  C-2d で品質テスト               … 半日・約300円
────────────────────────────────────
STEP 6  2回目以降の流れ                 ← ここからが本番
```

---

## STEP 1 ─ Network Volume を作る(10分)★これが土台

**いま生成物が消えているのは、これが無いからです。**

1. RunPod → **Storage** → **Network Volumes** → **+ New Network Volume**

2. 設定する項目

   | 項目 | 値 | 理由 |
   |---|---|---|
   | **Datacenter** | **L40S の在庫があるリージョン** | ⚠️ 下の注意を参照 |
   | **Size** | **200GB** | モデル + ComfyUI + 生成物の余裕 |
   | **Name** | `h3-studio` | 分かる名前なら何でも |

   > ⚠️ **いちばん間違えやすいところ:**
   > **Network Volume は、同じデータセンター内の Pod にしか接続できません。**
   > 先に **Pods → Deploy** の画面を開いて、**L40S がどのリージョンにあるか
   > 確認してから**ボリュームを作ってください。
   > 逆の順番でやると、作り直しになります。

3. 料金の確認: **1GBあたり月0.07ドル** → 200GBで **月14ドル(約2,200円)**

   > 💡 この月2,200円が、**「生成物が消える」「毎回42.5GB落とし直す」を
   > まとめて解決します。** いちばん費用対効果の高い出費です。

---

## STEP 2 ─ Pod を立てる(5分)

1. **Pods** → **Deploy**

2. **GPUを選ぶ: L40S (48GB)** ─ $0.86/hr

   > なぜ L40S か:H3は48GBあれば量子化を弱められるので**画質の変化が最小**。
   > しかも RTX 5090 より安い。詳細は [[02-GPU比較とローカルPC構成案]]

3. ⚠️ **Secure Cloud を選ぶ**(Community Cloud にしない)
   → クライアント案件なので。理由は [[03-クライアント情報とライセンス]]

4. ⚠️ **Network Volume の欄で、STEP 1 で作った `h3-studio` を指定する**
   **ここを忘れると、また全部消えます。** いちばん大事な一手です。

5. テンプレートは **PyTorch 系のもの**を選ぶ(CUDA入りなら何でも可)

6. **Container Disk** は 20GB 程度で十分
   (大きいものは全部 `/workspace` = Network Volume に置くので)

7. Deploy → 起動したら **Connect → Web Terminal**(または SSH)を開く

---

## STEP 3 ─ セットアップを流す(1回だけ)

ターミナルで、この2つを順番に実行します。

### ① スクリプトを Pod に取ってくる

**方法A: リポジトリが公開設定の場合**

```bash
cd /workspace
git clone -b claude/youthful-carson-xgv93z \
  https://github.com/yuri-ko26/sample-obsidian-1.git vault
```

> ⚠️ **`-b claude/youthful-carson-xgv93z` を必ず付けてください。**
> スクリプトはこの作業ブランチにあります。付けないと `main` を取ってきてしまい、
> スクリプトが入っていません。
> (このブランチを `main` にマージした後は、`-b` は不要になります)

**方法B: リポジトリが非公開の場合(おそらくこちら)**

上の `git clone` は認証を求められて失敗します。その場合はどちらかで:

- **RunPod の Web ターミナル/ファイルブラウザから、
  `scripts/runpod/setup-h3-comfyui.sh` を直接アップロードする**
  → `/workspace/setup-h3-comfyui.sh` に置いて、そのパスで実行してください

- または GitHub の **Personal Access Token** を使う

```bash
cd /workspace
git clone -b claude/youthful-carson-xgv93z \
  https://<あなたのユーザー名>:<トークン>@github.com/yuri-ko26/sample-obsidian-1.git vault
```

> 💡 **どちらでも詰まったら言ってください。** スクリプトの中身を
> そのままターミナルに貼り付けて作る方法もあります(1コマンドで済みます)。

### ② セットアップを実行する

```bash
bash /workspace/vault/scripts/runpod/setup-h3-comfyui.sh --gpu l40s
```

**何をするか一覧が出て、`[y/N]` と聞かれます。** 内容を見て `y` を押してください。

やること（自動）:
- ComfyUI を `/workspace/ComfyUI` に入れる（← Volume の中なので消えない）
- L40S に最適な形式のモデルを落とす
  - `minimax_h3_fl2va_pruned_fp8_scaled.safetensors`（映像）
  - `qwen3vl_32b_minimax_h3_int8_convrot.safetensors`（テキスト理解）
  - `minimax_h3_video_vae_fp16.safetensors`（映像の書き出し）
  - `minimax_h3_audio_vae_fp32.safetensors`（**音声。これが無いと無音になります**）
- **Sage Attention** を入れる（**生成速度が約2倍**＝料金が半分）

> 💡 **ダウンロード中は放置で大丈夫です。** 数十GBあるので時間がかかります。
> ⚠️ **途中で止まったら、同じコマンドをもう一度実行してください。**
> 落とし終わったファイルは飛ばして、続きから再開します。何度流しても壊れません。

### ③ Ref2VA も使う場合（複数の参照画像・動画・音声を使うモード）

```bash
bash /workspace/vault/scripts/runpod/setup-h3-comfyui.sh --gpu l40s --with-ref2va
```
（方法Bの場合は `/workspace/setup-h3-comfyui.sh` に読み替えてください）

> 今の「であう」は I2VA 中心なので、**最初は無しで大丈夫**です。
> 必要になったら後から足せます（既にあるものは飛ばします）。

---

## STEP 4 ─ ComfyUI を開く(5分)

```bash
bash /workspace/start-comfyui.sh
```

RunPod の **Connect** から **ポート 8188** を開くと ComfyUI が表示されます。

1. 上部メニューの **Video** テンプレートを開く
2. **MiniMax H3** のワークフロー（Image-to-Video など）を選ぶ
3. モデル選択欄に、STEP 3 で落としたファイルが出ていることを確認する

> ⚠️ **ComfyUI は v0.30.0 以降が必要**です（H3の公式対応がこのバージョンから）。
> 古いと H3 のテンプレートが出てきません。スクリプトが最新版を入れるので通常は大丈夫です。

> ⚠️ **Sage Attention でエラーが出て起動しない場合**は、
> `/workspace/start-comfyui.sh` の末尾の `--use-sage-attention` を消してください。
> 速度が2倍にならないだけで、H3自体は問題なく動きます。

---

## STEP 5 ─ C-2d で品質テスト(半日・約300円)

**買うか借りるかの決断は、ここで決まります。** → [[04-買うか借りるか-判断シート]]

1. 記録を開始する（別のターミナル、または手元のPCで）

```bash
python3 scripts/h3log.py pod start --project H3-Video-Series --gpu "L40S" --rate 0.86
```

2. `02-scenes-v2/C2d-tamachan-running-start-bump.md` の **v1のプロンプトをそのまま**、
   **同じ参照画像・同じ設定**で生成する

3. `03-generated-videos/C2d_v1.mp4`（H100版）と**並べて見比べる**

### 判定チェックリスト

- [ ] たまちゃんに**眉毛が生えていない** ←【崩れたら即・不合格】
- [ ] たまちゃんの笑い顔で目が三日月、口にコーラルピンクが見える
- [ ] ぽよんの口が**顔の横幅の1/3を超えて開いていない** ←【崩れたら即・不合格】
- [ ] ぽよんの口が輪郭線のみ・無着色で、ガムボールが透けている
- [ ] 接触時にぽよんが丸みを保っている（平らになっていない）
- [ ] ガムボール・紙吹雪がこぼれていない
- [ ] 全体の色味・質感が H100版と比べて劣化していない

**7項目中6つ以上OK → 合格。以後はL40Sで運用します。**

4. 結果を記録する

```bash
python3 scripts/h3log.py gen add \
  --project H3-Video-Series --cut C-2d --version "L40S検証" \
  --mode I2VA --quant fp8 --compute-s 200 \
  --video C2d_L40S.mp4 --verdict OK \
  --note "H100版と比較。眉毛なし・口の開きOK・ガムボール保持OK"

python3 scripts/h3log.py pod end
```

---

## STEP 6 ─ 2回目以降の流れ ★ここからが本番

**セットアップはもう二度とやりません。** 毎回これだけです。

### 制作を始めるとき

1. RunPod で Pod を立てる（**必ず `h3-studio` ボリュームを接続**）
2. ターミナルで:

```bash
bash /workspace/start-comfyui.sh
```

3. 手元で記録を開始:

```bash
python3 scripts/h3log.py pod start --project H3-Video-Series --gpu "L40S" --rate 0.86
```

**約2分で作業開始できます。**（以前は30分かかっていたところです）

### 生成している間のルール

- **書き溜めておいたプロンプトを、上から淡々と生成するだけ**
- **見返さない。悩まない。直さない。** ← それは停めてからやる作業です
- 生成物は `/workspace/ComfyUI/output/` に残ります（**もう消えません**）

### 終わるとき

1. 生成物を手元にダウンロードして `03-generated-videos/` に保存
2. **Pod を停止（Terminate）する**
3. 手元で:

```bash
python3 scripts/h3log.py pod end
```

4. そのあと Obsidian で落ち着いて見返し、次の版を書く ← **ここは無料**

> 💡 **`pod end` を忘れると次に `pod start` できません。** 停め忘れ防止の仕掛けです。
> 💡 Pod を止めても、Network Volume（月2,200円）だけは残ります。それでいいです。

---

## 困ったとき

| 症状 | 対処 |
|---|---|
| `/workspace がありません` と出る | Network Volume が Pod に接続されていません。Pod を作り直してください |
| ダウンロードが途中で止まる | **同じコマンドをもう一度実行**。続きから再開します |
| `No space left on device` | ボリュームの容量不足。RunPod でサイズを増やすか、`--with-ref2va` を外す |
| ComfyUI に H3 のテンプレートが無い | ComfyUI が v0.30.0 未満。`git -C /workspace/ComfyUI pull` で更新 |
| 起動時に Sage Attention のエラー | `/workspace/start-comfyui.sh` の `--use-sage-attention` を消す |
| 生成した動画が無音 | `minimax_h3_audio_vae_fp32.safetensors` が入っていません。セットアップを再実行 |
| VRAM不足（Out of memory）で落ちる | 解像度か尺を下げる。それでもダメなら L40S → H100 PCIe を試す |
| 顔が崩れる | GPUではなくプロンプト側の可能性。[[MiniMax-H3-運用ガイド]] の「崩れたときの立て直し方」へ |

**上のどれでも直らないときは、エラーメッセージをそのまま貼ってください。**

---

## 今日のゴール

- [ ] STEP 1: Network Volume（200GB）を作った
- [ ] STEP 2: L40S + Secure Cloud + ボリューム接続で Pod を立てた
- [ ] STEP 3: セットアップが完了した
- [ ] STEP 4: ComfyUI で H3 のテンプレートが開けた
- [ ] STEP 5: C-2d を作り比べて、判定した

**ここまで終われば、月12.7万円ペースは止まっています。**

---

## 関連

- [[00-結論とロードマップ]] ─ 全体像
- [[01-いますぐやるRunPodコスト削減]] ─ なぜこれをやるのか
- [[04-買うか借りるか-判断シート]] ─ STEP 5 の結果をどう使うか
- [[MiniMax-H3-運用ガイド]] ─ プロンプトと運用のノウハウ
