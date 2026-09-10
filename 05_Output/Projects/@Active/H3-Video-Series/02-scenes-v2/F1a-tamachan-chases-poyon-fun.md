---
project: H3-Video-Series-v2
cut: F-1a
mode: I2VA
status: superseded
---

> **status: superseded(2026-09-10)** — 分割すると後半カットでぽよんが別の生き物に
> 見えてしまう問題が発生したため撤回。**`F1-tamachan-chases-poyon.md`のv2(1カット版)
> を使用してください**。

# カットF-1a: たまちゃんがぽよんを楽しく追いかける→ぽよんフレームアウト→たまちゃんは追いかけ続ける

## シーン内容
Fビート(「雲の稜線おいかけっこ」)1回目の前半。F-1を前後半に分割したうちの「楽しく
おいかけっこ」パート。正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(たまちゃん左・ぽよん右、並んで立っている)から、たまちゃんがぽよんを
   楽しそうに追いかけ始める。ぽよんは右方向へ逃げるように弾みながら進み、たまちゃんが
   足元のでこぼこした雲を乗り越えながら本気で追う(足が遅い分、差は少しずつ開くが必死に詰めようとする)
2. ぽよんが画面右端まで逃げきり、完全にフレームアウトする
3. たまちゃんは立ち止まらず、ぽよんを追いかけている表情のまま右へ向かって動き続ける
   (この続きはF-1bで、ぽよんが後ろから登場して驚かす展開になる)

**表情は最初から最後まで「楽しく追いかけている」表情で統一**し、笑い等への表情切り替えは
一切行わない(表情切り替え時にデザインが崩れる問題を避けるため)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま追いかける
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)

## 参照画像
- Picture 1(最初のフレーム): 雲の稜線を横から見た構図。画面左にたまちゃん、
  右にぽよんが並んで立ち、どちらも通常の笑顔(F-1と同じ画像)

## プロンプト履歴

### v1 (2026-09-10)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the transparent, jelly-like rubber character begins bouncing away to the right, playfully fleeing, while the egg-shaped character chases right after it with real urgency, its short stiff legs never bending at the ankle and always walking up on the very tips of its toes, its heels never touching the ground, moving as briskly as it possibly can, both characters wearing bright, happy, playful expressions throughout as if this is a fun game, and these expressions never change or transition at any point in the shot. The pastel cloud ridge beneath them is bumpy and uneven, and the egg character determinedly clambers up and over each bump directly in its path without ever slowing its pursuit. Even moving as fast as it can, the egg character's short legs are still just a touch slower than the transparent character's bounces, so only a modest gap gradually opens between them the longer the chase goes on, and the egg character keeps closing distance with every stride it can manage. The egg character keeps chasing after it continuously despite this gap — it never comes to a stop, slows to a halt, or stands still while the transparent character is still visible and bouncing away; it keeps actively, happily chasing right up until the transparent character disappears from view. The transparent character bounces onward to the right, a short distance ahead of the egg character, until it bounces completely past the right edge of the frame and out of view, with the egg character still visibly chasing not far behind it, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. Even once the transparent character is no longer visible, the egg character does not stop or settle down at all — it keeps toddling forward determinedly toward the right edge, still chasing energetically as if still hot on the trail, its short stiff legs still moving the whole time, never coming to a full standstill or a calm idle pose, facing away toward the right, its bright, happy expression unchanged from the very start of the shot to the very end.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに逃げるように右方向へ弾み始め、卵形のキャラクターは常につま先立ちのまま、短く硬い脚(足首で曲がらず、踵は絶対に地面につかない)を目一杯動かして、本気の勢いですぐ後ろを追いかける——2人とも終始明るく楽しそうな表情のままで、この表情はショットの間一切変化・切り替わりをしない。2人の足元にある雲の稜線はでこぼこと起伏があり、卵形のキャラクターは追跡の速度を緩めることなく、行く手にある一つ一つの盛り上がりを懸命によじ登って越えていく。全力で追いかけていても、卵形のキャラクターの短い脚は弾んで進む透明なキャラクターにほんの少し及ばず、追いかけているうちに2人の間にはささやかな距離が少しずつ生まれていくが、卵形のキャラクターはできる限りその差を詰めようとし続ける。それでも卵形のキャラクターは、この距離にもめげずに動き続け、途中で止まったり立ち止まったりすることは一切ない——透明なキャラクターがまだ見えている間は、消えるその瞬間まで楽しそうに積極的に追いかけ続ける。透明なキャラクターは卵形のキャラクターの少し先を、さらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる——その間も卵形のキャラクターはすぐ後ろで追いかけ続ける様子がはっきり見えている。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。透明なキャラクターが見えなくなっても、卵形のキャラクターは決して止まったり落ち着いたりしない——まだ追跡中であるかのように、画面右端に向かって夢中でよちよちと進み続け、短く硬い脚はずっと動き続けたまま、完全に静止した落ち着いた姿勢に一切ならず、右を向いたままである。表情はショットの最初から最後まで、明るく楽しそうなまま一切変わらない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1a_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 生成後、最終フレームをF-1bのPicture1として切り出して使用すること(たまちゃん一人・右向きで動いている途中の姿、ぽよんは映っていない状態)

## ComfyUIでの設定メモ
- Picture 1: F-1と同じ画像(雲の稜線、たまちゃん左・ぽよん右)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安(追いかける→フレームアウト→追いかけ続けるまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 表情は最初から最後まで統一(笑いへの切り替え等は行わない)
