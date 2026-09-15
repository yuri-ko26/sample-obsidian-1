---
project: H3-Video-Series-v2
cut: F-7
mode: I2VA
status: draft
---

# カットF-7: たまちゃんがぽよんに顔をぐりぐり寄せて頬擦り→ぽよんは照れくさそうに受け入れる→2人の顔のアップで終わる

## シーン内容
F-6の続き。今回は追いかけっこではなく、2人が寄り添う穏やかな締めのカット。
正面固定の広い構図から始まり、たまちゃんがぽよんに歩み寄って顔をぐりぐりと
擦り寄せる仕草をし、ぽよんが照れくさそうにそれを受け入れる様子まで。カメラは
緩やかに寄っていき、最終的に2人の顔のアップショットで終わる(この点はF-1〜F-6の
「カメラ完全固定」ルールとは異なり、本カットでは意図的にゆっくり寄せる)。

1. Picture1の状態(たまちゃんが左寄りの雲、ぽよんが右寄り・少し高い位置の雲の
   そばで浮かぶように笑っている)から始まる
2. たまちゃんがぽよんの方へつま先立ちのまま歩み寄っていく。カメラも合わせて
   ゆっくりと2人へ寄っていく
3. たまちゃんがぽよんに顔を近づけ、ぐりぐりと擦り寄せる(頬擦り)仕草をする
4. ぽよんは一瞬驚くが、すぐに照れくさそうな、嬉しそうな表情でそれを受け入れる
   (目を少し柔らかく細める・小さく控えめな笑み・少し体を縮めるような仕草)
5. カメラはさらに寄っていき、最終的に2人の顔が画面いっぱいに映るアップショットで終わる

**キャラクター参照**: `01-characters/character-reference.md` の制約を必ず踏まえること。
特に:
- たまちゃんに眉毛は絶対につかない(アップになっても同様)
- たまちゃんは常につま先立ちのまま、踵は絶対に地面につかず、足首も曲げない
- ぽよんの中身は正確に「黄色4個・赤2個・水色1個・黄緑3個(合計10個)+カラフルな紙吹雪」
- ぽよんの口は輪郭線のみ・無着色のまま(体と同じ透明素材)。アップになり照れた
  表情になっても口の中に色は一切つかない
- ぽよんに新しい色(頬の赤み等)を追加しない。「照れ」は目の形・口の小ささ・
  体の縮こまり方など、既存のデザイン要素だけで表現する

## 参照画像
- Picture 1(最初のフレーム): いただいた画像。画面左寄りの雲にたまちゃんが立ち
  大笑いしており、画面右寄り・少し高い位置でぽよんが浮かぶように笑っている構図

## プロンプト履歴

### v2 (2026-09-15) — 現在の採用版(頬擦りをもっと「ぐりぐり」力強く)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous shot begins at the exact same wide framing and lens as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily, matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. After a brief happy moment, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As it approaches, the camera slowly and smoothly begins pushing in toward both characters, gradually tightening the framing over the course of the shot. Once close beside the transparent character, the egg character presses its face firmly against the transparent character's rounded body and rubs it vigorously and enthusiastically back and forth, again and again, in a big, energetic, affectionate grinding motion — much more forceful and playful than a gentle nuzzle, really digging its face in and rubbing hard with obvious excited affection. Each vigorous rub visibly jostles and wobbles the transparent character's whole soft body, its interior gumballs jiggling energetically along with it. The transparent character is briefly startled by this sudden, enthusiastic rubbing, then quickly relaxes into a bashful, pleased reaction despite the vigorous affection — its round eyes softening and narrowing slightly rather than staying wide open, its small mouth staying modest and closed rather than opening wide, its whole body wobbling and jiggling from the energetic rubbing while also drawing in slightly with a small, shy, happy shiver, gladly accepting the enthusiastic affectionate gesture even as it visibly wobbles from the force of it. The transparent character's mouth remains exactly the same thin, dark, uncolored outline it always is throughout this entire reaction, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind added anywhere on it — its interior gumballs, exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti, always settling naturally at the bottom of its body under gravity even as they jiggle from the vigorous rubbing, remain clearly visible the whole time. By the end of the shot, the camera has pushed all the way into a tight close-up of both characters' faces side by side, filling most of the frame, with the egg character's face still pressed affectionately and energetically against the transparent character, both wearing warm, happy, slightly bashful expressions, its round dot eyes crinkled happily, still with no eyebrows.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>とまったく同じ広い画角・レンズで始まる単一の連続したショットで、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも<Picture 1>の見た目・表情・位置のまま嬉しそうに笑っている状態から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。少し嬉しそうな時間を過ごした後、卵形のキャラクターが透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。近づくにつれて、カメラはゆっくりと滑らかに2人へ向かって寄っていき始め、ショットが進むにつれて徐々に画角が狭まっていく。透明なキャラクターのすぐそばまで来たところで、卵形のキャラクターは顔を透明なキャラクターの丸い体にぐっと押し付け、**何度も何度も、大きく元気よく、力強くすりすりと擦り寄せる**——優しいなでなでというよりずっと力強く遊び心のある動きで、興奮した愛情を隠さずに顔をぐりぐりと押し付けて擦る。この力強い擦り寄せの一回ごとに、透明なキャラクターの柔らかい体全体が目に見えて揺さぶられ、ぷるぷると波打ち、中のガムボールも一緒に元気よく揺れる。透明なキャラクターはこの突然の熱烈な擦り寄せに一瞬驚くが、この力強い愛情表現にもかかわらず、すぐに照れくさそうな、嬉しそうな反応へと落ち着く——丸い目は大きく見開いたままではなく、少し柔らかく細まり、小さな口は大きく開くのではなく控えめに閉じたままで、力強い擦り寄せでぷるぷると揺れ波打ちながらも、体全体がわずかに縮こまるような、恥ずかしそうで嬉しそうな小さな震えを見せ、その勢いに揺さぶられながらも嬉しそうにこの熱烈な愛情表現を受け入れる。透明なキャラクターの口は、この反応の間ずっと、いつもとまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されない——中のガムボール(正確に黄色4個・赤2個・水色1個・黄緑3個、合計10個、この数と色の組み合わせは変わらない、プラスカラフルな紙吹雪)は、力強い擦り寄せで揺れながらも常に重力に従って体の底に自然に沈んだまま、はっきりと見え続ける。ショットの終わりには、カメラは完全に寄りきり、2人の顔が並んだタイトなクローズアップとなり、画面の大部分を占める——卵形のキャラクターの顔は依然として透明なキャラクターに力強く愛おしそうに押し付けられたままで、2人とも温かく嬉しそうな、少し照れたような表情を浮かべており、丸い点目は嬉しそうに笑いじわになり、眉毛はやはりつかない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v2.mp4`(未生成)
- 判定: 未検証
- メモ: 「すりすりが優しすぎる」フィードバックへの対応版。頬擦りを「何度も・大きく・
  力強く」な「ぐりぐり」の動きに強化し、ぽよんの体が揺さぶられる反応も追加

### v1 (2026-09-15) — 旧版(すりすりが優しすぎた)

**H3プロンプト(ComfyUI用)**
```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous shot begins at the exact same wide framing and lens as shown in <Picture 1>, with the egg-shaped character standing on the cloud at left and the transparent, jelly-like rubber character hovering near the cloud at right, both laughing happily, matching their exact appearance, expression, and position from <Picture 1> at the very start. The egg character never has eyebrows at any point. The egg character's feet are simple stiff, rounded points fused directly to the ends of its legs, with no ankle joint of any kind that could ever bend or flex — it is anatomically built to only ever balance and move on the very tips of these feet, and its heels can never touch any surface at all. After a brief happy moment, the egg character begins walking toward the transparent character, always walking up on the very tips of its toes only, its heels never once touching the ground, its short stiff legs never bending at the ankle at any point. As it approaches, the camera slowly and smoothly begins pushing in toward both characters, gradually tightening the framing over the course of the shot. Once close beside the transparent character, the egg character leans its face in and gently nuzzles it, rubbing its cheek softly and affectionately against the transparent character's rounded body, in a warm, cuddly gesture. The transparent character is briefly startled by the sudden closeness, then quickly relaxes into a bashful, pleased reaction — its round eyes softening and narrowing slightly rather than staying wide open, its small mouth staying modest and closed rather than opening wide, its whole body drawing in slightly with a small, shy, happy wobble, gladly accepting the affectionate gesture. The transparent character's mouth remains exactly the same thin, dark, uncolored outline it always is throughout this entire reaction, staying just as transparent as the rest of its glossy body, with absolutely no new color, tint, or fill of any kind added anywhere on it — its interior gumballs, exactly 4 yellow, 2 red, 1 light blue, and 3 yellow-green, ten in total, this exact count and color mix never changing, plus colorful confetti, always settling naturally at the bottom of its body under gravity, remain clearly visible the whole time. By the end of the shot, the camera has pushed all the way into a tight close-up of both characters' faces side by side, filling most of the frame, with the egg character's face still affectionately nuzzled close to the transparent character, both wearing warm, happy, slightly bashful expressions, its round dot eyes crinkled happily, still with no eyebrows.

overall_soundscape: None.

non_diegetic_music: None.
```

**日本語訳**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。<Picture 1>とまったく同じ広い画角・レンズで始まる単一の連続したショットで、卵形のキャラクターが左側の雲に立ち、透明でゼリーのようなラバーキャラクターが右側の雲のそばに浮かぶように、2人とも<Picture 1>の見た目・表情・位置のまま嬉しそうに笑っている状態から始まる。卵形のキャラクターにはどの瞬間も眉毛はつかない。卵形のキャラクターの足は、脚の先端に直接固定されたシンプルで硬い丸い先端であり、曲がったり動いたりする足首の関節は一切存在しない——構造上、常につま先の先端だけでバランスを取り移動するようにできており、踵はどんな面にも決して触れることができない。少し嬉しそうな時間を過ごした後、卵形のキャラクターが透明なキャラクターの方へ歩き始める——常につま先だけで立ち、踵はどの瞬間も一切地面につかず、短く硬い脚は足首でどの瞬間も曲がらない。近づくにつれて、カメラはゆっくりと滑らかに2人へ向かって寄っていき始め、ショットが進むにつれて徐々に画角が狭まっていく。透明なキャラクターのすぐそばまで来たところで、卵形のキャラクターは顔を近づけ、透明なキャラクターの丸い体にやさしく、愛おしそうに頬を擦り寄せる、温かく甘えるような仕草をする。透明なキャラクターは突然の近さに一瞬驚くが、すぐに照れくさそうな、嬉しそうな反応へと落ち着く——丸い目は大きく見開いたままではなく、少し柔らかく細まり、小さな口は大きく開くのではなく控えめに閉じたままで、体全体がわずかに縮こまるような、恥ずかしそうで嬉しそうな小さな震えを見せながら、この愛情表現を喜んで受け入れる。透明なキャラクターの口は、この反応の間ずっと、いつもとまったく同じ薄く暗い無着色の輪郭線のままで、光沢のある体の残りの部分とまったく同じように透明なままであり、新しい色・色調・塗りつぶしはどこにも一切追加されない——中のガムボール(正確に黄色4個・赤2個・水色1個・黄緑3個、合計10個、この数と色の組み合わせは変わらない、プラスカラフルな紙吹雪)は常に重力に従って体の底に自然に沈んだまま、はっきりと見え続ける。ショットの終わりには、カメラは完全に寄りきり、2人の顔が並んだタイトなクローズアップとなり、画面の大部分を占める——卵形のキャラクターの顔は依然として透明なキャラクターに愛おしそうに擦り寄せられたままで、2人とも温かく嬉しそうな、少し照れたような表情を浮かべており、丸い点目は嬉しそうに笑いじわになり、眉毛はやはりつかない。

**環境音**
なし。

**BGM(観客のみに聞こえる)**
なし。

**生成結果**
- 動画ファイル: `03-generated-videos/F7_v1.mp4`(未生成)
- 判定: 未検証
- メモ:

## ComfyUIでの設定メモ
- Picture 1: いただいた画像(たまちゃん左・ぽよん右、2人とも笑っている構図)
- モード: I2VA(最後のフレーム画像は不要。カメラが自然に寄っていく展開)
- 尺: 6〜7秒目安(歩み寄る2s/頬擦り+ぽよんの照れ反応2.5s/クローズアップに寄りきる2s)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
- **重要**: このカットは意図的にカメラを寄せる(F-1〜F-6の「カメラ完全固定」とは異なる)
- **重要**: ぽよんの「照れ」は色を足さず、目・口の形と体の縮こまり方だけで表現すること
