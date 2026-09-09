---
project: H3-Video-Series-v2
cut: C-2d
mode: I2VA
status: draft
---

# カット C-2d: たまちゃんが少し助走をつけてぽよんにぶつかりにいく可愛いバージョン

## シーン内容
Cビート(「ぶつかって笑う」)のもう一つの別バージョン。C-2cの「大きくぶつかって
弾き飛ばされる」よりも軽く・可愛らしいテイストで、たまちゃんが**少し後ろに下がって
助走をつけてから**ぽよんに向かって走り、体当たりする。正面固定カメラ。

1. たまちゃんが2〜3歩、後ろ(画面右側)に下がって助走の距離を取る
2. 助走をつけて、ぽよんに向かって走り出す
3. ぽよんに軽くぶつかる。ぽよんは接触点でやさしくへこみ、その弾力でたまちゃんを
   ふわっと押し返す——たまちゃんは大きく吹き飛ばされることはなく、その場で少し
   後ろによろけて足元がふらつく程度
4. 勢いあまった感じがおかしくて、たまちゃんが笑い出す
5. ぽよんも一緒に笑う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない(点目と輪郭線の口のみ)
- たまちゃんの笑い顔は、目が三日月形になり口が開いて中にコーラルピンクが見える
- ぽよんは接触時に丸みを保ったままへこむ(ディンプル)。中のガムボール・紙吹雪は
  絶対にこぼれない
- **ぽよんの口は絶対に大きく開きすぎないこと**。輪郭線のみ・無着色(体と同じ透明素材、
  中のガムボールが透けて見える)で、口の開き幅は顔の横幅の3分の1程度までにとどめ、
  顔全体に対して控えめなサイズを保つこと

## 参照画像
- Picture 1(最初のフレーム): 「理想画質」の2ショット画像(薄い黄緑色の床+パステルの
  雲を背景に、左にぽよん、右にたまちゃんが並んで立つ構図。C-1・C-2b・C-2cと共通)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static front-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>. Both characters keep their exact appearance, colors, and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point — its face is only round dot eyes and an outline-only mouth. Starting from its position on the right as shown in <Picture 1>, the egg character takes a few small steps backward, away from the transparent, jelly-like rubber character on the left, giving itself a little more room for a running start. Then it toddles forward with a short, eager run-up toward the transparent character and gently bumps into it. The transparent character's round body dimples softly inward at the point of contact without ever flattening or losing its overall roundness, and its gentle springy rebound pushes the egg character lightly backward — not a hard fling, just enough to make it stumble back a small step or two, wobbling on its feet before it catches its balance. No matter how much the transparent character's body compresses, the colorful gumballs and confetti sealed inside it only shift and jostle against each other, never once flying out or escaping through its skin. Amused by its own stumbling momentum, the egg character bursts into happy laughter, its round dot eyes crinkling into laughing crescents — still with no eyebrows — and its mouth opening with a hint of soft coral pink visible inside. Watching this, the transparent character laughs too, its round eyes crinkling shut into laughing crescents while its mouth curves into only a modest, gently rounded smile shape — never opening wide, staying no more than about a third of the width of its face, made of nothing but a thin dark outline: there is no fill, shading, or paint of any color inside this mouth shape, and it stays just as transparent and see-through as its glossy skin, so the colorful gumballs and confetti behind it remain clearly visible straight through the open mouth outline.

overall_soundscape: A few light footsteps as the egg character steps backward, a brief pause, then quick eager footsteps as it runs forward, followed by a soft springy boing on contact and light shuffling as the egg character wobbles and catches its balance. Bright, happy laughter from both characters follows.

non_diegetic_music: A light, playful marimba melody with a little skip in its rhythm as the egg character backs up and runs in, resolving into a warm, cheerful flourish as both characters laugh.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定正面ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映している。2人とも<Picture 1>の見た目・色・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかず、顔は丸い点目と輪郭線だけの口のみである。<Picture 1>で示された右側の位置から、卵形のキャラクターは左側の透明でゼリーのようなラバーキャラクターから離れる方向へ2〜3歩後ずさりし、助走のための距離を少し取る。それから、透明なキャラクターに向かって短く元気によちよちと助走をつけて走り出し、やさしくぶつかる。透明なキャラクターの丸い体は接触点でやわらかくくぼむが、平らになったり丸みを失ったりすることはなく、そのやさしい弾力の反動で卵形のキャラクターを軽く後ろに押し返す——大きく吹き飛ばすのではなく、1〜2歩よろけて足元がふらつく程度に留め、すぐにバランスを取り戻す。透明なキャラクターの体がどれだけ圧縮されても、中に密閉された色とりどりのガムボールと紙吹雪はお互いにぶつかり合って揺れ動くだけで、外に飛び出したり表面からはみ出したりすることはない。自分のよろけた勢いがおかしくて、卵形のキャラクターは嬉しそうに笑い出し、丸い点目が笑いじわの三日月形になる——眉毛はやはりつかない——そして口はほんのりコーラルピンク色をのぞかせながら開く。それを見ていた透明なキャラクターも一緒に笑い出す——丸い目はぎゅっと閉じて笑いじわの三日月形になり、口は大きく開くことなく、控えめで丸みのある笑顔の形にとどまる——顔の横幅の3分の1程度までしか開かず、薄い輪郭線だけでできている。この口の中には色も陰影も塗りも一切なく、光沢のある体の表面とまったく同じように透き通ったままで、後ろにある色とりどりのガムボールと紙吹雪が、開いた口の輪郭線を通してそのままはっきり透けて見える。

**環境音**
卵形のキャラクターが後ずさりする軽い足音、一瞬の間のあと、勢いよく前に駆け出す元気な足音、続いて接触の瞬間の柔らかい「ぼよん」という音、卵形のキャラクターがよろけてバランスを取り戻すすり足の音。その後、2人の明るく嬉しそうな笑い声が続く。

**BGM(観客のみに聞こえる)**
軽やかで楽しげなマリンバのメロディが、卵形のキャラクターが後ずさりして走り出すリズムに合わせて弾み、2人が笑い出す瞬間に温かく明るいフレーズへと落ち着く。

**生成結果**
- 動画ファイル: `03-generated-videos/C2d_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 「理想画質」2ショット画像(C-1・C-2b・C-2cと共通)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 7秒目安(後ずさり→助走→接触→よろけ→2人分の笑いまで含むため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
