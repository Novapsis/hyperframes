"""Original synthesized score + SFX for the whiteboard film (deterministic)."""
import numpy as np, wave, json, os
SR = 48000; DUR = 92.6; N = int(SR * DUR); t = np.arange(N) / SR
rng = np.random.default_rng(11); HERE = os.path.dirname(__file__)
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
    s = (np.sin(2*np.pi*f*tt) + 0.35*np.sin(2*np.pi*2*f*tt) + 0.12*np.sin(2*np.pi*3*f*tt)) * np.exp(-tt * 2.6) * np.minimum(1, tt / 0.004)
    L[i0:i0+n] += s * amp * (1 - pan); R[i0:i0+n] += s * amp * (1 + pan)
BPM = 92; beat = 60 / BPM
prog = [[57, 60, 64, 69], [53, 57, 60, 65], [48, 52, 55, 60], [55, 59, 62, 67]]  # Am F C G
def section(a, b, amp, arp=True):
    x = a; k = 0
    while x < b:
        ch = prog[(k // 8) % 4]
        if k % 8 == 0:
            for m in ch[:3]: note(x, m - 12, amp * 0.55, 3.2)
        if arp: note(x, ch[k % 4] + 12, amp * 0.5, 1.4, pan=0.3 if k % 2 else -0.3)
        x += beat / 2; k += 1
section(0.3, 63.8, 0.05)
# the stop: only a low sustained note, then silence-ish
note(63.9, 45, 0.05, 6.0); note(69.5, 45, 0.035, 6.0)
section(75.2, 80.4, 0.025, arp=False)
section(80.55, 91.5, 0.06)
fade = np.clip((DUR - t) / 1.5, 0, 1); L *= fade; R *= fade
pk = max(abs(L).max(), abs(R).max()); write(os.path.join(HERE, "../assets/audio/music.wav"), L / pk * 0.5, R / pk * 0.5)
# ---------- SFX ----------
L = np.zeros(N); R = np.zeros(N)
def add(at, s, pan=0.0):
    i0 = int(at * SR); n = min(len(s), N - i0)
    if n > 0: L[i0:i0+n] += s[:n] * (1 - pan); R[i0:i0+n] += s[:n] * (1 + pan)
def scribble(d):
    n = int(d * SR); tt = np.arange(n) / SR
    no = rng.standard_normal(n); hi = no - np.convolve(no, np.ones(6) / 6, "same")
    env = (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 7 * tt))) * np.minimum(1, tt / 0.02) * np.minimum(1, (d - tt) / 0.03)
    return hi * env * 0.05
def click(amp=0.12, f=1800, dec=200):
    n = int(0.05 * SR); tt = np.arange(n) / SR
    return (np.sin(2*np.pi*f*tt) * 0.6 + rng.standard_normal(n) * 0.4) * np.exp(-tt * dec) * amp
for a, b in OPS:
    add(a - 0.02, click(0.06, 900, 300)); add(a, scribble(b - a))
for x in np.arange(11.0, 17.4, 1.0): add(x, click(0.05, 2600, 260))  # clock
gt = 30.0
while gt < 63.9: add(gt, click(0.035, 1300, 220)); gt += 0.18
gaps = [63.9 + 0.18 * (1.18 ** k) * k / 2 for k in range(1, 14)]
for g in gaps:
    if g < 65.8: add(g, click(0.035 * max(0.2, 1 - (g - 63.9) / 2), 1300, 220))
gt = 80.55
while gt < 91.0: add(gt, click(0.03, 1300, 220)); gt += 0.18
def chime(m, amp):
    n = int(1.6 * SR); tt = np.arange(n) / SR; f = midi(m)
    return (np.sin(2*np.pi*f*tt) + 0.5*np.sin(2*np.pi*1.5*f*tt)) * np.exp(-tt * 3) * amp
add(80.55, chime(76, 0.12)); add(80.75, chime(83, 0.1)); add(86.35, chime(84, 0.12))
add(63.88, click(0.15, 600, 120))  # marker stops
write(os.path.join(HERE, "../assets/sound-effects/sfx.wav"), L * 0.9, R * 0.9)
print("ok")
