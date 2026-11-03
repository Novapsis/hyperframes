"""Transcribe un audio en español con tiempos por palabra → build/words.json
Uso: python3 tools/transcribe.py <audio.wav> <salida.json>   |   --warmup (solo descarga el modelo)"""
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
model = WhisperModel("small", device="auto", compute_type="int8")
if sys.argv[1] == "--warmup":
    print("Modelo listo."); sys.exit(0)
src, out = sys.argv[1], sys.argv[2]
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-ar", "16000", "-ac", "1", "-f", "f32le", "-"], capture_output=True, check=True).stdout
segs, _ = model.transcribe(np.frombuffer(raw, np.float32), language="es", word_timestamps=True, beam_size=5)
words = []
for s in segs:
    print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text}")
    words += [(round(w.start, 2), round(w.end, 2), w.word.strip()) for w in s.words]
json.dump(words, open(out, "w"), ensure_ascii=False)
print(f"{len(words)} palabras → {out}")
