---
project: H3-Video-Series-v2
cut: E-2b
mode: FL2VA
status: draft
---

# カットE-2b: 大ジャンプの頂点から、2人が床に落ちて大笑いする(俯瞰、カメラは寄った状態から引いていく)

## シーン内容
E-2(たまちゃんがぽよんにお腹をくっつけて一緒に大ジャンプ)の直接の続き。
E-2はジャンプの頂点(カメラが寄ってフレームいっぱいになった状態)で終わって
いるため、このカットはその頂点からスタートし、2人が一緒に落下して床に着地し、
着地の余韻のまま2人とも目を閉じて大笑いし、最後は通常の俯瞰の広い構図
(カメラが引いた状態)で、普通に立ったまま笑い合っている2人の姿で終わる。

**設計メモ**:
- E-2はカメラが寄り切った状態(顔で画面いっぱい)で終わるため、このカットの
  Picture1はその続きとなる寄った構図を採用し、Picture2はカメラが通常の
  俯瞰の広い構図まで引いた、2人が笑っている様子を採用する。カメラの動きは
  E-2(寄っていく)とは逆に、**寄った状態から徐々に引いていく**構成になる。
  E-2で確立した「お腹をくっつける」「腕は伸びない」「無言」「ガムボール
  構成を動作の節目ごとに繰り返し明記する」の各手法をそのまま踏襲する。
- **v2での変更点**: 新しくいただいた参照画像2枚に合わせて更新。Picture2の
  実際の構図が「床を転がって寝転んだ状態」ではなく、**2人とも通常に立った
  ままの姿勢で目を閉じて大笑いしている**構図だったため、着地後の動作を
  「転がる」から**「着地の勢いで少し揺れながらも、立ったまま大笑いする」**
  に変更した。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの短く硬い腕は常に同じ短い固定長のまま、伸びたり長くなったりしない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(0.00秒・最初のフレーム): v2で新しくいただいた画像1。E-2の頂点の
  続きに相当する寄った構図。左にぽよん、右にたまちゃんが大笑いしている
- Picture 2(最後のフレーム): v2で新しくいただいた画像2。カメラが通常の俯瞰の
  広い構図まで引いた状態。左にぽよん、右にたまちゃんが**通常に立ったまま**、
  2人とも目を閉じて大笑いしている

## プロンプト履歴

### v3 (2026-09-15) — 現在の採用版(たまちゃんの手に指が生える不具合への対策)

「たまちゃんの手に指が生えてしまう」というご報告への対策版。たまちゃんの
短く硬い腕(手)について、これまでの「長さが伸びない」という制約に加えて、
**「指のない、単純な丸みを帯びた形状のまま変化しない」**という解剖学的制約を
明記した(たまちゃんの足首の関節が存在しない、という既存の制約と同じ考え方)。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the tight, face-filling framing established by <Picture 1>, continuing directly from the peak of their big joint jump, with the transparent, jelly-like rubber character and the egg-shaped character already laughing with wide, joyful, overjoyed expressions, matching their exact appearance and expression from <Picture 1>. At this starting point, the transparent character's interior contents consist of precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs — ten in total — plus colorful confetti, and this exact count and color mix must remain completely unchanged for the entire rest of the shot. The egg-shaped character's short, stiff arms are simple, smooth, rounded limbs with no fingers, digits, joints, or hand details of any kind — they must keep this exact same simple, fingerless, rounded shape throughout the entire shot, never sprouting fingers, never developing a hand shape, and never changing form in any way, no matter how much the character moves or how excited it gets. Neither character's mouth ever opens to speak, and neither character talks, says any words, or makes any vocalization at any point in this shot — both stay completely silent throughout, expressing all of their joy and laughter purely through their faces and body language, never through speech. From this peak, they begin descending back down under gravity, falling together side by side. As they fall, the camera begins pulling back out, its overhead angle never changing, the framing steadily widening moment by moment. They land back on the floor together with a soft, springy, cushioned impact, their bodies compressing slightly and bouncing gently on landing, but they stay standing upright on their feet the whole time — neither character falls over, tumbles, or rolls on the floor at any point. Throughout this fall and landing, the transparent character's gumballs tumble and jostle energetically inside with the motion, but their exact count and color mix — 4 yellow, 2 red, 1 light blue, 3 yellow-green, ten total — never changes even slightly, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point; and the egg-shaped character's short, stiff arms keep their same short, fixed length and same simple, fingerless, rounded shape throughout the entire fall and landing, never stretching, lengthening, or growing fingers at any point, its legs never bending at the ankle and its heels never touching the ground out of turn. The instant they land, still standing, both characters burst into hearty, uncontrollable laughter, their eyes closing with the sheer joy of it, their mouths opening wide in delighted laughter, their whole bodies shaking gently with each laugh as they stand there together, side by side, the egg-shaped character's arms still simple and fingerless even as they shake with laughter. As the camera keeps pulling back at a matched, steady pace, they continue standing and laughing together this way, completely silent apart from their laughing faces and shaking bodies, no words ever spoken by either of them. By the end of the shot, the camera has pulled all the way back out to the same wide, standard overhead framing and distance established by <Picture 2>, with the transparent character's gumballs still holding the exact same fixed 4 yellow, 2 red, 1 light blue, and 3 yellow-green, clearly visible through its glossy skin, and the egg-shaped character's arms still their same simple, short, rounded, fingerless shape, exactly matching the standing positions, poses, and joyfully laughing, eyes-closed expressions of both characters shown in <Picture 2> at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された、大きな共同ジャンプの頂点から直接続く、寄った・顔で画面いっぱいの構図から始まり、透明でゼリーのようなラバーキャラクターと卵形のキャラクターはすでに喜びにあふれた、興奮した表情で笑っている——<Picture 1>のとおりの見た目・表情のままである。この開始時点で、透明なキャラクターの中身は正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個)のガムボールとカラフルな紙吹雪から成り、この正確な数と色の組み合わせは、ショットの残り時間すべてを通してまったく変わらないままでなければならない。**卵形のキャラクターの短く硬い腕は、指も関節も手の細部も一切ない、シンプルで滑らかな丸みを帯びた四肢である——キャラクターがどれだけ動いても、どれだけ興奮しても、このまったく同じシンプルで指のない丸い形状をショット全体を通して保ち続けなければならず、指が生えたり、手のような形になったり、形状が変化したりすることは一切ない。**どちらのキャラクターの口も一切開いて話すことはなく、どちらのキャラクターも喋ったり、言葉を発したり、発声したりすることは一切ない——2人とも終始完全に無言のままで、喜びと笑いのすべてを顔と体の動きだけで表現し、言葉では一切表現しない。この頂点から、2人は重力に従って横に並んだまま一緒に落下し始める。落下するにつれて、カメラは俯瞰の角度を変えないまま、少しずつ引いていき始め、フレーミングは一瞬ごとに広がっていく。2人は一緒に、やわらかく弾力のあるクッションのような衝撃で床に着地し、体をわずかに圧縮させて着地時に軽く弾むが、その間ずっと足で立ったままの姿勢を保つ——どちらのキャラクターも転んだり、転がったり、床に寝そべったりすることは一切ない。この落下・着地の間ずっと、透明なキャラクターのガムボールはその動きに合わせて中で元気よく転がりぶつかり合うが、正確な数と色の組み合わせ——黄色4・赤2・水色1・黄緑3、合計10個——は少しも変わらず、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。また、卵形のキャラクターの短く硬い腕は、この落下・着地の間ずっと同じ短い固定された長さと**同じシンプルで指のない丸い形状**を保ち、一切伸びたり長くなったり**指が生えたりすることはなく**、足首も曲がらず、踵も地面につかない。着地した瞬間、立ったままの姿勢で、2人は一緒に心からの、抑えきれない大笑いを爆発させ、あまりの嬉しさに目を閉じ、口を大きく開けた喜びの笑いを見せ、笑うたびに体全体がやさしく揺れながら、並んで一緒に立っている——**卵形のキャラクターの腕は、笑いで体が揺れている間もシンプルで指のないままである。**カメラが同じ一定のペースで引き続けるのに合わせて、2人はこのまま立って笑い合い続け、笑っている顔と揺れる体以外は完全に無言のままで、どちらも一言も言葉を発しない。ショットの終わりには、カメラは<Picture 2>で確立された、通常の広い俯瞰の構図・距離まで完全に引き切っており、透明なキャラクターのガムボールは依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個のままで、光沢のある体を通してはっきりと見え、**卵形のキャラクターの腕も依然として同じシンプルで短く丸みを帯びた、指のない形状のまま**、<Picture 2>に示された2人の立ち姿勢・目を閉じた喜びに満ちた笑いの表情とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2b_v3.mp4`(未生成)
- 判定: 未検証
- メモ: 「たまちゃんの手に指が生える」不具合への対策版。腕の長さの制約に
  加えて、「指のない、単純な丸みを帯びた形状のまま変化しない」という
  解剖学的制約を追加した

### v2 (2026-09-15) — 旧版(たまちゃんの手に指が生えてしまう不具合が発生)

新しくいただいた参照画像2枚に合わせて更新。Picture2が「床を転がって寝転ぶ」
構図ではなく「通常に立ったまま目を閉じて大笑いする」構図だったため、着地後の
動作を転がる動きから、着地の勢いで少し体が弾む・揺れる程度に留め、そのまま
立った姿勢で大笑いする流れに変更した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the tight, face-filling framing established by <Picture 1>, continuing directly from the peak of their big joint jump, with the transparent, jelly-like rubber character and the egg-shaped character already laughing with wide, joyful, overjoyed expressions, matching their exact appearance and expression from <Picture 1>. At this starting point, the transparent character's interior contents consist of precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs — ten in total — plus colorful confetti, and this exact count and color mix must remain completely unchanged for the entire rest of the shot. Neither character's mouth ever opens to speak, and neither character talks, says any words, or makes any vocalization at any point in this shot — both stay completely silent throughout, expressing all of their joy and laughter purely through their faces and body language, never through speech. From this peak, they begin descending back down under gravity, falling together side by side. As they fall, the camera begins pulling back out, its overhead angle never changing, the framing steadily widening moment by moment. They land back on the floor together with a soft, springy, cushioned impact, their bodies compressing slightly and bouncing gently on landing, but they stay standing upright on their feet the whole time — neither character falls over, tumbles, or rolls on the floor at any point. Throughout this fall and landing, the transparent character's gumballs tumble and jostle energetically inside with the motion, but their exact count and color mix — 4 yellow, 2 red, 1 light blue, 3 yellow-green, ten total — never changes even slightly, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point; and the egg-shaped character's short, stiff arms keep their same short, fixed length throughout the entire fall and landing, never stretching or lengthening at any point, its legs never bending at the ankle and its heels never touching the ground out of turn. The instant they land, still standing, both characters burst into hearty, uncontrollable laughter, their eyes closing with the sheer joy of it, their mouths opening wide in delighted laughter, their whole bodies shaking gently with each laugh as they stand there together, side by side. As the camera keeps pulling back at a matched, steady pace, they continue standing and laughing together this way, completely silent apart from their laughing faces and shaking bodies, no words ever spoken by either of them. By the end of the shot, the camera has pulled all the way back out to the same wide, standard overhead framing and distance established by <Picture 2>, with the transparent character's gumballs still holding the exact same fixed 4 yellow, 2 red, 1 light blue, and 3 yellow-green, clearly visible through its glossy skin, exactly matching the standing positions, poses, and joyfully laughing, eyes-closed expressions of both characters shown in <Picture 2> at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された、大きな共同ジャンプの頂点から直接続く、寄った・顔で画面いっぱいの構図から始まり、透明でゼリーのようなラバーキャラクターと卵形のキャラクターはすでに喜びにあふれた、興奮した表情で笑っている——<Picture 1>のとおりの見た目・表情のままである。この開始時点で、透明なキャラクターの中身は正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個)のガムボールとカラフルな紙吹雪から成り、この正確な数と色の組み合わせは、ショットの残り時間すべてを通してまったく変わらないままでなければならない。どちらのキャラクターの口も一切開いて話すことはなく、どちらのキャラクターも喋ったり、言葉を発したり、発声したりすることは一切ない——2人とも終始完全に無言のままで、喜びと笑いのすべてを顔と体の動きだけで表現し、言葉では一切表現しない。この頂点から、2人は重力に従って横に並んだまま一緒に落下し始める。落下するにつれて、カメラは俯瞰の角度を変えないまま、少しずつ引いていき始め、フレーミングは一瞬ごとに広がっていく。2人は一緒に、やわらかく弾力のあるクッションのような衝撃で床に着地し、体をわずかに圧縮させて着地時に軽く弾むが、**その間ずっと足で立ったままの姿勢を保つ——どちらのキャラクターも転んだり、転がったり、床に寝そべったりすることは一切ない。**この落下・着地の間ずっと、透明なキャラクターのガムボールはその動きに合わせて中で元気よく転がりぶつかり合うが、正確な数と色の組み合わせ——黄色4・赤2・水色1・黄緑3、合計10個——は少しも変わらず、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。また、卵形のキャラクターの短く硬い腕は、この落下・着地の間ずっと同じ短い固定された長さを保ち、一切伸びたり長くなったりすることはなく、足首も曲がらず、踵も地面につかない。着地した瞬間、立ったままの姿勢で、2人は一緒に心からの、抑えきれない大笑いを爆発させ、あまりの嬉しさに目を閉じ、口を大きく開けた喜びの笑いを見せ、笑うたびに体全体がやさしく揺れながら、並んで一緒に立っている。カメラが同じ一定のペースで引き続けるのに合わせて、2人はこのまま立って笑い合い続け、笑っている顔と揺れる体以外は完全に無言のままで、どちらも一言も言葉を発しない。ショットの終わりには、カメラは<Picture 2>で確立された、通常の広い俯瞰の構図・距離まで完全に引き切っており、透明なキャラクターのガムボールは依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個のままで、光沢のある体を通してはっきりと見え、<Picture 2>に示された2人の立ち姿勢・目を閉じた喜びに満ちた笑いの表情とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2b_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 新しい参照画像に合わせて、着地後の動作を「転がる」から「立ったまま
  大笑いする」に変更した版。転ばない・転がらないことを明示的に否定文で
  禁止し、たまちゃんの足首・踵の制約もあわせて明記した

### v1 (2026-09-15) — 旧版(着地後、床を転がって寝転ぶ構成だったが、実際の参照画像と異なっていた)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the tight, face-filling framing established by <Picture 1>, continuing directly from the peak of their big joint jump, with the transparent, jelly-like rubber character and the egg-shaped character still pressed belly to belly, both already laughing with wide, joyful, overjoyed expressions, matching their exact appearance and expression from <Picture 1>. At this starting point, the transparent character's interior contents consist of precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs — ten in total — plus colorful confetti, and this exact count and color mix must remain completely unchanged for the entire rest of the shot. Neither character's mouth ever opens to speak, and neither character talks, says any words, or makes any vocalization at any point in this shot — both stay completely silent throughout, expressing all of their joy and laughter purely through their faces and body language, never through speech. From this peak, still pressed together belly to belly, they begin descending back down under gravity, falling together as one unit. As they fall, the camera begins pulling back out, its overhead angle never changing, the framing steadily widening moment by moment. They land back on the floor together with a soft, springy, cushioned impact, and the momentum of the landing carries them straight into a big, joyful, tumbling roll across the floor — their bodies rolling and turning over together side by side, limbs and bodies loosely tumbling in a silly, carefree, unhurried way, neither character ever speaking, both faces lit up with uncontrollable laughter the entire time. Throughout this fall, landing, and roll, the transparent character's gumballs tumble and jostle energetically inside with the motion, but their exact count and color mix — 4 yellow, 2 red, 1 light blue, 3 yellow-green, ten total — never changes even slightly, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point; and the egg-shaped character's short, stiff arms keep their same short, fixed length throughout the entire fall and roll, never stretching or lengthening at any point. As the camera keeps pulling back at a matched pace, the tumbling roll gradually slows and loses momentum, and both characters come to a natural, gentle stop lying on the floor, side by side, their bodies relaxed and slightly askew from the roll, both still laughing hard, their eyes closed with the sheer joy of it, their mouths wide open in delighted, unrestrained laughter, their whole bodies gently shaking with each laugh. By the end of the shot, the camera has pulled all the way back out to the same wide, standard overhead framing and distance established by <Picture 2>, with the transparent character's gumballs still holding the exact same fixed 4 yellow, 2 red, 1 light blue, and 3 yellow-green, clearly visible through its glossy skin, exactly matching the positions, poses, and joyfully laughing expressions of both characters shown in <Picture 2> at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の5.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された、大きな共同ジャンプの頂点から直接続く、寄った・顔で画面いっぱいの構図から始まり、透明でゼリーのようなラバーキャラクターと卵形のキャラクターは依然としてお腹を合わせたまま密着しており、2人ともすでに喜びにあふれた、興奮した表情で笑っている——<Picture 1>のとおりの見た目・表情のままである。この開始時点で、透明なキャラクターの中身は正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個)のガムボールとカラフルな紙吹雪から成り、この正確な数と色の組み合わせは、ショットの残り時間すべてを通してまったく変わらないままでなければならない。どちらのキャラクターの口も一切開いて話すことはなく、どちらのキャラクターも喋ったり、言葉を発したり、発声したりすることは一切ない——2人とも終始完全に無言のままで、喜びと笑いのすべてを顔と体の動きだけで表現し、言葉では一切表現しない。この頂点から、お腹を合わせたまま密着した状態のまま、2人は重力に従って一緒に落下し始め、一つの塊として落ちていく。落下するにつれて、カメラは俯瞰の角度を変えないまま、少しずつ引いていき始め、フレーミングは一瞬ごとに広がっていく。2人は一緒に、やわらかく弾力のあるクッションのような衝撃で床に着地し、その着地の勢いのまま、そのまま大きく楽しそうな、転がるような動きで床の上を一緒に転がっていく——体を横に並べたまま一緒に転がり回転し、手足や体が力の抜けた、おどけた、慌てない様子でゆるやかに転がっていき、どちらのキャラクターも一切話すことなく、その間ずっと2人の顔は抑えきれない笑いに輝いている。この落下・着地・転がりの間ずっと、透明なキャラクターのガムボールはその動きに合わせて中で元気よく転がりぶつかり合うが、正確な数と色の組み合わせ——黄色4・赤2・水色1・黄緑3、合計10個——は少しも変わらず、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。また、卵形のキャラクターの短く硬い腕は、この落下・転がりの間ずっと同じ短い固定された長さを保ち、一切伸びたり長くなったりすることはない。カメラが同じペースで引き続けるのに合わせて、転がる勢いは徐々にゆるやかになっていき、2人は床の上で並んで自然に穏やかに止まる——転がった勢いで体は少し斜めに崩れた、リラックスした姿勢になり、2人とも依然として激しく笑い続けており、あまりの嬉しさに目を閉じ、口を大きく開けた抑えきれない喜びの笑い声をあげ、笑うたびに体全体がやさしく揺れる。ショットの終わりには、カメラは<Picture 2>で確立された、通常の広い俯瞰の構図・距離まで完全に引き切っており、透明なキャラクターのガムボールは依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個のままで、光沢のある体を通してはっきりと見え、<Picture 2>に示された2人の位置・姿勢・喜びに満ちた笑いの表情とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2b_v1.mp4`(未生成)
- 判定: 未検証
- メモ: E-2の頂点(寄った構図)から直接続くカット。カメラはE-2(寄っていく)
  とは逆に、寄った状態から通常の俯瞰の広い構図まで引いていく。E-2で確立した
  「お腹をくっつける」「腕は伸びない」「無言」「ガムボール構成を繰り返し
  明記する」の各手法をそのまま踏襲した

## ComfyUIでの設定メモ
- Picture 1: v2で新しくいただいた画像1(E-2の頂点の続きに相当する寄った構図)
- Picture 2: v2で新しくいただいた画像2(カメラが引いた、通常の俯瞰の広い構図。
  2人とも立ったまま目を閉じて大笑い)
- モード: FL2VA
- 尺: 4.5秒目安(落下・着地・立ったまま大笑い・カメラが引ききるまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- E-2の実際の最終フレーム(頂点)とPicture1の見た目が一致しているか、
  生成前に確認すること
- v3で「たまちゃんの手に指が生える」不具合への対策を追加(`character-reference.md`
  にも恒久的な制約として記録済み)。他のカットでも同様の不具合が出た場合は
  同じ「指のない丸みを帯びた形状のまま」という文言を追加してください
