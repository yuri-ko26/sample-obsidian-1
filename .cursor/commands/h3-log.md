# H3生成ログ記録

## Description
H3で生成した動画を台帳(`07_System/Ledger/生成ログ.csv`)に記録します。
Pod の起動/停止の記録にも使えます。

## Prompt
H3の生成記録を台帳に追加してください。

### やること

1. 私が伝えた内容(カット名・版・判定・気づいたこと など)を読み取る
2. 不足している情報は、以下から**推測せずに補う**:
   - `05_Output/Projects/@Active/(案件)/02-scenes-v2/` の該当ノート
     → `mode`、解像度、尺、プロンプトのパス(`--prompt-ref`)
   - `07_System/Ledger/Pod稼働ログ.csv` の最新行 → GPU・単価
   - それでも分からない項目は**空のままにする**(でっち上げない)
3. `python3 scripts/h3log.py gen add` を実行する
4. 該当のシーンノートの「生成結果」欄も同じ内容で更新する
   (プロンプト本文は**絶対に上書きしない**。版として追記する)

### コマンドの形

```bash
python3 scripts/h3log.py gen add \
  --project (案件名) --cut (カット) --version (v1/v2...) \
  --mode (I2VA等) --quant (int8等) --compute-s (秒) \
  --resolution (864x480等) --duration (秒) --seed (seed) \
  --video (ファイル名.mp4) --verdict (OK/NG/未検証) \
  --prompt-ref "(シーンノートのパス)" \
  --note "(気づいたこと)"
```

### Pod の起動/停止を頼まれた場合

```bash
# 起動時
python3 scripts/h3log.py pod start --project (案件名) --gpu "(GPU名)" --rate (USD/時)
# 停止時
python3 scripts/h3log.py pod end
```

### 原価レポートを頼まれた場合

```bash
python3 scripts/h3log.py report --project (案件名) \
  --since (YYYY-MM-DD) --until (YYYY-MM-DD) \
  --jpy 155 --labor-hours (時間) --labor-rate (円/時) \
  --out "05_Output/Projects/@Active/(案件)/原価レポート-(YYYY-MM).md"
```

### 注意
- `--verdict` を NG にする場合も、**何が良かったかを `--note` に必ず残す**
  (H3は偶然の良さが出るので、NGの中に次の版のヒントがある)
- 実行後、記録された内容を1行で報告する
