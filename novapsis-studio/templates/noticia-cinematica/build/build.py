"""Generates index.html + subtitulos.srt. Run: python3 build/build.py"""
import os, json
HERE = os.path.dirname(__file__)
DUR = 26.9
W = json.load(open(os.path.join(HERE, "words.json")))
DISPLAY = ["¡Atención,", "Venezuela!", "Bank", "of", "America", "y", "representantes", "del", "Banco", "Mundial", "preparan", "una", "visita", "al", "país", "esta", "semana.",
           "¿El", "objetivo?", "Explorar", "una", "posible", "reestructuración", "de", "la", "deuda", "externa", "y", "oportunidades", "de", "financiamiento", "para", "empresas", "venezolanas.",
           "Por", "ahora,", "son", "acercamientos,", "no", "acuerdos", "confirmados.", "Pero", "esto", "abre", "una", "gran", "pregunta…",
           "¿Será", "que", "se", "viene", "una", "dolarización", "en", "Venezuela?"]
assert len(DISPLAY) == len(W), (len(DISPLAY), len(W))
GROUPS = [(0, 2), (2, 10), (10, 17), (17, 19), (19, 27), (27, 34), (34, 41), (41, 47), (47, 55)]
t = open(os.path.join(HERE, "index.template.html"), encoding="utf-8").read()
t = t.replace("{{VEN}}", open(os.path.join(HERE, "ven.path")).read())
grid = "".join(f'<line x1="{x}" y1="-110" x2="{x}" y2="650" />' for x in range(-130, 780, 88)) + "".join(f'<line x1="-130" y1="{y}" x2="770" y2="{y}" />' for y in range(-110, 660, 88))
t = t.replace("{{GRID}}", grid)
city = ""
for i, (x, w, h) in enumerate([(20, 50, 90), (80, 40, 150), (130, 60, 120), (200, 46, 200), (256, 56, 140), (322, 40, 170), (372, 60, 100), (440, 36, 130)]):
    wins = "".join(f'<i style="top:{18+k*26}px"></i>' for k in range(int(h/30)))
    city += f'<div class="bld cb" style="left:{x}px;width:{w}px;height:{h}px">{wins}</div>'
t = t.replace("{{CITY}}", city)
docs = "".join(f'<div class="doc dc" style="left:{(i%2)*16}px;top:{330-i*30}px;transform:rotate({(-3+i%3*3)}deg)"></div>' for i in range(10))
t = t.replace("{{DOCS}}", docs)
mini = ""
for i, (x, w, h, c) in enumerate([(0, 70, 90, "#2867a8"), (90, 90, 60, "#2ca58d"), (200, 60, 140, "#2867a8"), (280, 110, 70, "#c9a45d"), (20, 80, 50, "#2ca58d")]):
    mini += f'<div class="bld mb" style="left:{x}px;width:{w}px;height:{h}px;bottom:{0 if i<4 else 160}px;background:linear-gradient(180deg,{c},#173b4d)"></div>'
t = t.replace("{{MINI}}", mini)
caps = []; srt = []
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
for gi, (a, b) in enumerate(GROUPS):
    start = W[a][0]; end = W[GROUPS[gi + 1][0]][0] - 0.02 if gi + 1 < len(GROUPS) else W[-1][1] + 0.6
    spans = " ".join(f'<span class="w" data-a="{W[k][0]}" data-b="{W[k][1]}">{DISPLAY[k]}</span>' for k in range(a, b))
    caps.append(f'        <div id="cg{gi}" class="clip cg" data-start="{start}" data-duration="{round(end - start, 2)}" data-track-index="5"><span class="in">{spans}</span></div>')
    srt.append(f"{gi+1}\n{ts(start)} --> {ts(end)}\n{' '.join(DISPLAY[a:b])}\n")
t = t.replace("{{CAPTIONS}}", "\n".join(caps)).replace("{{S5DUR}}", str(round(DUR - 21.6, 2))).replace("{{BLK}}", str(DUR - 0.25)).replace("{{BLKD}}", "0.25").replace("{{DUR}}", str(DUR))
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(t)
open(os.path.join(HERE, "..", "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(srt))
print("ok")
