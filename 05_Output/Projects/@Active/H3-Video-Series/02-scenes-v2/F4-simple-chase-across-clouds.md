---
project: H3-Video-Series-v2
cut: F-4
mode: I2VA
status: draft
---

# カットF-4: たまちゃんがぽよんを追いかける(シンプルな追いかけっこのみ)

## シーン内容
高さの異なる雲が並ぶ構図(いただいた新しい参照画像)を使った、シンプルな追いかけっこの
カット。驚かし・きょろきょろ・退場などの展開は入れず、**純粋に追いかけっこだけ**を描く。
正面固定カメラ。

1. Picture1の状態(たまちゃんが左手前の雲の上、ぽよんが少し奥・右寄りの高さの違う
   雲の上に、それぞれ嬉しそうな表情で立っている/座っている)から始まる
2. ぽよんが楽しそうに弾みながら、高さの違う雲を飛び移るようにして右奥へ逃げていく
3. たまちゃんは足元のでこぼこした雲の起伏を乗り越えながら、つま先立ちのまま
   本気で追いかける
4. 表情はどちらも最初から最後まで変えず、ただ追いかけっこが続く(オチや驚きは付けない)

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)

## 参照画像
- Picture 1(最初のフレーム): たまちゃんが左手前の水色の雲の上、ぽよんが右奥・少し
  高い位置の雲の上にいる構図(いただいた新しい参照画像)。2人とも嬉しそうな表情

## プロンプト履歴

### v1 (2026-09-14)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single static shot, fixed in place for the entire video with no panning, tilting, zooming, or cutting, shows the pastel clouds of varying heights exactly as shown in <Picture 1>. Both characters keep their exact appearance and design from <Picture 1> unchanged throughout, with no distortion. The egg character never has eyebrows at any point. Neither character's facial expression changes at any point in this shot — both keep the same happy expression shown in <Picture 1> from the first frame to the last, with no transitions, no surprises, and no other story beats: this is purely a simple chase. From their starting positions, the transparent, jelly-like rubber character begins bouncing away playfully, hopping from cloud to cloud across the uneven, varying-height cloud terrain, while the egg-shaped character chases right after it, clambering up and over each bump and cloud edge in its path, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point, moving with real, determined urgency the whole time. The egg character's short legs are just a touch slower than the transparent character's bounces, so a small gap stays between them throughout, but the egg character keeps closing distance with every stride it can manage, never coming to a stop, slowing to a halt, or standing still at any point — it keeps actively chasing continuously for the entire shot. The transparent character's interior gumballs always settle naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shifting with each bounce without ever spilling out. Both characters continue this energetic chase across the cloud terrain for the entire duration of the shot, hopping and clambering from cloud to cloud, neither one ever stopping or settling down.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通して一切動かない単一の固定ショットで、<Picture 1>で示された通り、高さの異なるパステルカラーの雲を映している。2人とも<Picture 1>の見た目・デザインのまま、崩れたり変化したりすることなく保たれる。卵形のキャラクターにはどの瞬間も眉毛はつかない。このショットの間、どちらのキャラクターの表情も一切変化しない——2人とも<Picture 1>と同じ嬉しそうな表情を最初から最後まで保ち、表情の切り替えも、驚きの展開も、その他のストーリー要素も一切入らない。これは純粋にシンプルな追いかけっこである。最初の位置から、透明でゼリーのようなラバーキャラクターが楽しそうに弾み始め、高さの異なるでこぼこした雲の地形を飛び移りながら進んでいく。一方、卵形のキャラクターはそのすぐ後ろを追いかけ、行く手にある一つ一つの盛り上がりや雲の縁をよじ登って越えていく——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらず、本気の勢いで、終始必死に追いかける。卵形のキャラクターの短い脚は、弾んで進む透明なキャラクターにほんの少しだけ及ばないため、2人の間には小さな距離がずっと残るが、卵形のキャラクターはできる限りその差を詰めようとし続け、途中で止まったり立ち止まったりすることは一切ない——ショットの間ずっと積極的に追いかけ続ける。透明なキャラクターの中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。2人ともこのショットの間ずっと、雲の地形を飛び移り・よじ登りながらこの元気な追いかけっこを続け、どちらも一切止まったり落ち着いたりしない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F4_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた新しい参照画像(高さの異なる雲、たまちゃん手前・ぽよん奥)
- モード: I2VA(最後のフレーム画像は不要)
- 尺: 6秒目安(オチをつけない、シンプルな追いかけっこのみ)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: 表情は一切変えない・驚きやオチを入れない・つま先立ちを徹底、の3点を明記
