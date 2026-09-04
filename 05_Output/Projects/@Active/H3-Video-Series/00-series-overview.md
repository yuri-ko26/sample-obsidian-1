---
status: active
tool: MiniMax H3 (ComfyUI)
created: 2026-09-04
---

# H3動画シリーズ:卵くん & ラバーフレンド

## 概要
MiniMax H3(ComfyUIで生成)を使った、2キャラクターのショート動画シリーズ。
`.claude/skills/h3-prompt-writing` スキルを使って、シーンごとにH3用プロンプトを作成する。

## フォルダ構成
- `01-characters/` — 2キャラクターの共通設定(見た目・質感・動きの制約)。**毎回このファイルを踏まえてプロンプトを作ること**
- `02-scenes/` — シーンごとに作成したプロンプトと元になった画像の記録

## 進め方
1. 前のシーンの最終フレーム(または新しい画像)を「最初のフレーム」として用意
2. Claude Codeに「こういうシーンにしたい」と伝える
3. `01-characters/character-reference.md` の制約を守ったI2VA/FL2VAプロンプトを作成
4. `02-scenes/` に記録として保存(英語プロンプトに加えて**日本語訳も必ず併記する**)
5. ComfyUIで生成 → 次のシーンへ

## シーン一覧
- `02-scenes/01-bump-and-laugh.md` — ぽよんのドアップから始まり、ジャンプしてたまちゃんにぶつかり、二人で笑うシーン
- `02-scenes/02-rolling-play.md` — 俯瞰でぽよんとたまちゃんが並んでコロコロ転がって遊ぶシーン
- `02-scenes/03-cloud-ridge-chase.md` — 雲の稜線でぽよんとたまちゃんが追いかけっこをするシーン
- `02-scenes/04-rolling-catch-up.md` — 俯瞰でコロコロ転がってフレームアウト→再登場→ぽよんが追いつくシーン
- `02-scenes/05-overhead-big-jump.md` — 俯瞰固定カメラでぽよんが真上に大ジャンプし、たまちゃんにぶつかるシーン
