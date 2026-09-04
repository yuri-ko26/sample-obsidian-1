---
project: H3-Video-Series
scene: 14
mode: FL2VA
duration: 6s
---

# シーン14: ぽよんのドアップから後ずさりしてたまちゃんに近づく(カメラも引く)

## シーン内容
ぽよんの顔のドアップから始まる。ぽよんはその場で2回軽くバウンドし、
3回目で大きく跳ねながら正面(カメラ側)を向いたまま後ろに下がる。
ぽよんが後ろに下がるのに合わせて、カメラも少しずつ引いていく。
ぽよんは何度か跳ねながら後退を続け、たまちゃんに近づいていき、
最終的に2人が並んで立つ画像2の構図に着地する。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): ぽよんの顔のドアップ画像(点目・輪郭線だけの口、
  中のガムボールと紙吹雪が背景として見える構図)
- Picture 2(最後のフレーム): 淡い緑の床、パステルの雲を背景に、左にぽよん、
  右にたまちゃんが並んで立っている構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, begins in the position and framing established by Picture 1: an extreme close-up on the transparent, jelly-like rubber character's glossy face fills the frame, its round dark eyes and flat, outline-only mouth with no depth or colored interior surrounded by tightly packed colorful gumballs and drifting confetti visible inside its body. The camera holds a fixed static position at first. Still held in this tight close-up, the character bounces twice in place with small springy hops, its body compressing and rebounding each time while its interior gumballs and confetti shift gently without ever spilling out. On the third bounce, it launches into a much bigger hop, this time moving backward away from the camera while facing directly toward the camera the entire time, never turning around. As it begins retreating, the camera starts slowly pulling back as well, gradually widening the frame in sync with the character's backward motion. The transparent character continues bouncing backward several more times, its rubbery body compressing and rebounding with each hop, its contents still shifting but never spilling, gradually closing the distance toward the egg-shaped character, who stands waiting on the pale green floor amid soft pastel cloud shapes. The camera keeps pulling back until it reaches the wide framing established by Picture 2 at the end of the shot, with both characters now standing side by side in the exact pose, spacing, and composition shown in the final frame.

overall_soundscape: A soft rubbery squeak echoes at close range as the transparent character makes two small bounces in place, with the light clatter of gumballs shifting inside it each time. A bigger, springier bounce sound marks the third hop as it begins moving backward, followed by a steady rhythm of softer bounce sounds as it continues retreating toward the egg character, fading slightly as the frame widens.

non_diegetic_music: A playful pizzicato string phrase builds through the close-up bounces, continuing at a steady, bouncy tempo through the retreat, and settling into a gentle, contented resolution as the wide framing is reached.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。Picture 1で示された構図から始まる — 透明でゼリーのようなラバーキャラクターの光沢のある顔が画面いっぱいに映り、丸い黒目と、奥行きも中の色もない平面的な輪郭線だけの口が、体の中にぎっしり詰まったカラフルなガムボールと漂う紙吹雪に囲まれている。カメラは最初、固定された位置を保っている。このドアップのまま、キャラクターはその場で軽く2回、小さくバウンドし、跳ねるたびに体が縮んで伸び、中のガムボールと紙吹雪もそっと揺れ動くが決してこぼれない。3回目のバウンドで、キャラクターはさらに大きく弾み、今度はカメラの方を向いたまま、振り向かずに後ろへ下がっていく。後退が始まると同時に、カメラもゆっくりと引き始め、キャラクターの後退の動きに合わせて画角が少しずつ広がっていく。透明なキャラクターはそのまま何度か後ろへ弾みながら後退を続け、ゴム製の体は跳ねるたびに縮んでは伸び、中身は揺れ動くもののこぼれることはなく、淡い緑の床でパステルの雲を背景に待っている卵形のキャラクターとの距離を少しずつ縮めていく。カメラはそのまま引き続け、ショットの最後にPicture 2で示された通りの広い構図に達し、2人はまさに最終フレームに示された通りのポーズ・間隔・構図で並んで立っている。

**環境音**
透明なキャラクターがその場で2回小さくバウンドするたびに、近い距離でやわらかいゴムのきしみ音が響き、その中でガムボールが軽くカタカタと動く音が混ざる。3回目の跳躍で後ろへ動き始める瞬間には、より大きく弾力のある弾む音が鳴り、その後、卵形のキャラクターへ向かって後退を続ける間、より柔らかい弾む音が一定のリズムで続き、画角が広がるにつれて少しずつ音が和らいでいく。

**BGM(観客のみに聞こえる)**
陽気なピチカート弦楽器のフレーズが、ドアップでのバウンドの間に盛り上がっていき、後退の間も一定の弾むようなテンポで続き、広い構図に達したところで、穏やかで満ち足りたような響きに落ち着く。

## ComfyUIでの設定メモ
- 最初のフレーム画像(ぽよんのドアップ)を Picture 1、最後のフレーム画像(2人が並ぶ構図)を
  Picture 2 として、FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 6秒(プロンプト内の秒数表記と要一致)
- 今回はカメラも一緒に引く点が過去のシーンと異なる(シーン1は正面ドアップ固定→ジャンプで
  一気に広がる構成だったが、今回はぽよんの後退に合わせてカメラも徐々に引いていく)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
