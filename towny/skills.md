# ⚔️ Skills — ValhallaMMO y ValhallaTrinkets

## 📖 Introduccion — Empieza aqui

Si es la primera vez que ves este sistema, lee esto antes de continuar.

### ❓ ¿Que es ValhallaMMO?

ValhallaMMO es un plugin RPG que reemplaza el sistema de habilidades vanilla de Minecraft. Al jugar normalmente — minar, talar, pelear, pescar — vas subiendo de nivel en 14 skills distintas. Subir de nivel desbloquea mejoras permanentes llamadas **perks**.

No necesitas hacer nada especial para empezar: desde el primer bloque que mines o el primer mob que mates ya estaras ganando XP.

### 🔁 El loop de juego

```
Juegas normalmente
       ↓
Ganas XP en el skill correspondiente
       ↓
El skill sube de nivel → Power recibe XP automaticamente
       ↓
Power sube de nivel → obtienes puntos de habilidad
       ↓
Gastas puntos en el arbol de perks de cualquier skill
       ↓
Desbloqueas mejoras permanentes
```

### 📋 Las 16 skills

Con la actualización **Premium** se suman dos skills nuevas: **Artes Marciales** y **Comercio**. Ahora hay **16 skills** en el plugin, de las cuales **14 están activas** en el servidor. **Enchanting** y **Smithing** están desactivadas (ver más abajo).

| Categoria | Skills |
|---|---|
| Recoleccion | Mining, Woodcutting, Digging, Farming, Fishing |
| Artesania | Alchemy |
| Combate | Light Weapons, Heavy Weapons, Light Armor, Heavy Armor, Archery, **Artes Marciales** ✨ |
| Economia | **Comercio** ✨ |
| Central | Power |
| ❌ Desactivadas | Enchanting, Smithing |

{% hint style="success" %}
✨ **Novedad Premium:** Artes Marciales (combate sin armas y con nudilleras) y Comercio (mejores tratos y servicios con aldeanos). Mira su sección más abajo y la [página de Comercio](comercio.md).
{% endhint %}

| Skill | Como ganar XP |
|---|---|
| Mining | Minando bloques (diamante, obsidiana y minerales raros dan mas XP) |
| Woodcutting | Talando troncos de madera |
| Digging | Cavando tierra, arena, grava, barro |
| Farming | Cosechando cultivos maduros |
| Fishing | Pescando |
| Alchemy | Elaborando pociones en calderos y soportes de pociones |
| Smithing | ❌ Desactivado en el servidor (la herrería funciona en modo vanilla) |
| Light Weapons | Pegando con espadas, dagas o cuchillos |
| Heavy Weapons | Pegando con hachas o mazas |
| Light Armor | Recibiendo daño con armadura ligera equipada |
| Heavy Armor | Recibiendo daño con armadura pesada equipada |
| Archery | Disparando flechas con arco o ballesta |
| Artes Marciales ✨ | Peleando sin arma (a puños) o con nudilleras |
| Comercio ✨ | Comerciando con aldeanos (mas XP cuanto mejor el trato y mayor el rango del mercader) |
| Power | Sube automaticamente cada vez que sube cualquier otro skill |

### ❓ Que es Power

**Power** es el skill central (nivel maximo 256). No lo subes directamente: cada vez que cualquier otra skill sube de nivel, Power recibe XP automaticamente. Al subir Power obtienes **1 punto de habilidad** por nivel, que son los que usas para desbloquear perks.

### ❓ Que son los Perks

Los perks son mejoras permanentes organizadas en un arbol visual. Cada perk tiene:
- Un **nivel minimo** del skill requerido para desbloquearlo
- Un **costo en puntos de habilidad** (obtenidos de Power)

Para ver el arbol de un skill usa `/val skilltree [skill]` en el juego. Los perks desbloqueados no se pierden al morir ni al reiniciar el servidor.

### ⚔️ Como es diferente el combate

ValhallaMMO añade mecanicas de combate encima del sistema vanilla:

| Mecanica | Descripcion |
|---|---|
| Criticos | Probabilidad propia del plugin, no del vanilla |
| Sangrado | Dano en ticks tras un golpe, apilable |
| Parry | Bloqueo activo que contraataca al atacante |
| Evasion | Chance de esquivar un ataque completamente |
| Stun | Ralentizacion + ceguera + debilidad temporales |
| Tipos de dano | Melee, bludgeoning, projectile, fire, magic, radiant, necrotic |
| Armadura | Formula vanilla — la proteccion funciona igual que en Minecraft base |
| Anti-oneshot | Ningun jugador puede morir de un solo golpe por defecto |

La armadura ligera y pesada funcionan diferente entre si. La ligera da mas evasion y movilidad; la pesada da mas resistencia bruta y reflejo de dano.

Desde nivel 0 en los skills de combate, las armas y armaduras funcionan con su efectividad vanilla completa. Subir los skills de armadura y armas añade bonificaciones **por encima** de esa base, no recupera ningun deficit.

---

{% hint style="warning" %}
**Ajustes de balance (octubre y noviembre 2026):** los bonos positivos de los perks (daño, velocidad, drops, XP, regeneración, etc.) se rebajaron un **25%** en octubre. El **2 de noviembre** las skills de combate (Light Weapons, Heavy Weapons, Light Armor, Heavy Armor y Artes Marciales) recibieron **otro 25%** de rebaja, y los amuletos bajaron un **50%** (ver más abajo). Archery no recibió ese segundo recorte: al contrario, su penalización inicial se redujo a la mitad. No cambiaron los cooldowns, duraciones, cargas ni desbloqueos. Las tablas de esta página ya muestran los valores nuevos; los exactos de tu personaje se ven con `/val skilltree [skill]`.
{% endhint %}

---

## 💍 ¿Que es ValhallaTrinkets?

ValhallaTrinkets es un plugin complementario que añade **accesorios equipables** (trinkets) con bonos pasivos permanentes. Se accede con `/trinkets`.

### ⚙️ Como funcionan los trinkets

- Abres el menu con `/trinkets` — se abre una ventana separada de tu inventario normal
- Tienes hasta **7 ranuras** de trinket: las 5 primeras son para todos, la **6.ª** se desbloquea con el rango **Genpin** y la **7.ª** con **Machife**. Los rangos de donación **Toki, Cacique, Ulmen y Especial** también traen las 7 (Weichafe no agrega ranuras). No se suman entre sí: cuenta la mayor. Detalle en [Rangos](rangos.md)
- Cada trinket da uno o varios atributos: daño, velocidad, resistencia, critico, etc.
- Todos los trinkets del servidor comparten la misma categoria interna ("Accesorio"), asi que **puedes combinar hasta 7 trinkets distintos a la vez** — no hay una restriccion de "uno por tipo" como anillo/collar/etc.
- Los trinkets **se dropean al morir** (a menos que el servidor tenga keepInventory activo)
- Los bonos son pasivos: no tienes que hacer nada, se aplican solos mientras los tengas equipados

### 🎁 Como conseguir trinkets

Los trinkets **no se consiguen matando mobs ni minando bloques** normales. Se encuentran explorando estructuras del mundo, haciendo arqueologia, o pescando.

**Estructuras con cofres:**

| Estructura | Notas |
|---|---|
| Mazmorra (dungeon) | Cofres de spawner subterraneos |
| Mina Abandonada | Cofres en los mineshafts |
| Fortaleza (stronghold) | Pasillo y biblioteca |
| Puesto Pillager | Cofres superiores |
| Mansion del Bosque | Woodland Mansion |
| Portal Arruinado | En superficie o subterraneo |
| Bastion (Nether) | Cofre del tesoro |
| Fortaleza del Nether | Nether Bridge |
| Ciudad Antigua | Deep Dark |
| Ciudad del End | End City |
| Templo de la Jungla | Jungle Temple |
| Templo del Desierto | Desert Pyramid |
| Ruinas Submarinas | Underwater Ruin (grandes) |
| Nave Hundida | Cofre del tesoro |
| Tesoro Enterrado | Buried Treasure |
| Iglú | Cofre del sotano |
| Aldea | Herrero, armero y herramienta |

**Arqueologia:**

| Sitio | Como excavarlo |
|---|---|
| Templo del Desierto | Bloques de arena sospechosa |
| Ruinas del Camino | Trail Ruins, bloque raro |
| Ruinas Oceanicas | Warm y cold ocean ruins |

**Pesca:** Los trinkets pueden aparecer como tesoro al pescar.

**Probabilidad:** cada cofre de estas estructuras tiene una probabilidad cercana al **10%** de incluir un trinket adicional, repartida entre los **36 trinkets** del servidor con el mismo peso entre ellos.

**Crafteo de mejora:** algunos trinkets básicos se pueden combinar con una **Estrella del Nether** para mejorarlos directamente a su versión avanzada (por ejemplo, Vendaje Adhesivo + Estrella del Nether → Transfusión), sin depender de la suerte del loot.

Revisa la seccion de trinkets mas abajo para ver todos los disponibles con sus estadisticas.

---

## ⚙️ Mecanica general

- Al subir de nivel en cualquier skill, **Power** recibe **120 de EXP** automáticamente.
- Empiezas con **10 puntos de habilidad** y, al subir **Power**, obtienes **1 punto por nivel**, más puntos extra en los hitos de Power (niveles 10, 20, 30, 40, 50, 60, 70 y 80). Con Power al máximo (256) suman **282 puntos** en total.
- Los puntos se gastan en los árboles de perks individuales de cada skill. Comprar **todas** las ventajas de todas las skills costaría unos 138 puntos, así que hay que elegir (algunas ventajas son excluyentes entre sí).
- Puedes **olvidar** una ventaja y se te devuelven los puntos (no se devuelven ítems, dinero ni EXP).
- Los perks son permanentes — ni la muerte ni el reinicio los elimina.
- **XP de combate por zona:** si ganas XP de combate muchas veces en el mismo chunk (más de 15 eventos), la XP baja al **5 %**; afecta a Armas ligeras, Armas pesadas, Arquería y Artes Marciales. Los mobs de spawner y el PvP dan solo el 10 %. Farmear en un solo punto rinde muy poco.
- Las ventajas que piden nivel en **Herrería o Encantamiento** no se pueden conseguir hoy, porque esas skills están desactivadas.
- Usa `/val skilltree [skill]` para abrir el árbol visual en el juego.
- **Tope de XP por día (desde el 12 nov):** progresivo. Por skill y día, hasta **100.000** de XP bruta recibes el 100 %, los siguientes 100.000 el **50 %** y después el **25 %** (nunca 0; en pesca 80.000 + 80.000). Poder, Encantamiento y Herrería no tienen tope. Mira tu avance con `/limite`. Se reinicia todos los días a las **7:30 AM** (hora de Chile). Además la XP por acción de Minería, Excavación, Tala, Agricultura, Pesca, Alquimia y Comercio bajó un 25 %.

---

## 🔋 Power (max nivel 256)

**Como subir XP:** No se sube directo: recibe **120 de EXP** cada vez que cualquier otra skill sube de nivel. Nivel máximo 256.

**Bonos al empezar:** puntos de habilidad +10, daño crítico +0.5, daño de sangrado +2, duración del sangrado (ticks) +80, resistencia radiante +2, protección anti-oneshot +10%, recarga de la protección anti-oneshot (ticks) +6000.

**Bono por cada nivel:** puntos de habilidad +1.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 20: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 30: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 40: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 50: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 60: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 70: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1
- Nivel 80: resistencia PvP +7.5%, puntos de habilidad +2, vida máxima +2, armadura +1

**Árbol de perks:** 21 ventajas; comprarlas todas costaría 21 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Vitalidad I | 0 | 1 | — | Salud Máxima 1 |
| Piel de Hierro I | 0 | 1 | — | Armadura Natural +1 |
| Bendición Divina I | 0 | 1 | — | Suerte +0.075 |
| Restauración I | 0 | 1 | — | Regeneración de Salud 7.5% |
| Físico I | 0 | 1 | — | Daño Infligido 1.875% |
| Saqueador I | 0 | 1 | — | Botín de Mob 7.5% |
| Ambición I | 0 | 1 | — | Red. de Recarga de Habilidad 3.75% |
| Vitalidad II | 30 | 1 | Requiere Vitalidad I | Salud Máxima 1.125 |
| Piel de Hierro II | 30 | 1 | Requiere Piel de Hierro I | Armadura Natural +1.125 |
| Bendición Divina II | 30 | 1 | Requiere Bendición Divina I | Suerte +0.1125 |
| Restauración II | 30 | 1 | Requiere Restauración I | Regeneración de Salud 11.25% |
| Físico II | 30 | 1 | Requiere Físico I | Daño Infligido 2.812% |
| Saqueador II | 30 | 1 | Requiere Saqueador I | Botín de Mob 11.25% |
| Ambición II | 30 | 1 | Requiere Ambición I | Red. de Recarga de Habilidad 5.625% |
| Vitalidad III | 60 | 1 | Requiere Vitalidad II | Salud Máxima 1.875 |
| Piel de Hierro III | 60 | 1 | Requiere Piel de Hierro II | Armadura Natural +1.875 |
| Bendición Divina III | 60 | 1 | Requiere Bendición Divina II | Suerte +0.1875 |
| Restauración III | 60 | 1 | Requiere Restauración II | Regeneración de Salud 18.75% |
| Físico III | 60 | 1 | Requiere Físico II | Daño Infligido 4.688% |
| Saqueador III | 60 | 1 | Requiere Saqueador II | Botín de Mob 18.75% |
| Ambición III | 60 | 1 | Requiere Ambición II | Red. de Recarga de Habilidad 9.375% |

---

## ⛏️ Mining (max nivel 100)

**Como subir XP:** Minar bloques. XP real por bloque (la tabla base × 0.75, explosiones × 0.5625): Escombros ancestrales 840, Placas de netherita 420, Mineral de diamante abismal 315, Mineral de esmeralda abismal 315, Mineral de diamante 210, Mineral de esmeralda 210, Mineral de lapislázuli 168, Mineral de oro abismal 126, Mineral de lapislázuli abismal 126, Diamante 105.

**Bonos al empezar:** botín de minería -30%.

**Bono por cada nivel:** botín de minería +1%, botín de explosiones +1%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: botín de minería +1.125%, botín de explosiones +1.125%
- Nivel 25: botín de minería +1.875%, botín de explosiones +1.875%
- Nivel 50: botín de minería +3%, botín de explosiones +3%
- Nivel 75: botín de minería +4.5%, botín de explosiones +4.5%
- Nivel 100: botín de minería +6.75%, botín de explosiones +6.75%

**Árbol de perks:** 15 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Roca Frágil | 0 | 1 | — | Acelera tu minería en 3.75% y ganas algunos orbes de experiencia por bloque |
| Explosivos Encantados: Toque de Seda | 0 | gratis | Requiere Explosivos Encantados | Tu TNT rompe bloques como si fuera con un pico de Toque de Seda |
| Explosivos Encantados: Fortuna | 0 | gratis | Requiere Explosivos Encantados | Tu TNT rompe bloques como si fuera con un pico de Fortuna II |
| Espeleo | 20 | 1 | Requiere Roca Frágil | Aumenta el botín de minería en 3.75% y la suerte en 0.375. Aumenta la vel. de cocción en 9.375% |
| Demolista | 40 | 1 | Requiere Espeleo | Aumenta el radio de explosión del TNT y la resist. al daño en 18.75%, y el botín de explosiones en 7.5% |
| Aptitud Enana | 40 | 1 | Requiere Espeleo | Acelera tu minería en 7.5%, aumenta los orbes por bloque y desbloquea la habilidad Perforación |
| Terremoto | 60 | 1 | Requiere Demolista | Duplica los efectos de Demolista, y consigues el triple de TNT al fabricarlo |
| Extracción de Vetas | 60 | 1 | Requiere Aptitud Enana | Aumenta el botín de minería en 7.5% y la suerte en 1.125. Desbloquea Minería de Vetas y aumenta la vel. de cocción en 9.375% |
| Explosivos Encantados | 70 | 1 | Requiere Terremoto; También pide Enchanting Nivel 70 ❌ *(skill desactivada: hoy no se puede conseguir)* | Permite elegir entre Toque de Seda y Fortuna II como encantamientos para aplicar en todo tu TNT |
| Partidor de Tierra | 80 | 1 | Requiere una de: Terremoto, Extracción de Vetas | Aumenta la vel. de perforación en 1.125 y reduce a la mitad su recarga. Obtienes el doble de orbes de experiencia por bloque |
| Aspecto de Kali | 100 | 1 | Requiere una de: Partidor de Tierra | Tu Minería de Vetas puede ahora minar bloques como Andesita, Granito, Diorita y otros bloques comunes. El botín se transfiere directamente a tu inventario |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Minería a 0 y reduce la EXP ganada en -25%. A cambio, ganas 12.5% permanente de botín de minería y explosiones y 7.5% de vel. de minería |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Minería a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 12.5% permanente de botín de minería y explosiones y 7.5% de vel. de minería |
| Nueva Partida III | 100 | gratis | Requiere Nueva Partida II | Reinicia tu nivel de Minería a 0 y reduce la EXP ganada en -3%. A cambio, ganas de nuevo 6% permanente de botín de minería y explosiones y 4% de vel. de minería |
| Nueva Partida IV | 100 | gratis | Requiere Nueva Partida III | Reinicia tu nivel de Minería a 0 y reduce la EXP ganada en -1%. A cambio, ganas de nuevo 3% permanente de botín de minería y explosiones y 2% de vel. de minería |

---

## 🪵 Woodcutting (max nivel 100)

**Como subir XP:** Talar madera y descortezar troncos. Los valores más altos: Hifas distorsionadas (talar) 42, Hifas carmesí (talar) 42, Tallo distorsionado (talar) 31.5, Tallo carmesí (talar) 31.5, Madera de roble (talar) 31.5, Madera de abeto (talar) 31.5, Madera de abedul (talar) 31.5, Madera de jungla (talar) 31.5.

**Bono por cada nivel:** velocidad de tala +0.5%, botín de tala +1%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: velocidad de tala +0.562%, botín de tala +1.125%
- Nivel 25: velocidad de tala +0.938%, botín de tala +1.875%
- Nivel 50: velocidad de tala +1.5%, botín de tala +3%
- Nivel 75: velocidad de tala +2.25%, botín de tala +4.5%
- Nivel 100: velocidad de tala +3.375%, botín de tala +6.75%

**Árbol de perks:** 13 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Talador Novato | 0 | 1 | — | Acelera tu tala un 10% y ganas algunos orbes de experiencia por bloque |
| Hojas Doradas | 20 | 1 | Requiere Talador Novato | Las hojas a veces sueltan Manzanas Doradas y ganas más orbes de experiencia por bloque |
| Deforestación I | 40 | 1 | Requiere Hojas Doradas | Desbloquea el Tala-Árboles para árboles pequeños |
| Estilo de Vida Activo | 50 | 1 | Requiere Hojas Doradas; También pide Digging Nivel 50 | Aumenta el valor nutricional de muchos alimentos, reduce el consumo de hambre y aumenta la regeneración de salud |
| Carpintería | 60 | 1 | Requiere Deforestación I | Aumenta el rendimiento de la mayoría de recetas relacionadas con madera |
| Deforestación II | 60 | 1 | Requiere Deforestación I | Potencia el Tala-Árboles hasta 32 bloques y reduce su recarga a 7 segundos |
| Arboricultor | 80 | 1 | Requiere Deforestación I | Acelera tu tala un 20%, ganas muchos más orbes por bloque y los retoños crecen el doble de rápido |
| Deforestación III | 80 | 1 | Requiere Deforestación II | Potencia el Tala-Árboles hasta 128 bloques y reduce su recarga a 3 segundos |
| Hojas de Cristal | 100 | 1 | Requiere Arboricultor | Las hojas a veces sueltan Manzanas Joyadas y las Manzanas Doradas caen más frecuentemente |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Tala a 0 y reduce la EXP ganada en -25%. A cambio, ganas 15% permanente de botín, 12.5% de vel. y las manzanas Doradas/Cristalinas caen algo más frecuentemente |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Tala a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 15% permanente de botín, 12.5% de vel. y las manzanas Doradas/Cristalinas caen algo más frecuentemente |
| Nueva Partida III | 100 | gratis | Requiere Nueva Partida II | Reinicia tu nivel de Tala a 0 y reduce la EXP ganada en -3%. A cambio, ganas de nuevo 8% permanente de botín, 6% de vel. y las manzanas Doradas/Cristalinas caen algo más frecuentemente |
| Nueva Partida IV | 100 | gratis | Requiere Nueva Partida III | Reinicia tu nivel de Tala a 0 y reduce la EXP ganada en -1%. A cambio, ganas de nuevo 4% permanente de botín, 3% de vel. y las manzanas Doradas/Cristalinas caen algo más frecuentemente |

---

## 🕳️ Digging (max nivel 100)

**Como subir XP:** Cavar tierra, arena, arcilla y arqueología (cepillo). Los valores más altos: Fragmento resonante (cavar) 1050, Libro encantado (cavar) 525, Placas de netherita (cavar) 525, Diamante (cavar) 262.5, Esmeralda (cavar) 262.5, Perla de ender (cavar) 105, Fragmento de amatista (cavar) 105, Diamante (arqueología) 78.75.

**Bono por cada nivel:** botín de excavación +1%, velocidad de excavación +0.5%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: botín de excavación +1.125%, velocidad de excavación +0.562%
- Nivel 25: botín de excavación +1.875%, velocidad de excavación +0.938%
- Nivel 50: botín de excavación +3%, velocidad de excavación +1.5%
- Nivel 75: botín de excavación +4.5%, velocidad de excavación +2.25%
- Nivel 100: botín de excavación +6.75%, velocidad de excavación +3.375%

**Árbol de perks:** 13 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Excavador | 0 | 1 | — | Acelera tu excavación en 11.25% y ganas algunos orbes de experiencia por bloque |
| Filtrador | 20 | 1 | Requiere Excavador | Empiezas a encontrar recursos simples en el suelo, y ganas más orbes de experiencia por bloque |
| Replicación del Suelo | 40 | 1 | Requiere Filtrador | Aprendes la composición de la tierra y puedes reproducirla (desbloquea recetas para varios bloques tipo tierra) |
| Constructor Flexible | 50 | 1 | Requiere una de: Filtrador; También pide Mining Nivel 50 | Desbloquea varias interacciones para detallar tus construcciones (p.ej. añadir musgo a adoquines, agrietar ladrillos) |
| Arqueólogo | 60 | 1 | Requiere Replicación del Suelo | Los bloques sospechosos tienen una probabilidad 7.5% de reaparecer |
| Excavadora | 60 | 1 | Requiere Replicación del Suelo | Acelera tu excavación en 18.75% adicional |
| Historia Antigua | 80 | 1 | Requiere Arqueólogo | Los bloques sospechosos tienen una probabilidad adicional 11.25% de reaparecer, y hay probabilidad de encontrar arena o grava sospechosa al excavar cerca de estructuras |
| Bateo | 80 | 1 | Requiere Excavadora | Empiezas a encontrar recursos valiosos en el suelo |
| Tesoro Oculto | 100 | 1 | Requiere una de: Historia Antigua, Bateo | Empezarás a encontrar tesoros ocasionalmente al excavar |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Excavación a 0 y reduce la EXP ganada en -25%. A cambio, ganas 15% permanente de botín, 1.5 de suerte y 12.5% de vel. de excavación |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Excavación a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 15% permanente de botín, 1.5 de suerte y 12.5% de vel. de excavación |
| Nueva Partida III | 100 | gratis | Requiere Nueva Partida II | Reinicia tu nivel de Excavación a 0 y reduce la EXP ganada en -3%. A cambio, ganas de nuevo 8% permanente de botín, 0.75 de suerte y 6% de vel. de excavación |
| Nueva Partida IV | 100 | gratis | Requiere Nueva Partida III | Reinicia tu nivel de Excavación a 0 y reduce la EXP ganada en -1%. A cambio, ganas de nuevo 4% permanente de botín, 0.4 de suerte y 3% de vel. de excavación |

---

## 🌾 Farming (max nivel 100)

**Como subir XP:** Cosechar cultivos, criar y esquilar animales, y usar colmenas. Los valores más altos: Mushroom cow (esquilar) 525, Apiario (interactuar) 210, Colmena (interactuar) 210, Botella con miel (interactuar) 210, Hoglin (criar) 105, Oveja (esquilar) 105, Ocelote (criar) 94.5, Tortuga (criar) 94.5, Rana (criar) 84, Gato (criar) 84.

**Bono por cada nivel:** botín de agricultura +1%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: botín de agricultura +1.125%
- Nivel 25: botín de agricultura +1.875%
- Nivel 50: botín de agricultura +3%
- Nivel 75: botín de agricultura +4.5%
- Nivel 100: botín de agricultura +6.75%

**Árbol de perks:** 12 ventajas; comprarlas todas costaría 10 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Toque Suave | 0 | 1 | — | Desbloquea la capacidad de hacer clic derecho en cultivos para cosecharlos y replantar |
| Tierra Mágica | 20 | 1 | Requiere Toque Suave | Los cultivos crecen más rápido y generan algo de experiencia al cosecharlos |
| Dieta Basura | 30 | 1 | Requiere Toque Suave; ⚠️ Excluyente: bloquea Dieta Equilibrada | Te vuelves inmune a la comida en mal estado y te alimenta tres veces más, pero todos los demás alimentos pierden -25% de nutrición. Bloquea Dieta Equilibrada |
| Cosecha Bendita | 40 | 1 | Requiere Tierra Mágica | El botín de cosecha aumenta en 7.5% y generan aún más experiencia |
| Ganadería | 40 | 1 | Requiere Toque Suave | Los animales crecen 15% más rápido y sueltan 7.5% más objetos. Los animales criados otorgan 18.75% más orbes de experiencia |
| Apicultor | 50 | 1 | Requiere Toque Suave | Las abejas ya no te atacan. Las colmenas tienen 18.75% de prob. de rellenarse tras cosechar |
| Dieta Equilibrada | 50 | 1 | Requiere Toque Suave; ⚠️ Excluyente: bloquea Dieta Basura | Todos los alimentos, excepto los en mal estado, te alimentan 7.5% más. Bloquea Dieta Basura |
| Carnicería | 60 | 1 | Requiere Ganadería | Los animales crecen 22.5% más rápido y sueltan 11.25% más objetos. Los animales criados otorgan 18.75% más orbes y haces cuádruple daño a animales |
| Cosecha Divina | 80 | 1 | Requiere Cosecha Bendita | El botín de cosecha aumenta en 11.25% y generan mucha experiencia |
| Agricultura Automágica | 100 | 1 | Requiere Cosecha Divina | Desbloquea Cosecha de Campo, una habilidad que permite cosechar una gran área de cultivos casi instantáneamente |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Agricultura a 0 y reduce la EXP ganada en -25%. A cambio, ganas 15% permanente de botín de agricultura y carnicería |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Agricultura a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 15% permanente de botín de agricultura y carnicería |

---

## 🎣 Fishing (max nivel 100)

**Como subir XP:** Pescar. XP por pieza: Libro encantado 615, Pez tropical 495, Caparazón de nautilo 412.5, Montura 412.5, Caña de pescar 390, Pez globo 337.5, Etiqueta 337.5, Arco 315, Salmón crudo 206.25, Bacalao crudo 180. La XP de pesca también baja si farmeas siempre en el mismo chunk.

**Bono por cada nivel:** velocidad de pesca +2%, botín de pesca +2%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: velocidad de pesca +2.25%, botín de pesca +2.25%
- Nivel 25: velocidad de pesca +3.75%, botín de pesca +3.75%
- Nivel 50: velocidad de pesca +6%, botín de pesca +6%
- Nivel 75: velocidad de pesca +9%, botín de pesca +9%
- Nivel 100: velocidad de pesca +13.5%, botín de pesca +13.5%

**Árbol de perks:** 9 ventajas; comprarlas todas costaría 7 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Pescador Afortunado | 0 | 1 | — | Aumenta la suerte de pesca en 0.5625 |
| Pasión por los Mares | 20 | 1 | Requiere Pescador Afortunado | Aumenta los orbes de experiencia obtenidos pescando en 18.75% |
| Sentidos Profundos | 40 | 1 | Requiere Pasión por los Mares | Atrae peces 15% más rápido, aumenta la suerte de pesca en 1 |
| Scavenge de Mar Profundo | 50 | 1 | Requiere Pescador Afortunado; También pide Smithing Nivel 70 ❌ *(skill desactivada: hoy no se puede conseguir)* | Desbloquea la capacidad de desguazar herramientas y equipo en sus partes base |
| Amos Dobles | 60 | 1 | Requiere Sentidos Profundos | Gana una probabilidad 9.375% de doble captura |
| Cebo Dorado | 80 | 1 | Requiere Amos Dobles | Atrae peces 22.5% más rápido, aumenta la suerte de pesca en 0.9375 |
| Cebo Místico | 100 | 1 | Requiere Cebo Dorado | Gana una probabilidad 9.375% de doble captura, así como 37.5% más orbes de experiencia al pescar |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Pesca a 0 y reduce la EXP ganada en -25%. A cambio, ganas 25% permanente de botín de pesca, 1.25 de suerte y 12.5% de vel. de pesca |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Pesca a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 25% permanente de botín de pesca, 1.25 de suerte y 12.5% de vel. de pesca |

---

## 🧪 Alchemy (max nivel 100)

**Como subir XP:** Elaborando pociones en calderos y soportes de pociones. La XP depende de la **calidad** de la poción (calidad × 0.0018): elaborar a mano multiplica por **1.05** y automatizado (hoppers y droppers) solo por **0.075**.

**Bono por cada nivel:** habilidad de elaboración +0.75.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: habilidad de elaboración +1.125
- Nivel 25: habilidad de elaboración +1.688
- Nivel 50: habilidad de elaboración +2.813
- Nivel 75: habilidad de elaboración +3.938
- Nivel 100: habilidad de elaboración +5.625

**Calidad de las pociones:** cada poción tiene una puntuación de calidad que le da una etiqueta cosmética: Rancid (0), Tainted (30), Dirty (60), Cloudy (90), Clear (120), Refined (150), Pure (200), Shimmering (300+).

**Árbol de perks:** 11 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Combustión Estable | 0 | 1 | — | Acelera tu elaboración de pociones en 18.75% y aumenta su calidad ligeramente |
| Ingredientes Potentes | 20 | 1 | Requiere Combustión Estable | Otorga una probabilidad 7.5% de no gastar ingredientes al elaborar, y aumenta aún más la calidad de las pociones |
| Venenos Volátiles | 40 | 1 | Requiere Ingredientes Potentes | Mejora la calidad de tus venenos. Tus impactos indirectos con pociones arrojadizas son más fuertes |
| Catalizadores Efectivos | 40 | 1 | Requiere Ingredientes Potentes | Mejora la calidad de tus pociones beneficiosas. Acelera la elaboración en 28.13% |
| Veneno Corrosivo | 50 | 1 | Requiere Ingredientes Potentes; Requiere una de: Caballero, Bárbaro | Añade 4 cargas a tu habilidad de Recubrimiento de Arma. Desbloqueas recetas de venenos simples sin soporte de elaboración |
| Artillería Química | 60 | 1 | Requiere Venenos Volátiles | Mejora aún más la calidad de tus venenos. Mejora la intensidad de pociones arrojadizas, la duración y radio de pociones persistentes, y la fuerza de lanzamiento |
| Ingredientes Exóticos | 60 | 1 | Requiere Catalizadores Efectivos | Aumenta la calidad de pociones beneficiosas y la probabilidad de no gastar ingredientes en 11.25% y desbloquea recetas de Prisa y Aumento de Salud |
| Mezclas Poderosas | 80 | 1 | Requiere una de: Artillería Química, Ingredientes Exóticos | Permite fusionar los efectos de varias pociones en una, hasta 1.125 veces, con algo de pérdida de duración |
| Prima Materia | 100 | 1 | Requiere una de: Mezclas Poderosas | Mejora enormemente la calidad de todas tus pociones. Desbloquea Transmutación |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Alquimia a 0 y reduce la EXP ganada en -25%. A cambio, ganas 25 permanente de habilidad de elaboración y 37.5% de vel. de elaboración |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Alquimia a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 25 permanente de habilidad de elaboración y 50% de vel. de elaboración |

**Sistema de Transmutación:** con la Poción de Transmutación (desbloqueada en el perk final) puedes convertir ciertos bloques en otros usando un caldero — por ejemplo, troncos de un tipo de madera a otro, o minerales/bloques de valor (Hierro→Oro, Cobre→Hierro, Esmeralda↔Diamante) en lo que el plugin llama transmutación "Midas".

---

## 🔨 Smithing (max nivel 100)

{% hint style="danger" %}
❌ **Smithing está desactivado actualmente en el servidor.** La mesa de herrería y el crafteo de herramientas y armaduras funcionan en **modo vanilla estándar**: no se gana XP de Smithing, no hay calidad de equipo ni acceso a su árbol de perks. La información de abajo se conserva **solo como referencia** por si se reactiva en el futuro.
{% endhint %}

**Como subir XP:** A diferencia de los demás skills, Smithing **no da XP por craftear** directamente — la XP se gana **gastando la durabilidad** de las herramientas y armaduras que hayas forjado con el plugin. Cada punto de durabilidad gastado en una herramienta da **0.01 XP** (máximo 1000 XP por ítem), y cada punto gastado en una pieza de armadura da **0.005 XP** (máximo 200 XP por pieza).

**Penalización inicial por material:** cada material tiene su propio multiplicador de XP, que empieza en negativo para los metales y se va corrigiendo a medida que subes de nivel y desbloqueas perks:

| Material | Penalización inicial |
|---|---|
| Piedra / Cadena / Cobre | -50% XP |
| Oro / Hierro | -75% XP |
| Diamante | -90% XP |
| Netherite | -100% XP (sin XP hasta avanzar) |

Madera y cuero no tienen penalización inicial, pero **reciben una propia de -75% a partir del nivel 20** — el sistema está diseñado para empujarte a progresar de materiales básicos a avanzados en vez de quedarte minando XP fácil indefinidamente.

**Bono pasivo por nivel:** +0.75 a la habilidad general de crafteo (`genericcraftingskill`).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +19 habilidad de crafteo en madera y cuero |
| Perk 2 | 20 | +19 habilidad en piedra, cadena y cobre |
| Perk 3 | 40 | +19 habilidad en hierro y oro. Desbloquea las 16 recetas de equipo de Diamante (armadura completa, espada, hacha, pico, pala, azada, martillo de guerra, mandoble, lanza, daga, estoque, maza, lanza real) |
| Perk Arcos (Archery 50) | 50 | Requiere Archery 50. +19 habilidad de arcos y ballestas |
| Perk Prismarino | 70 | Requiere Perk 3. +19 habilidad con prismarina. Desbloquea receta del Tridente |
| Perk 4 | 60 | +19 habilidad en diamante. Permite reparar conservando encantamientos al usar el inventario |
| Perk Enderico | 90 | Requiere Perk 4. +19 habilidad enderica. Desbloquea recetas de Élitros y Cuero Coral |
| Perk 5 | 80 | +19 habilidad en netherite |
| Perk 6 — Maestria | 100 | +19 habilidad de crafteo general |

**Calidad del equipo:** cada pieza que crafteas tiene una puntuación de calidad que determina su etiqueta: Terrible (-500 a -60), Shoddy (-60 a -30), Decent (-30 a 0), Good (0 a 30), Great (30 a 60), Flawless (60 a 90), Masterful (90 a 120), Fabled (120 a 150), Peerless (150+).

---

## ❌ Enchanting — no disponible

El skill de Enchanting no esta activo actualmente en el servidor. La mesa de encantamiento y el yunque funcionan en modo vanilla estandar. No se gana XP de Enchanting ni se puede acceder a su arbol de perks.

---

## 🗡️ Light Weapons (max nivel 100)

**Como subir XP:** Golpeando con espadas, dagas, estoques y lanzas: **4.9 XP por punto de daño**. Los mobs de spawner dan solo el 10%, el PvP el 10% y la maza de vanilla el 10%. Si farmeas muchos golpes en el mismo chunk la XP baja al 5 %.

**Bonos al empezar:** daño +0%, retroceso +0%, reducción de inmunidad +0%.

**Bono por cada nivel:** velocidad de ataque +0.375%, daño +0.375%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: velocidad de ataque +0.422%, daño +0.422%
- Nivel 25: velocidad de ataque +0.703%, daño +0.703%
- Nivel 50: velocidad de ataque +1.12%, daño +1.12%
- Nivel 75: velocidad de ataque +1.69%, daño +1.69%
- Nivel 100: velocidad de ataque +2.53%, daño +2.53%

**Árbol de perks:** 11 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Paje | 0 | 1 | — | Aumenta el daño en 2.81% y añade una probabilidad 2.81% de infligir sangrado |
| Escudero | 20 | 1 | Requiere Paje | Aumenta la vel. de ataque en 2.81% y otorga 2.81% de prob. de golpe crítico |
| Caballero | 40 | 1 | Requiere Escudero | Desbloquea Parada. Aumenta el daño en 2.81% |
| Recubrimiento de Arma | 50 | 1 | Requiere Caballero | Desbloquea Recubrimiento de Arma, que permite aplicar efectos de poción en tus armas durante 2 golpes |
| Paladín | 60 | 1 | Requiere Caballero | Aumenta la vel. de ataque en 5.62%, los enemigos tienen 2.81% menos de inmunidad, y añade 2.81% de prob. de sangrado |
| Bioarma | 70 | 1 | Requiere Recubrimiento de Arma | El Recubrimiento de Arma se vuelve más fuerte, dura más, aplica mayor efecto y aguanta 2 golpes más |
| Titán | 70 | 1 | También pide Heavy_Armor Nivel 70 | Gana 3 de penetración de armadura, 8.44% más de retroceso y 0.281 mayor alcance de ataque |
| Templario | 80 | 1 | Requiere Paladín | Aumenta el daño en 2.81%, la Parada es mucho más fácil y fuerte, los enemigos tienen 5.62% menos de inmunidad, y añade 2.81% de sangrado |
| Señor de la Guerra | 100 | 1 | Requiere Templario | Aumenta la prob. de crítico en 2.81% y el daño crítico en 8.44%. Los críticos infligen Sangrado y el sangrado hace 0.75 más daño |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Armas Ligeras a 0 y reduce la EXP ganada en -25%. A cambio, ganas 7.5% permanente de daño de ataque, 10% de vel. de ataque y 5% de prob. de crítico |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Armas Ligeras a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 7.5% permanente de daño de ataque, 10% de vel. de ataque y 5% de prob. de crítico |

---

## 🪓 Heavy Weapons (max nivel 100)

**Como subir XP:** Golpeando con hachas, martillos de guerra, mazas y mandobles: **7 XP por punto de daño**. Los mobs de spawner dan solo el 10%, el PvP el 10% y la maza de vanilla el 10%. Si farmeas muchos golpes en el mismo chunk la XP baja al 5 %.

**Bonos al empezar:** velocidad de ataque +0%, daño +0%.

**Bono por cada nivel:** velocidad de ataque +0.375%, daño +0.375%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: velocidad de ataque +0.422%, daño +0.422%
- Nivel 25: velocidad de ataque +0.703%, daño +0.703%
- Nivel 50: velocidad de ataque +1.12%, daño +1.12%
- Nivel 75: velocidad de ataque +1.69%, daño +1.69%
- Nivel 100: velocidad de ataque +2.53%, daño +2.53%

**Árbol de perks:** 11 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Salvaje | 0 | 1 | — | Aumenta el daño en 2.81% |
| Bruto | 20 | 1 | Requiere Salvaje | Aumenta el daño de ataque de poder en 2.81% y otorga 2.81% de prob. de golpe crítico |
| Bárbaro | 40 | 1 | Requiere Bruto | Los ataques de poder infligen 14.1% de daño en área en un radio de 42.2% bloques. Aumenta el daño en 2.81% |
| Recubrimiento de Arma | 50 | 1 | Requiere Bárbaro | Desbloquea Recubrimiento de Arma, que permite aplicar efectos de poción en tus armas durante 1 golpes |
| Vikingo | 60 | 1 | Requiere Bárbaro | Aumenta el daño de ataque de poder en 4.22% y ganas 1.41 de penetración de armadura |
| Acero Tóxico | 70 | 1 | Requiere Recubrimiento de Arma | El Recubrimiento de Arma se vuelve más fuerte, dura más y aguanta 1 golpes más |
| Golpes Fragmentadores | 70 | 1 | También pide Woodcutting Nivel 70 | Gana 5.62% de penetración de armadura, 5.62% de prob. de aturdimiento, y haces 1.41% más daño por pieza de armadura ligera del enemigo |
| Berserker | 80 | 1 | Requiere Vikingo | Aumenta el daño en 2.81%, los ataques de poder hacen mucho más daño en área, y ganas 3 de penetración de armadura adicional |
| PortaMuerte | 100 | 1 | Requiere Berserker | Aumenta la prob. de crítico en 2.81% y el daño crítico en 8.44%. Los críticos infligen Sangrado y el sangrado hace 0.281 más daño |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Armas Pesadas a 0 y reduce la EXP ganada en -25%. A cambio, ganas 7.5% permanente de daño de ataque, 10% de daño de ataque de poder y 5% de prob. de crítico |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Armas Pesadas a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 7.5% permanente de daño de ataque, 10% de daño de ataque de poder y 5% de prob. de crítico |

---

## 🧥 Light Armor (max nivel 100)

**Como subir XP:** Recibiendo daño con armadura ligera (cuero, cota de malla): **7 XP** por la primera pieza equipada y **3.5** por cada pieza adicional. El daño de otros jugadores da el 10%. Si te farmean en el mismo chunk la XP baja al 5 %.

**Bonos al empezar:** efectividad de la armadura +0%, velocidad por pieza +0%, ahorro de hambre por pieza +0%, curación por pieza +0%, esquiva por pieza +1.88%.

**Bono por cada nivel:** efectividad de la armadura +0.375%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: efectividad de la armadura +0.422%
- Nivel 25: efectividad de la armadura +0.703%
- Nivel 50: efectividad de la armadura +1.12%
- Nivel 75: efectividad de la armadura +1.69%
- Nivel 100: efectividad de la armadura +2.53%

**Árbol de perks:** 11 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Tachones de Hierro | 0 | 1 | — | La armadura ligera se vuelve 2.81% más protectora |
| Desenvuelta | 20 | 1 | Requiere Tachones de Hierro | La armadura ligera te carga la mitad, mejorando la curación y el hambre |
| Metabolismo Controlado | 40 | 1 | Requiere Tachones de Hierro | Llevar un conjunto completo de armadura ligera te otorga 8.44% de reducción de consumo de hambre. La armadura ligera es 2.81% más protectora |
| Adrenalina | 50 | 1 | Requiere Tachones de Hierro | Desbloquea Adrenalina. Al llegar a poca vida, ganas brevemente potentes buffs para escapar del peligro |
| Compostura Perfecta | 50 | 1 | Requiere Tachones de Hierro; También pide Heavy_Weapons Nivel 50 | Llevar un conjunto completo de armadura ligera te otorga 14.1% de resist. a críticos e inmunidad a aturdimiento |
| Explorador Eficiente | 60 | 1 | Requiere Desenvuelta | Solo necesitas 3 piezas de armadura ligera para el bonus de conjunto. La armadura ligera no te carga nada |
| Reflejos Veloces | 60 | 1 | Requiere Metabolismo Controlado | Llevar un conjunto completo de armadura ligera te otorga 5.62% de prob. de esquivar un ataque. La armadura ligera es 2.81% más protectora |
| Rayo | 90 | 1 | Requiere Adrenalina | Mejora Adrenalina, aumentando la fuerza y duración de sus buffs y reduciendo su recarga a la mitad |
| Escamas de Dragón | 100 | 1 | Requiere Explorador Eficiente y Reflejos Veloces | Llevar un conjunto completo de armadura ligera te otorga 11.2% de resist. al daño mágico e inmunidad a Veneno, Ceguera y Hambre |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Armadura Ligera a 0 y reduce la EXP ganada en -25%. A cambio, ganas 0.625% permanente de resist. al daño y 1% de vel. de movimiento por pieza |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Armadura Ligera a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 0.625% permanente de resist. al daño y 1% de vel. de movimiento por pieza |

---

## 🛡️ Heavy Armor (max nivel 100)

**Como subir XP:** Recibiendo daño con armadura pesada (hierro, diamante, netherite, oro): **7 XP** por la primera pieza equipada y **3.5** por cada pieza adicional. El daño de otros jugadores da el 10%. Si te farmean en el mismo chunk la XP baja al 5 %.

**Bonos al empezar:** efectividad de la armadura +0%, velocidad por pieza +0%, ahorro de hambre por pieza +0%, curación por pieza +0%, imprecisión +0.

**Bono por cada nivel:** efectividad de la armadura +0.375%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: efectividad de la armadura +0.422%
- Nivel 25: efectividad de la armadura +0.703%
- Nivel 50: efectividad de la armadura +1.12%
- Nivel 75: efectividad de la armadura +1.69%
- Nivel 100: efectividad de la armadura +2.53%

**Árbol de perks:** 11 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Ajuste Reforzado | 0 | 1 | — | La armadura pesada se vuelve 2.81% más protectora |
| No Saltarte el Día de Piernas | 20 | 1 | Requiere Ajuste Reforzado | La armadura pesada te carga menos, mejorando la curación, el hambre y la precisión a distancia |
| Acero Vital | 40 | 1 | Requiere Ajuste Reforzado | Llevar un conjunto completo de armadura pesada te otorga 11.2% de curación adicional. La armadura pesada es 2.81% más protectora |
| Furia | 50 | 1 | Requiere Ajuste Reforzado | Desbloquea Furia. Al llegar a poca vida, ganas brevemente potentes buffs para mantenerte en combate más tiempo |
| Conoce tus Debilidades | 50 | 1 | Requiere Ajuste Reforzado; También pide Light_Weapons Nivel 50 | Llevar un conjunto completo de armadura pesada te otorga 14.1% de resist. a críticos e 7.03% de inmunidad |
| Infantería Innovadora | 60 | 1 | Requiere No Saltarte el Día de Piernas | Solo necesitas 3 piezas de armadura pesada para el bonus de conjunto. La armadura pesada te carga muy poco ahora |
| Traje con Pinchos | 80 | 1 | Requiere Acero Vital | Llevar un conjunto completo de armadura pesada te otorga 2.81% de prob. de reflejar 5.62% de daño al atacante. La armadura pesada es 2.81% más protectora |
| Rabia | 90 | 1 | Requiere Furia | Mejora Furia, aumentando la fuerza y duración de sus buffs y reduciendo su recarga a la mitad |
| Juggernaut | 100 | 1 | Requiere Infantería Innovadora y Traje con Pinchos | Llevar un conjunto completo de armadura pesada te otorga 11.2% de resist. al retroceso e inmunidad a Debilidad, Lentitud y Levitación |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Armadura Pesada a 0 y reduce la EXP ganada en -25%. A cambio, ganas 0.938% permanente de resist. al daño y 5% de resist. a críticos por pieza |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Armadura Pesada a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 0.938% permanente de resist. al daño y 5% de resist. a críticos por pieza |

---

## 🏹 Archery (max nivel 100)

**Como subir XP:** Disparando con arco (**21 XP** base) o ballesta (**28**). Sube con la distancia del disparo (hasta 100 bloques) y con el daño; con Infinity ×0.7. Spawners 10% y PvP 10%.

**Bonos al empezar:** imprecisión +2.5, daño de arco -10%, daño base por distancia -10%, bono de daño por distancia +10%, daño con Infinity -15%.

**Bono por cada nivel:** daño de arco +0.4%.

**Hitos de nivel** (se suman al llegar a ese nivel):
- Nivel 10: daño de arco +0.45%
- Nivel 25: daño de arco +0.75%
- Nivel 50: daño de arco +1.2%
- Nivel 75: daño de arco +1.8%
- Nivel 100: daño de arco +2.7%

**Árbol de perks:** 11 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Ranger | 0 | 1 | — | Mejora ligeramente la precisión, aumenta el daño en 3.75% |
| Cazador Eficiente | 20 | 1 | Requiere Ranger | Desbloquea Flechas de Piedra, reduce el consumo de munición en 3.75% |
| Arquero | 40 | 1 | Requiere Cazador Eficiente | Desbloquea Flechas de Cobre y Oro, mejora la precisión y otorga 3.75% de prob. de golpe crítico |
| Disparo Cargado I | 40 | 1 | Requiere Cazador Eficiente | Desbloquea Disparo Cargado. Los disparos cargados tienen más perforación, retroceso, velocidad, precisión y daño |
| Asesino | 50 | 1 | Requiere una de: Arquero; También pide Light_Armor Nivel 50 | Los impactos con el enemigo de espaldas y fuera de combate serán siempre críticos. Los críticos causan 18.75% más daño y sangrado |
| Infantería de Largo Alcance | 60 | 1 | Requiere Arquero | Desbloquea Flechas de Hierro y Éndrico, aumenta el daño a distancia en 3.75% y haces más daño cuanto más lejos estés del objetivo |
| FrancoTirador | 80 | 1 | Requiere Infantería de Largo Alcance | Desbloquea Flechas de Diamante, aumenta la prob. de crítico en 7.5% y el daño crítico en 11.25%. Gran mejora de precisión |
| Disparo Cargado II | 80 | 1 | Requiere Disparo Cargado I | Los disparos cargados ganan 1 y reducen su recarga. Más cargas, perforación, retroceso y daño. Los disparos cargados también ignoran la gravedad |
| Disparos Necróticos | 100 | 1 | Requiere FrancoTirador | Desbloquea Flechas de Netherita e Impuras, elimina la penalización de daño de arcos con Infinito, y mejora enormemente el daño a gran distancia |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Arquería a 0 y reduce la EXP ganada en -25%. A cambio, ganas 7.5% permanente de daño a distancia, -1.5 de imprecisión y 5% de prob. de crítico |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Arquería a 0 y reduce la EXP ganada en -8.5%. A cambio, ganas de nuevo 7.5% permanente de daño a distancia, -1.5 de imprecisión y 5% de prob. de crítico |

---

## 🥋 Artes Marciales (max nivel 100) ✨ Premium

**Como subir XP:** Peleando sin arma o con nudilleras: **10 XP por punto de daño**. Spawners 10% y PvP 10%; si farmeas en el mismo chunk la XP baja al 5 %.

**Bonos al empezar:** probabilidad de aturdir +7.5%.

**Bono por cada nivel:** daño sin arma +0.0375, poder de agarre +1.

**Mecanicas propias:**

| Mecanica | Descripcion |
|---|---|
| Aturdir (Stun) | Tus golpes tienen probabilidad de aturdir al enemigo |
| Golpe cargado | Retener el golpe acumula daño extra antes de soltarlo |
| Agarre (Grapple) | Te agarras al enemigo para ralentizarlo y debilitarlo |
| Desarme (Disarm) | Haces que los mobs suelten su arma (a jugadores no, por config del servidor) |
| Uppercut | Lanza al enemigo por los aires; si choca con una pared recibe daño por contusion |
| Meditacion | Una vez al dia (del juego), meditando en la cima de una montaña, eliges un efecto duradero |

**Árbol de perks:** 12 ventajas; comprarlas todas costaría 9 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Manos de Piedra | 0 | 1 | — | Te otorga +75% de daño sin arma extra |
| Disciplina | 20 | 1 | Requiere Manos de Piedra | Tus golpes tienen una probabilidad adicional +5.62% de aturdir. Retener tus golpes aumenta su daño |
| Golpes Despiadados | 20 | 1 | Requiere Manos de Piedra | Aumenta el daño de ataque en 1.5 y la prob. de golpe crítico en 5.62% |
| Suprimir y Controlar | 40 | 1 | Requiere Disciplina | Desbloquea el Agarre, que permite agarrarte a los enemigos para ralentizarlos y debilitarlos. Permite el Desarme |
| Uppercut | 40 | 1 | Requiere Golpes Despiadados | Desbloquea el Uppercut, y aumenta la prob. de golpe crítico en 8.44%. Tus golpes desarman escudos por 30 segundos |
| Vínculo del Alma | 60 | 1 | Requiere Suprimir y Controlar | El Agarre aplica sus efectos el doble de rápido, y mientras lo haces obtienes 30% de prob. de esquivar sus ataques. Desarmar completamente al enemigo te otorga además 50% de Robo de Vida por 8 segundos |
| Defenestración | 70 | 1 | Requiere Uppercut | Golpear a un objetivo en el aire lo lanza a gran velocidad. Si choca con una pared, recibe daño por contusión proporcional a su velocidad |
| Reflejos de Rayo | 80 | 1 | Requiere Vínculo del Alma | Sin atacar, ganas +16.9% de prob. de esquiva. Sin armadura, este efecto se triplicará |
| Om Mani Padmé Hum | 100 | 1 | Requiere Reflejos de Rayo | Desbloquea la Meditación. Una vez al día (del juego), medita en la cima de una montaña y elige entre ? poderosos efectos duraderos |
| Nirvana | 100 | gratis | También pide Smithing Nivel 100, Alchemy Nivel 100, Enchanting Nivel 100, Light_Weapons Nivel 100, Heavy_Weapons Nivel 100, Light_Armor Nivel 100, Heavy_Armor Nivel 100, Archery Nivel 100, Mining Nivel 100, Fishing Nivel 100, Farming Nivel 100, Woodcutting Nivel 100, Digging Nivel 100 ❌ *(skill desactivada: hoy no se puede conseguir)* | Realiza tu máximo potencial |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Artes Marciales a 0 y reduce la EXP ganada en -50%. A cambio, ganas 2 permanente de Daño, 0.5 de Alcance y 20% de Red. de Inmunidad |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Artes Marciales a 0 y reduce la EXP ganada en -25%. A cambio, ganas de nuevo 4 permanente de Daño, 0.5 de Alcance y 20% de Red. de Inmunidad |

**La Meditacion:** al desbloquear el perk final puedes meditar respondiendo en el chat entre **Combate**, **Habilidad** o **Recompensa**, y obtienes un efecto duradero acorde a tu eleccion.

---

## 🤝 Comercio (Trading) (max nivel 100) ✨ Premium

**Como subir XP:** Comerciando con **aldeanos**. Multiplicador por rango del mercader: Novato ×1, Aprendiz ×1.1, Oficial ×1.3, Experto ×1.6, Maestro ×2. Además, si el precio tiene descuento, el descuento se multiplica ×3 y se suma como multiplicador de XP.

**Bonos al empezar:** .

Esta skill va de la mano con todo el sistema de aldeanos. La explicación completa (profesiones, rangos, servicios, felicidad, reputación y precios) está en su propia página:

{% content-ref url="comercio.md" %}
[comercio.md](comercio.md)
{% endcontent-ref %}

**Desde nivel 0** ya puedes comerciar y hacer pedidos (ordering) a casi todas las profesiones. El árbol tiene dos ramas: **A** (mercancía) y **B** (servicios).

**Árbol de perks:** 12 ventajas; comprarlas todas costaría 10 puntos de habilidad.

| Perk | Nivel | Costo | Requisitos | Qué hace |
|---|---|---|---|---|
| Comprador en Masa | 0 | 1 | — | Puedes comprar 15% veces más tratos de un comerciante antes de agotar existencias |
| Carisma Amistoso | 20 | 1 | Requiere Comprador en Masa | Los comerciantes suben de nivel 18.75% más rápido y ofrecen más tratos |
| Aprendizaje | 20 | 1 | Requiere Comprador en Masa | La mayoría de comerciantes pueden entrenarte en su profesión, permitiéndote subir de nivel a un coste (escala con el nivel del comerciante, hasta 75 en nivel Maestro) |
| Entrega Express | 40 | 1 | Requiere Carisma Amistoso | Los pedidos se entregan 37.5% más rápido y puedes pedir 18.75% más |
| Traba jadores de Servicios | 40 | 1 | Requiere Aprendizaje | La mayoría de comerciantes pueden ofrecer servicios de mejora, permitiéndote mejorar o modificar objetos a un coste |
| Mercancía de Calidad | 60 | 1 | Requiere Entrega Express | Los objetos del comerciante tienen 0.15 mayor calidad cuando aplica. También puedes comerciar 22.5% objetos más |
| Descuento VIP | 60 | 1 | Requiere Traba jadores de Servicios | Los servicios son ahora 0.2475 más baratos |
| Gratitud | 80 | 1 | Requiere Mercancía de Calidad | Comerciar con un comerciante otorga la posibilidad de recibir un regalo aleatorio. Esta probabilidad aumenta con reputación y renombre, de 0-10% |
| Artesanos | 80 | 1 | Requiere Descuento VIP | Los objetos del comerciante tienen 0.225 mayor calidad |
| Mercado Negro | 100 | 1 | Requiere Gratitud y Artesanos | La mayoría de comerciantes ofrecen tratos exclusivos y poderosos al rango máximo (maestro) |
| Nueva Partida I | 100 | gratis | — | Reinicia tu nivel de Comercio a 0 y reduce la EXP ganada en -50%. A cambio, ganas 25% permanente de stock de comerciante, 0.25 de calidad de objeto y mayor selección de tratos |
| Nueva Partida II | 100 | gratis | Requiere Nueva Partida I | Reinicia tu nivel de Comercio a 0 y reduce la EXP ganada en -17%. A cambio, ganas de nuevo 25% permanente de stock de comerciante, 0.25 de calidad de objeto y mayor selección de tratos |

---

## ✨ Novedades de contenido Premium

Además de las dos skills nuevas, la versión Premium añade equipo y recetas nuevas. Todo se craftea en las estaciones custom del plugin (usa `/val recipes` para ver el recetario).

### 🥊 Nudilleras (Knuckles)

Arma de cuerpo a cuerpo ligada a **Artes Marciales**. Disponibles en **madera, piedra, hierro, oro y diamante** (más la versión Royal por herrería).

### ⚔️ Armas custom tier Diamante

El set de armas custom del plugin (lanza, gran hacha, maza, martillo de guerra, daga, estoque y lanza real) ahora llega hasta **Diamante**, sumándose a los tiers de madera, piedra, hierro, oro y cobre ya existentes.

### 👑 Tier Royal Diamond

Un nivel de mejora por encima del diamante que se consigue en la **mesa de herrería** (smithing): armadura, armas y herramientas en versión **Royal Diamond**, además de armaduras Royal de netherita.

### 🏹 Flechas custom

Nuevas flechas crafteables con efectos propios:

| Flecha | Efecto |
|---|---|
| Hierro / Cobre / Oro / Diamante / Netherita / Piedra / Pedernal | Flechas de distinto material y daño |
| Flecha de Teletransporte (Ender) | Te teletransporta al punto de impacto |
| Flecha Oscura (Unholy) | Elimina la inmunidad del objetivo |
| Flecha de Carbono | Flecha ligera de alto rendimiento |

### 🧪 Pociones de skill (Alchemy)

Nuevas recetas de elaboración enfocadas en progresión y combate: **más EXP de skill**, **mayor calidad al forjar y encantar**, **armadura**, **inmunidad**, **vulnerabilidad** y **aumento de curación**, en variantes normales, extendidas y potenciadas.

### 🎒 Cinturón de Pociones

Objeto crafteable que te permite llevar pociones a mano y usarlas al instante.

### 🔨 Desguace (Salvage)

En la estación custom puedes **romper equipo** que ya no uses para **recuperar parte de sus materiales**. No afecta al crafteo vanilla: es una opción adicional del plugin.

---

## ⚔️ Sistema de Combate

ValhallaMMO reemplaza el sistema de combate vanilla con mecánicas propias:

| Mecanica | Descripcion |
|---|---|
| Critico | Probabilidad de critico basada en stats. Daño critico calculado separado del vanilla |
| Sangrado | Daño por ticks, hasta 4 stacks. Reducible con resistencia a sangrado |
| Parry | Bloqueo activo con arma ligera. Exito: debuffa al enemigo. Fallo: te vulnera |
| Esquiva (Dodge) | Probabilidad de esquivar por pieza de armadura ligera |
| Stun | Lentitud + Ceguera + Debilidad por varios ticks |
| Rabia | Se activa bajo cierto % de HP con armadura pesada. Aumenta daño |
| Adrenalina | Se activa bajo cierto % de HP con armadura ligera. Aumenta velocidad |
| Coating | Aplicar veneno/efectos a tu arma por N cargas |
| Oneshot protection | Proteccion contra golpes que superan 3x tu HP maxima (con cooldown) |

---

## 📿 ValhallaTrinkets

Los **Trinkets** son accesorios que otorgan bonificaciones pasivas permanentes al equiparlos. Hay **36 trinkets** en el servidor, normalmente organizados en parejas básico/avanzado del mismo efecto.

### 📋 Lista completa de trinkets

| Trinket | Atributo principal | Valor |
|---|---|---|
| Pureza | Resistencia al veneno | +4.5% |
| Bezoar | Resistencia al veneno | +1.5% |
| Amuleto de Vitalidad | HP maxima | +0.2 |
| Erinle | HP maxima | +0.6 |
| Fuerza de Gungnir | Alcance de ataque | +0.188 |
| Anillo de Alcance | Alcance de ataque | +0.0625 |
| Collar Divino | Inmunidad plana | +0.6 |
| Collar de Cruz | Inmunidad plana | +0.2 |
| Narya | Resistencia al fuego | +3.75% |
| Anillo de Obsidiana | Resistencia al fuego | +1.25% |
| Banda de Precision | Prob. critico +0.175%, Daño critico +0.375% | — |
| Deathbringer | Prob. critico +0.375%, Daño critico +1% | — |
| Juggernaut | Armadura +0.75, Resistencia knockback +2% | — |
| Brazal Blindado | Armadura +0.25, Resistencia knockback +0.5% | — |
| Kratos | Daño melee | +0.75% |
| Amuleto del Vengador | Daño melee | +0.25% |
| Furia | Daño total +1.5%, Daño recibido +5% | — |
| Amuleto de Mania | Daño total +0.5%, Daño recibido +1.75% | — |
| Anillo de Shattering | Penetracion de armadura | +0.25% |
| Bane del Paladin | Penetracion de armadura | +0.75% |
| Anillo de Magnus | Resistencia magica | +3.75% |
| Anillo de Warding | Resistencia magica | +1.25% |
| Anillo de Defleccion | Resistencia a proyectiles | +0.75% |
| Athena | Resistencia a proyectiles | +2.5% |
| Renacimiento (Rebirth) | Bonus de curacion | +3.75% |
| Banda de Regeneracion | Bonus de curacion | +1.25% |
| Anillo de Proteccion | Resistencia al daño | +0.35% |
| Anillo Primordial | Resistencia al daño | +1.25% |
| Transfusion | Resistencia al sangrado | +3.75% |
| Vendaje Adhesivo | Resistencia al sangrado | +1.25% |
| Titan's Glove | Knockback | +0.125 |
| Banda de Fuerza | Knockback | +0.0438 |
| Artemis | Precision flecha +0.625, Ahorro municion -3.75%, Velocidad flecha +3.75% | — |
| Carcaj Magico | Precision flecha +0.25, Ahorro municion -1.25%, Velocidad flecha +1.25% | — |
| Hermes | Velocidad +3.75% (escalar), Altura de salto +0.125, Saltos extra +0.75 | — |
| Amuleto de Adrenalina | Velocidad +1.25% (escalar), Altura de salto +0.0438, Saltos extra +0.25 | — |

{% hint style="warning" %}
**Ajuste de balance (2 de noviembre de 2026):** los efectos de todos los amuletos se rebajaron un **50%** y la tabla de abajo ya muestra los valores nuevos. No cambiaron los **saltos extra** (Hermes y Amuleto de Adrenalina) ni el **daño recibido** de Furia y Amuleto de Mania. Los amuletos que ya tenías guardados **conservan los valores que tenían cuando los conseguiste**; los nuevos que encuentres salen con los valores rebajados.
{% endhint %}

**Nota:** DAMAGE_ALL y DAMAGE_MELEE son multiplicadores del sistema de combate de ValhallaMMO, no del sistema vanilla. DAMAGE_TAKEN aumenta el daño que recibes (trinkets de alto riesgo/alta recompensa como Furia).

---

## 📜 Comandos

### ⚔️ ValhallaMMO

| Comando | Descripcion |
|---|---|
| `/val` | Menu principal de ValhallaMMO |
| `/val help` | Lista todos los comandos disponibles |
| `/val skills` | Ver todos tus skills y niveles actuales |
| `/val skilltree [skill]` | Abrir el arbol de perks de un skill especifico |
| `/val stats` | Ver tus estadisticas personales de combate |
| `/val profile [jugador]` | Ver estadisticas detalladas de un jugador |
| `/val recipes` | Abrir el gestor de recetas personalizadas de ValhallaMMO |
| `/val resourcepack download` | Descargar el resource pack del plugin |

**Nombres de skills para `/val skilltree`:** `mining`, `woodcutting`, `digging`, `farming`, `fishing`, `alchemy`, `light_weapons`, `heavy_weapons`, `light_armor`, `heavy_armor`, `archery`, `martial_arts` ✨, `trading` ✨, `power` (Enchanting y Smithing están desactivados)

**Comercio:** para comerciar solo haz clic derecho sobre un aldeano con profesión. Haz **shift + clic** para ver su estado de ánimo. Detalle completo en la [página de Comercio](comercio.md).

### 📿 ValhallaTrinkets

| Comando | Descripcion |
|---|---|
| `/trinkets` | Abrir el menu de accesorios (trinkets) |

### 👥 Parties (grupos)

| Comando | Descripcion |
|---|---|
| `/party` | Menu de gestion de grupos |
| `/party join [id]` | Unirse a un grupo con su ID |
| `/party shareitem` | Compartir informacion de un item con el grupo |
