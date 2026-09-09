---
project: H3-Video-Series-v2
cut: C-2
mode: I2VA
status: draft
---

# カットC-2: たまちゃんが起き上がり、確信の笑顔で再び体当たり→今度はぽよんも転がって大笑い

## シーン内容
香盤表ビートC(「ぶつかって笑う」)の2回目。C-1からの**カットの継続性**が重要:
C-1の実際の最終フレームでは、たまちゃんは仰向けではなく、**横向きに前のめりで
倒れ込んだ姿勢**(頭が下がり気味、脚が後ろに伸びている)で笑っている。C-2はその
実際のポーズから始めて「起き上がる」動きを含めることで、2つのカットがつながって
見えるようにする。正面固定カメラ。

1. (C-1の実際の最終フレームの姿勢から)たまちゃんが、前のめりに倒れ込んだ姿勢から
   硬い腕を使って体を起こし、ぐらつきながらも元の立ち姿勢に戻る
2. 起き上がったところでぽよんと目が合う。この時たまちゃんの表情は、C-1の時のような
   「勇気を出す」間ではなく、**すでにいたずらっぽく確信めいた笑顔**(楽しさをもう知っている)
3. ためらわず、嬉しそうに(即座に)ぽよんに体当たりする
4. 今回はより強い勢いのため、**ぽよんも横に転がって倒れる**(C-1ではぽよんは倒れなかったが、
   今回は倒れる。丸みは保ったまま横倒しになり、決して平らにはならない)
5. たまちゃんは自分の体当たりの勢いのまま仰向けに転がる
6. 予想通りの楽しさに大喜びで笑う(驚きではなく、期待通りだった喜び)
7. 転がったままのぽよんもたまちゃんを見て、一緒に笑う

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に今回関係する制約:
- たまちゃんが起き上がる動き:踵をつけず、足首を曲げない棒状の足のまま、硬い腕で体を押し上げる
  (`02-scenes/20-tamachan-gets-back-up.md` の設計を踏襲)
- ぽよんが転がって倒れても、常に丸み(しずく型)を保ったまま。接触面が平らなまま残ることはなく、
  離れれば水風船のようにすぐ丸みを取り戻す
- ぽよんの中のガムボール・紙吹雪は絶対にこぼれない
- ぽよんの口は、笑っても輪郭線のみ・無着色のまま
- たまちゃんの笑い顔は、目が三日月形になり口が開いて中にコーラルピンクが見える

## 参照画像
- Picture 1(最初のフレーム): **C-1の実際の最終フレーム(受領・確定済み)**。画面左に
  ぽよんが立ち、目を閉じた三日月形の笑い目、輪郭線の口を大きく開けて笑い、中の
  ガムボール(赤・黄・緑・青)と紙吹雪が口の輪郭線を通して透けて見えている(色は
  ついていない)。画面右にたまちゃんが、横向きに前のめりに倒れ込んだ姿勢——頭部
  (白い殻側)がやや下がり、ピンクの殻側が上を向き、短い焦げ茶色の手足が後ろに
  伸びた状態——で、目を閉じた三日月形、口を開けてほんのりコーラルピンクが
  のぞく笑顔になっている。背景は薄い黄緑色の床+パステルの雲(Look Reference通り)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static front-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, continues from the exact framing shown in <Picture 1>, where the transparent, jelly-like rubber character stands on the left laughing, and the egg-shaped character on the right rests tipped forward onto its side, its head lowered and its short legs stretched out behind it, laughing in this tumbled pose. Both characters keep their exact appearance, colors, and design from <Picture 1> unchanged throughout, with no distortion. The egg character's laughter settles, and it braces its short, stiff, non-bending arms against the floor, pushing itself back upright from this tipped-over position, wobbling slightly as it rights itself and finds its balance before settling back into its normal standing pose, its feet never letting its heels touch the ground. Once standing, its eyes meet the transparent character's — and unlike hesitating, its expression is immediately a knowing, mischievous grin, already anticipating how much fun this is about to be. Without any pause to gather courage this time, the egg character happily and immediately launches itself sideways at the transparent character in an eager tackle. This time the impact carries much greater force: the transparent character itself is knocked off balance, its round body tipping sideways and toppling over to rest tilted on the floor, still perfectly round and never flattening. No matter how hard this impact is or how much the transparent character's body shakes and tips over, its sealed skin holds completely intact and the colorful gumballs and confetti inside only jostle against each other, never once flying out, falling loose, or escaping through its surface. Carried by its own momentum, the egg character tumbles backward and lands on its back again, and immediately bursts into delighted laughter — not from surprise this time, but from pure delight that it turned out exactly as much fun as it expected. Still resting tilted on its side on the floor, the transparent character turns to look at the egg character and laughs along with it, its round eyes crinkling shut into laughing crescents while its mouth stretches into a wide curved shape made of nothing but a thin dark outline, exactly like the rest of its clear body: there is no fill, shading, or paint of any color inside this mouth shape, and it stays just as transparent and see-through as its glossy skin, so the colorful gumballs and confetti behind it remain clearly visible straight through the open mouth outline, never obscured by any solid color and never spilling through the open shape either.

overall_soundscape: A soft rustle as the egg character pushes itself up and wobbles back onto its feet, followed by a moment of quiet as their eyes meet. A quick patter of footsteps as the egg character launches itself at the transparent character, then a deeper, springy boing as the impact knocks the transparent character off balance, mixed with a soft thud as it tips onto the floor. A second soft thud follows as the egg character tumbles onto its back. Bright, delighted laughter from both characters fills the rest of the shot.

non_diegetic_music: A playful, bouncy marimba melody, quieting briefly as the egg character stands up and their eyes meet, then bursting into an upbeat, tumbling flourish through the tackle and both characters' laughter.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定正面ショットで、<Picture 1>に示された通り、画面左で透明でゼリーのようなラバーキャラクターが立って笑い、画面右で卵形のキャラクターが横向きに前のめりに倒れ込み、頭を下げ気味に、短い脚を後ろに伸ばした姿勢のまま笑っている構図から続く。2人とも<Picture 1>の見た目・色・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターの笑いが落ち着き、短く硬い曲がらない腕を床について、その倒れ込んだ姿勢から体を起こし、少しぐらつきながら体勢を立て直してバランスを取ったあと、通常の立ち姿勢に戻る——足は最後まで踵が地面につくことはない。立ち上がったところで透明なキャラクターと目が合う——今回はためらう様子はなく、表情は最初からいたずらっぽく確信めいた笑顔で、これからどれだけ楽しくなるかをすでに分かっている様子である。今回は勇気を溜める間もなく、卵形のキャラクターは嬉しそうに、すぐさま透明なキャラクターに向かって横に体当たりする。今回の衝突ははるかに強い勢いを伴い、透明なキャラクター自身もバランスを崩し、丸い体が横に傾いて床の上に倒れ込む——それでも常に丸みを保ったままで、決して平らになることはない。この衝撃がどれだけ強くても、体がどれだけ揺れたり傾いたりしても、密閉された表面は完全に保たれ、中の色とりどりのガムボールと紙吹雪はお互いにぶつかり合って揺れ動くだけで、一度たりとも外に飛び出したり、こぼれ落ちたり、表面からはみ出したりすることはない。自分自身の勢いに運ばれるまま、卵形のキャラクターは後ろに転がって再び仰向けに倒れ、すぐに嬉しそうな笑い声を上げる——今回は驚きからではなく、予想通りにこれほど楽しかったという純粋な喜びからの笑いである。床の上に横倒しのまま留まっている透明なキャラクターも、卵形のキャラクターの方を向いて一緒に笑う——丸い目はぎゅっと閉じて笑いじわの三日月形になり、口は体の他の部分とまったく同じ、薄い輪郭線だけでできた大きくカーブした形に伸びる。この口の中には色も陰影も塗りも一切なく、光沢のある体の表面とまったく同じように透き通ったままで、後ろにある色とりどりのガムボールと紙吹雪が、開いた口の輪郭線を通してそのままはっきり透けて見え、どんな色にも塗りつぶされることも、その開いた形からこぼれ出ることもない。

**環境音**
卵形のキャラクターが体を起こしてぐらつきながら立ち上がるやわらかな衣擦れの音、続いて目が合う一瞬の静けさ。卵形のキャラクターが透明なキャラクターに向かって駆け出す軽い足音、そして衝突の瞬間の深みのある弾む「ぼよん」という音(透明なキャラクターがバランスを崩す様子とともに)、床に倒れ込む柔らかい「どすん」という音が混ざる。卵形のキャラクターが仰向けに転がる際にもう一度柔らかい「どすん」という音が続く。その後は2人の明るく嬉しそうな笑い声がショットの最後まで続く。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディ。たまちゃんが起き上がり目が合う瞬間に一度静かになり、体当たりから2人の笑いにかけて、明るく転がるような盛り上がりのフレーズへとつながる。

**生成結果**
- 動画ファイル: `03-generated-videos/C2_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- 最初のフレーム画像: **C-1の実際の最終フレーム(確定済み)**——ぽよん左・たまちゃん右
  (横向きに前のめりで倒れた姿勢)——を使用
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 12秒目安(起き上がる→目が合う→体当たり→ぽよんが倒れる→たまちゃんが転がる→2人の
  笑いまで含む長めのアクションのため。生成して尺が余る/足りないようなら調整)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 生成後は必ず`01-characters/character-reference.md`の「画質・色味の基準」2枚と見比べて、明るさ・彩度・質感がズレていないか確認する
