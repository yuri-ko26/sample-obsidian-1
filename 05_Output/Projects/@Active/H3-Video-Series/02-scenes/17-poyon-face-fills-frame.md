---
project: H3-Video-Series
scene: title-card-v5
mode: FL2VA
duration: 3s
---

# タイトルカード用パーツ:降りてきたぽよんに画面いっぱいまで寄る

## シーン内容
シーン13の続き。頭上からゆっくり下りてきたぽよんに、カメラがゆっくりと寄っていき、
最後はぽよんの透明な体(中のガムボールと紙吹雪)と顔が画面いっぱいを埋め尽くす。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 白背景、下に3体(ひよこ・たまご・とら)が並んで立ち、
  その頭上、画面上端から、中にガムボールと紙吹雪が入った透明なぽよんの下半分が
  下りてきている途中の構図(シーン13の最後のフレームと同じ)
- Picture 2(最後のフレーム): 透明なぽよんの体だけが画面いっぱいに広がったドアップ。
  中の色とりどりのガムボールと紙吹雪が大きく見え、中央に丸い目と輪郭線だけの
  笑顔の口(色はつかない)が見えている構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 3.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, begins in the position and framing established by Picture 1: the transparent, jelly-like rubber character — a limbless, ball-shaped body with no arms or hands — continues its slow, steady descent from the top edge of the frame, its lower half filled with colorful gumballs and confetti visible through its glossy clear surface, lowering down above the three small clay mascot characters standing together on the white background below. As the transparent character keeps descending at the same unhurried pace, the camera pushes in toward it with a slow, steady zoom, the transparent character's rounded body growing larger and larger in frame while the three characters below are gradually pushed out of view past the bottom edge. The camera continues closing in smoothly until the transparent character's glossy body fills the entire frame edge to edge, its interior gumballs and confetti now large and vivid, gently tumbling and shifting against its curved inner surface without ever spilling out. The push-in finally settles on its cheerful clay face at the center of the frame — round dark eyes with soft highlights, rosy cheeks, and a flat, outline-only smiling mouth with no depth and no colored interior — filling the screen completely as shown in Picture 2 at the end of the shot.

overall_soundscape: A very soft, low rubbery creak continues through the descent, with a gentle rattle of the gumballs shifting inside growing slightly louder and closer-sounding as the camera pushes in.

non_diegetic_music: The same slow, gently descending phrase on soft bells or a music box continues and swells warmly as the camera closes in, resolving into a bright, playful little flourish as the face fills the screen.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の3.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。Picture 1で示された構図から始まる — 手足のない、球体だけの体を持つ、透明でゼリーのようなラバーキャラクターが、画面上端から変わらぬ落ち着いたペースでゆっくりと下り続けており、光沢のある透明な表面越しに、下半分に詰まった色とりどりのガムボールと紙吹雪が見えている。その下には、白背景の上に小さなクレイのマスコットキャラクターが3体並んで立っている。透明なキャラクターが同じ落ち着いたペースで下り続ける間、カメラはゆっくりと一定の速さでズームインしてそちらへ寄っていき、透明なキャラクターの丸い体が画面の中でどんどん大きくなる一方、下にいた3体は画面下端の外へ少しずつ押し出されて見えなくなっていく。カメラはそのまま滑らかに寄り続け、ついには透明なキャラクターの光沢のある体が画面の端から端まで完全に埋め尽くすところまで近づく。中の色とりどりのガムボールと紙吹雪は今や大きくはっきりと見え、湾曲した内側の表面に沿ってそっと転がり動くものの、こぼれ出ることは決してない。カメラの寄りは最終的に、画面中央にあるその朗らかなクレイの顔 — ソフトなハイライトの入った丸い黒目、赤らんだ頬、そして奥行きも中の色もない平面的な輪郭線だけの笑顔の口 — に落ち着き、Picture 2で示された通り、画面いっぱいにその顔が広がったところでショットが終わる。

**環境音**
とても柔らかく低いゴムのきしみ音が降下の間ずっと続き、中のガムボールが揺れ動くかすかなカタカタという音は、カメラが寄っていくにつれて少しずつ大きく、近くに聞こえるようになる。

**BGM(観客のみに聞こえる)**
柔らかいベルまたはオルゴールによる、同じゆっくりと下降していくフレーズが続いたまま、カメラが寄っていくにつれて温かく膨らみ、顔が画面いっぱいに広がるところで明るく楽しげな小さなフレーズへと締めくくられる。

## ComfyUIでの設定メモ
- 最初のフレーム画像(シーン13の最後のフレームと同じ、3体の頭上にぽよんが下りてきている途中の構図)を Picture 1、
  最後のフレーム画像(ぽよんの体だけが画面いっぱいに広がったドアップ)を Picture 2 として、
  FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 3秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
