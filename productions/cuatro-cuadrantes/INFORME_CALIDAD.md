# Novapsis Studio — Los 4 Cuadrantes del Dinero · Informe

## Entregables

- **Proyecto:** `index.html`, generado con `python3 build/build.py` desde `build/index.template.html`.
  - Motor de dibujo: cada trazo SVG se revela a medida que la punta del marcador recorre su geometría (`getPointAtLength`).
  - Todo, incluidas la cámara, la mano y los engranajes, es una función pura del tiempo, así que el render es determinista.
- **Video:** `Los_4_Cuadrantes_Del_Dinero_Novapsis_Reel.mp4`, 1080×1920, 30 fps, H.264/AAC, 92,7 s, −14,0 LUFS y pico de −1,0 dBFS.
- **Portada:** `portada_instagram.png`, generada desde `build/cover.html`. Cabe dentro del recorte 3:4 del perfil.
- **Subtítulos:** `subtitulos.srt`, también quemados en el video.
- **Sincronización:** `build/ops.json`, con los 64 trazos y escrituras y sus tiempos.
- **Música y efectos:** `build/make_audio.py`, síntesis original. Incluye el trazo de marcador en cada dibujo, el tic del reloj, los engranajes y su frenado.

## Audio

- La voz y el texto no se modificaron. Solo se añadieron silencios expresivos: 0,7 s antes de "¿tu negocio seguiría funcionando?" y 0,5 s después.
- La alineación se hizo por pausas medidas con FFmpeg `silencedetect`, porque Whisper no está disponible en este entorno.

## Escena maestra

1. 62,75 s: la mano empieza la flecha entre engranajes.
2. 63,88 s ("Si mañana dejaras de trabajar"): la mano se congela con el trazo al 52 %.
3. Los engranajes frenan en cascada entre 63,9 y 65,7 s y el turquesa se apaga.
4. 66,7 s: la cámara se acerca a los engranajes detenidos.
5. Durante "sigues cambiando tu tiempo por dinero" el reloj de E sigue girando mientras D permanece quieto.
6. 77,6 s: la mano vuelve y dibuja a la persona en quien delegar, el engranaje 1 arranca.
7. Dibuja Entrada → Proceso → Resultado y arranca el engranaje 2.
8. 80,0–80,5 s: completa la flecha y arranca el engranaje 3.
9. La mano se retira y el sistema sigue girando sin ella.

## Precisión

- Se atribuye el modelo a Kiyosaki.
- Se usan las iniciales en español (E, A, D, I). No se añadió la nota sobre E, S, B, I porque habría saturado la pantalla.
- Se incluyen "RIESGO" y "NINGUNO GARANTIZA RIQUEZA".
- No hay cifras, billetes ni promesas de ingresos.

## Limitaciones / pendientes

1. **La mano es una ilustración vectorial, no fotográfica.** Su posición sí es exacta, porque la punta sigue cada trazo. Para realismo fotográfico hace falta un clip real grabado desde arriba sobre fondo blanco. El motor ya expone la posición de la punta en cada fotograma, así que se puede componer un clip o sprite real sobre `#hand`.
2. **Video de referencia:** no se recibió.
3. **Logo:** el de Novapsis es un PNG extraído del SVG suministrado. Falta la versión vectorial.
4. **CTA:** hay que verificar que el comentario AGENDA tenga respuesta operativa.
