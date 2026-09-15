---
project: H3-Video-Series-v2
cut: D-1
mode: I2VA
status: draft
---

# カットD-1: 俯瞰固定カメラ、画面左からフレームイン→中央を水平にコロコロ転がって右へフレームアウト

## シーン内容
> **注記(v10時点)**: 新しくいただいた画像(ぽよんが回転中、たまちゃんが立った
> ままの状態で、画面右寄りに並んでいる構図)をもとに、E-1への橋渡し部分を
> 更新。中央に到達したら、たまちゃんは仰向けに寝転んでそのままぽよんを
> 楽しそうに見守り続け、ぽよんは単に起き上がるだけでなく**ジャンプに備えた
> 「よし、次はこれをして遊ぼう!」という構えの姿勢**に入るところまで拡張。

> **注記(v9時点)**: E-1(ジャンプ)への橋渡しとして使うこのカットは、v7/v8で
> 一度「歩き/弾み」バージョンを試したが、v9で**「転がる」バージョンに戻した**
> (歩きではなく転がって中央へ向かい、そのまま停止する)。

クライアント要望どおり、俯瞰の固定カメラで、2人が画面左から入ってきて、画面中央を
水平にコロコロと転がって移動する。中央に到達したら停止し、仰向けに寝転んで
ぽよんだけ起き上がりE-1へ続く。単一の固定ショット。

**設計メモ**: 旧アーカイブ(シーン24〜27)で「回転の物理」表現に何度も試行錯誤した
経緯がある。今回は最終的に一番安定していた「前転(でんぐり返し)/カートホイール、
正面→背中→正面、を規則正しく繰り返す」表現をベースに採用。斜め回転になる問題を
避けるため「水平を保つ・斜めにならない」を強く明記している。生成後、回転の見え方に
違和感があれば、その場で微調整する想定。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは転がる間、短い手を上に上げたままの姿勢
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない
- 顔(目・口)は体の片面にしかないため、回転中に顔と体の向きの整合性を保つ

## 参照画像
- Picture 1(v10で採用・最初のフレーム): 新しくいただいた画像。薄い黄緑色の床を
  真上から見下ろす構図。画面右寄りに、ぽよんが回転している最中の姿勢、その右に
  たまちゃんが立った状態で並んでおり、左側に大きな余白が広がっている
- (v4〜v9で使用していた旧Picture1): 画面左寄りに、左側にぽよん・その右に
  たまちゃんが並び、右側に大きな余白が広がっている構図(過去バージョン用)

## プロンプト履歴

### v10 (2026-09-15) — 現在の採用版(新しい参照画像+ぽよんがジャンプ構えに入るまで拡張)

新しくいただいた画像を新しいPicture1として採用。画像ではぽよんは回転中の姿勢、
たまちゃんは(回転せず)立った状態で並んでいるため、**ぽよんは引き続き回転しながら
横滑りで進み、たまちゃんは回転せずつま先立ちで歩いて進む**という組み合わせで
中央へ向かう構成にした(たまちゃんが画像内で回転していないポーズのため)。
※この組み合わせの解釈で問題があれば教えてください。

中央に到達したら、**たまちゃんは仰向けに寝転んでそのままの姿勢を保ち、起き上がる
ぽよんを楽しそうに見つめ続ける**。ぽよんは起き上がった後、単に直立するだけでなく、
**体を少し沈めてバネのように構えた「今にもジャンプしそうな」姿勢**に入り、
「さあ次はこれをして遊ぼう!」という気持ちを、言葉を発さず体の動きだけで表現する
(E-1の大ジャンプへの橋渡し)。カメラは終始同じ俯瞰の位置に固定。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Neither character ever speaks, talks, or makes any vocalization at any point in this entire shot — there is no dialogue, no speech, no mouthed words, and no lip movement suggesting speech at any point; both characters remain completely silent throughout, expressing everything purely through body language and expression, never through speech. The transparent, jelly-like rubber character continues spinning steadily in place like a flat disc turning on the floor while gliding sideways at the same time, moving further onto the floor with each moment, continuing exactly the motion already visible in <Picture 1>. Critically, its face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it, exactly like the rest of its glossy skin. As the body spins, the face spins together with it as one single rigid piece: the face turns away and becomes hidden from view as that side of the body rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face the camera — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift and tumble inside with each spin, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. Beside it, the egg-shaped character moves in a completely different way, without any spinning or rolling at all: it toddles forward with small, bouncy steps, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point, its short arms swinging cheerfully with each step. Both characters continue moving toward the center of the frame this way, the transparent character spinning and gliding, the egg-shaped character toddling on tiptoe beside it, until both reach roughly the center of the frame. Once there, the egg-shaped character comes to a stop and happily flops down onto its back, settling flat on the floor, face up toward the camera, wearing a calm, happy smile, and stays exactly like this for the remainder of the shot — relaxed, still smiling, making no move to get up, its gaze turned toward the transparent character beside it, watching it with warm, happy interest the whole time. At the same moment, the transparent character stops spinning and gliding, and rights itself upright at the same spot near the center of the frame. Rather than simply standing still, it settles into a low, coiled, spring-loaded crouch, its whole body compressed slightly downward as if gathering energy, poised and ready to spring upward at any moment — its whole posture radiating eager, bursting anticipation, as if silently saying "alright, let's do this next!" purely through its body language, without speaking a single word. Its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing — shift and settle naturally at the bottom of its body under gravity as it crouches, never spilling out. The shot ends with the egg-shaped character lying flat on its back, smiling calmly and watching happily, and the transparent character beside it in this low, coiled, ready-to-jump crouch, both completely silent throughout, poised for what comes next.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。どちらのキャラクターも、このショット全体を通して一切話したり、喋ったり、発声したりすることはなく、2人とも終始完全に無言のままで、すべてを言葉ではなく体の動き・表情だけで表現する。透明でゼリーのようなラバーキャラクターは、<Picture 1>ですでに見えている動きをそのまま継続し、床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に横方向へ滑るように移動し、時間が経つにつれて床の上をさらに進んでいく。極めて重要な点として、その顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、光沢のある体の他の部分とまったく同じように、体の一箇所に恒久的に付着している。体が回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分の体がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周してカメラの方を向いたときにだけ再び顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色や余分なガムボールは一切現れない)——とカラフルな紙吹雪は、回転するたびに揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。その隣では、卵形のキャラクターがまったく異なる、回転や転がりを一切伴わない動き方をする——常につま先の先端だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらず、短い両腕は一歩ごとに楽しそうに揺れる、小さく弾むような足取りでよちよちと進む。2人はこのまま画面中央へ向かって進み続け——透明なキャラクターは回転しながら滑るように、卵形のキャラクターはその隣でつま先立ちでよちよちと——おおよそ画面中央に到達する。そこに到達すると、卵形のキャラクターは立ち止まり、嬉しそうに仰向けにゴロンと寝転がり、体を床に平らに横たえて、カメラの方(上)を向き、穏やかで嬉しそうな笑顔を浮かべ、ショットの残り時間ずっとこのままの状態を保つ——リラックスして、笑顔のまま、起き上がろうとする素振りは一切見せず、その視線は隣の透明なキャラクターの方へ向けられ、終始温かく嬉しそうな興味を持ってそれを見つめている。同じ瞬間、透明なキャラクターは回転と滑りをやめ、画面中央付近の同じ場所で体を起こして直立する。ただ静止して立つのではなく、体をわずかに沈めた、バネのように力を溜めた低い構えの姿勢に入り、いつでも上へ飛び出せるよう身構える——その姿勢全体から、今にもはじけそうな意欲的な期待感があふれ、まるで「よし、次はこれをやろう!」と、一言も声に出さず、体の動きだけで静かに語りかけているかのようである。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)——は、しゃがみ込む動きに合わせて重力に従って体の底に自然に沈み、こぼれることは一切ない。ショットの終わりには、卵形のキャラクターは仰向けに横たわり、穏やかな笑顔で嬉しそうに見つめており、透明なキャラクターはそのすぐそばで、この低く構えたジャンプ前の姿勢のまま——2人とも終始完全に無言のまま、次の展開に向けて身構えている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v10.mp4`(未生成)
- 判定: 未検証
- メモ: 新しい参照画像(ぽよん回転中・たまちゃん立ち姿、画面右寄り)を採用。
  ぽよんが回転しながら中央へ進み、たまちゃんはつま先立ちで歩いて中央へ進む
  組み合わせにした(画像内でたまちゃんが回転していないポーズのため)。中央到達後は
  たまちゃんが仰向けのままぽよんを見守り、ぽよんは単に起き上がるだけでなく
  「低く構えたジャンプ前の姿勢」まで踏み込んで拡張した

### v9 (2026-09-15) — 旧版(転がりバージョン、ぽよんは単に起き上がるだけ)

「歩いてではなく転がって中央へ」というご要望を受け、回転(転がり)バージョンに戻した。
セリフを喋ってしまう不具合の対策(v8で確立)は維持し、感情(意欲的で「よし、
いくぞー!」という気持ち)は同じまま、言葉には出さない形にしている。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Neither character ever speaks, talks, or makes any vocalization at any point in this entire shot — there is no dialogue, no speech, no mouthed words, and no lip movement suggesting speech at any point; both characters remain completely silent throughout, expressing everything purely through body language and expression, never through speech. Each character's body behaves as if it were mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to the direction of travel — this axle is the only line either character's body is able to rotate around; neither character is capable of spinning around a vertical axis like a top or a coin lying flat on a table, that kind of flat, in-place spinning is structurally impossible for them and never happens at any point. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously rotates forward around this fixed horizontal axle, end over end, exactly like a wheel rolling along the ground: the point of its body currently facing up rotates forward and down to become the point facing the floor, while the point that was facing the floor rotates up and around to become the new top — front, then back, then front again, in a steady, continuous, unbroken rotation as it advances. It stays perfectly level as it rotates, its axle never tilting diagonally, never drifting off to point in any other direction, and it never rises up or stands during this rolling. Beside it on the left, the transparent, jelly-like rubber character rotates forward around its own fixed horizontal axle the exact same way — end over end like a wheel, its top and bottom steadily and continuously swapping places with each rotation, its axle staying perpendicular to its direction of travel the entire time, never once spinning flat in place — its interior gumballs and confetti shifting inside without ever spilling out. Both continue rotating forward together at a matched pace around their own fixed horizontal axles, moving steadily rightward across the frame. Critically, instead of exiting the frame, once both characters reach roughly the center of the frame, they gradually slow their rotation and come to a gentle, natural stop there, settling flat on their backs, face up toward the camera, both wearing calm, happy smiles, coming to rest side by side in the middle of the shot. The camera remains fixed in this same overhead position throughout, never moving. After a brief calm moment lying there together, the egg character stays exactly where it is, remaining flat on its back the whole time, relaxed and still smiling, making no move to get up. At the same time, the transparent character alone begins to perk up with sudden, eager energy, silently and without speaking a single word — its body language alone conveying eager, excited enthusiasm, as if bursting to get moving — pushing itself up from lying flat into an upright, bouncy, ready-to-go posture, its whole body brimming with playful enthusiasm, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting and settling naturally at the bottom of its body under gravity as it rights itself, never spilling out. The shot ends with the egg character still lying flat on its back smiling calmly, and the transparent character upright beside it, full of eager, bouncy energy, completely silent throughout, ready for what comes next.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。**どちらのキャラクターも、このショット全体を通して一切話したり、喋ったり、発声したりすることはない——セリフ、発話、口パク、話しているように見える口の動きは一切なく、2人とも終始完全に無言のままで、すべてを言葉ではなく体の動き・表情だけで表現する。**それぞれのキャラクターの体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞う——この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——どちらのキャラクターも、体が回転できるのはこの軸のまわりだけである。コマやテーブルの上に横たわったコインのように、垂直な軸のまわりで平面的にその場で回転することは、どちらのキャラクターにとっても構造上不可能であり、どの瞬間にも一切起こらない。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、この固定された水平の軸のまわりを、まるで地面を転がる車輪のように端から端まで継続的に回転していく——現在上を向いている体の部分が前方・下方へ回転して床に面する部分になり、床に面していた部分が上方・後方へ回転して新しい上面になる——正面、そして背中、そしてまた正面、というのを進みながら一定のペースで途切れることなく回転し続ける。回転している間は常に体が水準を保ったまま回転し、その軸は決して斜めに傾いたり他の方向へずれたりすることはなく、この転がりの間は起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも、自分自身の固定された水平の軸のまわりを、まったく同じように——車輪のように端から端まで回転し、一回転するごとに上面と下面が着実かつ継続的に入れ替わり、軸は進行方向に対して常に垂直のままで、平面内でその場で回転することは一度もない——中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせて、それぞれの固定された水平の軸のまわりを回転しながら画面を右方向へ進んでいく。極めて重要な点として、画面外へ出ていく代わりに、2人とも画面のおおよそ中央に達したところで、回転を徐々にゆるめていき、そこで自然に穏やかに止まる——体を平らに仰向けにして、カメラの方(上)を向き、2人とも穏やかで嬉しそうな笑顔のまま、画面中央で並んで横たわる状態に落ち着く。カメラはこの間ずっと同じ俯瞰の位置に固定されたままで、一切動かない。しばらく穏やかに横たわった後、卵形のキャラクターはそのままの位置に留まり、仰向けに横たわったまま、リラックスして笑顔を保ち、起き上がろうとする素振りは一切見せない。同時に、透明なキャラクターだけが、**一言も声を出さず無言のまま**、突然の意欲的なエネルギーとともに起き上がり始める——**体の動きだけで、今にも動き出したいという意欲的で興奮した気持ちを伝える**——横たわった状態から、直立した、跳ねるような、いつでも動き出せそうな姿勢へと体を押し上げていく——体全体が遊び心のある熱意にあふれている。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は起き上がる動きに合わせて重力に従って体の底に自然に沈み、こぼれることは一切ない。ショットの終わりには、卵形のキャラクターは依然として仰向けに横たわり穏やかに笑っており、透明なキャラクターはそのすぐそばで直立し、意欲的で跳ねるようなエネルギーに満ち、**終始完全に無言のまま**、次の展開への準備が整っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v9.mp4`(未生成)
- 判定: 未検証
- メモ: 「歩いてではなく転がって中央へ」というご要望への対応版。転がりバージョンに
  戻しつつ、セリフを喋ってしまう不具合の対策(v8)は維持

### v8 (2026-09-15) — 旧版(歩き/弾みバージョン、セリフ対策は適用済み)

生成結果で、ぽよんが起き上がる際に「オールライ!レッツゴー!」と実際に声を出して
喋ってしまう不具合が発生。プロンプト内の引用符付きの台詞的な表現("alright, let's go!")
が、モデルにセリフ・音声として解釈されてしまったのが原因と考えられる。引用符付きの
台詞表現を完全に削除し、**セリフ・発話・音声は一切なしであることを明記**した。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion, and neither character spins, rolls, or tumbles at any point in this shot — all movement here is simple, natural walking and bouncing. Neither character ever speaks, talks, or makes any vocalization at any point in this entire shot — there is no dialogue, no speech, no mouthed words, and no lip movement suggesting speech at any point; both characters remain completely silent throughout, expressing everything purely through body language and expression, never through speech. Both characters move together toward the center of the frame in a cheerful, carefree, lighthearted mood, as if happily wondering what to do next — a relaxed, playful, unhurried little stroll rather than any kind of rush. The egg-shaped character toddles forward with small, bouncy steps, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point, its short arms swinging cheerfully with each step, its face wearing a bright, happy, carefree smile the whole time. Beside it, the transparent, jelly-like rubber character bounces along at the same cheerful, unhurried pace, its round body compressing gently downward and springing back up with each little bounce like a soft water balloon, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting and settling naturally at the bottom of its body under gravity with each bounce, never spilling out. Both continue this same cheerful, lighthearted pace together, side by side, moving steadily toward the middle of the frame. Once both characters reach roughly the center of the frame, they happily come to a stop there and playfully flop down onto their backs together, settling flat on the floor, face up toward the camera, both wearing calm, happy smiles, coming to rest side by side in the middle of the shot. After a brief calm moment lying there together, the egg character stays exactly where it is, remaining flat on its back the whole time, relaxed and still smiling, making no move to get up. At the same time, the transparent character alone begins to perk up with sudden, eager energy, silently and without speaking a single word — its body language alone conveying eager excitement, as if bursting to get moving — pushing itself up from lying flat into an upright, bouncy, ready-to-go posture, its whole body brimming with playful enthusiasm, its interior gumballs shifting and settling naturally at the bottom of its body under gravity as it rights itself, never spilling out. The shot ends with the egg character still lying flat on its back smiling calmly, and the transparent character upright beside it, full of eager, bouncy energy, completely silent throughout, ready for what comes next.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれ、このショットではどちらのキャラクターも回転・転がり・宙返りを一切しない——ここでの動きはすべてシンプルで自然な歩行と弾みのみである。**どちらのキャラクターも、このショット全体を通して一切話したり、喋ったり、発声したりすることはない——セリフ、発話、口パク、話しているように見える口の動きは一切なく、2人とも終始完全に無言のままで、すべてを言葉ではなく体の動き・表情だけで表現する。**2人とも、次に何をしようかと楽しそうに考えているかのような、るんるんとした気楽で明るい雰囲気で、画面中央へ向かって一緒に進んでいく——急ぐ様子は一切なく、リラックスした遊び心のある、のんびりとした散歩のような足取りである。卵形のキャラクターは小さく弾むような足取りでよちよちと進み、常につま先の先端だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらず、短い両腕は一歩ごとに楽しそうに揺れ、顔はずっと明るく気楽な笑顔を浮かべている。その隣では、透明でゼリーのようなラバーキャラクターが同じ気楽でのんびりとしたペースで弾みながら進み、水風船のように丸い体がやわらかく沈んでは弾んで戻る動きを一回ごとに繰り返し、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は弾むたびに重力に従って体の底に自然に沈み、こぼれることは一切ない。2人とも、この同じ明るくのんびりとしたペースのまま並んで、画面の中央へ向かって進み続ける。2人ともおおよそ画面中央に到達したところで、そこで嬉しそうに立ち止まり、一緒に楽しそうに仰向けにゴロンと寝転がり、体を床に平らに横たえて、カメラの方(上)を向き、2人とも穏やかで嬉しそうな笑顔のまま、画面中央で並んで横たわる状態に落ち着く。しばらく穏やかに横たわった後、卵形のキャラクターはそのままの位置に留まり、仰向けに横たわったまま、リラックスして笑顔を保ち、起き上がろうとする素振りは一切見せない。同時に、透明なキャラクターだけが、**一言も声を出さず無言のまま**、突然の意欲的なエネルギーとともに起き上がり始める——**体の動きだけで、今にも動き出したいという意欲的な興奮を伝える**——横たわった状態から、直立した、跳ねるような、いつでも動き出せそうな姿勢へと体を押し上げていく——体全体が遊び心のある熱意にあふれている。中のガムボールは起き上がる動きに合わせて重力に従って体の底に自然に沈み、こぼれることは一切ない。ショットの終わりには、卵形のキャラクターは依然として仰向けに横たわり穏やかに笑っており、透明なキャラクターはそのすぐそばで直立し、意欲的で跳ねるようなエネルギーに満ち、**終始完全に無言のまま**、次の展開への準備が整っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v8.mp4`(未生成)
- 判定: 未検証
- メモ: 「オールライ!レッツゴー!」と実際に喋ってしまう不具合の対策版。引用符付きの
  台詞的な表現をすべて削除し、「セリフ・発話・音声は一切なし」を明記した

### v7 (2026-09-15) — 旧版(引用符付きの台詞表現が原因で喋ってしまった)

回転(ごろごろ転がる)ではなく、**2人が「さあ次は何をしようか!」というような
るんるんと楽しい足取りで、俯瞰カメラの画面中央へ歩いて(弾んで)フレームインする**
方向に変更。カメラは終始俯瞰のまま固定。中央に到着した後は、v6と同じく
そのまま仰向けに寝転び、ぽよんだけ「よし、いくぞー!」と起き上がってE-1へ続く。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion, and neither character spins, rolls, or tumbles at any point in this shot — all movement here is simple, natural walking and bouncing. Both characters move together toward the center of the frame in a cheerful, carefree, lighthearted mood, as if happily wondering "what should we do next!" — a relaxed, playful, unhurried little stroll rather than any kind of rush. The egg-shaped character toddles forward with small, bouncy steps, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point, its short arms swinging cheerfully with each step, its face wearing a bright, happy, carefree smile the whole time. Beside it, the transparent, jelly-like rubber character bounces along at the same cheerful, unhurried pace, its round body compressing gently downward and springing back up with each little bounce like a soft water balloon, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting and settling naturally at the bottom of its body under gravity with each bounce, never spilling out. Both continue this same cheerful, lighthearted pace together, side by side, moving steadily toward the middle of the frame. Once both characters reach roughly the center of the frame, they happily come to a stop there and playfully flop down onto their backs together, settling flat on the floor, face up toward the camera, both wearing calm, happy smiles, coming to rest side by side in the middle of the shot. After a brief calm moment lying there together, the egg character stays exactly where it is, remaining flat on its back the whole time, relaxed and still smiling, making no move to get up. At the same time, the transparent character alone begins to perk up with sudden, eager energy — as if excitedly declaring "alright, let's go!" — pushing itself up from lying flat into an upright, bouncy, ready-to-go posture, its whole body brimming with playful enthusiasm, its interior gumballs shifting and settling naturally at the bottom of its body under gravity as it rights itself, never spilling out. The shot ends with the egg character still lying flat on its back smiling calmly, and the transparent character upright beside it, full of eager, bouncy energy, ready for what comes next.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれ、このショットではどちらのキャラクターも回転・転がり・宙返りを一切しない——ここでの動きはすべてシンプルで自然な歩行と弾みのみである。2人とも、「さあ次は何をしようか!」と楽しそうに考えているかのような、るんるんとした気楽で明るい雰囲気で、画面中央へ向かって一緒に進んでいく——急ぐ様子は一切なく、リラックスした遊び心のある、のんびりとした散歩のような足取りである。卵形のキャラクターは小さく弾むような足取りでよちよちと進み、常につま先の先端だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらず、短い両腕は一歩ごとに楽しそうに揺れ、顔はずっと明るく気楽な笑顔を浮かべている。その隣では、透明でゼリーのようなラバーキャラクターが同じ気楽でのんびりとしたペースで弾みながら進み、水風船のように丸い体がやわらかく沈んでは弾んで戻る動きを一回ごとに繰り返し、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は弾むたびに重力に従って体の底に自然に沈み、こぼれることは一切ない。2人とも、この同じ明るくのんびりとしたペースのまま並んで、画面の中央へ向かって進み続ける。2人ともおおよそ画面中央に到達したところで、そこで嬉しそうに立ち止まり、一緒に楽しそうに仰向けにゴロンと寝転がり、体を床に平らに横たえて、カメラの方(上)を向き、2人とも穏やかで嬉しそうな笑顔のまま、画面中央で並んで横たわる状態に落ち着く。しばらく穏やかに横たわった後、卵形のキャラクターはそのままの位置に留まり、仰向けに横たわったまま、リラックスして笑顔を保ち、起き上がろうとする素振りは一切見せない。同時に、透明なキャラクターだけが、まるで「よし、いくぞー!」と元気よく宣言するかのように、突然の意欲的なエネルギーとともに起き上がり始める——横たわった状態から、直立した、跳ねるような、いつでも動き出せそうな姿勢へと体を押し上げていく——体全体が遊び心のある熱意にあふれている。中のガムボールは起き上がる動きに合わせて重力に従って体の底に自然に沈み、こぼれることは一切ない。ショットの終わりには、卵形のキャラクターは依然として仰向けに横たわり穏やかに笑っており、透明なキャラクターはそのすぐそばで直立し、意欲的で跳ねるようなエネルギーに満ちて、次の展開への準備が整っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v7.mp4`(未生成)
- 判定: 未検証
- メモ: 転がり(回転)をやめ、るんるんとした歩き/弾みでフレームインする方向に
  変更。中央到着後の「仰向け→ぽよんだけ起き上がる」というE-1への継続部分はv6と同じ

### v6 (2026-09-15) — 旧版(転がってフレームイン→中央で停止)

Eビート(ジャンプ)への橋渡しとして、右へフレームアウトさせず**画面中央で転がりを
止め、2人とも仰向けに寝転んだ状態**で終わるよう変更。さらに、その仰向け状態から
**たまちゃんはゴロンとしたまま**、**ぽよんだけが「よし、いくぞー!」という
勢いのある様子で起き上がる**ところまでを追加。カメラは終始俯瞰のまま固定。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Each character's body behaves as if it were mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to the direction of travel — this axle is the only line either character's body is able to rotate around; neither character is capable of spinning around a vertical axis like a top or a coin lying flat on a table, that kind of flat, in-place spinning is structurally impossible for them and never happens at any point. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously rotates forward around this fixed horizontal axle, end over end, exactly like a wheel rolling along the ground: the point of its body currently facing up rotates forward and down to become the point facing the floor, while the point that was facing the floor rotates up and around to become the new top — front, then back, then front again, in a steady, continuous, unbroken rotation as it advances. It stays perfectly level as it rotates, its axle never tilting diagonally, never drifting off to point in any other direction, and it never rises up or stands during this rolling. Beside it on the left, the transparent, jelly-like rubber character rotates forward around its own fixed horizontal axle the exact same way — end over end like a wheel, its top and bottom steadily and continuously swapping places with each rotation, its axle staying perpendicular to its direction of travel the entire time, never once spinning flat in place — its interior gumballs and confetti shifting inside without ever spilling out. Both continue rotating forward together at a matched pace around their own fixed horizontal axles, moving steadily rightward across the frame. Critically, instead of exiting the frame, once both characters reach roughly the center of the frame, they gradually slow their rotation and come to a gentle, natural stop there, settling flat on their backs, face up toward the camera, both wearing calm, happy smiles, coming to rest side by side in the middle of the shot. The camera remains fixed in this same overhead position throughout, never moving. After a brief calm moment lying there together, the egg character stays exactly where it is, remaining flat on its back the whole time, relaxed and still smiling, making no move to get up. At the same time, the transparent character alone begins to perk up with sudden, eager energy — as if excitedly declaring "alright, let's go!" — pushing itself up from lying flat into an upright, bouncy, ready-to-go posture, its whole body brimming with playful enthusiasm, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting and settling naturally at the bottom of its body under gravity as it rights itself, never spilling out. The shot ends with the egg character still lying flat on its back smiling calmly, and the transparent character upright beside it, full of eager, bouncy energy, ready for what comes next.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。それぞれのキャラクターの体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞う——この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——どちらのキャラクターも、体が回転できるのはこの軸のまわりだけである。コマやテーブルの上に横たわったコインのように、垂直な軸のまわりで平面的にその場で回転することは、どちらのキャラクターにとっても構造上不可能であり、どの瞬間にも一切起こらない。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、この固定された水平の軸のまわりを、まるで地面を転がる車輪のように端から端まで継続的に回転していく——現在上を向いている体の部分が前方・下方へ回転して床に面する部分になり、床に面していた部分が上方・後方へ回転して新しい上面になる——正面、そして背中、そしてまた正面、というのを進みながら一定のペースで途切れることなく回転し続ける。回転している間は常に体が水準を保ったまま回転し、その軸は決して斜めに傾いたり他の方向へずれたりすることはなく、この転がりの間は起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも、自分自身の固定された水平の軸のまわりを、まったく同じように——車輪のように端から端まで回転し、一回転するごとに上面と下面が着実かつ継続的に入れ替わり、軸は進行方向に対して常に垂直のままで、平面内でその場で回転することは一度もない——中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせて、それぞれの固定された水平の軸のまわりを回転しながら画面を右方向へ進んでいく。**極めて重要な点として、画面外へ出ていく代わりに、2人とも画面のおおよそ中央に達したところで、回転を徐々にゆるめていき、そこで自然に穏やかに止まる——体を平らに仰向けにして、カメラの方(上)を向き、2人とも穏やかで嬉しそうな笑顔のまま、画面中央で並んで横たわる状態に落ち着く。カメラはこの間ずっと同じ俯瞰の位置に固定されたままで、一切動かない。**しばらく穏やかに横たわった後、卵形のキャラクターはそのままの位置に留まり、仰向けに横たわったまま、リラックスして笑顔を保ち、起き上がろうとする素振りは一切見せない。同時に、透明なキャラクターだけが、まるで「よし、いくぞー!」と元気よく宣言するかのように、突然の意欲的なエネルギーとともに起き上がり始める——横たわった状態から、直立した、跳ねるような、いつでも動き出せそうな姿勢へと体を押し上げていく——体全体が遊び心のある熱意にあふれている。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は起き上がる動きに合わせて重力に従って体の底に自然に沈み、こぼれることは一切ない。ショットの終わりには、卵形のキャラクターは依然として仰向けに横たわり穏やかに笑っており、透明なキャラクターはそのすぐそばで直立し、意欲的で跳ねるようなエネルギーに満ちて、次の展開への準備が整っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v6.mp4`(未生成)
- 判定: 未検証
- メモ: Eビートへの橋渡し版。フレームアウトの代わりに画面中央で停止→仰向け→
  たまちゃんはそのまま・ぽよんだけ「よしいくぞー!」と起き上がる、という
  E-1への継続を意識した終わり方に変更。E-1側の「2人とも起き上がる」という
  出だしは、この新しいD-1の終わり方(たまちゃんは仰向けのまま・ぽよんは
  すでに起き上がった状態)に合わせて後で調整が必要になる可能性あり

### v5 (2026-09-15) — 旧版(フレームアウトして終わる、Eビートへの継続なし)

「回転でいいです!」とのご要望を受け、v4の「固定された回転軸」の仕組みはそのまま
維持しつつ、①D-1-alt v2で確立した「顔は体表面の固定パーツとして体の回転と
一体で動く(見えなくなる/また見える)」という記述を両キャラクターに追加、
②回転のリズムに緩急をつけて楽しさを出す(速く回っては少しゆっくりになる、
を繰り返す)、③たまちゃんの上げた手が回転のたびに楽しそうにパタパタ揺れる、
という3点を加えた。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Each character's body behaves as if it were mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to the direction of travel — this axle is the only line either character's body is able to rotate around; neither character is capable of spinning around a vertical axis like a top or a coin lying flat on a table, that kind of flat, in-place spinning is structurally impossible for them and never happens at any point. Critically, each character's face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it. As each body rotates around its axle, its face rotates together with it as one single rigid piece: the face turns away and becomes hidden from view as that side rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face upward — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously rotates forward around this fixed horizontal axle, end over end, exactly like a wheel rolling along the ground: the point of its body currently facing up rotates forward and down to become the point facing the floor, while the point that was facing the floor rotates up and around to become the new top — front, then back, then front again, repeating as it advances. To make this fun and playful rather than mechanical, its rotation speed rises and falls in a bouncy, joyful rhythm — a couple of quicker, energetic rotations, then one slightly slower, more satisfying rotation, repeating this lively pattern the whole way — and with each rotation its two raised arms flop and flap cheerfully, swinging a little with the motion like it's having fun rolling along, without ever bending at any joint that would break its design. It stays perfectly level as it rotates, its axle never tilting diagonally, never drifting off to point in any other direction, and it never rises up or stands. Beside it on the left, the transparent, jelly-like rubber character rotates forward around its own fixed horizontal axle the exact same way — end over end like a wheel, its top and bottom steadily swapping places with each rotation, its axle staying perpendicular to its direction of travel the entire time, never once spinning flat in place — and it follows the same playful quick-quick-slow rhythm as the egg character, rolling with matched bouncy energy. Its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — tumble and jostle energetically with each rotation, clearly visible through its glossy transparent skin, without ever spilling out. Both continue rotating forward together at this same matched, playful pace around their own fixed horizontal axles, moving steadily rightward across the frame, until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。それぞれのキャラクターの体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞う——この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——どちらのキャラクターも、体が回転できるのはこの軸のまわりだけである。コマやテーブルの上に横たわったコインのように、垂直な軸のまわりで平面的にその場で回転することは、どちらのキャラクターにとっても構造上不可能であり、どの瞬間にも一切起こらない。**極めて重要な点として、それぞれのキャラクターの顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、体の一箇所に恒久的に付着している。それぞれの体が軸のまわりを回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周して再び上を向いたときにだけ顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。**ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、この固定された水平の軸のまわりを、まるで地面を転がる車輪のように端から端まで継続的に回転していく——現在上を向いている体の部分が前方・下方へ回転して床に面する部分になり、床に面していた部分が上方・後方へ回転して新しい上面になる——正面、そして背中、そしてまた正面、というのを進みながら繰り返す。**これを機械的にではなく楽しく遊び心のあるものにするため、回転の速さは楽しく弾むようなリズムで上下する**——2回ほど素早く元気な回転を行い、その後1回だけ少しゆっくりと、満足感のある回転をする、というこの生き生きとしたパターンを最後まで繰り返す——そして一回転するごとに、上げた両手が楽しそうにパタパタと揺れ、転がるのが楽しくてたまらないというように少し振られる(ただし、デザインを崩すような関節での曲がりは一切ない)。回転している間は常に体が水準を保ったまま回転し、その軸は決して斜めに傾いたり、他の方向へずれたりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも、自分自身の固定された水平の軸のまわりを、まったく同じように——車輪のように端から端まで回転し、一回転するごとに上面と下面が着実に入れ替わり、軸は進行方向に対して常に垂直のままで、平面内でその場で回転することは一度もない——そして卵形のキャラクターと同じ「速い・速い・ゆっくり」の楽しいリズムに合わせて、弾むような元気さで転がっていく。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は一回転するごとに元気よく転がりぶつかり合い、光沢のある透明な体を通してはっきりと見え、こぼれることは一切ない。二人はこのまま同じリズムを合わせながら、それぞれの固定された水平の軸のまわりを楽しく回転しつつ画面を右方向へまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v5.mp4`(未生成)
- 判定: 未検証
- メモ: 「回転でいいです!」とのご要望への対応版。v4の固定軸の仕組みを維持しつつ、
  顔の追従(D-1-alt v2の教訓)を両キャラクターに適用し、回転リズムに緩急・
  たまちゃんの手のパタパタ揺れを加えて楽しさを出した

### v4 (2026-09-15) — 旧版(「軸」を物理的な構造として明記、リズムの緩急なし)

v1〜v3の「でんぐり返し」「丸太」「コインフリップ」といった比喩がいずれも
不十分だったため、比喩ではなく**回転軸そのものを体に固定された物理構造として
明記**するアプローチに変更(F-5〜F-7で効果があった「足首の関節が存在しない」
という解剖学的制約の書き方と同じ考え方)。「縦回転以外は構造上できない」と
明示的に否定する一文も追加。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Each character's body behaves as if it were mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to the direction of travel — this axle is the only line either character's body is able to rotate around; neither character is capable of spinning around a vertical axis like a top or a coin lying flat on a table, that kind of flat, in-place spinning is structurally impossible for them and never happens at any point. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously rotates forward around this fixed horizontal axle, end over end, exactly like a wheel rolling along the ground: the point of its body currently facing up rotates forward and down to become the point facing the floor, while the point that was facing the floor rotates up and around to become the new top — front, then back, then front again, in a steady, continuous, unbroken rotation as it advances, never slowing to a glide, never pausing with its rotation stopped. It stays perfectly level as it rotates, its axle never tilting diagonally, never drifting off to point in any other direction, and it never rises up or stands. Beside it on the left, the transparent, jelly-like rubber character rotates forward around its own fixed horizontal axle the exact same way — end over end like a wheel, its top and bottom steadily and continuously swapping places with each rotation, its axle staying perpendicular to its direction of travel the entire time, never once spinning flat in place — its interior gumballs and confetti shifting inside without ever spilling out. Both continue rotating forward together at a matched pace around their own fixed horizontal axles, moving steadily rightward across the frame, until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。**それぞれのキャラクターの体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞う——この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——どちらのキャラクターも、体が回転できるのはこの軸のまわりだけである。コマやテーブルの上に横たわったコインのように、垂直な軸のまわりで平面的にその場で回転することは、どちらのキャラクターにとっても構造上不可能であり、どの瞬間にも一切起こらない。**ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、この固定された水平の軸のまわりを、まるで地面を転がる車輪のように端から端まで継続的に回転していく——現在上を向いている体の部分が前方・下方へ回転して床に面する部分になり、床に面していた部分が上方・後方へ回転して新しい上面になる——正面、そして背中、そしてまた正面、というのを進みながら一定のペースで途切れることなく回転し続け、決して速度を落として滑ったり、回転が止まったまま止まったりすることはない。回転している間は常に体が水準を保ったまま回転し、その軸は決して斜めに傾いたり、他の方向へずれたりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも、自分自身の固定された水平の軸のまわりを、まったく同じように——車輪のように端から端まで回転し、一回転するごとに上面と下面が着実かつ継続的に入れ替わり、軸は進行方向に対して常に垂直のままで、平面内でその場で回転することは一度もない——中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせて、それぞれの固定された水平の軸のまわりを回転しながら画面を右方向へまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v4.mp4`(未生成)
- 判定: 未検証
- メモ: 「もう一度作りたい」というリクエストへの対応版。比喩(でんぐり返し/丸太/
  コインフリップ)をやめ、回転軸を物理的な構造として明記するアプローチに変更

### v1 (2026-09-09) — 旧版(以下v1〜v3、すべて過去の試行錯誤の記録)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously somersaults forward across the floor in a straight, even cartwheel motion, its front and back alternating into view with each full turn — front, then back, then front again, repeating steadily as it advances — the same way a rolling ball toy tumbles forward end over end. It stays perfectly level as it tumbles, never tilting or wobbling off to one side or spinning diagonally, and it never rises up or stands. Beside it on the left, the transparent, jelly-like rubber character tumbles forward the same clean, even way, like a ball continuously rolling end over end, its own front and back alternating into view with each turn just as steadily, its interior gumballs and confetti shifting inside without ever spilling out. Both continue tumbling forward together at a matched pace, moving steadily rightward across the frame, until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、まっすぐで均等な前転(でんぐり返し)のような動きで床の上を継続的に前へ転がっていき、一回転するごとに正面と背中が交互に見える——正面、そして背中、そしてまた正面、というのを進みながら規則正しく繰り返す。ちょうど転がるボール型のおもちゃが端から端へ回転しながら進むのと同じ動きである。転がっている間は常に体が水平・水準を保ったまま転がり、決して片側に傾いたり、斜めに揺れたり、斜め回転したりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも同じように、ボールが端から端まで滑らかに転がるように前転し、こちらも一回転ごとに正面と背中が交互に規則正しく見え、中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせて前転を続けながら画面を右方向へまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v1.mp4`
- 判定: NG
- メモ: 体が「横に回転」(コマや円盤のように、床と平行な面の中でその場で回るような
  回転)になってしまった。欲しいのは「縦に回転」(丸太が地面を転がるように、
  進行方向に対して垂直な軸で前へ転がっていく回転)。→ v2で明確に書き分ける

### v2 (2026-09-09) — v1からの変更点: 「横回転(コマ状に平面内で回る)」と
「縦回転(丸太のように進行方向へ転がる)」の違いを明示的に対比して書き、
縦回転を強く指定した

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and rolls forward across the floor exactly like a log or a barrel rolling along the ground: its axis of rotation runs in a single straight horizontal line across its body, perpendicular to the direction it is traveling, so with each rotation its body pitches forward end-over-end, front tipping down and around to become back, then back tipping around to become front again — front, then back, then front again, repeating steadily as it advances. This is completely different from spinning flat like a coin or a top on a tabletop: the character never spins within the plane of the floor while staying in the same visual orientation, and its front and back must clearly and visibly alternate into view with each rotation, exactly as a rolling log shows its two ends alternating as it tumbles forward. It stays perfectly level as it tumbles, never tilting diagonally or wobbling off to one side, and it never rises up or stands. Beside it on the left, the transparent, jelly-like rubber character rolls forward the exact same way — end-over-end like a log rolling along the ground, its axis of rotation perpendicular to its direction of travel, its front and back clearly alternating into view with each turn, never spinning flat in place — its interior gumballs and confetti shifting inside without ever spilling out. Both continue rolling forward together at a matched pace, moving steadily rightward across the frame, until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、ちょうど丸太や樽が地面を転がるように床の上を前へ転がっていく——その回転軸は、体を横切る一本のまっすぐな水平線で、進行方向に対して垂直である。そのため一回転するごとに体が前方向へ端から端まで倒れ込むように回り、正面が下に倒れ込んで背中になり、また背中が倒れ込んで正面に戻る——正面、そして背中、そしてまた正面、というのを進みながら規則正しく繰り返す。これはテーブルの上でコマやコインが平らに回転するのとはまったく異なる動きである——床と同じ平面の中で、見た目の向きを保ったまま回転することは一切なく、正面と背中は一回転するごとにはっきりと目に見える形で入れ替わらなければならない。ちょうど転がる丸太が転がりながら両端を交互に見せるのと同じである。転がっている間は常に体が水準を保ったまま転がり、決して斜めに傾いたり片側に揺れたりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも、まったく同じように——丸太が地面を転がるように端から端まで回転し、回転軸は進行方向に対して垂直で、正面と背中が一回転するごとにはっきりと交互に見え、平面内でその場で回転することは一切ない——中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせて転がりながら画面を右方向へまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v2.mp4`
- 判定: NG
- メモ: 丸太のたとえがうまく伝わらなかった。ぽよんは相変わらず平面上でクルクル回転
  (コマ状)、たまちゃんはむしろ回転せず、蹴伸びのように地面を蹴っては滑る動きに
  なってしまった。→ v3で「丸太」の代わりに「コイン投げのように表と裏が交互に見える
  フリップ」という、より直感的なたとえに変更。「滑る/止まって進む」動きも明示的に禁止

### v3 (2026-09-09) — v1/v2からの変更点: 「丸太」のたとえをやめ、「コインを投げたときの
表裏が交互に見えるフリップ」に変更。あわせて、たまちゃんが蹴っては滑る動き(回転せず
移動する)を明示的に禁止する一文を追加

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously flips forward across the floor the same way a tossed coin flips through the air, showing its front face, then its back, then its front again in a steady, repeating cycle as it advances — never staying flat and spinning in one visual orientation the way a coin spins while lying down on a table. Its whole body is constantly flipping end-over-end this entire time; it is never sliding, coasting, or gliding smoothly across the floor with its rotation paused — there is no still or gliding phase at any point, only continuous, steady flipping the whole way. It stays perfectly level as it flips forward, never tilting diagonally or wobbling off to one side, and it never rises up or stands. Beside it on the left, the transparent, jelly-like rubber character flips forward the exact same way — its front and back steadily alternating into view with each flip, like a coin tumbling end-over-end, never spinning flat in one orientation and never pausing to glide — its interior gumballs and confetti shifting inside without ever spilling out. Both continue flipping forward together at a matched pace, moving steadily rightward across the frame, until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、投げたコインが空中でフリップするのと同じように、床の上を前へ継続的にフリップしていく——正面を見せ、次に背中を見せ、また正面を見せるというのを、進みながら規則正しく繰り返す——コインがテーブルの上に横たわったまま平らに回転するときのように、同じ向きを保ったまま平面で回転することは一切ない。体全体がこの間ずっと端から端までフリップし続けており、回転が止まって床の上を滑るように移動したり、なめらかに滑走したりすることは一切ない——止まる/滑る局面は一切なく、最初から最後まで一定のペースでフリップし続けるのみである。フリップしている間は常に体が水準を保ったまま前へ進み、決して斜めに傾いたり片側に揺れたりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも、まったく同じように——コインが端から端までフリップするように、一回転するごとに正面と背中が規則正しく交互に見え、同じ向きのまま平面で回転することも、途中で止まって滑ることも一切ない——中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせてフリップしながら画面を右方向へまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v3.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1(v10): 新しくいただいた画像(ぽよん回転中・たまちゃん立ち姿、画面右寄り、余白が左側)
- Picture 1(v4〜v9の旧版用): ぽよん左端寄り・たまちゃんその右、余白が右側
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 7秒目安(v10。ぽよんがジャンプ構えに入る分、やや長め)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- v10は「ぽよんが回転・たまちゃんがつま先歩き」という組み合わせで解釈した想定版。
  実際にたまちゃんも回転させたい場合は教えてください
- 回転が斜めになる/回転の向きがおかしいなど違和感があれば、その場でフィードバックをください
