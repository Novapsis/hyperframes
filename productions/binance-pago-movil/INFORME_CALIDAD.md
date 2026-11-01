# Binance Pago Móvil — Novapsis 360 · Informe de producción

## Entregables

| #   | Entregable                                   | Ruta                                                                         |
| --- | -------------------------------------------- | ---------------------------------------------------------------------------- |
| 1-2 | Proyecto HyperFrames + composición principal | `index.html` (generada desde `build/index.template.html` + `build/build.py`) |
| 3   | Assets                                       | `assets/`                                                                    |
| 4   | Narración (editada) / original               | `assets/audio/narracion.wav` / `assets/audio/narracion_original.wav`         |
| 5   | Subtítulos                                   | `subtitulos.srt` (+ quemados en el video)                                    |
| 6   | Video final                                  | `Binance_Pago_Movil_Novapsis360_Reel.mp4`                                    |
| 7   | Portada                                      | `portada_instagram.png`                                                      |
| 8   | Capturas de revisión                         | `review/snap/`, `review/final/`                                              |

## Audio

- La transcripción automática no fue posible: la red del entorno cloud bloquea la descarga del modelo Whisper (huggingface.co). Por eso las frases del guion aprobado se alinearon con las pausas reales de la voz, detectadas con FFmpeg `silencedetect`, y la posición de las palabras dentro de cada frase se estimó en proporción a sus sílabas.
- **Ajustes de ritmo, sin cambiar el texto ni la voz:**
  - Se añadieron +0,35 s de respiración antes de "Y si tienes un negocio…", la transición principal.
  - "Con Novapsis tres sesenta… administración" iba a unas 7,4 sílabas/s y se ralentizó al 92 % con `atempo`, que conserva el tono. Pasa de 7,4 a 8,1 s.
- La música y los efectos de sonido son síntesis original y determinista (`build/make_audio.py`). Sin licencias de terceros.
- Mezcla: voz al 100 %, música al 32 %, efectos al 70 %. Al final se normalizó a -14 LUFS / -1 dBTP.

## Cumplimiento de la regla "cero información inventada"

- Todas las pantallas son **recreaciones** y llevan la marca "RECREACIÓN ILUSTRATIVA" o "SIMULACIÓN VISUAL". No se usa el logotipo de Binance; la marca aparece solo como texto.
- Bs. 1.000,00 está marcado como "Monto de ejemplo". No se muestra ninguna tasa ni cantidad de USDT: aparece "—" o "según cotización".
- Se incluyen los avisos "Los tiempos de acreditación pueden variar", "Disponibilidad gradual" y "Compara cuántos USDT recibes".
- El panel de Novapsis está marcado como "REPRESENTACIÓN CONCEPTUAL". No muestra ninguna integración con Binance ni promete cumplimiento fiscal.

## Recursos faltantes (críticos)

1. \*\*Logotipo Novapsis: integrado (`assets/brand/novapsis/novapsis-logo.png`, extraído del SVG suministrado, que contiene un PNG embebido). Falta versión vectorial real.
2. **Capturas reales de Novapsis 360** (ventas, cobros, facturas, comprobantes, copiloto IA).
3. **Capturas reales** de la app de Binance con el flujo de depósito en VES.
4. Música con licencia, si se prefiere a la pista sintetizada.

## Validación

- `hyperframes lint` y `check`: 0 errores.
- Avisos aceptados:
  - Estructura en un solo archivo: el teléfono es un objeto persistente entre escenas.
  - Algunas líneas del subtítulo duran menos de lo recomendado porque están atadas a la velocidad de la voz.
  - Las filas de relleno en gris de las pantallas tienen bajo contraste a propósito, para que no compitan con la información.
- Snapshots revisados en los 24 momentos clave antes del render y en todos los cambios de escena del MP4 final.
- Correcciones aplicadas tras la revisión:
  - El texto del teléfono se transparentaba bajo el 0 %.
  - "COMPROBANTES" se desbordaba de su recuadro.
  - "ADMINISTRACIÓN INTELIGENTE" quedaba pegado al panel.
  - La transición de oscuro a perla pasaba por un gris sucio.

## Limitaciones conocidas

- El teléfono está construido en CSS (bisel metálico, cristal y sombra). No es un render 3D fotorrealista con Three.js, porque el entorno no tiene GPU (WebGL por software).
- La alineación palabra a palabra es una estimación con un margen aproximado de ±0,15 s. Los momentos clave (0 %, P2P, Depositar, VES, Convertir, USDT/USDC, AGENDA) se anclaron a pausas medidas.
- Antes de publicar, verifica las condiciones vigentes del servicio (comisión, disponibilidad y Casa de Cambios Insular).
