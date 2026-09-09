---
project: H3-Video-Series-v2
cut: D-1-alt2
mode: I2VA
status: draft
---

# カットD-1-alt2: ぽよんは弾んで移動、たまちゃんは蹴伸びで移動する推奨パターン

## シーン内容
D-1系のもう一つのバージョン。回転させようとして何度も不自然になった経緯を踏まえ、
**両方とも「回転」をやめ、それぞれすでに実績のある動き方**にした組み合わせ。

- **ぽよん**: 水風船のような柔らかいバウンス(C-1・C-3bで実績あり)で弾みながら移動
- **たまちゃん**: 蹴伸びスタイル(D-1-altで実績あり)で、地面を蹴っては滑る、を繰り返して移動

俯瞰固定カメラ、画面右から左へ移動(Picture 1に合わせて方向は調整可能)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま蹴る
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない

## 参照画像
- Picture 1(最初のフレーム): 俯瞰、薄い黄緑色の床。2人がすでにフレームインしている実画像

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The transparent, jelly-like rubber character moves by bouncing steadily leftward, each bounce like a soft water balloon compressing gently downward and springing back up, carrying it further left with every bounce, staying perfectly round and smooth with no flattening or distortion at any point. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift inside with each bounce without ever spilling out. Beside it, the egg-shaped character moves in a completely different way: it does not spin, tumble, or bounce at all. Instead, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth glide leftward across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater. After each glide slows, it plants its legs again for another quick kick-off, sending it gliding forward once more, repeating this kick-and-glide rhythm the whole way. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Both characters continue moving together at a matched overall pace across the frame, moving steadily leftward, until they fully exit past the left edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。透明でゼリーのようなラバーキャラクターは、水風船のように体がやわらかく沈んでは弾んで戻る動きを繰り返しながら、一定のペースで左方向へ弾んで移動していく——一回弾むごとにさらに左へ進み、常に完全に丸く滑らかな形を保ち、平らになったり歪んだりすることは一切ない。中のガムボールと紙吹雪は弾むたびに揺れ動くがこぼれることはない。その隣では、卵形のキャラクターがまったく異なる動き方をする——回転も転がりも弾みもしない。代わりに、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を左方向へ床の上でスーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じである。その滑りが緩やかになるたびに、再び脚をついてもう一度素早く蹴り出し、また前へ滑っていく、というキック&グライドのリズムを最後まで繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。2人ともこのまま全体としてペースを合わせながら左方向へ一定して進んでいき、完全に左端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt2_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: D-1と同じ画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 方向が逆(右へ進む)の場合は、プロンプト内の"leftward"/"left edge"を"rightward"/"right edge"に置き換えてください
