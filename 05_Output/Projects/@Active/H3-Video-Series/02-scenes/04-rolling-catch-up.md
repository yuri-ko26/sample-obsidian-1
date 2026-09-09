---
project: H3-Video-Series
scene: 4
mode: I2VA
duration: 9s
---

# シーン4: 俯瞰でコロコロ→フレームアウト→再登場してぽよんが追いつく

## シーン内容
俯瞰(真上から見下ろす)ショット。ぽよんとたまちゃんが同じ方向にコロコロ転がりながら、
完全にフレームアウトするまで転がっていく。その後、フレームアウトした側から再び2人が
転がって現れ、時々ぽよんの方が速く転がって追いつく場面を挟みながら、楽しそうに笑って
再びフレームアウトする。

## 最初のフレーム(Picture 1)
オリーブグリーンの床を真上から見下ろす構図。左にぽよん、右にたまちゃんが並んで
こちら(カメラ)を向いて立っている。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a static overhead shot looks straight down on the olive-green floor as shown in <Picture 1>, with the transparent, jelly-like rubber character on the left and the egg-shaped character on the right, both facing the camera. Both characters begin rolling together in the same direction, tumbling in sync across the floor; throughout the roll, each keeps its face-side correctly oriented, with the eyes and mouth remaining only on the front-facing side and never appearing on the back as the body turns, and the transparent character's interior gumballs and confetti drift and shift but never spill out. The two continue rolling side by side until both have completely exited the frame, with no part of either character remaining visible onscreen. [Shot 2] At 00:04.500, the camera holds the same static overhead framing as both characters roll back into frame from the same edge they exited, continuing to tumble together in the same direction, still correctly keeping their faces on the front-facing side through every rotation and the transparent character's contents never spilling. At times, the transparent character's rolling speeds up, pulling slightly ahead before catching back up alongside the egg character; both characters' outline-only mouths curve into happy grins and their eyes crinkle with laughter as they play. The two continue rolling together until both have completely exited the frame again, with no part of either character remaining visible as the shot ends.

overall_soundscape: A steady rhythmic sequence of soft rubbery squeaks and light rattling gumballs marks each turn of the transparent character's body, mixed with soft repeated thuds from the egg character tumbling alongside it. When the transparent character speeds up to catch up, its bouncing rhythm quickens briefly before settling back in sync. Both characters produce light, happy giggles throughout as they roll and play.

non_diegetic_music: An upbeat, rolling marimba melody at a bouncy tempo, briefly speeding up when the transparent character catches up before returning to its steady rolling rhythm.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通り、オリーブグリーンの床を真上から見下ろす固定の俯瞰ショットで、左に透明でゼリーのようなラバーキャラクター、右に卵形のキャラクターが並び、どちらもカメラの方を向いている。二人は同じ方向へ一緒に転がり始め、床の上を息を合わせて転がっていく。転がっている間、それぞれのキャラクターは顔のある面を常に正しい向きに保ち、目と口は前面にだけあり続け、体が回転しても背面に現れることはなく、透明なキャラクターの中のガムボールと紙吹雪は揺れ動くもののこぼれ出ることはない。二人は横に並んだまま転がり続け、どちらの体もまったく見えなくなるまで完全に画面の外へ出ていく。[Shot 2] 00:04.500の時点で、カメラは同じ固定の俯瞰構図を保ったまま、二人が先ほど出ていったのと同じ側から再び転がって画面に入ってきて、同じ方向へ一緒に転がり続け、回転のたびに顔は正しく前面にあり続け、透明なキャラクターの中身もこぼれることはない。時々、透明なキャラクターの転がる速度が上がり、少し先へ進んだかと思うとすぐに卵形のキャラクターの隣へ追いつく。二人とも輪郭線だけの口が楽しそうな笑みの形に曲がり、目は笑いじわのように細まりながら遊び続ける。二人はそのまま一緒に転がり続け、どちらの体もまったく見えなくなるまで、再び完全に画面の外へ出ていったところでこのショットが終わる。

**環境音**
透明なキャラクターの体が一回転するたびに、規則正しく柔らかいゴムのきしみ音と、中で軽くカタカタと揺れるガムボールの音が続き、それに卵形のキャラクターが隣で転がるたびの柔らかく繰り返す「ぽすん」という音が重なる。透明なキャラクターが追いつこうと速度を上げる場面では、その弾むリズムが一瞬速くなり、すぐにまた元の同じペースに戻る。二人は転がって遊んでいる間、ずっと軽やかで楽しそうな笑い声を上げ続ける。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、透明なキャラクターが追いつく場面で一瞬テンポを上げ、その後また落ち着いた一定の転がるリズムに戻る。

## ComfyUIでの設定メモ
- 最初のフレーム画像(オリーブグリーンの床に2人が並ぶ俯瞰構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 9秒(Shot 2の切り替えを00:04.500に設定。プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
