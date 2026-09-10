#!/usr/bin/env bash
# =============================================================================
# RunPod上に ComfyUI + MiniMax H3 を「Network Volume(/workspace)」へ構築する
#
#   最初の1回だけ実行します。2回目以降は既にあるものを飛ばすので、
#   同じコマンドをもう一度流しても壊れません(途中で失敗しても再開できます)。
#
#   使い方:
#     bash setup-h3-comfyui.sh --gpu l40s            # 何をするか確認してから実行
#     bash setup-h3-comfyui.sh --gpu l40s --yes      # 確認なしで実行
#     bash setup-h3-comfyui.sh --gpu l40s --dry-run  # 実行せず内容だけ見る
#
#   --gpu に指定できる値:
#     a40 a6000 a100 l40s rtx6000ada 4090 5090 rtxpro4500 pro6000mig48 rtxpro6000 h100
# =============================================================================
set -euo pipefail

WORKSPACE="${WORKSPACE:-/workspace}"
COMFY_DIR="$WORKSPACE/ComfyUI"
REPO="Comfy-Org/MiniMax-H3"
GPU=""; ASSUME_YES=0; DRY_RUN=0; WITH_REF2VA=0; SKIP_SAGE=0

log()  { printf '\033[1;36m▶ %s\033[0m\n' "$*"; }
ok()   { printf '\033[1;32m✅ %s\033[0m\n' "$*"; }
warn() { printf '\033[1;33m⚠️  %s\033[0m\n' "$*"; }
die()  { printf '\033[1;31m❌ %s\033[0m\n' "$*" >&2; exit 1; }
run()  { if [ "$DRY_RUN" = 1 ]; then printf '   [dry-run] %s\n' "$*"; else eval "$@"; fi; }

usage() { sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'; exit 0; }

while [ $# -gt 0 ]; do
  case "$1" in
    --gpu) GPU="${2:-}"; shift 2 ;;
    --yes|-y) ASSUME_YES=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    --with-ref2va) WITH_REF2VA=1; shift ;;
    --skip-sage) SKIP_SAGE=1; shift ;;
    -h|--help) usage ;;
    *) die "知らないオプション: $1  (--help で使い方)" ;;
  esac
done

# ---------------------------------------------------------------- GPUごとの構成
# H3は「拡散モデル + テキストエンコーダ(Qwen3-VL 32B) + VAE 2つ」で動きます。
# GPUの世代によって、速い量子化形式が違うので、ここで振り分けます。
# 世代ごとに「速い数値形式」が違うため、GPUで構成を振り分けます。
#   Ampere (A6000/A100)          … FP8非対応。INT8かBF16を使う
#   Ada     (L40S/RTX 6000 Ada)  … FP8が速い
#   Hopper  (H100)               … FP8/BF16
#   Blackwell (RTX 5090/PRO系)   … FP8 + NVFP4(この世代だけNVFP4が本当に速い)
case "$GPU" in
  a40|a6000|rtxa6000)
    case "$GPU" in
      a40) GPU_LABEL="A40 48GB (Ampere)" ;;
      *)   GPU_LABEL="RTX A6000 48GB (Ampere)" ;;
    esac
    DIFFUSION="minimax_h3_fl2va_pruned_int8_convrot.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_int8_convrot.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_int8_convrot.safetensors"
    NOTE="Ampere世代はFP8に非対応のためINT8を使います。48GBのVRAMには余裕があります。
                (システムRAMが64GB未満の場合、読み込み時にメモリ不足が出ることがあります)" ;;
  a100)
    GPU_LABEL="A100 SXM 80GB (Ampere)"
    DIFFUSION="minimax_h3_fl2va_pruned_bf16.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_bf16.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_int8_convrot.safetensors"
    NOTE="80GBあるので拡散モデルは量子化なし(BF16)。品質重視の構成です。" ;;
  l40s|rtx6000ada|6000ada)
    case "$GPU" in
      l40s) GPU_LABEL="L40S 48GB (Ada)" ;;
      *)    GPU_LABEL="RTX 6000 Ada 48GB (Ada)" ;;
    esac
    DIFFUSION="minimax_h3_fl2va_pruned_fp8_scaled.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_fp8_scaled.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_int8_convrot.safetensors"
    NOTE="Ada世代(48GB)はFP8が速い。NVFP4は速度上の利点がないので使いません。" ;;
  5090|rtxpro4500|pro4500)
    case "$GPU" in
      5090) GPU_LABEL="RTX 5090 32GB (Blackwell)" ;;
      *)    GPU_LABEL="RTX PRO 4500 32GB (Blackwell)" ;;
    esac
    DIFFUSION="minimax_h3_fl2va_pruned_fp8_scaled.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_fp8_scaled.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"
    NOTE="Blackwell世代のみNVFP4が本当に速い。32GBに収めるためテキストエンコーダを小さくします。" ;;
  pro6000mig48|rtxpro6000|pro6000)
    case "$GPU" in
      pro6000mig48) GPU_LABEL="PRO 6000 MIG 48GB (Blackwell)" ;;
      *)            GPU_LABEL="RTX PRO 6000 96GB (Blackwell)" ;;
    esac
    DIFFUSION="minimax_h3_fl2va_pruned_fp8_scaled.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_fp8_scaled.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"
    NOTE="Blackwell世代。NVFP4が使えるうえVRAMにも余裕があります。" ;;
  4090)
    GPU_LABEL="RTX 4090 24GB (Ada)"
    DIFFUSION="minimax_h3_fl2va_pruned_fp8_scaled.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_fp8_scaled.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_int8_convrot.safetensors"
    NOTE="24GBではVRAMに収まりきらず、システムRAMへの退避が多く発生します。遅くなります。" ;;
  h100)
    GPU_LABEL="H100 SXM/PCIe 80GB (Hopper)"
    DIFFUSION="minimax_h3_fl2va_pruned_bf16.safetensors"
    DIFFUSION_REF="minimax_h3_ref2va_pruned_bf16.safetensors"
    TEXT_ENCODER="qwen3vl_32b_minimax_h3_int8_convrot.safetensors"
    NOTE="80GBあるので拡散モデルはBF16(量子化なし)。品質比較の基準として使えます。" ;;
  "") die "--gpu を指定してください
   Ampere    : a40 / a6000 / a100
   Ada       : l40s / rtx6000ada / 4090
   Blackwell : 5090 / rtxpro4500 / pro6000mig48 / rtxpro6000
   Hopper    : h100" ;;
  *)  die "--gpu の値が不正です: $GPU  (--help で一覧)" ;;
esac

VIDEO_VAE="minimax_h3_video_vae_fp16.safetensors"
AUDIO_VAE="minimax_h3_audio_vae_fp32.safetensors"   # ← 音声用。省くと無音になります

# ------------------------------------------------------------------ 事前チェック
log "環境を確認します"
[ -d "$WORKSPACE" ] || die "$WORKSPACE がありません。Network VolumeがPodに接続されているか確認してください。"

MOUNT_INFO="$(df -h "$WORKSPACE" 2>/dev/null | tail -1 || true)"
if ! mountpoint -q "$WORKSPACE" 2>/dev/null; then
  warn "$WORKSPACE が独立したマウントに見えません。"
  warn "Network Volumeが未接続だと、Podを消したときに全部消えます。"
  warn "RunPodのPod設定で Network Volume が指定されているか確認してください。"
fi
echo "   空き容量: $MOUNT_INFO"

command -v python3 >/dev/null || die "python3 が見つかりません"
command -v git     >/dev/null || die "git が見つかりません"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null || warn "nvidia-smi が使えません(GPUなし?)"

# ------------------------------------------------------------------ 計画を表示
cat <<PLAN

────────────────────────────────────────────────────────────
 これから行うこと
────────────────────────────────────────────────────────────
 GPU構成      : $GPU_LABEL
 補足         : $NOTE
 インストール先: $COMFY_DIR   ← Network Volume の中(消えません)

 ダウンロードするモデル (リポジトリ: $REPO)
   diffusion_models/  $DIFFUSION
$( [ "$WITH_REF2VA" = 1 ] && echo "   diffusion_models/  $DIFFUSION_REF" )
   text_encoders/     $TEXT_ENCODER
   vae/               $VIDEO_VAE
   vae/               $AUDIO_VAE   (音声用・必須)

 ※ 合計で数十GBあります。初回は時間がかかりますが、
   Network Volume に置くので【この作業は最初の1回だけ】です。
 ※ 途中で止まっても、同じコマンドをもう一度実行すれば続きから再開します。
────────────────────────────────────────────────────────────

PLAN

if [ "$ASSUME_YES" != 1 ] && [ "$DRY_RUN" != 1 ]; then
  read -r -p "この内容で進めますか? [y/N] " reply
  case "$reply" in [yY]*) ;; *) echo "中止しました。"; exit 0 ;; esac
fi

# ------------------------------------------------------------------ ComfyUI
if [ -d "$COMFY_DIR/.git" ]; then
  ok "ComfyUI は既にあります → 最新版に更新します"
  run "git -C '$COMFY_DIR' pull --ff-only" || warn "更新に失敗しました(そのまま進みます)"
else
  log "ComfyUI を取得します"
  run "git clone https://github.com/comfyanonymous/ComfyUI '$COMFY_DIR'"
fi

log "ComfyUI の依存関係をインストールします"
run "python3 -m pip install --upgrade pip"
run "python3 -m pip install -r '$COMFY_DIR/requirements.txt'"
run "python3 -m pip install --upgrade 'huggingface_hub[cli]'"

# H3のネイティブ対応は ComfyUI 0.30.0 以降
if [ "$DRY_RUN" != 1 ]; then
  CV="$(git -C "$COMFY_DIR" describe --tags --abbrev=0 2>/dev/null || echo unknown)"
  echo "   ComfyUI バージョン: $CV  (H3には v0.30.0 以降が必要)"
fi

# ------------------------------------------------------------------ モデル取得
DL() {  # DL <サブフォルダ> <ファイル名>
  local sub="$1" file="$2" dest="$COMFY_DIR/models/$1"
  run "mkdir -p '$dest'"
  if [ -s "$dest/$file" ]; then
    ok "取得済み: $sub/$file"; return 0
  fi
  log "ダウンロード: $sub/$file"
  local cli="hf"; command -v hf >/dev/null 2>&1 || cli="huggingface-cli"
  local tmp="$COMFY_DIR/models/_hf_tmp" got=""
  # リポジトリの置き方が2通りあるので、両方試します
  for path in "split_files/$sub/$file" "$sub/$file"; do
    if run "$cli download '$REPO' '$path' --local-dir '$tmp'"; then got="$path"; break; fi
    warn "この場所にはありませんでした: $path (次を試します)"
  done
  [ "$DRY_RUN" = 1 ] && return 0
  [ -n "$got" ] || die "ダウンロードに失敗: $file
   → 通信かディスク容量を確認して、同じコマンドをもう一度実行してください。
   → 手動で確認する場合: https://huggingface.co/$REPO/tree/main"
  run "mv '$tmp/$got' '$dest/$file'"
  ok "完了: $sub/$file"
}

DL diffusion_models "$DIFFUSION"
if [ "$WITH_REF2VA" = 1 ]; then DL diffusion_models "$DIFFUSION_REF"; fi
DL text_encoders   "$TEXT_ENCODER"
DL vae             "$VIDEO_VAE"
DL vae             "$AUDIO_VAE"
run "rm -rf '$COMFY_DIR/models/_hf_tmp'"

# ------------------------------------------------------------ Sage Attention
# 生成速度がおよそ2倍になります(=料金が半分)。品質の劣化はごくわずか。
if [ "$SKIP_SAGE" != 1 ]; then
  log "Sage Attention を入れます(生成速度が約2倍になります)"
  if ! run "python3 -m pip install sageattention"; then
    warn "Sage Attention のインストールに失敗しました。"
    warn "H3自体は問題なく動きます。速度が2倍にならないだけなので、先に進んで大丈夫です。"
  fi
fi

# ------------------------------------------------------------------ 起動用
cat > "$WORKSPACE/start-comfyui.sh" <<'LAUNCH'
#!/usr/bin/env bash
# ComfyUI を起動します。Podを立てるたびに、これを実行するだけです。
set -euo pipefail
cd /workspace/ComfyUI
exec python3 main.py --listen 0.0.0.0 --port 8188 --use-sage-attention
LAUNCH
run "chmod +x '$WORKSPACE/start-comfyui.sh'"

cat <<DONE

────────────────────────────────────────────────────────────
 ✅ セットアップ完了
────────────────────────────────────────────────────────────
 次にやること:

   bash /workspace/start-comfyui.sh

 起動したら RunPod の「Connect」から 8188 番ポートを開いてください。
 ComfyUI の Video テンプレートに MiniMax H3 が入っています。

 【次回以降】
 Podを立て直しても、モデルは Network Volume に残っています。
 上の start-comfyui.sh を実行するだけで、2分ほどで作業を再開できます。
 このセットアップをもう一度やる必要はありません。

 ⚠️ Sage Attention でエラーが出て起動しない場合は、
    start-comfyui.sh の末尾 --use-sage-attention を消してください。
────────────────────────────────────────────────────────────

DONE
