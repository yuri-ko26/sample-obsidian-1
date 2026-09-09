---
project: H3-Video-Series
scene: 25
mode: FL2VA
duration: 6s
---

# シーン25: 俯瞰で上手からフレームインし、水平に転がって下手にフレームアウト

## シーン内容
シーン24と逆方向のバージョン。俯瞰の固定カメラ。薄い黄緑色の床の上を、
ぽよんが先に、たまちゃんがすぐ後ろに続く形で、画面右端(上手)から転がりながら
すでにフレームインしてきた直後の瞬間から始まる。2人はそのまま同じ水平方向
(右から左)へ楽しそうに転がり続け、画面左端(下手)まで転がりきって完全に
フレームアウトする。カメラは完全固定。

**設計メモ**: 最初のフレームは「すでに2人が画面の隅にフレームインしてきた直後」の
実画像(Picture 1)を使い、キャラクターの見た目をしっかり anchoring する。最後の
フレーム(Picture 2)は地面のみの実画像だが、これはPicture 1で見た目がすでに
固定されているため、意図しないデザインが生成されるリスクはない(問題になるのは
「最初」のフレームに誰もいない場合のみ)。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 薄い黄緑色の床を真上から見下ろす構図。画面右寄りに、
  左側(先行)にぽよん、右側(後方)にたまちゃんが並び、大きな余白が左側に広がっている
- Picture 2(最後のフレーム): 同じ薄い黄緑色の床のみ、キャラクターは映っていない構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor exactly as shown in <Picture 1>, the camera locked completely in place from the very first instant to the very last: the transparent, jelly-like rubber character rolls slightly ahead on the left and the egg-shaped character rolls close behind it on the right, both already tumbling steadily in the same direction along the same horizontal line, having just rolled into frame moments earlier from the right side. The camera never pans, tilts, zooms, dollies, or cuts away at any point, and never drifts or reframes even slightly; the floor, the framing, and the lens remain pixel-for-pixel identical throughout, with only the characters themselves moving within this one completely unchanging static frame. The transparent character's round body rotates smoothly end over end around its own horizontal axis at a happy, playful pace, like a ball rolling steadily along the ground, each full rotation carrying it further forward in a smooth, continuous barrel-roll rather than sliding flat across the floor. Its round dark eyes and flat, outline-only mouth stay fixed at one point on its glossy round surface, turning and spinning around together with the body itself as it rotates, so the face visibly rotates into view and away again with every turn rather than staying anchored in one screen position while the body spins beneath it. Its interior gumballs and confetti drift and shift inside without ever spilling out, its mouth staying pure uncolored line work throughout. Right behind it, the egg character stays lying down flat against the floor the entire time, its whole body rotating end over end around its own horizontal axis in exactly the same smooth, continuous barrel-roll motion as the transparent character beside it, like a log rolling steadily along the ground, each full rotation carrying it further forward at the same matched pace — it never slides or glides forward without rotating, and it never rises up, stands upright, or takes any walking steps at any point in the shot. It rolls with its short stubby arms held raised up above its tumbling body the whole time, its non-bending limbs staying lifted with each turn, its own flat, outline-only features staying pure line work with no depth or color as it rotates. The two continue rolling together in this same straight horizontal line, matching each other's pace exactly, moving steadily leftward across the full width of the frame until both have completely exited past the left edge, with no part of either character remaining visible, leaving only the empty pale yellow-green floor exactly as shown in <Picture 2>, in the exact same static framing as the opening frame, at the end of the shot.

overall_soundscape: A rhythmic sequence of rubbery squeaks and light rattles from the shifting gumballs marks each turn of the transparent character's body, mixed with soft, repeated thuds as the egg character tumbles right behind it. Both characters produce light, happy, breathy giggles throughout as they roll playfully across the floor and out of frame.

non_diegetic_music: An upbeat, rolling marimba melody at a cheerful, bouncy tempo, its rhythm mirroring the two characters' matched tumbling pace as they cross the frame and disappear.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り、薄い黄緑色の床を真上から見下ろしており、カメラは最初の瞬間から最後の瞬間まで完全に固定されたまま動かない。透明でゼリーのようなラバーキャラクターが少し先行して左側を、卵形のキャラクターがそのすぐ後ろの右側を、どちらもすでに同じ水平方向へ一定のペースで転がっており、少し前に画面右側からフレームインしたばかりの状態である。カメラは一切パン・チルト・ズーム・ドリーせず、ほんの少しもずれたり構図が変わったりすることはない。床も画角もレンズも、一画素単位でまったく同一のまま保たれ、この完全に変化しない固定フレームの中で動くのはキャラクターだけである。透明なキャラクターの丸い体は、まるでボールが地面を転がるように、自分自身の水平な軸を中心として滑らかに一回転また一回転と回り続け、楽しそうな軽快なペースで、一回転するごとにさらに前へ進んでいく — 床の上を滑るように平行移動するのではなく、なめらかに連続した樽転がりのような動きである。その丸い黒目と、平面的で輪郭線だけの口は、光沢のある丸い表面上の一箇所に固定されたまま、体そのものと一緒に回転し、回るたびに顔が画面に現れては見えなくなるを繰り返す — 体だけが下で回転して顔は画面上の同じ位置に留まり続けるようなことにはならない。中のガムボールと紙吹雪は漂うように揺れ動くが決してこぼれることはなく、口は終始無着色の線画のままである。そのすぐ後ろでは、卵形のキャラクターが終始床に寝そべったまま、透明なキャラクターとまったく同じ、滑らかで連続した樽転がりのような動きで、自分自身の水平な軸を中心として体全体が一回転また一回転と回り続け、まるで丸太が地面を転がるように、一回転するごとに同じペースでさらに前へ進んでいく — 回転せずに滑ったり滑走したりして前に進むことは決してなく、また、ショットのどの瞬間においても起き上がったり、立ち上がったり、歩くようなステップを踏んだりすることも一切ない。短く曲がらない手を転がっている間ずっと上に上げたまま転がり続け、一回転するたびもその手は上がったままで、奥行きも色もない平らな輪郭線だけの顔立ちはそのまま線画として保たれている。二人はこのまま同じ水平の直線上を、互いのペースを完全に合わせながら左方向へ転がり続け、画面の幅いっぱいを進んでいき、どちらの体もまったく見えなくなるまで完全に左端の外へ出ていき、<Picture 2>で示された通り、最初のフレームとまったく同じ固定構図のまま、誰もいない薄い黄緑色の床だけが残ったところでこのショットが終わる。

**環境音**
透明なキャラクターが一回転するたびに、やわらかく規則的なゴムのきしみ音と、中でガムボールが軽くカタカタと揺れる音が響き、そのすぐ後ろで卵形のキャラクターが転がるたびの柔らかく繰り返す「ぽすん」という音が混ざる。二人は床の上を楽しそうに転がって画面の外へ消えるまで、ずっと軽やかで幸せそうな笑い声を上げ続ける。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、二人のぴったり合った転がるペースに合わせたリズムを刻みながら、二人が画面を横切って姿を消すまで続く。

## ComfyUIでの設定メモ
- 最初のフレーム画像(2人がすでに右寄りにフレームインしている俯瞰構図)を Picture 1、
  最後のフレーム画像(同じ床のみ、キャラクターなし)を Picture 2 として、
  FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 6秒(プロンプト内の秒数表記と要一致)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
