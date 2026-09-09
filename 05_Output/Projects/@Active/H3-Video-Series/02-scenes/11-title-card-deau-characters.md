---
project: H3-Video-Series
scene: title-card-v2
mode: L2VA
duration: 5s
---

# タイトルカード(キャラクター入り版):「であう」

## シーン内容
真っ白な背景から、画面下から3体のクレイキャラクター(ひよこ・たまご・とら)が
ポップに飛び出して登場し、その後にタイトルテキスト「であう」と星の装飾が
楽しく弾みながら現れて、最終的に添付画像の構図に着地する。

## 最初と最後のフレーム
- 最初(推測で生成): 何もない、真っ白な無地の背景
- Picture 1(最後のフレーム): 白背景に、左からひよこ(黄色・青いオーバーオール)、
  中央にたまご(白×ピンク)、右にとら(黄色・黒縞・水色シャツ)が並んで立ち、
  その上に「で」(黄色)「あ」(水色)「う」(コーラルピンク)のクレイ文字と、
  白・水色・黄色・コーラルの星の装飾が散りばめられた完成構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, the shot begins on a plain, empty white background with soft, even studio lighting and no characters, text, or decorations visible. From the bottom edge of the frame, three clay mascot characters pop up together: on the left, a round yellow chick character with a small orange beak and blue dungarees bounces up into frame; in the center, a white-and-pink egg character with a cracked pink shell base bounces up alongside it; and on the right, a yellow tiger-cub character with dark stripes and a light blue shirt bounces up as well, all three landing side by side at the bottom of the frame with a soft, bouncy settle, their arms lightly raised as if greeting the viewer. A beat after the characters land, the title text begins to animate in above them: the clay letters "で", "あ", and "う" — in yellow, blue, and coral-pink respectively — bounce and tumble playfully into place from different directions, "で" dropping in from the upper left, "あ" rising up from below, and "う" swinging in from the upper right, each settling with a small squish. As the last letter settles, small decorative clay stars in pale yellow, powder blue, coral, and white pop into frame one by one around the text with a quick, bouncy scale-up, scattering playfully above and beside the letters. The scene settles into the exact character poses, text arrangement, and star placement established by <Picture 1> in the final frame.

overall_soundscape: A soft, bouncy pop sound marks the moment the three characters spring up into frame together, followed by playful giggles from all three. Each letter lands with a light squish sound as it settles into place, and each star appears with a quick, cheerful pop or chime.

non_diegetic_music: An upbeat, playful marimba or xylophone melody builds as the characters pop up, continuing through the bouncing letters and stars, and landing on a bright, cheerful final chord as the full title settles into place.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — <Picture 1>(Shot 1より)は対象動画の5.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。ショットは、柔らかく均一なスタジオ照明の、何もない真っ白な背景から始まり、キャラクター・テキスト・装飾のいずれも見えない状態である。画面下端から、3体のクレイマスコットキャラクターが一緒にポップに飛び出してくる — 左側には、小さなオレンジ色のくちばしと青いオーバーオールを身につけた丸い黄色のひよこキャラクターが弾みながら現れ、中央には、ピンク色の割れた殻の土台を持つ白とピンクのたまごキャラクターが一緒に弾んで現れ、右側には、濃い縞模様と水色のシャツを着た黄色のとらの子キャラクターも同じく弾んで現れる。3体とも画面下に横並びで、柔らかく弾むように着地し、まるで見ている人に挨拶するかのように腕を軽く上げる。キャラクターが着地した少し後、その上でタイトルテキストが動き始める — 黄色・水色・コーラルピンクのクレイ文字「で」「あ」「う」が、それぞれ違う方向から楽しげに弾みながら転がり込んでくる。「で」は左上から落ちてきて、「あ」は下から浮かび上がり、「う」は右上から振り子のように入ってきて、それぞれ小さく潰れながら着地する。最後の文字が収まると、淡い黄色・パウダーブルー・コーラル・白の小さな装飾用クレイの星が、文字の周りに1つずつ、何もない状態から一瞬で弾むように拡大しながらポップに現れ、文字の上や横に楽しげに散らばっていく。シーンは最後に、<Picture 1>で示されたキャラクターのポーズ・テキストの配置・星の配置とまったく同じ最終構図に落ち着く。

**環境音**
3体のキャラクターが一緒に画面へ弾むように飛び出す瞬間、柔らかく弾むようなポンという音が鳴り、続いて3体それぞれから楽しそうな笑い声が聞こえる。それぞれの文字が収まる際には軽い「むにゅっ」という着地音が鳴り、星が現れるたびに軽快で楽しいポンという音、あるいはチャイムのような音が鳴る。

**BGM(観客のみに聞こえる)**
明るく楽しいマリンバまたはシロフォンのメロディが、キャラクターが飛び出す場面から盛り上がり始め、文字や星が弾む間も続き、タイトル全体が収まったところで明るく陽気な最後の和音に着地する。

## ComfyUIでの設定メモ
- 最後のフレーム画像(添付の完成タイトル構図)を L2VA用の画像入力(Picture 1)に接続
- モード: L2VA(最初の状態はモデルが「真っ白な背景」という指示から推測して生成)
- 尺: 5秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
