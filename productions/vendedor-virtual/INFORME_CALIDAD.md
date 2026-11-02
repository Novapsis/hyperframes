# Novapsis 360 — Cómo Funciona un Vendedor Virtual · Informe

## Entregables

- **Proyecto:** `index.html`, generado con `python3 build/build.py`. Es una pizarra de 14 zonas recorrida por la cámara, con 85 trazos y escrituras sincronizados y la mano suministrada por el usuario. El motor es el mismo del video "4 cuadrantes".
- **Video:** `Novapsis360_Como_Funciona_Vendedor_Virtual.mp4`, 1080×1920, 30 fps, H.264/AAC, 98,7 s, −14,0 LUFS y pico de −1,0 dBFS.
- **Portada:** `portada_instagram.png`, generada desde `build/cover.html`.
- **Subtítulos:** `subtitulos.srt`, también quemados en el video.
- **Sincronización:** `build/ops.json`.
- **Música y efectos:** `build/make_audio.py`, síntesis original. Incluye notificaciones, campana, persiana, sellos y confirmaciones.

## Audio

- La locución se usó sin cambios de velocidad: el ritmo es parejo, de 96,3 s.
- Única edición: +0,6 s de pausa después de "¿Cuántas oportunidades de venta se están perdiendo?".
- La alineación se hizo por pausas medidas con FFmpeg, porque Whisper no está disponible en este entorno.

## Escenas clave

- **Mañana:** tienda con un reloj que marca las 7:00 AM; se abre la persiana y se enciende el cartel ABIERTO.
- **Clientes:** tres clientes con sus burbujas (batería, cadena, factura) mientras el dueño va de la estantería a la caja. Al mismo tiempo, cinco mensajes de WhatsApp entran uno tras otro.
- **Cierre:** las 5:00 PM, se baja la persiana, CERRADO y tres mensajes sin responder.
- **La pregunta:** "?" grande y una flecha incompleta de CONSULTA a OPORTUNIDAD DE VENTA; la mano se queda congelada.
- **Diagrama:** WhatsApp → Vendedor virtual → Información del negocio → Productos / Precios / Inventario / Horarios.
- **Demos:**
  - **Bujía:** Consultando inventario → tarjeta DISPONIBLE → respuesta.
  - **Cotización:** borrador marcado PREPARADA, con precios de ejemplo y la nota "no es una factura".
  - **Envíos:** las opciones Envío y Retiro en tienda.
  - **QR en la tienda:** un cliente escanea el código y recibe la respuesta por WhatsApp.
- **Concurrencia:**
  1. La mano dibuja el teléfono y las cuatro conexiones y se retira.
  2. Los cuatro chats reciben y responden con tiempos solapados.
  3. Los paquetes de datos siguen fluyendo sin la mano y sigue apareciendo "nuevo mensaje".
- **Todo organizado:** carpetas de Consultas, Pedidos y Facturas, una factura PREPARADA y un registro PENDIENTE DE VALIDACIÓN.
- **Control humano:** Verificar pago y Coordinar entrega, con check humano.
- **Resumen:** la tienda cerrada de noche y el canal digital sigue atendiendo.
- **Cierre:** "Recupera tu tiempo" y AGENDA escrita a mano, con el logo.

## Veracidad

- Todo está marcado como DEMO: chats, QR ("QR DEMO", no funcional) y precios de ejemplo.
- La cotización y la factura aparecen solo como preparadas o pendientes. No se muestran pagos verificados por la IA ni ventas cerradas.
- Envíos y horarios aparecen "según tus políticas" y "horario configurado".

## Pendientes

1. Comprobar que el comentario AGENDA tenga respuesta, automática o manual.
2. Logo vectorial de Novapsis: el que hay es un PNG extraído del SVG suministrado.
3. QR real: si se quiere uno funcional, hace falta el enlace oficial de WhatsApp del negocio.
4. Mano: es la ilustración suministrada por el usuario, no fotográfica. Es una imagen fija y en algunos trazos tapa parte del dibujo por un instante.
