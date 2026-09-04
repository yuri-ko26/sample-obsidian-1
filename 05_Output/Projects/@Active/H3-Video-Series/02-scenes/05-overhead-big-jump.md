---
project: H3-Video-Series
scene: 5
mode: I2VA
duration: 7s
---

# シーン5: 俯瞰でぽよんが真上に大ジャンプしてたまちゃんにぶつかる

## シーン内容
俯瞰の固定カメラ。2人がその場で顔を見合わせた瞬間、ぽよんがその場で軽く2回弾む。
たまちゃんは何が起こるのか不思議そうにぽよんを目で追う。3回目の弾みでぽよんは
真上(カメラ方向)へ大きく高くジャンプし、カメラに極めて近づくことで画面いっぱいに
ぽよんで埋め尽くされる。地上に残されたたまちゃんは驚いてぽよんを目で追う。
ぽよんが地面に降りる瞬間、たまちゃんにぶつかり、たまちゃんは横に倒れる。

## 最初のフレーム(Picture 1)
オリーブグリーンの床を真上から見下ろす構図。左に透明なぽよん(中にガムボール)、
右にたまちゃん(白とピンクの丸い頭部、短い腕)が並んでこちらを向いている。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a static overhead shot looks straight down on the olive-green floor as shown in <Picture 1>, with the transparent, jelly-like rubber character on the left and the egg-shaped character on the right, both facing up toward the camera. The two briefly glance toward each other, their eyes turning to meet, before the transparent character begins bouncing lightly in place twice, its round body compressing and lifting slightly with each small bounce while its interior gumballs and confetti shift gently without spilling out. The egg character's eyes follow the transparent character's motion with each bounce, its expression curious and puzzled, watching closely to see what will happen next. On the third bounce, the transparent character launches into a huge, towering jump straight upward toward the camera, rapidly growing larger in frame as it nears the lens until its glossy, rounded body fills the entire screen, completely blocking the view of the floor below. Left alone on the ground, the egg character tilts its head back with wide, startled eyes, tracking the now-enormous shape far above as it hangs at the peak of its jump. The transparent character then begins its descent back toward the floor, growing smaller again as it falls; as it lands, it collides directly into the egg character, its rubbery surface pressing inward into a smooth, curved dimple at the point of contact rather than flattening, staying round like a yo-yo, with none of its balls or confetti spilling out. The instant the transparent character separates from the egg character and leaves the floor, the dimpled area instantly springs back round again, like a water balloon released from pressure, never staying flat or rigid as it moves away. The egg character, its stiff, non-bending limbs unable to absorb the impact, topples sideways onto the floor in one simple motion, coming to rest on its side.

overall_soundscape: A quiet rustle marks the moment the two characters glance toward each other, followed by two soft rubbery bounces with light gumball rattles as the transparent character hops in place. A rising, whooshing bounce sound builds as it launches into its huge jump, growing louder as it fills the frame, then fades slightly as it hangs at the peak before a second whoosh signals its descent. A soft gasp comes from the egg character as it watches, followed by a muffled, springy thud as the transparent character lands and collides into it, and a soft flump as the egg character topples onto its side.

non_diegetic_music: A curious, softly rising pizzicato phrase plays through the bounces and the big jump, swelling at the peak of the leap before a light comedic thud accent lands on the moment of collision.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された通り、オリーブグリーンの床を真上から見下ろす固定の俯瞰ショットで、左に透明でゼリーのようなラバーキャラクター、右に卵形のキャラクターが並び、どちらもカメラの方(上)を向いている。二人は一瞬、互いに目を向け合い、視線が合ったところで、透明なキャラクターがその場で軽く2回弾み始め、小さく跳ねるたびに丸い体が縮んでは少し浮き上がり、中のガムボールと紙吹雪はそっと揺れ動くもののこぼれ出ることはない。卵形のキャラクターの目は、透明なキャラクターが弾むたびにその動きを追い、不思議そうな、いぶかしむような表情で、次に何が起こるのかをじっと見つめている。3回目の弾みで、透明なキャラクターはカメラに向かって真上へ、そびえ立つように大きく高いジャンプを繰り出し、レンズに近づくにつれて画面の中でみるみる大きくなっていき、やがてその光沢のある丸い体が画面全体を埋め尽くし、下の床の様子が完全に見えなくなる。地上に一人残された卵形のキャラクターは、頭をのけぞらせるように見上げ、見開いた驚いた目で、はるか頭上でジャンプの頂点に達している今や巨大に見えるその姿を追い続ける。透明なキャラクターはやがて床へ向かって下降を始め、落ちていくにつれて再び画面の中で小さくなっていく。着地する瞬間、透明なキャラクターは卵形のキャラクターに直接ぶつかり、接触した部分は平らに潰れるのではなく、ヨーヨーのように丸みを保ったままなめらかにくぼみ、中のボールや紙吹雪は一つもこぼれ出ない。透明なキャラクターが卵形のキャラクターから離れ、床からも離れた瞬間、そのへこんでいた部分は水風船から圧力が抜けたときのように即座に丸みを取り戻し、平らで固いまま動き続けることは決してない。卵形のキャラクターは、曲がらない硬い手足では衝撃を受け止めきれず、その場で横向きに一度で倒れ込み、横たわった状態で静止する。

**環境音**
二人が互いに目を向け合う瞬間、かすかな衣擦れのような音がし、続いて透明なキャラクターがその場で弾むたびに、柔らかいゴムの弾む音とガムボールの軽いカタカタという音が2回響く。大きなジャンプに入ると、盛り上がるようなヒュッという音が高まっていき、画面いっぱいに広がるにつれて音も大きくなり、ジャンプの頂点でわずかに音が和らいだのち、下降を告げる2度目のヒュッという音が鳴る。それを見守る卵形のキャラクターから小さな驚きの息づかいが聞こえ、続いて透明なキャラクターが着地してぶつかる、こもった弾力のある衝突音が響き、卵形のキャラクターが横向きに倒れ込む柔らかな「ふすん」という音で締めくくられる。

**BGM(観客のみに聞こえる)**
不思議そうに、そっと音を上げていくピチカートのフレーズが、弾みと大ジャンプの間じゅう流れ、ジャンプの頂点で盛り上がり、衝突の瞬間には軽くコミカルな「ドスン」というアクセントが入る。

## ComfyUIでの設定メモ
- 最初のフレーム画像(オリーブグリーンの床に2人が並ぶ俯瞰構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 7秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
