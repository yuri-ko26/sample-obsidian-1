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
2人は顔(頬)をぎゅっと押し付け合い、接触した部分だけが柔らかく潰れたように変形する。
キャラクターとしての色・シルエットは崩れず、目だけが上向きに開いたアルファベットの
「U」の字のカーブになる。

## 最初のフレーム(Picture 1)
シーン6・7と同じ、パステルカラーの雲(ピンク・ラベンダー・ミントグリーン)が層になった
クローズアップ背景のみ。キャラクターは映っていない。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the scene shown in <Picture 1> establishes a close-up view of layered pastel cloud hills in pink, lavender, and mint green beneath a soft blue-lavender sky, with no characters visible. From the left edge of the frame, the transparent, jelly-like rubber character enters, and from the right edge, the egg-shaped character enters, both moving toward the center of the frame until their faces are close together. The two then press their cheeks firmly against each other; at the exact point of contact, their rounded surfaces compress inward with a soft, gentle squish, flattening slightly against one another, while every identifying detail of each character — their distinct colors, overall silhouette, and the position of their features — stays fully recognizable and intact, with only that small contact area visibly deforming. As they press together, both characters' eyes close into a simple upward-curving line shaped like the letter "U", like the curve of a delighted, scrunched-shut smile, while their outline mouths remain their usual wide, cheerful grins, unaffected by the squish. They hold this cheek-to-cheek squished pose for a moment, cheeks softly bulging outward from the gentle pressure.

overall_soundscape: A soft, muffled squish sound marks the moment the two characters press their cheeks together, followed by light, happy giggles from both of them as they hold the pose.

non_diegetic_music: A short, playful pizzicato phrase with a soft, cushiony descending note landing right as the two faces squish together.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通り、パステルパープルがかった空の下に、ピンク・ラベンダー・ミントグリーンの雲が層になったクローズアップの景色から始まり、キャラクターの姿はまだない。画面左端から透明でゼリーのようなラバーキャラクターが、画面右端から卵形のキャラクターがそれぞれ入ってきて、どちらも画面中央に向かって進み、やがて顔が近づいていく。二人はそのまま頬をぎゅっと押し付け合い、接触したちょうどその部分だけ、丸みのある表面が柔らかく内側へ縮み、互いに軽く押し潰されたように変形する。一方で、それぞれのキャラクターを見分けるための特徴 — はっきりとした色合い、全体のシルエット、パーツの位置関係 — はすべてそのまま保たれ、変形するのはその小さな接触部分だけである。頬を押し付け合う間、二人の目はどちらも、閉じてうっとりした笑顔のようにカーブした、アルファベットの「U」の字の形をした上向きの曲線に変わり、一方で輪郭線だけの口は、この潰れにも影響されず、いつも通りの大きく陽気な笑顔のままである。二人はしばらくの間、頬を押し付け合ったまま潰れたポーズを保ち、圧力でふっくらと頬が外側に膨らんでいる。

**環境音**
二人が頬を押し付け合う瞬間、柔らかくこもった「むにゅっ」という音が鳴り、続いてそのポーズを保ちながら、二人から軽く楽しそうな笑い声が聞こえる。

**BGM(観客のみに聞こえる)**
短く遊び心のあるピチカートのフレーズが、柔らかくクッションのような下降音とともに鳴り、ちょうど二人の顔がぎゅっと押し潰される瞬間に着地する。

## ComfyUIでの設定メモ
- 最初のフレーム画像(シーン6・7と同じ、雲だけのクローズアップ背景、キャラクターなし)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 5秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
