#!/usr/bin/env bash
# Novapsis Studio — instalación local (macOS / Linux). Uso: bash setup.sh
set -e
ok(){ echo "  ✓ $1"; }; bad(){ echo "  ✗ $1"; MISSING=1; }
echo "Comprobando requisitos…"
command -v node >/dev/null && ok "Node $(node -v)" || bad "Node.js 22+  →  https://nodejs.org"
command -v ffmpeg >/dev/null && ok "FFmpeg" || bad "FFmpeg  →  macOS: brew install ffmpeg | Ubuntu: sudo apt install ffmpeg"
command -v python3 >/dev/null && ok "Python $(python3 -V | cut -d' ' -f2)" || bad "Python 3"
[ -n "$MISSING" ] && { echo "Instala lo que falta y vuelve a ejecutar."; exit 1; }
# Entorno aislado (.venv) con Python 3.12: faster-whisper aún no soporta 3.13+
PY=""
for c in python3.12 python3.11 python3.10 /opt/homebrew/bin/python3.12; do command -v $c >/dev/null && { PY=$c; break; }; done
if [ -z "$PY" ]; then
  if command -v brew >/dev/null; then echo "Instalando Python 3.12 (solo para este kit)…"; brew install python@3.12; PY=$(brew --prefix python@3.12)/bin/python3.12
  else echo "  ✗ Falta Python 3.12 (instálalo y repite)"; exit 1; fi
fi
echo "Creando entorno .venv con $($PY -V)…"
$PY -m venv .venv
.venv/bin/python -m pip install -q --upgrade pip
.venv/bin/python -m pip install -q faster-whisper numpy pillow
echo "Descargando modelo de transcripción (Whisper small, ~480 MB, solo la primera vez)…"
.venv/bin/python tools/transcribe.py --warmup
echo "Comprobando HyperFrames…"
npx --yes hyperframes@latest doctor || true
echo; echo "Listo. Crea tu primer video:  bash tools/nuevo.sh mi-video pizarra ruta/al/audio.wav"
