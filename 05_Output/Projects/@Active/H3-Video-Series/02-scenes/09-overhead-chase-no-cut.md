---
project: H3-Video-Series
scene: 9
mode: I2VA
duration: 8s
---

# シーン9: カットを割らずに同じ場所でフレームアウト・フレームインする追いかけっこ

## シーン内容
シーン5と同じ、俯瞰の固定カメラ・オリーブグリーンの床の構図。ぽよんがたまちゃんを
挑発するように弾んで逃げ、たまちゃんがよちよち歩きで追いかける。同じ場所(画面の右端・左端)
からフレームアウトしては、また同じ場所からフレームインする、を繰り返す。
**カットは一切割らず、最初から最後まで単一のショットとして描写する**
(`[Shot 2]`のような新しいショット表記を使うと、モデルがカット/場面転換として
扱ってしまうことがあるため、あえて使わない)。

## 最初のフレーム(Picture 1)
シーン5と同じ、オリーブグリーンの床を真上から見下ろす構図。左に透明なぽよん、
右にたまちゃんが並んでこちらを向いている。

## H3プロンプト(ComfyUI用)

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 3D CG, claymation-style character render, a single continuous static overhead shot holds the exact same fixed position, framing, and lens throughout the entire video, looking straight down on the olive-green floor as shown in <Picture 1>, with the transparent, jelly-like rubber character on the left and the egg-shaped character on the right, both facing up toward the camera. The camera never pans, tilts, zooms, or cuts away at any point, and no cut ever interrupts this one unbroken shot; only the characters move within this unchanging static frame. The transparent character springs into motion first, bouncing playfully toward the right edge of the frame and exiting completely past it, vanishing entirely from view. A beat later, the egg character toddles after it in its stiff, heel-less waddle, chasing it out of frame through that same right edge until it too is completely gone from view. A moment later, both characters reappear together from that same right edge, the transparent character bouncing back into frame first with the egg character toddling closely behind, now both moving back toward the left across the floor. They continue all the way until the transparent character bounces out past the left edge and completely disappears, immediately followed by the egg character toddling out after it through that same left edge, also vanishing from view. Shortly after, both come bouncing and toddling back into frame together from that same left edge, still playing their chase, before slowing to a stop near the center of the frame, both laughing.

overall_soundscape: A light, springy bounce sound and soft gumball rattle mark each of the transparent character's hops, while soft, muffled footsteps mark the egg character's toddling steps close behind. Both characters produce light, happy giggles throughout the chase.

non_diegetic_music: A playful, skipping pizzicato melody at a bright, bouncy tempo, its rhythm mirroring the back-and-forth chase across the frame.
```

## 日本語訳(参考用)

**指示行**
対象動画の0.00秒時点で、<Picture 1>(Shot 1より)が完全に参照されます。

**映像・音声描写**
[Shot 1] 3D CGのクレイアニメ調キャラクターレンダー。動画全体を通してまったく同じ固定位置・同じ画角・同じレンズのままの、一度も切り替わらない単一の俯瞰ショットで、<Picture 1>で示された通り、オリーブグリーンの床を真上から見下ろしており、左に透明でゼリーのようなラバーキャラクター、右に卵形のキャラクターが並び、どちらもカメラの方(上)を向いている。カメラは一切パン・チルト・ズームせず、この一つの途切れないショットをカットが遮ることは決してない。動くのはこの変化しない固定フレームの中のキャラクターだけである。まず透明なキャラクターが先に動き出し、いたずらっぽく弾みながら画面右端に向かい、完全にその外へ出て姿が見えなくなる。少し遅れて、卵形のキャラクターが硬く踵のつかないよちよち歩きでその後を追いかけ、同じ右端から画面の外へ出て、こちらも完全に見えなくなる。しばらくして、二人は同じ右端から一緒に再びフレームインし、透明なキャラクターが先に弾みながら戻り、卵形のキャラクターがすぐ後ろをよちよちとついてきて、今度は二人とも左方向へ向かって床の上を進んでいく。そのまま進み続け、透明なキャラクターが画面左端の外へ弾み出て完全に姿を消し、すぐに卵形のキャラクターも同じ左端からその後を追って画面の外へ出て、同じく見えなくなる。その少し後、二人は同じ左端から一緒に弾みながら、よちよち歩きながら再びフレームインし、追いかけっこを続けたのち、画面中央付近で動きを緩めて止まり、二人とも笑い合う。

**環境音**
透明なキャラクターが弾むたびに、軽やかで弾力のある音と、中で軽く鳴るガムボールの音が響き、その少し後ろから卵形のキャラクターのよちよち歩きの、柔らかくこもった足音が続く。追いかけっこをしている間、二人はずっと軽やかで楽しそうな笑い声を上げ続ける。

**BGM(観客のみに聞こえる)**
明るく弾むテンポの、軽快なピチカートのメロディが、画面を行ったり来たりする追いかけっこのリズムに合わせて鳴る。

## ComfyUIでの設定メモ
- 最初のフレーム画像(シーン5と同じ、オリーブグリーンの床に2人が並ぶ俯瞰構図)を Load Image → I2VA用の画像入力に接続
- モード: I2VA
- 尺: 8秒(プロンプト内の秒数表記と要一致)
- **重要**: `[Shot 2]`などの追加ショット表記は使わず、単一の`[Shot 1]`のみで最初から最後まで記述すること
  (複数のShot表記があると、カメラが同じ位置のままでもカット扱いされてしまうことがある)

## 生成結果
- (ここに生成した動画のメモ・最終フレームのスクショなどを追記していく)
