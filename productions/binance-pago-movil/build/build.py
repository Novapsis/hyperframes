"""Generates index.html (static, editable HTML). Run: python3 build/build.py"""
import os, re

HERE = os.path.dirname(__file__)
DUR = 73.9

# (start, end, text) — timed to the edited narration (assets/audio/narracion.wav)
CAPS = [
    (0.05, 2.3, "¿Sabías que ahora puedes comprar dólares digitales"),
    (2.3, 4.5, "en Binance usando *Pago Móvil*,"),
    (4.55, 6.6, "sin pagar comisión por depositar?"),
    (7.0, 9.9, "Recientemente Binance anunció una nueva función"),
    (9.9, 12.85, "que permite depositar bolívares directamente desde tu banco,"),
    (13.2, 15.7, "sin buscar vendedores en el mercado P2P."),
    (16.18, 17.25, "¿Y cómo funciona?"),
    (17.59, 20.1, "Entra en Binance, selecciona *Depositar*,"),
    (20.33, 21.3, "elige *bolívares*"),
    (21.35, 23.9, "y escoge *Pago Móvil* o transferencia bancaria."),
    (24.36, 26.38, "Introduce el monto y realiza el pago"),
    (26.42, 28.35, "desde una *cuenta a tu nombre*."),
    (28.68, 30.52, "Una vez acreditados los fondos,"),
    (30.57, 33.42, "entra en *Convertir* y consulta la opción"),
    (33.46, 35.75, "de cambiarlos por *USDT* o *USDC*."),
    (36.08, 37.02, "¡Pero ojo!"),
    (37.08, 39.15, "Aunque el depósito no tenga comisión,"),
    (39.45, 42.15, "*compara la tasa* de conversión antes de confirmar."),
    (42.48, 44.6, "Además, la función podría no estar disponible"),
    (44.6, 46.8, "todavía en todas las cuentas."),
    (47.47, 50.1, "Y si tienes un negocio, recuerda algo importante:"),
    (50.56, 51.95, "no basta con recibir dinero,"),
    (52.23, 54.4, "también necesitas tener tus operaciones"),
    (54.45, 55.98, "organizadas y respaldadas."),
    (56.07, 57.48, "Con *Novapsis 360*"),
    (58.0, 59.94, "puedes gestionar tus ventas, cobros,"),
    (60.08, 61.36, "facturas y comprobantes,"),
    (61.43, 63.32, "utilizando inteligencia artificial"),
    (63.37, 65.1, "para simplificar tu administración."),
    (65.53, 67.1, "¿Quieres poner tu negocio al día"),
    (67.18, 70.0, "y prepararte para las nuevas exigencias fiscales?"),
]

caps_html = []
for i, (a, b, txt) in enumerate(CAPS, 1):
    novapsis = a >= 47.2
    cls = "cap nv" if novapsis else "cap"
    inner = re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', txt)
    caps_html.append(
        f'      <div id="cap{i}" class="clip {cls}" data-start="{a}" data-duration="{round(b - a, 2)}" '
        f'data-track-index="5"><span class="cap-in">{inner}</span></div>'
    )

tpl = open(os.path.join(HERE, "index.template.html"), encoding="utf-8").read()
out = tpl.replace("{{CAPTIONS}}", "\n".join(caps_html)).replace("{{DUR}}", str(DUR))
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(out)

# SRT sidecar
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
srt = []
for i, (a, b, txt) in enumerate(CAPS + [(70.35, 71.32, "Comenta AGENDA"), (71.41, 72.55, "y evaluemos tu caso.")], 1):
    srt.append(f"{i}\n{ts(a)} --> {ts(b)}\n{txt.replace('*', '')}\n")
open(os.path.join(HERE, "..", "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(srt))
print("index.html + subtitulos.srt written")
