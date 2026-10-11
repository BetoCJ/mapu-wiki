# Pendientes de la wiki

## Comparación Towny vs Skyblock

Se compararon las 12 páginas que existen con el mismo nombre en `towny/` y `skyblock/` (battlepass, brewery, cajas, cosmeticos, crafteos, economia/README, economia/tiendas, encantamientos, minijuegos, misiones-y-recompensas, README y skills).

Resultado: **ninguna es idéntica ni está copiada de Towny**. Cada una tiene contenido propio de Skyblock (Küyen, Antü, Wenu Mapu, minions, islas, etc.) y no aparecen términos exclusivos de Towny (towns, naciones, KOTH, dungeons, rangos Winka-Machife). Por eso no se agregó ninguna nota `> Pendiente de revisar para Skyblock` en las páginas.

Lo que sí queda por revisar a mano, porque no hay forma de comprobarlo con los datos locales (solo existe la config de Towny):

| Página | Qué revisar |
|---|---|
| `skyblock/cajas.md` | Comparte con Towny el nombre «Caja Mapu» y el warp `/warp cajas`. Confirmar que esas dos cosas existen de verdad en Skyblock. |
| `skyblock/economia/README.md` | Describe `/tienda` y `zAuctionHouse`; en Towny la subasta es `/ah` con otro plugin. Confirmar el plugin y los comandos. |
| `skyblock/minijuegos.md` | Menciona `/ctf`, `/ffa`, `/dm`, `/bg`, `/col` (BattleArena). Confirmar que siguen activos. |
| `wiki/README.md` | Dice que Skyblock es «Próximamente», pero hay decenas de páginas publicadas de ese modo. Decidir cuál es la verdad. |

Páginas de Towny sin equivalente en Skyblock (no es un error, solo no existen allí): coinflip, comercio, dungeons, eventos, jobs, límites de granjas, rangos, towns, economia/mercado, y las tres Pyro con nombre distinto (pyromining/pyromineria, etc.).

## Guía de comandos

- Todos los comandos de `comandos.yml` están en modo `towny` (o `discord` para el bot), porque la guía original era de Towny. No se catalogaron comandos de Skyblock. Los de uso general (`/menu`, `/reglas`, `/wiki`, `/discord`…) probablemente sirvan en ambos modos; cuando alguien lo confirme, cambiar `modo` a `ambos`.
- La columna «permiso» vale `todos` salvo `/tf` (TownyFlight), `/premium` (cuenta premium), `/feed`, `/ender` y `/workbench` (rangos según `towny/rangos.md`) y `m!ciudad registrar` (alcalde). No se verificaron los permisos de LuckPerms comando por comando.
- Los comandos `/feed`, `/ender` y `/workbench` salen de `towny/rangos.md`, no de la guía original de Discord; confirmar nombres y esperas en el juego.

## Datos generados

- `towny/crafteos.md`: los ingredientes vanilla aparecen con su nombre en inglés (Netherite Scrap, Gold Block…) porque la base de CraftEnhance solo guarda el nombre del material. Los ítems custom salen con su nombre en español.
- `towny/economia/mercado.md`: los precios son los iniciales de Nascraft; los impuestos de compra/venta por ítem no se incluyen.
- `towny/cajas.md`: la sección generada convive con el texto manual de arriba, que ya no está sincronizado con la config (por ejemplo, el texto manual habla de 6 cajas de progresión y de probabilidades aproximadas). Revisar y, si se quiere, borrar lo manual que quede desactualizado.
- Rangos: no se generan (ver `README.md`).
