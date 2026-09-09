---
project: H3-Video-Series
scene: 8
mode: I2VA
duration: 5s
---

# シーン8: 顔を寄せてぎゅっと潰れ顔(Uの字の目)

## シーン内容
シーン6・7と同様、最初のフレームには背景の雲だけが映っており、キャラクターは映っていない。
ぽよんが画面左端から、たまちゃんが画面右端からフレームインし、画面中央に向かって近づいていく。
ぽよんが柔らかくぐにゃっと歪みながらたまちゃんの顔に近づいて押し当たる。
変形するのはぽよんの体だけで、たまちゃんの硬い殻は一切変形しない。
2人とも目は上向きに開いたアルファベットの「U」の字のカーブになり、口はいつも通りの
輪郭線の笑顔のまま。

## 最初のフレーム(Picture 1)
シーン6・7と同じ、パステルカラーの雲(ピンク・ラベンダー・ミントグリーン)が層になった
クローズアップ背景のみ。キャラクターは映っていない。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the scene shown in <Picture 1> establishes a close-up view of layered pastel cloud hills in pink, lavender, and mint green beneath a soft blue-lavender sky, with no characters visible. From the left edge of the frame, the transparent, jelly-like rubber character enters, and from the right edge, the egg-shaped character enters, both moving toward the center of the frame until their faces are close together. The transparent character then leans in with a soft, gooey squish, its rubbery body warping and compressing as it presses directly against the egg character's cheek; at the point of contact, only the transparent character's glossy surface flattens and deforms against the egg character's face, while the egg character's hard, rigid shell stays completely undented and unchanged, not deforming at all. Even as the transparent character's body warps, every identifying detail of each character — their distinct colors, overall silhouette, and the position of their features — stays fully recognizable and intact. In this moment, both characters share the exact same expression: their eyes close into a simple upward-curving line shaped like the letter "U", like the curve of a delighted, scrunched-shut smile, while their outline mouths remain their usual wide, cheerful grins, unaffected by the squish. They hold this pose for a moment, the transparent character's body still gently warped against the egg character's unmoved, rigid cheek.

overall_soundscape: A soft, muffled squish sound marks the moment the transparent character presses against the egg character's cheek, followed by light, happy giggles from both of them as they hold the pose.

non_diegetic_music: A short, playful pizzicato phrase with a soft, cushiony descending note landing right as the two faces squish together.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通り、パステルパープルがかった空の下に、ピンク・ラベンダー・ミントグリーンの雲が層になったクローズアップの景色から始まり、キャラクターの姿はまだない。画面左端から透明でゼリーのようなラバーキャラクターが、画面右端から卵形のキャラクターがそれぞれ入ってきて、どちらも画面中央に向かって進み、やがて顔が近づいていく。透明なキャラクターは柔らかくぐにゃっと歪みながら身を乗り出し、ゴム製の体が変形・圧縮されながら卵形のキャラクターの頬に直接押し当たる。接触した瞬間、変形するのは透明なキャラクターの光沢のある表面だけで、卵形のキャラクターの側は硬い殻のままへこむことも変形することも一切ない。透明なキャラクターの体が歪んでいる間も、それぞれのキャラクターを見分けるための特徴 — はっきりとした色合い、全体のシルエット、パーツの位置関係 — はすべてそのまま保たれている。この瞬間、二人はまったく同じ表情になる:目はどちらも、閉じてうっとりした笑顔のようにカーブした、アルファベットの「U」の字の形をした上向きの曲線に変わり、輪郭線だけの口は、この潰れにも影響されず、いつも通りの大きく陽気な笑顔のままである。二人はしばらくの間そのポーズを保ち、透明なキャラクターの体は歪んだまま、卵形のキャラクターの動かない硬い頬に押し当たっている。

**環境音**
透明なキャラクターが卵形のキャラクターの頬に押し当たる瞬間、柔らかくこもった「むにゅっ」という音が鳴り、続いてそのポーズを保ちながら、二人から軽く楽しそうな笑い声が聞こえる。

**BGM(観客のみに聞こえる)**
短く遊び心のあるピチカートのフレーズが、柔らかくクッションのような下降音とともに鳴り、ちょうど二人の顔がぎゅっと押し潰される瞬間に着地する。

## ComfyUIでの設定メモ
- 最初のフレーム画像(シーン6・7と同じ、雲だけのクローズアップ背景、キャラクターなし)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 5秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
