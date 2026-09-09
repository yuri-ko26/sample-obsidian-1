---
project: H3-Video-Series
scene: 15
mode: I2VA
duration: 9s
---

# シーン15: 雲の稜線でかくれんぼ(ぽよんが隠れて、たまちゃんが探して発見)

## シーン内容
シーン9と同じ最初のフレーム(横からの固定カメラ、雲の稜線)を使った別パターン。
ぽよんがジャンプしながらフレームアウトした後、雲の奥の方からひょこっと顔を出して隠れる。
たまちゃんは、いなくなったぽよんの姿を探して辺りを見回しながら画面の中を進んでいく。
ぽよんを発見すると、たまちゃんは大喜びでぽよんの方へ走っていき、そのままフレームアウトする。
カットは割らず、最初から最後まで単一のショットとして描写する。

## 最初のフレーム(Picture 1)
シーン9と同じ、パステルカラーの雲(ピンク・ラベンダー・ミントグリーン)を背景にした
横からの構図。手前左のラベンダー色の雲の上にたまちゃんが立ち、奥右上のミントグリーンの
雲の上空にぽよんが浮かんでいる。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, as shown in <Picture 1>: a soft pastel-purple sky above layered rounded cloud hills in pink, lavender, and mint green, with the egg-shaped character standing on a lavender cloud ridge in the foreground left, and the transparent, jelly-like rubber character hovering above a mint-green cloud ridge further back on the right, its round dark eyes and flat, outline-only mouth with no depth and no colored interior, the mouth staying pure uncolored line work at all times. The camera never pans, tilts, zooms, or cuts away at any point, and no cut ever interrupts this one unbroken shot. The transparent character springs into a bouncy jump and exits the frame completely past the right edge, vanishing from view, its interior gumballs and confetti drifting but never spilling out as it moves. A beat later, it peeks back into view from a different spot, poking just its head and shoulders up from behind a distant mint-green cloud hill deeper in the background, partially hidden, watching quietly. The egg character, noticing the transparent character is no longer in its usual place, tilts its head and begins toddling in its stiff, heel-less waddle across the cloud ridges, moving further into the frame as it looks side to side, searching for its missing friend. As the egg character's search brings it closer to the distant cloud where the transparent character is peeking, its eyes suddenly widen with delighted surprise upon spotting it, its outline mouth stretching into a wide, joyful grin. Overjoyed at finding its friend, the egg character breaks into an excited, hurried toddle straight toward the peeking transparent character, and the two bounce and toddle off together past the edge of the frame, vanishing from view as the shot ends.

overall_soundscape: A springy bounce sound and light gumball rattle mark the transparent character's jump out of frame, followed by a quiet, playful rustle as it peeks out from behind the distant cloud. Soft, muffled toddling footsteps accompany the egg character's searching steps, pausing briefly before a small gasp of delight marks the moment of discovery, followed by quicker, excited footsteps and both characters' happy giggles as they hurry off together.

non_diegetic_music: A curious, softly searching pizzicato phrase plays during the search, pausing briefly on a suspended note, then resolving into a bright, joyful flourish at the moment of discovery as the characters hurry off together.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り、パステルパープルがかった空の下に、ピンク・ラベンダー・ミントグリーンの丸みを帯びた雲の山が層になった景色が広がり、手前左のラベンダー色の雲の稜線に卵形のキャラクターが立ち、さらに奥、右側のミントグリーンの雲の稜線の上空に、透明でゼリーのようなラバーキャラクターが浮かんでいる。その丸い黒目と、奥行きも中の色もない平面的な輪郭線だけの口は、常に色のつかない線画のままである。カメラは一切パン・チルト・ズームせず、この一つの途切れないショットをカットが遮ることは決してない。透明なキャラクターは弾むようにジャンプし、画面右端の外へ完全に出て姿を消し、動いている間、中のガムボールと紙吹雪は揺れ動くもののこぼれ出ることはない。少し経つと、別の場所から再び姿を見せ、頭と肩の部分だけを、さらに奥にあるミントグリーンの遠い雲の山の陰からひょこっと覗かせ、半分隠れたまま静かに様子をうかがう。卵形のキャラクターは、透明なキャラクターがいつもの場所にいないことに気づき、首をかしげ、硬く踵のつかないよちよち歩きで雲の稜線の上を進み始め、左右を見回しながら画面の中をさらに奥へと進んでいき、いなくなった友達を探す。探しているうちに、透明なキャラクターが覗いている遠くの雲に近づいていくと、卵形のキャラクターの目が突然、喜びの見開いた表情になり、輪郭線だけの口が大きく嬉しそうな笑顔の形に伸びる。友達を見つけた喜びのあまり、卵形のキャラクターは興奮した様子で急いでよちよちと、覗いている透明なキャラクターの方へまっすぐ向かっていき、二人は一緒に弾みながら、よちよち歩きながら画面の外へ出て、姿が見えなくなったところでこのショットは終わる。

**環境音**
透明なキャラクターが画面の外へ跳んでいく瞬間、弾むような音と軽いガムボールのカタカタという音が鳴り、続いて遠くの雲の陰から覗く際には、静かで遊び心のある衣擦れのような音がする。卵形のキャラクターが探し歩く間は、柔らかくこもったよちよち歩きの足音が続き、一瞬止まった後、発見の瞬間に小さな喜びの息づかいが聞こえ、その後は少し速くなった足音と、二人が一緒に急いで去っていく間の楽しそうな笑い声が続く。

**BGM(観客のみに聞こえる)**
不思議そうに、そっと探るようなピチカートのフレーズが、探している間ずっと流れ、一瞬宙に浮いたような音で止まった後、発見の瞬間に明るく喜びに満ちたフレーズへと解決し、二人が一緒に急いで去っていく。

## ComfyUIでの設定メモ
- 最初のフレーム画像(シーン9と同じ、パステルの雲を背景に、手前左にたまちゃん・奥右上にぽよんが浮かぶ横からの構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 9秒(プロンプト内の秒数表記と要一致)
- **重要**: シーン9と同様、`[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
