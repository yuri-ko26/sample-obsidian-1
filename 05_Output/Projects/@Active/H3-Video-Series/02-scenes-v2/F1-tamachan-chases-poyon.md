---
project: H3-Video-Series-v2
cut: F-1
mode: I2VA
status: draft
---

> **注記(2026-09-10)**: 一度F-1a/F-1bに分割したが、後半カット(F-1b)にはぽよんが
> Picture1に映っていないため、AIが毎回ぽよんの見た目を一から想像し直してしまい、
> 「別の生き物」のようになる問題が発生。**1カットに戻すことで解決**(ぽよんが常に
> Picture1に映っている状態を保つ)。`F1a-tamachan-chases-poyon-fun.md`・
> `F1b-poyon-surprises-tamachan.md`は参考として残すが、**以後はこのファイルのv2を使用**。

# カットF-1: たまちゃんがぽよんを追いかける→ぽよんがフレームアウト→たまちゃんの後ろから出てくる→たまちゃんが振り返って笑う

## シーン内容
Fビート(「雲の稜線おいかけっこ」)の1回目。正面固定カメラ、雲の稜線を横から見た構図。

(以下はv3の構成。v1・v2は雲の稜線・床ありの構図で、たまちゃんが追いながら一緒に右へ進む流れだった)

1. Picture1の状態(たまちゃん左・ぽよん右)から、**まずぽよんが1人で右へ弾んでいき、
   完全にフレームアウトする**
2. そこで初めてたまちゃんが右へ追いかけ始めるが、**右端に着く前・途中で立ち止まり**、
   見失ったぽよんを探してきょろきょろと辺りを見渡す(だんだん不安そうになる)
3. ぽよんは**消えた右端ではなく、反対側の画面左端から**こっそり再登場し、
   たまちゃんの背後にゆっくり忍び寄る
4. たまちゃんは見当違いの方向を探し続けていて、ぽよんにまったく気づいていない
5. ぽよんが背後から「わっ!」と飛び出して驚かす → たまちゃんは飛び上がって振り返り、
   一瞬の驚き顔(丸く開いた口)になる
6. ぽよんだと分かった瞬間、驚き顔が笑顔に変わり、2人で一緒に笑い合う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま追いかける
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)

## 参照画像
- Picture 1(最初のフレーム・**v3で更新**): 層になったパステルの雲を背景に、画面左下寄りに
  たまちゃん、右上寄りに一回り大きくぽよんが位置し、どちらも通常の笑顔(2026-09-14いただいた画像1)
- (参考)画像2: 同じ構図でキャラクターが誰もいないパステルの雲の背景。
  **このカットは最後に2人が並んで笑っているためFL2VAの最終フレームには使えない**ので、
  v3ではI2VA(Picture 1のみ)として使用している。背景の色味・形状のリファレンスとして保管
- (v1・v2時点)Picture 1: 雲の稜線を横から見た構図。画面左にたまちゃん、
  右にぽよんが並んで立ち、どちらも通常の笑顔

## プロンプト履歴

### v5 (2026-09-14) — 現在の採用版(キャラクター形状ロックを追加)

**v4からの変更点**
- カメラ指定の直後に、**キャラクターの形状を固定する専用パラグラフ**を新設。
  これまで動きの記述に混ぜ込んでいた制約を、冒頭にまとめて明示する構成に変更
- **たまちゃんの足を最重要項目として徹底記述**(クライアント指摘):
  「脚は足首の関節がない硬い棒状」「歩く・急ぐ・止まる・振り返る・跳ぶ、どの動作でも
  丸いつま先の先端だけが接地」「踵は1フレームたりとも地面につかない」
  「踵・土踏まず・人間のような足の形が生えることは一切ない」
- たまちゃんの殻の構成(白/コーラルピンク・ギザギザの境目)、口に奥行きがないこと、
  眉毛が絶対につかないことを形状ロックとして明記
- ぽよんの「手足が絶対に生えない」「潰れても角ばらない」「離れた瞬間に丸みが戻る」
  「顔は体の前面にしかない」を明記
- **2人の大小関係(ぽよん15cm / たまちゃん10cm)が終始変わらない**ことを明記
- 崩れやすい3つの瞬間(急いで動くとき・驚いて振り返るとき・大笑いするとき)で、
  形状ロックを再度念押しする文を挿入

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single locked-off wide static shot holds the entire scene in frame for the whole video: the camera stays completely fixed in the exact same position, framing, focal length, and field of view as <Picture 1> from the very first frame to the very last, and it never zooms in, zooms out, pushes in, pulls out, pans, tilts, trucks, arcs, tracks or follows a character, reframes, crops closer, or cuts at any point. The full pastel cloud landscape shown in <Picture 1> stays completely visible from edge to edge for the entire duration, and no moment is ever framed as a close-up or as a tighter shot than <Picture 1>; the two characters remain small within this wide view the whole time, which is correct and intended. Both characters keep the exact appearance, proportions, scale, and design established in <Picture 1> in every single frame, with absolutely no drift, morphing, or distortion of their design at any moment. The egg-shaped character stands on the left: its upper half is a smooth matte white eggshell and its lower half is a coral-pink eggshell section, the two meeting along a jagged zigzag break line that keeps the exact same shape and position throughout; it has two short dark-brown arms and two short dark-brown legs. Its legs are stiff, straight, stick-like rods ending in small rounded tips, and they have no ankle joints whatsoever — they never bend, flex, or articulate at the ankle in any frame. The egg character walks, hurries, stops, turns, and reacts entirely up on the very tips of those rounded toes, and only those small rounded toe tips ever make contact with the ground; its heels never touch the ground at any moment, not for a single frame, and no heel, sole, arch, ankle, or human-like foot shape ever forms on it. Its legs keep that same stiff rod shape whether it is standing still, hurrying forward, coming to a stop, or spinning around in surprise. Its face consists only of two round black dot eyes and a thin outline-only mouth with no depth — a flat line drawn on the surface of the shell, never a three-dimensional hole — and the egg character never has eyebrows at any point, and never grows extra limbs, joints, fingers, toes, or any additional facial features. The larger transparent, jelly-like rubber character stands on the right: a smooth, glossy, glass-like teardrop body with a small pointed tip at the top, with no arms, legs, hands, or feet at any point — limbs never grow on it under any circumstance, and it moves only by bouncing like a soft water balloon. Inside it are exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing and no other colors or extra gumballs ever appearing, together with small colorful square and diamond confetti; they always settle naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall as it moves, shifting without ever spilling out no matter how hard it lands. Whenever it squashes or stretches it always keeps smooth rounded curves and never becomes angular, and the instant any part of it leaves the ground it springs straight back to a rounded shape like a water balloon — no part of it ever stays flat or rigid. Its face is two round black dot eyes with white highlights, a thin outline-only mouth, and faint orange-pink cheeks. The transparent character is clearly one size larger than the egg character, about half again its height, and this size relationship stays exactly the same for the whole video. Both characters have faces only on the front of their bodies, never on their backs, and their front-to-back orientation never flips. Both begin with bright, happy, playful expressions. The transparent character is the first one to leave: it bounces away to the right, playfully fleeing, bouncing further and further until it passes completely beyond the right edge of the frame and out of view, while the camera stays wide and motionless and does not follow it. Only then does the egg character hurry after it toward the right, moving as briskly as it possibly can while still staying entirely on the tips of its toes, its stiff rod legs never bending at the ankle and its heels never once dropping to the ground even at its fastest — its body, shell pattern, and proportions stay exactly as established while it moves quickly, with no stretching or deforming — and again the camera stays locked in place and never tracks it. Partway across the frame, well before it ever reaches the right edge, the egg character slows and comes to a full stop, still balanced on its toe tips, then begins looking around for the companion it has lost sight of — its head and body turning first to look right, then to look left, then to look right again, its round dot eyes darting from side to side, its thin outline-only mouth drawn into a flat, slightly worried line with no depth and still no eyebrows, growing a little more uneasy and confused with each passing moment. It is precisely because the egg character is so absorbed in this anxious searching that it completely fails to notice what happens next: the transparent character reappears not from the right edge where it vanished, but from the opposite side of the frame — creeping quietly and slowly into view from the left edge, behind the egg character's back, approaching at a slow, sneaky pace without making a sound, still with no limbs of any kind, its gumballs clearly visible and gently rolling against each other and the bottom of its body with each small movement, its mouth completely closed and neutral, a thin dark outline only, with absolutely no fill color of any kind inside it at any point. The egg character keeps searching in the wrong directions the entire time and never once looks behind itself, so it has no idea the transparent character is there. Once right behind the still-searching egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — stretching and squashing only in smooth rounded curves with no angular edges and no limbs appearing, its interior gumballs visibly jolting and tumbling together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — and even in this fast startled spin it stays entirely on its toe tips, its heels never touching down and its stiff legs never bending at the ankle, its shell keeping its exact white-and-coral-pink design with the same jagged break line, with no smearing or deformation of its shape. Its round dot eyes go wide and its mouth pops open for an instant into a small, rounded, startled shape with a hint of soft coral pink inside — and the very next moment, upon recognizing the transparent character right there behind it, that startled expression gives way to delighted laughter, its round dot eyes crinkling into laughing crescents, still with absolutely no eyebrows appearing, its mouth open wide with soft coral pink visible inside while the rest of its face keeps exactly the same design. Through this entire surprise and reaction, the camera does not move closer at all — it stays exactly as wide and exactly as far away as in <Picture 1>, with the whole cloud landscape still visible edge to edge, and never pushes in on their faces. At the exact same moment, the transparent character also breaks into a happy smile, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time, never once becoming opaque or colored. The two laugh together side by side for the rest of the shot, the egg character still standing on its toe tips with its heels off the ground, the transparent character bouncing happily in place beside it with no limbs and its mouth-outline staying just as thin, uncolored, and transparent as ever, both characters ending the shot with exactly the same design, proportions, and size relationship they had in <Picture 1>, on the very same locked-off wide framing the shot began with.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して、シーン全景を収めたワイドの固定ショット1つだけで構成される——カメラは<Picture 1>とまったく同じ位置・画角・焦点距離・写る範囲のまま、1フレーム目から最後の1フレームまで完全に固定され、どの瞬間もズームイン・ズームアウト・前進・後退・パン・チルト・横移動・アーク・キャラクターの追尾・フレーミングの変更・トリミング・カットを一切行わない。<Picture 1>に映っているパステルカラーの雲の風景は、端から端まで全編を通してずっと見えたままであり、どの瞬間もクローズアップや<Picture 1>より寄った画になることはない。2人のキャラクターはこのワイドの画面の中で終始小さいままであり、それが正しい意図された状態である。

**【キャラクター形状ロック】** 2人とも、<Picture 1>で確立された見た目・プロポーション・大きさ・デザインを1フレーム残らず保ち、どの瞬間もデザインがずれたり別物に変形したり崩れたりすることは一切ない。画面左に立つ卵形のキャラクター——上半分はマットな白い卵の殻、下半分はコーラルピンクの殻の断面で、その境目は**ギザギザのジグザグ線**であり、その形と位置は全編を通してまったく変わらない。短い焦げ茶色の腕が2本、短い焦げ茶色の脚が2本ある。**その脚は、先端が小さく丸い、硬くまっすぐな棒状であり、足首の関節はまったく存在しない——どのフレームにおいても足首で曲がったり、たわんだり、関節のように動いたりすることは一切ない。卵形のキャラクターは、歩くときも、急ぐときも、止まるときも、振り向くときも、驚いて反応するときも、常にその丸いつま先の先端だけで立っており、地面に接するのはその小さく丸いつま先の先端のみである。踵はどの瞬間も、1フレームたりとも地面につかず、踵・足の裏・土踏まず・足首・人間のような足の形が生えることは一切ない。立ち止まっていても、前へ急いでいても、止まるときも、驚いて勢いよく振り返るときも、脚は常に同じ硬い棒状の形のままである。**顔は丸い黒の点目2つと、奥行きのない薄い輪郭線だけの口のみ——殻の表面に描かれた平らな線であって、立体的な穴には決してならない——であり、卵形のキャラクターにはどの瞬間も眉毛はつかず、余分な手足・関節・指・つま先・追加の顔のパーツが生えることもない。画面右に立つ、ひと回り大きい透明でゼリーのようなラバーキャラクター——なめらかで光沢のある、ガラスのようなしずく型の体で、上部に小さくとがった突起がある。**手・腕・脚・足はどの瞬間にも存在せず、いかなる状況でも手足が生えることは決してない**。移動はやわらかい水風船のように弾むことだけで行う。体の中には正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは決して変わらず、他の色や余分なガムボールが現れることもない)のガムボールと、小さくカラフルな四角形・ひし形の紙吹雪が入っている。それらは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりお互いにくっついて見えたりすることは一切なく、動くたびにお互いや内壁にぶつかってころころと転がり、どんなに強く着地しても外にこぼれることはない。潰れるときも伸びるときも常になめらかな曲面を保ち、角ばることは決してなく、体のどの部分も地面から離れた瞬間に水風船のようにすぐ丸みを取り戻す——平らなまま・硬いままで残る部分は一切ない。顔は白いハイライト入りの丸い黒の点目2つ、薄い輪郭線だけの口、そして薄いオレンジ〜ピンクの頬である。**透明なキャラクターは卵形のキャラクターよりはっきりとひと回り大きく、身長でおよそ1.5倍であり、この大小関係は動画全体を通してまったく変わらない。** 2人とも顔は体の前面にしかなく、背面に顔が現れることはなく、前後の向きが入れ替わることもない。

2人とも明るく楽しそうな表情から始まる。まず先に画面から出ていくのは透明なキャラクターのほうである——楽しそうに逃げるように右方向へ弾んでいき、さらに右へ右へと弾んで、ついに画面右端を完全に越えて見えなくなる——その間もカメラはワイドのまま微動だにせず、追いかけない。そこで初めて卵形のキャラクターが右へ向かって追いかけ始める——できる限りの速さで進みながらも、**常に完全につま先立ちのままで、硬い棒状の脚は足首で曲がらず、最高速で動いているときですら踵が一度も地面に落ちることはない**——速く動いている間も、体・殻の模様・プロポーションは確立されたとおりのままで、伸びたり歪んだりしない——そしてこのときもカメラは固定されたままで、決して追尾しない。しかし画面の途中まで来たところで、右端にたどり着くよりずっと手前で卵形のキャラクターは速度を落としてぴたりと立ち止まり、つま先の先端でバランスを取ったまま、見失った相手を探して辺りを見回し始める——まず右を見て、次に左を見て、また右を見て、と体と頭を動かしながら探し、丸い点目は左右に忙しく動き、奥行きのない薄い輪郭線だけの口は平らな、少し心配そうな線になり、やはり眉毛はつかず、時間が経つにつれて少しずつ不安げで困惑した様子が強まっていく。卵形のキャラクターがこうして不安げに探すことに夢中になっているせいで、次に起こることにまったく気づかない——透明なキャラクターは、消えた右端からではなく、フレームの反対側から再登場する。画面左端から、音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていく——このときも手足はまったく生えておらず、中のガムボールははっきりと見え続け、小さな動きに合わせてお互いや体の底とぶつかって転がり、口は完全に閉じた中立の状態、薄い輪郭線のみで、中には一切色が入らない。卵形のキャラクターはその間ずっと見当違いの方向ばかりを探していて、一度も後ろを振り返らないため、透明なキャラクターがそこにいることにまるで気づいていない。まだ探し続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——伸び縮みするのはあくまでなめらかな曲面の範囲内で、角ばった形にはならず、手足も一切現れず、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——**この素早い振り返りの瞬間ですら、常につま先の先端だけで立っており、踵は地面につかず、硬い脚は足首で曲がらない**。殻は白とコーラルピンクの配色とジグザグの境目をそのまま正確に保ち、形がにじんだり変形したりすることはない。丸い点目は大きく見開かれ、口は一瞬だけ小さく丸い驚いた形にぱっと開いて中にやわらかなコーラルピンクがほんのりのぞく。そしてその次の瞬間、すぐ後ろに透明なキャラクターがいると分かった途端、その驚き顔は嬉しそうな笑い顔に変わる。丸い点目は笑いじわの三日月形になり、**眉毛は一切現れず**、口は大きく開いて中にやわらかなコーラルピンクがのぞくが、顔の他の部分のデザインはまったく同じままである。この驚きとリアクションの一連の間も、カメラはまったく近づかない——<Picture 1>とまったく同じワイドさ・同じ距離のままで、雲の風景は依然として端から端まで見えており、2人の顔に寄っていくことは一切ない。まったく同じ瞬間、透明なキャラクターも嬉しそうな笑顔になる——口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続け、一度たりとも不透明になったり着色されたりすることはない。2人はショットの残りの時間、並んで一緒に笑い合う——卵形のキャラクターは依然としてつま先立ちのまま踵を地面につけず、透明なキャラクターは手足のないままそのすぐ横で嬉しそうに弾み、その口の輪郭線は薄く無着色で透明なままである。2人とも、<Picture 1>とまったく同じデザイン・プロポーション・大小関係のままショットを終え、フレーミングも始まったときと同じ固定のワイドのままである。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1_v5.mp4`(未生成)
- 判定: 未検証
- メモ:

### v4 (2026-09-14) — 旧版(カメラ固定のみ強化・形状ロックなし)

**v3からの変更点**
- カメラ指定を大幅に強化。「ズームしない」だけでなく、**画角・焦点距離・画面の範囲が
  <Picture 1>と1フレーム目から最後まで完全に同一**であること、**雲の風景が端から端まで
  常に全部見えている**こと、**どの瞬間もクローズアップやより寄った画にならない**ことを明記
- 驚き・笑いの山場でカメラが寄りやすいため、**その瞬間にもカメラは動かず引いたまま**である
  ことを山場の文中でも念押し
- 「キャラクターはワイドの中で小さいままでよい」と明示し、被写体を大きく見せようとする
  バイアスを抑制

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single locked-off wide static shot holds the entire scene in frame for the whole video: the camera stays completely fixed in the exact same position, framing, focal length, and field of view as <Picture 1> from the very first frame to the very last, and it never zooms in, zooms out, pushes in, pulls out, pans, tilts, trucks, arcs, tracks or follows a character, reframes, crops closer, or cuts at any point. The full pastel cloud landscape shown in <Picture 1> stays completely visible from edge to edge for the entire duration, and no moment is ever framed as a close-up or as a tighter shot than <Picture 1>; the two characters remain small within this wide view the whole time, which is correct and intended. The egg-shaped character is on the left and the larger transparent, jelly-like rubber character is on the right. Both characters keep their exact appearance, scale, and design from <Picture 1> unchanged throughout, with no distortion, and both begin with bright, happy, playful expressions. The egg character never has eyebrows at any point — its face is only round black dot eyes and an outline-only mouth. The transparent character is the first one to leave: it bounces away to the right, playfully fleeing, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing and no other colors or extra gumballs ever appearing, together with small colorful square and diamond confetti — always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce, shifting without ever spilling out; it bounces further and further to the right until it passes completely beyond the right edge of the frame and out of view, while the camera stays wide and motionless and does not follow it. Only then does the egg character hurry after it toward the right, always walking up on the very tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle, moving as briskly as it possibly can, again with the camera staying locked in place and never tracking it. Partway across the frame, well before it ever reaches the right edge, the egg character slows and comes to a full stop, then begins looking around for the companion it has lost sight of — its head and body turning first to look right, then to look left, then to look right again, its round dot eyes darting from side to side, its small outline-only mouth drawn into a flat, slightly worried line, growing a little more uneasy and confused with each passing moment. It is precisely because the egg character is so absorbed in this anxious searching that it completely fails to notice what happens next: the transparent character reappears not from the right edge where it vanished, but from the opposite side of the frame — creeping quietly and slowly into view from the left edge, behind the egg character's back, approaching at a slow, sneaky pace without making a sound. Even during this slow creep, its interior gumballs stay clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement, and its mouth remains completely closed and neutral, a thin dark outline only, with absolutely no fill color of any kind inside it at any point. The egg character keeps searching in the wrong directions the entire time and never once looks behind itself, so it has no idea the transparent character is there. Once right behind the still-searching egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise, its round dot eyes going wide and its mouth popping open for an instant into a small, rounded, startled shape with a hint of soft coral pink inside — and the very next moment, upon recognizing the transparent character right there behind it, that startled expression gives way to delighted laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth open wide with soft coral pink visible inside. Through this entire surprise and reaction, the camera does not move closer at all — it stays exactly as wide and exactly as far away as in <Picture 1>, with the whole cloud landscape still visible edge to edge, and never pushes in on their faces. At the exact same moment, the transparent character also breaks into a happy smile, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time, never once becoming opaque or colored. The two laugh together side by side for the rest of the shot, the transparent character bouncing happily in place beside the egg character, pleased with its own successful surprise, its mouth-outline staying just as thin, uncolored, and transparent as ever even as it bounces, and the shot ends on the very same locked-off wide framing it began with.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。**動画全体を通して、シーン全景を収めたワイドの固定ショット1つだけで構成される**——カメラは<Picture 1>とまったく同じ位置・画角・焦点距離・写る範囲のまま、1フレーム目から最後の1フレームまで完全に固定され、どの瞬間もズームイン・ズームアウト・前進・後退・パン・チルト・横移動・アーク・キャラクターの追尾・フレーミングの変更・トリミング・カットを一切行わない。<Picture 1>に映っているパステルカラーの雲の風景は、**端から端まで全編を通してずっと見えたまま**であり、どの瞬間もクローズアップや<Picture 1>より寄った画になることはない。2人のキャラクターはこのワイドの画面の中で終始小さいままであり、それが正しい意図された状態である。画面左に卵形のキャラクター、右にひと回り大きい透明でゼリーのようなラバーキャラクターがいる。2人とも<Picture 1>の見た目・大きさ・デザインのまま、崩れたり変化したりすることなく全編を通して保たれ、どちらも明るく楽しそうな表情から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない——顔のパーツは丸い黒の点目と輪郭線だけの口のみである。まず先に画面から出ていくのは透明なキャラクターのほうである——楽しそうに逃げるように右方向へ弾んでいき、中のガムボールは正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは決して変わらず、他の色や余分なガムボールが現れることもない)と、小さくカラフルな四角形・ひし形の紙吹雪であり、常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりお互いにくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がり、揺れ動くがこぼれることはない。透明なキャラクターはさらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる——**その間もカメラはワイドのまま微動だにせず、追いかけない**。そこで初めて卵形のキャラクターが右へ向かって追いかけ始める——常につま先立ちのまま、踵は絶対に地面につかず、短く硬い脚は足首で曲がらず、できる限りの速さで進む——**このときもカメラは固定されたままで、決して追尾しない**。しかし画面の途中まで来たところで、右端にたどり着くよりずっと手前で卵形のキャラクターは速度を落としてぴたりと立ち止まり、見失った相手を探して辺りを見回し始める——まず右を見て、次に左を見て、また右を見て、と体と頭を動かしながら探し、丸い点目は左右に忙しく動き、輪郭線だけの小さな口は平らな、少し心配そうな線になり、時間が経つにつれて少しずつ不安げで困惑した様子が強まっていく。卵形のキャラクターがこうして不安げに探すことに夢中になっているせいで、次に起こることにまったく気づかない——透明なキャラクターは、消えた右端からではなく、フレームの反対側から再登場する。画面左端から、音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていく。このゆっくりとした忍び寄りの間も、中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。またこの間、透明なキャラクターの口は完全に閉じた中立の状態のままで、薄い輪郭線のみであり、中には一切色が入らない。卵形のキャラクターはその間ずっと見当違いの方向ばかりを探していて、一度も後ろを振り返らないため、透明なキャラクターがそこにいることにまるで気づいていない。まだ探し続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——丸い点目は大きく見開かれ、口は一瞬だけ小さく丸い驚いた形にぱっと開いて中にやわらかなコーラルピンクがほんのりのぞく。そしてその次の瞬間、すぐ後ろに透明なキャラクターがいると分かった途端、その驚き顔は嬉しそうな笑い顔に変わる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかず、口は大きく開いて中にやわらかなコーラルピンクがのぞく。**この驚きとリアクションの一連の間も、カメラはまったく近づかない**——<Picture 1>とまったく同じワイドさ・同じ距離のままで、雲の風景は依然として端から端まで見えており、2人の顔に寄っていくことは一切ない。まったく同じ瞬間、透明なキャラクターも嬉しそうな笑顔になる——口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続け、一度たりとも不透明になったり着色されたりすることはない。2人はショットの残りの時間、並んで一緒に笑い合う。透明なキャラクターは卵形のキャラクターのすぐ横で、いたずらが成功して満足そうにその場で嬉しそうに弾み、弾んでいる間もその口の輪郭線は薄く無着色で透明なままである。そしてショットは、始まったときとまったく同じ固定のワイドフレーミングのまま終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1_v4.mp4`(未生成)
- 判定: 未検証
- メモ:

### v3 (2026-09-14) — 旧版(カメラ指定は簡易・新しい参照画像版)

**v2からの変更点**
1. **ぽよんが先に単独でフレームアウト**する順序を明確化(v2はたまちゃんが追いながら一緒に右へ進む流れだった)
2. たまちゃんは追いかけ始めるが、**画面右端に到達する前・途中で立ち止まって**きょろきょろ見渡す
3. ぽよんの再登場を「**消えた右端ではなく、反対側の左端から**」と明示的に対比して記述
4. たまちゃんがぽよんにまったく気づいていないことを重ねて明記
5. 驚いた瞬間の「驚き顔」(丸く開いた口)を一拍入れてから笑顔に変わる流れを追加
6. 参照画像を新しい雲背景の2ショット画像に差し替え(I2VA)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the layered pastel cloud scenery exactly as shown in <Picture 1>, with the egg-shaped character on the left and the larger transparent, jelly-like rubber character on the right. Both characters keep their exact appearance, scale, and design from <Picture 1> unchanged throughout, with no distortion, and both begin with bright, happy, playful expressions. The egg character never has eyebrows at any point — its face is only round black dot eyes and an outline-only mouth. The transparent character is the first one to leave: it bounces away to the right, playfully fleeing, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing and no other colors or extra gumballs ever appearing, together with small colorful square and diamond confetti — always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce, shifting without ever spilling out; it bounces further and further to the right until it passes completely beyond the right edge of the frame and out of view, leaving the egg character alone in frame. Only then does the egg character hurry after it toward the right, always walking up on the very tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle, moving as briskly as it possibly can. Partway across the frame, well before it ever reaches the right edge, the egg character slows and comes to a full stop, then begins looking around for the companion it has lost sight of — its head and body turning first to look right, then to look left, then to look right again, its round dot eyes darting from side to side, its small outline-only mouth drawn into a flat, slightly worried line, growing a little more uneasy and confused with each passing moment. It is precisely because the egg character is so absorbed in this anxious searching that it completely fails to notice what happens next: the transparent character reappears not from the right edge where it vanished, but from the opposite side of the frame — creeping quietly and slowly into view from the left edge, behind the egg character's back, approaching at a slow, sneaky pace without making a sound. Even during this slow creep, its interior gumballs stay clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement, and its mouth remains completely closed and neutral, a thin dark outline only, with absolutely no fill color of any kind inside it at any point. The egg character keeps searching in the wrong directions the entire time and never once looks behind itself, so it has no idea the transparent character is there. Once right behind the still-searching egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise, its round dot eyes going wide and its mouth popping open for an instant into a small, rounded, startled shape with a hint of soft coral pink inside — and the very next moment, upon recognizing the transparent character right there behind it, that startled expression gives way to delighted laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth open wide with soft coral pink visible inside. At the exact same moment, the transparent character also breaks into a happy smile, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time, never once becoming opaque or colored. The two laugh together side by side for the rest of the shot, the transparent character bouncing happily in place beside the egg character, pleased with its own successful surprise, its mouth-outline staying just as thin, uncolored, and transparent as ever even as it bounces.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定ショットで、<Picture 1>で示された通り、層になったパステルカラーの雲の風景を映しており、画面左に卵形のキャラクター、右にひと回り大きい透明でゼリーのようなラバーキャラクターがいる。2人とも<Picture 1>の見た目・大きさ・デザインのまま、崩れたり変化したりすることなく全編を通して保たれ、どちらも明るく楽しそうな表情から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない——顔のパーツは丸い黒の点目と輪郭線だけの口のみである。**まず先に画面から出ていくのは透明なキャラクターのほうである**——楽しそうに逃げるように右方向へ弾んでいき、中のガムボールは正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは決して変わらず、他の色や余分なガムボールが現れることもない)と、小さくカラフルな四角形・ひし形の紙吹雪であり、常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりお互いにくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がり、揺れ動くがこぼれることはない。透明なキャラクターはさらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなり、卵形のキャラクターが1人だけフレームに残る。**そこで初めて**卵形のキャラクターが右へ向かって追いかけ始める——常につま先立ちのまま、踵は絶対に地面につかず、短く硬い脚は足首で曲がらず、できる限りの速さで進む。しかし画面の途中まで来たところで、**右端にたどり着くよりずっと手前で**卵形のキャラクターは速度を落としてぴたりと立ち止まり、見失った相手を探して辺りを見回し始める——まず右を見て、次に左を見て、また右を見て、と体と頭を動かしながら探し、丸い点目は左右に忙しく動き、輪郭線だけの小さな口は平らな、少し心配そうな線になり、時間が経つにつれて少しずつ不安げで困惑した様子が強まっていく。卵形のキャラクターがこうして不安げに探すことに夢中になっているせいで、次に起こることにまったく気づかない——**透明なキャラクターは、消えた右端からではなく、フレームの反対側から再登場する**。画面左端から、音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていく。このゆっくりとした忍び寄りの間も、中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。またこの間、透明なキャラクターの口は完全に閉じた中立の状態のままで、薄い輪郭線のみであり、中には一切色が入らない。卵形のキャラクターはその間ずっと見当違いの方向ばかりを探していて、一度も後ろを振り返らないため、透明なキャラクターがそこにいることにまるで気づいていない。まだ探し続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——丸い点目は大きく見開かれ、口は一瞬だけ小さく丸い驚いた形にぱっと開いて中にやわらかなコーラルピンクがほんのりのぞく。そしてその次の瞬間、すぐ後ろに透明なキャラクターがいると分かった途端、その驚き顔は嬉しそうな笑い顔に変わる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかず、口は大きく開いて中にやわらかなコーラルピンクがのぞく。まったく同じ瞬間、透明なキャラクターも嬉しそうな笑顔になる——口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——**極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず**、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続け、一度たりとも不透明になったり着色されたりすることはない。2人はショットの残りの時間、並んで一緒に笑い合う。透明なキャラクターは卵形のキャラクターのすぐ横で、いたずらが成功して満足そうにその場で嬉しそうに弾み、弾んでいる間もその口の輪郭線は薄く無着色で透明なままである。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1_v3.mp4`(未生成)
- 判定: 未検証
- メモ:

### v2 (2026-09-10) — 旧版(雲の稜線・床あり構図)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the transparent, jelly-like rubber character begins bouncing away to the right, playfully fleeing, while the egg-shaped character chases right after it with real urgency, always walking up on the very tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle, moving as briskly as it possibly can, both characters wearing bright, happy, playful expressions throughout this part of the shot. The pastel cloud ridge beneath them is bumpy and uneven, and the egg character determinedly clambers up and over each bump directly in its path without ever slowing its pursuit. Even moving as fast as it can, the egg character's short legs are still just a touch slower than the transparent character's bounces, so only a modest gap gradually opens between them the longer the chase goes on, and the egg character keeps closing distance with every stride it can manage, never coming to a stop, slowing to a halt, or standing still while the transparent character is still visible and bouncing away. Its interior gumballs always settle naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. The transparent character bounces onward to the right, a short distance ahead of the egg character, until it bounces completely past the right edge of the frame and out of view, with the egg character still visibly chasing not far behind it. Once the transparent character is no longer visible, the egg character keeps toddling forward a little further toward the right, still on the tips of its toes, then comes to a stop on top of a cloud, looking around anxiously for the transparent character it has lost sight of — its head and body turning first to look left, then to look right, then left again, its round dot eyes darting from side to side, its small outline-only mouth drawn into a flat, slightly worried line, growing a little more uneasy and confused with each passing moment. It is precisely because the egg character is so absorbed in this anxious searching that it fails to notice the transparent character has already circled back around: from the left edge of the frame, the transparent character quietly and slowly creeps back into view, approaching the egg character's back at a slow, sneaky pace, getting closer and closer without making a sound; even during this slow creep, its interior gumballs stay clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement. Throughout this entire creep, the transparent character's mouth remains completely closed and neutral, a thin dark outline only, with absolutely no fill color of any kind inside it at any point. Once right behind the still-searching egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — and upon spotting the transparent character right there behind it, its worried, searching expression instantly gives way to delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the exact same moment, the transparent character also breaks into a happy smile, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time, never once becoming opaque or colored. The transparent character bounces happily in place beside the egg character, pleased with its own successful surprise, its mouth-outline staying just as thin, uncolored, and transparent as ever even as it bounces.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに逃げるように右方向へ弾み始め、卵形のキャラクターは常につま先立ちのまま、短く硬い脚(足首で曲がらず、踵は絶対に地面につかない)を目一杯動かして、本気の勢いですぐ後ろを追いかける——このパートの間、2人とも明るく楽しそうな表情のままである。2人の足元にある雲の稜線はでこぼこと起伏があり、卵形のキャラクターは追跡の速度を緩めることなく、行く手にある一つ一つの盛り上がりを懸命によじ登って越えていく。全力で追いかけていても、卵形のキャラクターの短い脚は弾んで進む透明なキャラクターにほんの少し及ばず、追いかけているうちに2人の間にはささやかな距離が少しずつ生まれていくが、卵形のキャラクターはできる限りその差を詰めようとし続け、透明なキャラクターがまだ見えている間は途中で止まったり立ち止まったりすることは一切ない。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。透明なキャラクターは卵形のキャラクターの少し先を、さらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる——その間も卵形のキャラクターはすぐ後ろで追いかけ続ける様子がはっきり見えている。透明なキャラクターが見えなくなると、卵形のキャラクターはつま先立ちのまま右へ向かってもう少しだけ進み、雲の上で立ち止まる——そして、見失った透明なキャラクターを探して不安そうに辺りを見回し始める。まず左を見て、次に右を見て、また左を見て、と体と頭を動かしながら探し、丸い点目は左右に忙しく動き、輪郭線だけの小さな口は平らな、少し心配そうな線になり、時間が経つにつれて少しずつ不安げで困惑した様子が強まっていく。卵形のキャラクターがこうして不安げに探すことに夢中になっているせいで、透明なキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——画面左端から、透明なキャラクターが音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていき、少しずつ距離を詰めていく——このゆっくりとした忍び寄りの間も、中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。この忍び寄りの間ずっと、透明なキャラクターの口は完全に閉じた中立の状態のままで、薄い輪郭線のみであり、中には一切色が入らない。まだ探し続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——そしてすぐ後ろに透明なキャラクターがいるのを見つけた瞬間、不安そうに探していた表情は一瞬で、驚きと嬉しさの入り混じった笑い声に変わる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。まったく同じ瞬間、透明なキャラクターも嬉しそうな笑顔になる——口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——**極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず**、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続け、一度たりとも不透明になったり着色されたりすることはない。透明なキャラクターは卵形のキャラクターのすぐ横で、いたずらが成功して満足そうに、その場で嬉しそうに弾む——弾んでいる間も、その口の輪郭線は薄く無着色で透明なままである。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1_v2.mp4`(未生成)
- 判定: 未検証
- メモ: F-1a/F-1bの分割を撤回し、1カットに統合したバージョン。ぽよんが常にPicture1に
  映っている状態を保つことでキャラクター一貫性を確保しつつ、口の無着色指定を
  可能な限り強く明記した

### v1 (2026-09-10) — 旧版(分割前・widening gap強めバージョン)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static side-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel cloud ridge exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. From their starting positions, the transparent, jelly-like rubber character begins bouncing away to the right, playfully fleeing, while the egg-shaped character chases right after it with real urgency, its short stiff legs never bending at the ankle and its heels never touching the ground, moving as briskly as it possibly can. The pastel cloud ridge beneath them is bumpy and uneven, and the egg character determinedly clambers up and over each bump directly in its path without ever slowing its pursuit. Even moving as fast as it can, the egg character's short legs are still just a touch slower than the transparent character's bounces, so only a modest gap gradually opens between them the longer the chase goes on, and the egg character keeps closing distance with every stride it can manage. The egg character keeps chasing after it continuously despite this gap — it never comes to a stop, slows to a halt, or stands still while the transparent character is still visible and bouncing away; it keeps actively chasing right up until the transparent character disappears from view. The transparent character bounces onward to the right, a short distance ahead of the egg character, until it bounces completely past the right edge of the frame and out of view, with the egg character still visibly chasing not far behind it, its interior gumballs always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. Even once the transparent character is no longer visible, the egg character does not stop or settle down at all — it keeps toddling forward determinedly toward the right edge, still chasing desperately as if still hot on the trail, its short stiff legs still moving the whole time, never coming to a full standstill or a calm idle pose, facing away toward the right. It is precisely because the egg character is so absorbed in this relentless, still-moving chase that it fails to notice the transparent character has already circled back around: from the left edge of the frame, the transparent character quietly and slowly creeps back into view, approaching the egg character's back at a slow, sneaky pace, getting closer and closer without making a sound; even during this slow creep, its interior gumballs stay clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement. Once right behind the still-moving egg character, the transparent character suddenly pops forward with a big, sudden startling motion — a playful "boo!" surprise — and in this sudden pop, the gumballs inside visibly jolt and tumble together in a lively scatter before settling again, clearly visible through its glossy transparent skin the whole time. Caught completely off guard, the egg character jumps and whips around in surprise — and upon spotting the transparent character right there behind it, bursts into delighted, surprised laughter, its round dot eyes crinkling into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. The transparent character bounces happily in place beside it, pleased with its own successful surprise.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定横向きショットで、<Picture 1>で示された通り雲の稜線を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに逃げるように右方向へ弾み始め、卵形のキャラクターは短く硬い脚(足首で曲がらず、踵も地面につかない)を目一杯動かして、本気の勢いですぐ後ろを追いかける。2人の足元にある雲の稜線はでこぼこと起伏があり、卵形のキャラクターは追跡の速度を緩めることなく、行く手にある一つ一つの盛り上がりを懸命によじ登って越えていく。全力で追いかけていても、卵形のキャラクターの短い脚は弾んで進む透明なキャラクターにほんの少し及ばず、追いかけているうちに2人の間にはささやかな距離が少しずつ生まれていくが、卵形のキャラクターはできる限りその差を詰めようとし続ける。それでも卵形のキャラクターは、この距離にもめげずに**動き続け、途中で止まったり立ち止まったりすることは一切ない**——透明なキャラクターがまだ見えている間は、消えるその瞬間まで積極的に追いかけ続ける。透明なキャラクターは卵形のキャラクターの少し先を、さらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる——その間も卵形のキャラクターはすぐ後ろで追いかけ続ける様子がはっきり見えている。中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。透明なキャラクターが見えなくなっても、卵形のキャラクターは決して止まったり落ち着いたりしない——まだ追跡中であるかのように、画面右端に向かって夢中でよちよちと進み続け、短く硬い脚はずっと動き続けたまま、完全に静止した落ち着いた姿勢に一切ならず、右を向いたままである。卵形のキャラクターがこうして一心不乱にまだ動き続けている追跡に夢中になっているせいで、透明なキャラクターがすでに裏をかいて回り込んできたことにまったく気づかない——画面左端から、透明なキャラクターが音を立てずにゆっくりと、こっそりとした足取りで卵形のキャラクターの背後に忍び寄っていき、少しずつ距離を詰めていく——このゆっくりとした忍び寄りの間も、中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。まだ動き続けている卵形のキャラクターのすぐ後ろまで来たところで、透明なキャラクターは突然、大きくパッと飛び出すようにして、いたずらっぽく「わっ!」と驚かす——この急な飛び出しの瞬間、中のガムボールは勢いよく跳ねて一斉に散らばるように動き、その後また落ち着く様子が、光沢のある透明な体を通してずっとはっきりと見える。完全に不意を突かれた卵形のキャラクターは、びっくりして飛び上がりながら勢いよく振り返る——そしてすぐ後ろに透明なキャラクターがいるのを見つけた瞬間、驚きと嬉しさの入り混じった笑い声を上げる。丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。透明なキャラクターはそのすぐ横で、いたずらが成功して満足そうに、その場で嬉しそうに弾んでいる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1(v3): 2026-09-14にいただいた画像1(パステルの雲背景、たまちゃん左・ぽよん右)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 10秒目安(ぽよんがフレームアウト→たまちゃんが追って途中で止まる→きょろきょろ→
  反対側から登場→驚かす→2人で笑う、まで含むため)
- (v1・v2時点)Picture 1: 雲の稜線の画像(たまちゃん左・ぽよん右)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要(v4)**: カメラは完全固定・全景キープ。「ズームしない」の一文だけでは山場で寄られる
  ことがあるため、(1)冒頭で画角・焦点距離・写る範囲が Picture 1 と同一であること、
  (2)風景が端から端まで常に見えていること、(3)キャラクターは小さいままでよいこと、
  (4)驚き・笑いの瞬間にも寄らないこと、の4点を必ず入れる
- **重要(v5)**: カメラ指定の直後に**キャラクター形状ロックのパラグラフ**を独立して置く。
  特にたまちゃんの足は「足首の関節がない硬い棒状」「接地するのは丸いつま先の先端のみ」
  「踵は1フレームも地面につかない」を明記し、**急いで動くとき・驚いて振り返るとき**にも
  同じ内容を再度書く(速い動きのフレームで最も崩れやすいため)
