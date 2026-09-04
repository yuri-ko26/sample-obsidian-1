---
project: H3-Video-Series
scene: 7
mode: I2VA
duration: 4s
---

# シーン7: 舌を出してひょこっと下からフレームイン

## シーン内容
シーン6と同様、最初のフレームには背景の雲だけが映っており、キャラクターは映っていない。
そこに、ぽよんとたまちゃんが画面下から舌を出した茶目っ気のある表情でひょこっとフレームインする。

## 最初のフレーム(Picture 1)
シーン6と同じ、パステルカラーの雲(ピンク・ラベンダー・ミントグリーン)が層になった
クローズアップ背景のみ。キャラクターは映っていない。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the scene shown in <Picture 1> establishes a close-up view of layered pastel cloud hills in pink, lavender, and mint green beneath a soft blue-lavender sky, with no characters visible. From the bottom edge of the frame, the transparent, jelly-like rubber character and the egg-shaped character pop up together, peeking upward as if popping over an unseen ledge below the frame. Both wear a playful, mischievous grin with their tongues stuck out: the egg character's small, solid pink tongue pokes out from the corner of its curved smiling mouth, while the transparent character's tongue hangs as a simple looping outline shape, uncolored, matching its usual flat line-work mouth. They settle into frame with a small, bouncy wiggle, their eyes bright and playful, holding the cheeky pose for a moment as if inviting the viewer to play.

overall_soundscape: A light, springy pop sound marks the two characters bouncing up into frame together, followed by a soft, playful giggle from each of them as they hold their tongues-out grins.

non_diegetic_music: A short, bouncy pizzicato flourish with a comedic little slide, landing playfully as the two characters settle into their pose.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通り、パステルパープルがかった空の下に、ピンク・ラベンダー・ミントグリーンの雲が層になったクローズアップの景色から始まり、キャラクターの姿はまだない。画面下端から、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが一緒にひょこっと現れ、画面の外にある見えない縁を乗り越えるかのように上向きに顔を覗かせる。二人ともいたずらっぽく茶目っ気のある笑顔で舌を出している。卵形のキャラクターは、カーブした笑顔の口の端から小さな立体的なピンク色の舌を覗かせ、一方で透明なキャラクターの舌は、いつもの平らな線画の口と同じように、色のついていないループ状の輪郭線としてぶら下がっている。二人は小さく弾むように揺れながら画面の中に収まり、目を輝かせながら、見ている人を遊びに誘うかのように、その茶目っ気のあるポーズをしばらく保つ。

**環境音**
二人が一緒に画面の中へ弾むように現れる瞬間、軽やかで弾力のあるポンという音が鳴り、続いて舌を出したいたずらっぽい笑顔を保ちながら、それぞれから柔らかく楽しそうな笑い声が聞こえる。

**BGM(観客のみに聞こえる)**
短く弾むようなピチカートのフレーズが、コミカルに少し滑るような音の動きとともに鳴り、二人がポーズに収まるところで遊び心のある形で着地する。

## ComfyUIでの設定メモ
- 最初のフレーム画像(シーン6と同じ、雲だけのクローズアップ背景、キャラクターなし)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 4秒(短いポップアップのビートなので、プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
