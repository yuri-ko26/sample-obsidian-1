---
project: H3-Video-Series
scene: 1
mode: I2VA
duration: 6s
---

# シーン1: ぶつかって笑う

## シーン内容
最初のフレーム(2人が並んで立っている画像)から、左のラバーフレンドが軽く跳ねて卵くんにあたり、
卵くんが転がって倒れ、二人が笑うシーン。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a wide static shot frames the scene shown in <Picture 1>: the transparent, jelly-like rubber character with its rounded, teardrop-shaped body stands on the left, colorful gumballs and confetti visibly suspended inside, and the pastel egg character with a white upper shell, pink lower shell, and short stubby limbs stands on the right, both resting on the pale green floor against soft pastel cloud shapes. The transparent character, having no arms or legs, springs upward with a light, springy hop, its rubbery body stretching and its interior gumballs and confetti shifting and drifting freely without ever spilling out. It bounces sideways and collides softly into the egg character's rounded body; at the point of contact its rubber surface presses inward into a smooth, curved dimple rather than flattening, staying round like a yo-yo, and none of the balls or confetti escape. The egg character, balanced on its short heel-less feet with stiff, non-bending ankles, tips backward from the impact and rolls a half turn along the ground before settling on its back with its little arms and legs raised. The transparent character bounces once more upright beside it, and both characters' simple outlined mouths curve open into wide grins while their round eyes crinkle into laughing crescents, the egg rocking gently side to side as it laughs.

overall_soundscape: A soft rubbery bounce and squeak sounds each time the transparent character springs off the ground, followed by the light clatter of gumballs shifting inside its body. A muffled, springy thud marks the collision, followed by the light tumbling sound of the egg character rolling across the floor. Both characters produce bright, breathy toddler-like giggles as the scene ends.

non_diegetic_music: A playful pizzicato string melody at a bright, bouncy tempo, with a light xylophone accent landing on the moment of impact and a cheerful upward flourish as the characters laugh.
```

## ComfyUIでの設定メモ
- 最初のフレーム画像を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 6秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
