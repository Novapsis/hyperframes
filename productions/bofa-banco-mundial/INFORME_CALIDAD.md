# Novapsis — Bank of America + Banco Mundial · Informe

## Entregables

- **Video:** `Novapsis_BofA_BancoMundial_Venezuela_Reel.mp4`, 1080×1920, 30 fps, H.264, AAC estéreo a 48 kHz, 27,0 s, −14,1 LUFS. Termina con un corte a negro de 0,25 s.
- **Versión sin narración:** `Novapsis_BofA_BancoMundial_SIN_NARRACION.mp4`, solo con música y efectos.
- **Subtítulos:** `subtitulos.srt`.
- **Proyecto:** `index.html`, generado con `python3 build/build.py`. Tiempos por palabra en `build/words.json` y música y efectos en `build/make_audio.py`.

## Subtítulos karaoke (nuevo)

- Transcripción real con Whisper small (MIT), con tiempos por palabra.
- Cada frase aparece completa. La palabra que se está diciendo se ilumina en dorado; las ya dichas quedan en blanco y las siguientes en gris.
- El texto respeta el guion oficial: la puntuación del guion corrige la de la transcripción.

## Rigor

- **Nombres:** "BANK OF AMERICA" y "CORPORACIÓN FINANCIERA INTERNACIONAL · GRUPO BANCO MUNDIAL", en tipografía. No se usan logotipos de terceros.
- **Estado de la noticia:**
  - "VISITA PREVISTA · ESTA SEMANA".
  - "POSIBLE REESTRUCTURACIÓN" y "EVALUACIÓN PRELIMINAR".
  - "SIN ACUERDOS CONFIRMADOS", que aparece dos veces.
- **Cifras:** ninguna.
- **Dolarización:** solo aparece como pregunta.
- **Mapa:** silueta simplificada de Venezuela, con Caracas aproximada.

## Limitaciones

- La profundidad 3D es CSS 3D (mapa inclinado, paneles con rotación, extrusión tipográfica), sin Three.js, porque el entorno no tiene GPU.
