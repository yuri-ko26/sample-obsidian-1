---
project: H3-Video-Series-v2
cut: F-2
mode: I2VA
status: draft
---

# カットF-2: 今度はぽよんがたまちゃんを追いかける(F-1と同じ展開を反対の役割で)

## シーン内容
Fビート(「雲の稜線おいかけっこ」)の2回目。F-1と同じ流れを、追いかける側と
逃げる側を入れ替えて繰り返す。正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(たまちゃん左・ぽよん右、並んで立っている)から、今度は**ぽよんが
   たまちゃんを追いかける**。たまちゃんは右方向へ逃げるように走り、ぽよんがそのすぐ
   後ろを弾みながら追う
2. たまちゃんが画面右端まで逃げきり、完全にフレームアウトする
3. 少し間があって、今度はたまちゃんが**ぽよんの後ろ側(画面左側)から**ひょっこり現れる
4. 気配に気づいたぽよんが振り返り、後ろにたまちゃんがいるのを見つけて驚き、嬉しそうに笑う

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

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the egg-shaped character begins toddling away to the right, playfully fleeing, its short stiff legs never bending at the ankle and its heels never touching the ground, while the transparent, jelly-like rubber character bounces after it in close pursuit. The transparent character keeps bouncing after it continuously, matching the egg character's pace the whole time — it never comes to a stop or stands still while the egg character is still visible and fleeing; it keeps actively chasing right up until the egg character disappears from view, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. The egg character toddles further and further to the right until it moves completely past the right edge of the frame and out of view. Even once the egg character is no longer visible, the transparent character does not stop or settle down at all — it keeps bouncing forward determinedly toward the right edge, still chasing energetically as if still hot on the trail, glancing around eagerly while continuing its bouncing motion the whole time, never coming to a full standstill or a calm idle pose. It is precisely because the transparent character is so absorbed in this relentless, still-moving chase that it fails to notice the egg character has already circled back around: the egg character suddenly reappears from the left edge of the frame, sneaking up right behind the transparent character while it is still mid-bounce, facing the wrong way. Sensing something behind it, the transparent character turns to look — and upon spotting the egg character right there behind it, its round eyes crinkle shut into laughing crescents while its mouth curves into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline, staying just as transparent and see-through as its glossy skin so its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — remain clearly visible straight through the open mouth outline. The egg character stands happily beside it, pleased with its own trick, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、卵形のキャラクターが楽しそうに逃げるように右方向へよちよちと走り始める——短く硬い脚は足首で曲がることも、踵が地面につくこともない——一方、透明でゼリーのようなラバーキャラクターがそのすぐ後ろを弾みながら追いかける。透明なキャラクターは卵形のキャラクターのペースに合わせて**弾み続け、途中で止まったり立ち止まったりすることは一切ない**——卵形のキャラクターがまだ見えている間は、消えるその瞬間まで積極的に追いかけ続ける。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。卵形のキャラクターはさらに右へ右へと進んでいき、ついに画面右端を完全に越えて見えなくなる。卵形のキャラクターが見えなくなっても、透明なキャラクターは決して止まったり落ち着いたりしない——まだ追跡中であるかのように、画面右端に向かって夢中で弾み続け、弾みながらきょろきょろと辺りを探し続け、完全に静止した落ち着いた姿勢に一切ならない。透明なキャラクターがこうして一心不乱にまだ動き続けている追跡に夢中になっているせいで、卵形のキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——卵形のキャラクターが画面左端から突然現れ、まだ弾み続けている透明なキャラクターの、向きを間違えたそのすぐ後ろに忍び寄る。何かが後ろにいる気配を感じた透明なキャラクターが振り返る——そしてすぐ後ろに卵形のキャラクターがいるのを見つけた瞬間、丸い目はぎゅっと閉じて笑いじわの三日月形になり、口はほどよい広さの、やわらかなカーブの笑顔になる——顔の横幅の3分の1程度までしか開かず、薄い輪郭線だけでできていて、光沢のある体の表面とまったく同じように透き通ったままなので、中の正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪が、開いた口の輪郭線を通してそのままはっきり透けて見える。卵形のキャラクターはそのすぐ横で、いたずらが成功して満足そうに嬉しそうに立ち、丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F2_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: F-1と同じ画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 10秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
