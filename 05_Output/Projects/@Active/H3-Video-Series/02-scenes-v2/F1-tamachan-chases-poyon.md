---
project: H3-Video-Series-v2
cut: F-1
mode: I2VA
status: superseded
---

> **status: superseded** — ぽよんの口に色がついてしまう不具合の再発を受け、
> 1カットにまとめず前後半に分割しました。以後はこちらを使用してください:
> - `F1a-tamachan-chases-poyon-fun.md`(楽しくおいかけっこ)
> - `F1b-poyon-surprises-tamachan.md`(後ろから登場で驚く)

# カットF-1: たまちゃんがぽよんを追いかける→ぽよんがフレームアウト→たまちゃんの後ろから出てくる→たまちゃんが振り返って笑う

## シーン内容
Fビート(「雲の稜線おいかけっこ」)の1回目。正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(たまちゃん左・ぽよん右、並んで立っている)から、たまちゃんがぽよんを
   追いかけ始める。ぽよんは右方向へ逃げるように弾みながら進み、たまちゃんがそのすぐ後ろを追う
2. ぽよんが画面右端まで逃げきり、完全にフレームアウトする
3. 少し間があって、今度はぽよんが**たまちゃんの後ろ側(画面左側)から**ひょっこり現れる
   (追いついたと思ったら反対側から回り込んでいた、という展開)
4. 気配に気づいたたまちゃんが振り返り、後ろにぽよんがいるのを見つけて驚き、嬉しそうに笑う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま追いかける
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)

## 参照画像
- Picture 1(最初のフレーム): 雲の稜線を横から見た構図。画面左にたまちゃん、
  右にぽよんが並んで立ち、どちらも通常の笑顔

## プロンプト履歴

### v1 (2026-09-10)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the transparent, jelly-like rubber character begins bouncing away to the right, playfully fleeing, while the egg-shaped character chases right after it with real urgency, its short stiff legs never bending at the ankle and its heels never touching the ground, moving as briskly as it possibly can. The pastel cloud ridge beneath them is bumpy and uneven, and the egg character determinedly clambers up and over each bump directly in its path without ever slowing its pursuit. Even moving as fast as it can, the egg character's short legs are still just a touch slower than the transparent character's bounces, so only a modest gap gradually opens between them the longer the chase goes on, and the egg character keeps closing distance with every stride it can manage. The egg character keeps chasing after it continuously despite this gap — it never comes to a stop, slows to a halt, or stands still while the transparent character is still visible and bouncing away; it keeps actively chasing right up until the transparent character disappears from view. The transparent character bounces onward to the right, a short distance ahead of the egg character, until it bounces completely past the right edge of the frame and out of view, with the egg character still visibly chasing not far behind it, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. Even once the transparent character is no longer visible, the egg character does not stop or settle down at all — it keeps toddling forward determinedly toward the right edge, still chasing desperately as if still hot on the trail, its short stiff legs still moving the whole time, never coming to a full standstill or a calm idle pose, facing away toward the right. It is precisely because the egg character is so absorbed in this relentless, still-moving chase that it fails to notice the transparent character has already circled back around: from the left edge of the frame, the transparent character quietly and slowly creeps back into view, approaching the egg character's back at a slow, sneaky pace, getting closer and closer without making a sound; even during this slow creep, its interior gumballs stay clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement. Once right behind the still-moving egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — and upon spotting the transparent character right there behind it, bursts into delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. The transparent character bounces happily in place beside it, pleased with its own successful surprise.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに逃げるように右方向へ弾み始め、卵形のキャラクターは短く硬い脚(足首で曲がらず、踵も地面につかない)を目一杯動かして、本気の勢いですぐ後ろを追いかける。2人の足元にある雲の稜線はでこぼこと起伏があり、卵形のキャラクターは追跡の速度を緩めることなく、行く手にある一つ一つの盛り上がりを懸命によじ登って越えていく。全力で追いかけていても、卵形のキャラクターの短い脚は弾んで進む透明なキャラクターにほんの少し及ばず、追いかけているうちに2人の間にはささやかな距離が少しずつ生まれていくが、卵形のキャラクターはできる限りその差を詰めようとし続ける。それでも卵形のキャラクターは、この距離にもめげずに**動き続け、途中で止まったり立ち止まったりすることは一切ない**——透明なキャラクターがまだ見えている間は、消えるその瞬間まで積極的に追いかけ続ける。透明なキャラクターは卵形のキャラクターの少し先を、さらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる——その間も卵形のキャラクターはすぐ後ろで追いかけ続ける様子がはっきり見えている。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。透明なキャラクターが見えなくなっても、卵形のキャラクターは決して止まったり落ち着いたりしない——まだ追跡中であるかのように、画面右端に向かって夢中でよちよちと進み続け、短く硬い脚はずっと動き続けたまま、完全に静止した落ち着いた姿勢に一切ならず、右を向いたままである。卵形のキャラクターがこうして一心不乱にまだ動き続けている追跡に夢中になっているせいで、透明なキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——画面左端から、透明なキャラクターが音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていき、少しずつ距離を詰めていく——このゆっくりとした忍び寄りの間も、中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。まだ動き続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——そしてすぐ後ろに透明なキャラクターがいるのを見つけた瞬間、驚きと嬉しさの入り混じった笑い声を上げる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。透明なキャラクターはそのすぐ横で、いたずらが成功して満足そうに、その場で嬉しそうに弾んでいる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 今回いただいた画像(雲の稜線、たまちゃん左・ぽよん右)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 10秒目安(追いかける→フレームアウト→間→反対側から登場→振り返り→笑いまで含むため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
