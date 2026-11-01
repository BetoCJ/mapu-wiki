# Pendientes de la wiki


La modalidad Skyblock se archivó el 2026-11-01: sus páginas están en `_archivo/skyblock/` (fuera del índice y de la web). Para recuperarla: `git mv _archivo/skyblock skyblock` y volver a agregar la sección al `SUMMARY.md` y a la portada.

## Guía de comandos

- La columna «permiso» vale `todos` salvo `/tf` (TownyFlight), `/premium` (cuenta premium), `/feed`, `/ender` y `/workbench` (rangos según `towny/rangos.md`) y `m!ciudad registrar` (alcalde). No se verificaron los permisos de LuckPerms comando por comando.
- Los comandos `/feed`, `/ender` y `/workbench` salen de `towny/rangos.md`, no de la guía original de Discord; confirmar nombres y esperas en el juego.

## Datos generados

- `towny/crafteos.md`: los ingredientes vanilla aparecen con su nombre en inglés (Netherite Scrap, Gold Block…) porque la base de CraftEnhance solo guarda el nombre del material. Los ítems custom salen con su nombre en español.
- `towny/economia/mercado.md`: los precios son los iniciales de Nascraft; los impuestos de compra/venta por ítem no se incluyen.
- `towny/cajas.md`: la sección generada convive con el texto manual de arriba, que ya no está sincronizado con la config (por ejemplo, el texto manual habla de 6 cajas de progresión y de probabilidades aproximadas). Revisar y, si se quiere, borrar lo manual que quede desactualizado.
- Rangos: no se generan (ver `README.md`).

## Temporada 2 (revisar al publicar)

- La versión de Minecraft (26.3), la fecha de apertura (24/10/2026, tomada de la configuración del portal) y la invitación de Discord (YDJKpgEU3m, la misma que usan las webs) se escribieron a partir de los archivos del servidor y las webs: confirmarlas.
- Las páginas towny/encantamientos.md, towny/mascotas.md y towny/battlepass.md tienen secciones generadas: tras cambiar esos plugins ejecuta los generadores (ver README.md).
