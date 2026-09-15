---
project: H3-Video-Series-v2
cut: E-2
mode: FL2VA(3枚参照)
status: draft
---

# カットE-2: たまちゃんがぽよんにピタッとくっついて、2人一緒に大きくジャンプ(俯瞰、カメラ寄り)

## シーン内容
Eビート(「ジャンプ」)2回目のカット。俯瞰の角度を保ったカメラ、Picture1の状態
(2人ともすでに起き上がって並んで立っている)から始まる。

1. たまちゃんがぽよんの方へ体を寄せ、ぴたっと体をくっつける(密着する)——
   この時点の見た目がPicture2
2. 密着したまま、2人一緒に(タイミングを合わせて)真上に大きくジャンプする
3. カメラは**俯瞰の角度を保ったまま**、2人に向かって寄っていき(ズームイン/
   プッシュイン)、ジャンプの頂点では2人がフレームいっぱいに大きく、嬉しそうな
   満面の笑顔で映る——この時点の見た目がPicture3

**設計メモ**: 3枚の参照画像(くっつく前の全体像/くっついた直後・ジャンプ前/
ジャンプの頂点でカメラに寄った状態)を順番にいただいたため、v2でPicture1・
Picture2・Picture3の3枚をタイムライン上に位置づけるFL2VA形式に変更した
(「Picture 1 ... aligns with 0.00s; Picture 2 ... aligns with X秒; Picture 3 ...
aligns with Y秒」という並びを拡張)。「カメラに近づいてください」「カメラは
俯瞰カメラのままです」というご指示どおり、俯瞰の角度そのものは変えないまま
(上から見下ろす視点のまま)、Picture1→Picture2→Picture3にかけて徐々に
プッシュインしていく。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの移動:踵をつけず、足首を曲げない棒状の足のまま
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(0.00秒・最初のフレーム): いただいた画像1。俯瞰、薄い黄緑色の床。
  左側にぽよん、右側にたまちゃんが並んで立っている構図(2人ともすでに起き上がった
  状態、くっつく前)
- Picture 2(くっついてジャンプする直前): いただいた画像2。たまちゃんがぽよんに
  ぴたっと体を寄せてくっついている構図。カメラ距離はPicture1よりやや寄っている
- Picture 3(ジャンプの頂点・カメラに近い状態): いただいた画像3。2人がくっついた
  まま、カメラにかなり寄った状態で画面いっぱいに映り、2人とも満面の笑顔

## プロンプト履歴

### v2 (2026-09-15) — 現在の採用版(3枚の参照画像でタイムラインを明確化)

3枚の参照画像を時系列に沿って割り当てたFL2VA形式に変更。Picture1(くっつく前)→
Picture2(くっついた直後・ジャンプ前)→Picture3(ジャンプの頂点・カメラが寄った
状態)という3点をタイムライン上に明記し、その間の動き(体を寄せる→しゃがんで
力をためる→ジャンプ→カメラが俯瞰のまま寄っていく)を記述した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 2.50-second mark of the target video; Picture 3 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot begins in the position and framing established by <Picture 1>, looking straight down on the pale yellow-green floor, with the transparent, jelly-like rubber character and the egg-shaped character already standing upright side by side, matching their exact appearance, expression, and position from <Picture 1>. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. The egg-shaped character steps toward the transparent character, walking up on the very tips of its toes only, its heels never touching the ground, its short stiff legs never bending at the ankle, until it presses itself snugly right up against the transparent character's side, the two of them now touching, nestled closely together. As they come together like this, the camera keeps its overhead angle but pushes in slightly closer toward the pair, until, at the same moment they finish pressing together, the framing, distance, and pose exactly match <Picture 2>. From this closely nestled position, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera's overhead push-in continues at a matched pace, moving closer and closer toward the pair, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 3> at the end of the shot. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shift and tumble inside with the motion of the jump, always staying fully contained inside its glossy transparent body, never spilling out.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の2.50秒地点に、Picture 3(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは<Picture 1>で確立された位置・フレーミングから始まり、薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、<Picture 1>のとおりの見た目・表情・位置のまま、すでに並んで直立している。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。卵形のキャラクターは、常につま先の先端だけで立ち、踵は地面に一切つけず、短く硬い脚は足首でどの瞬間も曲がらないまま、透明なキャラクターの方へ歩み寄り、透明なキャラクターの体の横にぴたっと寄り添うように押し付け、2人は触れ合い、ぴったりとくっついた状態になる。このように体を寄せていく間、カメラは俯瞰の角度を保ったまま2人へ向かってわずかに寄っていき、体を寄せ終えるのとちょうど同じ瞬間に、フレーミング・距離・ポーズが<Picture 2>とぴったり一致する。この密着した状態から、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラの俯瞰プッシュインも同じペースで続き、2人へ向かってどんどん近づいていき、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、<Picture 3>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致してこのショットが終わる。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪——は、ジャンプの動きに合わせて揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、こぼれることは一切ない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 3枚の参照画像(くっつく前/くっついた直後・ジャンプ前/ジャンプの頂点で
  カメラに寄った状態)をタイムライン上に位置づけたFL2VA版。3枚のPictureを
  使う構文は本プロジェクトで初めての試みのため、うまく機能するか要検証

### v1 (2026-09-15) — 旧版(参照画像1枚のみ、I2VA)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single overhead shot looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>, where the transparent, jelly-like rubber character and the egg-shaped character both already stand upright side by side. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The camera keeps the exact same overhead, bird's-eye viewing angle throughout the entire shot, looking straight down at all times and never tilting, panning, or switching to a side or angled view — but it does slowly push in closer toward the two characters as the shot progresses, the framing gradually tightening around them. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language. The egg-shaped character steps toward the transparent character, walking up on the very tips of its toes only, its heels never touching the ground, its short stiff legs never bending at the ankle, until it presses itself snugly right up against the transparent character's side, the two of them now touching, nestled closely together. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit. As they rise, the camera's push-in continues at a matched pace, so that by the time they reach the peak of this big jump, the two of them together fill almost the entire frame, seen from directly overhead the whole time. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shift and tumble inside with the motion of the jump, always staying fully contained inside its glossy transparent body, never spilling out. After reaching the peak, both characters descend back down together under gravity, still pressed closely side by side, landing back on the floor at the same spot they jumped from, their bodies compressing slightly on landing before settling back into their normal resting shapes, the camera holding this close, filled-frame overhead framing at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の俯瞰ショットで、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、透明でゼリーのようなラバーキャラクターと卵形のキャラクターがどちらもすでに並んで直立している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく最後まで保たれる。カメラはショット全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ないが、ショットが進むにつれて2人に向かってゆっくりとプッシュインしていき、フレーミングは徐々に2人を中心にタイトになっていく。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きだけで表現する。卵形のキャラクターは、常につま先の先端だけで立ち、踵は地面に一切つけず、短く硬い脚は足首でどの瞬間も曲がらないまま、透明なキャラクターの方へ歩み寄り、透明なキャラクターの体の横にぴたっと寄り添うように押し付け、2人は触れ合い、ぴったりとくっついた状態になる。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようである。2人が上昇するのに合わせて、カメラのプッシュインも同じペースで続き、この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、終始真上から見た状態のまま映る。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪——は、ジャンプの動きに合わせて揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、こぼれることは一切ない。頂点に達した後、2人は密着したまま一緒に重力に従って下降し、跳んだのと同じ場所に着地し、着地の瞬間に体をわずかに圧縮させてから、それぞれ通常の休息姿勢に落ち着く——カメラはショットの終わりまで、この寄った・フレームいっぱいの俯瞰フレーミングを保ち続ける。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 「たまちゃんがポヨンにピタッとくっついて一緒に大きくジャンプ」+「カメラは
  俯瞰のまま寄っていく」というご指示への対応版。俯瞰の角度自体は変えず、
  プッシュインズームのみで「フレームいっぱいになる」効果を出している

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(俯瞰、ぽよん左・たまちゃん右で並んで立つ、くっつく前)
- Picture 2: いただいた画像2(たまちゃんがぽよんにくっついた直後、ジャンプ前)
- Picture 3: いただいた画像3(ジャンプの頂点、カメラに寄った状態、2人とも満面の笑顔)
- モード: FL2VA(Picture 1〜3の3枚参照、ComfyUI側で3枚とも読み込ませる設定に
  なっているか確認してください)
- 尺: 6秒目安(体を寄せる2.5s/しゃがんで力をため→ジャンプ上昇→頂点3.5s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 俯瞰角度を保ったままのプッシュインズームという、D-beatとは異なるカメラワークの
  カットのため、生成後の見え方に違和感があればフィードバックをください
- 3枚のPictureを使う構文は本プロジェクトで初めての試み。もしComfyUI側が
  3枚同時の参照に対応していない場合は、Picture2を省略してPicture1→Picture3の
  2枚構成に戻すことも検討してください
