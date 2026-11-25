#!/usr/bin/env bash
set -euo pipefail

runner_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
index_tts_root=/workspace/scratch/s06-index-tts2
export PYTHONPATH="$index_tts_root/official"
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 TOKENIZERS_PARALLELISM=false
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
export XDG_CACHE_HOME="$index_tts_root/cache" MPLCONFIGDIR="$index_tts_root/matplotlib" NUMBA_CACHE_DIR="$index_tts_root/numba"
cd -- "$index_tts_root/official"
exec "$index_tts_root/.venv/bin/python" -Bu "$runner_dir/run.py" "$@"
