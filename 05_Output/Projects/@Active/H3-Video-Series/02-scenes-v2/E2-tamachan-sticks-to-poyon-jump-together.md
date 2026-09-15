---
project: H3-Video-Series-v2
cut: E-2
mode: FL2VA
status: draft
---

# カットE-2: たまちゃんがぽよんにピタッとくっついて、2人一緒に大きくジャンプ(俯瞰、カメラ寄り)

## シーン内容
Eビート(「ジャンプ」)2回目のカット。俯瞰の角度を保ったカメラ、Picture1の状態
(2人ともすでに起き上がって並んで立っている)から始まる。

1. たまちゃんが**トトロにさつきとめいがくっつく時のように、勢いよく「えいっ!」と
   ぽよんに飛びつく**(ゆっくり歩み寄るのではなく、元気に跳びついて抱きつく)
2. くっついたまま、2人一緒に(タイミングを合わせて)真上に大きくジャンプする
3. カメラは**俯瞰の角度を保ったまま**、2人に向かって寄っていき(ズームイン/
   プッシュイン)、ジャンプの頂点では2人がフレームいっぱいに大きく、嬉しそうな
   満面の笑顔で映る——この時点の見た目がPicture2
4. **その後、高く飛んだところから2人一緒に地面へ落ちて着地し、着地の勢いで
   2人とも大笑いする**ところまでをショットに含める

**設計メモ**:
- **v3での変更点1**: 3枚の参照画像(v2)を使ったところ、生成の途中でぽよんの
  ガムボールの色がおかしくなる不具合が発生したため、「最初と最後の2枚だけ」に
  戻すご指示を受け、Picture1(くっつく前)+Picture2(ジャンプ頂点・カメラが寄った
  状態)の通常のFL2VA構成に戻した。中間のPicture(くっついた直後の画像)は
  参照画像としては使わず、テキスト描写のみで表現する。
- **v3での変更点2**: たまちゃんがぽよんにくっつく動作を、「歩み寄ってそっと
  体を寄せる」から、**「トトロにさつきとめいがくっつく時のように、勢いよく
  『えいっ!』と飛びつく」**という元気で弾けるような動きに変更。実際の
  プロンプト文では版権キャラクター名は使わず、「元気よく、飛び跳ねるように
  勢いをつけて相手の体に飛びつき、抱きつくように密着する」という動作として
  英語で具体的に記述している。
- **v5での変更点**: 「画面いっぱい二人の顔でぎゅうぎゅうになるまで高く飛んだ後、
  地面に落ちて大笑いするところまで入れてください」のご指示を受け、ショットの
  終わりをPicture2(ジャンプ頂点)で止めるのではなく、その先まで延長した。
  Picture2は**最後のフレームではなく、6.00秒地点の中間アンカー**として扱い、
  そこから先の「落下→着地→大笑い」はテキスト描写のみで続ける(この先を示す
  参照画像はないため)。尺もそれに合わせて延長している。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの移動:踵をつけず、足首を曲げない棒状の足のまま
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(0.00秒・最初のフレーム): いただいた画像1。俯瞰、薄い黄緑色の床。
  左側にぽよん、右側にたまちゃんが並んで立っている構図(2人ともすでに起き上がった
  状態、くっつく前)
- Picture 2(v5時点では6.00秒・ジャンプ頂点の中間アンカー、最後のフレームではない):
  いただいた画像3。ジャンプの頂点、カメラが俯瞰のまま大きく寄った構図。2人が
  くっついたまま画面いっぱいに映り、満面の笑顔
- (v2で使用・v3以降は不使用): くっついた直後・ジャンプ前の中間参照画像
  (色がおかしくなる不具合のため中間Pictureとしては使わないことにした)

## プロンプト履歴

### v7 (2026-09-15) — 現在の採用版(たまちゃんが喋る・手が伸びる不具合への対策、お腹をくっつける接触に変更)

実際の生成結果で、①たまちゃんが喋ってしまう、②飛びついて抱きつく際に
たまちゃんの手(腕)が不自然に伸びてしまう、という2つの不具合が判明。
原因として、「両腕を大きく広げて相手に飛びつき、抱きつく(both arms
wrapping tightly around it)」という描写が、たまちゃんの短く硬い腕を
無理に伸ばして相手を抱え込む絵として解釈されてしまった可能性が高い。

**対策**:
1. 接触の描写を「腕で抱きつく」から、ご指示どおり**「お腹をピタッと
   くっつける」**(体の前面・お腹同士を平らに押し当てる)に変更し、腕は
   常に短いまま体の脇に沿わせておくことを明記
2. たまちゃんの腕について、D-1系で確立した「足首の関節が存在しない」と
   同じ解剖学的制約の書き方を腕にも適用し、**「短く硬い腕は常に同じ短い
   長さを保ち、どの瞬間も伸びたり長くなったりしない」**ことを明記
3. 「どちらのキャラクターも一切話さない」という無言の指定を、特に飛びつきの
   瞬間の直前に改めて明記し、興奮した場面でも喋らないことを強調

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. At this starting point, the transparent character's interior contents consist of precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs — ten in total — plus colorful confetti, and this exact count and color mix must remain completely unchanged for the entire rest of the shot, no matter what happens to the character's body. Neither character's mouth ever opens to speak, and neither character talks, says any words, or makes any vocalization at any point in this shot — even in this most excited, energetic moment, both stay completely silent throughout, expressing everything purely through body language and facial expression alone, never through speech. With a burst of overflowing, can't-contain-it excitement, its eyes lighting up and its whole face breaking into an enormous grin, the egg-shaped character takes two quick, bounding running steps to build up speed, then explodes off the ground with as much force as it can muster, launching itself powerfully through the air toward the transparent character in a big, dramatic, all-out flying leap — not a small hop or a gentle step, but a bold, unrestrained, full-force pounce, the kind of enthusiastic, no-holding-back leap a small child gives when they can no longer wait and go flying toward someone they love. Throughout this entire leap, its short, stiff arms keep exactly the same short, fixed length they always have, staying close in against its sides — they never stretch, lengthen, or extend outward at any point, no matter how big or forceful the leap is. It crashes snugly into the transparent character with real momentum, landing with its round belly pressed flat and directly against the transparent character's side — belly to belly, the two front surfaces flattening together on contact — the two of them now touching, nestled closely together this way, its short arms still at their normal fixed length, simply resting near its sides rather than reaching out or wrapping around anything. The transparent character visibly rocking and wobbling from the strong, cheerful force of the impact before settling. Even as it rocks from this impact, its interior gumballs — still the exact same 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, never any other count or color — merely jostle and shift naturally inside, always staying fully contained inside its glossy transparent body and never flying out or passing through its skin at any point. Once pressed together belly to belly like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, their bellies still pressed together, as if leaping as a single unit. As they rise, the camera keeps its overhead angle but pushes in steadily closer toward the pair, moving closer and closer with each moment. Throughout this upward rise, the transparent character's gumballs continue tumbling gently inside with the motion, but the count and colors never change even slightly from the same 4 yellow, 2 red, 1 light blue, and 3 yellow-green, always fully contained inside the glossy transparent body, and the egg-shaped character's short arms remain their normal fixed length the entire time, never stretching. By the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 2> at this point of the shot — and at this peak moment, the transparent character's interior still holds exactly this same fixed set of 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, clearly visible through its glossy skin, with no gumball ever appearing or disappearing. From this peak, still pressed belly to belly and still filling almost the entire frame in this same close overhead framing, they begin descending back down under gravity, falling together as one unit, their combined weight picking up speed on the way down; during this fall, the transparent character's gumballs shift downward together under the motion, but their exact count and color mix — 4 yellow, 2 red, 1 light blue, 3 yellow-green, ten total — remains completely unchanged throughout the entire descent. They land back on the floor together with a springy, cushioned impact, their bodies compressing slightly and bouncing very slightly on landing before settling, still held belly to belly; at the instant of landing, the gumballs settle and jostle from the impact but their count and colors stay exactly the same as at the very start, never gaining or losing a single gumball and never shifting to any other color. The instant they land, both characters burst out laughing together — silently expressive, wide-open, joyful laughter shown purely through their faces and shaking bodies, with no words or sounds ever spoken by either of them — their mouths opening wide in delight, their whole bodies shaking gently with each laugh, still pressed close together belly to belly in the same tight, overhead, filled-frame close-up the entire time, the transparent character's gumballs still visibly the same fixed 4 yellow, 2 red, 1 light blue, and 3 yellow-green throughout the laughter, always fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. The shot ends with both characters still held close together belly to belly in this tight, filled-frame overhead close-up, laughing together with complete, joyful abandon.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。この開始時点で、透明なキャラクターの中身は正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個)のガムボールとカラフルな紙吹雪から成り、この正確な数と色の組み合わせは、体に何が起ころうとも、ショットの残り時間すべてを通してまったく変わらないままでなければならない。**どちらのキャラクターの口も一切開いて話すことはなく、どちらのキャラクターも喋ったり、言葉を発したり、発声したりすることは一切ない——この最も興奮した、エネルギッシュな瞬間であっても、2人とも終始完全に無言のままで、すべてを体の動きと表情だけで表現し、言葉では一切表現しない。**抑えきれないほどあふれる興奮とともに、目を輝かせ、顔いっぱいに大きな笑みを浮かべながら、卵形のキャラクターはまず勢いをつけるために弾むような2歩の助走を踏み、そして力の限り地面を蹴って爆発的に飛び出し、透明なキャラクターに向かって空中を力強く、大きく、劇的な全力の跳躍で飛んでいく——小さなホップやそっとした一歩ではなく、小さな子どもがもう待ちきれずに大好きな相手に向かって飛んでいくときのような、大胆で歯止めの利かない跳躍である。**この跳躍の間ずっと、その短く硬い腕はいつもとまったく同じ短い、固定された長さを保ち、体の脇に沿ったままである——跳躍がどれだけ大きく力強くても、腕が伸びたり、長くなったり、外側へ伸ばされたりすることは一切ない。**本物の勢いをもって透明なキャラクターにぶつかるように着地し、**丸いお腹を透明なキャラクターの体の側面に平らに、まっすぐ押し当てるようにして着地する——お腹とお腹が触れ合い、2つの前面が接触した瞬間に平らに合わさる**——2人は触れ合い、このようにぴったりと寄り添った状態になり、**その短い腕は依然として通常の固定された長さのままで、何かに向かって伸ばしたり巻きつけたりするのではなく、単に体の脇の近くに置かれているだけである。**透明なキャラクターは、この強く嬉しそうな衝撃の勢いで目に見えて揺れ、ぐらつきながら、やがて落ち着く。この衝撃で揺れている間も、中のガムボール——依然としてまったく同じ黄色4個・赤2個・水色1個・黄緑3個、合計10個で、他の数や色になることは一切ない——は自然に揺れ動き位置を変えるだけで、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。このようにお腹同士を合わせて密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、お腹を合わせたまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラは俯瞰の角度を保ったまま、2人へ向かって一定のペースで着実に寄っていく。この上昇の間ずっと、透明なキャラクターのガムボールはその動きに合わせて中で穏やかに転がり続けるが、数と色はまったく同じ黄色4個・赤2個・水色1個・黄緑3個から少しも変わらず、常に光沢のある透明な体の中に完全に収まっており、**卵形のキャラクターの短い腕もこの間ずっと通常の固定された長さのままで、一切伸びることはない。**この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、この時点で<Picture 2>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致する——そしてこの頂点の瞬間も、透明なキャラクターの中身は依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個、合計10個のガムボールの組み合わせを保っており、光沢のある体を通してはっきりと見え、ガムボールが現れたり消えたりすることは一切ない。この頂点から、2人はお腹を合わせたまま密着し、フレームのほぼ全体を占めるこの同じ寄った俯瞰フレーミングのまま、重力に従って一緒に一つの塊として落下し始め、合わさった重さで下降しながら速度を増していく——この落下の間、透明なキャラクターのガムボールはその動きに合わせて一緒に下方向へ移動するが、正確な数と色の組み合わせ——黄色4・赤2・水色1・黄緑3、合計10個——は下降の間ずっとまったく変わらないままである。2人は一緒に、弾力のあるクッションのような衝撃で床に着地し、体をわずかに圧縮させて着地時にごくわずかに弾みながら、お腹を合わせたまま落ち着く——着地の瞬間、ガムボールは衝撃で落ち着き揺れ動くが、その数と色は最初とまったく同じままで、一つのガムボールも増減したり、他の色に変わったりすることは一切ない。着地した瞬間、2人は一緒に大きく笑い出す——**言葉や音声を一切発することなく、表情と体の震えだけで示される、無言のまま口を大きく開けた喜びいっぱいの笑い**であり、笑うたびに体全体がやさしく揺れる——その間ずっと、お腹を合わせたまま、同じ寄った・俯瞰の・フレームいっぱいのクローズアップのまま、ぴったりとくっついている——透明なキャラクターのガムボールは、この大笑いの間も依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個のままで、常に光沢のある透明な体の中に完全に収まっており、一度も外に飛び出したり体の表面を突き抜けたりすることはない。ショットは、2人がお腹を合わせたまま、この寄った・フレームいっぱいの俯瞰クローズアップのまま、心から嬉しそうに大笑いしているところで終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v7.mp4`(未生成)
- 判定: 未検証
- メモ: 生成結果で①たまちゃんが喋ってしまう、②飛びつく際に手(腕)が
  不自然に伸びてしまう、という2つの不具合が判明したための対策版。
  「腕で抱きつく」描写を「お腹をピタッとくっつける」に変更し、腕については
  「常に短い固定長のまま伸びない」という解剖学的制約を追加。無言の指定も
  飛びつきの直前に改めて明記した

### v6 (2026-09-15) — 旧版(「両腕を広げて抱きつく」描写で、手が伸びる・喋る不具合が発生)

「ジャンプする時にポヨンのカラーボールの色が減ったり増えたりする」というご報告を
受けた対策版。これまでは中身のガムボール構成(黄色4・赤2・水色1・黄緑3、合計10個)
をショットの終わり付近で1回だけまとめて記述していたが、このカットは助走→飛びつき
→衝撃→しゃがみ→ジャンプ上昇→頂点→落下→着地→大笑い、と動作の区切りが多い
長いプロンプトのため、**F-10・D-3で確立した「動作の節目ごとにガムボールの
正確な数・色の組み合わせと完全収容を繰り返し明記する」パターン**を適用し、
飛びつきの瞬間・ジャンプ上昇中・頂点・落下中・着地の瞬間の計5箇所でガムボール
構成を個別に明記するよう変更した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. At this starting point, the transparent character's interior contents consist of precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs — ten in total — plus colorful confetti, and this exact count and color mix must remain completely unchanged for the entire rest of the shot, no matter what happens to the character's body. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. With a burst of overflowing, can't-contain-it excitement, its eyes lighting up and its whole face breaking into an enormous grin, the egg-shaped character takes two quick, bounding running steps to build up speed, then explodes off the ground with as much force as it can muster, launching itself powerfully through the air toward the transparent character in a big, dramatic, all-out flying leap — arms flung wide open, body fully stretched out mid-air — not a small hop or a gentle step, but a bold, unrestrained, full-force pounce, the kind of enthusiastic, no-holding-back glomp a small child gives when they can no longer wait and go flying into the arms of someone they love. It crashes snugly into the transparent character's side with real momentum, both arms wrapping tightly around it in a big embrace, the two of them now touching, nestled closely together, the transparent character visibly rocking and wobbling from the strong, cheerful force of the impact before settling. Even as it rocks from this impact, its interior gumballs — still the exact same 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, never any other count or color — merely jostle and shift naturally inside, always staying fully contained inside its glossy transparent body and never flying out or passing through its skin at any point. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera keeps its overhead angle but pushes in steadily closer toward the pair, moving closer and closer with each moment. Throughout this upward rise, the transparent character's gumballs continue tumbling gently inside with the motion, but the count and colors never change even slightly from the same 4 yellow, 2 red, 1 light blue, and 3 yellow-green, always fully contained inside the glossy transparent body. By the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 2> at this point of the shot — and at this peak moment, the transparent character's interior still holds exactly this same fixed set of 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, clearly visible through its glossy skin, with no gumball ever appearing or disappearing. From this peak, still pressed tightly together and still filling almost the entire frame in this same close overhead framing, they begin descending back down under gravity, falling together as one unit, their combined weight picking up speed on the way down; during this fall, the transparent character's gumballs shift downward together under the motion, but their exact count and color mix — 4 yellow, 2 red, 1 light blue, 3 yellow-green, ten total — remains completely unchanged throughout the entire descent. They land back on the floor together with a springy, cushioned impact, their bodies compressing slightly and bouncing very slightly on landing before settling, still held closely together; at the instant of landing, the gumballs settle and jostle from the impact but their count and colors stay exactly the same as at the very start, never gaining or losing a single gumball and never shifting to any other color. The instant they land, both characters burst out laughing together, their mouths opening wide in big, unrestrained, joyful laughter, their whole bodies shaking gently with each laugh, still pressed close together in the same tight, overhead, filled-frame close-up the entire time, the transparent character's gumballs still visibly the same fixed 4 yellow, 2 red, 1 light blue, and 3 yellow-green throughout the laughter, always fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. The shot ends with both characters still held close together in this tight, filled-frame overhead close-up, laughing together with complete, joyful abandon.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。この開始時点で、透明なキャラクターの中身は正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個)のガムボールとカラフルな紙吹雪から成り、この正確な数と色の組み合わせは、体に何が起ころうとも、ショットの残り時間すべてを通してまったく変わらないままでなければならない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。抑えきれないほどあふれる興奮とともに、目を輝かせ、顔いっぱいに大きな笑みを浮かべながら、卵形のキャラクターはまず勢いをつけるために弾むような2歩の助走を踏み、そして力の限り地面を蹴って爆発的に飛び出し、透明なキャラクターに向かって空中を力強く、大きく、劇的な全力の跳躍で飛んでいく——両腕を大きく広げ、体を空中で目一杯伸ばして——小さなホップやそっとした一歩ではなく、大胆で歯止めの利かない、全力の飛びつきであり、小さな子どもがもう待ちきれずに大好きな相手の腕の中へまっすぐ飛び込んでいくときのような、遠慮のない熱烈な抱きつきである。本物の勢いをもって透明なキャラクターの体の横にドンとぶつかるように着地し、両腕をしっかりとその体にまわして大きく抱きしめ、2人は触れ合い、ぴったりとくっついた状態になる——透明なキャラクターは、この強く嬉しそうな衝撃の勢いで目に見えて揺れ、ぐらつきながら、やがて落ち着く。この衝撃で揺れている間も、中のガムボール——依然としてまったく同じ黄色4個・赤2個・水色1個・黄緑3個、合計10個で、他の数や色になることは一切ない——は自然に揺れ動き位置を変えるだけで、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラは俯瞰の角度を保ったまま、2人へ向かって一定のペースで着実に寄っていく。この上昇の間ずっと、透明なキャラクターのガムボールはその動きに合わせて中で穏やかに転がり続けるが、数と色はまったく同じ黄色4個・赤2個・水色1個・黄緑3個から少しも変わらず、常に光沢のある透明な体の中に完全に収まっている。この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、この時点で<Picture 2>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致する——そしてこの頂点の瞬間も、透明なキャラクターの中身は依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個、合計10個のガムボールの組み合わせを保っており、光沢のある体を通してはっきりと見え、ガムボールが現れたり消えたりすることは一切ない。この頂点から、2人はぴったりと密着したまま、フレームのほぼ全体を占めるこの同じ寄った俯瞰フレーミングのまま、重力に従って一緒に一つの塊として落下し始め、合わさった重さで下降しながら速度を増していく——この落下の間、透明なキャラクターのガムボールはその動きに合わせて一緒に下方向へ移動するが、正確な数と色の組み合わせ——黄色4・赤2・水色1・黄緑3、合計10個——は下降の間ずっとまったく変わらないままである。2人は一緒に、弾力のあるクッションのような衝撃で床に着地し、体をわずかに圧縮させて着地時にごくわずかに弾みながら、ぴったりとくっついたまま落ち着く——着地の瞬間、ガムボールは衝撃で落ち着き揺れ動くが、その数と色は最初とまったく同じままで、一つのガムボールも増減したり、他の色に変わったりすることは一切ない。着地した瞬間、2人は一緒に大きな声で笑い出し、口を大きく開けて、遠慮のない喜びいっぱいの大笑いを見せ、笑うたびに体全体がやさしく揺れる——その間ずっと、同じ寄った・俯瞰の・フレームいっぱいのクローズアップのまま、ぴったりとくっついている——透明なキャラクターのガムボールは、この大笑いの間も依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個のままで、常に光沢のある透明な体の中に完全に収まっており、一度も外に飛び出したり体の表面を突き抜けたりすることはない。ショットは、2人がこの寄った・フレームいっぱいの俯瞰クローズアップのまま、ぴったりとくっついて、心から嬉しそうに大笑いしているところで終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v6.mp4`(未生成)
- 判定: 未検証
- メモ: 「ジャンプする時にガムボールの数が減ったり増えたりする」不具合への
  対策版。F-10・D-3で確立した「動作の節目ごとに正確な数・色の組み合わせを
  繰り返し明記する」パターンを適用し、飛びつきの衝撃・ジャンプ上昇中・
  頂点・落下中・着地の瞬間・大笑い中の計6箇所でガムボール構成を個別に
  明記した

### v5 (2026-09-15) — 旧版(ガムボール構成の明記が1箇所のみで、色や数が変わる不具合が発生)

「画面いっぱい二人の顔でぎゅうぎゅうになるまで高く飛んだ後、地面に落ちて
大笑いするところまで入れてください」のご指示を受け、v4でジャンプの頂点
(Picture2)で終わっていたショットを延長。Picture2を最後のフレームではなく
6.00秒時点の中間アンカーとして扱い、その先に「落下→着地→2人とも大笑い」を
テキストで追加した。尺も6秒→9秒に延長。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. With a burst of overflowing, can't-contain-it excitement, its eyes lighting up and its whole face breaking into an enormous grin, the egg-shaped character takes two quick, bounding running steps to build up speed, then explodes off the ground with as much force as it can muster, launching itself powerfully through the air toward the transparent character in a big, dramatic, all-out flying leap — arms flung wide open, body fully stretched out mid-air — not a small hop or a gentle step, but a bold, unrestrained, full-force pounce, the kind of enthusiastic, no-holding-back glomp a small child gives when they can no longer wait and go flying into the arms of someone they love. It crashes snugly into the transparent character's side with real momentum, both arms wrapping tightly around it in a big embrace, the two of them now touching, nestled closely together, the transparent character visibly rocking and wobbling from the strong, cheerful force of the impact before settling. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera keeps its overhead angle but pushes in steadily closer toward the pair, moving closer and closer with each moment, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 2> at this point of the shot. From this peak, still pressed tightly together and still filling almost the entire frame in this same close overhead framing, they begin descending back down under gravity, falling together as one unit, their combined weight picking up speed on the way down. They land back on the floor together with a springy, cushioned impact, their bodies compressing slightly and bouncing very slightly on landing before settling, still held closely together. The instant they land, both characters burst out laughing together, their mouths opening wide in big, unrestrained, joyful laughter, their whole bodies shaking gently with each laugh, still pressed close together in the same tight, overhead, filled-frame close-up the entire time. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, no other colors ever appearing at any point — plus colorful confetti, shift, tumble, and jostle energetically inside with the force of the flying leap, the impact, the jump, the fall, and the landing, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. The shot ends with both characters still held close together in this tight, filled-frame overhead close-up, laughing together with complete, joyful abandon.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。抑えきれないほどあふれる興奮とともに、目を輝かせ、顔いっぱいに大きな笑みを浮かべながら、卵形のキャラクターはまず勢いをつけるために弾むような2歩の助走を踏み、そして力の限り地面を蹴って爆発的に飛び出し、透明なキャラクターに向かって空中を力強く、大きく、劇的な全力の跳躍で飛んでいく——両腕を大きく広げ、体を空中で目一杯伸ばして——小さなホップやそっとした一歩ではなく、大胆で歯止めの利かない、全力の飛びつきであり、小さな子どもがもう待ちきれずに大好きな相手の腕の中へまっすぐ飛び込んでいくときのような、遠慮のない熱烈な抱きつきである。本物の勢いをもって透明なキャラクターの体の横にドンとぶつかるように着地し、両腕をしっかりとその体にまわして大きく抱きしめ、2人は触れ合い、ぴったりとくっついた状態になる——透明なキャラクターは、この強く嬉しそうな衝撃の勢いで目に見えて揺れ、ぐらつきながら、やがて落ち着く。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラは俯瞰の角度を保ったまま、2人へ向かって一定のペースで着実に寄っていき、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、この時点で<Picture 2>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致する。この頂点から、2人はぴったりと密着したまま、フレームのほぼ全体を占めるこの同じ寄った俯瞰フレーミングのまま、重力に従って一緒に一つの塊として落下し始め、合わさった重さで下降しながら速度を増していく。2人は一緒に、弾力のあるクッションのような衝撃で床に着地し、体をわずかに圧縮させて着地時にごくわずかに弾みながら、ぴったりとくっついたまま落ち着く。着地した瞬間、2人は一緒に大きな声で笑い出し、口を大きく開けて、遠慮のない喜びいっぱいの大笑いを見せ、笑うたびに体全体がやさしく揺れる——その間ずっと、同じ寄った・俯瞰の・フレームいっぱいのクローズアップのまま、ぴったりとくっついている。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色が現れることは一切ない)のガムボールとカラフルな紙吹雪——は、飛びつき・衝撃・ジャンプ・落下・着地の勢いに合わせて元気よく揺れ動き転がりぶつかり合うが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。ショットは、2人がこの寄った・フレームいっぱいの俯瞰クローズアップのまま、ぴったりとくっついて、心から嬉しそうに大笑いしているところで終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v5.mp4`(未生成)
- 判定: 未検証
- メモ: ジャンプ頂点(Picture2)で終わらせず、その先の落下→着地→大笑いまで
  延長した版。Picture2は最後のフレームではなく6.00秒時点の中間アンカーとして
  扱っている。落下・着地・大笑いの部分には対応する参照画像がないため、
  テキスト描写のみで構成している点に注意

### v4 (2026-09-15) — 旧版(ジャンプ頂点=Picture2で終わっていた)

「もっと勢いよく飛びついて欲しいです」のご指示を受け、v3の飛びつき描写を
さらに強化した。具体的には、①助走として2歩ほど勢いをつけて駆け寄ってから
跳ぶ、②跳躍の高さ・距離を大きくする(単なるホップではなく本格的なジャンプ)、
③着地の衝撃を強め、ぽよんがその勢いでより大きく揺れる、④たまちゃんの
表情も目を輝かせた興奮全開の顔にする、という4点を追加・強化した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. With a burst of overflowing, can't-contain-it excitement, its eyes lighting up and its whole face breaking into an enormous grin, the egg-shaped character takes two quick, bounding running steps to build up speed, then explodes off the ground with as much force as it can muster, launching itself powerfully through the air toward the transparent character in a big, dramatic, all-out flying leap — arms flung wide open, body fully stretched out mid-air — not a small hop or a gentle step, but a bold, unrestrained, full-force pounce, the kind of enthusiastic, no-holding-back glomp a small child gives when they can no longer wait and go flying into the arms of someone they love. It crashes snugly into the transparent character's side with real momentum, both arms wrapping tightly around it in a big embrace, the two of them now touching, nestled closely together, the transparent character visibly rocking and wobbling from the strong, cheerful force of the impact before settling. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera keeps its overhead angle but pushes in steadily closer toward the pair, moving closer and closer with each moment, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 2> at the end of the shot. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, no other colors ever appearing at any point — plus colorful confetti, shift, tumble, and jostle energetically inside with the force of the flying leap, the impact, and the jump, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。抑えきれないほどあふれる興奮とともに、目を輝かせ、顔いっぱいに大きな笑みを浮かべながら、卵形のキャラクターはまず勢いをつけるために弾むような2歩の助走を踏み、そして力の限り地面を蹴って爆発的に飛び出し、透明なキャラクターに向かって空中を力強く、大きく、劇的な全力の跳躍で飛んでいく——両腕を大きく広げ、体を空中で目一杯伸ばして——小さなホップやそっとした一歩ではなく、大胆で歯止めの利かない、全力の飛びつきであり、小さな子どもがもう待ちきれずに大好きな相手の腕の中へまっすぐ飛び込んでいくときのような、遠慮のない熱烈な抱きつきである。本物の勢いをもって透明なキャラクターの体の横にドンとぶつかるように着地し、両腕をしっかりとその体にまわして大きく抱きしめ、2人は触れ合い、ぴったりとくっついた状態になる——透明なキャラクターは、この強く嬉しそうな衝撃の勢いで目に見えて揺れ、ぐらつきながら、やがて落ち着く。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラは俯瞰の角度を保ったまま、2人へ向かって一定のペースで着実に寄っていき、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、<Picture 2>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致してこのショットが終わる。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色が現れることは一切ない)のガムボールとカラフルな紙吹雪——は、飛びつき・衝撃・ジャンプの勢いに合わせて元気よく揺れ動き転がりぶつかり合うが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v4.mp4`(未生成)
- 判定: 未検証
- メモ: 「もっと勢いよく飛びついて欲しいです」への対応版。助走・跳躍の
  大きさ・着地の衝撃・表情の4点を強化した

### v3 (2026-09-15) — 旧版(飛びつく動きに変更したが、まだ勢いが控えめだった)

3枚の参照画像を使ったv2で、生成中にぽよんのガムボールの色がおかしくなる
不具合が発生したため、Picture1(くっつく前)+Picture2(ジャンプ頂点)の
2枚構成に戻した。あわせて、たまちゃんがぽよんにくっつく動作を、ゆっくり
歩み寄る描写から、**勢いよく「えいっ!」と飛びつく、元気で弾けるような
動き**に変更した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. With sudden, bursting energy, the egg-shaped character springs off the ground with a quick, spirited little hop and launches itself sideways through the air toward the transparent character, arms open wide, in one energetic, joyful pounce — not a slow walk or a gentle step, but a lively, gleeful leap, the same kind of exuberant, delighted glomp a small child gives when eagerly throwing their arms around a beloved friend. It lands snugly pressed against the transparent character's side, both arms wrapped around it, the two of them now touching, nestled closely together, the transparent character rocking slightly from the cheerful impact of the landing. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera keeps its overhead angle but pushes in steadily closer toward the pair, moving closer and closer with each moment, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 2> at the end of the shot. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, no other colors ever appearing at any point — plus colorful confetti, shift and tumble inside with the motion of the pounce, landing, and jump, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。卵形のキャラクターは、突然のはじけるようなエネルギーとともに、素早く元気なひと跳ねで地面を蹴り、両腕を大きく広げて透明なキャラクターに向かって横向きに空中へ飛び出す、元気で嬉しそうなひと飛びで——ゆっくりとした歩みや静かな一歩ではなく、小さな子どもが大好きな友達に向かって思い切り腕を広げて抱きつくときのような、活気にあふれた、喜びいっぱいの跳躍である。透明なキャラクターの体の横にぴたっと押し付けられるように着地し、両腕をその体にまわして抱きつき、2人は触れ合い、ぴったりとくっついた状態になる——透明なキャラクターは、この嬉しそうな着地の勢いでわずかに揺れる。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラは俯瞰の角度を保ったまま、2人へ向かって一定のペースで着実に寄っていき、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、<Picture 2>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致してこのショットが終わる。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色が現れることは一切ない)のガムボールとカラフルな紙吹雪——は、飛びつき・着地・ジャンプの動きに合わせて揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v3.mp4`(未生成)
- 判定: 未検証
- メモ: 3枚参照(v2)で発生したガムボール色崩れ不具合への対策として2枚構成に
  戻した版。あわせて、たまちゃんがぽよんにくっつく動作を「ゆっくり歩み寄る」
  から「勢いよく飛びつく(トトロにさつきとめいがくっつく時のイメージ)」に
  変更。実際のプロンプトでは版権キャラクター名は使わず、動作そのものを
  具体的に英語で描写した

### v2 (2026-09-15) — 旧版(3枚参照、途中でガムボールの色がおかしくなった)

3枚の参照画像を時系列に沿って割り当てたFL2VA形式に変更。Picture1(くっつく前)→
Picture2(くっついた直後・ジャンプ前)→Picture3(ジャンプの頂点・カメラが寄った
状態)という3点をタイムライン上に明記し、その間の動き(体を寄せる→しゃがんで
力をためる→ジャンプ→カメラが俯瞰のまま寄っていく)を記述した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 2.50-second mark of the target video; Picture 3 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. The egg-shaped character steps toward the transparent character, walking up on the very tips of its toes only, its heels never touching the ground, its short stiff legs never bending at the ankle, until it presses itself snugly right up against the transparent character's side, the two of them now touching, nestled closely together. As they come together like this, the camera keeps its overhead angle but pushes in slightly closer toward the pair, until, at the same moment they finish pressing together, the framing, distance, and pose exactly match <Picture 2>. From this closely nestled position, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera's overhead push-in continues at a matched pace, moving closer and closer toward the pair, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 3> at the end of the shot. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shift and tumble inside with the motion of the jump, always staying fully contained inside its glossy transparent body, never spilling out.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の2.50秒地点に、Picture 3(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。卵形のキャラクターは、常につま先の先端だけで立ち、踵は地面に一切つけず、短く硬い脚は足首でどの瞬間も曲がらないまま、透明なキャラクターの方へ歩み寄り、透明なキャラクターの体の横にぴたっと寄り添うように押し付け、2人は触れ合い、ぴったりとくっついた状態になる。このように体を寄せていく間、カメラは俯瞰の角度を保ったまま2人へ向かってわずかに寄っていき、体を寄せ終えるのとちょうど同じ瞬間に、フレーミング・距離・ポーズが<Picture 2>とぴったり一致する。この密着した状態から、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラの俯瞰プッシュインも同じペースで続き、2人へ向かってどんどん近づいていき、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、<Picture 3>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致してこのショットが終わる。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪——は、ジャンプの動きに合わせて揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、こぼれることは一切ない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 3枚の参照画像(くっつく前/くっついた直後・ジャンプ前/ジャンプの頂点で
  カメラに寄った状態)をタイムライン上に位置づけたFL2VA版。3枚のPictureを
  使う構文は本プロジェクトで初めての試みのため、うまく機能するか要検証

### v1 (2026-09-15) — 旧版(参照画像1枚のみ、I2VA)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single overhead shot looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>, where the transparent, jelly-like rubber character and the egg-shaped character both already stand upright side by side. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The camera keeps the exact same overhead, bird's-eye viewing angle throughout the entire shot, looking straight down at all times and never tilting, panning, or switching to a side or angled view — but it does slowly push in closer toward the two characters as the shot progresses, the framing gradually tightening around them. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. The egg-shaped character steps toward the transparent character, walking up on the very tips of its toes only, its heels never touching the ground, its short stiff legs never bending at the ankle, until it presses itself snugly right up against the transparent character's side, the two of them now touching, nestled closely together. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera's push-in continues at a matched pace, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, seen from directly overhead the whole time. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shift and tumble inside with the motion of the jump, always staying fully contained inside its glossy transparent body, never spilling out. After reaching the peak, both characters descend back down together under gravity, still pressed closely side by side, landing back on the floor at the same spot they jumped from, their bodies compressing slightly on landing before settling back into their normal resting shapes, the camera holding this close, filled-frame overhead framing at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の俯瞰ショットで、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターがどちらもすでに並んで直立している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。カメラはショット全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ないが、ショットが進むにつれて2人に向かってゆっくりとプッシュインしていき、フレーミングは徐々に2人を中心にタイトになっていく。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。卵形のキャラクターは、常につま先の先端だけで立ち、踵は地面に一切つけず、短く硬い脚は足首でどの瞬間も曲がらないまま、透明なキャラクターの方へ歩み寄り、透明なキャラクターの体の横にぴたっと寄り添うように押し付け、2人は触れ合い、ぴったりとくっついた状態になる。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラのプッシュインも同じペースで続き、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、終始真上から見た状態のまま映る。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪——は、ジャンプの動きに合わせて揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、こぼれることは一切ない。頂点に達した後、2人は密着したまま一緒に重力に従って下降し、跳んだのと同じ場所に着地し、着地の瞬間に体をわずかに圧縮させてから、それぞれ通常の休息姿勢に落ち着く——カメラはショットの終わりまで、この寄った・フレームいっぱいの俯瞰フレーミングを保ち続ける。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 「たまちゃんがポヨンにピタッとくっついて一緒に大きくジャンプ」+「カメラは
  俯瞰のまま寄っていく」というご指示への対応版。俯瞰の角度自体は変えず、
  プッシュインズームのみで「フレームいっぱいになる」効果を出している

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(俯瞰、ぽよん左・たまちゃん右で並んで立つ、くっつく前)
- Picture 2: いただいた画像3(ジャンプの頂点、カメラに寄った状態、2人とも満面の笑顔)
  ※v5からは最後のフレームではなく6.00秒時点の中間アンカーとして使用
- モード: FL2VA(2枚構成。中間の「くっついた直後」画像は参照画像としては使わない)
- 尺: 9秒目安(助走+飛びつく2s/しゃがんで力をため→ジャンプ上昇→頂点4s/
  落下→着地→大笑い3s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 俯瞰角度を保ったままのプッシュインズームという、D-beatとは異なるカメラワークの
  カットのため、生成後の見え方に違和感があればフィードバックをください
- v2(3枚参照)でぽよんのガムボールの色が途中でおかしくなる不具合が発生したため、
  v3で2枚構成に戻した。今後、複数枚(3枚以上)のPicture参照を使う際は同様の
  色崩れが起きないか注意すること(`00-series-overview.md`にも記録済み)
- v5では「ジャンプする時にガムボールの数が減ったり増えたりする」不具合が発生。
  v6で動作の節目ごとに正確な数・色の組み合わせを繰り返し明記する対策を追加
  (`00-series-overview.md`にも記録済み)
- v6では「たまちゃんが喋る」「飛びつく際に手が伸びる」不具合が発生。原因は
  「両腕を広げて抱きつく」という描写だった可能性が高いため、v7で「お腹を
  ピタッとくっつける」接触に変更し、腕については「常に短い固定長のまま
  伸びない」という解剖学的制約を追加した(`00-series-overview.md`にも記録済み)
- v5でPicture2を「最後のフレーム」ではなく「中間アンカー(6.00秒)」として
  使う構成に変更した。落下・着地・大笑いの部分には対応する参照画像がないため、
  生成結果でこの部分の見た目が不安定にならないか特に注意して確認してください
