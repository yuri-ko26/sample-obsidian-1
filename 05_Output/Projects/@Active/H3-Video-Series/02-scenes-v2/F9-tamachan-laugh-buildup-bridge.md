---
project: H3-Video-Series-v2
cut: F-9
mode: FL2VA
status: draft
---

# カットF-9: たまちゃんの笑顔がだんだん大きくなっていく短い繋ぎカット(画像1→画像2)

## シーン内容
ほぼ同じ構図の2枚の画像(画像1=たまちゃんが控えめな笑顔・ぽよんが笑顔で並んでいる、
画像2=たまちゃんがより大きく口を開けて笑い、腕も少し弾んでいる)を自然に繋ぐ、
2〜3秒程度の短いカット。正面固定カメラ。

1. Picture1の状態(たまちゃんが控えめな笑顔、ぽよんが笑顔)から始まる
2. たまちゃんの笑顔がだんだん大きくなっていき、それに合わせて腕も楽しそうに
   小さく弾む・揺れる
3. ぽよんは表情は変えないが、完全に静止した置物のようにはせず、浮遊している
   キャラクターらしい**ふわふわとした小さな上下の浮き沈み**(中のガムボールも
   それに合わせてやさしく揺れる)を保つ。笑顔そのものは変えない
4. 最終的にPicture2で示された通りの、より大きく開けた笑顔・腕の位置で終わる

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし(D-1での教訓)

## 参照画像
- Picture 1(最初のフレーム): いただいた画像1。たまちゃんが控えめな笑顔で立ち、
  ぽよんが紫の雲の頂上付近で笑顔のまま浮かんでいる構図
- Picture 2(最後のフレーム): いただいた画像2。同じ構図で、たまちゃんがより大きく
  口を開けて笑っており、腕も少し上がった/弾んだ位置になっている

## プロンプト履歴

### v2 (2026-09-15) — 現在の採用版(ぽよんに自然な浮遊の微動を追加)

F-10と同じ理由(「完全静止だと不自然」)で、ぽよんに笑顔は変えないまま
ふわふわとした浮遊の上下動を追加した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 2.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing with a modest, happy smile and the transparent, jelly-like rubber character hovering near the purple cloud with its own happy smile, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything through body language and expression alone. The egg character never has eyebrows at any point. Over the course of this short shot, the egg character's smile steadily grows bigger and more joyful, its mouth opening wider and wider, its round dot eyes crinkling further into happy creases, as pure delight builds up in it — and in step with this growing joy, its short arms lift and swing a little, bouncing gently and cheerfully with the building happiness, its short stiff legs staying always up on the very tips of their toes, its heels never touching the ground. The transparent character keeps its smiling expression completely unchanged throughout — the same steady, happy smile it had at the very start, with no shift or transition of any kind — but it is not perfectly frozen either: being a soft, hovering, jelly-like character, it gently bobs and drifts up and down by a small amount the whole time, a light, natural floating motion, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — swaying and settling gently inside with this soft bobbing, clearly visible throughout, its mouth remaining a thin, dark, uncolored outline the entire time, staying just as transparent as the rest of its glossy body. By the end of this short shot, the egg character's smile and arm position have grown into the bigger, more joyful laugh and slightly raised, bouncing arm position shown in <Picture 2>, matching it exactly, while the transparent character continues its same gentle hovering motion beside it.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の2.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターは控えめな嬉しそうな笑顔で立ち、透明でゼリーのようなラバーキャラクターは紫の雲のそばで自分自身の嬉しそうな笑顔のまま浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動き・表情だけで表現する。卵形のキャラクターにはどの瞬間も眉毛はつかない。この短いショットが進む間、卵形のキャラクターの笑顔は着実にどんどん大きく、より喜びに満ちたものになっていき、口はどんどん大きく開き、丸い点目はさらに笑いじわに細まっていく——純粋な喜びが体の中にこみ上げてくるかのように。そしてこの高まる喜びに合わせて、短い両腕が持ち上がって少し揺れ、高まる嬉しさとともにやさしく楽しそうに弾む——短く硬い脚は常につま先の先端だけで立ったままで、踵はどの瞬間も地面につかない。透明なキャラクターは、笑顔の表情を終始まったく変えない——最初と同じ、変わらぬ嬉しそうな笑顔のままで、切り替わりや移行は一切ないが、かといって完全に静止しているわけでもない——柔らかく浮遊するゼリー状のキャラクターらしく、この間ずっと小さくふわふわと上下に揺れ漂う、軽く自然な浮遊の動きを見せ、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——はこのやさしい上下動に合わせて中で揺れ落ち着き、はっきりと見え続け、口は終始薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままである。この短いショットの終わりには、卵形のキャラクターの笑顔と腕の位置は、<Picture 2>で示された、より大きく喜びに満ちた笑い声と、少し上がって弾んだ腕の位置へと成長しており、それとぴったり一致する——その一方で、透明なキャラクターはそのすぐそばで同じやさしい浮遊の動きを続けている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F9_v2.mp4`(未生成)
- 判定: 未検証
- メモ: ぽよんが完全静止だと不自然、というご指摘への対応版。笑顔は変えないまま
  浮遊キャラクターらしい自然な上下の微動を追加した

### v1 (2026-09-15) — 旧版(ぽよんが完全に静止していた)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 2.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing with a modest, happy smile and the transparent, jelly-like rubber character hovering near the purple cloud with its own happy smile, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything through body language and expression alone. The egg character never has eyebrows at any point. Over the course of this short shot, the egg character's smile steadily grows bigger and more joyful, its mouth opening wider and wider, its round dot eyes crinkling further into happy creases, as pure delight builds up in it — and in step with this growing joy, its short arms lift and swing a little, bouncing gently and cheerfully with the building happiness, its short stiff legs staying always up on the very tips of their toes, its heels never touching the ground. The transparent character, meanwhile, keeps its expression and pose completely unchanged throughout — the same steady, happy smile it had at the very start, with no shift or transition of any kind — its mouth remaining a thin, dark, uncolored outline the entire time, staying just as transparent as the rest of its glossy body, with its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — clearly visible throughout, settling naturally at the bottom of its body under gravity. By the end of this short shot, the egg character's smile and arm position have grown into the bigger, more joyful laugh and slightly raised, bouncing arm position shown in <Picture 2>, matching it exactly.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の2.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターは控えめな嬉しそうな笑顔で立ち、透明でゼリーのようなラバーキャラクターは紫の雲のそばで自分自身の嬉しそうな笑顔のまま浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動き・表情だけで表現する。卵形のキャラクターにはどの瞬間も眉毛はつかない。この短いショットが進む間、卵形のキャラクターの笑顔は着実にどんどん大きく、より喜びに満ちたものになっていき、口はどんどん大きく開き、丸い点目はさらに笑いじわに細まっていく——純粋な喜びが体の中にこみ上げてくるかのように。そしてこの高まる喜びに合わせて、短い両腕が持ち上がって少し揺れ、高まる嬉しさとともにやさしく楽しそうに弾む——短く硬い脚は常につま先の先端だけで立ったままで、踵はどの瞬間も地面につかない。一方、透明なキャラクターは、この間ずっと表情もポーズもまったく変化しない——最初と同じ、変わらぬ嬉しそうな笑顔のままで、切り替わりや移行は一切なく——その口は終始薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——ははっきりと見え続け、常に重力に従って体の底に自然に沈んでいる。この短いショットの終わりには、卵形のキャラクターの笑顔と腕の位置は、<Picture 2>で示された、より大きく喜びに満ちた笑い声と、少し上がって弾んだ腕の位置へと成長しており、それとぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F9_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(たまちゃん控えめな笑顔・ぽよん笑顔)
- Picture 2: いただいた画像2(たまちゃんより大きな笑顔・腕が少し上がった位置)
- モード: FL2VA
- 尺: 2.5秒目安(ご要望の2〜3秒に収まるよう設定)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: ぽよんの表情・ポーズは一切変化させず、たまちゃんの笑顔の変化だけで繋ぐ
