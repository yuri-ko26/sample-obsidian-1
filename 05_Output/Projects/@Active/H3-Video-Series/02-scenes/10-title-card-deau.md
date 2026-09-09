---
project: H3-Video-Series
scene: title-card
mode: FL2VA
duration: 4s
---

# タイトルカード:「であう」

## シーン内容
グリーンバック(クロマキー合成用)の上に、クレイアニメ調の文字「で・あ・う」が
左から順に上からポンっと弾んで着地し、その周りに星のパーツがポップに現れて
タイトルロゴが完成する。カメラは固定(合成用に動かさない)。

## 最初と最後のフレーム
- Picture 1: 何もない、無地のグリーンバック(スタジオ照明の柔らかいグラデーションのみ)
- Picture 2: 「で」(黄色・爪のような黒いマーク付き)「あ」(水色)「う」(コーラルピンク)の
  クレイ文字が横一列に並び、周囲に白・水色・黄色・コーラルの星(塗りつぶし/輪郭のみ)が
  散りばめられた完成形

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style title card animation begins in the position and framing established by Picture 1: a plain, empty solid green screen with soft studio lighting and a subtle gradient, no elements visible. The camera holds a completely static shot throughout, never panning, tilting, or zooming, keeping the frame clean for chroma-key compositing. The first clay letter, "で", in bright yellow clay with three small dark claw-like marks, bounces down into frame from above on the left side and lands with a soft squish before settling upright. A beat later, the second letter, "あ", in sky-blue clay, bounces in from above at the center and lands beside the first letter with the same soft squish. Then the third letter, "う", in coral-pink clay, bounces in from above on the right, completing the word "であう" in a left-to-right row. As the last letter settles, small clay stars in pale yellow, powder blue, coral, and white — some solid, some hollow outlines — pop into frame one by one around the letters, each appearing with a quick, bouncy scale-up from nothing to full size, scattering playfully above, beside, and below the row of letters. The scene settles into the exact arrangement, spacing, and composition established by Picture 2 at the end of the shot.

overall_soundscape: A soft, squishy clay-landing sound plays as each letter bounces into place, followed by a quick, light pop or chime sound as each star appears around the letters.

non_diegetic_music: A short, playful marimba or xylophone flourish, with each note landing in sync with a letter or star appearing, building to a cheerful final chord as the full title settles into place.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調タイトルカードアニメーション。Picture 1で示された構図から始まる — 無地の緑色スクリーンに、柔らかいスタジオ照明のわずかなグラデーションのみがあり、要素は何もない。カメラは終始完全に固定され、パン・チルト・ズームは一切行わず、クロマキー合成のためにフレームをきれいなまま保つ。最初のクレイ文字「で」は、黒い爪のような小さなマークが3つ付いた明るい黄色のクレイでできており、画面左側の上から弾みながら降りてきて、柔らかく着地して直立して落ち着く。少し遅れて、2番目の文字「あ」が水色のクレイで、画面中央の上から弾みながら現れ、同じように柔らかく着地して最初の文字の隣に収まる。続いて3番目の文字「う」がコーラルピンクのクレイで画面右側の上から弾みながら現れ、左から右に並んだ「であう」という単語が完成する。最後の文字が落ち着くと、淡い黄色・パウダーブルー・コーラル・白のクレイの星(塗りつぶしのものと輪郭線だけのものが混在)が、文字の周りに1つずつポップに現れ、それぞれ何もない状態から一瞬で弾むように full size まで拡大し、文字の列の上・横・下に楽しげに散らばっていく。シーンは最後に、Picture 2で示された配置・間隔・構図とまったく同じ状態に落ち着く。

**環境音**
それぞれの文字が弾んで着地するたびに、柔らかく「むにゅっ」としたクレイの着地音が鳴り、続いて星が文字の周りに現れるたびに、軽快で短い「ポン」というチャイムのような音が鳴る。

**BGM(観客のみに聞こえる)**
短く遊び心のあるマリンバまたはシロフォンのフレーズが、文字や星が現れるタイミングに合わせて1音ずつ鳴り、タイトル全体が収まったところで陽気な和音で締めくくられる。

## ComfyUIでの設定メモ
- 最初のフレーム画像(無地の緑背景)と最後のフレーム画像(完成したタイトルロゴ)を、それぞれ
  FL2VA用の画像入力(Picture 1 / Picture 2)に接続
- モード: FL2VA
- 尺: 4秒(プロンプト内の秒数表記と要一致)
- カメラは完全固定(クロマキー合成前提のため)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
