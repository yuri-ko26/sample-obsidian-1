---
project: H3-Video-Series-v2
cut: D-1-alt4
mode: I2VA
status: draft
---

# カットD-1-alt4: 楽しいリズムの跳ね方バージョン(自然な物理・各キャラクターができる範囲の動き)

## シーン内容
D-1の別バージョン。俯瞰固定カメラ、画面左から右へ移動してフレームアウト。
これまでの「回転」に挑戦するのではなく、**各キャラクターが実際にできる自然な
動き(ぽよん=弾む、たまちゃん=つま先ホップ)の範囲内で、リズムに緩急・変化を
つけて楽しさを出す**方向性。不自然な回転や違和感のある動きは一切入れない。

- ぽよんは「水切り石」のように、大きくポーンと弾む→間に小さく2回連続で弾む、
  を繰り返すリズムで進む(高低差のある弾みで楽しさを出す)
- たまちゃんはぽよんのリズムに合わせてつま先でホップしながら進み、時々小さく
  両腕を左右に振って(バンザイのように)楽しそうに揺らす仕草を加える
- どちらも回転・転倒・不自然な変形は一切なし。常につま先立ち・足首を曲げない・
  ガムボールはこぼれない、という基本制約を厳守

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」。
  弾むたびにゆれるが絶対にこぼれない

## 参照画像
- Picture 1(最初のフレーム): D-1と同じ俯瞰画像(薄い黄緑色の床、画面左寄りに
  ぽよん・たまちゃんが並び、右側に余白)

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static overhead shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, looks straight down on the pale yellow-green floor exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion, and neither character ever spins, tumbles, flips, or rotates at any point — all of their movement stays completely natural and physically plausible for their own shape, only ever using motions each of them can actually do. The transparent, jelly-like rubber character moves rightward across the floor in a playful, varied bouncing rhythm, like a stone skipping across water: one big, high bounce that carries it a good distance forward, followed by two smaller, quicker bounces close together, then another big bounce, repeating this big-small-small pattern the whole way — staying perfectly round and smooth with no flattening or distortion at any point during any bounce. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shift and jostle playfully with each bounce, settling naturally at the bottom of its body under gravity, without ever spilling out. Beside it, the egg-shaped character hops rightward in time with the transparent character's bouncing rhythm, pushing off with both of its short, stiff legs together and landing briefly on its rounded toe tips before pushing off again for the next hop, its legs never bending at the ankle and its heels never touching the ground. Every few hops, it happily flaps its two short arms outward and up, like a cheerful little wave, before tucking them back in for the next hop — a small, joyful flourish rather than any kind of spin or flip. Both characters continue advancing rightward together at this same playful, varied pace, matching each other's overall rhythm, until they fully exit past the right edge of the frame, leaving the floor empty.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定俯瞰ショットで、パン・チルト・ズーム・カットは一切なく、<Picture 1>で示された通り薄い黄緑色の床を真上から見下ろしている。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれ、どちらのキャラクターも回転・転倒・宙返り・自転を一切行わない——すべての動きは、それぞれの体の形で実際にできる自然で物理的に無理のない動きの範囲に留まる。透明でゼリーのようなラバーキャラクターは、水切り石のような楽しく緩急のある弾むリズムで右方向へ進む——大きく高く弾んで大きく前進し、続けて小さく素早い弾みを2回、そしてまた大きな弾み、という「大・小・小」のパターンを繰り返す——どの弾みでも常に完全に丸く滑らかな形を保ち、潰れたり歪んだりすることは一切ない。中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)とカラフルな紙吹雪——は弾むたびに楽しそうに揺れ動き、常に重力に従って体の底に自然に沈み、こぼれることは一切ない。その隣では、卵形のキャラクターが透明なキャラクターの弾むリズムに合わせて右方向へホップしていく——短く硬い両脚をそろえて同時に蹴り出し、丸いつま先の先端に一瞬着地してからまた次のホップへ蹴り出す——脚は足首で曲がることも、踵が地面につくこともない。数回のホップごとに、卵形のキャラクターは短い両腕を楽しそうに外側・上方へパッと振り上げる——嬉しそうな小さな手振りのようで、また次のホップのために体に引き寄せる——これは回転や宙返りの類ではなく、小さく喜びに満ちた仕草である。2人ともこの同じ楽しく緩急のあるペースで、お互いの全体的なリズムを合わせながら右方向へ進み続け、ついに画面右端を完全に越えてフレームアウトし、床だけが残る。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt4_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 回転には挑戦せず、既に安定している弾み・ホップの動きにリズムの緩急
  (大・小・小の弾みパターン、数回ごとの手振り)を加えて楽しさを出したバージョン

## ComfyUIでの設定メモ
- Picture 1: D-1と同じ画像
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 回転・宙返りは一切使わず、弾み・ホップという既に安定した動きの
  リズム変化だけで「楽しさ」を出している
