---
project: H3-Video-Series-v2
cut: D-2-entrance
mode: FL2VA
status: draft
---

# カットD-2-entrance: 誰もいない床から2人が転がってフレームインする橋渡しカット

## シーン内容
既存の承認済み「左へ転がる」カット(`02-scenes/25-overhead-horizontal-roll-across-reverse.md`
相当)は、すでに2人がフレームインした状態から始まっていたため、フレームインする瞬間の
映像がなかった。**既存の承認済みカットの動き自体には一切手を加えず**、その開始ポーズに
ぴったりつながる短い「フレームインのみ」の橋渡しカットを新規に作る。

編集時は [このカット(D-2-entrance)] → [既存の承認済みカット] の順につなげる。
Picture 2(このカットの終了ポーズ)= 既存カットの開始フレームと同一画像にすることで、
つなぎ目がシームレスになる。

**重要な確認事項**: 既存の承認済みカットで実際に使われているプロンプト文(転がり方の
描写)がアーカイブの`25-overhead-horizontal-roll-across-reverse.md`と異なる場合は、
下記の「転がる動き」の描写をその内容に合わせて修正する必要がある。異なる場合は
教えてください。

## 参照画像
- Picture 1(最初のフレーム): 誰もいない、無地の薄い黄緑色の床のみ(百合子さん提供の
  無地グリーン画像を使用。真上から見下ろす俯瞰構図として使う)
- Picture 2(最後のフレーム): **受領済み・確定**。既存の承認済みカットの開始フレームと
  同一の実画像。薄い黄緑色の床を真上から見下ろす構図、画面右寄りに、左側にぽよん
  (透明な体越しに床が透けて見える、点目+輪郭線の笑顔)、右側にたまちゃん(白/ピンクの
  卵形、点目+輪郭線の笑顔、短い脚)が並んで立ち、左側には広い余白(何もない床)が
  画面の半分以上を占めている

## プロンプト履歴

### v1 (2026-09-09) — 下書き。既存カットの実際のプロンプトと突き合わせ後に確定する

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. From the right edge of the frame, the transparent, jelly-like rubber character and the egg-shaped character roll into view together, already tumbling steadily leftward along the same horizontal line the moment they appear, the transparent character rolling slightly ahead on the left side of the pair and the egg character rolling close behind it on the right side. The egg character rolls with its short stubby arms held raised up above its tumbling body the whole time, its non-bending limbs staying lifted with each turn. The transparent character's interior gumballs and confetti drift and shift inside as it rolls without ever spilling out. Both continue rolling steadily leftward at a matched pace until they reach the position shown in <Picture 2>, near the right portion of the frame with open floor still stretching out to their left, in the exact same static framing as the opening frame, at the end of the shot.

overall_soundscape: A rhythmic sequence of rubbery squeaks and light rattles from the shifting gumballs marks each turn of the transparent character's body, mixed with soft, repeated thuds as the egg character tumbles right behind it.

non_diegetic_music: An upbeat, rolling marimba melody at a cheerful, bouncy tempo, its rhythm mirroring the two characters' matched tumbling pace as they roll into frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り、薄い黄緑色の誰もいない床を真上から見下ろしている。カメラは一切パン・チルト・ズーム・カットをしない。画面右端から、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、現れた瞬間からすでに同じ水平の直線上を左方向へ一定のペースで転がりながらフレームインしてくる——透明なキャラクターがペアのやや左側を先行し、卵形のキャラクターがそのすぐ右側後方を転がる。卵形のキャラクターは、短く曲がらない手を転がっている間ずっと上に上げたまま転がり続ける。透明なキャラクターの中のガムボールと紙吹雪は転がるあいだ揺れ動くが、こぼれることはない。2人はこのままペースを合わせて左方向へ転がり続け、<Picture 2>に示された通りの位置——画面のやや右寄りで、左側にはまだ広い床が残っている状態——に到達したところで、最初のフレームとまったく同じ固定構図のまま、このショットが終わる。

**環境音**
透明なキャラクターが一回転するたびに、やわらかく規則的なゴムのきしみ音と、中でガムボールが軽くカタカタと揺れる音が響き、そのすぐ後ろで卵形のキャラクターが転がるたびの柔らかく繰り返す「ぽすん」という音が混ざる。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、2人がフレームインしてくるペースに合わせて流れる。

**生成結果**
- 動画ファイル: `03-generated-videos/D2-entrance_v1.mp4`
- 判定: NG
- メモ: 「誰もいない床→2人が忽然と現れて転がり出す」ような不自然な出方になった。
  空の床からの登場は、動画生成AIが根本的に苦手な動きだと判明。→ v2で方針転換
  (完全に見えない状態からではなく、画面端で体の一部がすでに見切れている状態から
  スタートする)

### v2 (2026-09-09) — たまちゃん単体版。方針転換:完全に空の床からではなく、
画面端でたまちゃんの体がすでに一部見切れている(かつ傾いた/転がっている途中に
見える)状態をPicture 1にする。ぽよんはこのカットには含めない(別途対応)。
I2VAに変更(明確な終了フレーム画像がまだないため)。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor exactly as shown in <Picture 1>. The egg-shaped character keeps its exact appearance and design from <Picture 1> unchanged throughout, with no distortion. At the very start, only part of its body is visible, cut off by the right edge of the frame, tilted at an angle mid-tumble exactly as shown in <Picture 1>, with most of its form still just off-screen beyond the right edge. The camera never pans, tilts, zooms, or cuts away at any point. The egg character continues rolling in from the right, its body advancing further onto the floor and becoming more and more visible within the frame with each moment, tumbling forward in a steady, even cartwheel motion, its front and back alternating into view with each full turn, its short stubby arms held raised up above its tumbling body the whole time, its non-bending limbs staying lifted with each turn. It stays perfectly level as it tumbles, never tilting off diagonally or wobbling to one side, and it never rises up or stands. By the end of the shot, the greater part of its body is now clearly visible well within the frame, still tumbling steadily leftward, with open floor continuing to stretch out further to its left.

overall_soundscape: A soft, repeated thud marks each turn of the egg character's body as it tumbles further into frame.

non_diegetic_music: An upbeat, rolling marimba melody at a cheerful, bouncy tempo, matching the egg character's steady tumbling pace as it rolls into frame.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。卵形のキャラクターは<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。最初の時点では、<Picture 1>に示された通り、体の一部だけが画面右端で見切れており、転がっている途中のように斜めに傾いた状態で、体の大部分はまだ画面右端の外側にある。カメラは一切パン・チルト・ズーム・カットをしない。卵形のキャラクターは右側からさらに転がり続けて入ってきて、時間が経つにつれて床の上でその姿がだんだんはっきりと見えるようになっていき、まっすぐで均等な前転(でんぐり返し)のような動きで、一回転するごとに正面と背中が交互に見える。短く曲がらない手は転がっている間ずっと上に上げたままで、一回転するたびもその手は上がったままである。転がっている間は常に体が水平・水準を保ったまま転がり、決して斜めに傾いたり片側に揺れたりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。ショットの終わりには、体の大部分が画面内にはっきりと見えるようになっており、なおも左方向へ一定のペースで転がり続けていて、その左側にはまだ床が広がっている。

**環境音**
卵形のキャラクターが転がってフレームインしてくる間、一回転するたびに柔らかく繰り返す「ぽすん」という音が響く。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、卵形のキャラクターがフレームインしてくる一定のペースに合わせて流れる。

**生成結果**
- 動画ファイル: `03-generated-videos/D2-entrance_v2.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 今回いただいた、たまちゃんの体が画面右端で一部見切れている俯瞰画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 3秒目安(短い橋渡しカットのため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 生成後、既存の承認済み「左へ転がる」カットの冒頭とつないでみて、動きの速度・
  キャラクターの位置に違和感がないか確認する
