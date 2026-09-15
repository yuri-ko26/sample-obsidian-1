---
project: H3-Video-Series-v2
cut: D-1-alt
mode: I2VA
status: draft
---

# カットD-1-alt: たまちゃんが蹴伸びスタイルで移動するバージョン

## シーン内容
D-1の別バージョン。俯瞰固定カメラ、画面右から左へ移動(または左から右、Picture 1に
合わせて調整)。ぽよんは平行にクルクル回転しながら移動し、**たまちゃんは回転せず、
蹴伸びのように地面を足で蹴っては体をスーッと滑らせ、また蹴っては滑る、を繰り返す**
移動方法にする。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま蹴る
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない

## 参照画像
- Picture 1(最初のフレーム): 俯瞰、薄い黄緑色の床。2人がすでにフレームインしている
  実画像(D-1で使用したものと同じ、または今回いただいた中間フレームの構図を使用)

## プロンプト履歴

### v2 (2026-09-15) — 現在の採用版(ぽよんの顔が回転せず固定されてしまう問題への対策)

生成結果で、ぽよんの体は回転しているのに顔(目・口)だけが同じ位置に張り付いたまま
動かない不具合が判明。顔は輪郭線で描かれた模様ではなく**体の表面に属する一部分**
であり、体の回転と一緒に動く(顔が横を向いたり裏返って見えなくなったりし、
また正面に回ってきたときだけ見える)ことを明記した。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The transparent, jelly-like rubber character spins steadily in place like a flat disc turning on the floor while gliding sideways at the same time. Critically, its face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it, exactly like the rest of its glossy skin. As the body spins, the face spins together with it as one single rigid piece: the face turns away and becomes hidden from view as that side of the body rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face the camera — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift inside without ever spilling out. Beside it, the egg-shaped character moves in a completely different way: it does not spin or tumble at all. Instead, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth glide across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater. After each glide slows, it plants its legs again for another quick kick-off, sending it gliding forward once more, repeating this kick-and-glide rhythm the whole way. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Both characters continue moving together at a matched overall pace across the frame until they fully exit past the edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。透明でゼリーのようなラバーキャラクターは、床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に横方向へ滑るように移動していく。**極めて重要な点として、その顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、光沢のある体の他の部分とまったく同じように、体の一箇所に恒久的に付着している。体が回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分の体がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周してカメラの方を向いたときにだけ再び顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。**中のガムボールと紙吹雪——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色や余分なガムボールは一切現れない)——は揺れ動くがこぼれることはない。その隣では、卵形のキャラクターがまったく異なる動き方をする——回転したり転がったりすることは一切ない。代わりに、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を床の上でスーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じである。その滑りが緩やかになるたびに、再び脚をついてもう一度素早く蹴り出し、また前へ滑っていく、というキック&グライドのリズムを最後まで繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。2人ともこのまま全体としてペースを合わせながら画面を横切り、完全に端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 「ぽよんの顔が体と一緒に回転せず、同じ位置に張り付いてしまう」不具合への
  対策版。顔は体表面に属する固定パーツであり、体の回転と一体で動く(見えなく
  なったり再び見えたりする)ことを明記

### v1 (2026-09-09) — 旧版(ぽよんの顔が回転せず固定されてしまった)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The transparent, jelly-like rubber character spins steadily in place like a flat disc turning on the floor while gliding sideways at the same time, its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shifting inside without ever spilling out. Beside it, the egg-shaped character moves in a completely different way: it does not spin or tumble at all. Instead, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth glide across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater. After each glide slows, it plants its legs again for another quick kick-off, sending it gliding forward once more, repeating this kick-and-glide rhythm the whole way. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Both characters continue moving together at a matched overall pace across the frame until they fully exit past the edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。透明でゼリーのようなラバーキャラクターは、床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に横方向へ滑るように移動していく。中のガムボールと紙吹雪は揺れ動くがこぼれることはない。その隣では、卵形のキャラクターがまったく異なる動き方をする——回転したり転がったりすることは一切ない。代わりに、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を床の上でスーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じである。その滑りが緩やかになるたびに、再び脚をついてもう一度素早く蹴り出し、また前へ滑っていく、というキック&グライドのリズムを最後まで繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。2人ともこのまま全体としてペースを合わせながら画面を横切り、完全に端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: D-1と同じ画像、または今回いただいた中間フレームの構図
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 方向(左→右 or 右→左)はPicture1の実際の構図に合わせて、プロンプト内の左右表現を調整すること
