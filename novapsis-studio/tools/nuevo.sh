#!/usr/bin/env bash
# Crea un proyecto nuevo desde una plantilla. Uso: bash tools/nuevo.sh <nombre> <pizarra|noticia-cinematica> <audio.wav>
set -e
NAME=$1; TPL=$2; AUDIO=$3
[ -z "$NAME" ] || [ -z "$TPL" ] || [ -z "$AUDIO" ] && { echo "Uso: bash tools/nuevo.sh <nombre> <pizarra|noticia-cinematica> <audio.wav>"; exit 1; }
DIR="producciones/$NAME"; [ -e "$DIR" ] && { echo "Ya existe $DIR"; exit 1; }
cp -R "templates/$TPL" "$DIR"
mkdir -p "$DIR/assets/audio" "$DIR/assets/sound-effects" "$DIR/review" "$DIR/renders"
cp "$AUDIO" "$DIR/assets/audio/narracion_original.wav"
ffmpeg -y -loglevel error -i "$AUDIO" -ar 48000 -ac 1 "$DIR/assets/audio/narracion.wav"
sed -i.bak "s/\"id\": \"[^\"]*\"/\"id\": \"$NAME\"/; s/\"name\": \"[^\"]*\"/\"name\": \"$NAME\"/" "$DIR/meta.json" && rm -f "$DIR/meta.json.bak"
python3 tools/transcribe.py "$DIR/assets/audio/narracion.wav" "$DIR/build/words.json"
echo; echo "Proyecto creado en $DIR"
echo "Duración: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$DIR/assets/audio/narracion.wav") s"
echo "Ahora abre Claude Code en esta carpeta y pídele el video con tu prompt."
