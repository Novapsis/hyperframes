"""Generates index.html, subtitulos.srt, build/ops.json. Run: python3 build/build.py"""
import os, re, json, random
HERE = os.path.dirname(__file__)
DUR = 98.6
AREAS = [((k % 4) * 1200, (k // 4) * 2100) for k in range(14)]
CAPS = [
    (0.05, 2.2, "¿Sabes cómo funciona un *vendedor virtual*?"),
    (2.69, 5.1, "Imagina una tienda de repuestos para motos."),
    (5.28, 6.6, "Son las *siete de la mañana*."),
    (7.24, 8.65, "El dueño abre su negocio."),
    (9.15, 12.92, "Un cliente busca una *batería*, otro necesita una *cadena*"),
    (13.28, 14.6, "y otro está esperando su *factura*."),
    (14.9, 17.15, "Mientras tanto, ¡el *WhatsApp* no deja de sonar!"),
    (17.46, 19.55, "A las *cinco de la tarde* cierra la tienda,"),
    (20.01, 22.12, "pero todavía tiene *mensajes sin responder*."),
    (22.56, 25.3, "¿Cuántas *oportunidades de venta* se están perdiendo?"),
    (26.11, 31.32, "Ahora imagina que tu negocio tuviera un vendedor que conoce todos tus productos,"),
    (31.53, 32.9, "*precios, existencias y horarios*."),
    (33.37, 35.21, "Un cliente pregunta por una *bujía*."),
    (35.71, 38.41, "El vendedor *consulta el inventario* y le responde."),
    (38.86, 40.59, "Otro necesita una *cotización*."),
    (40.98, 41.74, "¡Se la prepara!"),
    (42.15, 43.77, "Otro pregunta por los *envíos*."),
    (44.25, 46.1, "Le explica las opciones disponibles."),
    (46.57, 48.46, "¿Y el cliente que está dentro de la tienda,"),
    (48.64, 50.89, "pero no quiere hacer cola solo para preguntar?"),
    (51.41, 54.71, "Escanea un código y consulta directamente por *WhatsApp*."),
    (55.21, 56.68, "¡Y aquí viene lo interesante!"),
    (57.14, 61.06, "Tu vendedor virtual puede atender *múltiples conversaciones* al mismo tiempo,"),
    (61.21, 62.68, "mientras tú sigues trabajando."),
    (62.82, 66.17, "Además, deja las consultas y los pedidos *organizados*."),
    (66.68, 69.3, "Incluso puede preparar *facturas* y registrar operaciones,"),
    (69.3, 71.94, "según la configuración de tu negocio."),
    (72.45, 76.57, "Y tú mantienes el *control* para verificar los pagos y coordinar las entregas."),
    (77.04, 80.09, "Eso es un *vendedor virtual* con inteligencia artificial."),
    (80.6, 83.82, "Un asistente conectado a la *información real* de tu empresa,"),
    (83.97, 86.72, "que puede seguir atendiendo incluso después de cerrar."),
    (87.27, 91.22, "¿Te gustaría *recuperar tiempo* y dejar de perder oportunidades de venta?"),
    (91.71, 94.3, "Comenta *AGENDA* y te ayudamos a descubrir"),
    (94.3, 96.87, "cómo automatizar la atención de tu negocio."),
]
t = open(os.path.join(HERE, "index.template.html"), encoding="utf-8").read()

def chat(m):
    k = int(m.group(1))
    return (f'<g class="chatP{k} fx" data-area="{k}"><rect x="130" y="330" width="820" height="740" rx="36" fill="#ffffff" stroke="#171717" stroke-width="3" />'
            f'<path d="M130 420 H950" stroke="#e2e8f0" stroke-width="3" /><circle cx="190" cy="375" r="22" fill="#14b8a6" />'
            f'<text class="ui" x="228" y="385" font-size="28" font-weight="800">Tienda · Vendedor virtual</text>'
            f'<text class="ui" x="915" y="384" font-size="20" font-weight="800" text-anchor="end" fill="#64748b">DEMO</text></g>')
t = re.sub(r"\{\{CHAT (\d+)\}\}", chat, t)

boxtl = []
def box(m):
    n, x, y, q, a, tq, td, ta = m.groups(); x, y = int(x), int(y); q = q.replace("_", " "); a = a.replace("_", " ")
    tq, td, ta = float(tq), float(td), float(ta)
    boxtl.append(f'pop("#bq{n}", {tq}); pop("#ba{n}", {ta}); on("#bn{n}", {ta + 0.8}, 0.25);')
    return (f'<g id="bx{n}"><text class="ui" x="{x+20}" y="{y+40}" font-size="20" font-weight="700" fill="#64748b">Cliente {n} · WhatsApp</text>'
            f'<g id="bq{n}" class="fx"><rect x="{x+16}" y="{y+56}" width="288" height="52" rx="18" fill="#f1f5f9" /><text class="ui" x="{x+30}" y="{y+90}" font-size="21" font-weight="800">{q}</text></g>'
            f'<g class="dots" data-t0="{td}" data-t1="{ta}"><circle cx="{x+40}" cy="{y+140}" r="6" fill="#14b8a6" /><circle cx="{x+60}" cy="{y+140}" r="6" fill="#14b8a6" /><circle cx="{x+80}" cy="{y+140}" r="6" fill="#14b8a6" /></g>'
            f'<g id="ba{n}" class="fx"><rect x="{x+16}" y="{y+124}" width="288" height="52" rx="18" fill="#dcfce7" /><text class="ui" x="{x+30}" y="{y+158}" font-size="20" font-weight="800" fill="#166534">✓ {a}</text></g>'
            f'<g id="bn{n}" class="fx"><text class="ui" x="{x+20}" y="{y+218}" font-size="19" font-weight="700" fill="#64748b">nuevo mensaje</text>'
            f'<g class="dots" data-t0="{ta + 0.8}" data-t1="62.8"><circle cx="{x+170}" cy="{y+212}" r="5" fill="#25d366" /><circle cx="{x+186}" cy="{y+212}" r="5" fill="#25d366" /><circle cx="{x+202}" cy="{y+212}" r="5" fill="#25d366" /></g></g></g>')
t = re.sub(r"\{\{BOX (\d) (\d+) (\d+) (\S+) (\S+) ([\d.]+) ([\d.]+) ([\d.]+)\}\}", box, t)
t = t.replace("{{BOXTL}}", "\n      ".join(boxtl))

rnd = random.Random(42); cells = []
N = 11; s = 120 / N
def finder(cx, cy):
    return [(cx + i, cy + j) for i in range(3) for j in range(3) if not (i == 1 and j == 1)]
fixed = set(finder(0, 0) + finder(8, 0) + finder(0, 8))
for i in range(N):
    for j in range(N):
        if (i, j) in fixed or (rnd.random() < 0.45 and not ((i < 4 and j < 4) or (i > 6 and j < 4) or (i < 4 and j > 6))):
            cells.append(f'<rect x="{810 + i*s:.1f}" y="{555 + j*s:.1f}" width="{s+0.3:.1f}" height="{s+0.3:.1f}" fill="#171717" />')
t = t.replace("{{QR}}", "".join(cells))

def area(m):
    k = int(m.group(1)); x, y = AREAS[k]
    return f'data-area="{k}" transform="translate({x} {y})" data-tx="{x}" data-ty="{y}"'
t = re.sub(r'data-area="(\d+)"', area, t)
t = t.replace("{{AREAS}}", json.dumps(AREAS))
caps = []
for i, (a, b, txt) in enumerate(CAPS, 1):
    inner = re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', txt)
    caps.append(f'      <div id="cap{i}" class="clip cap" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="5"><span class="cap-in">{inner}</span></div>')
t = t.replace("{{CAPTIONS}}", "\n".join(caps)).replace("{{DUR}}", str(DUR))
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(t)
ops = sorted(set((float(a), float(b)) for a, b in re.findall(r'class="op [^"]*"[^>]*?data-t0="([\d.]+)" data-t1="([\d.]+)"', t)))
json.dump(ops, open(os.path.join(HERE, "ops.json"), "w"))
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s_, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s_:02},{ms:03}"
open(os.path.join(HERE, "..", "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{x.replace('*','')}\n" for i, (a, b, x) in enumerate(CAPS, 1)))
print("ok", len(ops), "ops")
