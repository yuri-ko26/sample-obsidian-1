---
project: H3-Video-Series-v2
cut: F-5
mode: I2VA
status: draft
---

# カットF-5: 新しい参照画像での追いかけっこ→たまちゃん途中で止まりきょろきょろ→反対側からぽよん登場して驚かす→2人で笑う

## シーン内容
新しい参照画像(たまちゃんが左手前のピンクの雲、ぽよんが右奥・高い位置の紫の雲にいる構図)
を使った追いかけっこカット。F-1と同じ「追いかける→見失う→反対側から驚かす」構成だが、
新しい構図・ポーズで作成。正面固定カメラ。

1. Picture1の状態から、ぽよんが先に楽しそうに弾みながら右方向(奥)へ逃げていき、
   画面右端から完全にフレームアウトする
2. たまちゃんはそれを追いかけ始めるが、途中で立ち止まり、まわりをきょろきょろと
   見渡す(見失って不安そうな表情になる)
3. ぽよんは、たまちゃんがフレームアウトした側(右)ではなく、**反対側の左端**から
   ひょこっと再登場する
4. ぽよんがたまちゃんに近づき、「わっ!」と驚かす。たまちゃんはびっくりして飛び上がる
5. 2人で顔を見合わせて嬉しそうに笑い合う

**表情切り替えはこのカットの中で2回のみ**:①追いかけている楽しい表情→見失って
きょろきょろする不安そうな表情、②驚いた表情→嬉しい笑顔。それ以外の場面では
表情を変化させない(表情切り替え時にデザインが崩れる問題を避けるため)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。笑顔になっても崩れない

## 参照画像
- Picture 1(最初のフレーム): たまちゃんが左手前のピンクの雲の上、ぽよんが右奥・高い
  位置の紫の雲の上にいる構図(いただいた新しい参照画像)。2人とも嬉しそうな表情

## プロンプト履歴

### v1 (2026-09-14)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel clouds exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the transparent, jelly-like rubber character begins bouncing away playfully to the right, deeper among the clouds, both characters wearing bright, happy, playful expressions at the start. It bounces further and further away until it moves completely past the right edge of the frame and out of view, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. The egg character chases right after it, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point, clambering over the clouds in its path. Partway through the chase, having lost sight of the transparent character, the egg character comes to a stop and begins looking around anxiously — its head and body turning first to look left, then to look right, then left again, its round dot eyes darting from side to side, its small outline-only mouth drawn into a flat, slightly worried line, growing a little more uneasy and confused with each passing moment. It is precisely because the egg character is so absorbed in this anxious searching that it fails to notice the transparent character has already circled back around — not from the same right side it disappeared from, but from the opposite side: from the left edge of the frame, the transparent character quietly pops back into view, its interior gumballs still clearly visible, gently shifting and rolling against each other and the bottom of its body as it approaches. The transparent character's mouth remains completely closed and neutral throughout this approach, a thin dark outline only, with absolutely no fill color of any kind inside it. Once close behind the still-searching egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — and upon spotting the transparent character right there, its worried, searching expression instantly gives way to delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the exact same moment, the transparent character also breaks into a happy smile, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time. Both characters end the shot laughing happily together.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに右方向、雲の奥へと弾みながら逃げていく——2人とも最初は明るく楽しそうな表情である。ついに画面右端を完全に越えて見えなくなるまで、さらに奥へと弾んでいく——中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。卵形のキャラクターはそのすぐ後ろを追いかける——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらず、行く手にある雲をよじ登りながら進む。追いかけている途中、透明なキャラクターを見失った卵形のキャラクターは立ち止まり、不安そうに辺りを見回し始める——まず左を見て、次に右を見て、また左を見て、と体と頭を動かしながら探し、丸い点目は左右に忙しく動き、輪郭線だけの小さな口は平らな、少し心配そうな線になり、時間が経つにつれて少しずつ不安げで困惑した様子が強まっていく。卵形のキャラクターがこうして不安げに探すことに夢中になっているせいで、透明なキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——消えたのと同じ右側からではなく、**反対側の左端**から、透明なキャラクターが静かにひょこっと再び現れる——中のガムボールははっきりと見え続け、近づくにつれて小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。この接近の間ずっと、透明なキャラクターの口は完全に閉じた中立の状態のままで、薄い輪郭線のみであり、中には一切色が入らない。まだ探し続けている卵形のキャラクターのすぐ近くまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——そしてすぐそこに透明なキャラクターがいるのを見つけた瞬間、不安そうに探していた表情は一瞬で、驚きと嬉しさの入り混じった笑い声に変わる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。まったく同じ瞬間、透明なキャラクターも嬉しそうな笑顔になる——口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。ショットの終わりには、2人とも一緒に嬉しそうに笑い合っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F5_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた新しい参照画像(たまちゃん手前ピンクの雲・ぽよん奥紫の雲)
- モード: I2VA(最後のフレーム画像は不要。いただいた2枚目の雲のみの画像はこのカットの
  終わり方[2人で笑い合う]とは一致しないため、Picture2としては使用していません)
- 尺: 8秒目安(追いかける→見失う→反対側から驚かす→笑うまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 表情切り替えは2回のみ(不安→楽しい追跡ではなく最初から楽しい→不安、驚き→笑顔)。
  「reacts」等の表情変化を誘発しうる単語は使用しない
