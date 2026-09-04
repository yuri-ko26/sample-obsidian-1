---
project: H3-Video-Series
scene: title-card-v4
mode: FL2VA
duration: 4s
---

# タイトルカード用パーツ:ぽよんが頭上からゆっくりフレームイン

## シーン内容
白背景に並んで立つ3体のキャラクター(ひよこ・たまご・とら)の頭の真上から、
透明のぽよんがゆっくりと下りてきてフレームインする。カメラは完全固定。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 白背景に、ひよこ・たまご・とらの3体だけが、上に余白のある
  全身の構図で並んで立っている(ぽよんはまだ映っていない)
- Picture 2(最後のフレーム): 同じ3体(全身)の上方、画面上端から、中にガムボールと紙吹雪が
  入った透明なぽよんの下半分が、頭上に下りてきている途中の構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, begins in the position and framing established by Picture 1: the three clay mascot characters — a yellow chick on the left, a white-and-pink egg character in the center, and a yellow tiger cub on the right — stand side by side on a plain white studio background, holding their smiling poses exactly as shown. The camera holds a completely static shot throughout, never panning, tilting, or zooming. From the top edge of the frame, directly above the three characters' heads, the transparent, jelly-like rubber character slowly descends into frame, its glossy rounded body gradually lowering into view from above at an unhurried, gentle pace. The colorful gumballs and confetti inside it remain visible through its clear surface, drifting and shifting gently as it descends without ever spilling out. It continues its slow, steady descent until it reaches the exact position, size, and framing established by Picture 2 at the end of the shot, hovering just above the three characters' heads, while the three characters below remain in their same poses, seemingly unaware of it approaching from above.

overall_soundscape: A very soft, low rubbery creak accompanies the slow descent, along with a faint, gentle rattle of the gumballs shifting inside.

non_diegetic_music: A slow, gently descending phrase on soft bells or a music box, mysterious yet playful, matching the unhurried pace of the descent.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。Picture 1で示された構図から始まる — 左に黄色いひよこ、中央に白とピンクのたまごキャラクター、右に黄色いとらの子が、真っ白なスタジオ背景に並んで立ち、示された通りの笑顔のポーズのままである。カメラは終始完全に固定され、パン・チルト・ズームは一切行わない。画面上端、3体の頭のちょうど真上から、透明でゼリーのようなラバーキャラクターがゆっくりとフレームに入ってきて、その光沢のある丸い体が、急がず穏やかなペースで少しずつ上から降りてくる。中の色とりどりのガムボールと紙吹雪は透明な表面を通してずっと見えたままで、降りてくる間そっと揺れ動くもののこぼれ出ることは決してない。そのままゆっくりと一定のペースで降り続け、Picture 2で示された通りの位置・大きさ・構図に達したところでショットが終わり、3体の頭のすぐ上に浮かんだ状態になる。一方、下にいる3体は同じポーズのまま、上から近づいてくるものにまだ気づいていない様子である。

**環境音**
ゆっくりとした降下に合わせて、とても柔らかく低いゴムのきしみ音がかすかに聞こえ、それに合わせて中のガムボールが軽く揺れる、かすかで穏やかなカタカタという音も混ざる。

**BGM(観客のみに聞こえる)**
柔らかいベルまたはオルゴールによる、ゆっくりと下降していくフレーズが、神秘的でありながらどこか楽しげに、降下のゆったりとしたペースに合わせて流れる。

## ComfyUIでの設定メモ
- 最初のフレーム画像(3キャラクターのみ、ぽよんなし)を Picture 1、最後のフレーム画像
  (ぽよんが頭上に下りてきている途中の構図)を Picture 2 として、FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 4秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
