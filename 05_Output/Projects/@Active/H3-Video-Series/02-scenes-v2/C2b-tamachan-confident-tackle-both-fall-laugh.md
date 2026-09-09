---
project: H3-Video-Series-v2
cut: C-2b
mode: I2VA
status: draft
---

# カットC-2b: 目が合い確信の笑顔で即座に体当たり→今度はぽよんも転がって大笑い

## シーン内容
元のC-2を2つに分割した後半部分。C-2aで立ち上がり終わった状態(「理想画質」2ショット
画像と同じポーズ)から始まる。正面固定カメラ。

1. 2人の目が合う。たまちゃんの表情は、C-1の時のような「勇気を出す」間ではなく、
   **すでにいたずらっぽく確信めいた笑顔**(楽しさをもう知っている)
2. ためらわず、嬉しそうに(即座に)ぽよんに体当たりする
3. 今回はより強い勢いのため、**ぽよんも横に転がって倒れる**(C-1ではぽよんは倒れなかったが、
   今回は倒れる。丸みは保ったまま横倒しになり、決して平らにはならない)
4. たまちゃんは自分の体当たりの勢いのまま転がる
5. 予想通りの楽しさに大喜びで笑う(驚きではなく、期待通りだった喜び)
6. 転がったままのぽよんもたまちゃんを見て、一緒に笑う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- ぽよんが転がって倒れても、常に丸み(しずく型)を保ったまま。接触面が平らなまま残ることはなく、
  離れれば水風船のようにすぐ丸みを取り戻す
- ぽよんの中のガムボール・紙吹雪は、衝撃がどれだけ強くても絶対にこぼれない
- ぽよんの口は、笑っても輪郭線のみ・無着色のまま(体と同じ透明素材、中のガムボールが透けて見える)
- たまちゃんの笑い顔は、目が三日月形になり口が開いて中にコーラルピンクが見える

## 参照画像
- Picture 1(最初のフレーム): C-1のPicture1として使った「理想画質」の2ショット画像
  (薄い黄緑色の床+パステルの雲を背景に、左にぽよん、右にたまちゃんが並んで
  立つ構図)。C-2aの終了フレームと同一

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static front-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>. Both characters keep their exact appearance, colors, and design from <Picture 1> unchanged throughout, with no distortion. Standing calmly as shown in <Picture 1>, the egg character on the right and the transparent, jelly-like rubber character on the left make eye contact — and immediately, without any pause to gather courage, the egg character's expression becomes a knowing, mischievous grin, already anticipating how much fun this is about to be. Happily and without hesitation, it launches itself sideways at the transparent character in an eager tackle. This time the impact carries much greater force than before: the transparent character itself is knocked off balance, its round body tipping sideways and toppling over to rest tilted on the floor, still perfectly round and never flattening. No matter how hard this impact is or how much the transparent character's body shakes and tips over, its sealed skin holds completely intact and the colorful gumballs and confetti inside only jostle against each other, never once flying out, falling loose, or escaping through its surface. Carried by its own momentum, the egg character tumbles and lands tipped over on the floor as well, and immediately bursts into delighted laughter — not from surprise this time, but from pure delight that it turned out exactly as much fun as it expected. Still resting tilted on its side on the floor, the transparent character turns to look at the egg character and laughs along with it, its round eyes crinkling shut into laughing crescents while its mouth stretches into a wide curved shape made of nothing but a thin dark outline, exactly like the rest of its clear body: there is no fill, shading, or paint of any color inside this mouth shape, and it stays just as transparent and see-through as its glossy skin, so the colorful gumballs and confetti behind it remain clearly visible straight through the open mouth outline, never obscured by any solid color and never spilling through the open shape either.

overall_soundscape: A moment of quiet as their eyes meet, then a quick patter of footsteps as the egg character launches itself at the transparent character, followed by a deeper, springy boing as the impact knocks the transparent character off balance, mixed with soft thuds as both characters tip and tumble onto the floor. Bright, delighted laughter from both characters fills the rest of the shot.

non_diegetic_music: A playful, bouncy marimba melody that bursts into an upbeat, tumbling flourish through the tackle and both characters' laughter.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定正面ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映している。2人とも<Picture 1>の見た目・色・デザインのまま、崩れたり変化したりすることなく保たれる。<Picture 1>の通り穏やかに立っている状態から、右側の卵形のキャラクターと左側の透明なキャラクターの目が合う——そして今回は勇気を溜める間もなく、卵形のキャラクターの表情はすぐさま、いたずらっぽく確信めいた笑顔になる。これからどれだけ楽しくなるかをすでに分かっている様子である。嬉しそうに、ためらうことなく、透明なキャラクターに向かって横に体当たりする。今回の衝突は以前よりもはるかに強い勢いを伴い、透明なキャラクター自身もバランスを崩し、丸い体が横に傾いて床の上に倒れ込む——それでも常に丸みを保ったままで、決して平らになることはない。この衝撃がどれだけ強くても、体がどれだけ揺れたり傾いたりしても、密閉された表面は完全に保たれ、中の色とりどりのガムボールと紙吹雪はお互いにぶつかり合って揺れ動くだけで、一度たりとも外に飛び出したり、こぼれ落ちたりすることはない。自分自身の勢いに運ばれるまま、卵形のキャラクターも床の上に倒れ込み、すぐに嬉しそうな笑い声を上げる——今回は驚きからではなく、予想通りにこれほど楽しかったという純粋な喜びからの笑いである。床の上に横倒しのまま留まっている透明なキャラクターも、卵形のキャラクターの方を向いて一緒に笑う——丸い目はぎゅっと閉じて笑いじわの三日月形になり、口は体の他の部分とまったく同じ、薄い輪郭線だけでできた大きくカーブした形に伸びる。この口の中には色も陰影も塗りも一切なく、光沢のある体の表面とまったく同じように透き通ったままで、後ろにある色とりどりのガムボールと紙吹雪が、開いた口の輪郭線を通してそのままはっきり透けて見え、どんな色にも塗りつぶされることも、その開いた形からこぼれ出ることもない。

**環境音**
目が合う一瞬の静けさ、続いて卵形のキャラクターが透明なキャラクターに向かって駆け出す軽い足音、そして衝突の瞬間の深みのある弾む「ぼよん」という音(透明なキャラクターがバランスを崩す様子とともに)、2人とも床に倒れ込む柔らかい「どすん」という音が混ざる。その後は2人の明るく嬉しそうな笑い声がショットの最後まで続く。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、体当たりから2人の笑いにかけて、明るく転がるような盛り上がりのフレーズへとつながる。

**生成結果**
- 動画ファイル: `03-generated-videos/C2b_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 「理想画質」2ショット画像(C-1・C-2aと共通)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 8秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
