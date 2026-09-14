---
project: H3-Video-Series-v2
cut: G-0
mode: FL2VA
status: draft
---

# カットG-0: 誰もいない雲から、たまちゃん→ぽよんの順にひょこっと登場し、目が合って笑い合う(Gビートの導入カット)

## シーン内容
Gビート(「いないいないばあ」)の直前に入る導入カット。誰もいない雲の風景から始まり、
たまちゃんが先に、続いてぽよんがそれぞれ雲の陰からひょこっと顔を出すように登場し、
最後は2人が目を合わせて笑い合うところまで。正面固定カメラ。

1. Picture1の状態(誰もいないパステルカラーの雲の風景)から始まる
2. たまちゃんが先に、画面右上の紫色の雲の向こう側からひょこっと顔・体を出すように現れ、
   その雲の頂上に腰掛ける
3. 少し間があって、ぽよんが画面中央下寄り(ピンクとミントの雲の境目あたり)から
   ひょこっと現れる
4. 2人が互いに気づいて目を合わせ、嬉しそうに笑い合う。Picture2で示された通りの
   位置・構図・表情で終わる

**設計メモ**: 最初のフレームには誰も映っていないが、最後のフレームに2人の見た目が
はっきり映っているため、FL2VAとして両方を参照させることでモデルが2人の見た目を
anchoring できる(プロジェクトの標準手法)。また「何もない状態から忽然と現れる」
不安定さを避けるため、2人とも**雲の陰・向こう側から顔を出すように登場する**
(「ひょこっと」の動き自体が、いきなり空間に出現するのではなく雲の稜線の向こうから
迫り上がってくる自然な動きになるよう記述している)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。笑顔になっても崩れない

## 参照画像
- Picture 1(最初のフレーム): 誰もいないパステルカラーの雲の風景(いただいた画像1)
- Picture 2(最後のフレーム): たまちゃんが右上の紫の雲の頂上に腰掛けて大笑いし、
  ぽよんが中央下寄り(ピンクとミントの雲の境目)で笑っている構図(いただいた画像2)

## プロンプト履歴

### v1 (2026-09-14)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel cloud landscape exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. The egg character never has eyebrows at any point. First, the egg-shaped character pops up from behind the tall purple cloud in the upper right, rising up over its crest as if it had been hiding just behind it, its head and body gradually coming into view from below the cloud's edge until it settles sitting on top of the purple cloud, its legs dangling over the edge, never bending at the ankle and never letting its heels touch the cloud's surface. A moment later, the transparent, jelly-like rubber character pops up in a similar way from between the pink and mint-green clouds near the lower center of the frame, rising into view from behind the cloud's edge rather than appearing out of nowhere, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, gently rolling and jostling against each other and the inner wall as it moves, shifting without ever spilling out. Once both characters have settled into place, they notice each other and turn to make eye contact, and together they break into delighted, happy laughter. The egg character's round dot eyes crinkle into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the same moment, the transparent character's round eyes crinkle shut into laughing crescents as well, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — this smiling mouth stays exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline the whole time. By the end of the shot, both characters are settled happily laughing together, matching the exact positions, poses, and expressions shown in <Picture 2>.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲の風景を映しており、最初は誰も映っていない。カメラは一切パン・チルト・ズーム・カットをしない。卵形のキャラクターにはどの瞬間も眉毛はつかない。まず、卵形のキャラクターが画面右上の背の高い紫色の雲の向こう側から、まるでその陰に隠れていたかのようにひょこっと顔・体を出す——雲の稜線の下から頭と体が少しずつ見えてくるようにして現れ、最終的に紫の雲の頂上に腰掛ける。足は雲の縁からぶらぶらと垂らし、足首は曲げず、踵が雲の表面につくこともない。少し間があって、今度は透明でゼリーのようなラバーキャラクターが、画面中央下寄りのピンクとミントグリーンの雲の間から、同じように何もないところから突然現れるのではなく雲の縁の向こうから迫り上がるようにしてひょこっと現れる——中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、動くたびにお互いや内壁にぶつかってやさしくころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪はこぼれることはない。2人ともその場に落ち着いた後、互いの存在に気づいて目を合わせ、一緒に嬉しそうな笑い声を上げる。卵形のキャラクターの丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。同じ瞬間、透明なキャラクターの丸い目もぎゅっと閉じて笑いじわの三日月形になり、口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。ショットの終わりには、2人とも一緒に嬉しそうに笑い合っている状態に落ち着き、<Picture 2>で示された通りの位置・ポーズ・表情とぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/G0_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(誰もいない雲の風景)
- Picture 2: いただいた画像2(たまちゃん・ぽよんが登場して笑い合っている構図)
- モード: FL2VA
- 尺: 6秒目安(たまちゃん登場→ぽよん登場→目が合って笑い合うまで)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 「何もないところから忽然と現れる」ではなく「雲の陰から迫り上がるように現れる」と明記すること(空フレーム登場の不安定さ対策)
