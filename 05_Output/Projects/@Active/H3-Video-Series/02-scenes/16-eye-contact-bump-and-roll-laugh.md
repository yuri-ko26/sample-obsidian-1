---
project: H3-Video-Series
scene: 16
mode: FL2VA
duration: 5s
---

# シーン16: 目が合って、ぽよんが弾んでたまちゃんにぶつかり、転がって大笑い

## シーン内容
2人が並んで立ち、目を合わせる場面から始まる。ぽよんはその場で2回軽く弾み、
3回目でたまちゃんの体に直接ぶつかる。たまちゃんは倒れ、転がった2人はそのまま
顔を寄せ合うように近づいて大笑いする。カメラは最後、その笑い顔にぐっと寄っていく。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 淡い緑の床、パステルの雲を背景に、左にぽよん、
  右にたまちゃんが並んで立ち、笑顔でこちらを向いている構図
- Picture 2(最後のフレーム): 転がって寄り添った2人の顔のドアップ。たまちゃんは目を
  閉じて大きく口を開けて笑い(口の中はほんのりピンク)、ぽよんも目を見開いて
  大きく口を開けて笑っている(口の中には色がつかない、輪郭線のみ)

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, begins in the position and framing established by Picture 1: the transparent, jelly-like rubber character stands on the left and the egg-shaped character stands on the right, side by side on the pale green floor against soft pastel cloud shapes, both facing the camera with content smiles. The two glance toward each other, their eyes meeting. The transparent character then bounces twice in place with small springy hops, its round body compressing and rebounding each time while its interior gumballs and confetti shift gently without ever spilling out, its flat, outline-only mouth staying pure uncolored line work throughout. On the third bounce, it springs directly sideways into the egg character's body; at the point of contact its rubbery surface presses inward into a smooth, curved dimple rather than flattening, staying round like a yo-yo, and none of its balls or confetti escape. The egg character, its stiff, non-bending limbs unable to absorb the impact, topples over from the force of the bump, and the two end up tumbled close together on the ground, their faces near one another. As they land, both burst into uncontrolled laughter: the egg character's eyes scrunch shut as its mouth opens wide with a hint of soft pink visible inside, while the transparent character's eyes go wide and bright with laughter, its own mouth opening into a wide shape that stays a pure, uncolored outline with no interior color. The camera pushes in with large amplitude as they laugh, closing in tightly on their overjoyed, tumbled-together faces to match the exact framing established by Picture 2 at the end of the shot.

overall_soundscape: A soft rubbery squeak and light gumball rattle mark each of the transparent character's two bounces in place, followed by a slightly bigger bounce sound and a muffled, springy thud as it bumps into the egg character. A soft flump marks the egg character toppling over, and then both characters burst into bright, uncontrollable giggling laughter that continues as the camera closes in.

non_diegetic_music: A playful pizzicato phrase plays through the bounces, with a light comedic accent landing on the bump and topple, before swelling into a warm, joyful flourish as the characters laugh together and the camera pushes in.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の5.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。Picture 1で示された構図から始まる — 透明でゼリーのようなラバーキャラクターが左に、卵形のキャラクターが右に、淡い緑の床の上にパステルの雲を背景にして並んで立ち、どちらもカメラの方を向いて満足そうな笑顔を浮かべている。二人は互いに目を向け合い、視線が合う。透明なキャラクターはその場で軽く2回バウンドし、跳ねるたびに丸い体が縮んでは伸び、中のガムボールと紙吹雪はそっと揺れ動くもののこぼれ出ることはなく、奥行きも色もない平面的な輪郭線だけの口はずっとそのままである。3回目のバウンドで、透明なキャラクターはそのまま横に弾んで卵形のキャラクターの体に直接ぶつかる。接触の瞬間、ラバーの表面は平らに潰れるのではなく、ヨーヨーのように丸みを保ったまま内側へなめらかにくぼみ、中のボールや紙吹雪は一つもこぼれ出ない。卵形のキャラクターは、曲がらない硬い手足では衝撃を受け止めきれず、ぶつかった勢いで倒れ込み、二人は顔を寄せ合うようにして一緒に地面に転がる。倒れ込むと同時に、二人とも抑えきれない笑いがこみ上げてくる — 卵形のキャラクターは目をぎゅっと閉じ、口を大きく開けて笑い、その内側にはほんのりピンク色が覗く一方、透明なキャラクターは目を大きく見開いて笑いに輝かせ、その口も大きく開くが、色のつかない輪郭線だけの形のままである。二人が笑っている間、カメラは大きな振れ幅で寄っていき、転がって寄り添いながら喜びに満ちた二人の顔に、Picture 2で示された通りの構図でぴたりと寄ったところでショットが終わる。

**環境音**
透明なキャラクターがその場で2回バウンドするたびに、柔らかいゴムのきしむ音と軽いガムボールのカタカタという音が響く。続いて、卵形のキャラクターにぶつかる瞬間には、少し大きめの弾む音とこもった弾力のある衝突音が鳴る。卵形のキャラクターが倒れ込む際には柔らかな「ふすん」という音がし、その後、二人とも明るく抑えきれない笑い声を上げ続け、カメラが寄っていく間もその笑い声は続く。

**BGM(観客のみに聞こえる)**
陽気なピチカートのフレーズがバウンドの間流れ、ぶつかって倒れる瞬間に軽いコミカルなアクセントが入り、その後、二人が一緒に笑い合い、カメラが寄っていくにつれて、温かく喜びに満ちたフレーズへと盛り上がっていく。

## ComfyUIでの設定メモ
- 最初のフレーム画像(2人が並んで立つ構図)を Picture 1、最後のフレーム画像(転がって
  大笑いするドアップ)を Picture 2 として、FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 5秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
