---
project: H3-Video-Series-v2
cut: E-1
mode: I2VA
status: draft
---

# カットE-1: 俯瞰、たまちゃんは仰向けのまま・ぽよんはすでに起き上がった状態から、ぴょんぴょん弾んでから一人で大きくジャンプする

## シーン内容
Eビート(「ジャンプ」)の最初のカット。D-1(v6)の続き。俯瞰固定カメラ、D-1の終わりの
状態(たまちゃんは仰向けに寝転んだまま、ぽよんはすでに「よし、いくぞー!」という
勢いで起き上がっている)から始まる。

1. Picture1の状態(たまちゃんは仰向けのまま、ぽよんはすでに直立している)からスタート
   (起き上がる動作は不要。D-1側ですでに完了しているため)
2. ぽよんがおもむろに(特に構えることなく)その場でぴょんぴょんと軽く弾み始める
3. 数回軽く弾んだ後、ぽよんは一人で大きく真上にジャンプする(たまちゃんは仰向けに
   寝転んだまま、体を起こさずにぽよんの様子を見ている)

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんが起き上がる動き:踵をつけず、足首を曲げない棒状の足のまま、硬い腕で体を押し上げる
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  これ以外は増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材、中のガムボールが透けて見える)

## 参照画像
- Picture 1(最初のフレーム): 俯瞰、薄い黄緑色の床。たまちゃんは仰向けに寝転んで
  笑顔のまま、ぽよんはそのすぐそばで「よし、いくぞー!」という勢いのある様子で
  すでに直立している構図(D-1 v6の最終フレーム)

## プロンプト履歴

### v2 (2026-09-15) — 現在の採用版(D-1 v6の新しい終わり方に合わせて「起き上がる」動作を削除)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>, where the egg-shaped character lies resting calmly on its back, smiling, and the transparent, jelly-like rubber character already stands upright beside it, full of eager, bouncy energy. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character makes no move to get up at any point in this shot — it stays flat on its back the whole time, relaxed and smiling, its short, stiff arms and legs never bending at any joint that would break its design, its heels never touching anything since it never stands. The transparent character, already standing, casually begins bouncing lightly in place, without any particular build-up, its round body compressing gently downward and springing back up each time like a soft water balloon, its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting inside without ever spilling out. It bounces this way exactly two times only — one, two, and no more than two small bounces in total — in a steady rhythm, then on the third beat it gathers itself and launches into one big solo jump straight upward, rising much higher than the two small bounces before it, its body stretching slightly taller as it leaves the ground. After reaching the peak of this big jump, it fully descends back down under gravity, its body compressing slightly as it lands back on the floor in the same spot right beside the egg character where it started, settling back into its normal round resting shape once it comes to rest on the ground. The egg character stays lying flat on its back the entire time, watching the transparent character with wide-eyed, fascinated curiosity as it bounces exactly twice, jumps, and comes all the way back down to land beside it again, its round dot eyes following the motion intently from launch to landing, without ever sitting up or rising from the floor.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、卵形のキャラクターは仰向けに寝転んで穏やかに笑い、透明でゼリーのようなラバーキャラクターはそのすぐそばで、意欲的で跳ねるようなエネルギーに満ちてすでに直立している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターはこのショットの間、起き上がろうとする素振りを一切見せない——仰向けに寝転んだまま、リラックスして笑顔を保ち、短く硬い腕や脚はデザインを崩すような関節での曲がりを一切見せず、立つことがないため踵が何かに触れることもない。すでに立っている透明なキャラクターは、特に構えることなく、おもむろにその場で軽く弾み始める——水風船のように体がやわらかく沈んでは弾んで戻る動きを繰り返し、中の正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は揺れ動くがこぼれることはない。この軽い弾みをちょうど2回だけ(1回、2回、それ以上は増やさない)、一定のリズムで繰り返し、3回目のタイミングで勢いをためて、真上に向かって一人で大きくジャンプする——それまでの2回の小さな弾みよりもはるかに高く上がり、地面を離れる瞬間には体が少し縦に伸びる。ジャンプの頂点に達したあとは、重力に従ってしっかりと最後まで下降し、体を少し圧縮させながら、最初にいたのと同じ場所、卵形のキャラクターのすぐ横に着地して、地面に落ち着いたところで通常の丸い休息姿勢に戻る。卵形のキャラクターはその間ずっと仰向けに寝転んだままで、丸い点目でその動きをじっと追いながら、興味津々といった様子で透明なキャラクターがちょうど2回弾んでからジャンプし、最後まで降りてきて再び自分の横に着地するまでを見つめている——一度も体を起こしたり床から立ち上がったりすることはない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E1_v2.mp4`(未生成)
- 判定: 未検証
- メモ: D-1 v6の新しい終わり方(たまちゃんは仰向けのまま・ぽよんはすでに起き上がり
  済み)に合わせて、冒頭の「2人とも起き上がる」動作を削除。たまちゃんは最後まで
  仰向けのまま、ぽよんの様子を見つめる形に変更

### v1 (2026-09-09) — 旧版(冒頭に「2人とも起き上がる」動作があった、D-1旧バージョン向け)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>, where the transparent, jelly-like rubber character and the egg-shaped character both lie resting on their backs. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Both characters push themselves upright: the egg character braces its short, stiff, non-bending arms against the floor and rises back onto its feet, wobbling slightly as it finds its balance, its heels never touching the ground and its legs never bending at the ankle, while the transparent character rounds itself back up into its normal upright resting position beside it. Once both are standing, the transparent character casually begins bouncing lightly in place, without any particular build-up, its round body compressing gently downward and springing back up each time like a soft water balloon, its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting inside without ever spilling out. It bounces this way exactly two times only — one, two, and no more than two small bounces in total — in a steady rhythm, then on the third beat it gathers itself and launches into one big solo jump straight upward, rising much higher than the two small bounces before it, its body stretching slightly taller as it leaves the ground. After reaching the peak of this big jump, it fully descends back down under gravity, its body compressing slightly as it lands back on the floor in the same spot right beside the egg character where it started, settling back into its normal round resting shape once it comes to rest on the ground. The egg character stays standing in place the whole time, watching the transparent character with wide-eyed, fascinated curiosity as it bounces exactly twice, jumps, and comes all the way back down to land beside it again, its round dot eyes following the motion intently from launch to landing.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターがどちらも仰向けに寝そべっている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。2人とも体を起こす——卵形のキャラクターは短く硬い曲がらない腕を床について足で立ち上がり、少しぐらつきながらバランスを取る。踵は地面につかず、足首が曲がることもない。一方、透明なキャラクターはそのそばで、通常の直立した休息姿勢に体を丸めて戻る。2人とも立ち上がったところで、透明なキャラクターは特に構えることなく、おもむろにその場で軽く弾み始める——水風船のように体がやわらかく沈んでは弾んで戻る動きを繰り返し、中の正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は揺れ動くがこぼれることはない。この軽い弾みを**ちょうど2回だけ**(1回、2回、それ以上は増やさない)、一定のリズムで繰り返し、3回目のタイミングで勢いをためて、真上に向かって一人で大きくジャンプする——それまでの2回の小さな弾みよりもはるかに高く上がり、地面を離れる瞬間には体が少し縦に伸びる。ジャンプの頂点に達したあとは、重力に従ってしっかりと最後まで下降し、体を少し圧縮させながら、最初にいたのと同じ場所、卵形のキャラクターのすぐ横に着地して、地面に落ち着いたところで通常の丸い休息姿勢に戻る。卵形のキャラクターはその間ずっとその場に立ったまま、丸い点目でその動きをじっと追いながら、興味津々といった様子で透明なキャラクターがちょうど2回弾んでからジャンプし、最後まで降りてきて再び自分の横に着地するまでを見つめている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: **D-1 v6の実際の最終フレーム**(たまちゃんは仰向け、ぽよんはすでに直立)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: **9秒目安**(v2で「起き上がる」動作が不要になったため11秒→9秒に短縮。
  内訳目安: 2回弾む2s/3回目の大ジャンプで上昇1.5s/頂点〜降下〜着地3s/着地後の余韻2.5s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
