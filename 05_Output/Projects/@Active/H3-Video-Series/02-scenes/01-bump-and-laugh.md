---
project: H3-Video-Series
scene: 1
mode: I2VA
duration: 8s
---

# シーン1: オープニング(ぽよんのドアップ→たまちゃんに激突して笑う)

## シーン内容
シリーズの最初のシーン。ぽよん(透明のラバーキャラクター)の顔のドアップから始まり、
カメラが引いて全身が見えてくる。ぽよんはカメラのすぐ前(ステージ手前)におり、
たまちゃん(卵キャラクター)はステージのだいぶ奥に立っている。
ぽよんは振り向かず正面(カメラ側)を向いたまま後方へジャンプし、カメラもそれに合わせて引いていく。
奥のたまちゃんにぶつかり、たまちゃんは止まらずに勢いで転がり続けて笑う。

## 最初のフレーム(Picture 1)
ぽよんの顔のドアップ画像(点目・輪郭線だけの口、中のガムボールと紙吹雪が背景として見える構図)。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, an extreme close-up shot frames the scene shown in <Picture 1>: the transparent, jelly-like rubber character's glossy skin fills the frame very close to the camera, its round dark eyes and flat, outline-only mouth with no depth and no colored interior surrounded by tightly packed colorful gumballs and drifting confetti shapes suspended inside its body. The camera pulls out with large amplitude, revealing that the character is standing much closer to the camera than the rest of the stage, its full teardrop-shaped body, having no arms or legs, positioned on the pale green floor against soft pastel cloud shapes, while a second character, an egg-shaped figure with a white upper shell, pink lower shell, short stubby limbs, and a similarly flat, depthless outlined mouth, stands far back on the stage, much deeper in the frame. Facing directly toward the camera the entire time without turning around, the transparent character springs upward with a light, springy hop and leaps straight backward away from the camera, its rubbery body stretching mid-flight while its interior gumballs and confetti drift and shift without ever spilling out; the camera continues to pull out in sync, tracking its retreat deeper into the scene until it lands directly into the egg character's rounded body far upstage. At the point of contact its rubber surface presses inward into a smooth, curved dimple rather than flattening, staying round like a yo-yo, and none of the balls or confetti escape. The egg character, balanced on its short heel-less feet with stiff, non-bending ankles, does not simply tip and stop but tumbles from the force of the impact, rolling continuously across the ground for several full rotations as the momentum carries it further, its little arms and legs swinging loosely with each turn, before it gradually loses speed and comes to rest on its back with its arms and legs raised. The transparent character bounces once more upright beside it, and both characters' flat, outline-only mouths widen into simple curved grin shapes, staying pure line work with no interior color and no depth, while their round eyes crinkle into laughing crescents, the egg character rocking gently side to side as it laughs.

overall_soundscape: A soft rubbery squeak echoes at extreme close range as the transparent character's body shifts, with the light clatter of gumballs settling inside it. A springy bounce sound builds as it leaps backward through the air, followed by a muffled, springy thud on impact, and the egg character's momentum carries it into a continuous tumbling roll across the floor, producing a rhythmic series of soft thuds as it turns over again and again before slowing to a stop. Both characters produce bright, breathy toddler-like giggles as the scene ends.

non_diegetic_music: A playful pizzicato string melody at a bright, bouncy tempo that builds through the leap, with a light xylophone accent landing on the moment of impact and a cheerful upward flourish as the characters laugh.
```

## ComfyUIでの設定メモ
- 最初のフレーム画像(ぽよんのドアップ)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 8秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
