---
project: H3-Video-Series
scene: 24
mode: I2VA
duration: 6s
---

# シーン24: 俯瞰で同じ水平方向にコロコロ転がり続けてフレームアウト

## シーン内容
俯瞰の固定カメラ。薄い黄緑色の床の上を、たまちゃんが先に、ぽよんがすぐ後ろに続く形で、
画面左端から転がりながらすでにフレームインしてきた直後の瞬間から始まる。2人はそのまま
同じ水平方向(左から右)に転がり続け、画面右端まで転がりきって完全にフレームアウトする。
たまちゃんは転がっている間、短い手を上に上げたままの姿勢。カメラは完全固定。

**設計メモ**: 参照画像に誰も映っていない(真っ白/空の床だけ)状態を最初のフレームにすると、
モデルがキャラクターの見た目を判断する手がかりを失い、意図しないデザインのキャラクターが
生成されるリスクがある。そのため「誰もいない状態」からではなく、「すでに画面の隅に
2人がフレームインしてきた直後」の実画像をPicture 1として使い、そこから先の動きだけを
テキストで描写する構成にしている。I2VA(最初のフレームのみ参照)のため、最後の
フレーム画像は不要。

## 最初のフレーム(Picture 1)
薄い黄緑色の床を真上から見下ろす構図。画面左寄りに、右側(先行)にたまちゃん、
左側(後方)にぽよんが並び、大きな余白が右側に広がっている。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor exactly as shown in <Picture 1>: the egg-shaped character rolls slightly ahead on the right and the transparent, jelly-like rubber character rolls close behind it on the left, both already tumbling steadily in the same direction along the same horizontal line, having just rolled into frame moments earlier. The camera never pans, tilts, zooms, or cuts away at any point. The egg character stays lying down flat against the floor the entire time, its body continuously turning over and over as it rolls, and it never rises up, stands upright, or takes any walking steps at any point in the shot. It rolls with its short stubby arms held raised up above its tumbling body the whole time, its non-bending limbs staying lifted with each turn, its flat, outline-only features staying pure line work with no depth or color as it rotates. Right behind it, the transparent character's round body turns over and over at the same steady pace, its interior gumballs and confetti drifting and shifting inside without ever spilling out, its own flat, outline-only mouth staying pure uncolored line work throughout. The two continue rolling together in this same straight horizontal line, matching each other's pace exactly, moving steadily across the full width of the frame until both have completely exited past the right edge, with no part of either character remaining visible and only the empty pale yellow-green floor left onscreen as the shot ends.

overall_soundscape: A soft, repeated series of muffled thuds marks the egg character tumbling along with its arms raised, mixed with a rhythmic sequence of rubbery squeaks and light rattles from the shifting gumballs as the transparent character rolls right behind it. Both characters produce light, breathy giggles throughout as they roll across the floor and out of frame.

non_diegetic_music: An upbeat, rolling marimba melody at a steady, bouncy tempo, its rhythm mirroring the two characters' matched tumbling pace as they cross the frame and disappear.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り、薄い黄緑色の床を真上から見下ろしており、卵形のキャラクターが少し先行して右側を、透明でゼリーのようなラバーキャラクターがそのすぐ後ろの左側を、どちらもすでに同じ水平方向へ一定のペースで転がっており、少し前に画面にフレームインしたばかりの状態である。カメラは一切パン・チルト・ズーム・カットをしない。卵形のキャラクターは終始床に寝そべったまま、その体が何度も回転し続けて転がっており、ショットのどの瞬間においても起き上がったり、立ち上がったり、歩くようなステップを踏んだりすることは一切ない。短く曲がらない手を転がっている間ずっと上に上げたまま転がり続け、一回転するたびもその手は上がったままで、奥行きも色もない平らな輪郭線だけの顔立ちはそのまま線画として保たれている。そのすぐ後ろでは、透明なキャラクターの丸い体が同じ一定のペースで何度も回転し、中のガムボールと紙吹雪が漂うように揺れ動くが決してこぼれることはなく、平面的で輪郭線だけの口も終始無着色の線画のままである。二人はこのまま同じ水平の直線上を、互いのペースを完全に合わせながら転がり続け、画面の幅いっぱいを進んでいき、どちらの体もまったく見えなくなるまで完全に右端の外へ出ていき、画面には誰もいない薄い黄緑色の床だけが残ったところでこのショットが終わる。

**環境音**
卵形のキャラクターが手を上げたまま転がるたびに、柔らかくこもった「ぽすん」という音が繰り返し響き、そのすぐ後ろで透明なキャラクターが転がるたびの、やわらかく規則的なゴムのきしみ音と、中でガムボールが軽くカタカタと揺れる音が混ざる。二人は床の上を転がって画面の外へ消えるまで、ずっと軽やかで息の弾んだ笑い声を上げ続ける。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、二人のぴったり合った転がるペースに合わせたリズムを刻みながら、二人が画面を横切って姿を消すまで続く。

## ComfyUIでの設定メモ
- 最初のフレーム画像(2人がすでに左寄りにフレームインしている俯瞰構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒(プロンプト内の秒数表記と要一致)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
