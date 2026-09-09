---
project: H3-Video-Series
scene: 20
mode: FL2VA
duration: 4s
---

# シーン20: 転んだたまちゃんが起き上がって元の立ち姿勢に戻る

## シーン内容
シーン16の続き。転んで仰向けになり、手足を上げて笑っているたまちゃんが、
起き上がって元の立ち姿勢に戻る。ぽよんはその隣でずっと立ったまま見守っている。
カメラは完全固定。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 淡い緑の床、パステルの雲を背景に、左にぽよん(中に
  赤・黄・緑・青のガムボールと紙吹雪)が立ち、右でたまちゃんが仰向けに転んで
  手足を上げ、笑っている構図
- Picture 2(最後のフレーム): 同じ構図で、左にぽよんが立ったまま、右でたまちゃんが
  起き上がって元通り立っている構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, beginning in the position established by Picture 1: the transparent, jelly-like rubber character stands upright on the left on the pale green floor against soft pastel cloud shapes, its interior gumballs and confetti resting gently, while the egg-shaped character lies on its back on the right, its stiff little arms and legs raised up in the air, its eyes crinkled shut and its mouth open wide in a happy laugh with a hint of soft pink visible inside, still catching its breath from the tumble. The camera never pans, tilts, zooms, or cuts away at any point. The transparent character stays in place, its flat, outline-only mouth staying pure uncolored line work throughout, watching over the egg character with a warm, patient smile. The egg character's laughter settles, and it plants its stiff arms against the floor, pushing itself upright in a simple, slightly wobbly motion, its non-bending ankles and heel-less feet finding their balance one small rock at a time. It rises past sitting and up onto its feet, straightening out fully until it stands upright again in the exact pose and position shown in Picture 2, its outline mouth curving back into its usual content smile as it settles beside the transparent character, both of them facing the camera together at the end of the shot.

overall_soundscape: A few last breathy giggles trail off from the egg character as it lies on its back. A series of soft, muffled shuffling sounds and small rocking thuds mark it pushing itself upright, with a light wobble creak as it finds its balance on its stiff feet, settling into a quiet, contented silence as it comes to a stop standing beside the transparent character.

non_diegetic_music: A gentle, playful pizzicato phrase plays softly as the egg character catches its breath, then rises in a light, bouncy little climbing melody that matches it getting back on its feet, resolving into a warm, settled chord as it stands upright again.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、Picture 1で示された構図から始まる — 透明でゼリーのようなラバーキャラクターが左側、淡い緑の床の上にパステルの雲を背景にして立ち、中のガムボールと紙吹雪は落ち着いて静止しており、右側では卵形のキャラクターが仰向けに倒れたまま、硬い小さな手足を宙に上げ、目をぎゅっと閉じて笑い、口を大きく開けてその内側にほんのりピンク色が覗いており、まだ転んだ余韻で息を弾ませている。カメラは一切パン・チルト・ズーム・カットをしない。透明なキャラクターはその場から動かず、平面的で輪郭線だけの口は終始無着色の線画のままで、温かく気長な笑顔で卵形のキャラクターを見守っている。卵形のキャラクターの笑いが落ち着くと、硬い腕を床に突いて、少しふらつきながらもシンプな動作で体を起こしていき、曲がらないくるぶしと踵のない足で少しずつバランスを取り戻していく。座った姿勢を過ぎてそのまま足の上に立ち上がり、Picture 2で示された通りのポーズと位置になるまでまっすぐ伸び上がり、輪郭線の口はいつもの満足げな笑顔に戻り、透明なキャラクターの隣に落ち着いたところで、二人ともカメラの方を向いてショットが終わる。

**環境音**
卵形のキャラクターが仰向けのまま、息の切れた最後の笑い声が数回聞こえる。体を起こしていく間、柔らかくこもった衣擦れの音と、小さく体を揺らして起き上がる際のコトコトという音が続き、硬い足でバランスを取る瞬間には軽いきしみ音が入り、透明なキャラクターの隣に立ち止まると静かで落ち着いた雰囲気になる。

**BGM(観客のみに聞こえる)**
卵形のキャラクターが息を整える間、穏やかで遊び心のあるピチカートのフレーズが静かに流れ、起き上がっていくにつれて軽やかに音程が上がっていく小さなメロディへと変わり、まっすぐ立ち上がったところで温かく落ち着いた和音に着地する。

## ComfyUIでの設定メモ
- 最初のフレーム画像(たまちゃんが仰向けに転んでいる構図)を Picture 1、最後のフレーム画像
  (たまちゃんが起き上がって立っている構図)を Picture 2 として、FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 4秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
