---
project: H3-Video-Series-v2
cut: D-2c
mode: FL2VA
status: draft
---

# カットD-2c: ぽよん単独・画面右端でくるっと回転してフレームアウトする(俯瞰)

> **注記**: シートの「D-3(2回目・行き)」は往復3回のうち2回目の2人同時カットの
> プレースホルダーであり、本カットとは別物です。本カットはぽよん一人だけが
> 映っている参照画像から作成した単独カットのため、`D-2c`として区別しています。

## シーン内容
俯瞰固定カメラ、ぽよん一人が画面右寄りに立っている状態から、くるっと回転しながら
画面右端の外へフレームアウトし、誰もいない床になって終わる短いカット。

**設計メモ**: D-1・D-2で確立した「回転軸を体に固定された物理構造として明記する」
手法・「顔は体表面の固定パーツとして体の回転と一体で動く」を踏襲。ガムボールの
色が変わってしまう不具合(F-10で判明)への対策として、回転中もガムボールの
正確な数・色の組み合わせを繰り返し明記する。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、こぼれない・色が変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- 顔(目・口)は体の表面に属する固定パーツであり、体の回転と一体で動く
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(最初のフレーム): いただいた画像1。薄い黄緑色の床を真上から見下ろす
  構図。画面右寄りにぽよん一人が立っている(たまちゃんは映っていない)
- Picture 2(最後のフレーム): いただいた画像2。誰もいない、無地の薄い黄緑色の床のみ

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 2.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor exactly as shown in <Picture 1>, with the transparent, jelly-like rubber character standing alone near the right side of the frame, matching its exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. The transparent character never speaks, talks, or makes any vocalization at any point — it stays completely silent throughout. Its body behaves as if mounted on a single rigid, invisible axle running straight through its center, lying flat against the floor and oriented perpendicular to its direction of travel — this axle is the only line its body is able to rotate around; it is not capable of spinning flat around a vertical axis like a top or a coin, that kind of flat spinning is structurally impossible for it and never happens. Critically, its face — its eyes and mouth — is a fixed part of its body's surface, permanently attached to one spot on it; as its body rotates around its axle, its face rotates together with it as one rigid piece, turning out of view and back into view with each full rotation, never staying fixed in the same on-screen position while the body spins independently. With a quick, cute little motion, the transparent character rolls forward around this fixed horizontal axle, end over end like a wheel, tumbling briskly toward the right edge of the frame, its top and bottom steadily alternating into view with each rotation. Throughout this entire roll, its interior gumballs remain exactly the same fixed set — precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing at any point, never shifting to any other colors, plus colorful confetti — always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point, settling naturally at the bottom under gravity between rotations, tumbling and jostling against each other and the inner wall with each turn, clearly visible the whole time through its glossy transparent skin. It continues rolling steadily rightward this way, moving briskly off the floor, until it fully exits past the right edge of the frame, leaving the floor completely empty, exactly matching the empty floor shown in <Picture 2> for the remainder of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の2.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターが画面右寄りに一人で立っている、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。透明なキャラクターは一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。その体は、中心をまっすぐ貫く一本の硬い、目に見えない軸に取り付けられているかのように振る舞う——この軸は床と平行に寝かされ、進行方向に対して垂直に向いている——この軸だけが、その体が回転できる唯一の線であり、コマやコインのように垂直な軸のまわりで平面的に回転することは構造上不可能であり、一切起こらない。極めて重要な点として、その顔(目と口)は体の表面に属する固定された一部分であり、体の一箇所に恒久的に付着している——体が軸のまわりを回転すると、顔も体と一体の硬いパーツとして一緒に回転し、一回転するごとに見えなくなったりまた見えたりし、体が独立して回転する間、顔が画面上の同じ位置に固定されたままになることは一切ない。透明なキャラクターは、素早く可愛らしい動きで、この固定された水平の軸のまわりを、車輪のように端から端まで転がりながら、画面右端に向かって軽快に転がっていき、一回転するごとに上面と下面が着実に交互に見える。この転がりの間ずっと、中のガムボールはまったく同じ固定された組み合わせのままである——正確に黄色4個・赤2個・水色1個・黄緑3個、合計10個、この数と色の組み合わせはどの瞬間も一切変わらず、他の色に変化することもなく、プラスカラフルな紙吹雪——常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはなく、回転と回転の間は重力に従って底に自然に沈み、一回転するたびにお互いや内壁とぶつかりころころと転がり、光沢のある透明な体を通して終始はっきりと見える。このまま右方向へ軽快に転がり続け、床の上を軽やかに進み、ついに画面右端を完全に越えてフレームアウトし、床は完全に誰もいない状態になり、<Picture 2>で示された誰もいない床とぴったり一致してこのショットの残りの時間を保つ。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D2c_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(ぽよん一人、画面右寄り)
- Picture 2: いただいた画像2(誰もいない床)
- モード: FL2VA
- 尺: 2.5秒目安(くるっと回転してすぐフレームアウトする短いカットのため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
