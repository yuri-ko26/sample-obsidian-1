---
project: H3-Video-Series
scene: title-card-v3
mode: L2VA
duration: 3s
---

# タイトルカード用パーツ:3キャラクターが下からポップに登場(テキストなし)

## シーン内容
真っ白な背景から、画面下から3体のクレイキャラクター(ひよこ・たまご・とら)が
ポップに飛び出して登場し、添付画像の並び順・ポーズにぴたっと着地する。
テキストや星の装飾は含まない、キャラクターのみのシンプルなポップアップ。

## 最初と最後のフレーム
- 最初(推測で生成): 何もない、真っ白な無地の背景
- Picture 1(最後のフレーム): 白背景に、左からひよこ(黄色・青いオーバーオール、
  笑って目を閉じている)、中央にたまご(白×ピンクの割れた殻、にっこり顔)、
  右にとら(黄色・黒縞・水色シャツ、口を開けて笑っている)が並んで立っている構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 3.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the shot begins on a plain, empty white background with soft, even studio lighting and nothing visible in frame. From the bottom edge of the frame, three clay mascot characters pop up together in one bouncy motion: on the left, a round yellow chick character with a small orange beak, tufted head feathers, and blue dungarees bounces up into frame with its eyes closed in a cheerful smile; in the center, a white-and-pink egg character with a cracked pink shell base bounces up alongside it, its simple round eyes and curved smile settling into place; and on the right, a yellow tiger-cub character with dark stripes, round ears, and a light blue shirt bounces up as well, its mouth open in a wide, happy grin. All three land side by side at the bottom of the frame with a soft, bouncy settle, coming to rest in the exact poses, spacing, and expressions established by <Picture 1> in the final frame.

overall_soundscape: A soft, bouncy pop sound marks the moment the three characters spring up into frame together, followed by light, playful giggles from all three as they settle into place.

non_diegetic_music: A short, upbeat marimba or xylophone flourish plays as the characters pop up, landing on a bright, cheerful final note as they settle.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — <Picture 1>(Shot 1より)は対象動画の3.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。ショットは、柔らかく均一なスタジオ照明の、何もない真っ白な背景から始まり、画面には何も映っていない。画面下端から、3体のクレイマスコットキャラクターが一つの弾むような動きで一緒にポップに飛び出してくる — 左側には、小さなオレンジ色のくちばし、頭のふさふさした羽、青いオーバーオールを身につけた丸い黄色のひよこキャラクターが、目を閉じた楽しそうな笑顔で弾みながら現れる。中央には、ピンク色の割れた殻の土台を持つ白とピンクのたまごキャラクターが一緒に弾んで現れ、シンプルな丸い目とカーブした笑顔が収まっていく。右側には、濃い縞模様・丸い耳・水色のシャツを身につけた黄色のとらの子キャラクターも同じく弾んで現れ、口を大きく開けた嬉しそうな笑顔を見せる。3体とも画面下に横並びで、柔らかく弾むように着地し、<Picture 1>で示された通りのポーズ・間隔・表情のまま、最終フレームに収まる。

**環境音**
3体のキャラクターが一緒に画面へ弾むように飛び出す瞬間、柔らかく弾むようなポンという音が鳴り、続いて3体が収まっていく間、それぞれから軽やかで楽しそうな笑い声が聞こえる。

**BGM(観客のみに聞こえる)**
短く明るいマリンバまたはシロフォンのフレーズが、キャラクターが飛び出す間に流れ、収まったところで明るく陽気な音で締めくくられる。

## ComfyUIでの設定メモ
- 最後のフレーム画像(添付の3キャラクターが並ぶ構図)を L2VA用の画像入力(Picture 1)に接続
- モード: L2VA(最初の状態はモデルが「真っ白な背景」という指示から推測して生成)
- 尺: 3秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
