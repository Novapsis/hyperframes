"""Generates index.html + subtitulos.srt + build/ops.json. Run: python3 build/build.py"""
import os, re, math, json
HERE = os.path.dirname(__file__)
DUR = 92.6
CAPS = [
    (0.05, 2.85, "¿En cuál de los *cuatro cuadrantes* del dinero te encuentras?"),
    (3.2, 6.1, "Robert Kiyosaki explica *cuatro formas* de generar ingresos"),
    (6.1, 9.3, "que pueden cambiar tu manera de entender el dinero."),
    (9.8, 11.15, "Primero, el *empleado*."),
    (11.65, 14.3, "Intercambia su tiempo y conocimientos por un salario."),
    (14.68, 17.4, "Si pierde su empleo, pierde esa fuente de ingresos."),
    (17.51, 19.1, "Segundo, el *autoempleado*."),
    (19.66, 20.62, "Es su propio jefe,"),
    (21.1, 23.6, "pero su negocio depende directamente de su trabajo."),
    (24.17, 26.97, "Si deja de trabajar, sus ingresos pueden detenerse."),
    (27.27, 28.97, "Tercero, el *dueño de negocio*."),
    (29.43, 33.28, "Construye sistemas, forma equipos y delega responsabilidades."),
    (33.57, 35.6, "Su empresa puede seguir funcionando"),
    (35.6, 37.7, "sin que tenga que estar presente todo el tiempo."),
    (38.18, 39.92, "Y cuarto, el *inversionista*."),
    (40.45, 43.9, "Utiliza su dinero para adquirir activos que pueden generar nuevos ingresos,"),
    (43.9, 46.05, "aunque también existen *riesgos*."),
    (46.5, 47.63, "¿Notas la diferencia?"),
    (48.09, 51.75, "Mientras unos dependen principalmente de su tiempo para generar dinero,"),
    (52.0, 55.65, "otros construyen *sistemas y activos* que pueden producir ingresos."),
    (55.98, 59.13, "Y recuerda: puedes estar en *varios cuadrantes* a la vez,"),
    (59.41, 61.12, "y ninguno *garantiza riqueza*."),
    (61.22, 63.45, "Ahora viene la pregunta más importante."),
    (63.88, 65.8, "Si mañana dejaras de trabajar,"),
    (66.71, 68.45, "¿tu negocio seguiría funcionando?"),
    (69.41, 72.2, "Porque si tu negocio se detiene cuando tú te detienes,"),
    (72.67, 74.65, "sigues cambiando tu tiempo por dinero."),
    (75.13, 77.45, "La solución no siempre es trabajar más horas,"),
    (77.59, 78.95, "sino aprender a *delegar*,"),
    (79.13, 81.5, "*crear sistemas* y *automatizar* procesos."),
    (81.94, 83.6, "¿Quieres empezar a dar ese paso?"),
    (84.05, 86.5, "Comenta la palabra *AGENDA*"),
    (86.5, 88.95, "y descubre cómo podemos ayudarte a automatizar tu negocio"),
    (89.4, 91.1, "para que no todo dependa de ti."),
]
def gear(r, n):
    ro, ri = r, r * 0.78
    pts = []
    for i in range(n):
        a0 = 2 * math.pi * i / n
        step = 2 * math.pi / n
        for f, rr in ((0.0, ri), (0.12, ro), (0.42, ro), (0.54, ri)):
            a = a0 + f * step
            pts.append((rr * math.cos(a), rr * math.sin(a)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
tpl = open(os.path.join(HERE, "index.template.html"), encoding="utf-8").read()
tpl = re.sub(r"\{\{GEAR (\d+) (\d+)\}\}", lambda m: gear(int(m.group(1)), int(m.group(2))), tpl)
caps = []
for i, (a, b, txt) in enumerate(CAPS, 1):
    inner = re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', txt)
    caps.append(f'      <div id="cap{i}" class="clip cap" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="5"><span class="cap-in">{inner}</span></div>')
out = tpl.replace("{{CAPTIONS}}", "\n".join(caps)).replace("{{DUR}}", str(DUR))
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(out)
ops = [(float(a), float(b)) for a, b in re.findall(r'class="op [^"]*"[^>]*?data-t0="([\d.]+)" data-t1="([\d.]+)"', out)]
ops += [(float(a), float(b)) for a, b in re.findall(r'data-p1="[\d.]+" data-t0="([\d.]+)" data-t1="([\d.]+)"', out)]
json.dump(sorted(set(ops)), open(os.path.join(HERE, "ops.json"), "w"))
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
open(os.path.join(HERE, "..", "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{t.replace('*','')}\n" for i, (a, b, t) in enumerate(CAPS, 1)))
print("ok", len(ops), "ops")
