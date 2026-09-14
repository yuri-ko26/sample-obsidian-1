---
project: H3-Video-Series-v2
cut: F-3
mode: FL2VA
status: draft
---

# カットF-3: たまちゃんがぽよんを追いかけて2人とも同じ方向にフレームアウトする(Fビートの退場カット)

## シーン内容
Fビート(「雲の稜線おいかけっこ」)の締め、退場カット。正面固定カメラ、雲の稜線を横から見た構図。

1. Picture1の状態(たまちゃん・ぽよんが並んで立ち、2人とも嬉しそうな表情)から始まる
2. ぽよんが先に右方向へ楽しそうに弾みながらフレームアウトする
3. 少し遅れて、たまちゃんも同じ右方向へぽよんを追いかけてフレームアウトする
4. 2人ともいなくなった後、Picture2で示された誰もいない雲の風景で終わる

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」

## 参照画像
- Picture 1(最初のフレーム): たまちゃんとぽよんが雲の上に並んで立ち、2人とも嬉しそうな表情(いただいた画像1)
- Picture 2(最後のフレーム): 誰もいないパステルカラーの雲の風景(いただいた画像2)

## プロンプト履歴

### v1 (2026-09-14)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the pastel cloud ridge exactly as shown in <Picture 1>, with both the egg-shaped character and the transparent, jelly-like rubber character standing together happily, matching their exact appearance, expression, and position from <Picture 1> at the very start. The camera never pans, tilts, zooms, or cuts away at any point. The egg character never has eyebrows at any point. After a brief happy moment together, the transparent character suddenly bounces off playfully to the right, its interior gumballs — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti — always settling naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall with each bounce, shifting with each bounce without ever spilling out. It bounces further and further to the right until it moves completely past the right edge of the frame and out of view. A brief beat later, the egg character reacts and immediately begins chasing after it in the very same direction, always walking up on the very tips of its toes, its heels never touching the ground, its short stiff legs never bending at the ankle, moving with real urgency — it, too, moves further and further to the right, following the exact same path the transparent character took, until it also moves completely past the right edge of the frame and out of view. Once both characters have fully exited the frame, the shot holds steady on the now-empty pastel cloud ridge for the remainder of the shot, with no characters visible anywhere in frame, exactly matching the empty landscape shown in <Picture 2>.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の5.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り雲の稜線を映しており、卵形のキャラクターと透明でゼリーのようなラバーキャラクターの両方が、最初は<Picture 1>とまったく同じ見た目・表情・位置で並んで嬉しそうに立っている。カメラは一切パン・チルト・ズーム・カットをしない。卵形のキャラクターにはどの瞬間も眉毛はつかない。少し嬉しそうな時間を過ごした後、透明なキャラクターが突然、楽しそうに右方向へ弾んで離れていく——中のガムボールは常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりくっついて見えたりすることは一切なく、弾むたびにお互いや内壁にぶつかってころころと転がる——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪は弾むたびに揺れ動くがこぼれることはない。透明なキャラクターはさらに右へ右へと弾んでいき、ついに画面右端を完全に越えて見えなくなる。少し遅れて、卵形のキャラクターが反応し、すぐさま同じ方向へ追いかけ始める——常につま先立ちのまま、踵は絶対に地面につかず、短く硬い脚は足首で曲がらず、本気の勢いで動く——卵形のキャラクターも、透明なキャラクターが通ったのとまったく同じ経路をたどって、さらに右へ右へと進んでいき、ついに画面右端を完全に越えて見えなくなる。2人とも完全にフレームアウトした後、ショットは誰もいなくなったパステルカラーの雲の稜線のまま残りの時間を保ち、画面のどこにもキャラクターは映っておらず、<Picture 2>で示された誰もいない風景とぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F3_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(たまちゃん・ぽよんが並んで嬉しそうに立つ)
- Picture 2: いただいた画像2(誰もいない雲の風景)
- モード: FL2VA
- 尺: 5秒目安(2人ともフレームアウトし、誰もいない状態で少し間を持たせるため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
