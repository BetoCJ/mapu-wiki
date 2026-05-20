# Skills — ValhallaMMO

El sistema de **Skills** (ValhallaMMO) reemplaza las habilidades vanilla y añade 14 habilidades con árboles de perks propios. Cada skill sube de nivel realizando su actividad correspondiente y desbloquea mejoras pasivas mediante un sistema de puntos de habilidad.

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

**Bono pasivo por cada nivel de Power:** +0.25 puntos de habilidad

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
| Perk A2 — Blast II | 60 | +25% radio TNT, +25% reduccion, +15% drops voladura, receta TNT x3 |
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
| Perk Carpentry | 60 | Recetas mejoradas de madera (6 tablas por tronco en vez de 4, escaleras x8, etc.) |
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
| Perk Combo (Mining 50) | 50 | Desbloquea conversiones de bloque: musgo, derretir, hacer hierba, crear concrete, etc. |
| Perk 3 — Crafter | 40 | Desbloquea recetas: arcilla, concrete x16 colores, podzol, mycelium, soul sand/soil |
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
| Perk Combo (Smithing 70) | 50 | Desbloquea recetas de salvage: recuperar materiales de equipo danado |
| Perk 2 | 20 | +25% multiplicador de esencia de pesca |
| Perk 3 | 40 | +20% velocidad de pesca, +1 suerte |
| Perk 4 | 60 | +12.5% drops de pesca |
| Perk 5 | 80 | +30% velocidad, +1.25 suerte |
| Perk 6 — Max | 100 | +12.5% drops, +50% multiplicador de esencia |

---

## Alchemy (max nivel 100)

**Como subir XP:** Preparar pociones en stand de pociones manualmente. El XP se multiplica por la calidad del resultado. Preparacion manual da 1.4x bonus vs automatica.

**Bono pasivo por nivel:** +0.75 habilidad de alquimia generica.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | -25% tiempo de preparacion, +10 habilidad de alquimia |
| Perk 2 | 20 | +10% ahorro de ingredientes, +15 habilidad |
| Perk A1 — Debuff | 40 | +15% intensidad splash, +10 habilidad debuff |
| Perk B1 — Buff | 40 | +10 habilidad buff, -37.5% tiempo de preparacion |
| Perk A2 — Splash | 60 | +10 habilidad debuff, +15% intensidad splash, +25% duracion/radio persistente, +25% velocidad lanzamiento |
| Perk B2 — Brew | 60 | +15 habilidad buff, +15% ahorro ingredientes, desbloquea pociones Haste y Health Boost |
| Perk Combo (LW o HW perk3) | 50 | +5 cargas de coating para armas, desbloquea recetas de viales (veneno, sagrado, anti-cura, daño) |
| Perk 3 — Combiner | 80 | -62.5% tiempo preparacion, desbloquea combinacion de pociones (hasta 1.5 combinaciones, -10% duracion) |
| Perk 4 — Transmutation | 100 | +25 habilidad general, radio de transmutacion +1, desbloquea pocion de transmutacion |

---

## Smithing (max nivel 100)

**Como subir XP:** Usar equipo — la durabilidad consumida al golpear bloques o mobs da XP. El tier del equipo importa: madera/cuero dan poca XP al principio, luego se penalizan al subir nivel y se prioriza el tier superior.

**Sistema de tier:** Al nivel 20 madera/cuero se penalizan y se desbloquea piedra/cobre; al 40 piedra/cobre se penalizan y sube hierro/oro; y asi sucesivamente.

**Bono pasivo por nivel:** +0.75 habilidad de crafteo generica (mejora calidad de items crafteados).

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 — Madera/Cuero | 0 | +25 habilidad crafteo madera, +25 habilidad cuero |
| Perk 2 — Piedra/Cobre | 20 | +25 habilidad piedra, +25 habilidad cadena, +25 habilidad cobre |
| Perk 3 — Hierro/Oro | 40 | +25 habilidad hierro/oro, desbloquea recetas de equipo de diamante |
| Perk Bows (Archery 50) | 50 | +25 habilidad arcos, +25 habilidad ballestas |
| Perk 4 — Diamante | 60 | +25 habilidad diamante, desbloquea reparacion de inventario sin perder encantamientos |
| Perk Prismarine | 70 | +25 habilidad prismarina, desbloquea receta de tridente |
| Perk 5 — Netherite | 80 | +25 habilidad netherite |
| Perk Enderic | 90 | +25 habilidad ender, desbloquea receta de elytra y cuero coral |
| Perk 6 — Max | 100 | +25 habilidad crafteo generica adicional |

---

## Enchanting (max nivel 100)

**Como subir XP:** Encantar objetos en mesa o yunque. XP base varia por encantamiento: Silk Touch/Infinity 700, Mending/Multishot/Flame 525, Fortune/Looting/Luck of the Sea 315, Sharpness/Efficiency/Piercing 126. Se multiplica por nivel del encantamiento.

**Penalizacion inicial:** -30% multiplicador de esencia, +100% refund y amplificacion (todo se recupera con perks).

**Bono pasivo por nivel:** +0.5 habilidad de encantamiento, +0.5 habilidad de yunque.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +10 habilidad encantamiento, +10 habilidad yunque |
| Perk A1 — Lapis | 20 | +5% refund de esencia, +10% ahorro de lapislazuli |
| Perk B1 — Esencia | 20 | +15% multiplicador esencia, +2.5% XP de todos los skills |
| Perk 2 | 40 | +15 habilidad encantamiento/yunque, +5% refund esencia |
| Perk A2 | 40 | +5% refund, +15% ahorro lapis, +10 habilidad enchant/yunque |
| Perk B2 — Elemental | 60 | +25% esencia, +7.5% XP todos skills, +20% conversion daño elemental, +25% multiplicador elemental |
| Perk Radiant/Necrotic | req. B2 | Exclusivo: elige tipo elemental Radiant (sagrado) o Necrotic (oscuro) |
| Perk Combo (Farming 50) | 70 | +0.5 suerte global |
| Perk 3 | 80 | +15 habilidad encantamiento/yunque |
| Perk Sharpnesses/Protections | req. 2 | Exclusivo: +0.5 nivel efectivo a encantamientos de daño O de proteccion |
| Perk 4 | 100 | +25 habilidad encantamiento/yunque |
| Perk Looting/Fortune/Unbreaking | req. 3 | Exclusivo: +1 nivel efectivo al encantamiento elegido |
| Perk Offensive/Defensive/Utility | req. 4 | Exclusivo: +0.5 nivel a categoria de encantamientos elegida |

---

## Light Weapons (max nivel 100)

**Como subir XP:** Golpear con espadas, dagas, rapiers, lanzas. 4.9 XP por punto de daño.

**Penalizacion inicial:** -30% daño, -30% knockback. Estas penalizaciones se recuperan completamente subiendo el skill.

**Bono pasivo por nivel:** +0.25% velocidad de ataque, +0.25% daño.

**Arbol de perks:**

| Perk | Nivel req. | Bonos |
|---|---|---|
| Perk 1 | 0 | +5% daño, +5% probabilidad de sangrado |
| Perk 2 | 20 | +5% velocidad ataque, +5% probabilidad critico |
| Perk 3 — Parry | 40 | +5% daño. Desbloquea parry: ventana efect. 3.5t, vuln. 7t, CD 50, reduccion daño 37.5%, debuff enemigo 15t |
| Perk 4 | 60 | +10% velocidad, +5% reduccion inmunidad, +5% sangrado |
| Perk A1 — Coating I | 50 | Desbloquea coating de arma (+1.5 cargas, -40% duracion, -25% amplificador) |
| Perk A2 — Coating II | 70 | +2 cargas coating, +5% duracion, +12.5% amplificador |
| Perk 5 | 80 | +5% sangrado, +5% daño, +10% reduccion inmunidad, mejora estadisticas de parry |
| Perk Combo (Heavy Armor 70) | 70 | +5 penetracion plana de armadura, +0.5 alcance de ataque, +15% knockback |
| Perk 6 — Max | 100 | +5% crit, +15% daño critico, sangrado al critico, +1 daño de sangrado |

---

## Heavy Weapons (max nivel 100)

**Como subir XP:** Golpear con hachas, martillos de guerra, mazas, mandobles. 7 XP por punto de daño.

**Penalizacion inicial:** -30% velocidad de ataque, -30% daño.

**Bono pasivo por nivel:** +0.25% velocidad de ataque, +0.25% daño.

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

**Penalizacion inicial:** -30% efectividad de armadura, -2.5% velocidad/pieza, -6.25% ahorro hambre/pieza, -6.25% curacion/pieza. Bonus inicial: +2.5% esquiva/pieza.

**Bono pasivo por nivel:** +0.25% efectividad de armadura.

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

**Penalizacion inicial:** -30% efectividad armadura, -5% velocidad/pieza, -12.5% hambre/pieza, -12.5% curacion/pieza, +3 imprecision de archeria.

**Bono pasivo por nivel:** +0.25% efectividad de armadura.

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
| Perk 2 | 20 | +5% ahorro de flechas, desbloquea receta flechas de piedra |
| Perk C1 — Charged Shot | 40 | Desbloquea disparo cargado (CD 300, 1.5 cargas, pierce 0.5, knockback 0.5, velocidad +25%) |
| Perk 3 | 40 | -0.75 imprecision, +5% crit arco/ballesta, flechas de cobre y doradas |
| Perk Stealth (Light Armor 50) | 50 | Crit garantizado desde sigilo, sangrado al critico, +25% daño critico |
| Perk 4 | 60 | +5% daño arco/ballesta, +10% ahorro flechas, +2.5% daño por distancia, flechas de hierro y teleportacion |
| Perk 5 | 80 | +10% crit, -1.25 imprecision, +15% daño critico, flechas de diamante |
| Perk C2 — Charged II | 80 | Mejora charged shot: velocidad maxima, recarga instantanea ballesta, sin gravedad, +10% daño, -100 CD, +1 carga |
| Perk 6 — Max | 100 | +5% daño por distancia, +15% daño con Infinity, flechas de netherite y anti-inmunidad |

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

Los **Trinkets** son accesorios que otorgan bonificaciones pasivas permanentes al equiparlos. Solo puedes equipar un trinket del mismo tipo a la vez.

### Lista completa de trinkets

| Trinket | Atributo principal | Valor |
|---|---|---|
| Pureza | Resistencia al veneno | +45% |
| Bezoar | Resistencia al veneno | +15% |
| Amuleto de Vitalidad | HP maxima | +2 (1 corazon) |
| Erinle | HP maxima | +6 (3 corazones) |
| Fuerza de Gungnir | Alcance de ataque | +0.75 |
| Anillo de Alcance | Alcance de ataque | +0.25 |
| Collar Divino | Inmunidad plana | +6 |
| Collar de Cruz | Inmunidad plana | +2 |
| Narya | Resistencia al fuego | +37.5% |
| Anillo de Obsidiana | Resistencia al fuego | +12.5% |
| Banda de Precision | Prob. critico +3.5%, Daño critico +7.5% | — |
| Deathbringer | Prob. critico +7.5%, Daño critico +20% | — |
| Juggernaut | Armadura +7.5, Resistencia knockback +20% | — |
| Brazal Blindado | Armadura +2.5, Resistencia knockback +5% | — |
| Kratos | Daño melee | +15% |
| Amuleto del Vengador | Daño melee | +5% |
| Furia | Daño total +30%, Daño recibido +50% | — |
| Amuleto de Mania | Daño total +10%, Daño recibido +17.5% | — |
| Anillo de Shattering | Penetracion de armadura | +5% |
| Bane del Paladin | Penetracion de armadura | +15% |
| Anillo de Magnus | Resistencia magica | +37.5% |
| Anillo de Warding | Resistencia magica | +12.5% |
| Anillo de Defleccion | Resistencia a proyectiles | +7.5% |
| Athena | Resistencia a proyectiles | +25% |
| Renacimiento (Rebirth) | Bonus de curacion | +37.5% |
| Banda de Regeneracion | Bonus de curacion | +12.5% |
| Anillo de Proteccion | Resistencia al daño | +3.5% |
| Anillo Primordial | Resistencia al daño | +12.5% |
| Transfusion | Resistencia al sangrado | +37.5% |
| Vendaje Adhesivo | Resistencia al sangrado | +12.5% |
| Titan's Glove | Knockback | +0.5 |
| Banda de Fuerza | Knockback | +0.175 |
| Artemis | Precision flecha +2.5, Ahorro municion -15%, Velocidad flecha +15% | — |
| Carcaj Magico | Precision flecha +1.0, Ahorro municion -5%, Velocidad flecha +5% | — |
| Hermes | Velocidad +15% (escalar), Altura de salto +0.5, Saltos extra +1.5 | — |
| Amuleto de Adrenalina | Velocidad +5% (escalar), Altura de salto +0.175, Saltos extra +0.5 | — |

**Nota:** DAMAGE_ALL y DAMAGE_MELEE son multiplicadores del sistema de combate de ValhallaMMO, no del sistema vanilla. DAMAGE_TAKEN aumenta el daño que recibes (trinkets de alto riesgo/alta recompensa como Furia).

---

## Comandos

| Comando | Descripcion |
|---|---|
| `/val` | Menu principal de ValhallaMMO |
| `/val skills` | Ver todos tus skills y niveles actuales |
| `/val stats` | Ver tus estadisticas personales de combate |
| `/val skilltree [skill]` | Abrir el arbol de perks de un skill especifico |

**Nombres de skills para el comando:** `mining`, `woodcutting`, `digging`, `farming`, `fishing`, `alchemy`, `smithing`, `enchanting`, `light_weapons`, `heavy_weapons`, `light_armor`, `heavy_armor`, `archery`, `power`
