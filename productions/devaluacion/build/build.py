"""Generates index.html + subtitulos.srt. Run: python3 build/build.py"""
import os, re, json, random
HERE = os.path.dirname(__file__)
DUR = 76.2
CAPS = [
    (0.0, 1.0, "*¡Devaluación!*"),
    (1.04, 3.8, "¿Sabías que puedes perder casi el *75 %*"),
    (3.86, 6.85, "del valor de tus ahorros sin gastar un solo bolívar?"),
    (7.28, 8.0, "Mira esto."),
    (8.5, 10.9, "En noviembre de 2025, *100 dólares*"),
    (10.96, 14.0, "equivalían a unos *22.400 bolívares*."),
    (14.46, 17.85, "Un año después, necesitas más de *89.000 bolívares*"),
    (17.9, 19.9, "para comprar esos mismos 100 dólares."),
    (20.4, 22.7, "Y si hubieras guardado los bolívares,"),
    (22.76, 25.5, "hoy apenas representarían unos *25 dólares*."),
    (25.58, 30.1, "Casi el *75 %* de su valor frente al dólar desapareció."),
    (30.66, 33.5, "Entonces, ¿cómo puedes reducir ese riesgo?"),
    (33.94, 36.4, "Aquí entran *USDT y USDC*."),
    (36.78, 41.4, "Son criptomonedas diseñadas para mantener un valor cercano al dólar estadounidense."),
    (41.84, 45.2, "Puedes adquirirlas con bolívares mediante servicios compatibles"),
    (45.26, 47.6, "y conservarlas en una billetera digital."),
    (48.08, 51.4, "Así puedes *reducir tu exposición* a la devaluación del bolívar."),
    (51.46, 53.0, "Pero atención,"),
    (53.1, 56.1, "no son dólares bancarios ni están *libres de riesgos*."),
    (56.36, 59.9, "Existen comisiones, estafas y posibles pérdidas de valor."),
    (60.06, 61.5, "Y *Bitcoin* es diferente."),
    (61.88, 64.4, "Su precio puede subir o bajar considerablemente."),
    (64.8, 69.1, "Recuerda, proteger tus ahorros no significa buscar ganancias milagrosas."),
    (69.28, 73.55, "Significa *conocer tus opciones* y aprender a tomar mejores decisiones."),
]
t = open(os.path.join(HERE, "index.template.html"), encoding="utf-8").read()
t = t.replace("{{TITLE}}", "".join(f'<span class="ltr" style="display:inline-block">{c}</span>' for c in "DEVALUACIÓN"))
rnd = random.Random(3); parts = []
while len(parts) < 70:
    x, y = rnd.uniform(110, 950), rnd.uniform(440, 1120)
    if 250 < x < 830 and 600 < y < 900: continue
    w = rnd.choice([30, 36, 42]); c = rnd.choice(["#b4605a", "#8a3b3b", "#d9877e", "#6b2b2b"])
    parts.append(f'<div class="pt a" style="left:{x:.0f}px;top:{y:.0f}px;width:{w}px;height:{w*0.45:.0f}px;background:{c};border-radius:2px;transform:rotate({rnd.uniform(-40,40):.0f}deg)"></div>')
t = t.replace("{{PARTS}}", "".join(parts))
stk = []
back = [(200, 150), (330, 170), (460, 140), (590, 180), (720, 160), (850, 150)]
front = [(140, 130), (265, 170), (390, 150), (515, 160), (640, 150), (765, 175), (890, 140)]
for i, (x, h) in enumerate(back):
    stk.append(f'<div class="stk s1" style="left:{x-60}px;top:{1150-h}px;height:{h}px;opacity:0.8"><div class="f"></div><div class="tp">Bs</div></div>')
for i, (x, h) in enumerate(front):
    cls = "s0" if i in (2, 3, 4) else "s1"
    stk.append(f'<div class="stk {cls}" style="left:{x-60}px;top:{1220-h}px;height:{h}px"><div class="f"></div><div class="tp">Bs</div></div>')
t = t.replace("{{STACKS}}", "".join(stk))
caps = []
for i, (a, b, x) in enumerate(CAPS, 1):
    inner = re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', x)
    caps.append(f'      <div id="cap{i}" class="clip cap" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="5"><span class="cap-in">{inner}</span></div>')
t = t.replace("{{CAPTIONS}}", "\n".join(caps)).replace("{{S7DUR}}", str(round(DUR - 64.6, 2))).replace("{{DUR}}", str(DUR))
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(t)
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
open(os.path.join(HERE, "..", "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{x.replace('*','')}\n" for i, (a, b, x) in enumerate(CAPS, 1)))
print("ok")
