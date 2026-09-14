---
project: H3-Video-Series-v2
cut: F-6
mode: I2VA
status: draft
---

# カットF-6: たまちゃんが先に逃げてぽよんが追いかける→2人とも完全にフレームアウト→思いもよらない場所からそれぞれひょこっと登場→笑い合う

## シーン内容
直前のカット(採用された最終カット)からの継続。**背景は変わらない**(いただいた
最終フレームと同じ雲の構図)。役割を入れ替え、今回はたまちゃんが先に逃げてぽよんが
追いかける。今回は片方だけでなく**2人とも完全にフレームアウト**する点がF-1/F-5と
異なる。その後、それぞれ「思いもよらない場所」からひょこっと登場し、最後は2人で
笑い合う。正面固定カメラ、背景据え置き、I2VA(開始フレーム1枚のみ参照)。

1. Picture1の状態(直前のカットの最終フレームと同じ構図・背景)から始まる
2. たまちゃんが先に、楽しそうに逃げるように走り始める
3. ぽよんがそのすぐ後ろを弾みながら追いかける
4. 2人とも同じ方向へ進み、**両方とも完全にフレームアウト**する
   (背景だけが残り、誰もいない状態に一瞬なる)
5. たまちゃんが先に一人で、予想外の場所(例:画面の思わぬ隅・雲の陰など)から
   ひょこっと顔を出す
6. 少し間があって、ぽよんも別の予想外の場所からひょこっと顔を出す
7. 2人が目を合わせて嬉しそうに笑い合う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。笑顔になっても崩れない
- 「何もないところから忽然と現れる」のではなく、雲の陰・画面端から迫り上がる/
  ひょこっと現れる自然な動きにすること(空フレーム登場の不安定さ対策)

## 参照画像
- Picture 1(最初のフレーム): **F-6実際の生成結果の1フレーム目(いただいた画像)に差し替え**。
  画面中央よりやや左寄り、紫色の雲とピンクの雲の境目にたまちゃんが立ち、両手を広げて
  大笑いしている。ぽよんは画面中央よりやや右、紫色の雲の頂上付近に宙に浮くようにして
  笑っている(ジェリー状の体で弾んだ直後のような浮遊感)

## プロンプト履歴

### v2 (2026-09-14) — 現在の採用版(実際の生成1フレーム目を参照画像に採用)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting — the camera's position, framing, and lens stay completely locked and unchanging from the first frame to the last, with absolutely no zooming in or out, no push-in, and no drifting at any point — shows the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing at the boundary between the purple and pink clouds, arms spread, laughing happily, and the transparent, jelly-like rubber character hovering near the crest of the purple cloud, also laughing happily, both matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, like a figure permanently on tiptoe, and its heels can never touch any surface at all. After a brief happy moment together, the egg character is the first to dash off playfully, toddling away to the right across the clouds, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. A beat later, the transparent character bounces down and after it in pursuit, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce, shifting without ever spilling out. Both characters move further and further to the right, following the same path, one after the other, until both of them move completely past the right edge of the frame and out of view. Once both characters have fully exited, the shot holds steady for a brief moment on the now-empty pastel clouds, exactly matching the same background and camera position as <Picture 1>, with no characters visible anywhere. The egg character is the first to reappear, popping up from a completely unexpected spot — from behind the pink cloud in the foreground, rising up over its crest as if it had been hiding there all along, nowhere near the path it originally ran along, still walking and standing purely on the tips of its toes, its heels never touching any surface. A moment later, the transparent character also pops up from its own unexpected spot — low down near the bottom edge of the frame, between the clouds, rising into view from behind a cloud's edge rather than appearing out of nowhere, its interior gumballs still clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement. Once both characters have settled into their new spots, they notice each other and turn to make eye contact, and together they break into delighted, happy laughter. The egg character's round dot eyes crinkle into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the exact same moment, the transparent character's round eyes crinkle shut into laughing crescents as well, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time. Both characters end the shot laughing happily together.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定ショットで——カメラの位置・画角・レンズは最初のフレームから最後のフレームまで完全に固定されたまま変化せず、ズームイン・ズームアウト・寄り・ドリフトのいずれも一切発生しない——<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターが紫色の雲とピンクの雲の境目に立ち、両手を広げて嬉しそうに大笑いしており、透明でゼリーのようなラバーキャラクターが紫の雲の頂上付近に浮かぶようにして、同じく嬉しそうに笑っている——2人とも<Picture 1>の見た目・表情・位置のまま始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。少し嬉しそうな時間を過ごした後、卵形のキャラクターが先に楽しそうに駆け出し、雲々を渡りながら右方向へよちよちと逃げていく——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。少し遅れて、透明なキャラクターが降りてきてそのあとを弾みながら追いかける——中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。2人とも同じ経路をたどって右へ右へと進んでいき、一人ずつ、ついに画面右端を完全に越えて見えなくなる。2人とも完全にフレームアウトした後、ショットは<Picture 1>とまったく同じ背景・カメラ位置のまま、誰もいない状態でしばらく静止する——画面のどこにもキャラクターは映っていない。卵形のキャラクターが先に再登場する——まったく予想外の場所、手前のピンクの雲の向こう側から、まるでずっとそこに隠れていたかのように、その雲の稜線を越えてひょこっと現れる。元々走っていった経路とはまったく関係のない場所である。この時も終始つま先の先端だけでバランスを取り、踵はどんな面にも一切触れない。少し間があって、透明なキャラクターも自分なりの予想外の場所——画面下端近くの、雲と雲の間の低い位置——から、何もないところから忽然と現れるのではなく雲の縁の向こうから迫り上がるようにしてひょこっと現れる。中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。2人とも新しい場所に落ち着いた後、互いの存在に気づいて目を合わせ、一緒に嬉しそうな笑い声を上げる。卵形のキャラクターの丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。まったく同じ瞬間、透明なキャラクターの丸い目もぎゅっと閉じて笑いじわの三日月形になり、口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。ショットの終わりには、2人とも一緒に嬉しそうに笑い合っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F6_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 実際に生成されたF-6動画の1フレーム目を新たなPicture1として採用し、
  プロンプトを作り直したバージョン

### v1 (2026-09-14) — 旧版(意図したPicture1を使用)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting — the camera's position, framing, and lens stay completely locked and unchanging from the first frame to the last, with absolutely no zooming in or out, no push-in, and no drifting at any point — shows the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character on the blue cloud and the transparent, jelly-like rubber character on the pink cloud, both laughing happily, matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, like a figure permanently on tiptoe, and its heels can never touch any surface at all. After a brief happy moment together, the egg character is the first to dash off playfully, toddling away to the right across the clouds, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. A beat later, the transparent character bounces after it in pursuit, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce, shifting without ever spilling out. Both characters move further and further to the right, following the same path, one after the other, until both of them move completely past the right edge of the frame and out of view. Once both characters have fully exited, the shot holds steady for a brief moment on the now-empty pastel clouds, exactly matching the same background and camera position as <Picture 1>, with no characters visible anywhere. The egg character is the first to reappear, popping up from a completely unexpected spot — from behind the tall purple cloud in the background, rising up over its crest as if it had been hiding there all along, nowhere near the path it originally ran along, still walking and standing purely on the tips of its toes, its heels never touching any surface. A moment later, the transparent character also pops up from its own unexpected spot — low down between the pink and blue clouds near the bottom of the frame, rising into view from behind the cloud's edge rather than appearing out of nowhere, its interior gumballs still clearly visible, gently shifting and rolling against each other and the bottom of its body with each small movement. Once both characters have settled into their new spots, they notice each other and turn to make eye contact, and together they break into delighted, happy laughter. The egg character's round dot eyes crinkle into laughing crescents, still with no eyebrows, its mouth opening wide with a hint of soft coral pink visible inside. At the exact same moment, the transparent character's round eyes crinkle shut into laughing crescents as well, its mouth curving into a moderately wide, gentle smile shape, no more than about a third of the width of its face, made of nothing but a thin dark outline — critically, this smiling mouth remains exactly as clear and transparent as the rest of its glossy body at every single frame of the smile, with absolutely no color, tint, shading, or fill of any kind ever appearing inside it, so its interior gumballs and confetti stay clearly visible straight through the open mouth outline the whole time. Both characters end the shot laughing happily together.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定ショットで——カメラの位置・画角・レンズは最初のフレームから最後のフレームまで完全に固定されたまま変化せず、ズームイン・ズームアウト・寄り・ドリフトのいずれも一切発生しない——<Picture 1>で示された通りパステルカラーの雲を映しており、水色の雲に卵形のキャラクター、ピンクの雲に透明でゼリーのようなラバーキャラクターがそれぞれ乗り、2人とも<Picture 1>の見た目・表情・位置のまま嬉しそうに大笑いしている状態から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。少し嬉しそうな時間を過ごした後、卵形のキャラクターが先に楽しそうに駆け出し、雲々を渡りながら右方向へよちよちと逃げていく——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。少し遅れて、透明なキャラクターがそのあとを弾みながら追いかける——中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。2人とも同じ経路をたどって右へ右へと進んでいき、一人ずつ、ついに画面右端を完全に越えて見えなくなる。2人とも完全にフレームアウトした後、ショットは<Picture 1>とまったく同じ背景・カメラ位置のまま、誰もいない状態でしばらく静止する——画面のどこにもキャラクターは映っていない。卵形のキャラクターが先に再登場する——まったく予想外の場所、背景にある背の高い紫色の雲の向こう側から、まるでずっとそこに隠れていたかのように、その雲の稜線を越えてひょこっと現れる。元々走っていった経路とはまったく関係のない場所である。この時も終始つま先の先端だけでバランスを取り、踵はどんな面にも一切触れない。少し間があって、透明なキャラクターも自分なりの予想外の場所——画面下寄り、ピンクの雲と水色の雲の間の低い位置——から、何もないところから忽然と現れるのではなく雲の縁の向こうから迫り上がるようにしてひょこっと現れる。中のガムボールははっきりと見え続け、小さな動きに合わせてやさしく揺れ動き、お互いや体の底とぶつかって転がる。2人とも新しい場所に落ち着いた後、互いの存在に気づいて目を合わせ、一緒に嬉しそうな笑い声を上げる。卵形のキャラクターの丸い点目は笑いじわの三日月形になり、眉毛はやはりつかない。口は大きく開いて中にほんのりコーラルピンク色がのぞく。まったく同じ瞬間、透明なキャラクターの丸い目もぎゅっと閉じて笑いじわの三日月形になり、口は顔の横幅の3分の1程度までしか開かない、ほどよい広さのやわらかなカーブの笑顔になり、薄い輪郭線だけでできている——極めて重要な点として、この笑顔の口は、笑顔になっているどの一瞬をとっても光沢のある体の表面とまったく同じように透き通ったままで、中には一切色・色調・陰影・塗りつぶしが決して現れず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。ショットの終わりには、2人とも一緒に嬉しそうに笑い合っている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F6_v1.mp4`
- 判定: 生成済み
- メモ: 実際に生成された動画の**1フレーム目(最初のカット)**をいただいた
  (たまちゃんが紫/ピンクの雲の境目で笑い、ぽよんが紫の雲の頂上付近に浮かんで
  笑っている構図)。指定したPicture1(たまちゃん右・水色の雲/ぽよん左・ピンクの雲)
  とはポーズ・位置が多少異なる形で生成された。次のカットで参照画像が必要になった
  場合は、この実際の生成フレームを使うこと。

## ComfyUIでの設定メモ
- Picture 1: **F-6実際の生成結果の1フレーム目**(たまちゃん:紫/ピンクの雲の境目、
  ぽよん:紫の雲の頂上付近に浮遊)
- モード: I2VA(最後のフレーム画像は不要。1枚の開始画像から自然に展開させる)
- 尺: 9秒目安(逃げる+追いかける2.5s/両方フレームアウト1s/誰もいない間1s/
  たまちゃん予想外の場所から登場1.5s/ぽよん予想外の場所から登場1.5s/目が合って笑う1.5s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: たまちゃんのつま先立ち・カメラ固定はF-5 v4の教訓を踏まえ、動きの節目ごとに繰り返し明記
