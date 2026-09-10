---
project: H3-Video-Series-v2
cut: F-1
mode: I2VA
status: draft
---

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

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the transparent, jelly-like rubber character begins bouncing away to the right, playfully fleeing, while the egg-shaped character toddles after it in close pursuit, its short stiff legs never bending at the ankle and its heels never touching the ground. The egg character keeps toddling after it continuously, matching the transparent character's pace the whole time — it never comes to a stop, slows to a halt, or stands still while the transparent character is still visible and bouncing away; it keeps actively chasing right up until the transparent character disappears from view. The transparent character bounces further and further to the right until it bounces completely past the right edge of the frame and out of view, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. Only once the transparent character has fully exited past the right edge does the egg character finally reach that same spot and come to a stop there, looking around, momentarily puzzled, standing with its back toward the left edge of the frame. After a brief pause, the transparent character suddenly bounces back into view from the left edge of the frame, sneaking up right behind the egg character. Sensing something behind it, the egg character turns around — and upon spotting the transparent character right there behind it, bursts into delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. The transparent character bounces happily in place beside it, pleased with its own trick.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに逃げるように右方向へ弾み始め、卵形のキャラクターがそのすぐ後ろをよちよちと追いかける——短く硬い脚は足首で曲がることも、踵が地面につくこともない。卵形のキャラクターは透明なキャラクターのペースに合わせて**動き続け、途中で止まったり立ち止まったりすることは一切ない**——透明なキャラクターがまだ見えている間は、消えるその瞬間まで積極的に追いかけ続ける。透明なキャラクターはさらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。透明なキャラクターが完全に右端の外へ出ていって初めて、卵形のキャラクターもその場所にたどり着いて止まり、一瞬戸惑ったように辺りを見回し、画面左端に背を向けて立つ。少し間を置いて、透明なキャラクターが今度は画面左端から突然弾んで現れ、卵形のキャラクターのすぐ後ろに忍び寄る。何かが後ろにいる気配を感じた卵形のキャラクターが振り返る——そしてすぐ後ろに透明なキャラクターがいるのを見つけた瞬間、驚きと嬉しさの入り混じった笑い声を上げる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。透明なキャラクターはそのすぐ横で、いたずらが成功して満足そうに、その場で嬉しそうに弾んでいる。

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
