---
project: H3-Video-Series-v2
cut: C-3
mode: FL2VA
status: superseded
---

# カットC-3: 笑いが落ち着き、次の楽しいことを予感して目を合わせ、フレームアウトする

> **2026-09-09時点でこのカットは廃止・分割済み**。走り出す動きで足首が曲がったり
> ぽよんの形が崩れたりする問題が発生したため、以下の2カットに分割した:
> - `C3a-tamachan-poyon-stand-up.md`(起き上がって静止するところまで)
> - `C3b-walk-off-frame.md`(静止した状態から、落ち着いて歩いてフレームアウト)
>
> このファイルは経緯の記録として残す。以降はC3a/C3bを使うこと。

## シーン内容
Cビート(「ぶつかって笑う」)の締めくくり。C-2d(v2)の最終フレームから始まり、
2人の笑いが落ち着いた後、顔を見合わせて「次も楽しいことしよう!」という表情になり、
一緒にフレームの外へ楽しそうに歩き去る。正面固定カメラ。旧アーカイブ
`02-scenes/23-laughing-recover-and-exit-frame.md` と同じ設計思想。

1. 大笑いしていた2人の笑いが少しずつ落ち着いていく
2. 顔を見合わせ、次も楽しいことをしよう!という、期待に満ちたいたずらっぽい表情になる
3. 2人並んで、楽しそうに画面の外へ歩いてフレームアウトする(方向はどちらでも良い
   とのことなので、右方向への退場として設計。左右反転すれば逆方向にも使える)
4. 画面には誰もいない床だけが残る

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない(点目と輪郭線の口のみ)
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。大きく開きすぎない
  (顔の横幅の3分の1程度まで)
- たまちゃんは踵をつけず、足首を曲げない棒状の足のまま歩く

## 参照画像
- Picture 1(最初のフレーム): C-2d(v2)の最終フレーム。画面左でぽよんが横倒しのまま
  控えめな笑顔で笑い、画面右でたまちゃんが前のめりに屈んだ姿勢で笑っている構図
- Picture 2(最後のフレーム): 無地の薄い黄緑色の床のみ(誰もいない構図)

## プロンプト履歴

### v1 (2026-09-09)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>, beginning with the transparent, jelly-like rubber character resting tilted on its side on the left and the egg-shaped character leaning forward on the right, both still laughing from before. The camera never pans, tilts, zooms, or cuts away at any point. Both characters keep their exact appearance and design from <Picture 1> unchanged while visible. Their laughter gradually settles, and the transparent character rights itself back to its normal round upright shape while the egg character straightens back up onto its feet, its heels never touching the ground. Once both are standing calm, they turn to look at each other, and their expressions shift into an eager, mischievous spark — already excited about finding the next fun thing to do together. Side by side, they toddle and bounce off happily toward the right edge of the frame, moving together at a playful, upbeat pace, until both have completely exited past the right edge with no part of either character remaining visible, leaving only the empty pale yellow-green floor exactly as shown in <Picture 2>, in the exact same static framing as the opening frame, at the end of the shot.

overall_soundscape: The characters' laughter softens into contented giggles, followed by light, bouncy footsteps as they toddle and hop off together toward the edge of frame, their happy chatter fading as they exit.

non_diegetic_music: A playful, upbeat marimba melody that picks up its pace as the two characters head off together, fading out warmly as they exit the frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映しており、画面左で透明でゼリーのようなラバーキャラクターが横倒しのまま、画面右で卵形のキャラクターが前のめりに屈んだ姿勢のまま、どちらもまだ笑っている状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。2人とも画面に映っている間は<Picture 1>の見た目・デザインのまま変化しない。2人の笑いは次第に落ち着いていき、透明なキャラクターは元の丸い直立した形に体を起こし、卵形のキャラクターも足で立ち上がる——踵は最後まで地面につかない。2人とも落ち着いて立ったところで、互いに顔を見合わせ、その表情は期待に満ちたいたずらっぽい輝きへと変わる——すでに次に一緒にする楽しいことを見つけようとわくわくしている様子である。並んで、2人は楽しそうによちよちと弾みながら画面右端へ向かい、楽しく軽快なペースで一緒に進んでいき、どちらの体もまったく見えなくなるまで完全に右端の外へ出ていき、<Picture 2>で示された通り、最初のフレームとまったく同じ固定構図のまま、誰もいない薄い黄緑色の床だけが残ったところでこのショットが終わる。

**環境音**
2人の笑い声が次第に落ち着いた含み笑いへと変わり、続いて2人が一緒によちよちと弾みながら画面端へ向かう軽やかな足音が響き、楽しそうな話し声が遠ざかりながら消えていく。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、2人が一緒に歩き去るにつれてペースを上げ、画面の外へ出ていくと温かくフェードアウトする。

**生成結果**
- 動画ファイル: `03-generated-videos/C3_v1.mp4`
- 判定: NG
- メモ: 笑いが落ち着いて真顔になる→また表情を作る、という表情の切り替えのタイミングで
  「知らない顔」(デザイン崩れ)になってしまう。→ v2で、笑顔を落ち着かせず、
  **笑顔のまま最後までフレームアウトする**構成に変更

### v2 (2026-09-09) — v1からの変更点: 「笑いが落ち着く→真顔→期待の表情→退場」の
表情切り替えをやめ、**最初から最後まで笑顔を保ったまま**退場する構成にした
(表情が切り替わる瞬間にデザインが崩れる問題を避けるため)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pale yellow-green floor and soft pastel cloud background exactly as shown in <Picture 1>, beginning with the transparent, jelly-like rubber character resting tilted on its side on the left and the egg-shaped character leaning forward on the right, both laughing exactly as shown. The camera never pans, tilts, zooms, or cuts away at any point. Both characters keep their exact appearance and design from <Picture 1> unchanged while visible, and both keep smiling and laughing throughout the entire shot — their happy, laughing expressions never settle into a neutral or calm face at any point. Still laughing, the transparent character rights itself back up to its normal round shape and the egg character rises back onto its feet, its heels never touching the ground, both of them still wearing the same delighted laughing expression the whole time. Without pausing to change their expression, they immediately toddle and bounce off together toward the right edge of the frame, still laughing and smiling the entire way, moving at a playful, upbeat pace, until both have completely exited past the right edge with no part of either character remaining visible, leaving only the empty pale yellow-green floor exactly as shown in <Picture 2>, in the exact same static framing as the opening frame, at the end of the shot.

overall_soundscape: The characters' happy laughter continues steadily throughout, mixed with light, bouncy footsteps as they toddle and hop off together toward the edge of frame, their laughter fading only as they exit.

non_diegetic_music: A playful, upbeat marimba melody that keeps its cheerful energy as the two characters head off together, fading out warmly as they exit the frame.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り薄い黄緑色の床とパステルの雲の背景を映しており、画面左で透明でゼリーのようなラバーキャラクターが横倒しのまま、画面右で卵形のキャラクターが前のめりに屈んだ姿勢のまま、<Picture 1>の通り2人とも笑っている状態から始まる。カメラは一切パン・チルト・ズーム・カットをしない。2人とも画面に映っている間は<Picture 1>の見た目・デザインのまま変化せず、**ショット全体を通してずっと笑顔・笑い続けたまま**である——嬉しそうな笑い顔が途中で真顔や落ち着いた表情に戻ることは一切ない。笑ったままの状態で、透明なキャラクターは元の丸い形に体を起こし、卵形のキャラクターも足で立ち上がる——踵は最後まで地面につかない——2人とも同じ嬉しそうな笑い顔をずっと保ったままである。表情を変えるための間を置かず、そのまま2人は一緒に、笑ったまま画面右端へ向かってよちよちと弾みながら進んでいき、最後までずっと笑顔・笑い続けたまま、楽しく軽快なペースで一緒に進み、どちらの体もまったく見えなくなるまで完全に右端の外へ出ていき、<Picture 2>で示された通り、最初のフレームとまったく同じ固定構図のまま、誰もいない薄い黄緑色の床だけが残ったところでこのショットが終わる。

**環境音**
2人の嬉しそうな笑い声がショットを通してずっと続き、2人が一緒によちよちと弾みながら画面端へ向かう軽やかな足音が混ざり、退場するにつれて笑い声だけが遠ざかりながら消えていく。

**BGM(観客のみに聞こえる)**
弾むようなテンポの陽気なマリンバのメロディが、2人が一緒に歩き去るあいだも明るいエネルギーを保ち、画面の外へ出ていくと温かくフェードアウトする。

**生成結果**
- 動画ファイル: `03-generated-videos/C3_v2.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: C-2d(v2)の実際の最終フレーム
- Picture 2: 無地の薄い黄緑色画像(床のみ、キャラクターなし)
- モード: FL2VA
- 尺: 6秒目安
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 左方向への退場にしたい場合は、プロンプト中の"right edge"を"left edge"に置き換えるだけでよい
