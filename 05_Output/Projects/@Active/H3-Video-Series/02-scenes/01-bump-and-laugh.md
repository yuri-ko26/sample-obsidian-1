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
近づいてくるぽよんに気づいて驚いた表情になる。ぽよんはたまちゃんにぶつかり、
たまちゃんは回転せずにその場でコテっと倒れて、二人で笑う。

## 最初のフレーム(Picture 1)
ぽよんの顔のドアップ画像(点目・輪郭線だけの口、中のガムボールと紙吹雪が背景として見える構図)。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, an extreme close-up shot frames the scene shown in <Picture 1>: the transparent, jelly-like rubber character's glossy skin fills the frame very close to the camera, its round dark eyes and flat, outline-only mouth with no depth and no colored interior surrounded by tightly packed colorful gumballs and drifting confetti shapes suspended inside its body. Still held in this tight close-up, the character bounces twice in place with small springy hops, its body compressing and rebounding each time while its interior gumballs and confetti shift gently, without yet revealing any more of the surrounding space. As it launches upward from the second hop into a much bigger jump, the camera begins to pull out with large amplitude at that same instant, widening the frame in sync with the jump to reveal an egg-shaped character, with a white upper shell, pink lower shell, short stubby limbs, and a similarly flat, depthless outlined mouth, already standing further back on the pale green floor against soft pastel cloud shapes. Facing directly toward the camera the entire time without turning around, the transparent character sails straight backward through the air toward the egg character, its rubbery body stretching mid-flight while its interior gumballs and confetti drift and shift without ever spilling out. As it closes the distance, the egg character's round eyes widen and its flat outlined mouth opens into a small startled shape, still pure line work with no depth or colored interior, reacting to the approaching character just before the transparent character collides squarely into it. At the point of contact its rubber surface presses inward into a smooth, curved dimple rather than flattening, staying round like a yo-yo, and none of the balls or confetti escape. The egg character, balanced on its short heel-less feet with stiff, non-bending ankles, topples straight backward from the impact without rolling or spinning, falling flat onto its back in one simple motion, its little arms and legs flopping up as it lands. The transparent character bounces once more upright beside it, and both characters' flat, outline-only mouths settle into simple curved grin shapes, staying pure line work with no interior color and no depth, while their round eyes crinkle into laughing crescents, the egg character rocking gently side to side as it laughs.

overall_soundscape: A soft rubbery squeak echoes at extreme close range as the transparent character makes two small bounces in place, with the light clatter of gumballs shifting inside it each time. A bigger springy bounce sound builds as it launches backward through the air, followed by a soft startled gasp from the egg character just before a muffled, springy thud marks the impact, and a single soft plop as it falls flat onto its back. Both characters produce bright, breathy toddler-like giggles as the scene ends.

non_diegetic_music: A playful pizzicato string melody at a bright, bouncy tempo that builds through the leap, with a light xylophone accent landing on the moment of impact and a cheerful upward flourish as the characters laugh.
```

## ComfyUIでの設定メモ
- 最初のフレーム画像(ぽよんのドアップ)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 8秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
