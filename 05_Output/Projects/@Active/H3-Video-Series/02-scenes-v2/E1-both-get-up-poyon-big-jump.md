---
project: H3-Video-Series-v2
cut: E-1
mode: I2VA
status: draft
---

# カットE-1: 俯瞰、2人が仰向けから起き上がり、ぽよんがぴょんぴょん弾んでから一人で大きくジャンプする

## シーン内容
Eビート(「ジャンプ」)の最初のカット。Dビート(往復の転がり)の続き。俯瞰固定カメラ、
2人とも仰向けに寝ている状態から始まる。

1. 2人とも仰向けの状態から起き上がる(カメラは俯瞰のまま動かない)
2. 起き上がったところで、ぽよんがおもむろに(特に構えることなく)その場でぴょんぴょんと
   軽く弾み始める
3. 数回軽く弾んだ後、ぽよんは一人で大きく真上にジャンプする(たまちゃんはこの時点では
   まだ何もせず、ぽよんの様子を見ている)

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんが起き上がる動き:踵をつけず、足首を曲げない棒状の足のまま、硬い腕で体を押し上げる
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  これ以外は増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材、中のガムボールが透けて見える)

## 参照画像
- Picture 1(最初のフレーム): 俯瞰、薄い黄緑色の床。左にぽよん、右にたまちゃんが
  ともに仰向けに寝ている構図(Dビートの往復転がりの続きの状態)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>, where the transparent, jelly-like rubber character and the egg-shaped character both lie resting on their backs. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Both characters push themselves upright: the egg character braces its short, stiff, non-bending arms against the floor and rises back onto its feet, wobbling slightly as it finds its balance, its heels never touching the ground and its legs never bending at the ankle, while the transparent character rounds itself back up into its normal upright resting position beside it. Once both are standing, the transparent character casually begins bouncing lightly in place, without any particular build-up, its round body compressing gently downward and springing back up each time like a soft water balloon, its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting inside without ever spilling out. It bounces this way exactly three times in a steady rhythm, then on the fourth beat it gathers itself and launches into one big solo jump straight upward, rising much higher than the three small bounces before it, its body stretching slightly taller as it leaves the ground. After reaching the peak of this big jump, it fully descends back down under gravity, its body compressing slightly as it lands back on the floor in the same spot right beside the egg character where it started, settling back into its normal round resting shape once it comes to rest on the ground. The egg character stays standing in place the whole time, watching the transparent character with wide-eyed, fascinated curiosity as it bounces three times, jumps, and comes all the way back down to land beside it again, its round dot eyes following the motion intently from launch to landing.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターがどちらも仰向けに寝そべっている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。2人とも体を起こす——卵形のキャラクターは短く硬い曲がらない腕を床について足で立ち上がり、少しぐらつきながらバランスを取る。踵は地面につかず、足首が曲がることもない。一方、透明なキャラクターはそのそばで、通常の直立した休息姿勢に体を丸めて戻る。2人とも立ち上がったところで、透明なキャラクターは特に構えることなく、おもむろにその場で軽く弾み始める——水風船のように体がやわらかく沈んでは弾んで戻る動きを繰り返し、中の正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は揺れ動くがこぼれることはない。この軽い弾みをちょうど3回、一定のリズムで繰り返し、4回目のタイミングで勢いをためて、真上に向かって一人で大きくジャンプする——それまでの3回の小さな弾みよりもはるかに高く上がり、地面を離れる瞬間には体が少し縦に伸びる。ジャンプの頂点に達したあとは、重力に従ってしっかりと最後まで下降し、体を少し圧縮させながら、最初にいたのと同じ場所、卵形のキャラクターのすぐ横に着地して、地面に落ち着いたところで通常の丸い休息姿勢に戻る。卵形のキャラクターはその間ずっとその場に立ったまま、丸い点目でその動きをじっと追いながら、興味津々といった様子で透明なキャラクターが3回弾んでからジャンプし、最後まで降りてきて再び自分の横に着地するまでを見つめている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 今回いただいた画像(俯瞰、2人とも仰向け)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 11秒目安(起き上がる→3回弾む→大ジャンプ→着地までしっかり含むため。8秒だと
  頂点で尺が足りなくなる可能性があるため延長)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
