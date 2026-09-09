---
project: H3-Video-Series-v2
cut: C-1
mode: I2VA
status: draft
---

# カットC-1: ぽよんが弾む→たまちゃんが体当たり→弾かれて転び、大笑い

## シーン内容
香盤表ビートC(「ぶつかって笑う」)の1回目。正面固定カメラ。

Picture 1(百合子さん指定の「画質・色味の理想」参照画像)を最初のフレームとして使用。
ぽよんとたまちゃんが並んで立っている状態から始まる。

1. ぽよんがその場で軽く2回はずむ(水風船のような柔らかい弾み)
2. 隣で見ていたたまちゃんが、楽しそうなぽよんを見て勇気を出し、横にジャンプして体当たりする
3. ぽよんに弾かれて、たまちゃんは倒れる
4. 面白い動きになったのがおかしくて、たまちゃんは笑い出す
5. それを見てぽよんも笑う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に今回関係する制約:
- ぽよんは接触時に丸みを保ったままへこむ(ディンプル)。接触が終われば即座に丸みを取り戻す
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない
- ぽよんの口は、笑っても輪郭線のみ・無着色のまま(たまちゃんと違い、口の中に色はつかない)
- たまちゃんの笑い顔は、目が三日月形になり口が開いて中にコーラルピンクが見える(例外表現)
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま動く

## 参照画像
- Picture 1(最初のフレーム): 百合子さん指定の「画質・色味の理想」参照画像(薄い黄緑色の床+
  パステルの雲を背景に、左にぽよん、右にたまちゃんが並んで立つ2ショット)。このカット単体の
  構図としても、そのまま最初のフレームとして使える

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static front-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>. Both characters keep their exact appearance, colors, and design from <Picture 1> unchanged throughout, with no distortion. On the left, the transparent, jelly-like rubber character bounces lightly in place twice, its round body compressing slightly downward and springing back up each time like a soft water balloon, its interior gumballs and confetti shifting gently inside without ever spilling out. Watching it bounce happily, the egg-shaped character on the right visibly gathers its courage for a brief beat, then launches itself sideways through the air toward the transparent character, throwing its whole body into a playful tackle. The instant it makes contact, the transparent character's round body dimples inward at the point of contact without ever flattening or losing its overall roundness, and its springy rebound knocks the egg character backward off its feet; the egg character topples sideways to the floor, its short stiff legs flipping up as it lands. The moment it lands, the egg character bursts into delighted laughter at how funny the tumble felt, its eyes crinkling shut into laughing crescents and its mouth opening wide with a hint of soft coral pink visible inside. Watching this, the transparent character laughs too, its round eyes crinkling shut into laughing crescents while its flat, outline-only mouth stretches into a wide, uncolored grin with no depth or interior color, its body already back to perfectly round with no trace of the earlier contact point remaining.

overall_soundscape: Two soft, rubbery squeak-bounces from the transparent character, then a light patter as the egg character launches itself sideways, followed by a springy boing on impact and a soft thud as the egg character topples to the floor. Bright, delighted laughter from both characters follows.

non_diegetic_music: A playful, bouncy marimba melody that lifts into a warm, cheerful flourish the moment both characters burst into laughter.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定正面ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映している。2人とも<Picture 1>の見た目・色・デザインのまま、崩れたり変化したりすることなく保たれる。左側の透明でゼリーのようなラバーキャラクターが、その場で軽く2回はずむ——水風船のように体がわずかに沈んでは弾んで戻る動きを2回繰り返し、中のガムボールと紙吹雪はやさしく揺れ動くがこぼれることはない。それを楽しそうに見ていた右側の卵形のキャラクターは、一瞬勇気を溜めるような間を見せたあと、横に飛び出して透明なキャラクターに向かって体全体で楽しそうに体当たりする。接触した瞬間、透明なキャラクターの丸い体は接触点でくぼむが、平らになったり丸みを失ったりすることはなく、その弾力のある反動で卵形のキャラクターは後ろによろけて足を取られ、短く硬い脚を跳ね上げながら横向きに床へ転がる。着地した瞬間、卵形のキャラクターはその転び方があまりにおかしくて嬉しそうに笑い出し、目は三日月形にきゅっと細まり、口は大きく開いて中にほんのりコーラルピンク色がのぞく。それを見ていた透明なキャラクターも一緒に笑い出す——丸い目はぎゅっと閉じて笑いじわの三日月形になり、平面的で輪郭線だけの口は奥行きも中の色もないまま大きな無着色の笑顔に伸び、体はすでに接触の跡も残らず完全に丸い形に戻っている。

**環境音**
透明なキャラクターが2回はずむやわらかいゴムの弾む音、卵形のキャラクターが横に飛び出す軽い足音、接触した瞬間の弾むような「ぼよん」という音、卵形のキャラクターが床に転がる柔らかい「どすん」という音。その後、2人の明るく嬉しそうな笑い声が続く。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、2人が笑い出す瞬間に温かく明るいフレーズへと盛り上がる。

**生成結果**
- 動画ファイル: `03-generated-videos/C1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- 最初のフレーム画像(百合子さん指定の「画質・色味の理想」2ショット画像)を Load Image → I2VA用の画像入力に接続
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 8秒目安(ぽよん2回弾む→溜め→ジャンプ→着地→2人分の笑いまで含むため、6秒だと窮屈な可能性。生成して尺が余る/足りないようなら調整)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 生成後は必ず`01-characters/character-reference.md`の「画質・色味の基準」2枚と見比べて、明るさ・彩度・質感がズレていないか確認する
