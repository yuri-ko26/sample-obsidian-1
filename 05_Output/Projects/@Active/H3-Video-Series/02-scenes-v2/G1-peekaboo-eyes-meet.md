---
project: H3-Video-Series-v2
cut: G-1
mode: FL2VA
status: draft
---

# カットG-1: 雲だけの背景に2人が両端からひょこっと顔を出し、目が合って「ばあ!」(Gビート1回目)

## シーン内容
Gビート(「いないいないばあ」×4)の1回目。正面固定カメラ、雲のクローズアップ背景。
F-3で2人がフレームアウトして誰もいなくなった雲の風景から、そのまま繋がる入り。

1. Picture1の状態(パステルの雲だけ、キャラクターなし)から始まる
2. 画面**左端からぽよん**が、同じ瞬間に**右端からたまちゃん**が、顔が見える分だけ
   ゆっくりひょこっと覗き込む(体の大部分はフレーム外のまま)
3. 一拍、2人とも正面を向いたまま静止する
4. 体はそれ以上動かさず、**目だけを動かして**お互いを見つける(ぽよんは右へ、たまちゃんは左へ)
5. 目が合った瞬間、2人とも「ばあ!」の驚き顔になり、その表情のままPicture2に着地する

**設計メモ(参照画像について)**: 最初のフレームには誰も映っていないが、最後のフレームに
2人の見た目がはっきり映っているため、FL2VAとして両方を参照させればモデルが2人の見た目を
anchoring できる(F-0と同じプロジェクト標準手法)。もし生成結果で2人が「忽然と画面内に
現れる」動きになってしまった場合は、`00-series-overview.md`のD2-entrance v2の知見どおり、
**Picture1を「両端に2人の体が2〜3割だけ見切れている状態」の画像に差し替える**こと。

**設計メモ(ぽよんの口)**: キャラクター設定の「驚き顔」例外ルールでは、ばあ!の瞬間に限り
口が立体的に開いて内側にほんのり色が見えてもよいとされている。ただしぽよんは口に色がつく
不具合が繰り返し発生しているため、このカットでは**たまちゃんだけ例外を適用**(口の中に
コーラルピンクがのぞく)し、**ぽよんは立体的に開いた驚き口のまま、素材は体と同じ透明を維持**
(口の奥に中のガムボールが透けて見える)という書き分けにしている。ぽよんの口にも色を
入れたい場合はv2で変更する。

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない(顔のパーツは点目と輪郭線の口のみ)
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかない/足首を曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんのガムボールは常に重力に従って体の底に沈み、動くところころ転がる
- ぽよんの口は大きくしすぎない(顔の横幅の3分の1程度まで)

## 参照画像
- Picture 1(最初のフレーム): パステルカラー(ピンク・ラベンダー・ミントグリーン)の雲が
  層になったクローズアップ背景のみ。キャラクターは映っていない(F-3の最終フレームがそのまま使える)
- Picture 2(最後のフレーム): 画面左端からぽよん、右端からたまちゃんが顔だけ覗かせ、
  2人とも目が合って「ばあ!」の驚き顔になっている構図

## プロンプト履歴

### v1 (2026-09-14)

**H3プロンプト(ComfyUI用)**
```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static shot holds the exact same fixed position, framing, and lens throughout the entire video, showing the close-up of layered pastel cloud hills in pink, lavender, and mint green beneath a soft blue-lavender sky exactly as shown in <Picture 1>, with no characters visible at the start. The camera never pans, tilts, zooms, or cuts away at any point. From the left edge of the frame, the transparent, jelly-like rubber character slowly peeks in, sliding in just far enough that its glossy rounded body and its face become visible while the rest of it stays past the left edge — its interior gumballs, exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green gumballs, ten in total, this exact count and color mix never changing and no other colors or extra gumballs ever appearing, together with small colorful square and diamond confetti, always settle naturally at the bottom of its body under gravity, never floating motionless in mid-air or appearing stuck together, rolling and jostling against each other and the inner wall as it moves, shifting without ever spilling out. At the very same moment, from the right edge of the frame, the egg-shaped character peeks in the same way, its white upper shell and coral-pink lower shell just visible while the rest of it stays past the right edge, staying up on the very tips of its toes the entire time, its heels never touching the ground and its short stiff legs never bending at the ankle. The egg character never has eyebrows at any point — its face is only round black dot eyes and an outline-only mouth. Both characters hold still for a beat, facing straight forward, and then, without turning or moving their bodies any further into the frame, each one shifts only its eyes toward the other: the transparent character's eyes dart to the right and the egg character's eyes dart to the left, and their gazes meet. In that single instant of recognition, both characters' mouths pop open into the same small, rounded, startled peekaboo shape — the egg character's open mouth shows a hint of soft coral pink inside as an exception to its usual flat outline mouth, while the transparent character's mouth stays just as transparent and see-through as its glossy skin, its mouth outline never filled with any color or paint, so the gumballs behind it remain visible straight through the open mouth outline, and this stays true even as its expression changes; its mouth also stays moderate in size, no more than about a third of the width of its face, never exaggerated or oversized. Both characters' round cheeks flush lightly, and they hold this single delighted, startled peekaboo expression without changing it again, matching the positions, framing, expressions, and appearance shown in <Picture 2> exactly at the end of the shot.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
参照画像と対象動画の対応 — Picture 1(Shot 1より)は対象動画の0.00秒地点に、Picture 2(Shot 1より)は対象動画の6.00秒地点に対応します。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の固定ショットで、<Picture 1>で示された通り、やわらかなブルー〜ラベンダーの空の下にピンク・ラベンダー・ミントグリーンの雲が層になったクローズアップの景色を映しており、開始時点ではキャラクターは一切映っていない。カメラは一切パン・チルト・ズーム・カットをしない。画面左端から、透明でゼリーのようなラバーキャラクターが、光沢のある丸い体と顔がちょうど見える分だけゆっくりと覗き込み、残りの部分は左端の外に留まったまま——中のガムボールは正確に黄色4個・赤2個・水色1個・黄緑3個(合計10個、この数と色の組み合わせは決して変わらず、他の色や余分なガムボールが現れることもない)と、小さくカラフルな四角形・ひし形の紙吹雪であり、常に重力に従って体の底に自然に沈み、宙に浮いたまま静止したりお互いにくっついて見えたりすることは一切なく、動くたびにお互いや内壁にぶつかってころころと転がり、揺れ動くがこぼれることはない。まったく同じ瞬間に、画面右端からは卵形のキャラクターも同じように覗き込み、白い上半分の殻とコーラルピンクの下半分の殻がちらりと見え、残りの部分は右端の外に留まる。卵形のキャラクターは終始つま先立ちのままで、踵は決して地面につかず、短く硬い脚は足首で曲がらない。卵形のキャラクターにはどの瞬間も眉毛はつかない——顔のパーツは丸い黒の点目と輪郭線だけの口のみである。2人は一拍、正面を向いたまま静止し、それから体をそれ以上フレームの中へ動かすことも向きを変えることもなく、目だけをすっと相手のほうへ動かす。透明なキャラクターの目は右へ、卵形のキャラクターの目は左へ動き、2人の視線が合う。その気づきの瞬間、2人の口は同時に、小さく丸い驚いた「いないいないばあ」の形にぱっと開く——卵形のキャラクターの開いた口には、いつもの平らな輪郭線だけの口の例外として、やわらかなコーラルピンクがほんのりのぞく。一方、透明なキャラクターの口は光沢のある肌と同じくどこまでも透明で見通せるままで、口の輪郭線の内側に色や塗りつぶしが入ることは一切なく、開いた口の輪郭の奥に中のガムボールが透けて見え続ける。これは表情が変わっても崩れない。またその口は大きさも控えめに保たれ、顔の横幅の3分の1程度までにとどまり、誇張された巨大な口にはならない。2人とも丸い頬がほんのり赤らみ、この驚いた嬉しそうな「ばあ!」の表情を一度きりのものとしてそれ以上変えずに保ち、<Picture 2>で示された位置・構図・表情・見た目とショットの最後でぴったり一致する。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/G1_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

<!-- 修正が必要になったら、上書きせず ### v2 (YYYY-MM-DD) — v1からの変更点: ... を追記していく -->

## ComfyUIでの設定メモ
- Picture 1: 誰もいない雲のクローズアップ背景(F-3の最終フレームを流用可)
- Picture 2: 2人が両端から顔を覗かせ、目が合って驚き顔になっている構図
- モード: FL2VA
- 尺: 6秒(香盤表どおり。覗き込み→一拍静止→目が合う→「ばあ!」を収めるため)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
