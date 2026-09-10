#!/usr/bin/env python3
"""H3のモデルを、リポジトリ内の置き場所を自動で探してダウンロードする。

リポジトリのフォルダ構成が split_files/ 配下かどうか等を推測せずに、
ファイル名で実物を探してから取得するので、構成が変わっても壊れない。
"""
import os, shutil, sys
from huggingface_hub import list_repo_files, hf_hub_download

REPO = "Comfy-Org/MiniMax-H3"
MODELS = os.environ.get("COMFY_MODELS", "/workspace/ComfyUI/models")

# GPU世代ごとの構成（環境変数 H3_PROFILE で切替）
PROFILES = {
    "h100":         ("minimax_h3_fl2va_pruned_bf16.safetensors",         "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
    "a100":         ("minimax_h3_fl2va_pruned_bf16.safetensors",         "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
    "a40":          ("minimax_h3_fl2va_pruned_int8_convrot.safetensors", "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
    "a6000":        ("minimax_h3_fl2va_pruned_int8_convrot.safetensors", "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
    "l40s":         ("minimax_h3_fl2va_pruned_fp8_scaled.safetensors",   "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
    "rtx6000ada":   ("minimax_h3_fl2va_pruned_fp8_scaled.safetensors",   "qwen3vl_32b_minimax_h3_int8_convrot.safetensors"),
    "rtxpro4500":   ("minimax_h3_fl2va_pruned_fp8_scaled.safetensors",   "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"),
    "rtxpro6000":   ("minimax_h3_fl2va_pruned_fp8_scaled.safetensors",   "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"),
}
VAES = ["minimax_h3_video_vae_fp16.safetensors", "minimax_h3_audio_vae_fp32.safetensors"]

profile = os.environ.get("H3_PROFILE", "h100")
if profile not in PROFILES:
    sys.exit(f"H3_PROFILE が不正です: {profile}\n選べる値: {', '.join(PROFILES)}")
diffusion, text_encoder = PROFILES[profile]

wanted = [("diffusion_models", diffusion), ("text_encoders", text_encoder)] + [("vae", v) for v in VAES]

print(f"構成: {profile}")
print("リポジトリのファイル一覧を取得中...")
files = list_repo_files(REPO)

for subdir, name in wanted:
    dest_dir = os.path.join(MODELS, subdir)
    dest = os.path.join(dest_dir, name)
    os.makedirs(dest_dir, exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"✅ 取得済み: {subdir}/{name}")
        continue
    matches = [f for f in files if f.rsplit("/", 1)[-1] == name]
    if not matches:
        sys.exit(f"❌ リポジトリに見つかりません: {name}\n"
                 f"   実際にあるファイル名の候補:\n   " +
                 "\n   ".join(f for f in files if f.endswith(".safetensors"))[:2000])
    remote = matches[0]
    print(f"⬇️  ダウンロード: {remote}")
    path = hf_hub_download(REPO, remote)          # 中断しても続きから再開されます
    shutil.copyfile(path, dest)
    print(f"✅ 配置しました: {subdir}/{name}")

print("\n完了。models/ の中身:")
for subdir in ("diffusion_models", "text_encoders", "vae"):
    d = os.path.join(MODELS, subdir)
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            size = os.path.getsize(os.path.join(d, f)) / 1e9
            print(f"  {subdir}/{f}  ({size:.1f} GB)")
