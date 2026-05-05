# Encantamientos Personalizados

Mapucraft usa el plugin **AdvancedEnchantments v9.10.1** para ofrecer un sistema de encantamientos completamente personalizado. Todos los encantamientos son adicionales a los vanilla y funcionan con el mismo equipo de siempre.

---

## Como obtenerlos

### Enchanter (`/enchanter`)
El metodo principal. Abre el menu del encantador y compra libros de encantamiento gastando **experiencia** o **dinero**. Puedes comprar libros de cualquier rareza o un libro aleatorio de un grupo especifico.

### Mesa de Encantamiento
Al encantar objetos en la mesa vanilla hay un **45% de probabilidad** de que el objeto reciba adicionalmente un encantamiento personalizado. Las chances por grupo son:

| Rareza | Probabilidad de aparecer |
|--------|--------------------------|
| Simple | 50% |
| Unico | 40% |
| Elite | 30% |
| Ultimate | 20% |
| Legendario | 10% |
| Fabled | No disponible en mesa |

Con el nivel mas alto de encantamiento puedes recibir entre 2 y 3 encantamientos custom a la vez.

### Tinkerer (`/tinkerer`)
Intercambia libros de encantamiento que no quieras por **Polvo Magico**. Util para deshacerse de encantamientos duplicados o de rarezas bajas.

### Alchemist (`/alchemist`)
Combina polvo magico para obtener **polvo de mayor calidad**, que aumenta la tasa de exito al aplicar libros.

### Auction House (`/ah`)
Otros jugadores pueden publicar libros de encantamiento a la venta.

---

## Sistema de Ranuras (Slots)

Cada objeto tiene un numero limitado de **ranuras de encantamiento**:

- **Maximo base:** 15 ranuras
- **Maximo con mejoras:** 20 ranuras

Las ranuras se pueden aumentar usando **Aumentadores de Ranura** (Slot Increasers), que se obtienen en el Enchanter o como loot. Agregar encantamientos consume ranuras segun el grupo del encantamiento.

El numero de ranuras disponibles se puede ver en el objeto si el servidor lo tiene habilitado.

---

## Sistema de Aplicacion

Cuando aplicas un libro de encantamiento arrastandolo sobre un objeto, hay dos metricas importantes:

- **Tasa de exito:** Probabilidad de que el encantamiento se aplique correctamente.
- **Tasa de destruccion:** Probabilidad de que el objeto se destruya si el encantamiento falla.

Puedes modificar estas tasas con **Polvo Magico** (aumenta el exito) y **Pergamino Blanco** (protege de destruccion). Si combinas dos libros del mismo encantamiento en el yunque o directamente sobre el objeto, el encantamiento sube de nivel.

---

## Sistema de Almas

Algunos encantamientos de rareza **Fabled** consumen **Almas** al activarse. Para usar este sistema:

1. Obtiene una **Runa del Alma** (`/ae giveitem`o eventos del servidor).
2. Arrastra la runa sobre el arma para activar el rastreo de almas.
3. Cada kill con esa arma acumula almas en ella.
4. Los encantamientos que consumen almas se activan automaticamente cuando tienes suficientes y se cumplen sus condiciones.

Los encantamientos soul son: **Nulify**, **Rush**, **Diploid** y **Multiplication**.

---

## Rarezas

Los encantamientos se dividen en 6 niveles de rareza, de menor a mayor poder:

| Rareza | Color del libro | Descripcion |
|--------|----------------|-------------|
| **Simple** | Gris claro | Encantamientos basicos de utilidad y combate menor |
| **Unico** | Verde | Efectos de debuffs y mejoras moderadas |
| **Elite** | Azul claro | Habilidades de combate especializadas |
| **Ultimate** | Lavanda/Morado claro | Encantamientos poderosos con efectos de area |
| **Legendario** | Dorado/Naranja | Habilidades raras con efectos muy fuertes |
| **Fabled** | Rosa/Coral | Los encantamientos mas poderosos del servidor |

---

## Comandos

| Comando | Descripcion |
|---------|-------------|
| `/enchanter` | Abre el menu del encantador (XP o dinero) |
| `/tinkerer` | Intercambia libros por polvo magico |
| `/alchemist` | Combina polvo de encantamiento |
| `/ae list` | Lista todos los encantamientos custom |
| `/ae info [nombre]` | Informacion detallada de un encantamiento |
| `/withdrawsouls` | Retira almas de un objeto |

---

## Lista de Encantamientos

Los simbolos de la columna "Aplica a" indican el tipo de objeto:
`Espadas` `Hachas` `Picos` `Palas` `Azadas` `Casco` `Pechera` `Pantalones` `Botas` `Armadura completa` `Arco` `Ballesta` `Tridente` `Cana de pescar` `Elitros`

---

### Simple

Encantamientos de rareza basica. Disponibles en la mesa de encantamiento (50% de probabilidad cuando activan los custom enchants).

| Encantamiento | Aplica a | Niv. max | Como funciona |
|---------------|----------|----------|---------------|
| **Strike** | Espadas, Arco, Ballesta, Tridente | 3 | Cada golpe o disparo tiene probabilidad (24-40%) de caer un rayo sobre el objetivo. Cooldown de 3-4 s. |
| **Aquatic** | Cascos | 1 | Proporciona respiracion acuatica permanente mientras llevas el casco puesto. Sin cooldown. |
| **Smelting** | Picos, Palas | 3 | Al minar, probabilidad (33/66/100%) de que el bloque se funda automaticamente, dando el drop procesado en lugar del raw. |
| **Experience** | Picos, Palas, Hachas | 5 | Al romper minerales (bloques con `ORE` en el nombre), probabilidad de obtener 2-5 XP adicionales directamente. |
| **Hasten** | Picos, Palas, Hachas | 3 | Probabilidad (15-45%) de ganar Prisa I, II o III temporalmente al romper bloques. Cooldown de 3 s. |
| **Rebreather** | Picos | 2 | Probabilidad (30/60%) de restaurar el nivel de aire al minar bajo el agua, evitando el ahogamiento. |
| **Glowing** | Cascos | 1 | Proporciona Vision Nocturna permanente mientras llevas el casco. |
| **Death Punch** | Espadas, Hachas | 5 | Al golpear un Zombie, probabilidad (16-80%) de infligir entre 10% y 40% de dano adicional. |
| **Bone Crusher** | Espadas, Hachas | 3 | Al golpear un Esqueleto, probabilidad (25-75%) de infligir entre 10% y 40% de dano adicional. |
| **Telepathy** | Picos, Palas, Hachas | 1 | Los drops de todos los bloques rotos van directamente a tu inventario en lugar de caer al suelo. |
| **Pies de Rana** | Botas | 2 | Proporciona Gracia del Delfin (velocidad en agua) de forma permanente. Nivel 2 da un nivel mas alto del efecto. |
| **Timbre de Vida** | Armadura | 2 | Al recibir dano en combate, probabilidad del 100% de obtener Absorcion I (100 o 200 ticks de duracion). Cooldown de 30 s. |
| **Pesca Ruidosa** | Cana de pescar | 2 | Al morder el anzuelo, probabilidad (30/60%) de obtener Suerte temporal y reproducir el sonido del delfin, facilitando la pesca. |
| **Brisa Ligera** | Botas | 2 | Proporciona Velocidad I o II de forma permanente mientras llevas las botas puestas. |
| **Brinco** | Cascos | 2 | Proporciona Salto (Jump Boost) I o II de forma permanente mientras llevas el casco. |
| **Lumbricida** | Palas | 2 | Al excavar, probabilidad pequena (2/5%) de recuperar Saturacion momentanea, evitando el hambre. |

---

### Unico

Encantamientos de segunda rareza. Disponibles en la mesa (40%) y en el Enchanter.

| Encantamiento | Aplica a | Niv. max | Como funciona |
|---------------|----------|----------|---------------|
| **Famine** | Espadas, Hachas | 4 | Al atacar, probabilidad (12-22%) de aplicar Hambre I o II al oponente durante 4-6 segundos. |
| **Berserk** | Espadas, Hachas | 5 | Al atacar, probabilidad (4-20%) de ganar Fuerza I o II pero tambien Fatiga Minera por unos segundos. Un encantamiento de alto riesgo/recompensa. |
| **Reflect** | Armadura | 5 | Al recibir dano, probabilidad (2-8%) de cancelar completamente el golpe y reflejar el 100% del dano al atacante. Cooldown de 5-20 s. |
| **Ward** | Armadura | 4 | Al recibir dano, probabilidad (4-10%) de cancelar el golpe completamente. Cooldown de 20 s. |
| **Ravenous** | Espadas, Hachas | 4 | Al golpear, probabilidad (14-26%) de recuperar 1-2 puntos de vida. Cooldown de 6 s. |
| **Slayer** | Espadas, Hachas | 4 | Al golpear mobs pasivos (no hostiles), probabilidad (25-100%) de infligir 10-40% de dano extra. |
| **Soulless** | Arco, Ballesta, Tridente | 4 | Al disparar a mobs hostiles, probabilidad (25-100%) de infligir 10-40% de dano extra. |
| **Virus** | Arco, Ballesta, Tridente | 4 | Al disparar, probabilidad (6-40%) de envenenar al objetivo. Nivel 3 aplica Veneno II. |
| **Devour** | Espadas, Hachas | 3 | Al matar un mob, probabilidad (10-35%) de recuperar 1 punto de hambre. |
| **Perish** | Arco, Ballesta, Tridente | 5 | Al disparar, probabilidad (9-21%) de aplicar Marchitamiento (Wither) al objetivo durante 3-5 segundos. |
| **Sangre Toxica** | Pechera | 3 | Al recibir dano, tu sangre envenena al atacante: nivel 1 envenena, nivel 2 envenena y marea, nivel 3 aplica veneno y nausea mas fuertes. |
| **Piel de Espinas** | Pechera | 2 | Al recibir dano, probabilidad (7-10%) de devolverle 1 punto de dano al atacante y aplicarle Lentitud brevemente. |
| **Toque Helado** | Espadas, Hachas | 3 | Al golpear, probabilidad (5-10%) de aplicar Fatiga Minera y Debilidad al objetivo durante 1.5-2.5 segundos. |
| **Rugido Protector** | Pechera | 2 | Al recibir dano de mobs, probabilidad (10-20%) de aplicar Debilidad al mob y reproducir el rugido del Ravager. |
| **Alarma de Enderman** | Cascos | 1 | Eres permanentemente invisible para los mobs mientras llevas el casco, hasta que los golpeas o interactuas con ellos. |

---

### Elite

Encantamientos de tercera rareza. Disponibles en la mesa (30%) y en el Enchanter.

| Encantamiento | Aplica a | Niv. max | Como funciona |
|---------------|----------|----------|---------------|
| **Impact** | Tridente | 4 | Al lanzar el tridente, probabilidad (5-14%) de duplicar el dano del golpe. Cooldown de 3-6 s. |
| **Ender Slayer** | Espadas, Hachas | 5 | Al golpear un Enderman o Dragon del End, probabilidad (16-41%) de infligir 10-40% de dano extra. |
| **Immolate** | Espadas, Hachas | 3 | Al golpear una Arana, probabilidad (25-75%) de infligir 10-40% de dano extra. |
| **Hook** | Cana de pescar | 3 | Al atrapar un pez, probabilidad (15-35%) de obtener XP adicional proporcional al nivel. Cooldown de 12 s. |
| **Snap** | Cana de pescar | 3 | Al atrapar a un jugador con la cana, lo atrae hacia ti con fuerza creciente (1-2 bloques). |
| **Reaper** | Hachas | 4 | Al golpear, probabilidad (8-14%) de aplicar Wither I y Ceguera al oponente durante 1.75-3 segundos. |
| **Nether Slayer** | Espadas, Hachas | 5 | Al golpear mobs del Nether (Blaze, Zombified Piglin, Ghast), probabilidad (16-41%) de infligir 10-40% de dano extra. |
| **Blind** | Espadas | 3 | Al golpear, probabilidad (17-33%) de aplicar Ceguera I/II/III al oponente durante 3-5 segundos. |
| **Frozen** | Armadura | 3 | Al recibir dano, probabilidad (19-26%) de aplicar Lentitud I/II/III al atacante durante 2-3 segundos. |
| **Poison** | Espadas, Hachas | 3 | Al golpear, probabilidad (6-35%) de aplicar Veneno I o II al objetivo. |
| **Poisoned** | Armadura | 4 | Al recibir cualquier dano, probabilidad (8-23%) de envenenar al atacante. |
| **Reforged** | Espadas, Hachas, Picos, Palas | 10 | Con cada uso del objeto, probabilidad (10-100%) de recuperar 1 punto de durabilidad. El nivel 10 lo repara siempre. |
| **Snare** | Arco, Ballesta | 4 | Al disparar, probabilidad (12-29%) de aplicar Lentitud y Fatiga Minera al objetivo. |
| **Springs** | Botas | 3 | Proporciona Salto (Jump Boost) I, II o III de forma permanente. |
| **Voodoo** | Armadura | 6 | Al recibir dano, probabilidad (5-21%) de aplicar Debilidad al atacante durante 3-6 segundos. |
| **Wither** | Armadura | 5 | Al recibir dano, probabilidad (9-21%) de aplicar Marchitamiento al atacante durante 3-7 segundos. |
| **Infernal** | Espadas, Hachas | 3 | Al golpear, probabilidad (15-50%) de prender fuego al objetivo durante 2-6 segundos con particulas de fuego. |
| **Extinguish** | Pantalones | 3 | Al recibir dano mientras estas en llamas, probabilidad (20-80%) de apagarte automaticamente. |
| **Vampire** | Espadas | 3 | Al golpear, probabilidad (7-15%) de recuperar 1-6 puntos de vida 2 segundos despues del golpe. |
| **Greatsword** | Espadas | 5 | Al golpear a un jugador que sostiene un arco, probabilidad (15-55%) de infligir 45-205% de dano adicional. |
| **Bowmaster** | Arco, Ballesta, Tridente | 5 | Al disparar a un jugador que sostiene una espada, probabilidad (15-55%) de infligir 45-205% de dano adicional. |
| **Marksman** | Ballesta | 4 | Al disparar con ballesta, probabilidad (13-32%) de infligir 50-150% de dano adicional. |
| **Poseidon** | Tridente | 4 | Al lanzar el tridente, probabilidad (13-32%) de infligir 50-150% de dano adicional. |
| **Replenish** | Picos | 3 | Al minar, probabilidad (30-60%) de recuperar 1-3 puntos de hambre. |
| **Smoke Bomb** | Cascos | 8 | Cuando tu vida esta por debajo de 2 corazones (o 2.5 con niveles altos), probabilidad de crear una nube de humo y cegar al atacante. |
| **Trickster** | Armadura | 8 | Al recibir dano, probabilidad (8-51%) de teletransportarte detras del oponente. Cooldown de 5 s. |
| **Critical** | Espadas | 3 | Al asestar un golpe critico, probabilidad (7-12%) de infligir 10-20% de dano extra. |
| **Blunt Force** | Hachas | 4 | Al golpear, probabilidad (5-12%) de infligirte a ti mismo 1-4 puntos de dano a cambio de un golpe devastador. |
| **Suspend** | Espadas | 3 | Al golpear mobs, probabilidad (40-100%) de que el mob no salga disparado por el knockback. Util para grinders. |
| **Nightwalker** | Espadas | 3 | Durante la noche, al golpear mobs, probabilidad (40-100%) de aplicarles Lentitud extrema durante 20 segundos. |
| **Magnet** | Espadas | 3 | Al golpear a un jugador, probabilidad (30-100%) de jalarlo hacia ti 1-3 bloques. |
| **Wolves** | Pechera | 10 | Al recibir dano, probabilidad de invocar 1-3 lobos aliados que atacan a tu atacante durante 8 segundos. |
| **Escapist** | Botas | 1 | Cuando tienes menos de 2.5 corazones, probabilidad del 30% de ganar Velocidad IV durante 0.25 segundos para escapar. |
| **Geologo Veloz** | Picos | 3 | Al picar un mineral (ore), probabilidad (7-20%) de ganar Velocidad I o II momentaneamente. Util para explorar cuevas. |
| **Disparo de Ghast** | Arco, Ballesta | 3 | Al disparar, probabilidad (15-35%) de causar dano extra, aplicar Nausea y reproducir el grito del Ghast. |
| **Tambores de Guerra** | Hachas | 3 | Al golpear, probabilidad (8-16%) de ganar Fuerza I o II temporalmente con el sonido de un yunque. |
| **Gravedad Cero** | Arco, Ballesta | 4 | Al disparar, probabilidad (4-10%) de aplicar Levitacion al objetivo durante 1-2.5 segundos. |
| **Impulso Sonico** | Arco, Ballesta | 3 | Al disparar, probabilidad (10-20%) de ganar Velocidad I o II brevemente. |
| **Grito de Guerra** | Hachas | 3 | Al golpear, probabilidad (4-8%) de ganar Fuerza para ti y aplicar Nausea al objetivo simultaneamente. |

---

### Ultimate

Encantamientos de cuarta rareza. Disponibles en la mesa (20%) y en el Enchanter.

| Encantamiento | Aplica a | Niv. max | Como funciona |
|---------------|----------|----------|---------------|
| **Harvest** | Azadas | 9 | Al cosechar, probabilidad (13-100%) de cosechar todos los cultivos en un area 3x3 de una sola vez. Funciona con trigo, zanahorias, papas, remolacha, cacao, verruga del Nether y mas. |
| **Auto Reel** | Cana de pescar | 4 | Al morder el anzuelo, probabilidad (25-100%) de recoger automaticamente la cana sin necesidad de hacer clic. |
| **Jelly Legs** | Botas | 3 | Al sufrir dano por caida, probabilidad (40-100%) de cancelarlo por completo. El nivel 3 es 100% de cancelacion. |
| **Lucky** | Cana de pescar | 3 | Al hacer clic derecho con la cana, probabilidad (75-95%) de ganar Suerte I/II/III durante 50 segundos para mejorar los drops de pesca. |
| **Permafrost** | Espadas | 5 | Al golpear, probabilidad (15-25%) de aplicar Lentitud y hacer sangrar al oponente durante 3 ondas de dano retardado. |
| **Timber** | Hachas | 3 | Al golpear un tronco, probabilidad (15-55%) de talar el arbol entero de un solo golpe. |
| **Arrow Deflect** | Armadura | 4 | Al recibir dano de proyectiles, probabilidad (15-45%) de cancelarlo completamente. Cooldown de 6 s. |
| **Arrow Break** | Hachas | 6 | Al recibir una flecha mientras sostienes el hacha, probabilidad (15-65%) de que rebote sin causarte dano. |
| **Exalted** | Espadas | 4 | Al golpear, probabilidad (12-36%) de curar todos tus efectos negativos (Lentitud, Ceguera, Veneno, Wither, Hambre, Debilidad, Fatiga). |
| **Dodge** | Armadura | 5 | Al recibir dano fisico, probabilidad (8-20%) de esquivarlo completamente. Agacharte (shift) aumenta la probabilidad en 7%. Cooldown de 20 s. |
| **Ice Aspect** | Espadas | 3 | Al golpear, probabilidad (15-31%) de aplicar Lentitud II al objetivo durante 5 segundos. |
| **Reinforced** | Elitros | 4 | Al recibir dano con los elitros equipados, probabilidad (15-75%) de reducir el dano en 15-45%. |
| **Implants** | Cascos | 3 | Cada 5 segundos, probabilidad (30-70%) de recuperar automaticamente 1 punto de hambre. |
| **Obsidianshield** | Armadura | 1 | Proporciona Resistencia al Fuego permanente mientras tienes cualquier pieza de armadura encantada equipada. |
| **Piercing** | Arco, Ballesta | 5 | Al disparar, probabilidad (13-37%) de infligir 50-150% de dano extra con cada flecha. |
| **Archer** | Arco | 4 | Al disparar con arco (no ballesta), probabilidad (13-32%) de infligir 50-150% de dano extra. |
| **Safeguard** | Armadura | 2 | Al recibir dano, probabilidad (5-9%) de obtener Resistencia I o II durante 3 segundos. |
| **Confuse** | Espadas | 4 | Al golpear, probabilidad (12-18%) de aplicar Nausea I/II/III/IV durante 3 segundos. |
| **Disintegrate** | Espadas | 4 | Al golpear, probabilidad (12-46%) de reducir la durabilidad de toda la armadura del enemigo en 2 puntos. |
| **Shatter** | Hachas | 4 | Al golpear, probabilidad (12-46%) de reducir la durabilidad de toda la armadura del enemigo en 2 puntos. |
| **Heavy** | Armadura | 5 | Al recibir un disparo de arco, probabilidad (4-21%) de reducir el dano en 2-10%. |
| **Tank** | Armadura | 4 | Al recibir un golpe de hacha, probabilidad (5-16%) de reducir el dano en 2-8%. |
| **Swordsman** | Armadura | 5 | Al recibir dano mientras sostienes una espada, probabilidad (4-21%) de reducir el dano en 1-22%. |
| **Cleave** | Hachas | 7 | Al golpear a un jugador, probabilidad (4-15%) de dano en area que alcanza a jugadores en radio 2-7. El dano por golpe es 1-3 puntos. |
| **Ambit** | Espadas, Hachas | 7 | Al golpear un mob, probabilidad (4-15%) de dano en area que alcanza mobs en radio 2-7. |
| **Guardians** | Armadura | 10 | Al recibir dano, probabilidad (6-24%) de invocar 1-4 Golems de Hierro aliados durante 8 segundos para defenderte. |
| **Longbow** | Arco, Ballesta | 4 | Al disparar a un jugador que sostiene un arco, probabilidad (12-33%) de infligir 25-100% de dano extra. |
| **Netherling** | Espadas | 3 | Al matar mobs mientras estas en el Nether, probabilidad (25-75%) de infligir 50% de dano extra. |
| **Endmaster** | Espadas | 3 | Al matar mobs mientras estas en el End, probabilidad (25-75%) de infligir 50% de dano extra. |
| **Creeper Armor** | Armadura | 3 | Al recibir dano de una explosion, probabilidad (25-75%) de cancelarlo por completo. El nivel 3 ademas te cura 1-2 puntos de vida. |
| **Spirits** | Armadura | 10 | Al recibir dano, probabilidad (2-27%) de invocar 3-5 Blazes aliados durante 8 segundos. Cooldown de 8 s. |
| **Bleed** | Hachas | 6 | Al golpear, probabilidad (8-60%) de aplicar Lentitud y causar 3 ondas de sangrado (1-3 dano cada una con 1 segundo entre ellas). |
| **Aegis** | Botas | 3 | Al sufrir dano por caida, probabilidad (40-70%) de ganar Velocidad I/II/III durante 3 segundos. |
| **Night Owl** | Espadas | 3 | Durante la noche, al golpear mobs, probabilidad (40-80%) de infligir 25-45% de dano extra. |
| **Fuddle** | Espadas | 3 | Al golpear a un jugador, probabilidad (5-9%) de reorganizar aleatoriamente su barra de acceso rapido (hotbar). Cooldown de 15 s. |
| **Mjolnir** | Hachas | 4 | Al golpear, probabilidad (6-12%) de desencadenar 3 rayos consecutivos que danan la armadura del enemigo y te curan. Cooldown de 30 s. |
| **Striker** | Arco | 3 | Al disparar, probabilidad (15-22%) de invocar una lluvia de flechas sobre el objetivo. |
| **Sniper** | Arco | 5 | Al disparar a la cabeza, probabilidad (15-35%) de duplicar el dano del disparo. |
| **Petrify** | Pantalones | 3 | Al recibir dano, probabilidad (5-11%) de petrificar al atacante con Lentitud extrema durante 5 segundos. |
| **Flap** | Elitros | 3 | Al volar con elitros, probabilidad de reproducir el sonido del Dragon del End. Efecto estetico. |
| **Beaconer** | Tridente | 3 | Al hacer clic derecho con el tridente, probabilidad de reproducir el sonido del faro. Efecto estetico. |
| **Immolation** | Espadas | 3 | Al golpear mobs, probabilidad (10-16%) de prender fuego a todos los mobs en radio 2-6. |
| **Erupcion** | Picos | 3 | Al minar, probabilidad muy baja (1-3%) de crear una erupcion que destruye bloques en radio 3-5. Cooldown de 10-20 s. |
| **Tala Epica** | Hachas | 3 | Al cortar arboles, probabilidad (7-17%) de ganar Prisa y Velocidad momentaneos. |
| **Ceguera Nocturna** | Espadas | 3 | Al golpear, probabilidad (2-7%) de aplicar Ceguera y Marchitamiento al oponente durante 1.5-2.5 segundos. |
| **Taladro Ensordecedor** | Picos | 3 | Al minar, probabilidad (4-10%) de ganar Prisa II/III/IV durante 3-5 segundos con sonido de piston. |
| **Parada Relampago** | Espadas | 3 | Al recibir dano, probabilidad (5-15%) de curarte 1-3 puntos de vida, ralentizar al atacante y reproducir un trueno. |
| **Despegue** | Elitros | 2 | Al hacer clic derecho con los elitros, lanzate al aire con impulso de 15-25 bloques sin necesidad de cohetes. Cooldown de 15-20 s. |

---

### Legendario

Encantamientos de quinta rareza. Disponibles en la mesa (10%) y en el Enchanter.

| Encantamiento | Aplica a | Niv. max | Como funciona |
|---------------|----------|----------|---------------|
| **Twinge** | Tridente | 4 | Al golpear en melee con el tridente, probabilidad (5-14%) de aplicar Lentitud y causar 3 ondas de sangrado durante 2 segundos. |
| **Beastslayer** | Espadas, Hachas | 4 | Al golpear mobs hostiles, probabilidad (25-100%) de infligir 10-40% de dano extra. |
| **Bait** | Cana de pescar | 3 | Al pescar, probabilidad (15-26%) de duplicar los drops obtenidos. Cooldown de 10-20 s. |
| **Hardened** | Armadura | 3 | Al recibir dano de jugadores, probabilidad (25-45%) de recuperar 1-2 puntos de durabilidad en la pieza de armadura golpeada. |
| **Patch** | Armadura | 3 | Al recibir dano de mobs, probabilidad (25-45%) de recuperar 1-2 puntos de durabilidad en la pieza de armadura golpeada. |
| **Turmoil** | Armadura | 3 | Al recibir dano, probabilidad (10-18%) de desactivar los Guardians, Spirits y otros encantamientos de invocacion del atacante durante 4 segundos. |
| **Lava Walker** | Botas | 1 | Caminar sobre lava la solidifica temporalmente bajo tus pies, permitiendo cruzarla. |
| **Water Walker** | Botas | 1 | Caminar sobre agua la solidifica temporalmente bajo tus pies. |
| **Aqua** | Botas | 4 | Mientras estes bajo el agua, probabilidad (8-23%) de que tus golpes dupliquen el dano. |
| **Judgement** | Elitros | 5 | Al recibir dano con elitros, probabilidad (6-16%) de envenenar al atacante y ganar Regeneracion I o II. |
| **Divert** | Armadura | 5 | Al recibir dano, probabilidad (6-16%) de envenenar al atacante y ganar Regeneracion I o II simultaneamente. |
| **Unholy** | Armadura | 5 | Al recibir dano de jugadores, probabilidad (2-10%) de aplicar Wither I y Debilidad al atacante durante 3-5 segundos. Cooldown de 40 s. |
| **Chaos** | Tridente | 5 | Al lanzar el tridente, probabilidad (2-10%) de aplicar Wither I y Debilidad al objetivo. Cooldown de 40 s. |
| **Convulse** | Botas | 6 | Al recibir dano, probabilidad (8-18%) de lanzar al atacante hacia arriba con fuerza 5-10. |
| **Barbarian** | Hachas | 4 | Al golpear con hacha en mano, probabilidad (8-25%) de infligir 25-100% de dano adicional. |
| **Lucid** | Armadura | 3 | Al recibir dano, probabilidad (22-42%) de curar la Ceguera y ganar Vision Nocturna durante 2-4 segundos. |
| **Double Strike** | Espadas | 3 | Al golpear, probabilidad (8-19%) de repetir el mismo golpe 1 segundo despues. |
| **Gears** | Botas | 3 | Proporciona Velocidad I, II o III de forma permanente mientras llevas las botas puestas. |
| **Inflame** | Hachas | 3 | Al golpear, probabilidad (10-16%) de prender fuego a todos los jugadores/entidades en radio 2-6. |
| **Inquisitive** | Espadas | 4 | Al matar un mob, probabilidad (30-45%) de multiplicar la XP que suelta en 1.25x, 1.5x, 1.75x o 2x segun el nivel. |
| **Lifesteal** | Espadas | 5 | Al golpear, probabilidad (9-25%) de robar 1-5 puntos de vida al objetivo y curarte. Cooldown de 15 s. |
| **Overload** | Armadura | 3 | Desbloquea 2, 4 o 6 puntos de vida adicionales (1-3 corazones extra) permanentemente. |
| **Armored** | Armadura | 4 | Al recibir golpes de espadas enemigas, probabilidad (6-20%) de reducir el dano en 2-8%. Cooldown de 8 s. |
| **Blacksmith** | Hachas | 5 | Al golpear, probabilidad (9-39%) de reparar el hacha 3-4 puntos de durabilidad pero a cambio de reducir el dano a la mitad en ese golpe. |
| **Deadshot** | Tridente | 5 | Al lanzar el tridente y golpear en la cabeza, probabilidad (15-35%) de duplicar el dano del impacto. |
| **Rocket Launch** | Arco | 3 | Al disparar, probabilidad del 12% de lanzar al objetivo hacia arriba con fuerza 10-20. |
| **Strife** | Tridente | 3 | Al golpear en melee con el tridente, probabilidad (5-15%) de infligir 15-30% de dano extra. |
| **Espejismo** | Pantalones | 3 | Al recibir dano, probabilidad (2-5%) de esquivarlo completamente, volverse invisible brevemente y cegar al atacante. Cooldown de 20-30 s. |
| **Fortaleza** | Armadura | 3 | Al recibir dano, probabilidad (2-5%) de ganar Resistencia II/III pero tambien Lentitud extrema (modo torreta). Cooldown de 35-45 s. |
| **Caos** | Arco, Ballesta | 4 | Al disparar, probabilidad (5-12%) de hacer caer un rayo e incendiar al objetivo. Cooldown de 20 s. |
| **Snag** | Espadas | 3 | Al golpear, probabilidad (10-100%) de eliminar el efecto de Velocidad del oponente. No disponible en Enchanter. |
| **Coro del Vacio** | Arco, Ballesta | 3 | Al disparar, probabilidad (5-11%) de aplicar Levitacion y Ceguera al objetivo con sonido de Shulker. |
| **Aura Cristalina** | Pantalones | 3 | Al recibir dano, probabilidad (5-11%) de ganar Resistencia II/III/IV durante 5-7 segundos con sonido de cristal. |
| **Talisman de Fuego** | Herramientas y Armadura | 1 | Proporciona inmunidad total al fuego (Resistencia al Fuego) y Vision Nocturna permanentes. Aplica a armadura y picos. |

---

### Fabled

Los encantamientos mas raros y poderosos. **No disponibles en la mesa de encantamiento.** Solo se obtienen en el Enchanter, como loot de eventos o de otros jugadores.

| Encantamiento | Aplica a | Niv. max | Como funciona |
|---------------|----------|----------|---------------|
| **Haste** | Picos, Palas, Hachas | 3 | Proporciona Prisa I, II o III de forma permanente mientras sostienes la herramienta. Nivel 3 es Prisa III constante. |
| **Restore** | Picos, Palas, Hachas | 4 | Cuando la herramienta esta a punto de romperse, probabilidad (40-100%) de que se repare automaticamente a la mitad de su durabilidad maxima, eliminandose el encantamiento al activarse. |
| **Hero** | Armadura | 1 | Proporciona el efecto Heroe de la Aldea permanentemente mientras llevas alguna pieza de armadura encantada. |
| **Neutralize** | Arco, Ballesta | 2 | Al disparar a un jugador, probabilidad (5-10%) de desarmarle, haciendo que suelte el objeto que sostiene. Cooldown de 20 s. |
| **Scare** | Espadas, Hachas | 5 | Al golpear, probabilidad (1.8-6%) de reemplazar el casco del oponente con una calabaza durante 2-4 segundos, cegandole parcialmente. |
| **Dominio Temporal** | Espadas, Hachas | 4 | Al golpear, probabilidad (2-7%) de aplicar Lentitud y Fatiga al oponente mientras te dan Velocidad y Prisa a ti. Cooldown de 45 s. |
| **Inmortalidad** | Pechera | 3 | Cuando tu vida baja de 4 corazones, el encantamiento se activa con 100% de probabilidad, curando 1-3 corazones y dandote Regeneracion durante 2.5-4 segundos. Cooldown de 240 s (4 minutos). |
| **Paralisis Absoluta** | Espadas | 4 | Al golpear, probabilidad (3-12%) de aplicar Lentitud extrema, Salto negativo y Debilidad muy alta al objetivo durante 2-5 segundos, inmovilizandole completamente. |
| **Bendicion de Merlin** | Picos, Palas, Hachas | 2 | Al minar, probabilidad muy baja (1-2%) de curar todos tus efectos negativos, restaurar 10 corazones completos y ganar Suerte durante un tiempo. Cooldown de 3-4 minutos. |
| **Despertar de Wither** | Espadas, Hachas | 3 | Al golpear con critico, probabilidad (4-10%) de aplicar Wither II, Lentitud extrema y Fatiga al oponente durante 3-5 segundos, mientras te curas 2-6 corazones. Sonido del Wither al activarse. |
| **Pulso de Dragon** | Armadura, Elitros | 3 | Cuando tu vida baja de 3 corazones, se activa con 100% de probabilidad para cancelar el golpe mortal y lanzarte al aire con impulso 20-40. Cooldown de 160-200 s. |
| **Destello Oscuro** | Espadas, Hachas | 3 | Al golpear, probabilidad (3-8%) de duplicar el dano del golpe con un efecto de trueno. Cooldown de 6-8 s. |
| **Infinito** | Armadura | 3 | Al recibir dano, probabilidad (2-6%) de cancelar el golpe completamente con mensaje al jugador. Cooldown de 8-10 s. |
| **Desmantelar** | Espadas | 4 | Al golpear, probabilidad (5-15%) de aplicar Lentitud y causar 3 ondas de hemorragia retardada de 1-3 dano cada una. |
| **Discurso Maldito** | Arco, Ballesta, Tridente | 2 | Al disparar, probabilidad (8-14%) de paralizar al objetivo con Lentitud III o IV y Ceguera durante 4-5 segundos, con el sonido del Guardian Anciano. |
| **Tecnica Inversa** | Armadura | 4 | Al recibir dano cuando tienes menos de 5 corazones, probabilidad (8-20%) de curarte 2-5 corazones instantaneamente con particulas de corazon. |
| **Hueco Purpura** | Arco, Ballesta, Tridente | 3 | Al disparar, probabilidad (3-7%) de duplicar el dano del proyectil y ademas caer un rayo sobre el objetivo. |
| **Expansion de Dominio** | Espadas, Hachas | 3 | Al golpear, probabilidad (5-11%) de aplicar Ceguera y Lentitud al objetivo durante 5-7 segundos con un mensaje intimidante. |
| **Golpe Divergente** | Espadas, Hachas | 4 | Al golpear, probabilidad (10-25%) de infligir 2-5 puntos de dano adicional medio segundo despues del golpe inicial. |
| **Sombra Quimera** | Armadura | 3 | Cuando tu vida baja de 3 corazones, con 100% de probabilidad cancela el golpe mortal, te vuelve invisible y te da Velocidad I o II durante 8 segundos. Cooldown de 60-120 s. |
| **Exorcista** | Espadas | 4 | Al golpear Zombies, Esqueletos, Wither Skeletons o Phantoms, probabilidad (30-60%) de infligir 25-60% de dano extra. |
| **Getsuga Tensho** | Espadas, Hachas | 4 | Al golpear, probabilidad (5-12%) de infligir 3-7 dano extra, aplicar Lentitud y caer un rayo, con el mensaje tematico de Bleach. Cooldown de 14-20 s. |
| **Bankai** | Espadas, Hachas | 3 | Al golpear, probabilidad (2-5%) de duplicar el dano, ganarte Velocidad II y Fuerza I durante 5-7 segundos. El nivel 3 ademas cae un rayo. Cooldown de 30-50 s. |
| **Flash Paso** | Botas, Pantalones | 3 | Al recibir dano, probabilidad (6-12%) de teletransportarte detras del atacante con Velocidad y cancelar el golpe en nivel 3. |
| **Presion del Reiatsu** | Pechera | 4 | Al recibir dano, probabilidad (12-25%) de aplicar Lentitud, Debilidad y (en nivel 3-4) Nausea al atacante durante 4-7 segundos. |
| **Lluvia Negra** | Espadas, Hachas | 4 | Al golpear, probabilidad (11-23%) de ganar 15-40% de dano extra acumulativo con particulas criticas. El nivel 4 muestra el mensaje de Kenpachi. |
| **Senescencia** | Armadura | 4 | Al recibir dano, probabilidad (5-12%) de robar 2-5 puntos de vida al atacante y curarte. Niveles altos ademas debilitan al atacante. Cooldown de 18-30 s. |
| **Terraformer** | Picos | 1 | Mina permanentemente en un area de 3x3 en todo momento. No requiere activacion. No se puede obtener del Enchanter. |
| **Soulbound** | Herramientas, Espadas, Arco, Ballesta | 3 | Al morir, probabilidad (4-8%) de conservar el objeto en lugar de soltarlo al suelo. Cooldown de 300 s entre activaciones. |

---

### Encantamientos de Almas (Soul Enchantments)

Estos encantamientos de rareza **Fabled** requieren el **Sistema de Almas** activo en el objeto. Consumen almas acumuladas para activarse.

Para activar el rastreo de almas, aplica una **Runa del Alma** al arma o herramienta arrastandola sobre el objeto.

| Encantamiento | Aplica a | Niv. max | Costo/activacion | Como funciona |
|---------------|----------|----------|------------------|---------------|
| **Nulify** | Espadas, Hachas | 4 | 40 almas | Al golpear, probabilidad (8-14%) de duplicar el dano y aplicar Ceguera al objetivo. Requiere minimo 40 almas acumuladas. |
| **Rush** | Elitros | 3 | 10 almas | Al volar con elitros, probabilidad (15-26%) de ganar Velocidad III/IV/V durante 3 segundos. |
| **Diploid** | Espadas | 5 | 5 almas | Al matar un mob, probabilidad (15-30%) de duplicar sus drops. |
| **Multiplication** | Picos | 5 | 5 almas | Al minar minerales (carbon, cobre, hierro, oro, lapislazuli, redstone, diamante, esmeralda, cuarzo, oro del Nether, debris antiguo y variantes de pizarra), probabilidad (15-30%) de duplicar el drop. |

---

## Items Especiales del Plugin

Ademas de los encantamientos, el plugin incluye items que modifican el sistema:

| Item | Funcion |
|------|---------|
| **Libro de Encantamiento** | Libro con un encantamiento especifico para aplicar a un objeto |
| **Libro Aleatorio** | Se limpia al hacer clic derecho para revelar un encantamiento aleatorio del grupo indicado |
| **Polvo Magico** | Aumenta la tasa de exito al aplicar libros |
| **Polvo Secreto** | Aumenta aun mas la tasa de exito |
| **Pergamino Blanco** | Protege el objeto de ser destruido si un encantamiento falla |
| **Pergamino Negro** | Elimina un encantamiento aleatorio del objeto |
| **Aumentador de Ranura** | Agrega una ranura de encantamiento adicional al objeto (hasta maximo de 20) |
| **Runa del Alma** | Activa el rastreo de almas en un arma o herramienta |
| **Orbe de Transmog** | Cambia el aspecto visual del objeto sin alterar sus encantamientos |
| **Orbe de Arma/Armadura/Herramienta** | Items especiales de administracion |
