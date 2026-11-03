# Novapsis Studio — kit local de producción de video

Todo lo necesario para producir los Reels de Novapsis en tu computadora con Claude Code y HyperFrames, con la misma forma de trabajar que en la nube y además GPU (3D real con Three.js), tus archivos y sin bloqueos de red.

## 1. Requisitos (una sola vez)

- **Node.js 22 o superior:** https://nodejs.org
- **FFmpeg:**
  - macOS: `brew install ffmpeg`
  - Windows: `winget install ffmpeg`
  - Ubuntu: `sudo apt install ffmpeg`
- **Python 3.10 o superior.**
- **Claude Code:** https://claude.com/claude-code

> En Windows, usa WSL o Git Bash para los scripts `.sh`.

## 2. Descargar el kit

Opción A, con git:

```bash
git clone -b claude/amazing-pasteur-lqe7t0 https://github.com/Novapsis/hyperframes.git
```

```bash
cd hyperframes/novapsis-studio
```

Opción B, sin git: descarga el ZIP del branch `claude/amazing-pasteur-lqe7t0` en GitHub, descomprímelo y entra en la carpeta `novapsis-studio`.

Puedes mover `novapsis-studio` a donde quieras, por ejemplo `~/videos-novapsis`. Es independiente del resto del repo.

## 3. Instalar

```bash
bash setup.sh
```

Comprueba Node, FFmpeg y Python, instala la transcripción y descarga el modelo Whisper una sola vez (unos 480 MB).

## 4. Hacer un video

1. Crea el proyecto con tu locución:

   ```bash
   bash tools/nuevo.sh mi-video noticia-cinematica ~/Descargas/locucion.wav
   ```

   Plantillas disponibles:
   - `pizarra`: estilo whiteboard con la mano y el lápiz.
   - `noticia-cinematica`: oscuro, 3D, con subtítulos karaoke.

   El script copia la plantilla, prepara el audio y transcribe la voz con tiempos por palabra.

2. Abre Claude Code en `novapsis-studio` y pega tu prompt indicando la carpeta: _"Proyecto producciones/mi-video, aquí está el brief…"_.
3. Mientras trabajo, puedes ver el video en vivo:
   ```bash
   cd producciones/mi-video && npx hyperframes preview
   ```
4. Render final, a -14 LUFS y listo para Instagram:
   ```bash
   bash tools/finalizar.sh producciones/mi-video Nombre_Final.mp4
   ```

## 5. Estructura

```
novapsis-studio/
  CLAUDE.md          ← instrucciones de la casa para Claude (estilo, reglas, QA)
  setup.sh           ← instalación
  tools/             ← nuevo.sh · transcribe.py · finalizar.sh
  shared/            ← logo, mano con lápiz, fuentes, GSAP
  templates/         ← pizarra · noticia-cinematica
  producciones/      ← tus videos (uno por carpeta)
```

## 6. Recursos que conviene añadir a `shared/brand/`

- **Logo vectorial de Novapsis y Novapsis 360:** SVG con trazados, no un PNG dentro de un SVG.
- **Capturas reales de Novapsis 360**, para demos sin recreaciones.
- **Música con licencia**, si se prefiere a la pista sintetizada.
- **Logos autorizados de terceros** (WhatsApp, USDT/USDC…), solo si hay permiso de uso.

## 7. Producciones anteriores

Las 7 producciones hechas en la nube están en `../productions/` de este mismo repo. Cualquiera se puede copiar a `producciones/` para reutilizarla.
