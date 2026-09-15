---
project: H3-Video-Series-v2
cut: E-2c
mode: FL2VA
status: draft
---

# カットE-2c: 大笑いしている2人をつなぐ短い橋渡しカット(俯瞰固定)

## シーン内容
E-2b(着地して立ったまま大笑い)の続きに使う想定の、ほぼ同じ構図・表情の
2枚の画像を自然につなぐ短いブリッジカット。俯瞰固定カメラ、2人ともすでに
大笑いしている状態から始まり、その笑いを保ったまま2〜3秒でPicture2の
状態へ自然につながるようにする。

**設計メモ**: いただいた2枚の画像はポーズ・表情がほぼ同一のため、F-9・F-10
で確立した「ほぼ同じ2枚の画像をつなぐ場合、完全に静止させると不自然になる
ため、表情・ポーズは維持しつつ軽いアイドルモーション(体の揺れ・弾み)を
加える」という手法を適用した。ここでは「笑いに合わせて体が小さく震える・
弾む」という、大笑いの動作そのものに合った自然な揺れを採用している。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの短く硬い腕は常に同じ短い固定長のまま、伸びたり長くなったりしない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(0.00秒・最初のフレーム): いただいた画像1。俯瞰、左にぽよん・
  右にたまちゃんが並んで立ち、2人とも目を閉じて楽しそうに大笑いしている
- Picture 2(最後のフレーム): いただいた画像2。ほぼ同じ構図・表情(左に
  ぽよん・右にたまちゃん、2人とも目を閉じて大笑い)

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 2.50-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor exactly as shown in <Picture 1>, with the transparent, jelly-like rubber character on the left and the egg-shaped character on the right, both already standing and laughing hard, their eyes closed with joy and their mouths open in delighted laughter, matching their exact appearance and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through their laughing faces and body language. Both characters continue laughing with complete, joyful abandon the whole time, their eyes staying gently closed, their mouths staying open in the same happy laugh, while their whole bodies keep shaking and bouncing very slightly and rhythmically with each little wave of laughter — a small, natural, repeated jiggle rather than a big or dramatic movement, exactly the kind of gentle full-body shake a body makes when caught in a fit of giggles. Neither character's pose, position, or facial expression changes in any major way; only this small, continuous laughing-shake motion animates them throughout. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing — jostle gently inside with each small shake of laughter, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. The egg-shaped character's short, stiff arms and legs keep their same fixed short length throughout, never stretching or bending at any joint that would break its design. Both characters continue this same gentle, joyful, laughing shake the whole way through, settling into the exact same pose, position, and delighted, eyes-closed laughing expression shown in <Picture 2> at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の2.50秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしており、左に透明でゼリーのようなラバーキャラクター、右に卵形のキャラクターが、すでに立って激しく笑っており、目を閉じて嬉しそうに、口を開けた喜びの笑いを浮かべている、<Picture 1>のとおりの見た目・位置のままの状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままで、すべてを笑っている顔と体の動きだけで表現する。2人ともその間ずっと、心から嬉しそうに笑い続け、目は穏やかに閉じたまま、口は同じ嬉しそうな笑いの形で開いたまま、体全体が笑いの波に合わせてごく小さく、リズミカルに震え、弾み続ける——大きく劇的な動きではなく、ちょうど笑いの発作に襲われたときの体のような、小さく自然な、繰り返しの震えである。どちらのキャラクターのポーズ・位置・表情も大きく変化することはなく、この小さく継続する「笑いの震え」の動きだけが2人に生命感を与えている。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボール——は、笑いの小さな震えのたびに中で穏やかに揺れ動くが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。卵形のキャラクターの短く硬い腕と脚は、この間ずっと同じ短い固定された長さを保ち、デザインを崩すような関節での伸びや曲がりは一切ない。2人はこのまま同じ、穏やかで嬉しそうな笑いの震えを続けながら、<Picture 2>に示されたのと同じポーズ・位置・目を閉じた嬉しそうな笑いの表情に収まってこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E2c_v1.mp4`(未生成)
- 判定: 未検証
- メモ: ほぼ同一の2枚の画像をつなぐ短いブリッジカット。F-9・F-10の
  アイドルモーション手法を踏襲し、「笑いに合わせた小さな全身の震え」を
  動きの核として採用した

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(ぽよん左・たまちゃん右、2人とも大笑い)
- Picture 2: いただいた画像2(ほぼ同じ構図・表情)
- モード: FL2VA
- 尺: 2.5秒目安(ご指示どおり2〜3秒の短い橋渡しカット)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
