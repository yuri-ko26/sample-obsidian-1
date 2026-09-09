---
project: H3-Video-Series-v2
cut: C-3a
mode: FL2VA
status: draft
---

# カットC-3a: 転がって笑っていた2人が起き上がり、静かに立ち止まる

## シーン内容
元のC-3を2つに分割した前半部分。走り出す動きを含めると足首が曲がったり
ぽよんの形が崩れたりする問題があったため、**「起き上がって静止する」までを
1カットとして独立させ、実画像でラストフレームをアンカーする**。正面固定カメラ。

C-2d(v2)の最終フレーム(ぽよんが横倒し、たまちゃんが前のめりに笑っている)から、
2人とも起き上がって、C-1・C-2a/bで使っている「理想画質」の落ち着いた立ち姿に
戻るところまで。ここでは**歩き出さない・走らない**——静止するところで終わる。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんが起き上がる動き:踵をつけず、足首を曲げない棒状の足のまま
- ぽよんが起き上がる際、体は常に丸み(しずく型)を保つ

## 参照画像
- Picture 1(最初のフレーム): C-2d(v2)の実際の最終フレーム(ぽよんが横倒しのまま
  控えめな笑顔、たまちゃんが前のめりに屈んだ姿勢で笑っている構図)
- Picture 2(最後のフレーム): 「理想画質」の2ショット画像(薄い黄緑色の床+
  パステルの雲を背景に、左にぽよん、右にたまちゃんが並んで立つ構図。C-1・C-2a/bと共通)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>, beginning with the transparent, jelly-like rubber character resting tilted on its side on the left and the egg-shaped character leaning forward on the right, both laughing exactly as shown. The camera never pans, tilts, zooms, or cuts away at any point. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. Their laughter gently settles as the transparent character rights itself back up to its normal round shape, staying perfectly smooth and round throughout the motion with no distortion at any point, and the egg character braces its short, stiff, non-bending arms and pushes itself back upright, wobbling slightly as it finds its balance, its feet never letting its heels touch the ground and its legs never bending at the ankle. Both settle into their calm, normal standing pose side by side, coming to a complete stop and staying still, their expressions returning to their usual resting look, matching the pose, framing, and appearance shown in <Picture 2> exactly at the end of the shot.

overall_soundscape: The characters' laughter softens into quiet, contented giggles, followed by a soft rustle as the egg character braces its arms and pushes itself upright, and a gentle settling sound as the transparent character rounds itself back into shape.

non_diegetic_music: A gentle, settling musical phrase that quiets down as both characters come to a calm, still stop.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映しており、画面左で透明でゼリーのようなラバーキャラクターが横倒しのまま、画面右で卵形のキャラクターが前のめりに屈んだ姿勢のまま、<Picture 1>の通り2人とも笑っている状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。2人の笑いはやさしく落ち着いていき、透明なキャラクターは元の丸い形に体を起こす——その動きの間もずっと完全に滑らかで丸い形を保ち、一切歪まない。卵形のキャラクターは短く硬い曲がらない腕を床について体を起こし、少しぐらつきながらバランスを取る——足は最後まで踵が地面につかず、足首が曲がることも一切ない。2人とも並んで、落ち着いた通常の立ち姿勢に収まり、完全に止まってじっと静止し、表情も通常の落ち着いた様子に戻って、ショットの終わりには<Picture 2>で示された通りのポーズ・構図・見た目とぴったり一致する。

**環境音**
2人の笑い声がやさしく落ち着いた含み笑いへと変わり、続いて卵形のキャラクターが腕をついて体を起こす柔らかな衣擦れの音、透明なキャラクターが丸い形に戻るやさしい音が響く。

**BGM(観客のみに聞こえる)**
穏やかで落ち着いていく音楽のフレーズが、2人が静かに止まるにつれて静まっていく。

**生成結果**
- 動画ファイル: `03-generated-videos/C3a_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: C-2d(v2)の実際の最終フレーム
- Picture 2: 「理想画質」2ショット画像(C-1・C-2a/bと共通)
- モード: FL2VA
- 尺: 4秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
