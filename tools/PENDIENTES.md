# Pendientes de la wiki


La modalidad Skyblock se archivó el 2026-11-01: sus páginas están en `_archivo/skyblock/` (fuera del índice y de la web). Para recuperarla: `git mv _archivo/skyblock skyblock` y volver a agregar la sección al `SUMMARY.md` y a la portada.

## Guía de comandos

- La columna «permiso» vale `todos` salvo `/tf` (TownyFlight), `/premium` (cuenta premium), `/feed`, `/ender` y `/workbench` (rangos según `towny/rangos.md`) y `m!ciudad registrar` (alcalde). No se verificaron los permisos de LuckPerms comando por comando.
- Los comandos `/feed`, `/ender` y `/workbench` salen de `towny/rangos.md`, no de la guía original de Discord; confirmar nombres y esperas en el juego.

## Revisión de producción 2026-11-08 (confirmar en juego)

- **Cofre ender de Toki/Cacique/Ulmen/Especial:** los permisos de LuckPerms dan 6 filas a Toki (`purpur.enderchest.rows.six` en el grupo `toki`) y los demás lo heredan; Cacique y Ulmen solo definen 5, pero Purpur toma la mayor. La wiki antes decía 4/5/5. Si la intención era 4/5/5, hay que quitar `six` de `toki`.
- **Hogares de Toki:** el grupo define 7, pero hereda de `machife` (8); CMI toma el mayor, así que Toki = 8. Si no se quiere, quitar `machife` de sus padres (ojo: también heredaría ranuras de amuletos).
- **Warps que la wiki/menús mencionan pero no existen en `CMI/Saves/Warps.yml`:** `comercio` (también en los tutoriales de Nascraft y QuickShop del menú), `mercado`, `modelos` (MapuCore), `personalizados`, `BossSemanal`, `buildbattle`, `laberinto`, `predungeon` (menú de AdvancedEnchantments). Warps que existen: coliseo, preduels, koth, dungeons, tntrun, spleef, PropHunt, FallGuy, parkour, piñata, evento, Halloween, cumpleaños, Concierto, comunidad, casino, cajas, tops, cosmeticos, iglesia, juzgado, save, afk, Vehiculos (+ Carcel, sin menú).
- Parkours (`MapuParkours`): 4 parkours listos pero sin recompensas configuradas (`reward-items` y `reward-commands` vacíos, enfriamiento 24 h).

## Datos generados

- `towny/crafteos.md`: los ingredientes vanilla aparecen con su nombre en inglés (Netherite Scrap, Gold Block…) porque la base de CraftEnhance solo guarda el nombre del material. Los ítems custom salen con su nombre en español.
- `towny/economia/mercado.md`: los precios son los iniciales de Nascraft; los impuestos de compra/venta por ítem no se incluyen.
- `towny/cajas.md`: la sección generada convive con el texto manual de arriba, que ya no está sincronizado con la config (por ejemplo, el texto manual habla de 6 cajas de progresión y de probabilidades aproximadas). Revisar y, si se quiere, borrar lo manual que quede desactualizado.
- Rangos: no se generan (ver `README.md`).

## Temporada 2 (revisar al publicar)

- La versión de Minecraft (26.3), la fecha de apertura (24/10/2026, tomada de la configuración del portal) y la invitación de Discord (YDJKpgEU3m, la misma que usan las webs) se escribieron a partir de los archivos del servidor y las webs: confirmarlas.
- Las páginas towny/encantamientos.md, towny/mascotas.md y towny/battlepass.md tienen secciones generadas: tras cambiar esos plugins ejecuta los generadores (ver README.md).

## Auditoría de MyPet 2026-11-08 (solo lectura; no se cambió nada en el servidor)

- Las 190 mascotas de la tienda tienen tipo en `pet-config.yml`, vida y velocidad propias y entre 4 y 9 árboles; los 171 árboles se pueden alcanzar (sin requisitos ni herencias rotas). Nombres, rarezas y precios coinciden entre la tienda de DeluxeMenus y el catálogo web.
- 14 árboles citan tipos que no existen en `pet-config.yml` (`Chameleon` en 8 y `Capybara` en 6): MyPet los ignora; se pueden quitar de los `MobTypes`.
- Cinco descripciones genéricas se repiten en 25 mascotas («Una criatura voladora legendaria», «Una criatura voladora», «Un globito que te sigue», «Un gólem de piedra mágica», «Un zorro de nueve colas»).
- 63 mascotas no pueden usarse de montura en ningún árbol (los 6 Globos, los Cubee dulces, etc.) y 41 no tienen habilidad de daño (mascotas de apoyo). Es decisión de diseño; confirmar que es lo que se quiere.
- Cómo regenerar: `python tools/mypet_datos.py <plugins> <servidor-web>/public/assets/mascotas/detalle.json` y `generar_wiki.py --solo fichas --solo arboles`.
