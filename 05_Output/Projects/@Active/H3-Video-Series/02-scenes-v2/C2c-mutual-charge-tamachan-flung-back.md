---
project: H3-Video-Series-v2
cut: C-2c
mode: I2VA
status: draft
---

# カット C-2c: ぽよんが2回弾んで「よーしいくぞ!」→お互いに向かっていってぶつかる→たまちゃんが弾き飛ばされて仰向けに倒れ、2人で大笑い

## シーン内容
Cビート(「ぶつかって笑う」)の別バージョン。これまでのC-1・C-2bは片方だけが
相手に体当たりする内容だったが、今回は**両方が同時に相手に向かっていく**
「お互いにぶつかりに行く」構成。正面固定カメラ。

1. ぽよんがその場で2回弾む(水風船のような柔らかい弾み)。「よーしいくぞ!」という
   気合いの入った、やる気満々の様子
2. 2回目の弾みの後、**2人とも同時に相手に向かって突進し**、画面中央でぶつかる
   (どちらか一方だけが動くのではなく、双方が自分から向かっていく)
3. ぶつかった衝撃で、たまちゃんが勢いよく弾き飛ばされ、**仰向けに**倒れる
   (ぽよんは弾力で押し返すが、自身は倒れずその場でしっかり持ちこたえる)
4. 仰向けに倒れたたまちゃんは、その勢いのおかしさに笑い出す
5. ぽよんもその様子を見て一緒に笑う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない(点目と輪郭線の口のみ)
- たまちゃんの笑い顔は、目が三日月形になり口が開いて中にコーラルピンクが見える
- ぽよんは接触時に丸みを保ったままへこむ(ディンプル)。衝撃がどれだけ強くても
  中のガムボール・紙吹雪は絶対にこぼれない
- ぽよんの口は、笑っても輪郭線のみ・無着色のまま(体と同じ透明素材、中のガムボールが
  透けて見える)。大笑いでも口は大きくなりすぎず、控えめな笑みより少し広がる程度

## 参照画像
- Picture 1(最初のフレーム): 「理想画質」の2ショット画像(薄い黄緑色の床+パステルの
  雲を背景に、左にぽよん、右にたまちゃんが並んで立つ構図。C-1・C-2bと共通)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static front-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>. Both characters keep their exact appearance, colors, and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point — its face is only round dot eyes and an outline-only mouth. On the left, the transparent, jelly-like rubber character bounces lightly in place twice with determined, eager energy, its round body compressing slightly downward and springing back up each time like a soft water balloon, as if gearing itself up and ready to go. No matter how much its body compresses, the colorful gumballs and confetti sealed inside it only shift and jostle against each other, never once flying out or escaping through its skin. Right after the second bounce, both characters charge toward each other at the same moment, neither one standing still — the egg character rushing in from the right, the transparent character launching forward from the left — and they collide together in the middle of the frame. The impact sends the egg character flying backward off its feet with great force, and it lands flat on its back on the floor, its short stiff legs flopping up as it lands. The transparent character absorbs the impact with a springy rebound, its round body dimpling inward at the point of contact without ever flattening or losing its overall roundness, and holds its ground without toppling over; even at the moment of hardest impact, its sealed skin holds completely and not a single gumball or piece of confetti escapes. The moment it lands on its back, the egg character bursts into delighted laughter at how funny the impact felt, its round dot eyes crinkling into laughing crescents — still with no eyebrows — and its mouth opening wide with a hint of soft coral pink visible inside. Watching this, the transparent character laughs too, its round eyes crinkling shut into laughing crescents while its mouth curves into a moderately wide, gentle smile shape — not exaggerated or oversized, just a natural, modestly wider curve than its usual resting smile, made of nothing but a thin dark outline: there is no fill, shading, or paint of any color inside this mouth shape, and it stays just as transparent and see-through as its glossy skin, so the colorful gumballs and confetti behind it remain clearly visible straight through the open mouth outline.

overall_soundscape: Two soft, rubbery squeak-bounces from the transparent character, then quick footsteps from both characters as they rush toward each other, followed by a big springy boing on impact and a soft thud as the egg character lands on its back. Bright, delighted laughter from both characters follows.

non_diegetic_music: A playful, bouncy marimba melody that builds through the two bounces and the charge, then bursts into a warm, cheerful flourish the moment both characters laugh.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定正面ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映している。2人とも<Picture 1>の見た目・色・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかず、顔は丸い点目と輪郭線だけの口のみである。左側の透明でゼリーのようなラバーキャラクターが、気合いの入ったやる気満々の様子で、その場で軽く2回はずむ——水風船のように体がわずかに沈んでは弾んで戻る動きを2回繰り返し、まるで「よし行くぞ」と気持ちを高めているかのようである。体がどれだけ圧縮されても、中に密閉された色とりどりのガムボールと紙吹雪はお互いにぶつかり合って揺れ動くだけで、外に飛び出したり表面からはみ出したりすることはない。2回目の弾みの直後、**2人とも同時に相手に向かって突進する**——どちらも動かずに待っているのではなく、卵形のキャラクターは右側から、透明なキャラクターは左側から、それぞれ勢いよく前に飛び出し、画面中央でぶつかり合う。その衝撃で卵形のキャラクターは大きな勢いで後ろに弾き飛ばされ、床の上に仰向けに倒れ込み、短く硬い脚が着地とともに跳ね上がる。透明なキャラクターはその衝撃を弾力のある反動で受け止め、丸い体が接触点でくぼむが、平らになったり丸みを失ったりすることはなく、自分自身は倒れずその場でしっかり持ちこたえる——最も強い衝撃を受けたその瞬間でさえ、密閉された表面は完全に保たれ、ガムボールも紙吹雪も一粒たりとも外に漏れ出すことはない。仰向けに倒れた瞬間、卵形のキャラクターはその衝撃のおかしさに嬉しそうに笑い出し、丸い点目が笑いじわの三日月形になる——眉毛はやはりつかない——そして口は大きく開いて中にほんのりコーラルピンク色がのぞく。それを見ていた透明なキャラクターも一緒に笑い出す——丸い目はぎゅっと閉じて笑いじわの三日月形になり、口はほどよい広さの、やわらかなカーブの笑顔になる——誇張されすぎたり、顔の大部分を占めるような巨大な口にはならず、普段の控えめな笑みより少しだけ広がる程度の、薄い輪郭線だけでできた自然な大きさにとどまる。この口の中には色も陰影も塗りも一切なく、光沢のある体の表面とまったく同じように透き通ったままで、後ろにある色とりどりのガムボールと紙吹雪が、開いた口の輪郭線を通してそのままはっきり透けて見える。

**環境音**
透明なキャラクターが2回はずむやわらかいゴムの弾む音、続いて2人が同時に駆け寄る軽い足音、そして衝突の瞬間の大きく弾む「ぼよん」という音、卵形のキャラクターが仰向けに倒れる柔らかい「どすん」という音。その後、2人の明るく嬉しそうな笑い声が続く。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、2回の弾みと突進を通して盛り上がり、2人が笑い出す瞬間に温かく明るいフレーズへとはじける。

**生成結果**
- 動画ファイル: `03-generated-videos/C2c_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 「理想画質」2ショット画像(C-1・C-2bと共通)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 8秒目安(2回弾む→突進→衝突→着地→2人分の笑いまで含むため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
