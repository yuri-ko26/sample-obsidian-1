---
project: H3-Video-Series
scene: 26
mode: FL2VA
duration: 6s
---

# シーン26: 下手からたまちゃん・ぽよんの順に転がりながらフレームインし、中央で止まって顔を見合わせ大笑い

## シーン内容
俯瞰の固定カメラ。最初は誰もいない薄い黄緑色の床だけの構図から始まる。
画面左端(下手)から、たまちゃんが先に、ぽよんがすぐ後ろに続く形で、
横並びで水平に転がりながらフレームインしてくる。2人はそのまま画面中央まで
転がって進み、中央で並んで止まる。止まったところで互いに顔を見合わせ、
大笑いする(ぽよんは目を閉じて輪郭線の口を大きく笑顔に、たまちゃんも目を
細めて口を大きく開けて笑い、短い手足を左右に広げる)。カメラは完全固定。

**設計メモ**: 最初のフレーム(Picture 1)には誰も映っていないが、最後のフレーム
(Picture 2)に2人の見た目がはっきり映っているため、FL2VAとして両方を参照させることで
モデルが2人の見た目を anchoring できる(空フレームのリスクが生じるのは、
最初・最後どちらの参照画像にもキャラクターの姿が一切ない場合のみ)。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 薄い黄緑色の床のみ。キャラクターは映っていない構図
- Picture 2(最後のフレーム): 画面中央に、左にぽよん、右にたまちゃんが並んで止まり、
  2人とも大笑いしている構図(ぽよんは目を閉じて輪郭線の口を大きく開けて笑い、
  たまちゃんも目を細めて口を大きく開けて笑い、短い手足を左右に広げている)

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. From the left edge of the frame, the egg-shaped character rolls into view first, tumbling steadily along the ground, with the transparent, jelly-like rubber character rolling right behind it, both tumbling side by side along the same horizontal line as they continue further into the frame, the transparent character's interior gumballs and confetti drifting and shifting inside without ever spilling out. As the two roll toward the middle of the floor, their tumbling gradually slows, and they come to a gentle stop side by side in the center of the frame, the transparent character settling on the left and the egg character settling on the right. Once still, they turn to face each other, their eyes meeting, and immediately burst into big, delighted laughter: the transparent character's round eyes crinkle shut into laughing crescents as its flat, outline-only mouth stretches into a wide, uncolored grin with no depth or interior color, while the egg character's own eyes crinkle into laughing crescents as its mouth opens wide with a hint of soft pink visible inside, its short stubby arms and legs splaying outward to the sides as it laughs, both of them coming to rest in the exact poses and framing shown in <Picture 2> at the end of the shot.

overall_soundscape: A rhythmic sequence of rubbery squeaks and light rattles from the shifting gumballs marks each turn of the transparent character's body, mixed with soft, repeated thuds as the egg character tumbles right behind it. As their rolling slows to a stop, a final soft settling sound marks them coming to rest, followed by a bright, delighted burst of giggling laughter from both characters as their eyes meet.

non_diegetic_music: An upbeat, rolling marimba melody at a cheerful, bouncy tempo as the two roll in and slow to a stop, resolving into a warm, joyful flourish the moment their eyes meet and they burst into laughter together.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り、薄い黄緑色の床のみが映る誰もいない構図から始まる。カメラは一切パン・チルト・ズーム・カットをしない。画面左端から、卵形のキャラクターが先に転がりながら姿を見せ、着実に床の上を転がり進んでいき、そのすぐ後ろで透明でゼリーのようなラバーキャラクターも転がりながら続き、二人は同じ水平の直線上を横並びで転がって画面のさらに奥へと進んでいき、透明なキャラクターの中のガムボールと紙吹雪は漂うように揺れ動くもののこぼれ出ることはない。二人が床の中央に向かって転がっていくにつれて、その転がる勢いは次第に緩やかになっていき、画面中央で並んでそっと止まる — 透明なキャラクターが左側に、卵形のキャラクターが右側に落ち着く。静止すると、二人は互いに顔を向け合い、目が合った瞬間、すぐに大きく嬉しそうな笑いがこみ上げる — 透明なキャラクターの丸い目はぎゅっと閉じて笑いじわの三日月形になり、平面的で輪郭線だけの口は奥行きも中の色もないまま大きく無着色の笑顔に伸びる。一方、卵形のキャラクターも目を笑いじわの三日月形に細め、口を大きく開けてその内側にほんのりピンク色が覗き、短く曲がらない手足を左右に広げながら笑う。二人とも<Picture 2>で示された通りのポーズと構図に落ち着いたところでショットが終わる。

**環境音**
透明なキャラクターが一回転するたびに、やわらかく規則的なゴムのきしみ音と、中でガムボールが軽くカタカタと揺れる音が響き、そのすぐ後ろで卵形のキャラクターが転がるたびの柔らかく繰り返す「ぽすん」という音が混ざる。転がる勢いが緩やかになり止まる瞬間には、最後にそっと落ち着く音が響き、その後、目が合った二人から明るく嬉しそうな笑い声がはじけるように上がる。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、二人が転がってきて止まるまで流れ、目が合って二人が一緒に笑い出す瞬間に、温かく喜びに満ちたフレーズへと解決する。

## ComfyUIでの設定メモ
- 最初のフレーム画像(床のみ、キャラクターなし)を Picture 1、最後のフレーム画像
  (中央で2人が並んで大笑いしている構図)を Picture 2 として、FL2VA用の画像入力に
  それぞれ接続
- モード: FL2VA
- 尺: 6秒(プロンプト内の秒数表記と要一致)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
