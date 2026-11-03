#!/usr/bin/env bash
# Render final + mezcla a -14 LUFS con limitador. Uso: bash tools/finalizar.sh producciones/<nombre> <Nombre_Final.mp4>
set -e
DIR=$1; OUT=$2; cd "$DIR"
python3 build/build.py
npx --yes hyperframes lint
npx --yes hyperframes render -o renders/raw.mp4 -f 30 -q delivery
ffmpeg -y -hide_banner -loglevel error -i renders/raw.mp4 -c:v copy \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,alimiter=limit=0.84:level=false" \
  -ar 48000 -ac 2 -c:a aac -b:a 256k -movflags +faststart "$OUT"
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)"
echo "Listo: $DIR/$OUT"
