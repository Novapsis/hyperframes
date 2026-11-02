"""Original synthesized score + SFX (deterministic)."""
import numpy as np, wave, json, os
SR = 48000; DUR = 98.6; N = int(SR * DUR); t = np.arange(N) / SR
rng = np.random.default_rng(5); HERE = os.path.dirname(__file__)
OPS = json.load(open(os.path.join(HERE, "ops.json")))
def write(path, L, R):
    x = np.clip(np.stack([L, R], 1), -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype("<i2").tobytes())
def midi(m): return 440 * 2 ** ((m - 69) / 12)
L = np.zeros(N); R = np.zeros(N)
def note(at, m, amp, dur=1.8, pan=0.0):
    i0 = int(at * SR); n = min(int(dur * SR), N - i0)
    if n <= 0: return
    tt = np.arange(n) / SR; f = midi(m)
    s = (np.sin(2*np.pi*f*tt) + 0.35*np.sin(2*np.pi*2*f*tt) + 0.1*np.sin(2*np.pi*3*f*tt)) * np.exp(-tt * 2.8) * np.minimum(1, tt / 0.004)
    L[i0:i0+n] += s * amp * (1 - pan); R[i0:i0+n] += s * amp * (1 + pan)
beat = 60 / 100
prog = [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 67]]  # Cmaj7 Am7 Fmaj7 G
def section(a, b, amp, step=0.5, arp=True):
    x = a; k = 0
    while x < b:
        ch = prog[(k // int(4 / step)) % 4]
        if k % int(4 / step) == 0:
            for m in ch[:3]: note(x, m - 12, amp * 0.55, 3.0)
        if arp: note(x, ch[k % 4] + 12, amp * 0.45, 1.2, pan=0.3 if k % 2 else -0.3)
        x += beat * step; k += 1
section(0.2, 22.4, 0.045)
note(22.6, 45, 0.04, 4.0)
section(26.0, 55.0, 0.05)
section(55.0, 63.0, 0.06, step=0.25)
section(63.0, 86.9, 0.05)
section(86.9, 97.6, 0.055)
fade = np.clip((DUR - t) / 1.5, 0, 1); L *= fade; R *= fade
pk = max(abs(L).max(), abs(R).max()); write(os.path.join(HERE, "../assets/audio/music.wav"), L/pk*0.5, R/pk*0.5)
L = np.zeros(N); R = np.zeros(N)
def add(at, s):
    i0 = int(at * SR); n = min(len(s), N - i0)
    if n > 0: L[i0:i0+n] += s[:n]; R[i0:i0+n] += s[:n]
def scribble(d):
    n = int(d * SR); tt = np.arange(n) / SR; no = rng.standard_normal(n); hi = no - np.convolve(no, np.ones(6)/6, "same")
    return hi * (0.6 + 0.4*np.abs(np.sin(2*np.pi*7*tt))) * np.minimum(1, tt/0.02) * np.minimum(1, (d-tt)/0.03) * 0.045
def tone(f, d, amp, dec):
    n = int(d * SR); tt = np.arange(n) / SR; return np.sin(2*np.pi*f*tt) * np.exp(-tt*dec) * amp
def ping(amp=0.1): return tone(1760, 0.25, amp, 18) + tone(2637, 0.25, amp*0.6, 22)
def click(amp=0.08): n = int(0.04*SR); tt = np.arange(n)/SR; return (rng.standard_normal(n)*0.5 + np.sin(2*np.pi*1500*tt)) * np.exp(-tt*220) * amp
def chime(m, amp): return tone(midi(m), 1.2, amp, 3) + tone(midi(m)*1.5, 1.2, amp*0.5, 4)
def bell(): return sum(tone(f, 1.6, 0.07, 3) for f in (1320, 1980, 2640))
def whoosh(d=1.0, amp=0.06):
    n = int(d*SR); tt = np.arange(n)/SR; no = rng.standard_normal(n); lo = np.convolve(no, np.ones(30)/30, "same"); return lo * np.sin(np.pi*tt/d)**2 * amp * 3
for a, b in OPS: add(a - 0.02, click(0.04)); add(a, scribble(b - a))
add(7.3, bell()); add(7.25, whoosh(0.7)); add(19.15, whoosh(0.7))
for x in [15.5, 15.82, 16.14, 16.46, 16.78]: add(x, ping(0.09))
for x in [20.55, 33.6, 38.95, 42.3, 52.6, 57.6, 58.0, 58.4, 58.8, 84.5, 85.2, 85.9]: add(x, ping(0.07))
for x in [35.75, 42.85]: add(x, click(0.1))
for x in [37.35, 39.95, 44.5, 53.4, 58.9, 59.5, 60.0, 60.5]: add(x, chime(84, 0.06))
for x in [41.45, 67.75, 74.55, 75.85]: add(x, chime(79, 0.09))
add(52.15, tone(2200, 0.12, 0.08, 30))
add(93.55, chime(84, 0.1)); add(94.5, chime(91, 0.07))
write(os.path.join(HERE, "../assets/sound-effects/sfx.wav"), L*0.9, R*0.9); print("ok")
