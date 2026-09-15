---
project: H3-Video-Series-v2
cut: D-2
mode: I2VA
status: draft
---

# カットD-2: 俯瞰固定カメラ、反対方向へコロコロ転がりながらフレームアウト(単調にならないよう多少歪みを加えたバージョン)

## シーン内容
D-1とは反対方向へ、俯瞰の固定カメラで2人が転がりながら画面外へフレームアウトする
カット。D-1(v9)のようにきっちり水平・一定ペースで転がるのではなく、**多少歪に、
速度やタイミングにばらつきをつけて、単調にならないようにする**ことを重視。

**設計メモ**: D-1で確立した「回転軸を体に固定された物理構造として明記する」
手法をベースに、そこへ意図的な「不完全さ」を加える——
- 転がる速さが一定ではなく、時々わずかに速くなったり遅くなったりする
- 進む経路もまっすぐ一直線ではなく、わずかに上下(画面内でのふらつき)をともないながら
  全体としては同じ方向へ進む
- ただし、回転軸自体が斜めに傾いたり、平面内でその場回転(コマ状)になったりする
  ことは絶対に避ける(過去の失敗パターン)。あくまで「速度・経路のばらつき」だけで
  歪さ・自然さを出し、回転そのものの構造(軸)は崩さない

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは転がる間、短い手を上に上げたままの姿勢
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、こぼれない
- 顔(目・口)は体の表面に属する固定パーツであり、体の回転と一体で動く(D-1での教訓)
- セリフ・発話・音声は一切なし(D-1での教訓)

## 参照画像
- Picture 1(最初のフレーム): D-1と同じ俯瞰画像(薄い黄緑色の床、画面左寄りに
  ぽよん・たまちゃんが並び、右側に余白)

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout. Each character's body behaves as if it were mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to its direction of travel — this axle is the only line either character's body is able to rotate around; neither character is capable of spinning around a vertical axis like a top or a coin lying flat on a table, that kind of flat, in-place spinning is structurally impossible for them and never happens at any point, and the axle itself never tilts diagonally at any point either. Critically, each character's face — its eyes and mouth — is a fixed part of its body's surface, permanently attached to one spot on it; as the body rotates around its axle, the face rotates together with it as one rigid piece, turning out of view and back into view with each full rotation, never staying fixed in the same on-screen position while the body spins independently. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and rolls forward around this fixed horizontal axle, end over end like a wheel, front and back steadily alternating into view with each rotation. Rather than rolling at one perfectly even, mechanical pace, its rotation speed varies naturally and unevenly as it goes — sometimes rotating a little quicker for a few turns, then a little slower for the next few, unevenly and unpredictably rather than in any regular pattern — and its path across the floor wanders very slightly up and down within the frame as it goes, rather than tracking one perfectly straight line, giving it a charmingly imperfect, slightly lopsided quality, even though its axle itself always stays level and perpendicular to its overall direction of travel, never tilting diagonally. Beside it, the transparent, jelly-like rubber character rolls forward around its own fixed horizontal axle the same way — end over end like a wheel, its top and bottom alternating with each rotation, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — tumbling and jostling inside with each rotation without ever spilling out — and it has its own slightly uneven rotation speed and slightly wandering path as well, independent from the egg character's own variations, so the two of them roll along together with a natural, lively, not-quite-synchronized quality rather than moving like two identical mechanical wheels. Both continue rolling forward this way, each with their own small variations in speed and path, moving steadily overall in the same direction across the frame, until both of them fully exit past the edge of the frame, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。それぞれのキャラクターの体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞う——この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——どちらのキャラクターも、体が回転できるのはこの軸のまわりだけである。コマやテーブルの上に横たわったコインのように、垂直な軸のまわりで平面的にその場で回転することは、どちらのキャラクターにとっても構造上不可能であり、どの瞬間にも一切起こらず、軸自体が斜めに傾くこともどの瞬間にも一切ない。極めて重要な点として、それぞれのキャラクターの顔(目と口)は体の表面に属する固定された一部分であり、体の一箇所に恒久的に付着している——体が軸のまわりを回転すると、顔も体と一体の硬いパーツとして一緒に回転し、一回転するごとに見えなくなったりまた見えたりし、体が独立して回転する間、顔が画面上の同じ位置に固定されたままになることは一切ない。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、この固定された水平の軸のまわりを、車輪のように端から端まで転がっていき、一回転するごとに正面と背中が着実に交互に見える。完全に均一で機械的なペースで転がるのではなく、その回転速度は進みながら自然に、不均一に変化する——数回転だけ少し速く回転し、次の数回転は少し遅く、規則性のない不規則なパターンで——また、床を進む経路も完全にまっすぐな一直線をたどるのではなく、画面内でごくわずかに上下にふらつきながら進む。これにより、愛嬌のある、少し不揃いな雰囲気が生まれるが、それでもその軸自体は常に水準を保ち、全体の進行方向に対して垂直なままで、決して斜めに傾くことはない。その隣では、透明でゼリーのようなラバーキャラクターも、自分自身の固定された水平の軸のまわりを同じように転がっていく——車輪のように端から端まで転がり、一回転するごとに上面と下面が入れ替わり、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は一回転するごとに転がりぶつかり合うが、こぼれることは一切ない——そしてこちらも、卵形のキャラクターとは独立した、独自のわずかに不均一な回転速度とわずかにふらつく経路を持つため、2人はまったく同じ機械的な車輪のように動くのではなく、自然で生き生きとした、ぴったりとは揃わない雰囲気で一緒に転がっていく。2人ともこのまま、それぞれ独自の小さな速度・経路のばらつきを持ちながら転がり続け、全体としては画面を同じ方向へ着実に進んでいき、ついに2人とも画面端を完全に越えてフレームアウトし、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D2_v1.mp4`(未生成)
- 判定: 未検証
- メモ: D-1で確立した回転軸の仕組み(+顔の追従、+セリフなし)をベースに、
  速度・経路にわずかな不規則性を加えて単調さを避けたバージョン

## ComfyUIでの設定メモ
- Picture 1: D-1と同じ画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 「歪み」は速度・経路のばらつきのみで表現し、回転軸自体を斜めにしたり
  平面回転にしたりしないこと(過去の失敗パターンを避けるため)
