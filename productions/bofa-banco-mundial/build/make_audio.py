import numpy as np, wave, os
SR=48000; DUR=26.9; N=int(SR*DUR); t=np.arange(N)/SR; rng=np.random.default_rng(4); HERE=os.path.dirname(__file__)
def write(p,L,R):
    x=np.clip(np.stack([L,R],1),-1,1)
    with wave.open(p,"wb") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype("<i2").tobytes())
def midi(m): return 440*2**((m-69)/12)
def env(a,b,f=0.8): return np.clip((t-a)/f,0,1)*np.clip((b-t)/f,0,1)
L=np.zeros(N); R=np.zeros(N)
for a,b,notes,amp in [(0,15.3,[38,45,50,53],0.022),(15.2,21.7,[36,43,48,51],0.02),(21.6,26.7,[38,45,49,56],0.026)]:
    e=env(a,b)*amp
    for i,m in enumerate(notes):
        f=midi(m); L+=e*np.sin(2*np.pi*f*1.003*t+i); R+=e*np.sin(2*np.pi*f/1.003*t)
def kick(at,amp):
    i0=int(at*SR); n=min(int(0.35*SR),N-i0); tt=np.arange(n)/SR; k=np.sin(2*np.pi*np.cumsum(45+80*np.exp(-tt*25))/SR)*np.exp(-tt*8)*amp; L[i0:i0+n]+=k; R[i0:i0+n]+=k
def hat(at,amp):
    i0=int(at*SR); n=min(int(0.04*SR),N-i0); tt=np.arange(n)/SR; s=rng.standard_normal(n)*np.exp(-tt*150)*amp; L[i0:i0+n]+=s; R[i0:i0+n]+=s
b=60/112; x=0.9
while x<21.4: kick(x,0.12); hat(x+b/2,0.02); hat(x+b*0.75,0.012); x+=b
fade=np.clip((26.65-t)/0.15,0,1); L*=fade; R*=fade
pk=max(abs(L).max(),abs(R).max()); write(os.path.join(HERE,"../assets/audio/music.wav"),L/pk*0.5,R/pk*0.5)
L=np.zeros(N); R=np.zeros(N)
def add(at,s):
    i0=int(at*SR); n=min(len(s),N-i0)
    if n>0: L[i0:i0+n]+=s[:n]; R[i0:i0+n]+=s[:n]
def impact(a=0.7):
    n=int(1.4*SR); tt=np.arange(n)/SR; return (np.sin(2*np.pi*np.cumsum(35+90*np.exp(-tt*14))/SR)*np.exp(-tt*3)+rng.standard_normal(n)*np.exp(-tt*30)*0.3)*a
def whoosh(d=0.8,a=0.05):
    n=int(d*SR); tt=np.arange(n)/SR; no=rng.standard_normal(n); lo=np.convolve(no,np.ones(20)/20,"same"); return lo*np.sin(np.pi*tt/d)**2*a*4
def glass(f=2800,a=0.08):
    n=int(1.0*SR); tt=np.arange(n)/SR; return (np.sin(2*np.pi*f*tt)+0.5*np.sin(2*np.pi*f*2.3*tt))*np.exp(-tt*5)*a
def paper(d=0.3,a=0.08):
    n=int(d*SR); tt=np.arange(n)/SR; no=rng.standard_normal(n); hi=no-np.convolve(no,np.ones(8)/8,"same"); return hi*np.sin(np.pi*tt/d)*a
def blip(f=1200,a=0.07):
    n=int(0.12*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.exp(-tt*35)*a
add(0.02,impact(0.7)); add(0.1,blip(900)); add(1.0,whoosh(1.2)); add(1.5,whoosh(1.0,0.035))
add(1.48,glass(2600)); add(2.6,glass(3100)); add(4.96,blip(1400))
add(6.5,whoosh(0.8)); add(7.14,impact(0.15))
for i in range(10): add(8.3+i*0.06,paper())
add(10.6,whoosh(1.4,0.03)); add(11.8,glass(2200,0.06)); add(14.9,whoosh(0.8))
add(17.85,impact(0.18)); add(20.5,glass(1800,0.08)); add(21.45,whoosh(0.7))
add(22.95,impact(0.6)); add(22.95,glass(1500,0.06))
write(os.path.join(HERE,"../assets/sound-effects/sfx.wav"),L*0.9,R*0.9); print("ok")
