# Novapsis — Devaluación · Informe

## Entregables

- **Video:** `Novapsis_Devaluacion_Reel.mp4`, 1080×1920, 30 fps, H.264, AAC estéreo a 48 kHz, 76,3 s, −14,2 LUFS.
- **Portada:** `portada_instagram.png`, generada desde `build/cover.html`.
- **Subtítulos:** `subtitulos.srt`, también quemados en el video.
- **Proyecto:** `index.html`, generado con `python3 build/build.py`.
- **Audio:** `build/make_audio.py`, música y efectos de síntesis original, sin licencias de terceros.
- **Transcripción:** `build/words.json`, con tiempos por palabra.

## Audio y sincronización

- La locución no se modificó: 73,6 s, sin cambios de velocidad.
- Transcripción real con Whisper small (CTranslate2, licencia MIT), obtenido desde el paquete npm `@skillninja/shortmovie-telop-model`. Toda la sincronización está anclada a tiempos de palabra medidos.

## Verificación de cifras

| Dato                    | Valor                                                       |
| ----------------------- | ----------------------------------------------------------- |
| 03/11/2025              | 100 USD = 22.396 Bs (tasa BCV de referencia, dato aprobado) |
| 03/11/2026              | 100 USD = 89.111 Bs (tasa BCV de referencia, dato aprobado) |
| 22.396 Bs en 2026       | 22.396 ÷ 89.111 × 100 = 25,13 USD                           |
| Pérdida frente al dólar | 1 − 22.396/89.111 = −74,87 %                                |

- La locución redondea ("unos 22.400", "más de 89.000", "casi el 75 %"). En pantalla se usan las cifras exactas.
- Las mismas cifras aparecen en todas las escenas, sin contradicciones.
- Se usa el tipo de cambio BCV. No hay datos de inflación ni de cotización P2P.
- **Las tasas no se verificaron contra la fuente:** se usaron tal como venían en el brief. El entorno no permite consultar el BCV.

## Responsabilidad

- **Billete y pilas:** el billete de 1 USD es una "ILUSTRACIÓN CONCEPTUAL" y las pilas de Bs están marcadas como esquemáticas.
- **USDT y USDC:**
  - Aparecen como "OBJETIVO DE PARIDAD: 1 USD", con la nota "el precio de mercado puede desviarse".
  - No se usan sus logotipos oficiales: son discos genéricos con el nombre.
  - El flujo de conversión indica "Comisiones y tipo de cambio variable según el proveedor y el mercado", junto con "REDUCE LA EXPOSICIÓN · NO LA ELIMINA".
- **Riesgos:** se muestran comisiones, estafas, pérdidas de valor, red, dirección y custodia.
- **Bitcoin:** aparece "BITCOIN ≠ STABLECOIN" con un gráfico marcado como ilustrativo, sin datos reales ni promesa de rentabilidad.
- **Cierre:** "Contenido educativo · no es asesoría financiera".

## Limitaciones

- La profundidad 3D es CSS 3D (perspectiva, entrada por profundidad, rotación de monedas), sin Three.js ni WebGL, porque el entorno no tiene GPU.
- El logo de Novapsis es el PNG extraído del SVG suministrado, que contiene un mapa de bits. Falta la versión vectorial real.
- No se generó un master de mayor calidad aparte; el MP4 se exportó en calidad "delivery".
