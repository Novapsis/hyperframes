"""Generates index.html. Run: python3 build/build.py"""
import os, re
HERE = os.path.dirname(__file__)
DUR = 49.0
CTA_START = 42.3
CAPS = [
    (0.05, 2.3, "¿Y si tu próximo vendedor trabajara"),
    (2.38, 3.6, "las *veinticuatro horas* del día,"),
    (3.65, 6.05, "los *trescientos sesenta y cinco días* del año?"),
    (6.48, 7.1, "¡Y lo mejor!"),
    (7.5, 9.2, "Ya conoce todo tu *inventario*."),
    (9.61, 11.0, "Con *Novapsis 360*,"),
    (11.3, 13.75, "conectas tu *WhatsApp* al sistema administrativo"),
    (13.84, 15.9, "y tu vendedor con *inteligencia artificial*"),
    (16.36, 18.0, "comienza a atender clientes por ti."),
    (18.45, 20.4, "Responde mensajes, muestra productos,"),
    (20.54, 22.2, "consulta precios, verifica existencias"),
    (22.25, 25.4, "y prepara *cotizaciones* automáticamente."),
    (25.88, 27.35, "¡Incluso mientras tú duermes!"),
    (27.66, 29.25, "No es simplemente *otro chatbot*."),
    (29.76, 32.9, "Es un asistente conectado a la *información real* de tu negocio."),
    (33.32, 35.05, "Menos tiempo pegado al teléfono."),
    (35.45, 37.0, "Más *oportunidades* de vender."),
    (37.38, 38.62, "*Novapsis 360*."),
    (38.98, 40.35, "Tu negocio sigue atendiendo,"),
    (40.53, 42.15, "incluso cuando tú descansas."),
]
EXTRA = [(42.51, 43.42, "Comenta AGENDA"), (43.52, 45.4, "y recibe el enlace para descubrir"), (45.47, 47.6, "cómo tener tu propio vendedor virtual.")]
caps_html = []
for i, (a, b, txt) in enumerate(CAPS + [(43.52, 45.4, "y recibe el enlace para descubrir"), (45.47, 47.6, "cómo tener tu propio vendedor virtual.")], 1):
    inner = re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', txt)
    caps_html.append(f'      <div id="cap{i}" class="clip cap" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="5"><span class="cap-in">{inner}</span></div>')
tpl = open(os.path.join(HERE, "index.template.html"), encoding="utf-8").read()
out = tpl.replace("{{CAPTIONS}}", "\n".join(caps_html)).replace("{{CTA_DUR}}", str(round(DUR - CTA_START, 2))).replace("{{DUR}}", str(DUR))
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(out)
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
srt = [f"{i}\n{ts(a)} --> {ts(b)}\n{t.replace('*', '')}\n" for i, (a, b, t) in enumerate(CAPS + EXTRA, 1)]
open(os.path.join(HERE, "..", "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(srt))
print("ok")
