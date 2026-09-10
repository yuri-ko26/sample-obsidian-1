---
project: H3-Video-Series-v2
cut: B-1
mode: FL2VA
status: draft
---

# カットB-1: メイン3人の頭上にぽよんが降りてきて、そのままカメラが寄ってドアップになる

## シーン内容
香勒表ビートB(「ゲスト登場」)の最初のカット。タイトル(3人のみ)が終わった直後、
メインキャラクター3人(ひよちゃん・たまちゃん・しまちゃん)が並んでいるところへ、
画面上からぽよんが降りてきて頭上に現れる。3人がそれを見上げるのと同時に、
カメラがぽよんへ寄っていき、最終的にぽよんの顔(輪郭線の目・口、中のガムボールと
紙吹雪)が画面いっぱいになるドアップで終わる。約4秒。この終わり方が、次のカット
(ぽよんのドアップから後ずさりしてたまちゃんとの2ショットに広がる/B-2)へ
自然につながるように設計している。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- ぽよんの中のガムボール・紙吹雪はこぼれない/数と色を変えない
- ぽよんの体は常に丸み(しずく型)を保つ、歪まない
- ひよちゃん・しまちゃん・たまちゃんの見た目はPicture 1のまま変化しない

## 参照画像
- Picture 1(最初のフレーム): 白背景、ひよちゃん(左)・たまちゃん(中央)・しまちゃん(右)の
  3人が並んで立ち、画面上部からぽよんが下半分だけフレームインして頭上に浮かんでいる構図。
  3人はぽよんの方を見上げている
- Picture 2(最後のフレーム): ぽよんの顔の極端なドアップ。輪郭線の目・口、頬のチーク、
  中の色とりどりのガムボールと紙吹雪が画面いっぱいに広がっている構図

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous shot begins in the wide framing shown in <Picture 1>, with the chick character, the egg-shaped character, and the tiger character standing together against the white background, all three looking upward at the transparent, jelly-like rubber character as it hangs partway into frame from above. All three characters keep their exact appearance and design from <Picture 1> unchanged throughout. The transparent character continues descending slowly and smoothly, its round body drifting downward at a gentle, floating pace, while the camera simultaneously pushes in toward it in one continuous, unbroken move, the framing steadily tightening around the transparent character as it descends. As the camera pushes closer, the three characters below gradually slide out of frame at the bottom and sides, no longer visible, while the transparent character's glossy round surface fills more and more of the frame. Its interior gumballs and confetti drift and shift gently inside without ever spilling out, and its round, dark eyes and flat, outline-only mouth grow larger and larger within the frame as the camera nears. By the end of the shot, the transparent character's face fills the entire frame in an extreme close-up, its round eyes, gently curved outline mouth, and soft blush cheeks surrounded by the colorful gumballs and confetti pressing close behind its glossy surface, matching the framing shown in <Picture 2> exactly.

overall_soundscape: A soft, airy descending tone as the transparent character drifts downward, mixed with the gentle rustle of the gumballs and confetti shifting inside it as the camera draws nearer.

non_diegetic_music: A light, curious, softly rising musical phrase that builds gently as the camera pushes in, landing on a warm, inviting note as the transparent character's face fills the frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>に示された通りのワイドな構図から始まる一続きのショットで、ひよこキャラクター・卵形のキャラクター・とらキャラクターの3人が白背景の前に並んで立ち、画面上部から半分だけフレームインして浮かんでいる透明でゼリーのようなラバーキャラクターを、全員が見上げている。3人とも<Picture 1>の見た目・デザインのまま最後まで変化しない。透明なキャラクターはゆっくりと滑らかに降下を続け、丸い体がふわりと漂うようなペースで下がっていく一方、カメラも同時に、一度も途切れることのない一続きの動きでそのキャラクターへ寄っていき、降下するにつれて画角がだんだんタイトになっていく。カメラが近づくにつれ、下にいた3人は画面の下端・両端からだんだん見えなくなっていき、透明なキャラクターの光沢のある丸い表面が画面をどんどん占めていく。中のガムボールと紙吹雪はやさしく揺れ動くがこぼれることはなく、丸い黒目と平面的で輪郭線だけの口は、カメラが近づくにつれて画面の中でどんどん大きくなっていく。ショットの終わりには、透明なキャラクターの顔が画面いっぱいの極端なドアップとなり、丸い目、やわらかくカーブした輪郭線の口、頬のやさしいチークの後ろに色とりどりのガムボールと紙吹雪が迫って見える構図となり、<Picture 2>とぴったり同じ画角で終わる。

**環境音**
透明なキャラクターが降下するあいだの、やわらかく空気を含んだような下降音に、カメラが近づくにつれて中のガムボールと紙吹雪が揺れ動くやさしい音が混ざる。

**BGM(観客のみに聞こえる)**
軽やかで好奇心をくすぐるような、静かに盛り上がっていくフレーズが、カメラが寄っていくにつれて高まり、透明なキャラクターの顔が画面いっぱいになる瞬間、温かく迎え入れるような音で着地する。

**生成結果**
- 動画ファイル: `03-generated-videos/B1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

### v2 (2026-09-10) — 2〜3秒の短い繋ぎカットとして再設計。ゆっくり漂うような降下・
push-inではなく、テンポの速いクイックな寄りに変更

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 3.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous shot begins in the wide framing shown in <Picture 1>, with the chick character, the egg-shaped character, and the tiger character standing together against the white background, all three looking upward at the transparent, jelly-like rubber character as it hangs partway into frame from above. All three characters keep their exact appearance and design from <Picture 1> unchanged throughout. The transparent character drops the rest of the way down at a brisk, energetic pace while the camera simultaneously pushes in toward it, in one swift, continuous, unbroken move — quicker than a slow drift but still smooth and readable, covering the full distance from the wide shot to an extreme close-up in a few seconds. As the camera rushes in, the three characters below quickly slide out of frame at the bottom and sides, no longer visible, while the transparent character's glossy round surface rapidly fills more and more of the frame. Its interior gumballs and confetti jostle and shift inside without ever spilling out, and its round, dark eyes and flat, outline-only mouth grow larger very quickly within the frame as the camera rushes nearer. By the end of the shot, the transparent character's face fills the entire frame in an extreme close-up, its round eyes, gently curved outline mouth, and soft blush cheeks surrounded by the colorful gumballs and confetti pressing close behind its glossy surface, matching the framing shown in <Picture 2> exactly.

overall_soundscape: A quick, airy whoosh as the transparent character drops and the camera rushes in, with a bright rattle of the gumballs and confetti shifting inside it.

non_diegetic_music: A short, quick, rising musical sting that lands on a bright, inviting note the instant the transparent character's face fills the frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の3.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>に示された通りのワイドな構図から始まる一続きのショットで、ひよこキャラクター・卵形のキャラクター・とらキャラクターの3人が白背景の前に並んで立ち、画面上部から半分だけフレームインして浮かんでいる透明でゼリーのようなラバーキャラクターを、全員が見上げている。3人とも<Picture 1>の見た目・デザインのまま最後まで変化しない。透明なキャラクターは元気で軽快なペースで残りの距離を降下し、同時にカメラも一度も途切れることのない一続きの動きでそのキャラクターへ寄っていく——ゆっくりとした漂うような動きよりは速いが、それでも滑らかで見やすい速度で、ワイドショットから極端なドアップまでの全距離を数秒でカバーする。カメラが勢いよく近づくにつれ、下にいた3人はすばやく画面の下端・両端から見えなくなっていき、透明なキャラクターの光沢のある丸い表面が急速に画面を占めていく。中のガムボールと紙吹雪は揺れ動くがこぼれることはなく、丸い黒目と平面的で輪郭線だけの口は、カメラが勢いよく近づくにつれて画面の中で急速に大きくなっていく。ショットの終わりには、透明なキャラクターの顔が画面いっぱいの極端なドアップとなり、丸い目、やわらかくカーブした輪郭線の口、頬のやさしいチークの後ろに色とりどりのガムボールと紙吹雪が迫って見える構図となり、<Picture 2>とぴったり同じ画角で終わる。

**環境音**
透明なキャラクターが降下し、カメラが勢いよく寄っていく瞬間の素早く空気を含んだ「ヒュッ」という音に、中のガムボールと紙吹雪が揺れる明るいカタカタという音が混ざる。

**BGM(観客のみに聞こえる)**
短く素早い、上昇するような音楽のスティングが、透明なキャラクターの顔が画面いっぱいになる瞬間に、明るく迎え入れるような音で着地する。

**生成結果**
- 動画ファイル: `03-generated-videos/B1_v2.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 3人+頭上のぽよんのワイドショット実画像
- Picture 2: ぽよんの顔ドアップ実画像
- モード: FL2VA
- 尺: v1=4秒 / v2=3.5秒(2〜3秒よりもう少し長くてもよいとのことで調整)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること(カメラが動くカットだが、あくまで1つの連続したショットとして描写する)
- 次のカット(ぽよんのドアップから後ずさりして2ショットに広がる想定)につながるよう、
  終了フレームの構図を合わせておくこと
