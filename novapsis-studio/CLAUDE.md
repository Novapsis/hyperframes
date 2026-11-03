# Novapsis Studio — instrucciones para Claude

Estudio de producción de Reels verticales (1080×1920, 30 fps) para Novapsis con HyperFrames. Antes de componer, lee la skill `/hyperframes`; si no está instalada, ejecuta `npx hyperframes skills update`.

## Flujo obligatorio

1. **Audio primero.** Usa la locución aprobada sin cambiar palabras. Si el proyecto no tiene `build/words.json`, transcríbela con `python3 tools/transcribe.py <wav> <proyecto>/build/words.json`. Todo se sincroniza a tiempos de palabra medidos.
2. **Velocidad de la voz.** Solo se ajusta si hay un tramo realmente rápido, con `atempo` sin cambiar el tono, o añadiendo pausas breves (0,3–0,7 s) en momentos de impacto. Siempre se avisa al usuario.
3. **Construcción.** Cada proyecto se genera desde `build/index.template.html`, `build/build.py` y `build/make_audio.py`. Nunca se edita `index.html` a mano.
4. **Validación.** `npx hyperframes lint`, sin errores. Después `npx hyperframes snapshot --at …` en todos los momentos clave, revisando cada fotograma antes del render.
5. **Render.** Con `bash tools/finalizar.sh`. Después se extraen fotogramas del MP4 final y se revisan antes de entregar.
6. **Entrega.** MP4, `portada_instagram.png`, `subtitulos.srt` e `INFORME_CALIDAD.md`, en el que se dice qué no se pudo verificar.

## Estilo de la casa (aprendido con el usuario)

- **Subtítulos karaoke por defecto:** la frase completa con la palabra que suena en dorado o turquesa, las ya dichas en blanco y las que vienen en gris (ver `templates/noticia-cinematica`).
- **Pizarra:** usar la mano de `shared/hand/hand-pencil.png`. La punta del lápiz sigue el trazo exacto y el brazo va recortado justo después del puño de la manga.
- **Efectos de sonido sutiles.** Nada de barridos fuertes en las transiciones: el usuario los rechazó. La voz siempre manda. Mezcla a −14 LUFS con pico ≤ −1 dBTP y limitador.
- **Texto:** nunca debe salirse de su contenedor. Revisar los anchos con snapshots.
- **Montos y datos de ejemplo:** grandes y visibles cuando sirven al mensaje, siempre con la nota "Montos de ejemplo" o "DEMO".
- **Dibujos:** reconocibles. Una moto tiene que parecer una moto, no una bicicleta.

## Rigor

- No inventar cifras, acuerdos, integraciones ni capturas oficiales. Lo conceptual se marca como "DEMO", "RECREACIÓN ILUSTRATIVA" o "ILUSTRACIÓN CONCEPTUAL".
- No generar logotipos. Usar solo `shared/brand/`. Los logos de terceros se ponen en tipografía si no hay recurso autorizado.
- Las finanzas se tratan como educación, sin promesas de rentabilidad. Las cifras del brief se verifican con fuentes cuando haya red.

## En local se puede (y conviene)

- Usar Three.js/WebGL para 3D real (billetes, monedas, mapas, teléfonos). Ver `/hyperframes`, referencia de runtimes.
- Usar los recursos reales del usuario y consultar la web para verificar datos.
- Abrir `npx hyperframes preview` para que el usuario revise en vivo.
