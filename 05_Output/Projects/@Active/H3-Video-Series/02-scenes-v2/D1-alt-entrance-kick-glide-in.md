---
project: H3-Video-Series-v2
cut: D-1-alt-entrance
mode: FL2VA
status: draft
---

# カットD-1-alt-entrance: 誰もいない床から2人が蹴伸びパターンでフレームインする(D-1-altの直前の導入カット)

## シーン内容
D-1-alt(蹴伸び・キック&グライド版)の直前に入る導入カット。誰もいない薄い黄緑色の
床から始まり、たまちゃんは体の向きを変えずに蹴伸びのキック&グライドで、ぽよんは
平らな円盤のようにその場でくるくる回転しながら横滑りし、2人が**画面右端**から
一緒にフレームインして左方向へ進み、画面左寄りの位置(Picture2)で止まるところまで。
入ってきた右側には広い余白が残る。俯瞰固定カメラ。

**設計メモ**: D1-alt v2で確立した、ぽよんが「平らな円盤のようにその場で回転しながら
横滑りする」回転方式(D-1・D-2・D-2cで使う「端から端まで転がる軸固定回転」とは
別物)と、「顔は体表面の固定パーツとして体の回転と一体で動く」手法をそのまま踏襲。
たまちゃんの蹴伸び(キック&グライド)移動もD-1-altと同じ描写を使用。
セリフ・発話は一切なしと明記(D-1系の標準ルール)。

**v3での変更点**: 「みぎひだりはんたいでした」のご指摘を受け、v2で画面右端からに
変更した方向を画面左端からへ差し戻し、あわせて新しくいただいた画像2に合わせ、
Picture2の構図をたまちゃんが左・ぽよんがその右という並びに更新。

**v4での変更点**: 「左から右に変えてください」のご指摘を受けて確認したところ、
正しくは「フレームインする方向を右→左に戻す」ことだと判明。**入ってくる辺を
画面右端に戻し**、右から左へ進んで、Picture2の位置(画面左寄り)で止まる構成に
修正。到着位置・並び(たまちゃん左・ぽよん右)はv3のPicture2のまま変更なし。
たまちゃんが体の向きを変えずキックだけで進む点(v2で追加)もそのまま維持。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない
- たまちゃんは蹴伸びの間、足首を曲げず、踵を地面につけない棒状の足のまま蹴る
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」、こぼれない
- 顔(目・口)は体の表面に属する固定パーツであり、体の回転と一体で動く
- セリフ・発話・音声は一切なし

## 参照画像
- Picture 1(最初のフレーム): いただいた画像1。誰もいない、無地の薄い黄緑色の床のみ
- Picture 2(最後のフレーム): いただいた画像2。画面左寄りに、左側にたまちゃん、
  その右にぽよんが回転している最中の姿勢で並んでいる構図。右側(入ってきた側)に
  広い余白が残る

## プロンプト履歴

### v4 (2026-09-15) — 現在の採用版(フレームインを右端からに戻し、左寄りで停止)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout. From the right edge of the frame, the egg-shaped character and the transparent, jelly-like rubber character move into view together, traveling leftward, each moving in its own distinct way. The egg-shaped character does not spin, tumble, or turn its body to face its direction of travel at all — its facing direction and body orientation stay exactly the same as its pose in <Picture 2>, fixed and unchanging, the entire time. Instead, while keeping that same fixed orientation, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth sideways glide leftward across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater, without ever turning to face the direction it is gliding toward. After each glide slows, it plants its legs again for another quick kick-off in the same fixed orientation, sending it gliding leftward once more, repeating this kick-and-glide rhythm the whole way in. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Beside it, the transparent character moves completely differently: it spins steadily in place like a flat disc turning on the floor while gliding leftward at the same time, moving further onto the floor with each moment. Critically, its face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it, exactly like the rest of its glossy skin. As the body spins, the face spins together with it as one single rigid piece: the face turns away and becomes hidden from view as that side of the body rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face the camera — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift and tumble inside with each spin, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. Both characters move into frame together this way, entering steadily from the right edge and traveling leftward, gradually advancing further onto the floor and becoming more visible with each moment, until they reach the positions and poses shown in <Picture 2>, coming to a natural, gentle stop there near the left portion of the frame, with open floor stretching out to their right — the side they entered from — matching <Picture 2> exactly, including the egg-shaped character's fixed facing direction and the transparent character's spinning pose with its face visible from its current rotated angle, at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り誰もいない薄い黄緑色の床を真上から見下ろしており、開始時点ではキャラクターは一人も映っていない。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。**画面右端から**、卵形のキャラクターと透明でゼリーのようなラバーキャラクターが一緒に、**左方向へ進みながら**フレームインしてくる——それぞれがまったく異なる動き方をする。卵形のキャラクターは、回転したり転がったり、進行方向へ体ごと向き直ったりすることは一切ない——その向いている方向・体の向きは<Picture 2>でのポーズとまったく同じまま、終始固定され変わらない。その代わりに、その同じ固定された向きを保ったまま、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を床の上で**左方向へ**スーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じであり、滑っていく方向へ向き直ることは一切ない。その滑りが緩やかになるたびに、同じ固定された向きのまま再び脚をついてもう一度素早く蹴り出し、また左へ滑っていく、というキック&グライドのリズムをフレームインしている間ずっと繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。その隣では、透明なキャラクターがまったく異なる動き方をする——床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に**左方向へ**滑るように移動し、時間が経つにつれて床の上をさらに進んでいく。極めて重要な点として、その顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、光沢のある体の他の部分とまったく同じように、体の一箇所に恒久的に付着している。体が回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分の体がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周してカメラの方を向いたときにだけ再び顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色や余分なガムボールは一切現れない)——とカラフルな紙吹雪は、回転するたびに揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。2人はこのようにして一緒にフレームインし、**画面右端から左方向へ進みながら**、時間が経つにつれて床の上でその姿がだんだんはっきりと見えるようになっていき、<Picture 2>に示された位置・姿勢に到達したところで、画面左寄りで自然に穏やかに止まり、**入ってきた側である右側**には広い床の余白が残る——卵形のキャラクターの固定された向き、透明なキャラクターが現在の回転角度で顔が見えているポーズも含めて、<Picture 2>とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt-entrance_v4.mp4`(未生成)
- 判定: 未検証
- メモ: フレームインする辺を右端に戻し(移動方向は右→左)、到着位置はv3の
  Picture2(左寄り)のまま変更なしの版

### v3 (2026-09-15) — 旧版(左からフレームイン、後に右からが正しいと判明)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout. From the left edge of the frame, the egg-shaped character and the transparent, jelly-like rubber character move into view together, each moving in its own distinct way. The egg-shaped character does not spin, tumble, or turn its body to face its direction of travel at all — its facing direction and body orientation stay exactly the same as its pose in <Picture 2>, fixed and unchanging, the entire time. Instead, while keeping that same fixed orientation, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth sideways glide across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater, without ever turning to face the direction it is gliding toward. After each glide slows, it plants its legs again for another quick kick-off in the same fixed orientation, sending it gliding sideways once more, repeating this kick-and-glide rhythm the whole way in. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Beside it, the transparent character moves completely differently: it spins steadily in place like a flat disc turning on the floor while gliding sideways at the same time, moving further onto the floor with each moment. Critically, its face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it, exactly like the rest of its glossy skin. As the body spins, the face spins together with it as one single rigid piece: the face turns away and becomes hidden from view as that side of the body rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face the camera — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift and tumble inside with each spin, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. Both characters move into frame together this way, entering steadily from the left edge, gradually advancing further onto the floor and becoming more visible with each moment, until they reach the positions and poses shown in <Picture 2>, coming to a natural, gentle stop there near the left portion of the frame, with open floor stretching out to their right, matching <Picture 2> exactly — including the egg-shaped character's fixed facing direction and the transparent character's spinning pose with its face visible from its current rotated angle — at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り誰もいない薄い黄緑色の床を真上から見下ろしており、開始時点ではキャラクターは一人も映っていない。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。**画面左端から**、卵形のキャラクターと透明でゼリーのようなラバーキャラクターが一緒にフレームインしてくる——それぞれがまったく異なる動き方をする。卵形のキャラクターは、回転したり転がったり、進行方向へ体ごと向き直ったりすることは一切ない——その向いている方向・体の向きは<Picture 2>でのポーズとまったく同じまま、終始固定され変わらない。その代わりに、その同じ固定された向きを保ったまま、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を床の上で横方向へスーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じであり、滑っていく方向へ向き直ることは一切ない。その滑りが緩やかになるたびに、同じ固定された向きのまま再び脚をついてもう一度素早く蹴り出し、また横へ滑っていく、というキック&グライドのリズムをフレームインしている間ずっと繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。その隣では、透明なキャラクターがまったく異なる動き方をする——床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に横方向へ滑るように移動し、時間が経つにつれて床の上をさらに進んでいく。極めて重要な点として、その顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、光沢のある体の他の部分とまったく同じように、体の一箇所に恒久的に付着している。体が回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分の体がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周してカメラの方を向いたときにだけ再び顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色や余分なガムボールは一切現れない)——とカラフルな紙吹雪は、回転するたびに揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。2人はこのようにして一緒にフレームインし、**画面左端から**着実に進みながら、時間が経つにつれて床の上でその姿がだんだんはっきりと見えるようになっていき、<Picture 2>に示された位置・姿勢に到達したところで、画面左寄りで自然に穏やかに止まり、右側には広い床の余白が残る——卵形のキャラクターの固定された向き、透明なキャラクターが現在の回転角度で顔が見えているポーズも含めて、<Picture 2>とぴったり一致してこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt-entrance_v3.mp4`(未生成)
- 判定: 未検証
- メモ: 左右反転のご指摘を受けて左からのフレームインに差し戻し、新しいPicture2
  (たまちゃんが左・ぽよんが右)に合わせて更新した版

### v2 (2026-09-15) — 旧版(右からフレームイン、後に左右逆と判明)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout. From the right edge of the frame, the transparent, jelly-like rubber character and the egg-shaped character move into view together, each moving in its own distinct way. The transparent character spins steadily in place like a flat disc turning on the floor while gliding sideways at the same time, moving further onto the floor with each moment. Critically, its face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it, exactly like the rest of its glossy skin. As the body spins, the face spins together with it as one single rigid piece: the face turns away and becomes hidden from view as that side of the body rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face the camera — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift and tumble inside with each spin, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. Beside it, the egg-shaped character moves in a completely different way: it does not spin, tumble, or turn its body to face its direction of travel at all — its facing direction and body orientation stay exactly the same as its pose in <Picture 2>, fixed and unchanging, the entire time. Instead, while keeping that same fixed orientation, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth sideways glide across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater, without ever turning to face the direction it is gliding toward. After each glide slows, it plants its legs again for another quick kick-off in the same fixed orientation, sending it gliding sideways once more, repeating this kick-and-glide rhythm the whole way in. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Both characters move into frame together this way, entering steadily from the right edge, gradually advancing further onto the floor and becoming more visible with each moment, until they reach the positions and poses shown in <Picture 2>, matching <Picture 2> exactly — including the transparent character's spinning pose with its face visible from its current rotated angle, and the egg-shaped character's fixed facing direction — at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り誰もいない薄い黄緑色の床を真上から見下ろしており、開始時点ではキャラクターは一人も映っていない。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。**画面右端から**、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが一緒にフレームインしてくる——それぞれがまったく異なる動き方をする。透明なキャラクターは、床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に横方向へ滑るように移動し、時間が経つにつれて床の上をさらに進んでいく。極めて重要な点として、その顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、光沢のある体の他の部分とまったく同じように、体の一箇所に恒久的に付着している。体が回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分の体がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周してカメラの方を向いたときにだけ再び顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色や余分なガムボールは一切現れない)——とカラフルな紙吹雪は、回転するたびに揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。その隣では、卵形のキャラクターがまったく異なる動き方をする——回転したり転がったり、進行方向へ体ごと向き直ったりすることは一切ない——**その向いている方向・体の向きは<Picture 2>でのポーズとまったく同じまま、終始固定され変わらない**。その代わりに、その同じ固定された向きを保ったまま、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を床の上で横方向へスーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じであり、滑っていく方向へ向き直ることは一切ない。その滑りが緩やかになるたびに、同じ固定された向きのまま再び脚をついてもう一度素早く蹴り出し、また横へ滑っていく、というキック&グライドのリズムをフレームインしている間ずっと繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。2人はこのようにして一緒にフレームインし、**画面右端から**着実に進みながら、時間が経つにつれて床の上でその姿がだんだんはっきりと見えるようになっていき、<Picture 2>に示された位置・姿勢——透明なキャラクターが現在の回転角度で顔が見えているポーズ、卵形のキャラクターの固定された向きも含めて——にぴったり一致したところでこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt-entrance_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 右からのフレームイン+たまちゃんの向き固定への変更版

### v1 (2026-09-15) — 旧版(左からフレームイン)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 4.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the empty pale yellow-green floor exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. Neither character ever speaks, talks, or makes any vocalization at any point — both stay completely silent throughout. From the left edge of the frame, the transparent, jelly-like rubber character and the egg-shaped character move into view together, each moving in its own distinct way. The transparent character spins steadily in place like a flat disc turning on the floor while gliding sideways at the same time, moving further onto the floor with each moment. Critically, its face — its eyes and mouth — is not a separate marking floating independently on top of its body; it is a fixed part of the body's surface, permanently attached to one spot on it, exactly like the rest of its glossy skin. As the body spins, the face spins together with it as one single rigid piece: the face turns away and becomes hidden from view as that side of the body rotates away from the camera, then comes back into view again only once that same spot has rotated all the way back around to face the camera — the face must never stay fixed in place, floating in the same on-screen position or orientation while the body spins independently underneath or around it. Its interior contents — exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs (ten in total, this exact count and color mix never changing, no other colors or extra gumballs appearing), plus colorful confetti — shift and tumble inside with each spin, always staying fully contained inside its glossy transparent body, never flying out or passing through its skin at any point. Beside it, the egg-shaped character moves in a completely different way: it does not spin or tumble at all. Instead, it plants its short, stiff legs against the floor and gives a quick, sharp kick-off, launching its whole body into a smooth glide across the floor — exactly like a swimmer pushing off the wall and gliding in a streamlined position underwater. After each glide slows, it plants its legs again for another quick kick-off, sending it gliding forward once more, repeating this kick-and-glide rhythm the whole way in. Its arms stay tucked in close to its body during each glide, its legs never bending at the ankle and its heels never touching the ground. Both characters move into frame together this way, entering steadily from the left edge, gradually advancing further onto the floor and becoming more visible with each moment, until they reach the positions and poses shown in <Picture 2>, matching <Picture 2> exactly — including the transparent character's spinning pose with its face visible from its current rotated angle — at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の4.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定俯瞰ショットで、<Picture 1>で示された通り誰もいない薄い黄緑色の床を真上から見下ろしており、開始時点ではキャラクターは一人も映っていない。カメラは一切パン・チルト・ズーム・カットをしない。どちらのキャラクターも一切話したり喋ったり発声したりすることはなく、終始完全に無言のままである。画面左端から、透明でゼリーのようなラバーキャラクターと卵形のキャラクターが一緒にフレームインしてくる——それぞれがまったく異なる動き方をする。透明なキャラクターは、床の上で平らな円盤のように一定のペースでその場でくるくると回転しながら、同時に横方向へ滑るように移動し、時間が経つにつれて床の上をさらに進んでいく。極めて重要な点として、その顔(目と口)は体の上に独立して浮いている別の模様ではなく、体の表面に属する固定された一部分であり、光沢のある体の他の部分とまったく同じように、体の一箇所に恒久的に付着している。体が回転すると、顔も体と一体の硬いパーツとして一緒に回転する:その部分の体がカメラから離れる方向へ回転すれば顔も一緒に向こうを向いて見えなくなり、同じ箇所がぐるっと一周してカメラの方を向いたときにだけ再び顔が見える——顔が画面上の同じ位置・同じ向きのまま固定されたまま浮いていて、体だけがその下や周りで独立して回転する、ということは決して起こらない。中のガムボール——正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは変わらず、他の色や余分なガムボールは一切現れない)——とカラフルな紙吹雪は、回転するたびに揺れ動き転がるが、常に光沢のある透明な体の中に完全に収まったままで、一度も外に飛び出したり体の表面を突き抜けたりすることはない。その隣では、卵形のキャラクターがまったく異なる動き方をする——回転したり転がったりすることは一切ない。代わりに、短く硬い脚を床につけて素早く鋭い蹴り出しを行い、体全体を床の上でスーッと滑らせる——ちょうど水泳選手が壁を蹴って、水中で流線型の姿勢のまま滑っていくのと同じである。その滑りが緩やかになるたびに、再び脚をついてもう一度素早く蹴り出し、また前へ滑っていく、というキック&グライドのリズムをフレームインしている間ずっと繰り返す。滑っている間、腕は体に沿って引き寄せられた状態を保ち、脚は足首で曲がることも、踵が地面につくことも一切ない。2人はこのようにして一緒にフレームインし、画面左端から着実に進みながら、時間が経つにつれて床の上でその姿がだんだんはっきりと見えるようになっていき、<Picture 2>に示された位置・姿勢——透明なキャラクターが現在の回転角度で顔が見えているポーズも含めて——にぴったり一致したところでこのショットが終わる。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/D1-alt-entrance_v1.mp4`(未生成)
- 判定: 未検証
- メモ: 空の床からの登場のため、生成結果を見て「忽然と現れる」ような違和感が
  出た場合は、体の一部が画面端ですでに見切れている状態から始まるI2VA版への
  切り替えを検討する(D-1-entranceと同じ注意点)

## ComfyUIでの設定メモ
- Picture 1: いただいた画像1(誰もいない薄い黄緑色の床)
- Picture 2: いただいた画像2(画面左寄りに、たまちゃんが左・ぽよんが右で
  回転中の姿勢で並ぶ、右側=入ってきた側に余白)
- モード: FL2VA
- 尺: 4秒目安(短い導入カットのため)
- 移動方向: 画面右端からフレームイン→左方向へ進んで左寄りで停止
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- 生成後、D-1-alt(v2)の冒頭と自然につながるか確認すること
