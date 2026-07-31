# 🚜 Granjas: Límites y Mecánicas de Mobs

El servidor tiene varias capas de optimización para evitar lag, todas pensadas para que las granjas sigan funcionando sin romper el rendimiento para el resto de jugadores. Aquí te explicamos cómo funciona la generación, activación y despawn de mobs, y qué límites debes tener en cuenta al diseñar tu granja.

***

## 📡 Generación natural de mobs

* **Rango de generación:** los mobs solo aparecen dentro de un radio de **4 chunks** (64 bloques) alrededor de cada jugador.
* **Spawns por jugador:** el servidor usa generación **por jugador**, no un cupo global del mundo. Esto significa que si hay varios jugadores AFK en distintas granjas, no compiten entre sí por el mismo límite de mobs — cada uno tiene su propia "cuota" cerca suyo.

> 💡 Si tu granja no genera mobs, revisa que estés dentro de los 64 bloques del punto de spawn y que el área esté bien iluminada/oscura según el tipo de mob.

***

## 👁️ Activación de IA (Entity Activation Range)

Los mobs no "piensan" todo el tiempo — su IA solo se activa cuando un jugador está dentro de cierta distancia. Fuera de ese rango, el mob existe pero no se mueve ni reacciona (aunque sistemas automáticos como caídas o ahogamiento sí lo pueden matar).

| Tipo de entidad | Rango de activación |
|---|---|
| Animales | 16 bloques |
| Monstruos | 24 bloques |
| Raiders (pillagers, etc.) | 48 bloques |
| Voladores (phantom, ghast, etc.) | 48 bloques |
| Aldeanos | 16 bloques |
| Entidades acuáticas | 12 bloques |
| Misceláneo | 8 bloques |

Además, el servidor "despierta" periódicamente mobs inactivos para evitar que se queden congelados para siempre: por ejemplo, hasta 4 monstruos cada 400 ticks (20s) se reactivan brevemente aunque no haya jugadores cerca.

> 💡 Para granjas con sistema de muerte automático (caída, ahogo, lava) esto no es un problema porque no depende de la IA. Pero si tu granja necesita que los mobs caminen o ataquen, asegúrate de estar dentro del rango de activación correspondiente.

***

## 👻 Despawn de mobs

Si ningún jugador está lo bastante cerca, los mobs comienzan a desaparecer:

| | Distancia |
|---|---|
| **Despawn suave (soft)** | a partir de 30 bloques, hay una probabilidad de despawn cada intento |
| **Despawn duro (hard)** | a los 64 bloques, el mob desaparece sí o sí |

Esto aplica a monstruos, animales, axolotes y la mayoría de criaturas. Es más estricto que el Minecraft vanilla normal, así que en granjas AFK **no te alejes más de 64 bloques** del punto donde se generan/acumulan los mobs, idealmente mantente dentro de los 30 bloques para evitar perder mobs antes de matarlos.

***

## 🧱 Spawners

* **IA desactivada:** los mobs generados por un spawner de monstruos tienen su IA "nerfeada" (no atacan ni se mueven de forma normal) — están pensados para ser eliminados por un sistema automático, no para luchar contra ellos.
* **Frecuencia:** los spawners revisan si pueden generar un mob cada 2 ticks, con un retraso vanilla de entre 200 y 800 ticks (10 a 40 segundos) entre cada intento de spawn.

***

## 🧹 MobFarmManager — limpieza automática de entidades

**MobFarmManager** es el plugin que evita que se acumulen demasiadas entidades en una misma zona. En simple: cada cierto tiempo revisa los chunks donde hay jugadores y, si encuentra más entidades de las permitidas, borra el exceso.

* Revisa el área cada **30 segundos**.
* Agrupa varios chunks alrededor del jugador (un área de 5x5 chunks) para calcular los límites, en vez de mirar cada chunk por separado.
* Algunos límites importantes por grupo de chunks:

| Entidad | Límite |
|---|---|
| Animales en general (categoría) | 60 |
| Monstruos en general (categoría) | 80 |
| Iron Golem | 5 |
| Aldeano | 15 |
| Wither | 5 |
| Warden | 8 |
| Ender Dragon | 3 |
| Zombified Piglin | 40 |
| Mobs hostiles comunes (zombie, esqueleto, creeper, araña, slime, drowned, husk...) | 20 |
| Animales comunes (vaca, cerdo, oveja, gallina) | 20 |
| Snow Golem | 20 |
| Falling blocks (bloques cayendo) | 10 |
| Flechas | 20 |

* **Qué NO se borra:** animales domesticados (con correa), con nombre personalizado, con silla de montar, bebés, armor stands con items puestos, e item frames con items — todos quedan protegidos de la limpieza automática.

***

## 🧠 Optimización de IA a distancia (DAB)

El servidor usa **DAB** (*Distant Activation of Behaviors*), un sistema que ahorra rendimiento reduciendo cada cuánto "piensan" los mobs que están **lejos** de los jugadores, sin congelar a los que tienes cerca.

* Los mobs a más de **12 bloques** de cualquier jugador empiezan a ticar su IA (pathfinding y comportamiento) con menos frecuencia.
* Cuanto más lejos está el mob, menos seguido reacciona, hasta un mínimo de una vez por segundo (20 ticks) para los más lejanos.
* Los mobs **cerca de ti se comportan con total normalidad**: este sistema reemplazó a un control anterior que a veces "congelaba" mobs de forma rara y molesta, así que esa sensación ya no debería ocurrir.

**Entidades excluidas** (siempre tican normal, sin importar la distancia):

| Entidad | Por qué está excluida |
|---|---|
| 🧑‍🌾 Aldeano | Granjas de trading y de reproducción de aldeanos siguen funcionando |
| 🦎 Axolote | Evita que se queden inmóviles bajo el agua |
| 🐗 Hoglin | Comportamiento en el Nether intacto |
| 🧟 Piglin zombificado | Granjas de oro y portales siguen funcionando |
| 🐐 Cabra | Comportamiento intacto |

> 💡 En la práctica esto es **mejor para tus granjas**: los mobs con los que interactúas de cerca ya no se "traban", y las granjas de las entidades excluidas no se ven afectadas por la reducción de IA a distancia (siempre dentro de los límites de despawn y activación de arriba).

***

## 🔧 Otros detalles útiles para construir granjas

* **Tolvas (hoppers):** funcionan aunque tengan un bloque sólido encima (no necesitas dejarlas "abiertas" hacia arriba), y se ajustan automáticamente para no sobrecargar el servidor si están muy activas.
* **Agrupado de items y experiencia:** los items en el suelo se agrupan en un radio de 4 bloques y los orbes de experiencia en 6 bloques, para reducir la cantidad de entidades sueltas.
* **Tiempo de despawn de items:** alrededor de 4.5 minutos — recuerda recoger el loot de tu granja antes de que desaparezca.
* **TNT:** el servidor procesa hasta 80 bloques de TNT detonados por tick, útil si usas granjas basadas en TNT (duplicadores de arena, cactus, etc.).
* **Colisiones entre entidades:** se limitan a un máximo de 3 entidades empujándose entre sí a la vez, para que las granjas muy densas no generen lag extra por el empuje constante de mobs.

***

{% hint style="info" %}
Estos sistemas (MobFarmManager y DAB) están pensados para proteger el rendimiento del servidor para todos los jugadores. Si tu granja "pierde" mobs o items, lo más probable es que estés superando alguno de los límites de MobFarmManager de esta página — repártela en varias zonas o reduce la densidad para evitar la limpieza automática.
{% endhint %}
