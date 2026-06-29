# ⚔️ Skills — ValhallaMMO y ValhallaTrinkets

## Introduccion — Empieza aqui

Si es la primera vez que ves este sistema, lee esto antes de continuar.

### ¿Que es ValhallaMMO?

ValhallaMMO es un plugin RPG que reemplaza el sistema de habilidades vanilla de Minecraft. Al jugar normalmente — minar, talar, pelear, pescar — vas subiendo de nivel en 14 skills distintas. Subir de nivel desbloquea mejoras permanentes llamadas **perks**.

No necesitas hacer nada especial para empezar: desde el primer bloque que mines o el primer mob que mates ya estaras ganando XP.

### El loop de juego

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

### Las 14 skills

De las 14 skills del plugin, **13 están activas** en el servidor. Solo **Enchanting** está desactivada (ver más abajo).

| Categoria | Skills |
|---|---|
| Recoleccion | Mining, Woodcutting, Digging, Farming, Fishing |
| Artesania | Alchemy, Smithing |
| Combate | Light Weapons, Heavy Weapons, Light Armor, Heavy Armor, Archery |
| Central | Power |
| ❌ Desactivada | Enchanting |

| Skill | Como ganar XP |
|---|---|
| Mining | Minando bloques (diamante, obsidiana y minerales raros dan mas XP) |
| Woodcutting | Talando troncos de madera |
| Digging | Cavando tierra, arena, grava, barro |
| Farming | Cosechando cultivos maduros |
| Fishing | Pescando |
| Alchemy | Elaborando pociones en calderos y soportes de pociones |
| Smithing | Gastando la durabilidad de herramientas y armaduras que craftees |
| Light Weapons | Pegando con espadas, dagas o cuchillos |
| Heavy Weapons | Pegando con hachas o mazas |
| Light Armor | Recibiendo daño con armadura ligera equipada |
| Heavy Armor | Recibiendo daño con armadura pesada equipada |
| Archery | Disparando flechas con arco o ballesta |
| Power | Sube automaticamente cada vez que sube cualquier otro skill |

### Que es Power

**Power** es el skill central (nivel maximo 256). No lo subes directamente: cada vez que cualquier otra skill sube de nivel, Power recibe XP automaticamente. Al subir Power obtienes **1 punto de habilidad** por nivel, que son los que usas para desbloquear perks.

### Que son los Perks

Los perks son mejoras permanentes organizadas en un arbol visual. Cada perk tiene:
- Un **nivel minimo** del skill requerido para desbloquearlo
- Un **costo en puntos de habilidad** (obtenidos de Power)

Para ver el arbol de un skill usa `/val skilltree [skill]` en el juego. Los perks desbloqueados no se pierden al morir ni al reiniciar el servidor.

### Como es diferente el combate

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

## ¿Que es ValhallaTrinkets?

ValhallaTrinkets es un plugin complementario que añade **accesorios equipables** (trinkets) con bonos pasivos permanentes. Se accede con `/trinkets`.

### Como funcionan los trinkets

- Abres el menu con `/trinkets` — se abre una ventana separada de tu inventario normal
- Tienes hasta **7 ranuras** de trinket (las primeras 5 disponibles para todos; las ultimas 2 requieren el permiso de un rango)
- Cada trinket da uno o varios atributos: daño, velocidad, resistencia, critico, etc.
- Todos los trinkets del servidor comparten la misma categoria interna ("Accesorio"), asi que **puedes combinar hasta 7 trinkets distintos a la vez** — no hay una restriccion de "uno por tipo" como anillo/collar/etc.
- Los trinkets **se dropean al morir** (a menos que el servidor tenga keepInventory activo)
- Los bonos son pasivos: no tienes que hacer nada, se aplican solos mientras los tengas equipados

### Como conseguir trinkets

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

## Mecanica general

- Al subir de nivel en cualquier skill, **Power** recibe 70 XP automáticamente.
- Al subir **Power**, obtienes **0.25 puntos de habilidad** por nivel.
- Los puntos se gastan en los árboles de perks individuales de cada skill.
- Los perks son permanentes — ni la muerte ni el reinicio los elimina.
- Usa `/val skilltree [skill]` para abrir el árbol visual en el juego.

---

## Power (max nivel 256)

**Power** es el skill central que une todas las demás habilidades.

**Bonos iniciales al unirte:**
- +3 puntos de habilidad
- +0.5% daño crítico, +2 daño de sangrado, +80 ticks de duración de sangrado
- +2% resistencia radiante, +10% protección contra oneshot (CD 6000 ticks)

**Bono pasivo por cada nivel de Power:** +1 punto de habilidad

**Perks especiales por nivel (acumulables):**
- Cada 10 niveles hasta el 80: +0.1 resistencia PvP (máximo +0.8 al nivel 80)

**Árbol de perks de Power** (7 columnas, 3 niveles cada una):

| Columna | Nivel 0 | Nivel 30 | Nivel 60 |
|---|---|---|---|
| Vida | +1 corazon max | +1.5 corazones | +2.5 corazones |
| Armadura | +1 armadura | +1.5 armadura | +2.5 armadura |
| Suerte | +0.1 suerte | +0.15 suerte | +0.25 suerte |
| Regeneracion HP | +10% regen | +15% regen | +25% regen |
| Daño de ataque | +2.5% daño | +3.75% daño | +6.25% daño |
| Drops de mobs | +10% drops | +15% drops | +25% drops |
| Reduccion de CD | -5% cooldowns | -7.5% cooldowns | -12.5% cooldowns |

---

## Mining (max nivel 100)

**Como subir XP:** Minar bloques. Diamante 280 XP, Diamante Deepslate 420, Ancient Debris 1120, Esmeralda 280, Oro 112, Hierro 56.

**Penalizacion inicial:** -30% drops de mineria hasta que subes el skill.

**Bono pasivo por nivel:** +0.5% drops de mineria, +0.5% drops de voladura (TNT).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% velocidad de minado, +5% XP de bloque |
| Perk 2 | 20 | +5% drops, +0.5 suerte, +12.5% velocidad de coccion |
| Perk B1 — Drilling | 40 | +10% velocidad, +10% XP, desbloquea perforacion (velocidad x2, CD 600, dur. 100) |
| Perk A1 — Blast I | 40 | +25% radio TNT, +25% reduccion daño TNT, +10% drops de voladura |
| Perk B2 — Vein | 60 | +10% drops, +1.5 suerte, desbloquea vein mining (todos los minerales) |
| Perk A2 — Blast II | 60 | +25% radio TNT, +25% reduccion daño TNT, +15% drops voladura |
| Perk A3 — Blast Mode | 70 | Req. tambien Enchanting 70. Elige: Silk Touch o Fortune para voladuras |
| Perk 3 — Mastery | 80 | +1.5 velocidad drill, -300 CD drill, +50% multiplicador XP bloque, +12.5% coccion |
| Perk 4 — Max | 100 | Pickup instantaneo en vein mining, extiende vein a piedra y basalto |

---

## Woodcutting (max nivel 100)

**Como subir XP:** Talar madera. Tronco normal 28 XP, Madera (wood block) 42, Hongos del Nether 56; Descorezar (strip) da 14-28 XP.

**Bono pasivo por nivel:** +0.25% velocidad de tala, +0.5% drops de madera.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% velocidad de tala, +5% XP de bloque |
| Perk 2 | 20 | +5% XP, +5 suerte |
| Perk Combo (Digging 50) | 50 | +15% bonos de comida (todos tipos), +15% regen HP, +15% ahorro de hambre |
| Perk 3 — Treecapitator | 40 | Desbloquea tala de arboles completos (CD 100, limite 8 bloques) |
| Perk Capitator A | 60 | -30 CD treecapitator, +16 limite de bloques (total 24) |
| Perk Carpentry | 60 | Bonos de tala adicionales |
| Perk Capitator B | 80 | -40 CD treecapitator, +40 limite de bloques (total 64) |
| Perk 4 | 80 | +15% XP, +5% velocidad, +100% tasa de crecimiento instantaneo |
| Perk 5 | 100 | +5 suerte adicional |

---

## Digging (max nivel 100)

**Como subir XP:** Cavar tierra, arena, arcilla. Drops especiales de arqueologia dan mucho XP: Diamante (drop) 350, Netherite scrap 700, Echo Shard 1400.

**Bono pasivo por nivel:** +0.5% drops, +0.25% velocidad de excavacion.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +15% velocidad de excavar, +5% XP |
| Perk 2 | 20 | +1.5 suerte, +10% XP |
| Perk Combo (Mining 50) | 50 | +15% bonos de comida (todos tipos), +15% regen HP, +15% ahorro de hambre |
| Perk 3 | 40 | Desbloquea conversiones de bloque: podzol, mycelium, arcilla, concrete, soul sand/soil (via bloque de conversion, no mesa de crafteo) |
| Perk A1 — Archeology I | 60 | +10% probabilidad de repeticion arqueologica, +1.5 suerte arqueologica |
| Perk B1 — Speed | 60 | +25% velocidad de excavacion adicional |
| Perk A2 — Archeology II | 80 | +15% repeticion, probabilidad de generar arena/grava sospechosa cerca de estructuras |
| Perk B2 | 80 | +1.5 suerte |
| Perk 4 — Max | 100 | +1.5 suerte adicional (req. A2 o B2) |

---

## Farming (max nivel 100)

**Como subir XP:** Cosechar cultivos (trigo 33.6, melon 56, zanahoria 28), criar animales (vacas 84, cerdos 70), esquilar ovejas 140, interactuar con colmenas 280.

**Bono pasivo por nivel:** +0.5% drops de agricultura.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | Desbloquea cosecha instantanea al romper cultivos maduros |
| Perk 1C — Carroñero | 30 | Inmunidad a comida mala, +2 HP/sat en comida cruda y podrida (bloquea Perk 2C) |
| Perk 2 | 20 | +15% XP de agriculture, +50% tasa de crecimiento instantaneo |
| Perk 2C — Gourmet | 50 | +0.1 bonus de comida en todos los tipos (bloquea Perk 1C) |
| Perk 3 | 40 | +15% XP, +1.5 suerte, +10% drops |
| Perk 1A — Ganadero | 40 | +20% velocidad de crecimiento animal, +10% drops de matanza, +25% XP cria |
| Perk 1B — Apicultor | 50 | Inmunidad a agresion de abejas, +25% probabilidad de ahorrar miel en colmena |
| Perk 2A — Carnicero | 60 | +30% vel. crecimiento, +15% drops matanza, +25% XP cria, +150% daño a animales |
| Perk 4 | 80 | +20% XP, +1.5 suerte, +15% drops |
| Perk 5 — Field Harvest | 100 | Desbloquea cosecha masiva de campo (pickup automatico, CD 50 ticks) |

---

## Fishing (max nivel 100)

**Como subir XP:** Pescar. Bacalao 140, Salmon 175, Pez globo 350, Pez tropical 560, Libro encantado/Arco/Cana 420.

**Bono pasivo por nivel:** +1% velocidad de pesca, +1% drops de pesca.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +0.75 suerte de pesca |
| Perk Combo (Smithing 70) | 50 | Requiere Smithing 70 (skill desactivado — perk no disponible actualmente) |
| Perk 2 | 20 | +25% multiplicador de esencia de pesca |
| Perk 3 | 40 | +20% velocidad de pesca, +1 suerte |
| Perk 4 | 60 | +12.5% drops de pesca |
| Perk 5 | 80 | +30% velocidad, +1.25 suerte |
| Perk 6 — Max | 100 | +12.5% drops, +50% multiplicador de esencia |

---

## 🧪 Alchemy (max nivel 100)

**Como subir XP:** Elaborando pociones en calderos y soportes de pociones. El XP depende de la **calidad** de la poción resultante (no hay una cifra fija por receta): elaborar manualmente da un multiplicador de **x1.4**, mientras que elaborar de forma automatizada (con droppers/hoppers) reduce el XP a un multiplicador de **x0.25**.

**Calidad de las pociones:** cada poción tiene una puntuación de calidad que le da una etiqueta cosmética: Rancid (0), Tainted (30), Dirty (60), Cloudy (90), Clear (120), Refined (150), Pure (200), Shimmering (300+).

**Bono pasivo por nivel:** +0.75 a la habilidad general de elaboración (`genericbrewingskill`).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | -25% tiempo de fermentación, +10 habilidad de elaboración |
| Perk 2 | 20 | +10% probabilidad de ahorrar ingredientes, +15 habilidad de elaboración |
| Perk A1 — Debuffs I | 40 | +0.15 intensidad mínima de splash, +10 habilidad de pociones debilitantes |
| Perk B1 — Buffs I | 40 | +10 habilidad de pociones de beneficio, -37.5% tiempo de fermentación |
| Perk Combo (Light/Heavy Weapons 50) | 50 | Desbloquea untar armas con viales (veneno, santo, anti-curación, daño) |
| Perk A2 — Debuffs II | 60 | +15 habilidad debilitante, +0.15 intensidad splash, +25% duración/radio de poción persistente, +25% velocidad de lanzamiento |
| Perk B2 — Buffs II | 60 | +15 habilidad de beneficio, +15% ahorro de ingredientes. Desbloquea recetas de Prisa y Aumento de Salud |
| Perk 3 — Combinación | 80 | -62.5% tiempo de fermentación. Desbloquea combinar hasta 1.5 efectos de poción en una sola |
| Perk 4 — Transmutación | 100 | +25 habilidad de elaboración, +1 radio de transmutación. Desbloquea todas las transmutaciones y la receta de Poción de Transmutación |

**Sistema de Transmutación:** con la Poción de Transmutación (desbloqueada en el perk final) puedes convertir ciertos bloques en otros usando un caldero — por ejemplo, troncos de un tipo de madera a otro, o minerales/bloques de valor (Hierro→Oro, Cobre→Hierro, Esmeralda↔Diamante) en lo que el plugin llama transmutación "Midas".

---

## 🔨 Smithing (max nivel 100)

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
| Perk 1 | 0 | +25 habilidad de crafteo en madera y cuero |
| Perk 2 | 20 | +25 habilidad en piedra, cadena y cobre |
| Perk 3 | 40 | +25 habilidad en hierro y oro. Desbloquea las 16 recetas de equipo de Diamante (armadura completa, espada, hacha, pico, pala, azada, martillo de guerra, mandoble, lanza, daga, estoque, maza, lanza real) |
| Perk Arcos (Archery 50) | 50 | Requiere Archery 50. +25 habilidad de arcos y ballestas |
| Perk Prismarino | 70 | Requiere Perk 3. +25 habilidad con prismarina. Desbloquea receta del Tridente |
| Perk 4 | 60 | +25 habilidad en diamante. Permite reparar conservando encantamientos al usar el inventario |
| Perk Enderico | 90 | Requiere Perk 4. +25 habilidad enderica. Desbloquea recetas de Élitros y Cuero Coral |
| Perk 5 | 80 | +25 habilidad en netherite |
| Perk 6 — Maestria | 100 | +25 habilidad de crafteo general |

**Calidad del equipo:** cada pieza que crafteas tiene una puntuación de calidad que determina su etiqueta: Terrible (-500 a -60), Shoddy (-60 a -30), Decent (-30 a 0), Good (0 a 30), Great (30 a 60), Flawless (60 a 90), Masterful (90 a 120), Fabled (120 a 150), Peerless (150+).

---

## Enchanting — no disponible

El skill de Enchanting no esta activo actualmente en el servidor. La mesa de encantamiento y el yunque funcionan en modo vanilla estandar. No se gana XP de Enchanting ni se puede acceder a su arbol de perks.

---

## Light Weapons (max nivel 100)

**Como subir XP:** Golpear con espadas, dagas, rapiers, lanzas. 4.9 XP por punto de daño.

**Bono pasivo por nivel:** +0.25% velocidad de ataque, +0.25% daño (acumulativo sobre el baseline vanilla).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% daño, +5% probabilidad de sangrado |
| Perk 2 | 20 | +5% velocidad ataque, +5% probabilidad critico |
| Perk 3 — Parry | 40 | +5% daño. Desbloquea parry: ventana efect. 4t, vuln. 7t, CD 50, reduccion daño 37.5%, debuff enemigo 15t |
| Perk 4 | 60 | +10% velocidad, +5% reduccion inmunidad, +5% sangrado |
| Perk A1 — Coating I | 50 | Desbloquea coating de arma (+2 cargas, -40% duracion, -25% amplificador) |
| Perk A2 — Coating II | 70 | +2 cargas coating, +5% duracion, +12.5% amplificador |
| Perk 5 | 80 | +5% sangrado, +5% daño, +10% reduccion inmunidad. Mejora parry: +4t ventana efectiva, -30 CD, +5t debuff enemigo, -5t debuff propio, +12.5% reduccion daño, +25% reduccion CD en parry exitoso |
| Perk Combo (Heavy Armor 70) | 70 | +5 penetracion plana de armadura, +0.5 alcance de ataque, +15% knockback |
| Perk 6 — Max | 100 | +5% crit, +15% daño critico, sangrado al critico, +1 daño de sangrado |

---

## Heavy Weapons (max nivel 100)

**Como subir XP:** Golpear con hachas, martillos de guerra, mazas, mandobles. 7 XP por punto de daño.

**Bono pasivo por nivel:** +0.25% velocidad de ataque, +0.25% daño (acumulativo sobre el baseline vanilla).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% daño |
| Perk 2 | 20 | +5% daño de poder (power attack), +5% crit |
| Perk 3 — Power Attack | 40 | +5% daño, +25% fraccion power attack, +0.75 radio power attack |
| Perk 4 | 60 | +7.5% daño power attack, +2.5 penetracion plana |
| Perk A1 — Coating I | 50 | Desbloquea coating (+1 carga, -40% duracion, -12.5% amplificador) |
| Perk A2 — Coating II | 70 | +1 carga, +5% duracion, +12.5% amplificador |
| Perk 5 | 80 | +5% daño, +12.5% fraccion power attack, +0.25 radio, +5 penetracion plana |
| Perk Combo (Woodcutting 70) | 70 | +10% probabilidad de stun, +10% penetracion de armadura fraccion, +2.5% daño vs armadura ligera |
| Perk 6 — Max | 100 | +5% crit, +15% daño critico, sangrado al critico, +0.5 daño de sangrado |

---

## Light Armor (max nivel 100)

**Como subir XP:** Recibir daño con armadura ligera (cuero, cota de malla). 7 XP base por pieza, 3.5 XP adicional por segunda pieza o mas.

**Bonus inicial:** +2.5% esquiva por pieza equipada.

**Bono pasivo por nivel:** +0.25% efectividad de armadura (acumulativo sobre el baseline vanilla).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% efectividad armadura ligera |
| Perk 1A | 20 | +0.5% velocidad/pieza, +1.75% ahorro hambre/pieza, +1.75% curacion/pieza |
| Perk 1B | 40 | +15% ahorro hambre conjunto completo, +5% efectividad armadura |
| Perk 1C — Adrenalina | 50 | Desbloquea modo adrenalina (umbral 15% HP, nivel 0.5, CD 6000 ticks) |
| Perk Combo (Heavy Weapons 50) | 50 | +25% resistencia a crits enemigos, +50% resistencia a stun |
| Perk 2A | 60 | Reduce requisito de piezas para set bonus en 0.5. +0.75% vel/pieza, +1.375% hambre y curacion/pieza |
| Perk 2B | 60 | +10% esquiva con conjunto completo, +5% efectividad armadura |
| Perk 2C — Adrenalina II | 90 | +2 nivel adrenalina, +10% umbral, -3000 CD |
| Perk 2 — Maestria | 100 | Inmunidad a Veneno/Ceguera/Hambre, +20% resistencia magica |

---

## Heavy Armor (max nivel 100)

**Como subir XP:** Recibir daño con armadura pesada (hierro, diamante, netherite, dorada). Mismo sistema que Light Armor.

**Bono pasivo por nivel:** +0.25% efectividad de armadura (acumulativo sobre el baseline vanilla).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% efectividad armadura pesada |
| Perk 1A | 20 | +0.94% velocidad/pieza, +1.25% hambre/pieza, +1.25% curacion/pieza, -0.5 imprecision archeria |
| Perk 1B | 40 | +20% bono curacion conjunto completo, +5% efectividad armadura |
| Perk 1C — Rabia | 50 | Desbloquea modo rabia (umbral 15% HP, nivel 0.5, CD 6000 ticks) |
| Perk Combo (Light Weapons 50) | 50 | +25% resistencia a crits, +12.5% bonus de fraccion de inmunidad |
| Perk 2A | 60 | Reduce requisito set en 0.5. +0.94% vel/pieza, +2.5% hambre/pieza, +2.5% curacion/pieza, -0.5 imprecision |
| Perk 2B | 80 | +5% probabilidad reflejo, +10% fraccion reflejo de daño, +5% efectividad armadura |
| Perk 2C — Rabia II | 90 | +2 nivel rabia, +10% umbral, -3000 CD |
| Perk 2 — Maestria | 100 | Inmunidad a Lentitud/Debilidad/Levitacion, +20% resistencia a knockback |

---

## Archery (max nivel 100)

**Como subir XP:** Disparar con arco (21 XP base) o ballesta (28 XP base). El XP aumenta con la distancia del disparo.

**Penalizacion inicial:** +5 imprecision, -20% daño de arco, -30% daño con Infinity.

**Bono pasivo por nivel:** +0.2% daño de arco.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | -0.5 imprecision, +5% daño arco, +5% daño ballesta |
| Perk 2 | 20 | +5% ahorro de flechas |
| Perk C1 — Charged Shot | 40 | Desbloquea disparo cargado (CD 300, 2 cargas, pierce 1, knockback 1, velocidad +25%) |
| Perk 3 | 40 | -0.75 imprecision, +5% crit arco/ballesta |
| Perk Stealth (Light Armor 50) | 50 | Crit garantizado desde sigilo, sangrado al critico, +25% daño critico |
| Perk 4 | 60 | +5% daño arco/ballesta, +10% ahorro flechas, +2.5% daño por distancia |
| Perk 5 | 80 | +10% crit, -1.25 imprecision, +15% daño critico |
| Perk C2 — Charged II | 80 | Mejora charged shot: velocidad maxima, recarga instantanea ballesta, sin gravedad, +10% daño, -100 CD, +1 carga, +1 knockback |
| Perk 6 — Max | 100 | +5% daño por distancia, +15% daño con Infinity |

---

## Sistema de Combate

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

## ValhallaTrinkets

Los **Trinkets** son accesorios que otorgan bonificaciones pasivas permanentes al equiparlos. Hay **36 trinkets** en el servidor, normalmente organizados en parejas básico/avanzado del mismo efecto.

### Lista completa de trinkets

| Trinket | Atributo principal | Valor |
|---|---|---|
| Pureza | Resistencia al veneno | +9% |
| Bezoar | Resistencia al veneno | +3% |
| Amuleto de Vitalidad | HP maxima | +0.4 |
| Erinle | HP maxima | +1.2 |
| Fuerza de Gungnir | Alcance de ataque | +0.375 |
| Anillo de Alcance | Alcance de ataque | +0.125 |
| Collar Divino | Inmunidad plana | +1.2 |
| Collar de Cruz | Inmunidad plana | +0.4 |
| Narya | Resistencia al fuego | +7.5% |
| Anillo de Obsidiana | Resistencia al fuego | +2.5% |
| Banda de Precision | Prob. critico +0.35%, Daño critico +0.75% | — |
| Deathbringer | Prob. critico +0.75%, Daño critico +2% | — |
| Juggernaut | Armadura +1.5, Resistencia knockback +4% | — |
| Brazal Blindado | Armadura +0.5, Resistencia knockback +1% | — |
| Kratos | Daño melee | +1.5% |
| Amuleto del Vengador | Daño melee | +0.5% |
| Furia | Daño total +3%, Daño recibido +5% | — |
| Amuleto de Mania | Daño total +1%, Daño recibido +1.75% | — |
| Anillo de Shattering | Penetracion de armadura | +0.5% |
| Bane del Paladin | Penetracion de armadura | +1.5% |
| Anillo de Magnus | Resistencia magica | +7.5% |
| Anillo de Warding | Resistencia magica | +2.5% |
| Anillo de Defleccion | Resistencia a proyectiles | +1.5% |
| Athena | Resistencia a proyectiles | +5% |
| Renacimiento (Rebirth) | Bonus de curacion | +7.5% |
| Banda de Regeneracion | Bonus de curacion | +2.5% |
| Anillo de Proteccion | Resistencia al daño | +0.7% |
| Anillo Primordial | Resistencia al daño | +2.5% |
| Transfusion | Resistencia al sangrado | +7.5% |
| Vendaje Adhesivo | Resistencia al sangrado | +2.5% |
| Titan's Glove | Knockback | +0.25 |
| Banda de Fuerza | Knockback | +0.0875 |
| Artemis | Precision flecha +1.25, Ahorro municion -7.5%, Velocidad flecha +7.5% | — |
| Carcaj Magico | Precision flecha +0.5, Ahorro municion -2.5%, Velocidad flecha +2.5% | — |
| Hermes | Velocidad +7.5% (escalar), Altura de salto +0.25, Saltos extra +0.75 | — |
| Amuleto de Adrenalina | Velocidad +2.5% (escalar), Altura de salto +0.0875, Saltos extra +0.25 | — |

**Nota:** DAMAGE_ALL y DAMAGE_MELEE son multiplicadores del sistema de combate de ValhallaMMO, no del sistema vanilla. DAMAGE_TAKEN aumenta el daño que recibes (trinkets de alto riesgo/alta recompensa como Furia).

---

## Comandos

### ValhallaMMO

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

**Nombres de skills para `/val skilltree`:** `mining`, `woodcutting`, `digging`, `farming`, `fishing`, `alchemy`, `smithing`, `light_weapons`, `heavy_weapons`, `light_armor`, `heavy_armor`, `archery`, `power`

### ValhallaTrinkets

| Comando | Descripcion |
|---|---|
| `/trinkets` | Abrir el menu de accesorios (trinkets) |

### Parties (grupos)

| Comando | Descripcion |
|---|---|
| `/party` | Menu de gestion de grupos |
| `/party join [id]` | Unirse a un grupo con su ID |
| `/party shareitem` | Compartir informacion de un item con el grupo |
