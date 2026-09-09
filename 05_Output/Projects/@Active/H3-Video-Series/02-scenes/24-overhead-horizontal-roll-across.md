---
project: H3-Video-Series
scene: 24
mode: I2VA
duration: 6s
---

# シーン24: 俯瞰で同じ水平方向にコロコロ転がり続けてフレームアウト

## シーン内容
俯瞰の固定カメラ。薄い黄緑色の床の上を、たまちゃんが先に、ぽよんがすぐ後ろに続く形で、
画面左端から転がりながらすでにフレームインしてきた直後の瞬間から始まる。2人はそのまま
同じ水平方向(左から右)に転がり続け、画面右端まで転がりきって完全にフレームアウトする。
たまちゃんは転がっている間、短い手を上に上げたままの姿勢。カメラは完全固定。

**設計メモ**: 参照画像に誰も映っていない(真っ白/空の床だけ)状態を最初のフレームにすると、
モデルがキャラクターの見た目を判断する手がかりを失い、意図しないデザインのキャラクターが
生成されるリスクがある。そのため「誰もいない状態」からではなく、「すでに画面の隅に
2人がフレームインしてきた直後」の実画像をPicture 1として使い、そこから先の動きだけを
テキストで描写する構成にしている。I2VA(最初のフレームのみ参照)のため、最後の
フレーム画像は不要。

## 最初のフレーム(Picture 1)
薄い黄緑色の床を真上から見下ろす構図。画面左寄りに、右側(先行)にたまちゃん、
左側(後方)にぽよんが並び、大きな余白が右側に広がっている。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg-shaped character lies flat on the right, both of its short arms raised up the whole time, and physically rotates around its own horizontal axis like a rolling log — it does NOT stay face-up while sliding sideways; instead, the side of its body facing the camera keeps changing as it turns, its face pointing straight up toward the camera for only a moment before rotating away out of view and its back or side facing up instead, then rotating back around to face the camera again, this cycle of facing up / rotating away / facing up again repeating continuously with every full turn as it advances. Beside it on the left, the transparent, jelly-like rubber character rotates the same way, like a ball physically tumbling end over end, its face likewise rotating into view and out of view again with each full turn rather than remaining fixed facing the camera. Both roll together at a matched pace straight across the frame until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。卵形のキャラクターは右側で寝そべったまま、両手をずっと上に上げた状態で、自分の水平な軸を中心に丸太のように**物理的に回転する**——**顔が常に上を向いたまま横に滑るように移動するのではなく**、回転するにつれて体のどの面がカメラ側を向くかが変わり続け、顔が真上(カメラ側)を向くのは一瞬だけで、そこから回転して顔が見えなくなり背中や横腹が上を向き、その後また回転して顔が戻ってくる、という「顔が見える→見えなくなる→また見える」のサイクルを、前進しながら一回転ごとに繰り返す。その左隣では、透明でゼリーのようなラバーキャラクターも同じように、ボールが端から端まで転がるように物理的に回転し、顔も同様に一回転ごとに見えたり見えなくなったりを繰り返し、常にカメラの方を向いたまま固定されることはない。二人はペースを合わせたまま画面をまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

## ComfyUIでの設定メモ
- 最初のフレーム画像(2人がすでに左寄りにフレームインしている俯瞰構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒(プロンプト内の秒数表記と要一致)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
