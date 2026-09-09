---
project: H3-Video-Series-v2
cut: C-3b
mode: FL2VA
status: draft
---

# カットC-3b: 落ち着いた立ち姿から、ゆっくり並んで歩いてフレームアウトする

## シーン内容
元のC-3を2つに分割した後半部分。C-3aで静止した「理想画質」の立ち姿から始まり、
2人でゆっくりと落ち着いたペースで歩いてフレームアウトする。**走ったり弾んだり
する速い動きは使わず**、あくまでゆっくりとしたよちよち歩きに留めることで、
足首が曲がったりぽよんの形が崩れたりする問題を避ける。正面固定カメラ。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま、ゆっくりよちよち歩く
  (走らない・急がない)
- ぽよんは足がないため、ゆっくりとした穏やかな弾みで移動する(激しく跳ねない)。
  常に丸み(しずく型)を保ち、形が崩れたり潰れたりしない

## 参照画像
- Picture 1(最初のフレーム): 「理想画質」の2ショット画像(薄い黄緑色の床+パステルの
  雲を背景に、左にぽよん、右にたまちゃんが並んで立つ構図。C3aの終了フレームと同一)
- Picture 2(最後のフレーム): 無地の薄い黄緑色の床のみ(誰もいない構図)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>, with the transparent, jelly-like rubber character and the egg-shaped character standing calmly side by side exactly as shown. The camera never pans, tilts, zooms, or cuts away at any point. Both characters keep their exact appearance and design from <Picture 1> unchanged while visible, with no distortion at any point. They turn to look at each other with a happy, contented smile, then begin moving together toward the right edge of the frame at a slow, unhurried, gentle pace — never running or rushing. The egg character toddles forward with small, calm steps, its short stiff legs never bending at the ankle and its heels never touching the ground. The transparent character moves alongside it with a slow, soft, gentle bounce, staying perfectly round and smooth with no flattening or distortion at any point in its motion. Side by side at this same relaxed pace, they continue toward the right edge of the frame until both have completely exited past it, with no part of either character remaining visible, leaving only the empty pale yellow-green floor exactly as shown in <Picture 2>, in the exact same static framing as the opening frame, at the end of the shot.

overall_soundscape: Soft, unhurried footsteps from the egg character mixed with the gentle, quiet squeak of the transparent character's slow bounce, both fading gradually as the two move off toward the edge of frame.

non_diegetic_music: A warm, gentle marimba melody at an easygoing, relaxed tempo, fading out softly as the two characters exit the frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映しており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>の通り落ち着いて並んで立っている状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。2人とも画面に映っている間は<Picture 1>の見た目・デザインのまま、一切歪むことなく保たれる。2人は嬉しそうな、満ち足りた笑顔で互いに顔を見合わせたあと、画面右端に向かって、ゆっくりと急がない穏やかなペースで一緒に進み始める——走ったり急いだりすることは一切ない。卵形のキャラクターは小さく落ち着いた歩幅でよちよちと進み、短く硬い脚は足首で曲がることも、踵が地面につくことも一切ない。透明なキャラクターはそのそばを、ゆっくりとやわらかく穏やかに弾みながら進み、その動きのあいだ、常に完全に丸く滑らかな形を保ち、平らになったり歪んだりすることは一切ない。並んだまま、この落ち着いたペースを保って画面右端へと進んでいき、どちらの体もまったく見えなくなるまで完全に右端の外へ出ていき、<Picture 2>で示された通り、最初のフレームとまったく同じ固定構図のまま、誰もいない薄い黄緑色の床だけが残ったところでこのショットが終わる。

**環境音**
卵形のキャラクターの落ち着いた足音と、透明なキャラクターのゆっくりとした静かな弾む音が混ざり合い、2人が画面端へ向かうにつれて次第に遠ざかっていく。

**BGM(観客のみに聞こえる)**
温かくのんびりとしたテンポのマリンバのメロディが、2人が画面の外へ出ていくと穏やかにフェードアウトする。

**生成結果**
- 動画ファイル: `03-generated-videos/C3b_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 「ゆっくり歩く」ではなく、キャラクターらしい移動方法(ぽよんは弾む、
  たまちゃんはつま先で地面を蹴る)にしてほしいとの指示を受け、v2で修正

### v2 (2026-09-09) — v1からの変更点: 「ゆっくり歩く」から、ぽよんは弾んで退場・
たまちゃんはつま先で地面を蹴って進む、それぞれのキャラクターらしい移動方法に変更

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>, with the transparent, jelly-like rubber character and the egg-shaped character standing calmly side by side exactly as shown. The camera never pans, tilts, zooms, or cuts away at any point. Both characters keep their exact appearance and design from <Picture 1> unchanged while visible, with no distortion at any point. They turn to look at each other with a happy, contented smile, hold that eye contact for a brief beat, and give a small, decisive nod to one another — a silent "let's go!" agreement — then begin moving together toward the right edge of the frame. The transparent character moves by bouncing steadily forward, each bounce like a soft water balloon compressing gently downward and springing back up, carrying it further right with every bounce, staying perfectly round and smooth with no flattening or distortion at any point. The egg character moves alongside it by pushing off the floor with its toes each time, its short stiff legs never bending at the ankle and its heels never once touching the ground — each step is a small kick-off from its rounded toe tips, propelling it forward in the same steady rhythm as the transparent character's bounces. Side by side at this matched pace, they continue toward the right edge of the frame until both have completely exited past it, with no part of either character remaining visible, leaving only the empty pale yellow-green floor exactly as shown in <Picture 2>, in the exact same static framing as the opening frame, at the end of the shot.

overall_soundscape: A steady rhythm of soft, rubbery squeak-bounces from the transparent character, mixed with light, repeated taps from the egg character pushing off the floor with its toes, both fading gradually as the two move off toward the edge of frame.

non_diegetic_music: A warm, bouncy marimba melody keeping a steady, matched rhythm with the two characters' movement, fading out softly as they exit the frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映しており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>の通り落ち着いて並んで立っている状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。2人とも画面に映っている間は<Picture 1>の見た目・デザインのまま、一切歪むことなく保たれる。2人は嬉しそうな、満ち足りた笑顔で互いに顔を見合わせ、その視線を一瞬保ったあと、無言の「よし、行こう!」というように小さくきっぱりとうなずき合う。それから画面右端に向かって一緒に進み始める。透明なキャラクターは、水風船のように体がやわらかく沈んでは弾んで戻る動きを繰り返しながら、一回弾むごとにさらに右へ進んでいき、常に完全に丸く滑らかな形を保ち、平らになったり歪んだりすることは一切ない。卵形のキャラクターはそのそばを、毎回つま先で床を蹴って進む——短く硬い脚は足首で曲がることも、踵が地面につくことも一切なく、丸まったつま先の先端から小さく蹴り出すようにして、透明なキャラクターの弾むリズムと同じ一定のペースで前へ進んでいく。並んだまま、このペースを合わせて画面右端へと進んでいき、どちらの体もまったく見えなくなるまで完全に右端の外へ出ていき、<Picture 2>で示された通り、最初のフレームとまったく同じ固定構図のまま、誰もいない薄い黄緑色の床だけが残ったところでこのショットが終わる。

**環境音**
透明なキャラクターの一定のリズムのやわらかいゴムの弾む音に、卵形のキャラクターがつま先で床を蹴る軽く繰り返す音が混ざり、2人が画面端へ向かうにつれて次第に遠ざかっていく。

**BGM(観客のみに聞こえる)**
温かく弾むようなマリンバのメロディが、2人の動きに合わせた一定のリズムを刻み、画面の外へ出ていくと穏やかにフェードアウトする。

**生成結果**
- 動画ファイル: `03-generated-videos/C3b_v2.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 「理想画質」2ショット画像(C3aの終了フレームと共通)
- Picture 2: 無地の薄い黄緑色画像(床のみ、キャラクターなし)
- モード: FL2VA
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
