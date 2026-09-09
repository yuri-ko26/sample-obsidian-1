---
project: H3-Video-Series-v2
cut: D-1
mode: I2VA
status: draft
---

# カットD-1: 俯瞰固定カメラ、画面左からフレームイン→中央を水平にコロコロ転がって右へフレームアウト

## シーン内容
クライアント要望どおり、俯瞰の固定カメラで、2人が画面左から入ってきて、画面中央を
水平にコロコロと転がって移動し、右側へフレームアウトする。単一の固定ショット。

**設計メモ**: 旧アーカイブ(シーン24〜27)で「回転の物理」表現に何度も試行錯誤した
経緯がある。今回は最終的に一番安定していた「前転(でんぐり返し)/カートホイール、
正面→背中→正面、を規則正しく繰り返す」表現をベースに採用。斜め回転になる問題を
避けるため「水平を保つ・斜めにならない」を強く明記している。生成後、回転の見え方に
違和感があれば、その場で微調整する想定。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは転がる間、短い手を上に上げたままの姿勢
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない
- 顔(目・口)は体の片面にしかないため、回転中に顔と体の向きの整合性を保つ

## 参照画像
- Picture 1(最初のフレーム): 薄い黄緑色の床を真上から見下ろす構図。画面左寄りに、
  左側にぽよん(画面左端に触れる程度の位置)、その右にたまちゃんが並び、右側に
  大きな余白が広がっている

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg-shaped character, on the right of the pair, has both of its short arms raised up the whole time, and continuously somersaults forward across the floor in a straight, even cartwheel motion, its front and back alternating into view with each full turn — front, then back, then front again, repeating steadily as it advances — the same way a rolling ball toy tumbles forward end over end. It stays perfectly level as it tumbles, never tilting or wobbling off to one side or spinning diagonally, and it never rises up or stands. Beside it on the left, the transparent, jelly-like rubber character tumbles forward the same clean, even way, like a ball continuously rolling end over end, its own front and back alternating into view with each turn just as steadily, its interior gumballs and confetti shifting inside without ever spilling out. Both continue tumbling forward together at a matched pace, moving steadily rightward across the frame, until they fully exit past the right edge, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。ペアの右側にいる卵形のキャラクターは、両手をずっと上に上げた状態のまま、まっすぐで均等な前転(でんぐり返し)のような動きで床の上を継続的に前へ転がっていき、一回転するごとに正面と背中が交互に見える——正面、そして背中、そしてまた正面、というのを進みながら規則正しく繰り返す。ちょうど転がるボール型のおもちゃが端から端へ回転しながら進むのと同じ動きである。転がっている間は常に体が水平・水準を保ったまま転がり、決して片側に傾いたり、斜めに揺れたり、斜め回転したりすることはなく、途中で起き上がったり立ち上がったりすることも一切ない。その左隣では、透明でゼリーのようなラバーキャラクターも同じように、ボールが端から端まで滑らかに転がるように前転し、こちらも一回転ごとに正面と背中が交互に規則正しく見え、中のガムボールと紙吹雪は揺れ動くがこぼれることはない。二人はこのままペースを合わせて前転を続けながら画面を右方向へまっすぐ横切り、完全に右端の外へ出ていき、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 今回いただいた画像(ぽよん左端寄り・たまちゃんその右、余白が右側)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 回転が斜めになる/回転の向きがおかしいなど違和感があれば、その場でフィードバックをください
