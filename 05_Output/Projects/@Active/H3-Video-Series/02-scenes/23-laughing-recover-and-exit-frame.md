---
project: H3-Video-Series
scene: 23
mode: FL2VA
duration: 5s
---

# シーン23: 大笑いから起き上がり、目を合わせて次の楽しいことへ下手にフレームアウト

## シーン内容
シーン22の続き。倒れて体を震わせながら大笑いしていた2人が、少しずつ笑いを
落ち着けて起き上がる。起き上がったところで目を合わせ、「次の楽しいところへ
行こう!」というように嬉しそうな表情を交わし、2人並んで下手(画面左側)へ
楽しそうにフレームアウトしていく。最後は誰もいない雲の背景だけが残る。
カメラは完全固定。

## 最初と最後のフレーム(どちらも実画像を使用)
- Picture 1(最初のフレーム): 左でぽよんが横向きに倒れ、丸みを保ったまま傾いた姿勢で
  目を閉じて笑っている構図。右でたまちゃんも仰向けに転んで手足を上げ、
  楽しそうに笑っている構図
- Picture 2(最後のフレーム): 2人がいなくなった、パステルの雲と薄緑色の床だけの
  背景のみの構図

## H3プロンプト(ComfyUI用)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, beginning in the position established by Picture 1: the transparent, jelly-like rubber character lies tipped over on its side on the left, still perfectly round and never flattening, its eyes crinkled shut and its flat, outline-only mouth curved into a wide, uncolored laughing grin, while the egg-shaped character lies on its back on the right, its stiff little arms and legs raised in the air, its eyes crinkled shut and its mouth open wide with a hint of soft pink visible inside, both of them shaking gently with the last of their laughter against the pale green floor and soft pastel cloud shapes. The camera never pans, tilts, zooms, or cuts away at any point. Their laughter gradually settles into calm, happy breathing, and both characters begin to rouse themselves: the transparent character rocks itself upright again with a soft bounce, while the egg character plants its stiff arms against the floor and pushes itself back onto its feet in a simple, slightly wobbly motion. Once both are standing again, they turn and glance at each other, their round eyes bright and their outline mouths curving into wide, eager grins, as if silently agreeing that it's time to go find the next fun thing to do together. Still smiling at one another, the transparent character bounces playfully off toward the left edge of the frame first, with the egg character toddling eagerly right behind it in its stiff, heel-less waddle, both of them exiting the frame together past its left edge in high spirits, leaving behind only the empty pale green floor and soft pastel cloud shapes exactly as shown in Picture 2 at the end of the shot.

overall_soundscape: A few last trembling giggles fade out from both characters as they lie on the ground. Soft rustling and rocking sounds mark the transparent character bouncing itself upright and the egg character's muffled shuffling as it pushes itself back onto its feet. A quiet, happy little laugh passes between them as their eyes meet, followed by a light springy bounce from the transparent character and soft, quick toddling footsteps from the egg character as both hurry off toward the left, their bright giggles trailing off as they leave the frame.

non_diegetic_music: A soft, settling pizzicato phrase plays as the laughter fades and the characters get back up, brightening into a playful, skipping little melody as they glance at each other, then bouncing along cheerfully as the two hurry off together to their next adventure.
```

## 日本語訳(参考用)

**指示行**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の5.00秒地点に対応します。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、Picture 1で示された構図から始まる — 透明でゼリーのようなラバーキャラクターが左側で横向きに倒れたまま、完全に丸みを保って平らに潰れることなく、目をぎゅっと閉じ、平面的で輪郭線だけの口を大きく無着色の笑顔のカーブに曲げている。右側では卵形のキャラクターが仰向けに倒れ、硬い小さな手足を宙に上げ、目をぎゅっと閉じ、口を大きく開けてその内側にほんのりピンク色が覗いており、二人とも淡い緑の床とパステルの雲を背景に、笑いの余韻で体を小さく震わせている。カメラは一切パン・チルト・ズーム・カットをしない。二人の笑いは次第に落ち着き、穏やかで幸せそうな呼吸に変わっていき、やがて二人とも体を起こし始める — 透明なキャラクターは軽く弾みながら自分で起き上がり、卵形のキャラクターは硬い腕を床に突いて、少しふらつきながらも体を起こして足で立ち上がる。二人とも立ち上がると、互いに顔を向けて目を合わせ、丸い目を輝かせ、輪郭線の口を大きく期待に満ちた笑顔のカーブに広げる — まるで無言のうちに、次に一緒に楽しむことを探しに行こうと決めたかのように。互いに笑い合ったまま、透明なキャラクターがまず画面左端に向かって楽しそうに弾みながら進み、卵形のキャラクターも硬く踵のつかないよちよち歩きで、すぐ後ろから嬉しそうについていき、二人とも上機嫌のまま画面左端の外へ一緒にフレームアウトしていき、Picture 2で示された通り、淡い緑の床とパステルの雲だけが残る誰もいない構図でショットが終わる。

**環境音**
二人が地面に横たわったまま、震えるような最後の笑い声が数回聞こえて消えていく。透明なキャラクターが弾みながら起き上がる柔らかな衣擦れの音と、卵形のキャラクターが体を起こして足で立ち上がる、こもった衣擦れの音が続く。目が合う瞬間、静かで嬉しそうな小さな笑い声が交わされ、その後、透明なキャラクターの軽やかな弾む音と、卵形のキャラクターの素早く柔らかいよちよち歩きの足音が続き、二人が画面左端へ急いで向かう間、明るい笑い声が遠ざかりながらフレームアウトしていく。

**BGM(観客のみに聞こえる)**
笑いが落ち着いて二人が起き上がる間、穏やかに落ち着いていくピチカートのフレーズが流れ、二人が目を合わせる瞬間には軽やかで遊び心のある小さなメロディへと明るくなり、その後、二人が次の冒険へ一緒に楽しそうに急いで向かうにつれて、弾むように陽気なフレーズが続く。

## ComfyUIでの設定メモ
- 最初のフレーム画像(2人が倒れて大笑いしている構図)を Picture 1、最後のフレーム画像
  (2人がいなくなった雲の背景のみの構図)を Picture 2 として、FL2VA用の画像入力にそれぞれ接続
- モード: FL2VA
- 尺: 5秒(プロンプト内の秒数表記と要一致)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
