---
project: H3-Video-Series-v2
cut: F-10
mode: FL2VA
status: draft
---

# カットF-10: ほぼ同じ構図の2枚を自然に繋ぐ短いカット(画像1→画像2)

## シーン内容
ほぼ同じ構図の2枚の画像を自然に繋ぐ短いカット。**ぽよんはたまちゃんの左側から
右側へ実際に移動する**(画像1ではたまちゃんの左、画像2ではたまちゃんの右)。
正面固定カメラ。

1. Picture1の状態(たまちゃんが嬉しそうに笑い片腕を広げている、ぽよんはたまちゃんの
   左側で笑顔のまま浮かんでいる)から始まる
2. たまちゃんは同じ嬉しい笑顔を保ったまま、楽しそうに体を左右に小さく揺らし、
   もう片方の腕も広げていく
3. ぽよんは表情・笑顔は変えないまま、**ジャンプ(跳ねるような不連続な弾み)で
   2〜3回、たまちゃんの左側から右側へ移動する**。「ふわふわ漂う」ような連続的な
   移動ではなく、はっきりとした跳躍の繰り返しにすることで、中のガムボールの色が
   不自然に変わってしまう不具合を避ける。**ジャンプ中も含め、ガムボールは
   一度も体の外に飛び出さない**
4. 最終的にPicture2で示された通り、たまちゃんが両腕を広げて弾んでおり、ぽよんが
   たまちゃんの右側に移動した状態で終わる

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし(D-1での教訓)
- 表情は最初から最後まで同じ笑顔のまま変化しない(切り替えは行わない)

## 参照画像
- Picture 1(最初のフレーム): いただいた画像1。たまちゃんが嬉しそうに笑い、片腕を
  横に広げている。ぽよんは**たまちゃんの左側**で笑顔のまま浮かんでいる
- Picture 2(最後のフレーム): いただいた画像2。たまちゃんが同じ笑顔のまま両腕を
  横に広げて楽しそうに弾んでおり、ぽよんは**たまちゃんの右側**に移動している

## プロンプト履歴

### v4 (2026-09-15) — 現在の採用版(連続的な浮遊移動をやめ、ジャンプでの移動に変更)

生成結果で、ぽよんの中のガムボールの色が不思議に変わってしまう不具合が発生。
「ふわふわと連続的に漂う」という曖昧な動きの記述が原因と考え、**はっきりとした
2〜3回のジャンプ(跳躍)による移動**に変更。各ジャンプの瞬間にもガムボールの
正確な数・色の組み合わせを明記し、体の外に一切飛び出さないことも強調した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 3.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing with one arm held out to the side, laughing happily, and the transparent, jelly-like rubber character hovering to the egg character's left, wearing its own happy smile, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything through body language and expression alone. The egg character never has eyebrows at any point, and its happy, laughing expression never changes or switches to any other expression throughout the entire shot — it keeps the exact same laugh from the first frame to the last. Over the course of this short shot, the egg character sways gently and playfully from side to side, still balanced purely on the tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle at any point, and as it sways it happily brings its other short arm up and out as well, so that both arms end up held out to its sides, its whole body giving a small, joyful little bounce with the motion. At the same time, the transparent character keeps its same happy smile completely unchanged throughout, and moves from the egg character's left side over to the egg character's right side using two or three clear, distinct hopping bounces — not a smooth, continuous drift or float, but a series of separate, well-defined little jumps, each one a clean arc through the air followed by a soft landing, moving a bit further to the right with each individual bounce. At every single point during this movement — mid-air during each jump, and while landing — its interior gumballs remain exactly the same fixed set: precisely 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing at any point, never shifting to any other colors, plus colorful confetti; even during the jumps, the gumballs stay fully contained inside its glossy transparent body at all times, never flying out, never passing through its skin, and never leaving its body for even an instant, always settling naturally at the bottom under gravity between jumps, clearly visible the entire time through its glossy transparent skin, gently jostling and rolling against each other and the inner wall with each bounce and landing. Its mouth remains a thin, dark, uncolored outline the entire time, staying just as transparent as the rest of its glossy body. By the end of this short shot, the egg character has both arms held out to its sides and is bouncing happily in place, matching the exact pose shown in <Picture 2>, its laughing expression unchanged throughout, while the transparent character has completed its hopping journey over to the egg character's right side, its same happy smile unchanged, its interior gumballs still exactly the same 4 yellow, 2 red, 1 light blue, and 3 yellow-green, matching the position shown in <Picture 2> exactly.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の3.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターは片腕を横に広げて嬉しそうに笑って立ち、透明でゼリーのようなラバーキャラクターは卵形のキャラクターの左側で自分自身の嬉しそうな笑顔のまま浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動き・表情だけで表現する。卵形のキャラクターにはどの瞬間も眉毛はつかず、その嬉しそうな笑い表情はショット全体を通して一切変化せず、他の表情に切り替わることもない——最初から最後までまったく同じ笑顔のままである。この短いショットが進む間、卵形のキャラクターは、常につま先の先端だけでバランスを取り、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらないまま、楽しそうにやさしく体を左右に揺らし、揺れながらもう片方の短い腕も嬉しそうに持ち上げて横に広げていき、最終的に両腕とも横に広げた状態になり、体全体がこの動きに合わせて小さく嬉しそうに弾む。同時に、透明なキャラクターは同じ嬉しそうな笑顔を終始まったく変えないまま、卵形のキャラクターの左側から右側へ、**2〜3回のはっきりとした、それぞれ区切られた跳躍で**移動する——滑らかで連続的な漂い・浮遊ではなく、一つ一つが独立した、明確な小さなジャンプの連なりであり、それぞれがきれいな弧を描いて空中を飛び、やわらかく着地し、一回ジャンプするごとに少しずつ右へ進んでいく。この移動の間、**どの瞬間をとっても**——各ジャンプの空中にいる間も、着地している間も——中のガムボールはまったく同じ固定された組み合わせのままである:正確に黄色4個・赤2個・水色1個・黄緑3個、合計10個、この数と色の組み合わせはどの瞬間も一切変わらず、他の色に変化することもなく、プラスカラフルな紙吹雪。ジャンプの最中であっても、ガムボールは常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり、体の表面を突き抜けたりすることはなく、一瞬たりとも体から離れることはなく、ジャンプとジャンプの間は常に重力に従って底に自然に沈み、光沢のある透明な体を通して終始はっきりと見え、跳躍・着地のたびにお互いや内壁とやさしくぶつかりころころと転がる。口は終始薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままである。この短いショットの終わりには、卵形のキャラクターは両腕を横に広げた状態で嬉しそうにその場で弾んでおり、<Picture 2>で示された通りのポーズとぴったり一致し、笑い表情はその間ずっと変わらない——その一方で、透明なキャラクターは卵形のキャラクターの右側への跳躍の旅を終えており、同じ嬉しそうな笑顔は変わらないまま、中のガムボールも依然としてまったく同じ黄色4個・赤2個・水色1個・黄緑3個のままで、<Picture 2>で示された位置とぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F10_v4.mp4`(未生成)
- 判定: 未検証
- メモ: ガムボールの色が不思議に変わってしまう不具合への対策版。連続的な
  「浮遊」ではなく2〜3回のはっきりとしたジャンプによる移動に変更し、各ジャンプの
  瞬間ごとにガムボールの正確な数・色・体内への完全な収まりを明記した

### v3 (2026-09-15) — 旧版(連続的な浮遊移動、ガムボールの色が変わってしまった)

「画像1・画像2でぽよんはたまちゃんの左から右へ移動しているはず」というご指摘を
受け、単なる上下の微動ではなく、**ぽよんが実際にたまちゃんの左側から右側へ
横移動する**よう修正した。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 3.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing with one arm held out to the side, laughing happily, and the transparent, jelly-like rubber character hovering to the egg character's left, wearing its own happy smile, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything through body language and expression alone. The egg character never has eyebrows at any point, and its happy, laughing expression never changes or switches to any other expression throughout the entire shot — it keeps the exact same laugh from the first frame to the last. Over the course of this short shot, the egg character sways gently and playfully from side to side, still balanced purely on the tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle at any point, and as it sways it happily brings its other short arm up and out as well, so that both arms end up held out to its sides, its whole body giving a small, joyful little bounce with the motion. At the same time, the transparent character keeps its same happy smile completely unchanged throughout, but it does not stay in place — it gently floats and bounces its way across the frame, drifting smoothly from the egg character's left side, passing gradually behind or in front of it, over to the egg character's right side, a soft, unhurried, floating journey across rather than an instant jump, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting and rolling gently inside as it drifts, always clearly visible through its glossy transparent skin, settling naturally at the bottom of its body under gravity, its mouth remaining a thin, dark, uncolored outline the entire time, staying just as transparent as the rest of its glossy body. By the end of this short shot, the egg character has both arms held out to its sides and is bouncing happily in place, matching the exact pose shown in <Picture 2>, its laughing expression unchanged throughout, while the transparent character has completed its drift over to the egg character's right side, its same happy smile unchanged, matching the position shown in <Picture 2> exactly.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の3.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターは片腕を横に広げて嬉しそうに笑って立ち、透明でゼリーのようなラバーキャラクターは卵形のキャラクターの左側で自分自身の嬉しそうな笑顔のまま浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動き・表情だけで表現する。卵形のキャラクターにはどの瞬間も眉毛はつかず、その嬉しそうな笑い表情はショット全体を通して一切変化せず、他の表情に切り替わることもない——最初から最後までまったく同じ笑顔のままである。この短いショットが進む間、卵形のキャラクターは、常につま先の先端だけでバランスを取り、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらないまま、楽しそうにやさしく体を左右に揺らし、揺れながらもう片方の短い腕も嬉しそうに持ち上げて横に広げていき、最終的に両腕とも横に広げた状態になり、体全体がこの動きに合わせて小さく嬉しそうに弾む。同時に、透明なキャラクターは同じ嬉しそうな笑顔を終始まったく変えないが、その場に留まることはない——やさしく浮遊しながら弾むように画面を横切っていき、卵形のキャラクターの左側から、その後ろまたは前を通り過ぎるようにして、徐々に卵形のキャラクターの右側へと漂っていく——瞬間移動ではなく、柔らかく急がない、浮遊しながらの横断である——中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は漂う間もやさしく揺れ転がり、光沢のある透明な体を通して常にはっきりと見え、重力に従って体の底に自然に沈み、口は終始薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままである。この短いショットの終わりには、卵形のキャラクターは両腕を横に広げた状態で嬉しそうにその場で弾んでおり、<Picture 2>で示された通りのポーズとぴったり一致し、笑い表情はその間ずっと変わらない——その一方で、透明なキャラクターは卵形のキャラクターの右側への移動を完了しており、同じ嬉しそうな笑顔は変わらないまま、<Picture 2>で示された位置とぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F10_v3.mp4`(未生成)
- 判定: 未検証
- メモ: ぽよんがたまちゃんの左→右へ実際に移動するよう修正したバージョン

### v2 (2026-09-15) — 旧版(ぽよんは上下の微動のみで位置は変えていなかった)

「ぽよんが動かないとどう自然に繋がるのか」というご指摘を受け、ぽよんを完全に
静止させるのではなく、笑顔・ポーズ自体は変えないまま**ふわふわとした浮遊の
上下動**(中のガムボールもそれに合わせてやさしく揺れる)を持たせた。

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 3.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing with one arm held out to the side, laughing happily, and the transparent, jelly-like rubber character hovering near the purple cloud with its own happy smile, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything through body language and expression alone. The egg character never has eyebrows at any point, and its happy, laughing expression never changes or switches to any other expression throughout the entire shot — it keeps the exact same laugh from the first frame to the last. Over the course of this short shot, the egg character sways gently and playfully from side to side, still balanced purely on the tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle at any point, and as it sways it happily brings its other short arm up and out as well, so that both arms end up held out to its sides, its whole body giving a small, joyful little bounce with the motion. The transparent character keeps its smiling expression, pose, and position completely unchanged throughout — the same steady, happy smile it had at the very start, with no shift, transition, or pose change of any kind — but it is not perfectly frozen either: being a soft, hovering, jelly-like character, it gently bobs and drifts up and down by a small amount the whole time, a light, natural floating motion, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — swaying and settling gently inside with this soft bobbing, always clearly visible through its glossy transparent skin, its mouth remaining a thin, dark, uncolored outline the entire time, staying just as transparent as the rest of its glossy body. By the end of this short shot, the egg character has both arms held out to its sides and is bouncing happily in place, matching the exact pose shown in <Picture 2>, its laughing expression unchanged throughout, while the transparent character continues its same gentle hovering motion beside it, its own expression and pose still matching <Picture 2> exactly.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の3.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターは片腕を横に広げて嬉しそうに笑って立ち、透明でゼリーのようなラバーキャラクターは紫の雲のそばで自分自身の嬉しそうな笑顔のまま浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動き・表情だけで表現する。卵形のキャラクターにはどの瞬間も眉毛はつかず、その嬉しそうな笑い表情はショット全体を通して一切変化せず、他の表情に切り替わることもない——最初から最後までまったく同じ笑顔のままである。この短いショットが進む間、卵形のキャラクターは、常につま先の先端だけでバランスを取り、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらないまま、楽しそうにやさしく体を左右に揺らし、揺れながらもう片方の短い腕も嬉しそうに持ち上げて横に広げていき、最終的に両腕とも横に広げた状態になり、体全体がこの動きに合わせて小さく嬉しそうに弾む。透明なキャラクターは、笑顔の表情・ポーズ・位置を終始まったく変えない——最初と同じ、変わらぬ嬉しそうな笑顔のままで、切り替わりやポーズの変化は一切ないが、かといって完全に静止しているわけでもない——柔らかく浮遊するゼリー状のキャラクターらしく、この間ずっと小さくふわふわと上下に揺れ漂う、軽く自然な浮遊の動きを見せ、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——はこのやさしい上下動に合わせて中で揺れ落ち着き、光沢のある透明な体を通して常にはっきりと見えており、口は終始薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままである。この短いショットの終わりには、卵形のキャラクターは両腕を横に広げた状態で嬉しそうにその場で弾んでおり、<Picture 2>で示された通りのポーズとぴったり一致し、笑い表情はその間ずっと変わらない——その一方で、透明なキャラクターはそのすぐそばで同じやさしい浮遊の動きを続けており、その表情・ポーズも<Picture 2>とぴったり一致したままである。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F10_v2.mp4`(未生成)
- 判定: 未検証
- メモ: ぽよんが完全静止だと不自然、というご指摘への対応版。表情・ポーズは
  変えないまま、浮遊キャラクターらしい自然な上下の微動を追加した

### v1 (2026-09-15) — 旧版(ぽよんが完全に静止していた)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 3.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel clouds exactly as shown in <Picture 1>, with the egg-shaped character standing with one arm held out to the side, laughing happily, and the transparent, jelly-like rubber character hovering near the purple cloud with its own happy smile, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything through body language and expression alone. The egg character never has eyebrows at any point, and its happy, laughing expression never changes or switches to any other expression throughout the entire shot — it keeps the exact same laugh from the first frame to the last. Over the course of this short shot, the egg character sways gently and playfully from side to side, still balanced purely on the tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle at any point, and as it sways it happily brings its other short arm up and out as well, so that both arms end up held out to its sides, its whole body giving a small, joyful little bounce with the motion. The transparent character, meanwhile, keeps its expression and pose completely unchanged throughout — the same steady, happy smile and position it had at the very start, with no shift or transition of any kind — its mouth remaining a thin, dark, uncolored outline the entire time, staying just as transparent as the rest of its glossy body, with its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — clearly visible throughout, settling naturally at the bottom of its body under gravity. By the end of this short shot, the egg character has both arms held out to its sides and is bouncing happily in place, matching the exact pose shown in <Picture 2>, its laughing expression unchanged throughout.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の3.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通りパステルカラーの雲を映しており、卵形のキャラクターは片腕を横に広げて嬉しそうに笑って立ち、透明でゼリーのようなラバーキャラクターは紫の雲のそばで自分自身の嬉しそうな笑顔のまま浮かんでいる、<Picture 1>の見た目・表情・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動き・表情だけで表現する。卵形のキャラクターにはどの瞬間も眉毛はつかず、その嬉しそうな笑い表情はショット全体を通して一切変化せず、他の表情に切り替わることもない——最初から最後までまったく同じ笑顔のままである。この短いショットが進む間、卵形のキャラクターは、常につま先の先端だけでバランスを取り、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらないまま、楽しそうにやさしく体を左右に揺らし、揺れながらもう片方の短い腕も嬉しそうに持ち上げて横に広げていき、最終的に両腕とも横に広げた状態になり、体全体がこの動きに合わせて小さく嬉しそうに弾む。一方、透明なキャラクターは、この間ずっと表情もポーズもまったく変化しない——最初と同じ、変わらぬ嬉しそうな笑顔と位置のままで、切り替わりや移行は一切なく——その口は終始薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——ははっきりと見え続け、常に重力に従って体の底に自然に沈んでいる。この短いショットの終わりには、卵形のキャラクターは両腕を横に広げた状態で嬉しそうにその場で弾んでおり、<Picture 2>で示された通りのポーズとぴったり一致し、笑い表情はその間ずっと変わらない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F10_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(たまちゃん片腕を広げて笑う)
- Picture 2: いただいた画像2(たまちゃん両腕を広げて弾む、同じ笑顔)
- モード: FL2VA
- 尺: 3秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: ぽよんの表情・ポーズは一切変化させず、たまちゃんの腕の動きだけで繋ぐ。
  表情切り替えは行わない(同じ笑顔を最初から最後まで保つ)
