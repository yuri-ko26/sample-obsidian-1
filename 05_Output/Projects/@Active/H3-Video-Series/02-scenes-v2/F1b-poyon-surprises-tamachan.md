---
project: H3-Video-Series-v2
cut: F-1b
mode: I2VA
status: draft
---

# カットF-1b: ぽよんがたまちゃんの後ろから登場して驚かす→たまちゃんが振り返って笑う

## シーン内容
Fビート(「雲の稜線おいかけっこ」)1回目の後半。F-1a(楽しくおいかけっこ)の続き。
正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(たまちゃんが一人、右向きでまだ追いかけている途中の姿。ぽよんは
   画面に映っていない)から、たまちゃんは気づかずそのまま動き続ける
2. たまちゃんの後ろ(画面左側)から、ぽよんがゆっくりこっそり登場し忍び寄る
3. ぽよんがたまちゃんのすぐ後ろまで来たところで、勢いよく前に飛び出して「わっ!」と驚かす
4. 気配に気づいたたまちゃんが振り返り、後ろにぽよんがいるのを見つけて驚き、嬉しそうに笑う。
   ぽよんも嬉しそうにその場で弾む

**表情切り替えはこのカットの最後、たまちゃんが振り返って笑う一回のみに限定**し、
それ以外の場面では表情を変化させない(表情切り替え時にデザインが崩れる問題を避けるため)。
**ぽよんの口は、笑顔になる瞬間も含めて常に輪郭線のみ・無着色のまま**であることを
強く明記する(口の中に色がついてしまう不具合の再発防止)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま動く
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。これは表情が変わっても絶対に崩れない

## 参照画像
- Picture 1(最初のフレーム): F-1aの実際の最終フレームを切り出したもの。
  たまちゃんが画面右寄りで一人、右向きにまだ動いている途中の姿(ぽよんは映っていない)

## プロンプト履歴

### v1 (2026-09-10)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>, with only the egg-shaped character visible, still mid-stride facing right as if still chasing something, and no other character in view. The egg character keeps its exact appearance and design from <Picture 1> unchanged throughout, with no distortion, and never has eyebrows at any point. The egg character continues toddling forward toward the right, still moving continuously, still chasing energetically as if still hot on the trail, its short stiff legs never bending at the ankle and its heels never touching the ground, never coming to a full standstill, its expression unchanged and neutral-happy throughout this part of the shot. It is precisely because the egg character is so absorbed in this relentless, still-moving chase that it fails to notice the transparent, jelly-like rubber character has already circled back around: from the left edge of the frame, the transparent character quietly and slowly creeps back into view, approaching the egg character's back at a slow, sneaky pace, getting closer and closer without making a sound; even during this slow creep, its interior gumballs stay clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti, never floating motionless in mid-air and never appearing stuck together. Throughout this entire creep, the transparent character's mouth remains completely closed and neutral, a thin dark outline only, with absolutely no fill color of any kind inside it. Once right behind the still-moving egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — and upon spotting the transparent character right there behind it, this is the one and only expression change in the entire shot: the egg character bursts into delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the same moment, the transparent character also breaks into a happy smile, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — this smiling mouth stays exactly as transparent and see-through as the rest of its glossy body, with absolutely no color, tint, or fill of any kind appearing inside it at any point, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline the whole time. The transparent character bounces happily in place beside the egg character, pleased with its own successful surprise, its mouth-outline staying just as thin, uncolored, and transparent as ever even as it bounces.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映しており、卵形のキャラクターだけが右向きでまだ何かを追いかけているように動いている途中の姿で映っており、他のキャラクターは映っていない。卵形のキャラクターは<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれ、どの瞬間も眉毛はつかない。卵形のキャラクターは右へ向かってよちよちと動き続け、まだ夢中で追いかけているかのように、短く硬い脚(足首で曲がらず、踵も地面につかない)を止めることなく動かし続け、完全に静止することは一切ない——このパートの間、表情は変化せず中立的で楽しそうな表情のままである。卵形のキャラクターがこうして一心不乱にまだ動き続けている追跡に夢中になっているせいで、透明なキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——画面左端から、透明なキャラクターが音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていき、少しずつ距離を詰めていく——このゆっくりとした忍び寄りの間も、中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は、宙に浮いたまま静止したりくっついて見えたりすることは一切ない。この忍び寄りの間ずっと、透明なキャラクターの口は完全に閉じた中立の状態のままで、薄い輪郭線のみであり、中には一切色が入らない。まだ動き続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——そしてすぐ後ろに透明なキャラクターがいるのを見つけた瞬間、これがこのショット全体で唯一の表情変化となる:卵形のキャラクターは驚きと嬉しさの入り混じった笑い声を上げ、丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。同じ瞬間、透明なキャラクターも嬉しそうな笑顔になる——口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——この笑顔の口は、光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・着色・塗りつぶしが入らず、開いた口の輪郭線を通して中の正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個)のガムボールとカラフルな紙吹雪がそのままはっきりと見え続ける。透明なキャラクターは卵形のキャラクターのすぐ横で、いたずらが成功して満足そうに、その場で嬉しそうに弾む——弾んでいる間も、その口の輪郭線は薄く無着色で透明なままである。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1b_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: F-1aの実際の最終フレームを切り出した画像(たまちゃん一人・右向き・ぽよん不在)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 5〜6秒目安(忍び寄り→驚かす→振り返り→笑いまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 表情切り替えはラストの一回のみ。ぽよんの口の無着色・透明指定は特に強く効かせること
