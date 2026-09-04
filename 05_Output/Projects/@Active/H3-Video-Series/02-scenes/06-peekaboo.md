---
project: H3-Video-Series
scene: 6
mode: I2VA
duration: 4s
---

# シーン6: いないいないばあ

## シーン内容
最初のフレームには背景の雲だけが映っており、キャラクターは映っていない。
そこにぽよんが画面左端から、たまちゃんが画面右端から、それぞれフレームインしてくる。
お互い体はあまり動かさず、目だけを動かして相手の顔を確認し合う「見つけた!」の瞬間。
その瞬間、二人とも例外的に立体的な「驚き口」になる。

## 最初のフレーム(Picture 1)
パステルカラーの雲(ピンク・ラベンダー・ミントグリーン)が層になったクローズアップ背景のみ。
キャラクターは映っていない。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the scene shown in <Picture 1> establishes a close-up view of layered pastel cloud hills in pink, lavender, and mint green beneath a soft blue-lavender sky, with no characters visible. From the left edge of the frame, the transparent, jelly-like rubber character peeks in, just enough of its glossy rounded body entering to reveal its face, its wide round eyes darting toward the right side of the frame. At the same moment, from the right edge, the egg-shaped character peeks in as well, its white-and-pink shell just visible, its own eyes darting toward the left to meet the transparent character's gaze. The two spot each other using only a quick shift of their eyes, without turning or moving their bodies further into frame, and in that instant of recognition both characters' mouths pop open into the same small, rounded, startled "oh" shape, showing a hint of soft pink color inside as an exception to their usual flat outline mouths, their round cheeks lightly flushed, as if caught in a peekaboo game.

overall_soundscape: A soft, playful rustle marks each character peeking in from its side, followed by a light, surprised "oh" gasp from each of them at the same instant their eyes meet.

non_diegetic_music: A short, bright glissando on a music box or xylophone, landing on a cheerful, surprised chord right as the two spot each other.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通り、パステルパープルがかった空の下に、ピンク・ラベンダー・ミントグリーンの雲が層になったクローズアップの景色から始まり、キャラクターの姿はまだない。画面左端から、透明でゼリーのようなラバーキャラクターが、光沢のある丸い体をちょうど顔が見える分だけ覗かせながらフレームインし、その丸く見開いた目は画面右側へ向かって動く。同じ瞬間、画面右端からは卵形のキャラクターも同じように顔を覗かせ、白とピンクの殻がちらりと見え、その目も左側へ向かって動き、透明なキャラクターの視線と合う。二人は体をそれ以上フレームの中へ動かすことなく、目だけをすっと動かして互いの姿を見つけ合う。その気づきの瞬間、二人とも口が同時に、いつもの平らな輪郭線だけの口とは例外的に、小さく丸い驚いた「お」の形にぱっと開き、内側にほんのりピンク色が覗く。頬もほんのり赤らみ、まるでいないいないばあで見つかったかのような表情になる。

**環境音**
それぞれのキャラクターが自分の側からひょこっと顔を覗かせる瞬間、やわらかく軽い衣擦れのような音がし、二人の目が合うのと同時に、双方から小さく驚いた「あっ」という短い息の音が重なる。

**BGM(観客のみに聞こえる)**
オルゴールまたはシロフォンによる短く明るいグリッサンドが、二人が互いを見つけたちょうどその瞬間、陽気で驚きを感じさせる和音に着地する。

## ComfyUIでの設定メモ
- 最初のフレーム画像(雲だけのクローズアップ背景、キャラクターなし)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 4秒(短いいないいないばあのビートなので、プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
