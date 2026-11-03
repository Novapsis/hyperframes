"""Original cinematic score + SFX (deterministic)."""
import numpy as np, wave, os
SR = 48000; DUR = 76.2; N = int(SR * DUR); t = np.arange(N) / SR
rng = np.random.default_rng(9); HERE = os.path.dirname(__file__)
def write(path, L, R):
    x = np.clip(np.stack([L, R], 1), -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype("<i2").tobytes())
def midi(m): return 440 * 2 ** ((m - 69) / 12)
def env(a, b, f=1.5): return np.clip((t - a) / f, 0, 1) * np.clip((b - t) / f, 0, 1)
L = np.zeros(N); R = np.zeros(N)
def pad(a, b, notes, amp):
    e = env(a, b, 1.2) * amp
    for i, m in enumerate(notes):
        f = midi(m); d = 1 + 0.003 * (i - 1)
        L[:] += e * np.sin(2*np.pi*f*d*t) * (0.85 + 0.15*np.sin(2*np.pi*0.1*t + i))
        R[:] += e * np.sin(2*np.pi*f/d*t + 0.5) * (0.85 + 0.15*np.sin(2*np.pi*0.13*t + i))
pad(0.3, 20.4, [38, 45, 50, 53], 0.022)       # Dm tension
pad(20.2, 30.6, [34, 41, 46, 49], 0.02)       # Bbm — loss
pad(30.4, 51.4, [41, 48, 53, 57, 60], 0.02)   # F — discovery
pad(51.2, 64.7, [40, 47, 52, 55], 0.018)      # Em — caution
pad(64.5, 76.2, [36, 43, 48, 52, 55, 59], 0.024)  # Cmaj7 — resolution
def kick(at, amp):
    i0 = int(at*SR); n = min(int(0.4*SR), N - i0); tt = np.arange(n)/SR
    k = np.sin(2*np.pi*np.cumsum(45 + 80*np.exp(-tt*25))/SR) * np.exp(-tt*7) * amp; L[i0:i0+n] += k; R[i0:i0+n] += k
def tick(at, amp, f=2400):
    i0 = int(at*SR); n = min(int(0.05*SR), N - i0); tt = np.arange(n)/SR
    s = np.sin(2*np.pi*f*tt) * np.exp(-tt*120) * amp; L[i0:i0+n] += s; R[i0:i0+n] += s
beat = 60/96
for a, b, amp in [(6.5, 20.2, 0.14), (30.6, 51.2, 0.1), (64.8, 74.5, 0.12)]:
    x = a
    while x < b: kick(x, amp); tick(x + beat/2, 0.03); x += beat
x = 14.4
while x < 17.4: tick(x, 0.02 + 0.03*(x-14.4)/3, 3000); x += 0.125   # riser
fade = np.clip((DUR - t)/1.5, 0, 1) * np.clip(t/0.3, 0, 1); L *= fade; R *= fade
pk = max(abs(L).max(), abs(R).max()); write(os.path.join(HERE, "../assets/audio/music.wav"), L/pk*0.5, R/pk*0.5)
L = np.zeros(N); R = np.zeros(N)
def add(at, s):
    i0 = int(at*SR); n = min(len(s), N - i0)
    if n > 0: L[i0:i0+n] += s[:n]; R[i0:i0+n] += s[:n]
def impact(amp=0.7):
    n = int(1.6*SR); tt = np.arange(n)/SR
    return (np.sin(2*np.pi*np.cumsum(35 + 90*np.exp(-tt*14))/SR)*np.exp(-tt*3) + rng.standard_normal(n)*np.exp(-tt*30)*0.3) * amp
def paper(d=0.5, amp=0.12):
    n = int(d*SR); tt = np.arange(n)/SR; no = rng.standard_normal(n); hi = no - np.convolve(no, np.ones(8)/8, "same")
    return hi * np.abs(np.sin(2*np.pi*9*tt)) * np.sin(np.pi*tt/d) * amp
def metal(f=2600, amp=0.1):
    n = int(0.9*SR); tt = np.arange(n)/SR
    return (np.sin(2*np.pi*f*tt) + 0.6*np.sin(2*np.pi*f*2.76*tt) + 0.4*np.sin(2*np.pi*f*5.4*tt)) * np.exp(-tt*6) * amp
def whoosh(d=0.9, amp=0.18):
    n = int(d*SR); tt = np.arange(n)/SR; no = rng.standard_normal(n); lo = np.convolve(no, np.ones(20)/20, "same")
    return lo * np.sin(np.pi*tt/d)**2 * amp * 4
def blip(f=1200, amp=0.07):
    n = int(0.12*SR); tt = np.arange(n)/SR; return np.sin(2*np.pi*f*tt) * np.exp(-tt*35) * amp
def drop(amp=0.4):
    n = int(2.0*SR); tt = np.arange(n)/SR; return np.sin(2*np.pi*np.cumsum(120*np.exp(-tt*1.2)+30)/SR) * np.exp(-tt*1.5) * amp
add(0.18, impact(0.8)); add(2.86, blip(900, 0.08)); add(5.85, whoosh(0.8)); add(6.55, impact(0.35))
for x in [9.5, 9.62, 9.74]: add(x, paper())
add(10.34, metal(2400, 0.06)); add(12.7, blip(1500))
add(14.6, paper(0.4, 0.1))
for i in range(12): add(15.5 + i*0.08, paper(0.25, 0.07))
add(17.3, impact(0.45)); add(20.2, whoosh(0.8))
add(23.3, drop(0.35)); add(25.6, impact(0.75))
add(30.4, whoosh(1.0)); add(34.5, metal(2900, 0.12)); add(35.55, metal(3300, 0.12))
for x in [43.1, 44.0, 45.0, 46.6]: add(x, blip(1300, 0.06))
add(52.0, blip(700, 0.12)); add(52.25, blip(700, 0.12))
for x in [56.78, 57.8, 58.86]: add(x, blip(500, 0.08))
add(60.15, metal(2000, 0.12)); add(62.56, blip(1800, 0.06)); add(63.02, blip(600, 0.06))
add(64.5, whoosh(1.0)); add(72.8, metal(1760, 0.1)); add(72.8, impact(0.25))
write(os.path.join(HERE, "../assets/sound-effects/sfx.wav"), L*0.9, R*0.9); print("ok")
