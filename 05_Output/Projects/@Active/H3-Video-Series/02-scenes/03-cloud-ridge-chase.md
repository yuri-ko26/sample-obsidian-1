---
project: H3-Video-Series
scene: 3
mode: I2VA
duration: 8s
---

# シーン3: 雲の稜線での追いかけっこ

## シーン内容
パステルカラーの雲が連なる稜線の上で、ぽよんとたまちゃんが追いかけっこをして遊ぶシーン。
ぽよんはジャンプして移動し、たまちゃんは足首が曲がらないよちよち歩きで追いかける。
どちらかが画面からフレームアウトすると、別の場所(別の雲の稜線)から再び登場する。

## 最初のフレーム(Picture 1)
パステルパープルの空を背景に、ピンク・ラベンダー・ミントグリーンの雲が層になった稜線。
手前左下のピンクの雲にたまちゃんが立ち、奥右上のミントグリーンの雲の上空にぽよんが浮かんでいる構図。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the scene shown in <Picture 1> establishes a soft pastel-purple sky above layered rounded cloud hills in pink, lavender, and mint green, forming a rolling ridge landscape. The egg-shaped character, with its white upper shell, pink lower shell, short stubby limbs, and a flat, outline-only mouth with no depth or color, stands on the pink cloud ridge in the lower left. The transparent, jelly-like rubber character, having no arms or legs, hovers in the air above the mint-green cloud ridge further back on the right, its colorful gumballs and confetti settled inside its body, its own mouth the same flat, depthless outline. The egg character begins toddling rightward along the ridge in its stiff, heel-less waddle, its ankles staying rigid and unbending with each step, chasing after the transparent character. The transparent character springs into a big, playful bounce, arcing off the ridge and disappearing behind the mint-green cloud hill past the right edge of the frame, its interior gumballs and confetti drifting weightlessly without ever spilling out as it flies. [Shot 2] At 00:03.000, the camera cuts to a closer view of the mint-green cloud ridge, where the transparent character suddenly bounces back into frame from the left edge, landing lightly on the cloud's surface before immediately springing off again toward the right, its rubbery body compressing and rebounding with each hop, contents shifting but never spilling. [Shot 3] At 00:05.500, the camera cuts back to the wider cloud-ridge landscape as the egg character reappears from a different cloud ridge on the right side of the frame, still toddling in its stiff-ankle waddle without turning its ankles, spotting the transparent character bouncing away in the distance and continuing the chase across the layered clouds as the shot ends.

overall_soundscape: Soft, muffled footsteps thump with each toddling step the egg character takes across the cloud surface, while a springy rubbery squeak and light rattle of shifting gumballs mark each of the transparent character's bounces. Both characters produce light, breathy giggles throughout as they chase each other across the clouds.

non_diegetic_music: A playful, skipping xylophone melody at a bright, bouncy tempo, its rhythm alternating between light toddling steps and springy bounces.
```

## 日本語訳(参考用)

**指示行**: 対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**: [Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された構図から始まり、パステルパープルの空の下に、ピンク・ラベンダー・ミントグリーンの丸みを帯びた雲の山が層になって連なる稜線が広がる。白い上半分・ピンクの下半分の殻、短い手足、奥行きも色もない平らな輪郭線だけの口を持つ卵形のキャラクターが、手前左下のピンクの雲の稜線に立っている。手足のない透明でゼリーのようなラバーキャラクターは、さらに奥、右側のミントグリーンの雲の稜線の上空に浮かんでおり、体の中には色とりどりのガムボールと紙吹雪が落ち着いて収まり、口も同じく奥行きのない平らな輪郭線でできている。卵形のキャラクターは、踵のつかない硬いくるぶしのまま右方向へよちよちと歩き始め、一歩ごとにくるぶしは曲がらずまっすぐなまま、透明なキャラクターを追いかけていく。透明なキャラクターは大きく楽しげに弾み、稜線から弧を描いて跳び上がり、ミントグリーンの雲の山の陰へ、画面右端の外へと姿を消していき、飛んでいる間、中のガムボールと紙吹雪は重さを感じさせないようにふわりと漂うが、こぼれ出ることは決してない。[Shot 2] 00:03.000の時点で、カメラはミントグリーンの雲の稜線をより近くから捉えたカットに切り替わり、透明なキャラクターが突然画面左端から跳ね戻ってきて、雲の表面に軽やかに着地したかと思うとすぐにまた右方向へ弾み出し、跳ねるたびにゴム製の体が縮んでは伸び、中身は揺れ動くもののこぼれることはない。[Shot 3] 00:05.500の時点で、カメラは再びより広い雲の稜線の景色に戻り、卵形のキャラクターが画面右側の別の雲の稜線から姿を現し、依然としてくるぶしを曲げない硬いよちよち歩きのまま、遠くで跳ねながら去っていく透明なキャラクターの姿に気づき、層になった雲の上での追いかけっこを続けたところでこのショットが終わる。

**環境音**: 卵形のキャラクターがよちよちと一歩踏み出すたびに、雲の表面に柔らかくこもった足音が響き、一方で透明なキャラクターが跳ねるたびに、弾力のあるゴムのきしみ音と、中で揺れるガムボールの軽いカタカタという音が重なる。二人は雲の上で追いかけっこをしている間、ずっと軽やかで息の弾んだ笑い声を上げ続ける。

**BGM(観客のみに聞こえる)**: 明るく弾むテンポの、跳ねるようなシロフォンのメロディが、よちよち歩きの軽い足取りと、弾むようなジャンプの間でリズムを交互に変化させる。

## ComfyUIでの設定メモ
- 最初のフレーム画像(雲の稜線に2人がいる構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 8秒(Shot 2を00:03.000、Shot 3を00:05.500に設定。プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
