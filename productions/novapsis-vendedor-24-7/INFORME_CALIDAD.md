# Novapsis 360 — Tu Vendedor Nunca Duerme · Informe

## Entregables

- **Proyecto:**
  - `index.html`, generado desde `build/index.template.html` con `python3 build/build.py`
  - Música y efectos: `build/make_audio.py`, con sus tiempos en `build/times.json`
- **Video:** `Novapsis360_VendedorVirtual_24_7_Reel.mp4`, 1080×1920, 30 fps, H.264/AAC, 49,1 s, −14,2 LUFS y pico de −1,9 dBFS.
- **Portada:** `portada_instagram.png`, generada desde `build/cover.html`. Todo su contenido queda dentro del recorte 3:4 de la cuadrícula del perfil.
- **Subtítulos:** `subtitulos.srt` y quemados en el video.
- **Revisión:** `review/snap/` (contact sheets) y `review/final/sheet.jpg` (28 fotogramas del MP4 final).

## Audio

- Se usó la locución aprobada, de 47,7 s, sin ninguna edición. El ritmo es parejo, así que no hizo falta ajustar tiempos.
- Alineación: con FFmpeg `silencedetect` sobre el guion exacto, porque Whisper no se puede descargar en este entorno. Las palabras clave quedaron ancladas a pausas medidas:
  - "veinticuatro horas": 2,45 s
  - "365 días": 3,7 s
  - "inventario": 8,5 s
  - "Novapsis 360": 9,6 s
  - "WhatsApp": 11,7 s
  - "inteligencia artificial": 14,6 s
  - "responde mensajes" / "muestra productos" / "consulta precios" / "verifica existencias" / "cotizaciones": 18,5 / 19,6 / 20,6 / 21,7 / 23,6 s
  - "duermes": 25,9 s
  - "chatbot": 27,7 s
  - "oportunidades": 35,6 s
  - "Novapsis 360": 37,4 s
  - "AGENDA": 42,9 s
- La música y los efectos son síntesis original, sin licencias de terceros.

## Veracidad

- **Productos, precios y chat:** marcados como DEMO o DATOS DEMO.
- **Cotización:** aparece como "BORRADOR · DEMO — lista para revisión y envío por tu equipo". No se simula ningún envío, pago ni despacho.
- **Integración:** se presenta como "Integración de software con los permisos que tú configuras".
- **Promesas:** no hay cifras de ventas, porcentajes ni garantías.

## Pendientes / bloqueos antes de publicar

1. **Respuesta automática al comentario AGENDA.** La locución dice "recibe el enlace", así que hay que verificar que esa automatización esté operativa antes de publicar.
2. **Video de referencia de Claude.** No se recibió (`WhatsApp Video 2026-11-01 at 21.52.22.mp4`). El estilo se construyó a partir de la descripción del prompt.
3. **Logo de WhatsApp.** No hay un recurso oficial autorizado. Se usó un ícono genérico de burbuja en verde y la palabra "WhatsApp".
4. **Logo de Novapsis.** El SVG suministrado contiene un PNG embebido, así que falta la versión vectorial real.
5. **Producto real.** Faltan capturas reales de Novapsis 360 y un catálogo demo real.

## Validación

- `hyperframes lint` / `check`: 0 errores.
- Avisos aceptados: proyecto en un solo archivo y pistas con muchos clips.
- Correcciones aplicadas tras revisar los fotogramas:
  - Hueco vacío durante "¡Y lo mejor!".
  - El contenido del chat se veía bajo la cabecera.
  - El cursor de AGENDA aparecía mal colocado.
  - Las líneas de transición tachaban "365 DÍAS".
- Limitación: los efectos 3D son con CSS, sin Three.js, porque el entorno no tiene GPU.
