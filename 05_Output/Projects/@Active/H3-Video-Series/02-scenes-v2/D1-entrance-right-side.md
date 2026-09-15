---
project: H3-Video-Series-v2
cut: D-1-entrance-right
mode: FL2VA
status: draft
---

# カットD-1-entrance-right: 誰もいない床から2人が画面右側へ転がってフレームインする

## シーン内容
誰もいない薄い黄緑色の床から始まり、2人が画面右端から転がってフレームインして
きて、画面右寄りの位置(Picture2)に到着するところまで。左側には広い余白が残る。
俯瞰固定カメラ。既存の`D-1-entrance`(画面左からフレームイン)と対になる、
右側からのフレームイン版。

**設計メモ**: D-1・D-1-entranceで確立した「回転軸を体に固定された物理構造として
明記する」手法・「顔は体表面の固定パーツとして体の回転と一体で動く」・
「セリフ・発話は一切なし」をすべて踏襲。Picture2ではぽよん・たまちゃんとも
回転前の静止した見た目のため、「Picture2の見た目に向かって回転しながら進み、
そこで自然に停止する」という記述にした。

> **要確認**: このカットが物語のどの位置に入るか(例: D-2「帰り」カットの
> 直前の導入、または新しい往復の導入など)について、具体的なご指示があれば
> 教えてください。ひとまずいただいた画像どおりのプロンプトを用意しました。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは転がる間、短い手を上に上げたままの姿勢
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、こぼれない
- 顔(目・口)は体の表面に属する固定パーツであり、体の回転と一体で動く
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(最初のフレーム): いただいた画像1。誰もいない、無地の薄い黄緑色の床のみ
- Picture 2(最後のフレーム): いただいた画像2。画面右寄りに、ぽよん・たまちゃんが
  並んで立つ(回転前の静止した見た目)。左側に大きな余白が残る

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout. From the right edge of the frame, the transparent, jelly-like rubber character and the egg-shaped character roll into view together, traveling leftward, each character's body behaving as if mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to their direction of travel — this axle is the only line either character's body is able to rotate around, and neither character is capable of spinning flat around a vertical axis like a top or a coin, that kind of flat spinning is structurally impossible for them and never happens. Critically, each character's face — its eyes and mouth — is a fixed part of its body's surface, permanently attached to one spot on it; as each body rotates around its axle, its face rotates together with it as one rigid piece, turning out of view and back into view with each full rotation, never staying fixed in the same on-screen position while the body spins independently. The egg-shaped character rolls forward around its fixed horizontal axle, end over end like a wheel, its two short arms raised up the whole time, its front and back steadily alternating into view with each rotation. Beside it, the transparent character rolls forward around its own fixed horizontal axle the same way, end over end like a wheel, its top and bottom alternating with each rotation, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — tumbling and jostling inside with each rotation without ever spilling out. Both characters roll into frame together this way, entering steadily from the right edge and traveling leftward, gradually advancing further onto the floor and becoming more visible with each moment. Both continue rolling leftward at a matched pace until they reach the positions shown in <Picture 2>, coming to a natural, gentle stop there, settling into a calm, upright standing pose side by side near the right portion of the frame, with open floor stretching out to their left, in the exact same static framing as the opening frame, matching <Picture 2> exactly at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り誰もいない薄い黄緑色の床を真上から見下ろしている。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。画面右端から、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが一緒に、左方向へ進みながら転がりフレームインしてくる——それぞれのキャラクターの体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞い、この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——この軸だけが、どちらのキャラクターの体も回転できる唯一の線であり、どちらのキャラクターもコマやコインのように垂直な軸のまわりで平面的に回転することは構造上不可能であり、一切起こらない。極めて重要な点として、それぞれのキャラクターの顔(目と口)は体の表面に属する固定された一部分であり、体の一箇所に恒久的に付着している——それぞれの体が軸のまわりを回転すると、顔も体と一体の硬いパーツとして一緒に回転し、一回転するごとに見えなくなったりまた見えたりし、体が独立して回転する間、顔が画面上の同じ位置に固定されたままになることは一切ない。卵形のキャラクターは、この固定された水平の軸のまわりを、車輪のように端から端まで転がっていき、短い両腕はずっと上に上げたままで、一回転するごとに正面と背中が着実に交互に見える。その隣では、透明なキャラクターも自分自身の固定された水平の軸のまわりを同じように転がっていく——車輪のように端から端まで転がり、一回転するごとに上面と下面が入れ替わり、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は一回転するごとに転がりぶつかり合うが、こぼれることは一切ない。2人はこのようにして一緒に、画面右端から左方向へ進みながら転がってフレームインし、時間が経つにつれて床の上でその姿がだんだんはっきりと見えるようになっていく。2人はこのままペースを合わせて左方向へ転がり続け、<Picture 2>に示された位置に到達したところで、そこで自然に穏やかに止まり、画面右寄りで並んで落ち着いた立ち姿勢に収まり、左側にはまだ床が広がっている——最初のフレームとまったく同じ固定構図のまま、<Picture 2>とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-entrance-right_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(誰もいない薄い黄緑色の床)
- Picture 2: いただいた画像2(画面右寄りにぽよん・たまちゃんが並ぶ、左側に余白)
- モード: FL2VA
- 尺: 4秒目安(短い導入カットのため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
