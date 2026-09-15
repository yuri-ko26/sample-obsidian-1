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

### v5 (2026-09-15) — 現在の採用版(ジャンプ頂点の先、落下→着地→大笑いまで延長)

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
  色崩れが起きないか注意すること(`00-series-overview.md`にも記録予定)
- v5でPicture2を「最後のフレーム」ではなく「中間アンカー(6.00秒)」として
  使う構成に変更した。落下・着地・大笑いの部分には対応する参照画像がないため、
  生成結果でこの部分の見た目が不安定にならないか特に注意して確認してください
