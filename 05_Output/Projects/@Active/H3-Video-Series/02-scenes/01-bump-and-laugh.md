---
project: H3-Video-Series
scene: 1
mode: I2VA
duration: 8s
---

# シーン1: オープニング(ぽよんのドアップ→たまちゃんに激突して笑う)

## シーン内容
シリーズの最初のシーン。ぽよん(透明のラバーキャラクター)の顔のドアップから始まる。
アップのまま軽くその場で2回バウンドし、2回目のバウンドから大きなジャンプに入る瞬間にカメラが引き始める。
ぽよんは振り向かず正面(カメラ側)を向いたまま後方へ大きくジャンプし、カメラもそれに合わせて引いていく。
たまちゃん(卵キャラクター)はカメラが引いた時点から後方に立っている姿が見えており、
ぽよんはそこから何度か連続でバウンドしながらたまちゃんに近づいていく。
近づいてくるぽよんに気づいて驚いた表情になる。ぽよんはたまちゃんにぶつかり、
たまちゃんは回転せずにその場でコテっと倒れて、二人で笑う。

## 最初のフレーム(Picture 1)
ぽよんの顔のドアップ画像(点目・輪郭線だけの口、中のガムボールと紙吹雪が背景として見える構図)。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, an extreme close-up shot frames the scene shown in <Picture 1>: the transparent, jelly-like rubber character's glossy skin fills the frame very close to the camera, its round dark eyes and flat, outline-only mouth with no depth and no colored interior surrounded by tightly packed colorful gumballs and drifting confetti shapes suspended inside its body. Still held in this tight close-up, the character bounces twice in place with small springy hops, its body compressing and rebounding each time while its interior gumballs and confetti shift gently, without yet revealing any more of the surrounding space. As it launches upward from the second hop into a much bigger jump, the camera begins to pull out with large amplitude at that same instant, widening the frame in sync with the jump to reveal an egg-shaped character, with a white upper shell, pink lower shell, short stubby limbs, and a similarly flat, depthless outlined mouth, already standing further back on the pale green floor against soft pastel cloud shapes. Facing directly toward the camera the entire time without turning around, the transparent character bounces several times in a row backward across the pale green floor, each hop carrying it further toward the egg character, its rubbery body compressing and rebounding with every landing while its interior gumballs and confetti drift and shift without ever spilling out. As it closes the last of the distance with a final hop, the egg character's round eyes widen and its flat outlined mouth opens into a small startled shape, still pure line work with no depth or colored interior, reacting to the approaching character just before the transparent character collides squarely into it. At the point of contact its rubber surface presses inward into a smooth, curved dimple rather than flattening, staying round like a yo-yo, and none of the balls or confetti escape. The egg character, balanced on its short heel-less feet with stiff, non-bending ankles, topples straight backward from the impact without rolling or spinning, falling flat onto its back in one simple motion, its little arms and legs flopping up as it lands. The transparent character bounces once more upright beside it, and both characters' flat, outline-only mouths settle into simple curved grin shapes, staying pure line work with no interior color and no depth, while their round eyes crinkle into laughing crescents, the egg character rocking gently side to side as it laughs.

overall_soundscape: A soft rubbery squeak echoes at extreme close range as the transparent character makes two small bounces in place, with the light clatter of gumballs shifting inside it each time. A bigger springy bounce sound marks its launch backward, followed by a steady series of softer bounce-and-squeak sounds as it hops repeatedly toward the egg character, then a soft startled gasp from the egg character just before a muffled, springy thud marks the impact, and a single soft plop as it falls flat onto its back. Both characters produce bright, breathy toddler-like giggles as the scene ends.

non_diegetic_music: A playful pizzicato string melody at a bright, bouncy tempo that builds through the leap, with a light xylophone accent landing on the moment of impact and a cheerful upward flourish as the characters laugh.
```

## 日本語訳(参考用)

**指示行**: 対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**: [Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>で示された構図をドアップで映す — 透明でゼリーのようなラバーキャラクターの光沢のある表面がカメラのすぐ近くで画面いっぱいに広がり、丸い黒目と、奥行きも中の色もない平面的な輪郭線だけの口が、体の中にぎっしり詰まったカラフルなガムボールと漂う紙吹雪に囲まれている。このドアップのまま、キャラクターはその場で軽く2回、小さくバウンドし、跳ねるたびに体が縮んで伸び、中のガムボールと紙吹雪もそっと揺れ動くが、まだ周囲の様子は見えない。2回目のバウンドから大きなジャンプへ入ると同時に、カメラは大きな振れ幅で引き始め、ジャンプに合わせて画角が広がり、白い上半分・ピンクの下半分の殻、短い手足、同じように奥行きのない輪郭線だけの口を持つ卵形のキャラクターが、淡いパステルの雲を背景にした薄緑色の床の上に、すでに奥に立っている姿が見えてくる。透明なキャラクターは終始カメラの方を向いたまま振り向かず、淡い緑の床の上を後方へ向かって連続で何度も弾みながら跳ね、跳ねるたびに卵形のキャラクターとの距離を縮めていき、着地するたびにゴム製の体は縮んでは伸び、中のガムボールと紙吹雪は揺れ動くが決してこぼれない。最後のひと跳ねで距離を詰めきると、卵形のキャラクターの丸い目が見開かれ、輪郭線だけの口が奥行きも色もないまま小さく驚いた形に開き、透明なキャラクターがまともにぶつかる直前の反応を見せる。接触の瞬間、ラバーの表面は平らに潰れるのではなく、ヨーヨーのように丸みを保ったまま内側へなめらかにくぼみ、中のボールや紙吹雪は一つもこぼれ出ない。卵形のキャラクターは、踵のない短い脚と曲がらない硬いくるぶしのままバランスを取っていたが、衝突の勢いで回転したり転がったりせず、まっすぐ後ろへコテっと一度で仰向けに倒れ、小さな手足がふわりと跳ね上がる。透明なキャラクターはその横でもう一度弾んで元の位置に戻り、二人とも輪郭線だけの平らな口が、内側の色も奥行きもないまま、シンプルな曲線の笑顔の形に落ち着き、丸い目は笑いじわのように細まり、卵形のキャラクターは笑いながら体を左右にゆっくり揺らす。

**環境音**: 透明なキャラクターがその場で2回小さくバウンドするたびに、ごく近い距離でやわらかいゴムのきしむ音が響き、その中でガムボールが軽くカタカタと動く音が混ざる。後方へ大きく飛び出す瞬間には、より大きな弾むような音が高まり、その後、卵形のキャラクターに向かって何度も跳ねながら近づく間、柔らかい弾む音ときしむ音が一定のリズムで続く。続いて卵形のキャラクターの小さな驚きの息づかいが聞こえ、その直後にこもった弾力のある衝突音が鳴り、最後に仰向けに倒れる際の小さく柔らかい「ぽすん」という音がする。シーンの終わりには、二人とも明るく息の弾んだ子どものような笑い声を上げる。

**BGM(観客のみに聞こえる)**: 明るく弾むテンポのピチカート弦楽器のメロディが、ジャンプの間に盛り上がっていき、衝突の瞬間には軽いシロフォンのアクセントが入り、二人が笑うところで陽気に音程が上がるフレーズで締めくくられる。

## ComfyUIでの設定メモ
- 最初のフレーム画像(ぽよんのドアップ)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 8秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
