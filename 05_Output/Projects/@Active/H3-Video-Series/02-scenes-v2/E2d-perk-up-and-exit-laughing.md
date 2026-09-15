---
project: H3-Video-Series-v2
cut: E-2d
mode: FL2VA
status: draft
---

# カットE-2d: 大笑いの状態からむくっと起き上がり、楽しそうに笑いながらフレームアウトする(俯瞰固定)

## シーン内容
E-2b/E-2cの続き。2人ともすでに立って大笑いしている状態(Picture1)から、
**むくっと勢いよく体を起こして元気を取り戻し**、楽しそうに笑いながら
2人一緒にフレームの外へ歩いて(弾んで)いき、最後は誰もいない床だけが
残る(Picture2)。俯瞰固定カメラ。

**設計メモ**: 「むくっと起き上がって」という表現だが、いただいた画像1では
2人ともすでに立っている状態のため、「寝転んだ状態から起き上がる」動作
そのものではなく、**「落ち着きかけていた体を勢いよくシャキッと起こし直す、
元気を取り戻すような仕草」**として解釈した。方向は指定がないため、
ひとまず画面右方向へフレームアウトする想定にしている(左方向が正しい
場合は教えてください)。たまちゃんの手が指のない丸い形状のまま変化しない
(E-2bで確立)、ぽよんのガムボール構成を動作の節目ごとに繰り返し明記する、
セリフなし、の各制約をそのまま踏襲する。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの短く硬い腕は、指のない単純な丸みを帯びた形状のまま変化しない
- たまちゃんの移動:踵をつけず、足首を曲げない棒状の足のまま
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(0.00秒・最初のフレーム): いただいた画像1。俯瞰、左にぽよん・
  右にたまちゃんが並んで立ち、2人とも大笑いしている
- Picture 2(最後のフレーム): いただいた画像2。誰もいない、無地の薄い
  黄緑色の床のみ

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor exactly as shown in <Picture 1>, with the transparent, jelly-like rubber character on the left and the egg-shaped character on the right, both already standing and laughing hard, matching their exact appearance and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through their laughing faces and body language. The egg-shaped character's short, stiff arms are simple, smooth, rounded limbs with no fingers, digits, joints, or hand details of any kind, and they keep this exact same fingerless, rounded shape throughout the entire shot, never sprouting fingers or changing form at any point. After a brief moment of laughing in place, both characters suddenly perk up together with a fresh burst of energy, their bodies straightening and springing upright as if catching a renewed wave of excitement, still laughing and smiling brightly the whole time. They then move off together toward the right side of the frame, still laughing and full of joy — the egg-shaped character moving with small, bouncy steps, always walking up on the very tips of its toes only, its heels never touching the ground, its short stiff legs never bending at the ankle, its short fingerless arms swinging cheerfully with each step; the transparent character bouncing along beside it at a matched, cheerful pace, its round body compressing gently downward and springing back up with each little bounce. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing — shift and settle naturally at the bottom of its body under gravity with each bounce, always staying fully contained inside its glossy transparent body, never spilling out or passing through its skin at any point. Both characters continue this same cheerful, laughing exit together, moving steadily toward the right edge of the frame, the transparent character's gumballs still holding the exact same fixed 4 yellow, 2 red, 1 light blue, and 3 yellow-green throughout, and the egg-shaped character's arms still their same simple, fingerless, rounded shape, until they fully exit past the right edge of the frame, leaving the floor completely empty, exactly matching the empty floor shown in <Picture 2> for the remainder of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、左に透明でゼリーのようなラバーキャラクター、右に卵形のキャラクターが、すでに立って激しく笑っている、<Picture 1>のとおりの見た目・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままで、すべてを笑っている顔と体の動きだけで表現する。卵形のキャラクターの短く硬い腕は、指も関節も手の細部も一切ない、シンプルで滑らかな丸みを帯びた四肢であり、ショット全体を通してこのまったく同じ指のない丸い形状を保ち続け、指が生えたり形状が変化したりすることは一切ない。その場でしばらく笑い合った後、2人は突然、新たな元気の波を受け止めたかのように、体をシャキッと伸ばしてむくっと起き上がるように一緒に姿勢を正し、その間もずっと明るく笑い、微笑み続ける。その後、2人は一緒に画面右側へ向かって、笑いと喜びに満ちたまま移動していく——卵形のキャラクターは小さく弾むような足取りで、常につま先の先端だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらず、指のない短い腕は一歩ごとに楽しそうに揺れる。透明なキャラクターはその隣で、同じ楽しいペースに合わせて弾みながら進み、丸い体が水風船のようにやわらかく沈んでは弾んで戻る動きを繰り返す。その中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボール——は、弾むたびに重力に従って体の底に自然に沈み、常に光沢のある透明な体の中に完全に収まったままで、こぼれたり体の表面を突き抜けたりすることは一切ない。2人はこのまま同じ、楽しそうに笑いながらのフレームアウトを続け、画面右端へ向かって着実に進んでいき、透明なキャラクターのガムボールは依然としてまったく同じ固定された黄色4個・赤2個・水色1個・黄緑3個のまま、卵形のキャラクターの腕も依然として同じシンプルで指のない丸い形状のまま、2人が完全に画面右端の外へ出ていくまで続き、床は完全に誰もいない状態になり、<Picture 2>で示された誰もいない床とぴったり一致してこのショットの残りの時間を保つ。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2d_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 「むくっと起き上がって」を、寝転んだ状態からの起き上がりではなく
  「元気を取り戻すように姿勢を正す仕草」として解釈した。フレームアウトの
  方向(右)は仮の想定のため、違う場合は教えてください

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(ぽよん左・たまちゃん右、2人とも大笑い)
- Picture 2: いただいた画像2(誰もいない薄い黄緑色の床)
- モード: FL2VA
- 尺: 4.5秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- フレームアウトの方向(右方向と仮定)が実際の意図と合っているか確認すること
