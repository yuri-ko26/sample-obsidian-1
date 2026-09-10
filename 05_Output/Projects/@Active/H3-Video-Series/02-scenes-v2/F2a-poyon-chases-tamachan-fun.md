---
project: H3-Video-Series-v2
cut: F-2a
mode: I2VA
status: draft
---

# カットF-2a: ぽよんがたまちゃんを楽しく追いかける→たまちゃんフレームアウト→ぽよんは追いかけ続ける

## シーン内容
Fビート(「雲の稜線おいかけっこ」)2回目の前半。F-1aと同じ流れを役割を入れ替えて。
正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(たまちゃん左・ぽよん右、並んで立っている)から、今度はたまちゃんが
   楽しそうに右方向へ走って逃げ始め、ぽよんがそのすぐ後ろを弾みながら追いかける
2. たまちゃんが画面右端まで逃げきり、完全にフレームアウトする
3. ぽよんは止まらず、追いかけている様子のまま弾み続ける
   (この続きはF-2bで、たまちゃんが後ろから登場して驚かす展開になる)

**表情は最初から最後まで「楽しく追いかけている」表情で統一**し、笑い等への表情切り替えは
一切行わない。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま走る
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

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the egg-shaped character begins toddling away to the right with real energy, playfully fleeing, its short stiff legs never bending at the ankle and always walking up on the very tips of its toes, its heels never touching the ground, while the transparent, jelly-like rubber character bounces after it in close pursuit, both characters wearing bright, happy, playful expressions throughout as if this is a fun game, and these expressions never change or transition at any point in the shot. The pastel cloud ridge beneath them is bumpy and uneven, and both characters move briskly over each bump in their path without ever slowing down. The transparent character keeps bouncing after the egg character continuously, matching its pace closely — it never comes to a stop or stands still while the egg character is still visible and fleeing; it keeps actively, happily chasing right up until the egg character disappears from view, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. The egg character toddles further and further to the right until it moves completely past the right edge of the frame and out of view, with the transparent character still visibly chasing not far behind it. Even once the egg character is no longer visible, the transparent character does not stop or settle down at all — it keeps bouncing forward determinedly toward the right edge, still chasing energetically as if still hot on the trail, glancing around eagerly while continuing its bouncing motion the whole time, never coming to a full standstill or a calm idle pose, its bright, happy expression unchanged from the very start of the shot to the very end; throughout this continued bouncing, its interior gumballs stay clearly visible through its glossy transparent skin, rolling and tumbling against each other and the inner wall with each bounce.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、卵形のキャラクターが元気よく楽しそうに逃げるように右方向へよちよちと走り始める——常につま先立ちのまま、短く硬い脚は足首で曲がることも、踵が地面につくこともない——一方、透明でゼリーのようなラバーキャラクターがそのすぐ後ろを弾みながら追いかける——2人とも終始明るく楽しそうな表情のままで、この表情はショットの間一切変化・切り替わりをしない。2人の足元にある雲の稜線はでこぼこと起伏があるが、2人とも速度を緩めることなく一つ一つの盛り上がりを乗り越えていく。透明なキャラクターは卵形のキャラクターのペースにほぼ合わせて弾み続け、途中で止まったり立ち止まったりすることは一切ない——卵形のキャラクターがまだ見えている間は、消えるその瞬間まで楽しそうに積極的に追いかけ続ける。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。卵形のキャラクターはさらに右へ右へと進んでいき、ついに画面右端を完全に越えて見えなくなる——その間も透明なキャラクターはすぐ後ろで追いかけ続ける様子がはっきり見えている。卵形のキャラクターが見えなくなっても、透明なキャラクターは決して止まったり落ち着いたりしない——まだ追跡中であるかのように、画面右端に向かって夢中で弾み続け、弾みながらきょろきょろと辺りを探し続け、完全に静止した落ち着いた姿勢に一切ならない——表情はショットの最初から最後まで、明るく楽しそうなまま一切変わらない。この弾み続けている間も、中のガムボールは光沢のある透明な体を通してずっとはっきりと見え、弾むたびにお互いや内壁にぶつかってころころと転がる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F2a_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 生成後、最終フレームをF-2bのPicture1として切り出して使用すること(ぽよん一人・右向きで弾んでいる途中の姿、たまちゃんは映っていない状態)

## ComfyUIでの設定メモ
- Picture 1: F-1と同じ画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 表情は最初から最後まで統一(笑いへの切り替え等は行わない)
