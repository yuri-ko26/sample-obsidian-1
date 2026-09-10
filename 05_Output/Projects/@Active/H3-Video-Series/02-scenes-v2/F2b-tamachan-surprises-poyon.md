---
project: H3-Video-Series-v2
cut: F-2b
mode: I2VA
status: superseded
---

> **status: superseded(2026-09-10)** — F-1bと同じ理由(分割時のキャラクター一貫性
> 問題)で撤回。**`F2-poyon-chases-tamachan.md`のv2(1カット版)を使用してください**。

# カットF-2b: たまちゃんがぽよんの後ろから登場して驚かす→ぽよんが振り返って笑う

## シーン内容
Fビート(「雲の稜線おいかけっこ」)2回目の後半。F-2a(楽しくおいかけっこ)の続き。
正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(ぽよんが一人、右向きでまだ弾んで追いかけている途中の姿。たまちゃんは
   画面に映っていない)から、ぽよんは気づかずそのまま弾み続ける
2. ぽよんの後ろ(画面左側)から、たまちゃんがこっそり登場し忍び寄る
3. たまちゃんがぽよんのすぐ後ろまで来たところで、勢いよく前に飛び出して「わっ!」と驚かす
4. 気配に気づいたぽよんが振り返り、後ろにたまちゃんがいるのを見つけて驚き、嬉しそうに笑う。
   たまちゃんも嬉しそうにその場で立つ

**表情切り替えはこのカットの最後、ぽよんが振り返って笑う一回のみに限定**し、
それ以外の場面では表情を変化させない。**ぽよんの口は、笑顔になる瞬間も含めて常に
輪郭線のみ・無着色のまま**であることを強く明記する(口の中に色がついてしまう不具合の再発防止)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま動く
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。これは表情が変わっても絶対に崩れない

## 参照画像
- Picture 1(最初のフレーム): F-2aの実際の最終フレームを切り出したもの。
  ぽよんが画面右寄りで一人、右向きにまだ弾んでいる途中の姿(たまちゃんは映っていない)

## プロンプト履歴

### v1 (2026-09-10)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>, with only the transparent, jelly-like rubber character visible, still mid-bounce facing right as if still chasing something, and no other character in view. The transparent character keeps its exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The transparent character continues bouncing forward toward the right, still moving continuously, still chasing energetically as if still hot on the trail, glancing around eagerly, never coming to a full standstill, its mouth remaining completely closed and neutral throughout this part of the shot — a thin dark outline only, with absolutely no fill color of any kind inside it — and its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti. It is precisely because the transparent character is so absorbed in this relentless, still-bouncing chase that it fails to notice the egg-shaped character has already circled back around: from the left edge of the frame, the egg character quietly and quickly creeps back into view, sneaking up behind the transparent character, its short stiff legs never bending at the ankle and always walking up on the very tips of its toes, its heels never touching the ground, its expression neutral and unchanged during this creep, never eyebrows at any point. Once right behind the still-bouncing transparent character, the egg character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise. Caught completely off guard, the transparent character jumps in surprise and whips around — and in this sudden jolt of surprise, the gumballs inside visibly jostle and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Upon spotting the egg character right there behind it, this is the one and only expression change in the entire shot: the transparent character breaks into a happy smile, its round eyes crinkling shut into laughing crescents, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — this smiling mouth stays exactly as transparent and see-through as the rest of its glossy body, with absolutely no color, tint, or fill of any kind appearing inside it at any point, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline the whole time. At the same moment, the egg character also bursts into delighted laughter, standing happily beside the transparent character, pleased with its own successful surprise, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映しており、透明でゼリーのようなラバーキャラクターだけが右向きでまだ何かを追いかけているように弾んでいる途中の姿で映っており、他のキャラクターは映っていない。透明なキャラクターは<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。透明なキャラクターは右へ向かって弾み続け、まだ夢中で追いかけているかのように、きょろきょろと辺りを見回しながら完全に静止することは一切ない——このパートの間、口は完全に閉じた中立の状態のままで、薄い輪郭線のみであり中には一切色が入らない——中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪。透明なキャラクターがこうして一心不乱にまだ弾み続ける追跡に夢中になっているせいで、卵形のキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——画面左端から、卵形のキャラクターが音を立てずに素早く戻ってきて、透明なキャラクターの後ろに忍び寄る——常につま先立ちのまま、短く硬い脚は足首で曲がることも、踵が地面につくこともなく、この忍び寄りの間の表情は中立で変化せず、眉毛はどの瞬間もつかない。まだ弾み続けている透明なキャラクターのすぐ後ろまで来たところで、卵形のキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす。完全に不意を突かれた透明なキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——この驚きの瞬間、中のガムボールは勢いよく揺れて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。すぐ後ろに卵形のキャラクターがいるのを見つけた瞬間、これがこのショット全体で唯一の表情変化となる:透明なキャラクターは嬉しそうな笑顔になり、丸い目はぎゅっと閉じて笑いじわの三日月形になり、口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——この笑顔の口は、光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・着色・塗りつぶしが入らず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。同じ瞬間、卵形のキャラクターも嬉しそうな笑い声を上げ、透明なキャラクターのすぐ横で、いたずらが成功して満足そうに立つ。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F2b_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: F-2aの実際の最終フレームを切り出した画像(ぽよん一人・右向き・たまちゃん不在)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 5〜6秒目安(忍び寄り→驚かす→振り返り→笑いまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 表情切り替えはラストの一回のみ。ぽよんの口の無着色・透明指定は特に強く効かせること
