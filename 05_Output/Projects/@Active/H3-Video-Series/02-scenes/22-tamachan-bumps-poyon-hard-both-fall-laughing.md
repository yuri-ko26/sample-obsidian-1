---
project: H3-Video-Series
scene: 22
mode: FL2VA
duration: 4s
---

# シーン22: たまちゃんが思い切って強くぶつかり、ぽよんも倒れて2人で体を震わせて大笑い

## シーン内容
シーン16・20・21の続き。2人は目を合わせ、楽しさを予感してニコニコしている。
たまちゃんは今回思い切って、前より強くぽよんに体当たりしにいく。強い衝撃で
今度はぽよんもバランスを崩して横向きに倒れ、たまちゃんも自分の勢いで転がって
倒れる。2人ともその場に倒れたまま、体を震わせるほど大笑いする。カメラは完全固定。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 淡い緑の床、パステルの雲を背景に、左にぽよん、
  右にたまちゃんが並んで立ち、笑顔でこちらを向いている構図
- Picture 2(最後のフレーム): 左でぽよんが横向きに倒れ、丸みを保ったまま傾いた姿勢で
  目を閉じて笑っている構図。右でたまちゃんも仰向けに転んで手足を上げ、
  楽しそうに笑っている構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, beginning in the position and framing established by Picture 1: the transparent, jelly-like rubber character stands on the left and the egg-shaped character stands on the right, side by side on the pale green floor against soft pastel cloud shapes, both facing the camera with content smiles. The camera never pans, tilts, zooms, or cuts away at any point. The two glance toward each other, their smiles widening right away into knowing, mischievous grins, already delighted in anticipation, clearly remembering how much fun this same game was a moment ago. This time the egg character gathers itself with extra determination, its stiff little limbs pulling back before it launches itself sideways through the air with much greater force than before, throwing its whole body eagerly and hard at the transparent character. The egg character's body presses squarely into the transparent character's rubbery surface, which yields inward into a smooth, curved dimple rather than flattening, staying round like a yo-yo, and none of its balls or confetti escape. This time, the impact is strong enough that the transparent character itself is knocked off balance, its round body tipping sideways and toppling over to rest tilted on the floor, still perfectly round and never flattening, its interior gumballs and confetti settling gently inside without ever spilling out. The egg character, its own stiff, non-bending limbs unable to absorb the force of its own hard leap, tumbles down onto its back at the same time, its little arms and legs flopping up into the air. Both characters end up down on the floor together, and as they land, their laughter becomes so strong that their whole bodies shake and tremble with it: the egg character's eyes crinkle shut as its mouth opens wide with a hint of soft pink visible inside, while the transparent character's flat, outline-only mouth curves into an equally wide, uncolored grin, its round eyes crinkled with mirth, both of them shaking with uncontrollable laughter in the exact poses and framing shown in Picture 2 at the end of the shot.

overall_soundscape: A quiet, happy little giggle passes between the two characters as their eyes meet. A quick, determined shuffling sound marks the egg character pulling back before its harder leap, followed by a bigger, muffled springy thud as it throws itself into the transparent character. A soft wobbling creak marks the transparent character tipping over and settling on its side, and a gentle flump marks the egg character tumbling onto its back. Both characters then burst into bright, shaking, uncontrollable giggling laughter that keeps trembling on as the shot ends.

non_diegetic_music: A bright, eager pizzicato phrase bounces along as the two share their knowing grins, building with a bigger, more dramatic swell as the egg character leaps harder this time, a heavier comedic accent landing on the bump and double topple, before settling into a warm, joyful, gently trembling flourish as both characters shake with laughter together.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、Picture 1で示された構図から始まる — 透明でゼリーのようなラバーキャラクターが左に、卵形のキャラクターが右に、淡い緑の床の上にパステルの雲を背景にして並んで立ち、どちらもカメラの方を向いて満足そうな笑顔を浮かべている。カメラは一切パン・チルト・ズーム・カットをしない。二人は互いに目を向け合い、すぐにいたずらっぽい確信めいた笑顔へと広がっていく — さっき同じ遊びがどれほど楽しかったかをはっきり覚えていて、すでに期待に満ちて嬉しそうである。今回、卵形のキャラクターはいつもよりさらに気合を入れて身構え、硬い小さな手足を一度引いてから、前回よりずっと強い勢いで透明なキャラクターへ横に体全体を思い切りぶつけにいく。卵形のキャラクターの体は透明なキャラクターのラバーの表面に真正面から押し当たり、表面は平らに潰れるのではなく、ヨーヨーのように丸みを保ったまま内側へなめらかにくぼむ。中のボールや紙吹雪は一つもこぼれ出ない。今回はその衝撃が強く、透明なキャラクター自身もバランスを崩し、丸い体を横に傾けながら床の上に倒れ込み、傾いた姿勢のまま止まるが、体は平らに潰れることなく完全に丸みを保ったままで、中のガムボールと紙吹雪もそっと落ち着き、こぼれ出ることはない。卵形のキャラクターも、自分の強いジャンプの勢いを曲がらない硬い手足では受け止めきれず、同時に仰向けに転がり倒れ、小さな手足がふわりと宙に跳ね上がる。二人はそのまま一緒に床に倒れ込み、着地すると同時に、その笑いはあまりに強くなって体全体が震えるほどになる — 卵形のキャラクターは目をぎゅっと閉じ、口を大きく開けてその内側にほんのりピンク色が覗く一方、透明なキャラクターの平面的で輪郭線だけの口も同じくらい大きく、無着色のまま笑顔の形に曲がり、丸い目は笑いじわのように細まり、二人とも抑えきれない笑いに体を震わせながら、Picture 2で示された通りのポーズと構図に落ち着いたところでショットが終わる。

**環境音**
二人の目が合った瞬間、静かで嬉しそうな小さな笑い声が交わされる。卵形のキャラクターが強く跳ぶ前に一度身構える、気合の入った素早い衣擦れの音が続き、透明なキャラクターに体当たりする瞬間、これまでより大きな、こもった弾力のある衝突音が鳴る。透明なキャラクターが横に傾いて倒れ込む柔らかいきしみ音と、卵形のキャラクターが仰向けに倒れ込む柔らかな「ふすん」という音が続き、その後、二人とも明るく震えるほど抑えきれない笑い声を上げ続けたままショットが終わる。

**BGM(観客のみに聞こえる)**
二人が確信めいた笑みを交わす間、明るく前のめりなピチカートのフレーズが弾むように流れ、今回は卵形のキャラクターがより強く跳ぶのに合わせて、より大きくドラマチックに盛り上がっていく。ぶつかって二人とも倒れる瞬間には、これまでより重みのあるコミカルなアクセントが入り、その後、二人が一緒に震えながら笑い合う、温かく喜びに満ちた小刻みなフレーズへと落ち着いていく。

## ComfyUIでの設定メモ
- 最初のフレーム画像(2人が並んで立つ構図)を Picture 1、最後のフレーム画像(ぽよんが横に
  倒れ、たまちゃんも仰向けに転んで2人で大笑いしている構図)を Picture 2 として、
  FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 4秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
