# ⌨️ Comandos

_Actualizado el 23/11/2026._

Esta es la lista de comandos del servidor y del bot de Discord. Los lugares a los que se viaja con `/warp` están en [Warps](warps.md). También está publicada en el canal **#comandos** del Discord, y dentro del juego puedes usar `/tutoriales`.

***

<!-- AUTO:inicio comandos -->
## 📜 Lista de comandos (generado)

> Esta lista se genera desde `wiki/tools/comandos.yml`, la misma fuente que usa la guía del canal #comandos de Discord. Para actualizarla: `python wiki/tools/generar_comandos.py`.

### 👋 Para empezar

**👋 Primeros pasos**

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/menu` | menú principal con todo el servidor | Todos | Towny |
| `/tutoriales` | guías de cada sistema dentro del juego | Todos | Towny |
| `/reglas` | reglas del servidor (léelas) | Todos | Towny |
| `/rtp` | viaja a un lugar aleatorio para empezar | Todos | Towny |
| `/recursos` | mundo de recursos para juntar materiales | Todos | Towny |
| `/linkear` | vincula tu cuenta con Discord (roles y premios) | Todos | Towny |

### 🏘️ Towny — towns y naciones

**Tu town**

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/t new <nombre>` | funda una town ($5.000) | Todos | Towny |
| `/t list` | lista de towns | Todos | Towny |
| `/t join <nombre>` | únete a una town | Todos | Towny |
| `/t claim` | reclama el chunk donde estás ($150, 8 por residente) | Todos | Towny |
| `/t deposit <monto>` | paga el mantenimiento (se cobra a las 12:00) | Todos | Towny |
| `/t spawn` | vuelve al spawn de tu town | Todos | Towny |
| `/t invite <jugador>` | invita a alguien a tu town | Todos | Towny |
| `/tf` | vuela dentro de tu town | TownyFlight | Towny |

**Parcelas y naciones**

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/plot forsale <precio>` | vende una parcela a un residente | Todos | Towny |
| `/plot set <tipo>` | shop, farm, arena, inn, embassy… | Todos | Towny |
| `/n new <nombre>` | crea una nación ($40.000) | Todos | Towny |
| `/n spawn` | viaja al spawn de tu nación | Todos | Towny |
| `/res` | tu información de residente | Todos | Towny |

### 💰 Economía y comercio

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/balance` | tu dinero | Todos | Towny |
| `/baltop` | los más ricos | Todos | Towny |
| `/pay <jugador> <monto>` | envía dinero a otro jugador | Todos | Towny |
| `/market` | mercado global con precios que cambian | Todos | Towny |
| `/ah` | casa de subastas | Todos | Towny |
| `/ah sell <precio>` | vende el ítem que tienes en la mano | Todos | Towny |
| `/qs create <precio>` | crea una tienda en un cofre | Todos | Towny |
| `/adminshop` · `/shop` | tienda del servidor | Todos | Towny |
| `/trade <jugador>` | intercambio seguro, sin estafas | Todos | Towny |

### 📈 Progreso

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/rankup` | mira tus requisitos y sube de rango | Todos | Towny |
| `/jobs browse` | trabajos disponibles | Todos | Towny |
| `/jobs join <trabajo>` | únete a un trabajo (máx. 3) | Todos | Towny |
| `/skills` | habilidades RPG | Todos | Towny |
| `/trinkets` | tus amuletos | Todos | Towny |
| `/minar` | progresión de minería | Todos | Towny |
| `/pesca` | progresión de pesca | Todos | Towny |
| `/granja` | progresión de agricultura | Todos | Towny |
| `/enchanter` | encantamientos únicos | Todos | Towny |
| `/enchantdex` | ver todos los encantamientos | Todos | Towny |
| `/crafteos` | recetas exclusivas del servidor | Todos | Towny |
| `/brew info` | recetas de Brewery | Todos | Towny |
| `/misiones` | misiones diarias con recompensa | Todos | Towny |
| `/rewards` | recompensas diarias, semanales y mensuales | Todos | Towny |
| `/bp` | Pase de Batalla | Todos | Towny |
| `/limite` | cuánta XP llevas hoy por habilidad y cuánto te falta; el límite se reinicia a las 7:30 AM | Todos | Towny |
| `/recetas` | menú de recetas personalizadas del servidor | Todos | Towny |
| `/cratekey balance` | cuántas llaves de cajas tienes (las llaves ahora son virtuales) | Todos | Towny |

### 🎉 Eventos y diversión

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/vote` | vota cada día: premios y la Piñata al llegar a 40 votos | Todos | Towny |
| `/warp koth` | KOTH cada 4 horas: domina la zona | Todos | Towny |
| `/warp dungeons` | dungeons con jefes y recompensas | Todos | Towny |
| `/warp cajas` | abre tus llaves | Todos | Towny |
| `/warp parkour` | minijuego de parkour | Todos | Towny |
| `/warp spleef` | minijuego Spleef | Todos | Towny |
| `/warp tntrun` | minijuego TNT Run | Todos | Towny |
| `/warp PropHunt` | minijuego de escondite de objetos | Todos | Towny |
| `/warp FallGuy` | minijuego Fall Guys: carrera de obstáculos | Todos | Towny |
| `/mpk lobby` | menú de parkours: elige uno y entra | Todos | Towny |
| `/warp piñata` | zona de la Piñata | Todos | Towny |
| `/warp evento` | sala de eventos | Todos | Towny |
| `/warp preduels` | sala de espera PvP | Todos | Towny |
| `/duel <jugador>` | duelo 1v1 | Todos | Towny |
| `/warp coliseo` | arena de duelos | Todos | Towny |
| `/cf` | CoinFlip | Todos | Towny |
| `/warp casino` | CoinFlip y apuestas | Todos | Towny |
| `/loteria` | lotería: sorteos todos los días a las 14:00 y 21:00 (boleto $2.000) | Todos | Towny |
| `/warp comunidad` | zona social | Todos | Towny |
| `/warp iglesia` | iglesia: sistema de bodas | Todos | Towny |
| `/warp Vehiculos` | garaje y transporte | Todos | Towny |
| `/warp cosmeticos` | zona de cosméticos | Todos | Towny |
| `/pp` | partículas | Todos | Towny |
| `/skin <nombre>` | cambia tu skin | Todos | Towny |
| `/petcapturehelper` | cómo capturar mascotas | Todos | Towny |
| `/mascotasespeciales` | tienda de 200 mascotas con modelo 3D (se pagan con MapuPoints) | Todos | Towny |
| `/mapucraft` | menú de MapuCore: modelos, materiales, nombre, lore, spawners, llaves y claims | Todos | Towny |
| `/modelo` | aplica o quita un modelo custom de un ítem | Todos | Towny |
| `/materiales` | elige un material de construcción y recibe una shulker llena | Todos | Towny |
| `/warp afk` | 2 MapuPoints por hora estando AFK | Todos | Towny |
| `/warp tops` | los mejores jugadores | Todos | Towny |

### 🛠️ Utilidades

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `/back` | vuelve a donde moriste | Todos | Towny |
| `/pvp` | activa o desactiva tu PvP (1 h de espera) | Todos | Towny |
| `/basurero` | elimina ítems que no necesitas | Todos | Towny |
| `/chatdevoz` | cómo usar el chat de voz (Simple Voice Chat) | Todos | Towny |
| `/premium` | si tienes cuenta premium, entra sin contraseña | Cuenta premium | Towny |
| `/mapa` | mapa web del servidor | Todos | Towny |
| `/wiki` | enlace a la wiki | Todos | Towny |
| `/discord` | enlace al Discord | Todos | Towny |
| `/tienda` | tienda del servidor (donaciones) | Todos | Towny |
| `/feed` | recupera tu hambre (cada 2 h) | KumeChe o superior | Towny |
| `/ender` | abre tu cofre ender (cada 2 h) | Weupife o superior | Towny |
| `/workbench` | abre una mesa de crafteo | Genpin o superior | Towny |

### 🤖 Comandos del bot en Discord

Úsalos con `m!` o con `/` en #canal.

**Minecraft y Towny**

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `m!perfil <nick>` | perfil, town, tiempo jugado y votos | Todos | Discord |
| `m!town <nombre>` | ficha de una town | Todos | Discord |
| `m!mitown` | la ficha de tu town | Todos | Discord |
| `m!nacion <nombre>` | ficha de una nación | Todos | Discord |
| `m!naciones` | todas las naciones | Todos | Discord |
| `m!towns` | ranking por residentes, chunks o antigüedad | Todos | Discord |
| `m!vincular` | cómo vincular tu cuenta | Todos | Discord |
| `m!premios` | tus premios pendientes en el juego | Todos | Discord |
| `m!status` | estado del servidor | Todos | Discord |

**Comunidad**

| Comando | Descripción | Quién puede | Modo |
|---|---|---|---|
| `m!help` | todos los comandos del bot | Todos | Discord |
| `m!ciudad registrar` | publica tu town en el foro (en #canal) | Alcalde (si la verificación está activa) | Discord |
| `m!suggest` | envía una sugerencia (también en #canal) | Todos | Discord |
| `m!vote` | votos | Todos | Discord |
| `m!rangos` | rangos | Todos | Discord |
| `m!kits` | kits | Todos | Discord |
<!-- AUTO:fin comandos -->

***

## 🆕 Comandos de los sistemas nuevos (noviembre 2026)

Estos comandos son de los sistemas propios de Mapucraft que llegaron en noviembre. Todos son para **todos los jugadores**.

### 🎮 Juegos y eventos

| Comando | Descripción | Más info |
|---|---|---|
| `/sumo` | menú del sumo (alias `/mapusumo`) | [Sumo](../towny/sumo.md) |
| `/sumo unirse <arena>` · `/sumo salir` · `/sumo lista` | entrar, salir y ver las arenas | [Sumo](../towny/sumo.md) |
| `/sumo top [métrica] [página]` · `/sumo stats [jugador]` | ranking y estadísticas del sumo | [Sumo](../towny/sumo.md) |
| `/sumo apostar <monto\|aceptar\|rechazar\|cancelar\|sin>` | apuesta opcional en tu duelo | [Sumo](../towny/sumo.md) |
| `/sumo apostar <jugador> <monto>` | apuesta de espectador a quién gana | [Sumo](../towny/sumo.md) |
| `/bingo` | cartón del Bingo Diario (alias `/bd`) | [Bingo Diario](../towny/bingo-diario.md) |
| `/bingo entregar` · `/bingo top [dia\|semana\|mes\|total]` · `/bingo racha` · `/bingo premios` · `/bingo avisos [on\|off]` | jugar y consultar el Bingo Diario | [Bingo Diario](../towny/bingo-diario.md) |
| `/bingoevento` | menú del Bingo de Eventos (alias `/bingoe`) | [Bingo de Eventos](../towny/bingo-evento.md) |
| `/bingoevento comprar [n]` · `cartones` · `premios` · `bolas` | comprar y seguir tus cartones | [Bingo de Eventos](../towny/bingo-evento.md) |
| `/loteria auto <boletos> [rondas]` · `/loteria auto off` | compra automática de boletos | [Lotería](../towny/loteria.md) |
| `/mpk join <parkour>` · `/mpk leave` · `/mpk spawn` · `/mpk restart` · `/mpk checkpoint` | jugar los parkours cortos | [Parkours cortos](../towny/parkours.md) |
| `/mpk top <parkour>` · `/mpk stats` · `/mpk claim` | ranking, estadísticas y premios pendientes | [Parkours cortos](../towny/parkours.md) |
| `/chatgames top` · `/chatgames stats` · `/chatgames toggle` | juegos del chat (alias `/mapujuegos`) | [Juegos del chat](../towny/chatgames.md) |
| `/amigosecreto` | Amigo Secreto: `inscribirse`, `salir`, `amigo`, `regalar` | [Amigo Secreto](../towny/eventos/amigo-secreto.md) |
| `/adviento` · `/adviento premium` | Calendario de Adviento (desde el 1 de diciembre) | [Navidad](../towny/eventos/navidad.md) |
| `/kothjusto` | tus penalizaciones en el KOTH | [KOTH](../towny/eventos/koth.md) |

### 🧰 Utilidades

| Comando | Descripción | Más info |
|---|---|---|
| `/warps` | menú de warps (2 páginas) | [Warps](warps.md) |
| `/brujula` | menú de atajos; te devuelve la Brújula de Mapucraft si la perdiste | [MapuCore](../towny/mapucore.md) |
| `/mapucraft kits` | elegir un kit pendiente | [MapuCore](../towny/mapucore.md) |
| `/recetas buscar <texto>` · `/recetas como` · `/recetas usos` · `/recetas puedo` | buscar recetas y ver para qué sirve un ítem | [Crafteos](../towny/crafteos.md) |
| `/mochilas` | abrir tu mochila (o clic derecho con ella en la mano) | [Mochilas](../towny/mochilas.md) |
| `/renovacion` | estado de tu rango y de su renovación (alias `/renovar`) | [Renovación](../towny/renovacion-de-rangos.md) |
