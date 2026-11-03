#!/usr/bin/env bash
# Novapsis Studio — instalación local (macOS / Linux). Uso: bash setup.sh
set -e
ok(){ echo "  ✓ $1"; }; bad(){ echo "  ✗ $1"; MISSING=1; }
echo "Comprobando requisitos…"
command -v node >/dev/null && ok "Node $(node -v)" || bad "Node.js 22+  →  https://nodejs.org"
command -v ffmpeg >/dev/null && ok "FFmpeg" || bad "FFmpeg  →  macOS: brew install ffmpeg | Ubuntu: sudo apt install ffmpeg"
command -v python3 >/dev/null && ok "Python $(python3 -V | cut -d' ' -f2)" || bad "Python 3.10+"
[ -n "$MISSING" ] && { echo "Instala lo que falta y vuelve a ejecutar."; exit 1; }
echo "Instalando dependencias de Python (transcripción y audio)…"
python3 -m pip install --user -q faster-whisper numpy pillow
echo "Descargando modelo de transcripción (Whisper small, ~480 MB, solo la primera vez)…"
python3 tools/transcribe.py --warmup
echo "Comprobando HyperFrames…"
npx --yes hyperframes@latest doctor || true
echo; echo "Listo. Crea tu primer video:  bash tools/nuevo.sh mi-video pizarra ruta/al/audio.wav"
