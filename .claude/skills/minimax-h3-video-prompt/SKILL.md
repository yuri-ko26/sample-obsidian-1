---
name: minimax-h3-video-prompt
description: 動画生成AI「MiniMax H3」向けのプロンプトを作成・リライトするためのスキル。T2VA/I2VA/FL2VA/L2VA(テキストや先頭・末尾フレームからの動画生成)、および Ref2VA(画像・動画・音声を参照する完全参照モード)のプロンプトを書くとき、"MiniMax H3", "MiniMax-H3", "integrated_multimodal_description", "overall_soundscape", "non_diegetic_music" などの語が出てきたときに使う。
---

# MiniMax H3 動画プロンプト作成スキル

MiniMax H3 の公式プロンプトガイド(Hugging Face: `VIDEO_PROMPT_WRITING_GUIDE_base_en.md` / `VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`)に基づく、動画生成プロンプトの作成手順。MiniMax H3 のプロンプトを作成・修正する依頼が来たら、必ずこのスキルの手順とリファレンスに従うこと。

## 手順

1. **入力モードを特定する**
   - `T2VA`: テキストのみから動画全体を組み立てる
   - `I2VA`: 先頭フレーム(画像1枚)から前方に展開する
   - `FL2VA`: 先頭フレームと末尾フレーム(画像2枚)の間を繋ぐ
   - `L2VA`: 末尾フレーム(画像1枚)に収束させる
   - `Ref2VA`: 画像・動画・音声などを参照素材として使う完全参照モード
2. **参照ガイドを読む**
   - `T2VA` / `I2VA` / `FL2VA` / `L2VA` の場合 → `references/base-en.md` を読み、最終プロンプト構造(instruction部 + 3つの共通コアフィールド)に従う。
   - `Ref2VA`(参照モード)の場合 → `references/ref-en.md` を読み、6セクション構成のリライト形式に従う。
3. **フィールド名・セクション順・ラベル・時刻表記を一字一句変えずに維持する**。フィールド名(`integrated_multimodal_description` など)は英語のまま書く。
4. 完成したプロンプトを提示する前に、下記の「出力ルール」と「品質チェック」を満たしているか確認する。

## モード別の要点(base)

- `integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music` の3フィールドを、この順番で使う(詳細は `references/base-en.md`)。
- **T2VA**: 画像アライメント指示なし。3つのコアフィールドから直接始める。
- **I2VA**: 先頭に `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.` を置く。
- **FL2VA**: 先頭に `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark...; Picture 2 (from Shot N) aligns with the S.SS-second mark...` を置く。
- **L2VA**: 先頭に `How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.` を置く。

## 参照モード(Ref2VA)の要点

`subject_definitions` → `summary` → `retention_analysis` → `detailed_description` → `overall_soundscape` → `non_diegetic_music` の順で6セクションを書く。参照ラベル(`<Subject N>` / `<Picture N>` / `<Video N>` / `<Audio N>`)は全セクションで一貫させる。詳細・ラベルの使い分け・保持関係の書き方(`fully_preserved` など)は `references/ref-en.md` を参照。

## 共通の出力ルール

- リライト本文は英語で書く。`<d>` タグ内のセリフ・歌詞、および画面に実際に表示される文字だけは元の言語のまま残す。
- 各ショットで「構図・被写体の見た目と位置・環境と光・アクションと状態変化・カメラワーク・現在の音・参照素材が実際に反映される箇所」を明示する。
- あらすじの要約や、未解決の参照ラベル、指定尺と合わない時間指定は避ける。
- カメラワークは「動きの種類 + 振幅 + 速度」を自然な英語の一文として書く(振幅・速度は意味がある場合のみ追加)。
- 話者には `(S1)`, `(S2)` のような安定したIDを付け、ショットをまたいで同じIDを使い続ける。

## 品質チェック(Tips)

- 全体の尺が、依頼された動画の長さ(4〜15秒)と一致しているか。
- 参照ラベル(`<Picture 1>`, `<Video 1>`, `<Audio 1>` など)が全セクションで一貫しているか。
- "cinematic" や "beautiful" のような抽象的な言葉ではなく、具体的な視覚・音の描写になっているか。
- キーフレームを使う場合(I2VA / FL2VA / L2VA)、先頭・末尾フレームがタイムライン上のどこに繋がるかを明示しているか。

## リファレンス

- `references/base-en.md` — T2VA / I2VA / FL2VA / L2VA 用の完全ガイド(構造、ショット・カット、カメラワーク一覧表、セリフ・歌唱、画面内テキスト、サウンドスケープ、BGM、各モードの実例付き)。
- `references/ref-en.md` — Ref2VA(完全参照モード)用の完全ガイド(6セクション構成、参照ラベルの定義、`summary` のタスク種別、`retention_analysis` の関係マーカー、`detailed_description` の書き方、完全な実例付き)。

必要な箇所は都度この2ファイルを読み込んで、記載されている用語・表・実例に忠実に従うこと。
