---
project: H3-Video-Series
scene: 27
mode: I2VA
duration: 6s
---

# シーン27: 俯瞰で水平方向にコロコロ転がり続けてフレームアウト(ぽよんのみバージョン)

## シーン内容
シーン24からたまちゃんを取り除き、ぽよんだけが登場するバージョン。俯瞰の固定カメラ。
薄い黄緑色の床の上を、ぽよんが画面左端からすでに転がりながらフレームインしてきた
直後の瞬間から始まる。そのまま同じ水平方向(左から右)に転がり続け、画面右端まで
転がりきって完全にフレームアウトする。カメラは完全固定。

## 最初のフレーム(Picture 1)
実画像を使用。薄い黄緑色の床を真上から見下ろす構図。画面左寄りにぽよんが1体だけ位置し、
大きな余白が右側に広がっている(たまちゃんは映っていない)。透明でしずく型のボディで、
上部の尖った先端が小さなフック状に見える。中には赤・黄・緑・青のガムボールと紙吹雪が入り、
点目+輪郭線の口でにっこり微笑み、頬に薄いピンクの丸いチークが見える。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. The character keeps its exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The transparent, jelly-like rubber character, a limbless, ball-shaped body with no arms or legs, continuously somersaults forward across the floor in a straight, even cartwheel motion, its front and back alternating into view with each full turn — front, then back, then front again, repeating steadily as it advances — the same way a rolling ball toy tumbles forward end over end. It stays perfectly level as it tumbles, never tilting or wobbling off to one side or spinning diagonally, and it never rises up or stands. Its interior gumballs and confetti drift and shift inside without ever spilling out. It continues tumbling forward at a steady, even pace straight across the frame until it fully exits past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。キャラクターは<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。透明でゼリーのようなラバーキャラクター(手足のない球体)は、まっすぐで均等な前転(でんぐり返し)のような動きで床の上を継続的に前へ転がっていき、一回転するごとに正面と背中が交互に見える——正面、そして背中、そしてまた正面、というのを進みながら規則正しく繰り返す。ちょうど転がるボール型のおもちゃが端から端へ回転しながら進むのと同じ動きである。転がっている間は常に体が水平・水準を保ったまま転がり、決して片側に傾いたり、斜めに揺れたり、斜め回転したりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。中のガムボールと紙吹雪は漂うように揺れ動くが決してこぼれることはない。このまま一定のペースで前転を続けながら画面をまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

## ComfyUIでの設定メモ
- 最初のフレーム画像(ぽよんだけが左寄りにフレームインしている俯瞰構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒(プロンプト内の秒数表記と要一致)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
