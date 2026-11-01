"""Synthesizes the music bed and SFX (original, license-free) for the reel.
Deterministic: fixed seed. Output: assets/audio/music.wav, assets/sound-effects/sfx.wav
"""
import numpy as np, wave, json, os

SR = 48000
DUR = 49.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)
HERE = os.path.dirname(__file__)
TIMES = json.load(open(os.path.join(HERE, "times.json")))


def write(path, x):
    x = np.clip(x, -1, 1)
    st = (np.stack([x[0], x[1]], 1) * 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())


def env_seg(a, b, fade=1.5):
    e = np.clip((t - a) / fade, 0, 1) * np.clip((b - t) / fade, 0, 1)
    return e


def midi(m):
    return 440 * 2 ** ((m - 69) / 12)


# ---------- MUSIC ----------
L = np.zeros(N); R = np.zeros(N)
BPM = 104; beat = 60 / BPM

# Pad chords by section (midi notes)
sections = [
    (0.0, 6.4, [45, 52, 57, 60, 64], 0.8),      # Am - hook
    (6.4, 18.2, [53, 60, 64, 67, 72], 0.9),     # Fmaj7 - inventory / connection
    (18.2, 25.6, [48, 55, 64, 67, 71], 0.9),    # Cmaj7 - demo
    (25.6, 27.6, [50, 57, 62, 65, 69], 0.5),    # Dm9 - night
    (27.6, 37.2, [53, 60, 64, 67, 72], 0.9),    # Fmaj7 - differentiation / benefit
    (37.2, 49.0, [48, 55, 64, 67, 74], 1.0),    # Cadd9 - brand + CTA
]
for a, b, notes, amp in sections:
    e = env_seg(a - 0.6, b + 0.6, 1.2) * amp
    for i, m in enumerate(notes):
        f = midi(m)
        det = 1 + 0.0025 * (i - 2)
        sL = np.sin(2 * np.pi * f * det * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)
        sR = np.sin(2 * np.pi * f / det * t + 0.7) + 0.25 * np.sin(2 * np.pi * 2 * f * t + 0.3)
        trem = 0.85 + 0.15 * np.sin(2 * np.pi * 0.12 * t + i)
        L += 0.018 * e * sL * trem
        R += 0.018 * e * sR * trem

# Sub kick pulse (sections with drive)
def kick(at, amp):
    i0 = int(at * SR); n = int(0.35 * SR)
    if i0 >= N: return
    n = min(n, N - i0)
    tt = np.arange(n) / SR
    f = 48 + 70 * np.exp(-tt * 30)
    ph = 2 * np.pi * np.cumsum(f) / SR
    k = np.sin(ph) * np.exp(-tt * 9) * amp
    L[i0:i0 + n] += k; R[i0:i0 + n] += k

def pluck(at, m, amp, pan=0.0):
    i0 = int(at * SR); n = int(0.5 * SR)
    if i0 >= N: return
    n = min(n, N - i0)
    tt = np.arange(n) / SR
    f = midi(m)
    p = (np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(2 * np.pi * 2 * f * tt)) * np.exp(-tt * 9) * amp
    L[i0:i0 + n] += p * (1 - pan); R[i0:i0 + n] += p * (1 + pan)

drive = [(1.0, 6.2, 0.12), (6.5, 25.5, 0.13), (27.7, 37.0, 0.15), (37.4, 47.6, 0.12)]
for a, b, amp in drive:
    x = a
    while x < b:
        kick(x, amp); x += beat

arps = [
    (6.5, 18.2, [69, 72, 76, 79], 0.03),
    (18.2, 25.5, [67, 71, 76, 79], 0.03),
    (27.7, 37.0, [72, 76, 79, 84], 0.032),
    (39.0, 47.6, [74, 79, 83, 86], 0.03),
]
for a, b, notes, amp in arps:
    x = a; k = 0
    while x < b:
        pluck(x, notes[k % 4], amp, pan=0.35 * (1 if k % 2 else -1)); x += beat / 2; k += 1

# Final resolve: fade the last second
fade = np.clip((DUR - t) / 1.4, 0, 1)
fadein = np.clip(t / 0.25, 0, 1)
L *= fade * fadein; R *= fade * fadein
peak = max(np.abs(L).max(), np.abs(R).max())
L, R = L / peak * 0.5, R / peak * 0.5
write(os.path.join(HERE, "..", "assets/audio/music.wav"), np.stack([L, R]))

# ---------- SFX ----------
L = np.zeros(N); R = np.zeros(N)

def add(at, sig):
    i0 = int(at * SR); n = min(len(sig), N - i0)
    L[i0:i0 + n] += sig[:n]; R[i0:i0 + n] += sig[:n]

def tap(amp=0.35):
    n = int(0.06 * SR); tt = np.arange(n) / SR
    return (np.sin(2 * np.pi * 2200 * tt) * 0.5 + rng.standard_normal(n) * 0.3) * np.exp(-tt * 90) * amp

def impact(amp=0.7):
    n = int(1.2 * SR); tt = np.arange(n) / SR
    f = 40 + 120 * np.exp(-tt * 18)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 4)
    shimmer = np.sin(2 * np.pi * 1760 * tt) * np.exp(-tt * 6) * 0.15
    return (body + shimmer) * amp

def whoosh(d=0.7, amp=0.22):
    n = int(d * SR); tt = np.arange(n) / SR
    noise = rng.standard_normal(n)
    # crude band-pass sweep via moving averages
    k = 12; sm = np.convolve(noise, np.ones(k) / k, "same")
    hi = noise - sm
    e = np.sin(np.pi * tt / d) ** 2
    return hi * e * amp

def chime(m=81, amp=0.18):
    n = int(1.6 * SR); tt = np.arange(n) / SR
    f = midi(m)
    return (np.sin(2 * np.pi * f * tt) + 0.5 * np.sin(2 * np.pi * f * 1.5 * tt)) * np.exp(-tt * 3) * amp

def pulse(amp=0.3):
    n = int(0.5 * SR); tt = np.arange(n) / SR
    return np.sin(2 * np.pi * 110 * tt) * np.exp(-tt * 10) * amp

add(0.02, pulse())
for x in TIMES["taps"]:
    add(x, tap())
for x in TIMES["whooshes"]:
    add(x - 0.35, whoosh())
add(TIMES["zero"] - 0.03, impact())
for x in TIMES["chimes"]:
    add(x, chime(79, 0.12))
add(TIMES["agenda"], chime(86, 0.2))
add(TIMES["logo"], impact(0.35))
for x in TIMES["msgs"]:
    add(x, chime(88, 0.08))
add(TIMES["logo"], chime(84, 0.16))
write(os.path.join(HERE, "..", "assets/sound-effects/sfx.wav"), np.stack([L, R]) * 0.9)
print("ok")
