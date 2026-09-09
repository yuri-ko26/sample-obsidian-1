---
project: H3-Video-Series-v2
cut: C-2
mode: I2VA
status: draft
---

# カットC-2: たまちゃんが起き上がり、確信の笑顔で再び体当たり→今度はぽよんも転がって大笑い

## シーン内容
香盤表ビートC(「ぶつかって笑う」)の2回目。C-1からの**カットの継続性**が重要:
C-1はたまちゃんが仰向けで笑い転げている状態で終わるため、C-2はその状態から始めて
「起き上がる」動きを含めることで、2つのカットがつながって見えるようにする。正面固定カメラ。

1. (C-1の続きの姿勢から)たまちゃんが仰向けの状態から、硬い腕を使って体を起こし、
   ぐらつきながらも元の立ち姿勢に戻る
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
- Picture 1(最初のフレーム): **C-1の最終フレーム**(たまちゃんが仰向けで笑い転げていて、
  ぽよんはその横に立って一緒に笑っている構図)。C-1を生成したら、その最終フレームの
  スクリーンショットをここで使用し、見た目のカットのつながりを保証する。
  (まだC-1が未生成のため、現時点ではC-1のプロンプト文中の終了時の記述を仮の設計として使用)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static front-on shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, continues from the exact framing shown in <Picture 1>, where the egg-shaped character lies on its back laughing beside the transparent, jelly-like rubber character standing next to it. Both characters keep their exact appearance, colors, and design from <Picture 1> unchanged throughout, with no distortion. The egg character's laughter settles, and it pushes itself upright using its short, stiff, non-bending arms, wobbling slightly as it finds its balance before settling back into its normal standing pose, its feet never letting its heels touch the ground. Once standing, its eyes meet the transparent character's — and unlike hesitating, its expression is immediately a knowing, mischievous grin, already anticipating how much fun this is about to be. Without any pause to gather courage this time, the egg character happily and immediately launches itself sideways at the transparent character in an eager tackle. This time the impact carries much greater force: the transparent character itself is knocked off balance, its round body tipping sideways and toppling over to rest tilted on the floor, still perfectly round and never flattening, its interior gumballs and confetti shifting but never spilling out. Carried by its own momentum, the egg character tumbles backward and lands on its back again, and immediately bursts into delighted laughter — not from surprise this time, but from pure delight that it turned out exactly as much fun as it expected. Still resting tilted on its side on the floor, the transparent character turns to look at the egg character and laughs along with it, its round eyes crinkling shut into laughing crescents while its flat, outline-only mouth stretches into a wide, uncolored grin with no depth or interior color.

overall_soundscape: A soft rustle as the egg character pushes itself up and wobbles back onto its feet, followed by a moment of quiet as their eyes meet. A quick patter of footsteps as the egg character launches itself at the transparent character, then a deeper, springy boing as the impact knocks the transparent character off balance, mixed with a soft thud as it tips onto the floor. A second soft thud follows as the egg character tumbles onto its back. Bright, delighted laughter from both characters fills the rest of the shot.

non_diegetic_music: A playful, bouncy marimba melody, quieting briefly as the egg character stands up and their eyes meet, then bursting into an upbeat, tumbling flourish through the tackle and both characters' laughter.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定正面ショットで、<Picture 1>に示された通り、卵形のキャラクターが仰向けで笑いながら横たわり、そのすぐそばに透明でゼリーのようなラバーキャラクターが立っている構図から続く。2人とも<Picture 1>の見た目・色・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターの笑いが落ち着き、短く硬い曲がらない腕を使って体を起こし、少しぐらつきながらバランスを取ったあと、通常の立ち姿勢に戻る——足は最後まで踵が地面につくことはない。立ち上がったところで透明なキャラクターと目が合う——今回はためらう様子はなく、表情は最初からいたずらっぽく確信めいた笑顔で、これからどれだけ楽しくなるかをすでに分かっている様子である。今回は勇気を溜める間もなく、卵形のキャラクターは嬉しそうに、すぐさま透明なキャラクターに向かって横に体当たりする。今回の衝突ははるかに強い勢いを伴い、透明なキャラクター自身もバランスを崩し、丸い体が横に傾いて床の上に倒れ込む——それでも常に丸みを保ったままで、決して平らになることはなく、中のガムボールと紙吹雪は揺れ動くもののこぼれることはない。自分自身の勢いに運ばれるまま、卵形のキャラクターは後ろに転がって再び仰向けに倒れ、すぐに嬉しそうな笑い声を上げる——今回は驚きからではなく、予想通りにこれほど楽しかったという純粋な喜びからの笑いである。床の上に横倒しのまま留まっている透明なキャラクターも、卵形のキャラクターの方を向いて一緒に笑う——丸い目はぎゅっと閉じて笑いじわの三日月形になり、平面的で輪郭線だけの口は奥行きも中の色もないまま大きな無着色の笑顔に伸びる。

**環境音**
卵形のキャラクターが体を起こしてぐらつきながら立ち上がるやわらかな衣擦れの音、続いて目が合う一瞬の静けさ。卵形のキャラクターが透明なキャラクターに向かって駆け出す軽い足音、そして衝突の瞬間の深みのある弾む「ぼよん」という音(透明なキャラクターがバランスを崩す様子とともに)、床に倒れ込む柔らかい「どすん」という音が混ざる。卵形のキャラクターが仰向けに転がる際にもう一度柔らかい「どすん」という音が続く。その後は2人の明るく嬉しそうな笑い声がショットの最後まで続く。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディ。たまちゃんが起き上がり目が合う瞬間に一度静かになり、体当たりから2人の笑いにかけて、明るく転がるような盛り上がりのフレーズへとつながる。

**生成結果**
- 動画ファイル: `03-generated-videos/C2_v1.mp4`(未生成)
- 判定: 未検証
- メモ: Picture 1はC-1の実際の最終フレームに差し替えること(現状は仮設計)

## ComfyUIでの設定メモ
- 最初のフレーム画像: **C-1生成後の最終フレーム**(たまちゃん仰向け+ぽよん起立の構図)を使用。
  C-1がまだ未生成の場合は、C-1完成後にこのメモを更新してから生成すること
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 12秒目安(起き上がる→目が合う→体当たり→ぽよんが倒れる→たまちゃんが転がる→2人の
  笑いまで含む長めのアクションのため。生成して尺が余る/足りないようなら調整)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 生成後は必ず`01-characters/character-reference.md`の「画質・色味の基準」2枚と見比べて、明るさ・彩度・質感がズレていないか確認する
