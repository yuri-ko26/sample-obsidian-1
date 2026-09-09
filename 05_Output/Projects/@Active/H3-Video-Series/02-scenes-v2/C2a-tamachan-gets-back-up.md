---
project: H3-Video-Series-v2
cut: C-2a
mode: FL2VA
status: draft
---

# カットC-2a: たまちゃんが倒れた姿勢から起き上がり、元の立ち姿に戻る

## シーン内容
元のC-2を2つに分割した前半部分。C-2生成時、起き上がる途中でたまちゃんの顔が
別デザインになってしまう問題があったため、**「起き上がり終わった状態」を実画像で
アンカーする**ことで解決する。正面固定カメラ。

C-1の実際の最終フレーム(たまちゃんが横向きに前のめりで倒れて笑っている)から、
たまちゃんが体を起こして元の立ち姿勢に戻り、2人とも落ち着いた通常の表情に戻る
ところまで。終了フレームには、C-1のPicture1として使った「理想画質」の2ショット
画像(ぽよん左・たまちゃん右、正しいデザインで並んで立つ構図)をそのまま使うことで、
顔の破綻を防ぐ。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんが起き上がる動き:踵をつけず、足首を曲げない棒状の足のまま、硬い腕で体を押し上げる
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)

## 参照画像
- Picture 1(最初のフレーム): C-1の実際の最終フレーム。画面左にぽよんが立ち笑い、
  画面右にたまちゃんが横向きに前のめりに倒れ込んだ姿勢で笑っている構図
- Picture 2(最後のフレーム): C-1のPicture1として使った「理想画質」の2ショット画像
  (薄い黄緑色の床+パステルの雲を背景に、左にぽよん、右にたまちゃんが並んで
  立つ構図、2人とも落ち着いた通常の表情)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point — its face is only round dot eyes and an outline-only mouth. The camera never pans, tilts, zooms, or cuts away at any point. On the left, the transparent, jelly-like rubber character's laughter gently settles as it stands still. On the right, the egg-shaped character, resting tipped forward onto its side with its head lowered, also settles from laughing, then braces its short, stiff, non-bending arms against the floor and pushes itself back upright, wobbling slightly as it rights itself and finds its balance, its feet never letting its heels touch the ground. It settles into its normal standing pose beside the transparent character, both of them now calm and still, their expressions returning to their normal resting look, matching the pose, framing, and appearance shown in <Picture 2> exactly at the end of the shot.

overall_soundscape: A soft rustle as the egg character braces its arms and pushes itself upright, followed by quiet, gentle footsteps as it wobbles back into a steady standing position.

non_diegetic_music: A gentle, settling musical phrase that quiets down as both characters return to their calm standing pose.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定正面ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。カメラは一切パン・チルト・ズーム・カットをしない。画面左側では、透明でゼリーのようなラバーキャラクターの笑いが静かに落ち着き、じっと立ったままになる。画面右側では、頭を下げ気味に横向きに前のめりで倒れていた卵形のキャラクターも笑いが落ち着き、短く硬い曲がらない腕を床について体を起こし、少しぐらつきながら体勢を立て直してバランスを取る——足は最後まで踵が地面につくことはない。透明なキャラクターの隣で通常の立ち姿勢に落ち着き、2人とも穏やかに静止した状態になり、表情も通常の落ち着いた様子に戻って、ショットの終わりには<Picture 2>で示された通りのポーズ・構図・見た目とぴったり一致する。

**環境音**
卵形のキャラクターが腕を床につき体を起こす柔らかな衣擦れの音、続いてぐらつきながら安定した立ち姿勢に戻るまでの静かな足音。

**BGM(観客のみに聞こえる)**
穏やかで落ち着いていく音楽のフレーズが、2人が静かな立ち姿に戻るにつれて静まっていく。

**生成結果**
- 動画ファイル: `03-generated-videos/C2a_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: C-1の実際の最終フレーム
- Picture 2: C-1のPicture1として使った「理想画質」2ショット画像(そのまま流用)
- モード: FL2VA
- 尺: 4秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
