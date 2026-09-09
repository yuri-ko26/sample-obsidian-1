---
project: H3-Video-Series-v2
cut: D-1-alt3
mode: I2VA
status: draft
---

# カットD-1-alt3: 2人が息を合わせて両足ジャンプで跳ねながら移動する3つ目のパターン

## シーン内容
D-1系の3つ目のバリエーション。「回転(コロコロ)」「蹴伸び」に続く3つ目の選択肢として、
**2人が同じリズムで、揃ってぴょんぴょん跳ねながら移動する**パターン。回転も歩行も
使わないため、これまで問題になっていた回転の不自然さ・足首の破綻リスクを避けられる。

- **ぽよん**: 水風船のような柔らかいバウンス(実績あり)
- **たまちゃん**: 両足(短く硬い脚)を揃えて、ぴょん、ぴょん、と跳ねながら進む。
  ジャンプするたびに一瞬つま先立ちで着地し、また跳ぶ、を繰り返す(踵は一切つかない)

2人のジャンプのタイミングを合わせることで、「一緒に楽しく移動している」感じを
演出する。俯瞰固定カメラ、画面右から左へ移動(Picture 1に合わせて方向は調整可能)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま跳ぶ
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない

## 参照画像
- Picture 1(最初のフレーム): 俯瞰、薄い黄緑色の床。2人がすでにフレームインしている実画像

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Both characters move together in a happy, matched rhythm of little hops, bouncing in sync with each other the whole way. The transparent, jelly-like rubber character bounces steadily leftward, each bounce like a soft water balloon compressing gently downward and springing back up, staying perfectly round and smooth with no flattening or distortion at any point, its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shifting with each bounce without ever spilling out. Beside it, the egg-shaped character hops leftward at the exact same rhythm, pushing off with both of its short, stiff legs together at once and landing briefly on its rounded toe tips before pushing off again for the next hop — its legs never bending at the ankle and its heels never once touching the ground. Neither character spins, tumbles, or slides between hops; each hop is a clean little jump landing back on its toes. The two move side by side at this same synchronized, playful hopping pace, advancing steadily leftward across the frame until they fully exit past the left edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。2人は楽しそうに、息の合った小さな跳ねのリズムで一緒に移動し、最後まで互いに息を合わせて弾む。透明でゼリーのようなラバーキャラクターは、水風船のように体がやわらかく沈んでは弾んで戻る動きを繰り返しながら、一定のペースで左方向へ弾んでいき、常に完全に丸く滑らかな形を保ち、平らになったり歪んだりすることは一切ない。中のガムボールと紙吹雪は弾むたびに揺れ動くがこぼれることはない。その隣では、卵形のキャラクターがまったく同じリズムで左方向へ跳ねていく——短く硬い両脚を同時に地面から蹴り出し、丸まったつま先の先端で一瞬着地してから、また次の跳躍のために蹴り出す——脚は足首で曲がることも、踵が地面につくことも一切ない。どちらのキャラクターも、跳ねている間に回転したり転がったり滑ったりすることは一切なく、それぞれの跳躍はつま先で着地するきれいな小さなジャンプである。2人はこの息の合った楽しい跳ねるペースを保ったまま並んで進み、画面を左方向へ一定して横切り、完全に左端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt3_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: D-1と同じ画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 方向が逆(右へ進む)の場合は、プロンプト内の"leftward"/"left edge"を"rightward"/"right edge"に置き換えてください
