---
project: H3-Video-Series-v2
cut: F-0
mode: FL2VA
status: draft
---

# カットF-0: 雲の稜線の背景に、たまちゃんとぽよんがフレームインしてくる(F-1の前の導入カット)

## シーン内容
Fビート(「雲の稜線おいかけっこ」)の直前に入る導入カット。最初は誰もいない雲の稜線の
背景から始まり、たまちゃんとぽよんが画面左からフレームインしてきて、F-1の開始位置
(たまちゃん左・ぽよん右、並んで立つ構図)に到着するところまで。正面固定カメラ。

**設計メモ**: 最初のフレームには誰も映っていないが、最後のフレームに2人の見た目が
はっきり映っているため、FL2VAとして両方を参照させることでモデルが2人の見た目を
anchoring できる(プロジェクトの標準手法)。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま歩く
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」

## 参照画像
- Picture 1(最初のフレーム): 誰もいない雲の稜線のみの構図
- Picture 2(最後のフレーム): 画面左にたまちゃん、右にぽよんが並んで立ち、
  どちらも通常の笑顔になっている構図(F-1のPicture1と同一)

## プロンプト履歴

### v1 (2026-09-10)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel cloud ridge exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. From the left edge of the frame, the egg-shaped character and the transparent, jelly-like rubber character enter together, the egg character toddling forward with small steps, its short stiff legs never bending at the ankle and its heels never touching the ground, while the transparent character bounces along beside it like a soft water balloon, its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. The egg character slows and comes to a stop first, settling into its standing position, while the transparent character continues a little further before also slowing to a stop just beside it. Both characters settle into a calm, happy standing pose side by side, matching the positions, framing, and appearance shown in <Picture 2> exactly at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り雲の稜線を映しており、最初は誰も映っていない。カメラは一切パン・チルト・ズーム・カットをしない。画面左端から、卵形のキャラクターと透明でゼリーのようなラバーキャラクターが一緒に入ってくる——卵形のキャラクターは短い歩幅でよちよちと進み、短く硬い脚は足首で曲がることも踵が地面につくこともなく、透明なキャラクターは水風船のようにそのそばを弾みながら進む。中の正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。卵形のキャラクターが先に速度を落として立ち止まり、その立ち位置に収まる一方、透明なキャラクターはもう少し先まで進んでから、そのすぐ横で同じく立ち止まる。2人とも穏やかで嬉しそうな立ち姿勢に並んで落ち着き、ショットの終わりには<Picture 2>で示された通りの位置・構図・見た目とぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F0_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: 今回いただいた誰もいない雲の稜線画像
- Picture 2: F-1のPicture1と同じ(たまちゃん左・ぽよん右)
- モード: FL2VA
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
