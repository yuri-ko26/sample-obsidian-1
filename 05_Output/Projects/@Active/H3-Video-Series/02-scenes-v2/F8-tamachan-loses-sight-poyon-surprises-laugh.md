---
project: H3-Video-Series-v2
cut: F-8
mode: FL2VA
status: draft
---

# カットF-8: たまちゃんがぽよんを見失いきょろきょろ探す→後ろからぽよんが登場して驚かす→2人で笑う

## シーン内容
新しい参照画像2枚(開始フレーム・終了フレーム)を使ったカット。ぽよんを見失った
たまちゃんがきょろきょろ探し、気づかないうちにぽよんが後ろに回り込んで「わっ!」と
驚かし、2人で笑い合うところまで。正面固定カメラ。

1. Picture1の状態(たまちゃんが紫/ピンクの雲の境目に立ち、控えめな笑顔。ぽよんは
   紫の雲の頂上付近に浮かんでいる)から始まる
2. たまちゃんが目を離した隙に、ぽよんはその場からそっと離れて見えなくなる
3. ぽよんが見当たらないことに気づいたたまちゃんは、辺りをきょろきょろと探し始める
   (不安ではなく、軽く気楽に/またはワクワくしながら探す)
4. たまちゃんが探すのに夢中になっている間に、ぽよんはこっそりたまちゃんの後ろに
   回り込む
5. ぽよんが後ろから「わっ!」と驚かす。たまちゃんはびっくりして振り返る
6. 2人とも大きく口を開けて嬉しそうに笑い合う。Picture2で示された通りの
   表情・構図で終わる

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。笑顔になっても崩れない
- きょろきょろ探す表情は**不安・心配ではなく軽く気楽/ワクワクした様子**にすること
  (F-5での教訓を踏襲)

## 参照画像
- Picture 1(最初のフレーム): いただいた画像。たまちゃんが紫/ピンクの雲の境目に
  立ち、控えめな笑顔。ぽよんは紫の雲の頂上付近に浮かび、笑っている
- Picture 2(最後のフレーム): いただいた画像。同じ構図で、たまちゃん・ぽよんとも
  大きく口を開けて嬉しそうに笑っている

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 7.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing at the boundary between the purple and pink clouds and the transparent, jelly-like rubber character hovering near the crest of the purple cloud, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. While the egg character is looking elsewhere for a moment, the transparent character quietly slips away from its spot near the purple cloud and disappears from view without making a sound. A moment later, the egg character turns back and notices the transparent character is no longer there, and begins looking around for it in a light, easygoing, cheerful way — its head and body turning to look this way and that, its round dot eyes glancing around with bright curiosity, its small mouth staying in a relaxed, pleasant expression; critically, this stays a relaxed, lighthearted kind of looking around, never becoming worried, anxious, or distressed in any way. It keeps casually looking around like this for several long moments, always balanced purely on the tips of its toes, its heels never touching any surface, with no sign of the transparent character reappearing anywhere yet. It is precisely because the egg character is so absorbed in this cheerful searching that it fails to notice the transparent character has quietly circled around behind it: the transparent character sneaks up from behind, approaching slowly and quietly, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — staying clearly visible, gently shifting and rolling against each other and the bottom of its body as it moves, its mouth remaining a thin, dark, uncolored outline throughout this approach, with absolutely no fill color of any kind inside it. Once right behind the still-searching egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — even in this sudden startled motion, its feet stay up on the very tips of its toes, its heels never touching the ground, its ankles not bending at any point — and upon spotting the transparent character right there, its light, cheerful expression instantly gives way to delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the exact same moment, the transparent character also breaks into a happy, wide-open laugh, its mouth opening into a big, joyful shape made of nothing but a thin dark outline — critically, this laughing mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline the whole time. By the end of the shot, both characters are laughing happily together, matching the exact positions, poses, and expressions shown in <Picture 2>.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の7.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターが紫とピンクの雲の境目に立ち、透明でゼリーのようなラバーキャラクターが紫の雲の頂上付近に浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。卵形のキャラクターが一瞬別の方を見ている間に、透明なキャラクターは音を立てずにそっと紫の雲のそばから離れ、見えなくなる。少し経って、卵形のキャラクターが振り返ると透明なキャラクターがもういないことに気づき、軽く朗らかな様子で辺りを探し始める——頭と体があちこちを向き、丸い点目は明るい好奇心とともに見回し、小さな口はリラックスした心地よい形のまま。極めて重要な点として、これはリラックスした軽い探し方のままであり、不安・心配・苦悩には一切ならない。卵形のキャラクターはこのように気楽に辺りを探す様子をかなり長い間続け、常につま先の先端だけでバランスを取り、踵はどんな面にも一切触れず、透明なキャラクターが再び現れる気配はまったくない。卵形のキャラクターがこうして朗らかに探すことに夢中になっているせいで、透明なキャラクターがすでにこっそり後ろに回り込んできたことにまったく気づかない——透明なキャラクターはゆっくり静かに後ろから忍び寄っていき、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——ははっきりと見え続け、動くたびにお互いや体の底とぶつかってやさしく転がる。この接近の間ずっと、口は薄く暗い無着色の輪郭線のままで、中には一切色が入らない。まだ探し続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——この突然の驚きの動作の間も、足は終始つま先の先端だけで浮いたままで、踵は地面に一切触れず、足首もどの瞬間も曲がらない——そしてすぐそこに透明なキャラクターがいるのを見つけた瞬間、軽く朗らかだった表情は一瞬で、驚きと嬉しさの入り混じった笑い声に変わる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。まったく同じ瞬間、透明なキャラクターも嬉しそうに大きく口を開けて笑う——口は薄い輪郭線だけでできた大きく喜びに満ちた形に開く——極めて重要な点として、この笑う口は、どの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。ショットの終わりには、2人とも一緒に嬉しそうに笑い合っており、<Picture 2>で示された通りの位置・ポーズ・表情とぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F8_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像(たまちゃん紫/ピンクの境目・控えめな笑顔、ぽよん紫の雲頂上付近で浮遊)
- Picture 2: いただいた画像(同じ構図で2人とも大きく口を開けて笑っている)
- モード: FL2VA
- 尺: 7秒目安(ぽよんが離れる1s/たまちゃんが気づき探す3s/ぽよんが後ろに回り込む1s/驚かす+笑う2s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: きょろきょろ探す表情は不安ではなく軽く朗らかに(F-5の教訓を踏襲)
