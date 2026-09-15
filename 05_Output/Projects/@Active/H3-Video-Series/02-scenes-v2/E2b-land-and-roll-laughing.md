---
project: H3-Video-Series-v2
cut: E-2b
mode: FL2VA
status: draft
---

# カットE-2b: 大ジャンプの頂点から、2人が床に落ちて転がりながら大笑いする(俯瞰、カメラは寄った状態から引いていく)

## シーン内容
E-2(たまちゃんがぽよんにお腹をくっつけて一緒に大ジャンプ)の直接の続き。
E-2はジャンプの頂点(カメラが寄ってフレームいっぱいになった状態)で終わって
いるため、このカットはその頂点からスタートし、2人が一緒に落下して床に着地し、
その勢いのまま床の上をゴロゴロと転がりながら大笑いし、最後は通常の俯瞰の
広い構図(カメラが引いた状態)で、笑い転げている2人の姿で終わる。

**設計メモ**: E-2はカメラが寄り切った状態(顔で画面いっぱい)で終わるため、
このカットのPicture1はその続きとなる寄った構図(いただいた画像1)を採用し、
Picture2はカメラが通常の俯瞰の広い構図まで引いた、2人が床で転がり笑って
いる様子(いただいた画像2)を採用した。カメラの動きはE-2(寄っていく)とは
逆に、**寄った状態から徐々に引いていく**構成になる。E-2で確立した
「お腹をくっつける」「腕は伸びない」「無言」「ガムボール構成を動作の
節目ごとに繰り返し明記する」の各手法をそのまま踏襲する。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの短く硬い腕は常に同じ短い固定長のまま、伸びたり長くなったりしない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(0.00秒・最初のフレーム): いただいた画像1。E-2の頂点の続きに
  相当する寄った構図。左にぽよん(満面の笑顔)、右にたまちゃん(目を閉じて
  楽しそうに大笑い)
- Picture 2(最後のフレーム): いただいた画像2。カメラが通常の俯瞰の広い
  構図まで引いた状態。左にぽよん、右にたまちゃんが床の上で転がり、2人とも
  目を閉じて大笑いしている

## プロンプト履歴

### v1 (2026-09-15)

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
- Picture 1: いただいた画像1(E-2の頂点の続きに相当する寄った構図)
- Picture 2: いただいた画像2(カメラが引いた、通常の俯瞰の広い構図。2人が
  床で転がり大笑い)
- モード: FL2VA
- 尺: 5秒目安(落下・着地・転がり・カメラが引ききるまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- E-2の実際の最終フレーム(頂点)とPicture1の見た目が一致しているか、
  生成前に確認すること
