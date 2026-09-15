---
project: H3-Video-Series-v2
cut: F-7
mode: FL2VA
status: draft
---

# カットF-7: たまちゃんが体ごとぽよんに寄りかかり、ずり落ちるように擦りつく→2人とも笑い続けたまま低い体勢で終わる

## シーン内容
F-6の続き。今回は追いかけっこではなく、2人が寄り添う穏やかな締めのカット。

**参考動画あり**(ユーザー提供、理想の動きとして確認済み): たまちゃんが体全体を横に
大きく傾けてぽよんの丸い体にもたれかかり、そのままぐりぐりと擦りつきながら体勢が
だんだん低く崩れていき、最終的にぽよんの根元近くで足を投げ出したような低い姿勢で
落ち着く。**カメラは一切動かず完全固定**(参考動画でも終始固定)。**表情は最初から
最後まで2人とも変わらず笑ったまま**で、途中で照れる・驚くといった表情変化は入らない
(参考動画でもぽよんは終始大きく口を開けて笑ったまま)。

1. Picture1の状態(たまちゃんが左寄りの雲、ぽよんが右寄り・少し高い位置の雲の
   そばで浮かぶように笑っている)から始まる
2. たまちゃんがぽよんの方へつま先立ちのまま歩み寄っていく(カメラは固定のまま動かない)
3. ぽよんはたまちゃんが近づく間に雲の上へふわりと降り、たまちゃんが寄りかかれる
   高さに落ち着く
4. たまちゃんがぽよんの丸い体に体全体を横向きに傾けてもたれかかり、ぐりぐりと
   何度も擦りつく。体勢はもたれかかるにつれてだんだん低く崩れていく
5. 2人とも最初から最後まで大きく口を開けて笑ったままの表情を保つ
6. 最終的にたまちゃんはぽよんの根元近くで、足を投げ出したような低く傾いた姿勢で
   落ち着き、2人とも笑い合ったまま終わる

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。笑顔のままでも口の中に
  色は一切つかない
- カメラは完全固定・ズームなし(参考動画に準拠)
- 表情切り替えなし。2人とも最初から最後まで笑顔のまま

## 参照画像
- Picture 1(最初のフレーム): いただいた画像。画面左寄りの雲にたまちゃんが立ち
  大笑いしており、画面右寄り・少し高い位置でぽよんが浮かぶように笑っている構図
- Picture 2(最後のフレーム): いただいた新しい画像。たまちゃんの顔が画面左、
  ぽよんの顔が画面右のタイトなクローズアップ。たまちゃんの手がぽよんの体に
  添えられており、2人とも大きく口を開けて笑っている(このカットのラストの
  ズームアップ先の構図として使用)

## プロンプト履歴

### v5 (2026-09-15) — 現在の採用版(ラストのズームアップ先をPicture2として明示・FL2VA化)

ラストにズームアップした先の具体的な構図(たまちゃんの手がぽよんに添えられ、
2人の顔が並んで大きく口を開けて笑っているクローズアップ)を実際の画像でいただいたため、
FL2VAに変更しPicture2として参照させる。動き自体(体を傾けて擦りつく/表情変化なし)はv4のまま。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 7.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot shows the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily with their mouths wide open, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera stays completely fixed and unmoving, with no panning, tilting, zooming, or cutting of any kind, for almost the entire shot — it only moves once, right at the very end, as described below. The egg character never has eyebrows at any point, and both characters keep this same wide-open, big, happy laughing expression completely unchanged from the very first frame all the way to the very last frame of the shot — there is no expression transition, no shift to surprise or shyness, and no moment where either character's mouth closes or changes shape at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. Still laughing with its mouth wide open the whole time, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As the egg character approaches, the transparent character gently bounces down and settles onto the surface of its own cloud, coming to rest at a height the egg character can lean against. Once right beside it, the egg character tips its whole body sideways, leaning its entire body weight against the transparent character's round, glossy side, and begins rubbing against it vigorously and repeatedly, again and again, in a big, energetic, affectionate grinding motion, still laughing with its mouth wide open the entire time. With each vigorous rub, the egg character's body sinks and tilts a little lower and further sideways, its posture gradually collapsing downward against the transparent character's rounded body, its legs splaying out at an increasingly low, tilted angle, while its mouth stays wide open in the exact same unbroken laugh throughout. One of the egg character's small arms comes to rest gently against the transparent character's rounded side as it settles into this low, leaning pose. The transparent character's whole soft body visibly jostles and wobbles with each rub, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — jiggling energetically along with it, always settling naturally at the bottom of its body under gravity even as they jiggle, never floating motionless in mid-air or appearing stuck together. The transparent character keeps laughing with its mouth wide open the entire time as well, its mouth remaining exactly the same thin, dark, uncolored outline it always is, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind ever added anywhere on it, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline throughout. Only in these final moments of the shot does the camera finally move at all: it gently and smoothly pushes in toward both characters' faces, the only camera movement in the entire shot, ending the shot on a close, tight two-shot exactly matching <Picture 2> — the egg character's face at left and the transparent character's face at right, filling most of the frame, the egg character's arm resting against the transparent character's side, both still laughing with their mouths wide open in the exact same unbroken happy expression from the very start of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の7.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通りパステルカラーの雲を映す単一の連続したショットで、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも口を大きく開けて嬉しそうに笑っている、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラはショットのほぼ全体を通して完全に固定され動かない——パン・チルト・ズーム・カットのいずれも一切行わない——動くのは、後述する通りラストの一度きりである。卵形のキャラクターにはどの瞬間も眉毛はつかず、2人ともこの同じ、口を大きく開けた嬉しそうな笑い表情を、ショットの最初のフレームから最後のフレームまでまったく変えない——表情の切り替えは一切なく、驚きや照れへの変化もなく、どちらのキャラクターの口も閉じたり形を変えたりする瞬間は一切ない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。口を大きく開けて笑ったまま、卵形のキャラクターは透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。卵形のキャラクターが近づくにつれて、透明なキャラクターはやさしく弾んで自分の雲の表面に降り立ち、卵形のキャラクターがもたれかかれる高さに落ち着く。すぐそばまで来たところで、卵形のキャラクターは体全体を横に傾け、透明なキャラクターの丸く光沢のある側面に体重を預けるようにもたれかかり、何度も何度も、大きく元気よく擦りつき始める——この間ずっと口を大きく開けて笑ったままである。擦りつくたびに、卵形のキャラクターの体は少しずつ低く、さらに横に傾いて沈んでいき、その姿勢は透明なキャラクターの丸い体に押し当てられながらだんだんと崩れ落ちていき、脚はますます低く傾いた角度で投げ出されていくが、口は終始まったく同じ途切れない笑いの形のまま開いている。この低く傾いた姿勢に落ち着くにつれて、卵形のキャラクターの小さな腕の片方が、透明なキャラクターの丸い側面にそっと添えられる。透明なキャラクターの柔らかい体全体は、擦りつかれるたびに目に見えて揺さぶられ波打ち、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——も一緒に元気よく揺れ動くが、揺れながらも常に重力に従って体の底に自然に沈んだままで、宙に浮いたまま静止したりくっついて見えたりすることは一切ない。透明なキャラクターもこの間ずっと口を大きく開けて笑い続け、その口は常にまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。このショットの最後の瞬間になって初めて、カメラがようやく動く——2人の顔へ向かってゆっくりと滑らかに寄っていく、このショット全体で唯一のカメラの動きであり、最終的に<Picture 2>とぴったり一致するタイトなツーショットで終わる——卵形のキャラクターの顔が画面左、透明なキャラクターの顔が画面右、画面の大部分を占め、卵形のキャラクターの腕は透明なキャラクターの側面に添えられたまま、2人ともショットの最初とまったく同じ、途切れることのない口を大きく開けた嬉しそうな笑い表情のまま笑い続けている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v5.mp4`(未生成)
- 判定: 未検証
- メモ: ラストのズームアップ先の具体的な構図をPicture2として実画像で指定した
  FL2VA版。たまちゃんの腕がぽよんに添えられる描写も追加

### v4 (2026-09-15) — 旧版(I2VA、ズームアップ先の具体像なし)

v3の動き(体ごと寄りかかり擦りつく/表情変化なし)はそのまま、**ラストの一瞬だけ
カメラが2人の顔にゆっくり寄っていく**演出を追加。それまでは完全固定。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot shows the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily with their mouths wide open, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera stays completely fixed and unmoving, with no panning, tilting, zooming, or cutting of any kind, for almost the entire shot — it only moves once, right at the very end, as described below. The egg character never has eyebrows at any point, and both characters keep this same wide-open, big, happy laughing expression completely unchanged from the very first frame all the way to the very last frame of the shot — there is no expression transition, no shift to surprise or shyness, and no moment where either character's mouth closes or changes shape at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. Still laughing with its mouth wide open the whole time, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As the egg character approaches, the transparent character gently bounces down and settles onto the surface of its own cloud, coming to rest at a height the egg character can lean against. Once right beside it, the egg character tips its whole body sideways, leaning its entire body weight against the transparent character's round, glossy side, and begins rubbing against it vigorously and repeatedly, again and again, in a big, energetic, affectionate grinding motion, still laughing with its mouth wide open the entire time. With each vigorous rub, the egg character's body sinks and tilts a little lower and further sideways, its posture gradually collapsing downward against the transparent character's rounded body, its legs splaying out at an increasingly low, tilted angle, while its mouth stays wide open in the exact same unbroken laugh throughout. The transparent character's whole soft body visibly jostles and wobbles with each rub, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — jiggling energetically along with it, always settling naturally at the bottom of its body under gravity even as they jiggle, never floating motionless in mid-air or appearing stuck together. The transparent character keeps laughing with its mouth wide open the entire time as well, its mouth remaining exactly the same thin, dark, uncolored outline it always is, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind ever added anywhere on it, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline throughout. The egg character settles into a low, sideways-leaning, sprawled pose near the base of the transparent character, its legs splayed out at an angle, its body still pressed affectionately against the transparent character's side, both still laughing with their mouths wide open in the exact same happy expression as at the very start. Only in these final moments of the shot does the camera finally move at all: it gently and smoothly pushes in toward both characters' faces, the only camera movement in the entire shot, ending the shot on a close, tight two-shot of both characters' faces side by side, filling most of the frame, both still laughing with their mouths wide open in the exact same unbroken happy expression from the very start of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通りパステルカラーの雲を映す単一の連続したショットで、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも口を大きく開けて嬉しそうに笑っている、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラはショットのほぼ全体を通して完全に固定され動かない——パン・チルト・ズーム・カットのいずれも一切行わない——動くのは、後述する通りラストの一度きりである。卵形のキャラクターにはどの瞬間も眉毛はつかず、2人ともこの同じ、口を大きく開けた嬉しそうな笑い表情を、ショットの最初のフレームから最後のフレームまでまったく変えない——表情の切り替えは一切なく、驚きや照れへの変化もなく、どちらのキャラクターの口も閉じたり形を変えたりする瞬間は一切ない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。口を大きく開けて笑ったまま、卵形のキャラクターは透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。卵形のキャラクターが近づくにつれて、透明なキャラクターはやさしく弾んで自分の雲の表面に降り立ち、卵形のキャラクターがもたれかかれる高さに落ち着く。すぐそばまで来たところで、卵形のキャラクターは体全体を横に傾け、透明なキャラクターの丸く光沢のある側面に体重を預けるようにもたれかかり、何度も何度も、大きく元気よく擦りつき始める——この間ずっと口を大きく開けて笑ったままである。擦りつくたびに、卵形のキャラクターの体は少しずつ低く、さらに横に傾いて沈んでいき、その姿勢は透明なキャラクターの丸い体に押し当てられながらだんだんと崩れ落ちていき、脚はますます低く傾いた角度で投げ出されていくが、口は終始まったく同じ途切れない笑いの形のまま開いている。透明なキャラクターの柔らかい体全体は、擦りつかれるたびに目に見えて揺さぶられ波打ち、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——も一緒に元気よく揺れ動くが、揺れながらも常に重力に従って体の底に自然に沈んだままで、宙に浮いたまま静止したりくっついて見えたりすることは一切ない。透明なキャラクターもこの間ずっと口を大きく開けて笑い続け、その口は常にまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。卵形のキャラクターは透明なキャラクターの根元近くで、低く横向きに傾いた、足を投げ出したような姿勢に落ち着き、その体は依然として透明なキャラクターの側面に愛おしそうに押し当てられたまま、2人ともショットの最初とまったく同じ、口を大きく開けた嬉しそうな笑い表情のまま笑い続けている。このショットの最後の瞬間になって初めて、カメラがようやく動く——2人の顔へ向かってゆっくりと滑らかに寄っていく、このショット全体で唯一のカメラの動きであり、最終的に2人の顔が並んだタイトなツーショットのクローズアップで終わる——画面の大部分を占め、2人ともショットの最初とまったく同じ、途切れることのない口を大きく開けた嬉しそうな笑い表情のまま笑い続けている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v4.mp4`(未生成)
- 判定: 未検証
- メモ: ラストの一瞬だけカメラが2人の顔にゆっくり寄っていく演出を追加。
  それ以外(体を傾けて擦りつく動き・表情は変えない)はv3のまま

### v3 (2026-09-15) — 旧版(カメラ完全固定、ズームなし)

参考動画(ユーザー提供)で確認した実際の理想の動き: カメラ完全固定/たまちゃんが体ごと
横に傾いてぽよんにもたれかかり、擦りつきながら体勢がだんだん低く崩れる/2人とも
最初から最後まで大きく口を開けて笑ったまま、表情変化なし。この動きに合わせて
「顔を寄せてのクローズアップ」「照れる反応」の要素は削除した。

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting whatsoever — the camera's position, framing, and lens stay completely locked and unchanging from the first frame to the last, with absolutely no zooming in or out, no push-in, and no drifting at any point — shows the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily with their mouths wide open, matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point, and both characters keep this same wide-open, big, happy laughing expression completely unchanged from the very first frame to the very last frame of the shot — there is no expression transition, no shift to surprise or shyness, and no moment where either character's mouth closes or changes shape at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. Still laughing with its mouth wide open the whole time, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As the egg character approaches, the transparent character gently bounces down and settles onto the surface of its own cloud, coming to rest at a height the egg character can lean against. Once right beside it, the egg character tips its whole body sideways, leaning its entire body weight against the transparent character's round, glossy side, and begins rubbing against it vigorously and repeatedly, again and again, in a big, energetic, affectionate grinding motion, still laughing with its mouth wide open the entire time. With each vigorous rub, the egg character's body sinks and tilts a little lower and further sideways, its posture gradually collapsing downward against the transparent character's rounded body, its legs splaying out at an increasingly low, tilted angle, while its mouth stays wide open in the exact same unbroken laugh throughout. The transparent character's whole soft body visibly jostles and wobbles with each rub, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — jiggling energetically along with it, always settling naturally at the bottom of its body under gravity even as they jiggle, never floating motionless in mid-air or appearing stuck together. The transparent character keeps laughing with its mouth wide open the entire time as well, its mouth remaining exactly the same thin, dark, uncolored outline it always is, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind ever added anywhere on it, so its interior gumballs and confetti remain clearly visible straight through the open mouth outline throughout. By the end of the shot, the egg character has settled into a low, sideways-leaning, sprawled pose near the base of the transparent character, its legs splayed out at an angle, its body still pressed affectionately against the transparent character's side — both characters still laughing with their mouths wide open in the exact same happy expression as at the very start of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定ショットで——カメラの位置・画角・レンズは最初のフレームから最後のフレームまで完全に固定されたまま変化せず、ズームイン・ズームアウト・寄り・ドリフトのいずれも一切発生しない——<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも口を大きく開けて嬉しそうに笑っている、<Picture 1>の見た目・表情・位置のままの状態から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかず、2人ともこの同じ、口を大きく開けた嬉しそうな笑い表情を、ショットの最初のフレームから最後のフレームまでまったく変えない——表情の切り替えは一切なく、驚きや照れへの変化もなく、どちらのキャラクターの口も閉じたり形を変えたりする瞬間は一切ない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。口を大きく開けて笑ったまま、卵形のキャラクターは透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。卵形のキャラクターが近づくにつれて、透明なキャラクターはやさしく弾んで自分の雲の表面に降り立ち、卵形のキャラクターがもたれかかれる高さに落ち着く。すぐそばまで来たところで、卵形のキャラクターは体全体を横に傾け、透明なキャラクターの丸く光沢のある側面に体重を預けるようにもたれかかり、何度も何度も、大きく元気よく擦りつき始める——この間ずっと口を大きく開けて笑ったままである。擦りつくたびに、卵形のキャラクターの体は少しずつ低く、さらに横に傾いて沈んでいき、その姿勢は透明なキャラクターの丸い体に押し当てられながらだんだんと崩れ落ちていき、脚はますます低く傾いた角度で投げ出されていくが、口は終始まったく同じ途切れない笑いの形のまま開いている。透明なキャラクターの柔らかい体全体は、擦りつかれるたびに目に見えて揺さぶられ波打ち、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——も一緒に元気よく揺れ動くが、揺れながらも常に重力に従って体の底に自然に沈んだままで、宙に浮いたまま静止したりくっついて見えたりすることは一切ない。透明なキャラクターもこの間ずっと口を大きく開けて笑い続け、その口は常にまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されず、開いた口の輪郭線を通して中のガムボールと紙吹雪がそのままはっきりと見え続ける。ショットの終わりには、卵形のキャラクターは透明なキャラクターの根元近くで、低く横向きに傾いた、足を投げ出したような姿勢に落ち着いており、その体は依然として透明なキャラクターの側面に愛おしそうに押し当てられたまま——2人ともショットの最初とまったく同じ、口を大きく開けた嬉しそうな笑い表情のまま笑い続けている。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v3.mp4`(未生成)
- 判定: 未検証
- メモ: ユーザー提供の参考動画の動き(体ごと寄りかかって擦りつき低く崩れる/
  カメラ完全固定/2人とも終始笑顔のまま)に合わせて全面的に書き換えたバージョン

### v2 (2026-09-15) — 旧版(顔のクローズアップ+照れ反応、参考動画とは異なる動き)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous shot begins at the exact same wide framing and lens as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily, matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. After a brief happy moment, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As it approaches, the camera slowly and smoothly begins pushing in toward both characters, gradually tightening the framing over the course of the shot. Once close beside the transparent character, the egg character presses its face firmly against the transparent character's rounded body and rubs it vigorously and enthusiastically back and forth, again and again, in a big, energetic, affectionate grinding motion — much more forceful and playful than a gentle nuzzle, really digging its face in and rubbing hard with obvious excited affection. Each vigorous rub visibly jostles and wobbles the transparent character's whole soft body, its interior gumballs jiggling energetically along with it. The transparent character is briefly startled by this sudden, enthusiastic rubbing, then quickly relaxes into a bashful, pleased reaction despite the vigorous affection — its round eyes softening and narrowing slightly rather than staying wide open, its small mouth staying modest and closed rather than opening wide, its whole body wobbling and jiggling from the energetic rubbing while also drawing in slightly with a small, shy, happy shiver, gladly accepting the enthusiastic affectionate gesture even as it visibly wobbles from the force of it. The transparent character's mouth remains exactly the same thin, dark, uncolored outline it always is throughout this entire reaction, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind added anywhere on it — its interior gumballs, exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti, always settling naturally at the bottom of its body under gravity even as they jiggle from the vigorous rubbing, remain clearly visible the whole time. By the end of the shot, the camera has pushed all the way into a tight close-up of both characters' faces side by side, filling most of the frame, with the egg character's face still pressed affectionately and energetically against the transparent character, both wearing warm, happy, slightly bashful expressions, its round dot eyes crinkled happily, still with no eyebrows.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>とまったく同じ広い画角・レンズで始まる単一の連続したショットで、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも<Picture 1>の見た目・表情・位置のまま嬉しそうに笑っている状態から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。少し嬉しそうな時間を過ごした後、卵形のキャラクターが透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。近づくにつれて、カメラはゆっくりと滑らかに2人へ向かって寄っていき始め、ショットが進むにつれて徐々に画角が狭まっていく。透明なキャラクターのすぐそばまで来たところで、卵形のキャラクターは顔を透明なキャラクターの丸い体にぐっと押し付け、**何度も何度も、大きく元気よく、力強くすりすりと擦り寄せる**——優しいなでなでというよりずっと力強く遊び心のある動きで、興奮した愛情を隠さずに顔をぐりぐりと押し付けて擦る。この力強い擦り寄せの一回ごとに、透明なキャラクターの柔らかい体全体が目に見えて揺さぶられ、ぷるぷると波打ち、中のガムボールも一緒に元気よく揺れる。透明なキャラクターはこの突然の熱烈な擦り寄せに一瞬驚くが、この力強い愛情表現にもかかわらず、すぐに照れくさそうな、嬉しそうな反応へと落ち着く——丸い目は大きく見開いたままではなく、少し柔らかく細まり、小さな口は大きく開くのではなく控えめに閉じたままで、力強い擦り寄せでぷるぷると揺れ波打ちながらも、体全体がわずかに縮こまるような、恥ずかしそうで嬉しそうな小さな震えを見せ、その勢いに揺さぶられながらも嬉しそうにこの熱烈な愛情表現を受け入れる。透明なキャラクターの口は、この反応の間ずっと、いつもとまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されない——中のガムボール(正確に黄色4個・赤2個・水色1個・黄緑3個、合計10個、この数と色の組み合わせは変わらない、プラスカラフルな紙吹雪)は、力強い擦り寄せで揺れながらも常に重力に従って体の底に自然に沈んだまま、はっきりと見え続ける。ショットの終わりには、カメラは完全に寄りきり、2人の顔が並んだタイトなクローズアップとなり、画面の大部分を占める——卵形のキャラクターの顔は依然として透明なキャラクターに力強く愛おしそうに押し付けられたままで、2人とも温かく嬉しそうな、少し照れたような表情を浮かべており、丸い点目は嬉しそうに笑いじわになり、眉毛はやはりつかない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 「すりすりが優しすぎる」フィードバックへの対応版。頬擦りを「何度も・大きく・
  力強く」な「ぐりぐり」の動きに強化し、ぽよんの体が揺さぶられる反応も追加

### v1 (2026-09-15) — 旧版(すりすりが優しすぎた)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous shot begins at the exact same wide framing and lens as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily, matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. After a brief happy moment, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As it approaches, the camera slowly and smoothly begins pushing in toward both characters, gradually tightening the framing over the course of the shot. Once close beside the transparent character, the egg character leans its face in and gently nuzzles it, rubbing its cheek softly and affectionately against the transparent character's rounded body, in a warm, cuddly gesture. The transparent character is briefly startled by the sudden closeness, then quickly relaxes into a bashful, pleased reaction — its round eyes softening and narrowing slightly rather than staying wide open, its small mouth staying modest and closed rather than opening wide, its whole body drawing in slightly with a small, shy, happy wobble, gladly accepting the affectionate gesture. The transparent character's mouth remains exactly the same thin, dark, uncolored outline it always is throughout this entire reaction, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind added anywhere on it — its interior gumballs, exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti, always settling naturally at the bottom of its body under gravity, remain clearly visible the whole time. By the end of the shot, the camera has pushed all the way into a tight close-up of both characters' faces side by side, filling most of the frame, with the egg character's face still affectionately nuzzled close to the transparent character, both wearing warm, happy, slightly bashful expressions, its round dot eyes crinkled happily, still with no eyebrows.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>とまったく同じ広い画角・レンズで始まる単一の連続したショットで、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも<Picture 1>の見た目・表情・位置のまま嬉しそうに笑っている状態から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。少し嬉しそうな時間を過ごした後、卵形のキャラクターが透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。近づくにつれて、カメラはゆっくりと滑らかに2人へ向かって寄っていき始め、ショットが進むにつれて徐々に画角が狭まっていく。透明なキャラクターのすぐそばまで来たところで、卵形のキャラクターは顔を近づけ、透明なキャラクターの丸い体にやさしく、愛おしそうに頬を擦り寄せる、温かく甘えるような仕草をする。透明なキャラクターは突然の近さに一瞬驚くが、すぐに照れくさそうな、嬉しそうな反応へと落ち着く——丸い目は大きく見開いたままではなく、少し柔らかく細まり、小さな口は大きく開くのではなく控えめに閉じたままで、体全体がわずかに縮こまるような、恥ずかしそうで嬉しそうな小さな震えを見せながら、この愛情表現を喜んで受け入れる。透明なキャラクターの口は、この反応の間ずっと、いつもとまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されない——中のガムボール(正確に黄色4個・赤2個・水色1個・黄緑3個、合計10個、この数と色の組み合わせは変わらない、プラスカラフルな紙吹雪)は常に重力に従って体の底に自然に沈んだまま、はっきりと見え続ける。ショットの終わりには、カメラは完全に寄りきり、2人の顔が並んだタイトなクローズアップとなり、画面の大部分を占める——卵形のキャラクターの顔は依然として透明なキャラクターに愛おしそうに擦り寄せられたままで、2人とも温かく嬉しそうな、少し照れたような表情を浮かべており、丸い点目は嬉しそうに笑いじわになり、眉毛はやはりつかない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像(たまちゃん左・ぽよん右、2人とも笑っている構図)
- Picture 2: いただいた新しい画像(ラストのズームアップ先。たまちゃん左・ぽよん右の
  顔のクローズアップ、たまちゃんの腕がぽよんに添えられている)
- モード: FL2VA
- 尺: 7秒目安(歩み寄る2s/もたれかかり擦りつき+体勢が崩れていく3s/ラストの
  ズームアップ2s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 体を傾けて擦りつく〜低い姿勢に落ち着くまではカメラ完全固定、
  **ラストの一瞬だけ**Picture2の構図にゆっくりズームアップして終わる
- **重要**: 表情切り替えなし。2人とも最初から最後まで大きく口を開けて笑ったまま
  (ズームアップ後も同じ笑顔のまま)
- 参考動画: `4528990b-MiniMax_H3_00205_.mp4`(ユーザー提供、体を横に傾けて
  もたれかかり擦りつく動きの参考として使用)
