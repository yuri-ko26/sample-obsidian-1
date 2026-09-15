---
project: H3-Video-Series-v2
cut: E-3
mode: L2VA
status: draft
---

# カットE-3: 2人ともワクワクした気持ちで一緒に大きくジャンプ(俯瞰、カメラ寄り・頂点で着地)

> **このカットはエピソード1の最後のカットです。** ジャンプの頂点、2人がワクワクした
> 満面の笑顔でカメラいっぱいに寄った瞬間で映像が終わる想定。着地やその後の展開は
> 描かず、この幸せいっぱいの瞬間で締めくくる。

## シーン内容
Eビート(「ジャンプ」)3回目、最後のカット。E-2(たまちゃんがぽよんにくっついて
一緒にジャンプ)の続き。E-2ではぽよんが「たまちゃんがくっついてきたこと」に
驚いている様子だったが、このカットでは**ぽよんもたまちゃんと同じくらい
「一緒にジャンプしたい」という気持ちでいっぱいで、2人とも最初からワクワクした
表情で寄り添い、息を合わせて大きくジャンプする**。カメラは俯瞰の角度を保ったまま、
2人に向かってプッシュインしていき、ジャンプの頂点で画面いっぱいの寄った構図に
なる——このいただいた画像がその頂点の瞬間。

**設計メモ**: いただいた画像は1枚のみで、ジャンプの頂点・カメラが寄った瞬間の
最終フレームに相当するため、L2VA形式(最終フレームから逆算し、そこへ至る
自然な導入を組み立てる)を採用。E-2で確立した「俯瞰角度を保ったままのプッシュイン
ズーム」「たまちゃんはつま先立ちで移動」「セリフなし」「ガムボール収容」の各手法を
踏襲しつつ、**E-2との違い(一方的な驚きではなく、最初から2人とも同じ気持ちで
ワクワクしている)を明確に書き分けた**。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんの移動:踵をつけず、足首を曲げない棒状の足のまま
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、
  こぼれない・増えない・変わらない
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(6.00秒・最後のフレーム): いただいた画像。ジャンプの頂点、カメラが
  俯瞰のまま大きく寄った構図。左にぽよん(満面の笑顔)、右にたまちゃんが密着し、
  2人ともワクワクした嬉しそうな表情

## プロンプト履歴

### v1 (2026-09-15)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render. A single continuous shot keeps the exact same overhead, bird's-eye viewing angle throughout the entire video, looking straight down at all times and never tilting, panning, or switching to a side or angled view. The shot opens with the transparent, jelly-like rubber character and the egg-shaped character already standing upright close together on the pale yellow-green floor, having just landed from their previous jump, both already wearing bright, eager, excited expressions as they glance toward each other — this time, unlike before, the transparent character is not surprised or caught off guard; instead, it shares the exact same eager excitement as the egg-shaped character from the very start, both of them radiating a mutual, matching feeling of wanting to jump together. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout, expressing everything purely through body language and delighted facial expression. The egg-shaped character steps the last short distance toward the transparent character, walking up on the very tips of its toes only, its heels never touching the ground, its short stiff legs never bending at the ankle, and presses itself snugly against the transparent character's side; at the same moment, the transparent character leans warmly into the contact, both of them nestling closely together with matching, excited smiles. Once pressed together like this, both characters crouch down slightly at the same moment, gathering their energy together in perfect unison, their excitement visibly building in their expressions, and then launch upward together in one big joint jump, rising straight up side by side, still touching, as if leaping as a single unit, both faces lit up with pure, shared joy throughout the rise. As they rise, the camera keeps its overhead angle but pushes in steadily closer toward the pair, moving closer and closer with each moment. The transparent character's interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing, plus colorful confetti — shift and tumble inside with the motion of the jump, always staying fully contained inside its glossy transparent body, never spilling out. By the time they reach the peak of this big jump, the two of them together fill almost the entire frame, both wearing wide, delighted, joyful smiles, seen from directly overhead the whole time, exactly matching the tight, close-up framing, poses, and expressions shown in <Picture 1> at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — <Picture 1>(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。単一の連続したショットで、動画全体を通してまったく同じ俯瞰・鳥瞰の角度を保ち、常に真上から見下ろしたままで、傾いたり、パンしたり、横や斜めのアングルに切り替わったりすることは一切ない。ショットは、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが、前のジャンプからちょうど着地したところで、薄い黄緑色の床の上にすでに近くに並んで立っている状態から始まり、2人ともすでに明るく意欲的な、ワクワクした表情でお互いを見つめ合っている——今回は前回と違い、透明なキャラクターは驚いたり不意を突かれたりしていない。代わりに、最初から卵形のキャラクターとまったく同じ意欲的な興奮を共有しており、2人とも「一緒にジャンプしたい」という互いに一致した気持ちにあふれている。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のまま、すべてを体の動きと嬉しそうな表情だけで表現する。卵形のキャラクターは、常につま先の先端だけで立ち、踵は地面に一切つけず、短く硬い脚は足首でどの瞬間も曲がらないまま、透明なキャラクターの方へ最後の短い距離を歩み寄り、その体の横にぴたっと押し付ける。同じ瞬間、透明なキャラクターも温かくその接触に寄りかかり、2人とも一致した、興奮した笑顔でぴったりと寄り添う。このように密着したところで、2人は同じ瞬間にわずかにしゃがみ込み、完璧に息を合わせて力をため、その表情には興奮がはっきりと高まっていき、そして一緒に真上へ向かって一つの大きな共同ジャンプへと飛び立ち、触れ合ったまま横に並んでまっすぐ上昇していく——まるで一つの塊として跳んでいるかのようであり、上昇する間ずっと2人の顔には純粋な、共有された喜びが輝いている。2人が上昇するのに合わせて、カメラは俯瞰の角度を保ったまま、2人へ向かって一定のペースで着実に寄っていく。透明なキャラクターの中身——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらない)のガムボールとカラフルな紙吹雪——は、ジャンプの動きに合わせて揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、こぼれることは一切ない。この大きなジャンプの頂点に達する頃には、2人合わせてほぼフレーム全体を埋めるほど大きく、どちらも満面の、喜びにあふれた笑顔を浮かべ、終始真上から見た状態のまま、<Picture 1>で示された寄った・クローズアップのフレーミング・ポーズ・表情とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/E3_v1.mp4`(未生成)
- 判定: 未検証
- メモ: E-2との違い(一方的な驚きではなく、最初から2人ともワクワクした
  気持ちを共有している)を明記したL2VA版。参照画像1枚(ジャンプ頂点の
  クローズアップ)から逆算して導入部分を組み立てた

## ComfyUIでの設定メモ
- Picture 1: いただいた画像(ジャンプの頂点、カメラに寄った状態、2人ともワクワクした笑顔)
- モード: L2VA(最終フレームのみ、開始状態はプロンプト内で推論して記述)
- 尺: 6秒目安(E-2と同じ尺感)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- E-2の直後に続くカットという想定(E-2の着地状態から始まる)。もし独立したカット
  として使う場合や開始状態のイメージが違う場合は教えてください
- **このカットはエピソード1の最後のカットです。** ジャンプの頂点・満面の笑顔で
  カメラいっぱいになった瞬間で映像が終わる想定(着地やその後の展開なし)
