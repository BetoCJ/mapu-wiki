# ✨ Encantamientos Personalizados

{% hint style="info" %}
🗓️ **Disponible desde el 7 de noviembre** (semana 3, sistema renovado). → [Hoja de ruta](hoja-de-ruta.md)
{% endhint %}

Mapucraft usa un sistema de encantamientos completamente personalizado con **221 encantamientos** adicionales a los vanilla. Todos funcionan con el mismo equipo de siempre y tienen libros con **texturas personalizadas** segun su rareza.

{% hint style="success" %}
🆕 **Temporada 2:** 9 encantamientos nuevos (Mawida, Rayen, Lawen, Weichafe, Kintu, Perforante, Raíz, Ruka y Lafken), Gears pasa a 2 niveles y se rebalancearon varias habilidades. La lista de abajo está siempre al día.
{% endhint %}

---

## 🔍 Como obtenerlos

### 🪄 Enchanter (`/enchanter`)

El metodo principal. Abre el menu del encantador y compra libros de encantamiento gastando **experiencia** o **dinero**.

![](<../.gitbook/assets/ae_enchanter.png>)

El menu muestra los **8 tipos de libros** disponibles segun su rareza: Simple, Unico, Elite, Ultimate, Legendario, Fabled, y libros especiales de Arma, Armadura, Herramienta y Aleatorio. Al hacer clic en uno se abre una confirmacion de compra antes de efectuar la transaccion. Los botones del fondo permiten filtrar por categoria, resetear filtros o cerrar el menu.

### 📖 Mesa de Encantamiento

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

Ademas, hay un **3% de probabilidad separado** de que la mesa te de directamente un **libro de encantamiento personalizado** (en lugar de encantarlo en el objeto). El nivel de encantamiento de la mesa determina la rareza del libro:

| Nivel de mesa | Rarezas posibles del libro |
|--------------|---------------------------|
| Nivel bajo | Simple, Unico |
| Nivel medio | Elite, Ultimate |
| Nivel alto | Legendario (los Fabled ya no salen de la mesa) |

### 🔧 Tinkerer (`/tinkerer`)

Intercambia libros de encantamiento que no quieras por **Gemas de Suerte**. Util para deshacerse de encantamientos duplicados o de rarezas bajas.

![](<../.gitbook/assets/ae_tinkerer.png>)

El menu tiene dos columnas: **INPUT** (izquierda) donde arrastras los libros que quieres cambiar, y **RESULT** (derecha) donde aparecen las Gemas de Suerte obtenidas. Puedes procesar varios libros a la vez en un solo intercambio.

### 🧪 Alchemist (`/alchemist`)

Combina Gemas de Suerte para obtener **Paquetes Arcanos**. Un Paquete Arcano es un envoltorio misterioso que al abrirse (clic derecho) puede contener una Gema de Suerte, aunque el resultado no esta garantizado.

![](<../.gitbook/assets/ae_alchemist.png>)

El menu tiene un slot central donde colocas las Gemas de Suerte. Las flechas indican la conversion: varias Gemas de Suerte se combinan en un Paquete Arcano.

### 📚 Diccionario de Encantamientos (`/enchantdex`)

Consulta todos los encantamientos del servidor directamente en el juego sin salir.

![](<../.gitbook/assets/ae_enchantdex.png>)

Al abrir el diccionario aparece una barra de categorias para filtrar por tipo. Al seleccionar una categoria se muestra la **lista de encantamientos** con paginacion:

![](<../.gitbook/assets/ae_enchantdex_list.png>)

Al hacer clic en cualquier encantamiento de la lista se abre su **ficha de detalle** con descripcion, niveles, items compatibles y como conseguirlo:

![](<../.gitbook/assets/ae_enchantdex_detail.png>)

### 🔨 Auction House (`/ah`)

Otros jugadores pueden publicar libros de encantamiento a la venta. Es una fuente util para conseguir libros raros de Legendario o Fabled sin depender del Enchanter.

---

## 🧷 Sistema de Ranuras (Slots)

Cada objeto tiene un numero limitado de **ranuras de encantamiento**:

- **Maximo base:** 9 ranuras
- **Maximo con mejoras:** 13 ranuras (+4 con Libro Universal o Tomos)

Las ranuras se pueden aumentar usando:

- **Libro Universal** — agrega +1 ranura al objeto (no tiene tasa de fallo)
- **Tomo de Armas / Tomo de Armadura / Tomo de Herramientas** — agrega varias ranuras a la vez segun el tipo de objeto, pero tiene una **Tasa de Exito** (puede fallar sin romper el objeto)

Agregar encantamientos consume ranuras segun el grupo del encantamiento. Las ranuras no se muestran en el lore del objeto por defecto.

---

## 🧪 Sistema de Aplicacion

Para aplicar un encantamiento, **arrastra el libro encima del objeto** en el inventario. Cada libro tiene dos metricas:

- **Tasa de exito:** Probabilidad de que el encantamiento se aplique correctamente.
- **Tasa de destruccion:** Probabilidad de que el objeto sea destruido si el encantamiento falla.

Puedes modificar estas tasas antes de aplicar el libro:

| Item | Como se usa | Efecto |
|------|-------------|--------|
| **Gema de Suerte** | Arrastrala sobre el **libro** antes de aplicarlo | Reduce la Tasa de Destruccion del libro en un porcentaje segun su rareza |
| **Runa de la Proteccion** | Arrastrala sobre el **objeto** antes de encantar | Protege el objeto de ser destruido si el encantamiento falla |
| **Paquete Arcano** | Abrir hace clic derecho | Puede contener una Gema de Suerte aleatoria segun la suerte |

**Subir de nivel un encantamiento:** combina dos libros del mismo encantamiento en el yunque, o arrastra directamente el libro sobre el objeto que ya lo tiene. Los objetos nunca se destruyen al combinar (solo podria eliminarse la proteccion de la Runa si hubiera fallo).

> Los items con la etiqueta **No Modificable** en su descripcion no pueden recibir encantamientos personalizados.

---

## 👻 Sistema de Almas

Algunos encantamientos de rareza **Fabled** consumen **Almas** al activarse. Para usar este sistema:

1. Obtiene una **Runa del Alma** (eventos del servidor o el Enchanter).
2. Arrastra la runa sobre el arma para activar el rastreo de almas.
3. Cada kill con esa arma acumula almas en ella.
4. Los encantamientos que consumen almas se activan automaticamente cuando tienes suficientes y se cumplen sus condiciones.

Los encantamientos que **gastan** almas son **Nulify** (40), **Rush** (10) y **Multiplication** (8 por activacion). Para alimentarlos existen los que **generan** almas: **Spiritmaster**, **Axe of Spirits**, **Soulgrind** y **Soulminer** (este solo genera almas al minar menas). Cada uno aparece marcado con 👻 en la lista de abajo.

---

## 💎 Rarezas

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

## 📜 Comandos

| Comando | Descripcion |
|---------|-------------|
| `/enchanter` | Abre el menu del encantador (XP o dinero) |
| `/tinkerer` | Intercambia libros por Gemas de Suerte |
| `/alchemist` | Combina Gemas de Suerte para obtener Paquetes Arcanos |
| `/enchantdex` | Abre el diccionario de encantamientos en el juego |
| `/ae list` | Lista todos los encantamientos custom por consola/chat |
| `/ae info [nombre]` | Informacion detallada de un encantamiento por consola/chat |
| `/withdrawsouls` | Retira almas acumuladas de un objeto |
| `/apply` | Reactiva los efectos de la armadura que llevas puesta (util si un efecto permanente deja de funcionar) |

---

## 📖 Lista de Encantamientos

Aplicar un encantamiento ocupa una ranura. Los símbolos de «Aplica a» indican qué objeto lo admite; **Maza** y **Lanzas** son las armas de los encantamientos temáticos mapuche.

<!-- AUTO:inicio encantamientos -->
Hay **221 encantamientos personalizados** en total. Esta lista se genera sola desde la configuración real del servidor, así que siempre está al día. **Prob.** es la probabilidad de activarse (mínimo–máximo según el nivel), **Espera** el enfriamiento en segundos y 🆕 marca los nuevos de la temporada 2.

| Rareza | Encantamientos |
|---|---:|
| ⚪ Simple | 19 |
| 🟢 Único | 23 |
| 🔵 Elite | 46 |
| 🟣 Ultimate | 52 |
| 🟡 Legendario | 42 |
| 🔴 Fabled | 39 |

### ⚪ Simple

Básicos de utilidad y combate menor.

| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |
|---|---|---:|---:|---:|---|
| **%group-color%Antü** | Espadas | 2 | 100% | — | La energía solar otorga velocidad de movimiento mientras empuñas la espada. |
| **%group-color%Aquatic** | Cascos | 1 | 100% | — | Permite respirar bajo el agua |
| **%group-color%Bone Crusher** | Espadas, Hachas | 3 | 25–75% | 1–2 s | Aumenta el daño infligido a esqueletos |
| **%group-color%Brinco** | Cascos | 2 | 100% | — | Otorga salto potenciado permanente. |
| **%group-color%Brisa Ligera** | Botas | 2 | 100% | — | Flotas suavemente como si una brisa te elevara, amortiguando las caídas permanentemente. |
| **%group-color%Death Punch** | Espadas, Hachas | 5 | 16–80% | 0–2 s | Aumenta el daño infligido a zombies. |
| **%group-color%Experience** | Picos, Palas, Hachas | 5 | 15–75% | 2 s | Posibilidad de obtener más experiencia de los minerales |
| **%group-color%Glowing** | Cascos | 1 | 100% | — | Proporciona visión nocturna permanente |
| **%group-color%Hasten** | Picos, Palas, Hachas | 3 | 15–45% | 3 s | Posibilidad de ganar prisa después de romper bloques |
| **%group-color%Lumbricida** | Palas | 2 | 2–5% | — | Al excavar, probabilidad de recuperar saturación para no pasar hambre. |
| **%group-color%Nawel** | Maza | 3 | 25–45% | 4 s | Posibilidad de lanzar al enemigo por los aires con un golpe poderoso. |
| **%group-color%Pesca Ruidosa** | Caña de pescar | 2 | 30–60% | — | Delfines chapotearán fuerte al morder el pez ayudándote a atraparlo. |
| **%group-color%Pichi** | Botas | 2 | 30–50% | 3 s | Pequeño impulso de velocidad al saltar. |
| **%group-color%Pies de Rana** | Botas | 2 | 100% | — | Otorga de forma pasiva Gracia del Delfín, haciéndote nadar extremadamente rápido. |
| **%group-color%Rebreather** | Picos | 2 | 30–60% | 3 s | Posibilidad de recuperar aire al minar bajo el agua |
| **%group-color%Smelting** | Picos, Palas | 3 | 33–100% | — | Posibilidad de fundir bloques minados. |
| **%group-color%Strike** | Tridente, Arco, Ballesta, Espadas | 3 | 24–40% | 3–4 s | Posibilidad de golpear con un rayo al oponente |
| **%group-color%Timbre de Vida** | Armadura | 2 | 100% | 30 s | Al entrar en combate echa a sonar una campana de auxilio y te otorga absorción. |
| **%group-color%Trayén** | Lanzas | 3 | 30–80% | 8 s | Posibilidad de obtener respiración acuática al golpear un enemigo bajo el agua. |

### 🟢 Único

Efectos moderados y debuffs.

| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |
|---|---|---:|---:|---:|---|
| **%group-color%Alarma de Enderman** | Cascos | 1 | 100% | — | Pasa desapercibido entre monstruos hasta golpearlos, sonando como un Enderman furioso. |
| **%group-color%Anchimalen** | Cascos | 3 | 15–25% | — | El espíritu de luz regenera lentamente tu salud mientras lo portas. |
| **%group-color%Berserk** | Espadas, Hachas | 5 | 4–20% | 4–8 s | Posibilidad de ganar fuerza y fatiga de minería. |
| **%group-color%Devour** | Espadas, Hachas | 3 | 10–35% | — | Posibilidad de restaurar comida al matar mobs. |
| **%group-color%Famine** | Espadas, Hachas | 4 | 12–22% | 8 s | Posibilidad de dar el efecto de hambre al oponente. |
| **%group-color%Kürüf Tiwe** | Tridente | 3 | 20–40% | 5 s | La lanza arrojada arrastra al enemigo hacia ti al impactar. |
| **%group-color%Kürüfkona** | Maza | 3 | 12–22% | 6 s | El impacto del mazo aturde al enemigo, ralentizándolo y causando náuseas. |
| **%group-color%Longko** | Espadas, Hachas | 2 | 60–100% | 5 s | Al eliminar a un jugador, el jefe guerrero gana fuerza y velocidad temporalmente. |
| **%group-color%Perish** | Tridente, Arco, Ballesta | 5 | 9–21% | 3 s | Posibilidad de causar efecto de marchitamiento al disparar. |
| **%group-color%Piel de Espinas** | Pecheras | 2 | 7–10% | 7–8 s | Daña y ralentiza al atacante que te golpee. |
| **%group-color%Pirün** | Lanzas | 3 | 18–30% | 4–5 s | El giro veloz de la lanza envenena al enemigo al impactar. |
| **%group-color%Ravenous** | Espadas, Hachas | 4 | 14–26% | 6 s | Posibilidad de recuperar hambre mientras luchas |
| 🆕 **%group-color%Raíz** | Pecheras | 3 | 15–35% | 6–10 s | Posibilidad de plantarte firme y no retroceder al ser golpeado. |
| **%group-color%Reflect** | Armadura | 5 | 3–11% | 20 s | Absorbe el daño del enemigo y lo refleja. |
| **%group-color%Rugido Protector** | Pecheras | 2 | 10–20% | 15 s | Ruge como un devastador empujando monstruos cercanos. |
| 🆕 **%group-color%Ruka** | Armadura | 3 | 10–26% | 8–12 s | Posibilidad de resguardarte y recibir menos daño de proyectiles. |
| **%group-color%Sangre Tóxica** | Pecheras | 3 | 10–20% | 8 s | Al ser atacado, tu sangre tóxica tiene probabilidad de envenenar y confundir a tu atacante. |
| **%group-color%Sin Alma** | Tridente, Arco, Ballesta | 4 | 25–100% | 0–2 s | Aumenta el daño infligido a mobs hostiles. |
| **%group-color%Slayer** | Espadas, Hachas | 4 | 25–100% | 0–2 s | Aumenta el daño infligido a mobs pasivos |
| **%group-color%Toque Helado** | Espadas, Hachas | 3 | 5–10% | 12 s | Aplica fatiga minera y debilidad al rival temporalmente. |
| **%group-color%Virus** | Tridente, Arco, Ballesta | 4 | 6–40% | 2 s | Posibilidad de causar veneno al disparar. |
| **%group-color%Ward** | Armadura | 4 | 4–10% | 20 s | Posibilidad de absorber el daño del enemigo |
| **%group-color%Ñuke** | Pecheras | 3 | 8–16% | 10 s | El espíritu materno otorga posibilidad de regeneración al ser golpeado. |

### 🔵 Elite

Habilidades de combate especializadas.

| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |
|---|---|---:|---:|---:|---|
| **%group-color%Blind** | Espadas | 3 | 17–33% | 5 s | Posibilidad de causar ceguera al atacar. |
| **%group-color%Blunt Force** | Hachas | 4 | 5–12% | 5 s | Posibilidad de golpear con gran fuerza. |
| **%group-color%Bowmaster** | Tridente, Arco, Ballesta | 5 | 15–55% | 2 s | Multiplica el daño contra jugadores que están usando una espada. |
| **%group-color%Coñi** | Espadas | 3 | 5–10% | 10 s | Cada golpe del joven guerrero tiene posibilidad de infundirle fuerza momentánea. |
| **%group-color%Critical** | Espadas | 3 | 7–12% | 5 s | Aumenta el daño realizado con golpes críticos. |
| **%group-color%Disparo de Ghast** | Arco, Ballesta | 3 | 15–35% | 10–12 s | Dispara la flecha con el sonido desgarrador de un Ghast causando confusión. |
| **%group-color%Ender Slayer** | Espadas, Hachas | 5 | 16–41% | 2 s | Aumenta el daño infligido a Enderman y dragones Ender |
| **%group-color%Escapist** | Botas | 1 | 30% | — | Posibilidad de obtener un impulso de Velocidad IV con poca salud. |
| **%group-color%Extinguish** | Pantalones | 3 | 20–80% | — | Posibilidad de extinguirse cuando estás en llamas. |
| **%group-color%Frozen** | Armadura | 3 | 19–26% | 6 s | Puede causar lentitud al atacante cuando te defiendes. |
| **%group-color%Geólogo Veloz** | Picos | 3 | 7–20% | 8 s | Al picar ores, te otorga un subidón momentáneo de Velocidad para moverte volando por las cuevas. |
| **%group-color%Gravedad Cero** | Arco, Ballesta | 4 | 4–10% | 15 s | Las flechas imbuidas alteran la gravedad del objetivo, haciéndolo flotar. |
| **%group-color%Greatsword** | Espadas | 5 | 15–55% | 2 s | Multiplica el daño contra jugadores que están usando un arco. |
| **%group-color%Grito de Guerra** | Hachas | 3 | 4–8% | 15 s | Aumenta el propio daño y marea al objetivo. |
| **%group-color%Hook** | Caña de pescar | 3 | 15–35% | 12 s | Obtén más experiencia al pescar. |
| **%group-color%Immolate** | Espadas, Hachas | 3 | 25–75% | 0–2 s | Aumenta el daño infligido a arañas |
| **%group-color%Impact** | Tridente | 4 | 5–14% | 3–6 s | Posibilidad de duplicar el daño infligido |
| **%group-color%Impulso Sónico** | Arco, Ballesta | 3 | 10–20% | 12 s | Otorga un fuerte impulso de velocidad al disparar. |
| **%group-color%Infernal** | Espadas, Hachas | 3 | 15–50% | 2 s | Efecto de fuego explosivo. |
| 🆕 **%group-color%Kintu** | Espadas | 3 | 12–28% | 12–20 s | Posibilidad de marcar al enemigo, revelándolo aunque sea invisible. |
| **%group-color%Kollong** | Pantalones | 3 | 12–20% | 8 s | Al ser atacado, lanzas una cortina de humo que ciega a tu agresor. |
| 🆕 **%group-color%Lafken** | Caña de pescar | 3 | 25–55% | 10–15 s | Posibilidad de recuperar hambre al pescar, como un banquete del mar. |
| **%group-color%Llanka** | Lanzas | 4 | 10–22% | 12 s | La lanza de cristal congela al enemigo impidiéndole moverse. |
| **%group-color%Magnet** | Espadas | 3 | 30–100% | 5 s | Tu ataque atrae a los jugadores hacia ti. |
| **%group-color%Marchitamiento** | Armadura | 5 | 9–21% | 3 s | Posibilidad de causar efecto de marchitamiento al atacante. |
| **%group-color%Marksman** | Ballesta | 4 | 13–32% | 3 s | Aumenta el daño infligido con ballestas. · ⛔ no combina con %group-color%Piercing |
| **%group-color%Nether Slayer** | Espadas, Hachas | 5 | 16–41% | 2 s | Aumenta el daño infligido a mobs del Nether. |
| **%group-color%Nightwalker** | Espadas | 3 | 40–100% | — | Congelar a los mobs durante la noche. |
| **%group-color%Pillán** | Maza | 4 | 8–20% | 5 s | Invoca el rayo del espíritu del trueno al golpear, dañando también la armadura. |
| **%group-color%Poison** | Espadas, Hachas | 3 | 6–35% | 2 s | Posibilidad de causar veneno al atacar. |
| **%group-color%Poisoned** | Armadura | 4 | 8–23% | 6 s | Posibilidad de envenenar a tu atacante. |
| **%group-color%Poseidon** | Tridente | 4 | 13–32% | 3 s | Aumenta el daño infligido con tridentes. · ⛔ no combina con %group-color%Piercing |
| 🆕 **%group-color%Rayen** | Azadas | 3 | 10–26% | — | Posibilidad de obtener el doble de cultivos al cosechar. |
| **%group-color%Reaper** | Hachas | 4 | 8–14% | 10–16 s | Posibilidad de dar efectos de Wither y ceguera al oponente. |
| **%group-color%Reforged** | Hachas, Espadas, Picos, Palas | 10 | 8–80% | — | Protege la durabilidad de las armas y herramientas, haciendo que duren más. |
| **%group-color%Replenish** | Picos | 3 | 30–60% | — | Posibilidad de restaurar comida mientras se mina. |
| **%group-color%Smoke Bomb** | Cascos | 8 | 9–38% | 2 s | Lanza una bomba de humo para distraer a los enemigos cuando tu salud es baja. |
| **%group-color%Snap** | Caña de pescar | 3 | 15–100% | 0–6 s | Atrae a la entidad golpeada hacia ti. |
| **%group-color%Snare** | Arco, Ballesta | 4 | 12–29% | 3 s | Posibilidad de ralentizar y fatigar a los enemigos con proyectiles. |
| **%group-color%Springs** | Botas | 3 | 100% | — | Otorga un impulso de salto. |
| **%group-color%Suspend** | Espadas | 3 | 40–100% | — | Posibilidad de no causar retroceso a los mobs. |
| **%group-color%Tambores de Guerra** | Hachas | 3 | 8–16% | 15 s | Golpear crea el sonido retumbante de un yunque amplificando tu Daño inmensamente. |
| **%group-color%Trickster** | Armadura | 8 | 8–51% | 5 s | Posibilidad de teletransportarse detrás del oponente al ser golpeado. |
| **%group-color%Vampire** | Espadas | 3 | 7–15% | 4 s | Posibilidad de curarte después de atacar. |
| **%group-color%Voodoo** | Armadura | 6 | 5–21% | 2 s | Posibilidad de debilitar al atacante. |
| **%group-color%Wolves** | Pecheras | 10 | 6–30% | 10–20 s | Posibilidad de invocar lobos para defenderte en combate. |

### 🟣 Ultimate

Poderosos, con efectos de área.

| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |
|---|---|---:|---:|---:|---|
| **%group-color%Aegis** | Botas | 3 | 40–70% | 3 s | Posibilidad de ganar velocidad al recibir daño por caída. |
| **%group-color%Ambit** | Espadas, Hachas | 7 | 4–15% | 8–14 s | Daño a mobs en un radio que aumenta con el nivel de encantamiento. |
| **%group-color%Archer** | Arco | 4 | 13–32% | 3 s | Aumenta el daño infligido con arcos. · ⛔ no combina con %group-color%Piercing |
| **%group-color%Arrow Break** | Hachas | 6 | 15–65% | 8–10 s | Posibilidad de que las flechas reboten mientras sostienes un objeto con este encantamiento. |
| **%group-color%Arrow Deflect** | Armadura | 4 | 15–45% | 6 s | Posibilidad de prevenir que una flecha enemiga cause daño. |
| **%group-color%Auto Reel** | Caña de pescar | 4 | 25–100% | — | Automáticamente recoge la caña de pescar cuando muerde |
| **%group-color%Beaconer** | Tridente | 3 | 33–75% | 5 s | Posibilidad de escuchar el sonido del faro desactivándose al hacer clic derecho con un Tridente. |
| **%group-color%Bleed** | Hachas | 6 | 8–60% | — | Causar sangrado al oponente. |
| **%group-color%Ceguera Nocturna** | Espadas | 3 | 2–7% | 18 s | Probabilidad de aplicar ceguera y marchitamiento al rival. |
| **%group-color%Cherufe** | Maza | 3 | 6–10% | 12–15 s | Desata el espíritu del meteoro: explosión de fuego que dañaa a enemigos cercanos. |
| **%group-color%Cleave** | Hachas | 7 | 4–15% | 8–14 s | Daño a jugadores en un radio que aumenta con el nivel de encantamiento. |
| **%group-color%Confuse** | Espadas | 4 | 12–18% | 6–8 s | Posibilidad de dar el efecto de náusea. |
| **%group-color%Cosecha** | Azadas | 9 | 13–100% | — | Tiene la posibilidad de cosechar en un área de 3x3. |
| **%group-color%Creeper Armor** | Armadura | 3 | 25–75% | — | Posibilidad de ser inmune al daño explosivo, con una posibilidad de curación en niveles más altos. |
| **%group-color%Despegue** | Élitros | 2 | 100% | 15–20 s | Haz clic derecho para salir disparado hacia el cielo sin necesidad de fuegos artificiales. |
| **%group-color%Disintegrate** | Espadas | 4 | 12–46% | 2 s | Posibilidad de causar daño adicional a la durabilidad de toda la armadura enemiga con cada ataque. |
| **%group-color%Dodge** | Armadura | 5 | 8–20% | 20 s | Posibilidad de esquivar ataques físicos, con mayor probabilidad al agacharse. |
| **%group-color%Endmaster** | Espadas | 3 | 25–75% | — | Doble daño a mobs en el End. |
| **%group-color%Erupción** | Picos | 3 | 1–3% | 10–20 s | Crea una gran erupción minera destrozando bloques en una amplia zona. |
| **%group-color%Espíritus** | Armadura | 10 | 2–27% | 8 s | Posibilidad de invocar blazes guardianes. |
| **%group-color%Exalted** | Espadas | 4 | 12–36% | 8 s | Posibilidad de eliminar efectos de poción negativos. |
| **%group-color%Flap** | Élitros | 3 | 33–75% | 5 s | Posibilidad de reproducir el sonido de aleteo del dragón al volar con Elitros. |
| **%group-color%Guardians** | Armadura | 10 | 6–24% | 8–15 s | Posibilidad de invocar gólems de hierro para ayudarte. |
| **%group-color%Heavy** | Armadura | 5 | 4–21% | 4 s | Disminuye el daño de los arcos enemigos en un 2% por nivel. |
| **%group-color%Ice Aspect** | Espadas | 3 | 15–31% | 2 s | Posibilidad de causar lentitud en el enemigo. |
| **%group-color%Immolation** | Espadas | 3 | 10–16% | 4–5 s | Pone en llamas a todos los mobs en un radio. |
| **%group-color%Implants** | Cascos | 3 | 30–70% | — | Posibilidad de restaurar comida cada pocos segundos. |
| **%group-color%Jelly Legs** | Botas | 3 | 40–100% | — | Posibilidad de negar el daño por caída. |
| **%group-color%Kimün** | Picos | 3 | 10–20% | 1 s | El conocimiento ancestral extrae energía de cada bloque roto. |
| **%group-color%Longbow** | Arco, Ballesta | 4 | 12–33% | 4 s | Aumenta en gran medida el daño infligido a jugadores enemigos que tienen un arco en las manos. |
| **%group-color%Lucky** | Caña de pescar | 3 | 75–95% | 12 s | Posibilidad de aumentar la suerte al pescar. |
| **%group-color%Malón** | Lanzas | 3 | 8–14% | 8–10 s | El giro de la lanza golpea a todos los enemigos en un radio creciente. |
| 🆕 **%group-color%Mawida** | Hachas | 4 | 8–28% | 3–6 s | Posibilidad de talar el árbol completo de un solo golpe. |
| **%group-color%Mjolnir** | Hachas | 4 | 6–12% | 30 s | Posibilidad de invocar un poderoso relámpago sobre tu objetivo. |
| **%group-color%Netherling** | Espadas | 3 | 25–75% | — | Doble daño a mobs en el Nether. |
| **%group-color%Night Owl** | Espadas | 3 | 40–80% | — | Infligir más daño a los mobs durante la noche. |
| **%group-color%Obsidianshield** | Armadura | 1 | 100% | — | Proporciona resistencia al fuego permanente. |
| **%group-color%Parada Relámpago** | Espadas | 3 | 5–15% | 18 s | Bloquear o repeler daño genera un trueno distractor y regenerativo. |
| **%group-color%Permafrost** | Espadas | 5 | 15–25% | 12–15 s | Posibilidad de ralentizar y hacer sangrar a los oponentes. |
| **%group-color%Petrify** | Pantalones | 3 | 5–11% | 20 s | Posibilidad de dar lentitud extrema al atacante. |
| **%group-color%Piercing** | Arco, Ballesta | 5 | 13–37% | 3 s | Inflige más daño. · ⛔ no combina con %group-color%Archer, %group-color%Marksman, %group-color%Poseidon |
| **%group-color%Püllü** | Espadas | 3 | 7–13% | 8 s | Roba la energía vital y la esencia de experiencia de cada golpe asestado. |
| **%group-color%Rayün** | Armadura | 3 | 5–11% | 10 s | El rayo de luz contraataca al agresor con un relámpago cuando eres dañado. |
| **%group-color%Reinforced** | Élitros | 4 | 15–75% | 1 s | Reduce el daño recibido. |
| **%group-color%Safeguard** | Armadura | 2 | 5–9% | 5 s | Posibilidad de obtener resistencia al daño al defender. |
| **%group-color%Shatter** | Hachas | 4 | 12–46% | 2 s | Posibilidad de causar daño adicional a la durabilidad de toda la armadura enemiga con cada ataque. |
| **%group-color%Sniper** | Arco | 5 | 15–35% | 5 s | Los disparos a la cabeza con arco infligen el doble de daño. |
| **%group-color%Striker** | Arco | 3 | 15–22% | 8 s | Lluvia de flechas sobre el oponente. |
| **%group-color%Swordsman** | Armadura | 5 | 4–21% | 4 s | Posibilidad de reducir el daño entrante mientras se empuña una espada, hasta un 22% en el nivel máximo. |
| **%group-color%Tala Épica** | Hachas | 3 | 7–17% | 4 s | Talar genera Prisa y Velocidad de movimiento. |
| **%group-color%Taladro Ensordecedor** | Picos | 3 | 4–10% | 10 s | Escucha el sonido de pistones pesados mientras destrozas bloques a máxima velocidad. |
| **%group-color%Tank** | Armadura | 4 | 5–16% | 3 s | Disminuye el daño de los ataques de hachas enemigas en un 2% por nivel. |

### 🟡 Legendario

Raros y muy fuertes.

| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |
|---|---|---:|---:|---:|---|
| **%group-color%Aqua** | Botas | 4 | 8–23% | 3–5 s | Doble daño mientras se está en el agua. |
| **%group-color%Armored** | Armadura | 4 | 6–20% | 8 s | Disminuye el daño de espadas enemigas en un 2% por nivel. |
| **%group-color%Aura Cristalina** | Pantalones | 3 | 5–11% | 30 s | Al recibir golpes te recubres de cristal otorgando gran resistencia. |
| **%group-color%Bait** | Caña de pescar | 3 | 15–26% | 10–20 s | Posibilidad de recibir dobles drops al pescar. |
| **%group-color%Barbarian** | Hachas | 4 | 8–25% | 8 s | Posibilidad de infligir más daño con hachas. |
| **%group-color%Beastslayer** | Espadas, Hachas | 4 | 25–100% | 0–2 s | Aumenta el daño infligido a mobs hostiles. |
| **%group-color%Blacksmith** | Hachas | 5 | 9–39% | 3 s | Repara tu arma a cambio de hacer menos daño. |
| **%group-color%Caos** | Arco, Ballesta | 4 | 5–12% | 20 s | Probabilidad de tirar un rayo e incendiar el objetivo. |
| **%group-color%Chaos** | Tridente | 5 | 2–10% | 40 s | Infligir efectos de debilidad y marchitamiento. |
| **%group-color%Convulse** | Botas | 6 | 8–18% | 10 s | Posibilidad de lanzar a los atacantes por el aire. |
| **%group-color%Coro del Vacío** | Arco, Ballesta | 3 | 5–11% | 15 s | Proyectiles que silban con la brisa del Shulker aplicando ceguera levitante. |
| **%group-color%Deadshot** | Tridente | 5 | 15–35% | 5 s | Los disparos a la cabeza con tridentes infligen el doble de daño. |
| **%group-color%Divert** | Armadura | 5 | 6–16% | 20–25 s | Posibilidad de envenenar al oponente y obtener regeneración. |
| **%group-color%Double Strike** | Espadas | 3 | 8–19% | 15 s | Posibilidad de golpear dos veces. |
| **%group-color%Espejismo** | Pantalones | 3 | 2–5% | 20–30 s | Probabilidad de esquivar completamente un ataque y volverte invisible, confundiendo al atacante. |
| **%group-color%Fortaleza** | Armadura | 3 | 2–5% | 35–45 s | Al recibir daño, puede otorgar Resistencia y Lentitud simulando inamovilidad. |
| **%group-color%Gears** | Botas | 2 | 100% | — | Añade velocidad cuando se equipa. |
| **%group-color%Hardened** | Armadura | 3 | 25–45% | 7 s | Posibilidad de recuperar durabilidad cuando te dañan. |
| **%group-color%Inflame** | Hachas | 3 | 10–16% | 4–5 s | Pone en llamas a todos los jugadores en un radio. |
| **%group-color%Inquisitive** | Espadas | 4 | 30–45% | 4 s | Posibilidad de aumentar las gotas de EXP de los mobs. |
| **%group-color%Judgement** | Élitros | 5 | 6–16% | 20–25 s | Posibilidad de envenenar al oponente y obtener regeneración. |
| **%group-color%Lava Walker** | Botas | 1 | 100% | — | Caminar sobre la lava. |
| 🆕 **%group-color%Lawen** | Pecheras | 3 | 12–28% | 25–40 s | Con poca vida, posibilidad de regenerarte con hierbas medicinales. · ⛔ no combina con %group-color%Inmortalidad, %group-color%Sombra Quimera, %group-color%Pulso de Dragón, %group-color%Técnica Inversa |
| **%group-color%Lifesteal** | Espadas | 5 | 9–25% | 15 s | Posibilidad de robar salud al atacar. |
| **%group-color%Longko Pillán** | Maza | 3 | 4–8% | 20–25 s | El jefe del trueno encadena relámpagos que golpean al objetivo y dañan su armadura. |
| **%group-color%Lucid** | Armadura | 3 | 22–42% | 5 s | Posibilidad de curar ceguera y ganar visión nocturna cuando se recibe daño. |
| **%group-color%Nawel Konün** | Lanzas | 3 | 6–10% | 15–18 s | El jaguar penetra las defensas: duplica el daño y roba la vida del objetivo. |
| **%group-color%Ngen** | Espadas, Hachas | 3 | 5–11% | 10 s | El espíritu guardián hace que tus ataques ignoren la protección de la armadura enemiga. |
| **%group-color%Overload** | Armadura | 3 | 100% | — | Desbloquea corazones adicionales. |
| **%group-color%Patch** | Armadura | 3 | 25–45% | 7 s | Posibilidad de recuperar durabilidad cuando recibes daño de mobs. |
| 🆕 **%group-color%Perforante** | Hachas, Lanzas, Maza | 4 | 5–14% | 6–8 s | Posibilidad de que el golpe ignore la protección de la armadura. |
| **%group-color%Rocket Launch** | Arco | 3 | 12% | 7 s | Posibilidad de lanzar al enemigo por el aire. |
| **%group-color%Snag** | Espadas | 3 | 10–100% | 30–60 s | Posibilidad de eliminar el efecto de velocidad de un enemigo. · 🎁 solo por eventos o admin |
| **%group-color%Strife** | Tridente | 3 | 5–15% | 3–8 s | Incrementa el daño cuerpo a cuerpo de los tridentes. |
| **%group-color%Talismán de Fuego** | Armadura, Picos | 1 | 100% | — | Te brinda inmunidad total al fuego y visión nocturna permanente. |
| **%group-color%Turmoil** | Armadura | 3 | 10–18% | 8 s | Posibilidad de evitar que los guardias del oponente aparezcan. |
| **%group-color%Twinge** | Tridente | 4 | 5–14% | 3–6 s | Hace que el enemigo sangre al ser golpeado con un ataque cuerpo a cuerpo. |
| **%group-color%Unholy** | Armadura | 5 | 2–10% | 40 s | Defender con efectos de debilidad y marchitamiento. |
| **%group-color%Water Walker** | Botas | 1 | 100% | — | Caminar sobre el agua. |
| 🆕 **%group-color%Weichafe** | Espadas, Hachas | 3 | 20–50% | 10–15 s | Al eliminar a un enemigo, ganas absorción y velocidad breves. |
| **%group-color%Wekufe** | Armadura | 3 | 5–9% | 15 s | El espíritu maligno maldice al atacante con marchitamiento y debilidad al dañarte. |
| **%group-color%Witranalwe** | Armadura | 3 | 10–20% | 20 s | El espíritu que se eleva: cuando tu salud es baja te vuelves invisible y veloz. |

### 🔴 Fabled

Los más poderosos del servidor. No salen de la mesa de encantamientos.

| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |
|---|---|---:|---:|---:|---|
| **%group-color%Bankai** | Espadas, Hachas | 3 | 2–5% | 30–50 s | Libera el estado final de tu zanpakutō devastando al enemigo con poder absoluto. |
| **%group-color%Bendición de Merlín** | Picos, Hachas, Palas | 2 | 1–2% | 180–240 s | Probabilidad de un destello mágico minero que limpia todos tus efectos negativos, te cura al 100% y te hace brillar de suerte. |
| **%group-color%Desmantelar** | Espadas | 4 | 5–15% | 4–5 s | Una técnica de corte invisible que causa severa hemorragia. |
| **%group-color%Despertar de Wither** | Espadas, Hachas | 3 | 4–10% | 40 s | Criticos terroríficos invocan el spawn de un wither al golpear marchitando al rival. |
| **%group-color%Destello Oscuro** | Espadas, Hachas | 3 | 3–8% | 6–8 s | Un impacto concentrado de energía maldita que aturde. |
| **%group-color%Diploid** | Espadas | 5 | 15–30% | 5–8 s | Tiene probabilidad de multiplicar los drops de mobs. Cuesta 5 almas / activación. |
| **%group-color%Discurso Maldito** | Arco, Ballesta, Tridente | 2 | 8–14% | 10–12 s | Fuerza al enemigo a detenerse con palabras imbuidas en energía. |
| **%group-color%Dominio Temporal** | Espadas, Hachas | 4 | 2–7% | 40–45 s | Congela el tiempo para tu oponente mientras tú te aceleras. |
| **%group-color%Exorcista** | Espadas | 4 | 30–60% | 2 s | Elimina a los no-muertos y espritus malditos con gran facilidad. |
| **%group-color%Expansión de Dominio** | Espadas, Hachas | 3 | 5–11% | 15–25 s | Atrapa a tu oponente abrumando todos sus sentidos. |
| **%group-color%Flash Paso** | Botas, Pantalones | 3 | 6–12% | 16–25 s | Domina el Shunpo para desaparecer del punto de impacto en un instante. |
| **%group-color%Getsuga Tenshō** | Espadas, Hachas | 4 | 5–12% | 14–20 s | Lanza una ola de energía espiritual comprimida que desgarra al enemigo. |
| **%group-color%Golpe Divergente** | Espadas, Hachas | 4 | 10–25% | 5–6 s | Un doble impacto que descarga energa de forma retardada. |
| **%group-color%Hacha de los Espíritus** | Hachas | 3 | 45–75% | — | Probabilidad de obtener más almas al matar jugadores. · 👻 genera almas |
| **%group-color%Haste** | Picos, Palas, Hachas | 3 | 100% | — | Permite usar las herramientas más rápido |
| **%group-color%Hero** | Armadura | 1 | 100% | — | Otorga Héroe de la Aldea. |
| **%group-color%Hueco Púrpura** | Arco, Ballesta, Tridente | 3 | 3–7% | 14–18 s | Fusión de rojo y azul que borra la materia frente a ti. |
| **%group-color%Infinito** | Armadura | 3 | 2–6% | 8–10 s | La técnica impecable que detiene los ataques antes de alcanzarte. |
| **%group-color%Inmortalidad** | Pecheras | 3 | 100% | 300 s | Si la vida baja críticamente, te recupera salud y otorga regeneración. · ⛔ no combina con %group-color%Sombra Quimera, %group-color%Pulso de Dragón, %group-color%Técnica Inversa, %group-color%Lawen |
| **%group-color%Lluvia Negra** | Espadas, Hachas | 4 | 11–23% | 6–20 s | La locura del combate te embriaga, aumentando tu poder con cada golpe encadenado. |
| **%group-color%Multiplication** | Picos | 5 | 15–30% | 5–8 s | Probabilidad de multiplicar drops de minerales. Cuesta 5 almas / activación. · 👻 gasta 8 almas |
| **%group-color%Neutralize** | Arco, Ballesta | 2 | 5–10% | 20 s | Posibilidad de desarmar al oponente. |
| **%group-color%Ngümin Antü** | Espadas, Hachas | 2 | 1.5–2.5% | 60 s | El tejido solar detiene el tiempo: congela al objetivo y paraliza a los enemigos cercanos. |
| **%group-color%Nulify** | Espadas, Hachas | 4 | 8–14% | 10 s | Tiene una pequeña probabilidad de infligir el doble de daño dejando al enemigo ciego. Cuesta 40 almas/activación · 👻 gasta 40 almas |
| **%group-color%Presión del Reiatsu** | Pecheras | 4 | 12–25% | 8–14 s | Tu energía espiritual aplasta a los enemigos cercanos ralentizándolos con tu mera presencia. |
| **%group-color%Pulso de Dragón** | Armadura, Élitros | 3 | 100% | 190–240 s | Emites un aleteo sónico salvador para cancelar daños mortales y huir volando. · ⛔ no combina con %group-color%Inmortalidad, %group-color%Sombra Quimera, %group-color%Técnica Inversa, %group-color%Lawen |
| **%group-color%Püllümapu** | Lanzas | 2 | 2–3% | 45 s | Drena el alma de la tierra del enemigo: roba vida y aplica marchitamiento profundo. |
| **%group-color%Restore** | Picos, Palas, Hachas | 4 | 40–100% | — | Posibilidad de reparar el ítem a mitad de su durabilidad al romperse, perdiendo el encantamiento. |
| **%group-color%Rush** | Élitros | 3 | 15–26% | 5 s | Probabilidad de impulso de velocidad al despegar con la elytra. Cuesta 10 almas / activación. · 👻 gasta 10 almas |
| **%group-color%Scare** | Espadas, Hachas | 5 | 1.8–6% | 20 s | Posibilidad de reemplazar el casco del oponente con una calabaza por un tiempo corto. |
| **%group-color%Senescencia** | Armadura | 4 | 5–12% | 18–30 s | Drenas la vitalidad del enemigo canalizando el poder del Rey Espiritual. |
| **%group-color%Sombra Quimera** | Armadura | 3 | 100% | 120–180 s | Te fundes en las sombras para eludir un golpe fatal. · ⛔ no combina con %group-color%Inmortalidad, %group-color%Pulso de Dragón, %group-color%Técnica Inversa, %group-color%Lawen |
| **%group-color%Soulbound** | Herramientas, Espadas, Arco, Ballesta | 3 | 4–8% | 300 s | Tiene una pequeña probabilidad de conservar el objeto al morir. |
| **%group-color%Soulgrind** | Espadas | 3 | 30–70% | — | Probabilidad de obtener almas matando mobs. · 👻 genera almas |
| **%group-color%Soulminer** | Picos | 3 | 5–15% | — | Tiene probabilidad de obtener almas minando. · 👻 genera almas |
| **%group-color%Spiritmaster** | Espadas | 3 | 35–55% | — | Tiene probabilidad de obtener más almas al matar jugadores. · 👻 genera almas |
| **%group-color%Terraformer** | Picos | 1 | 100% | — | Mina en un área de 3x3 de forma permanente. · 🎁 solo por eventos o admin |
| **%group-color%Técnica Inversa** | Armadura | 4 | 8–20% | 20–25 s | Sanación avanzada al canalizar energía maldita positiva. · ⛔ no combina con %group-color%Inmortalidad, %group-color%Sombra Quimera, %group-color%Pulso de Dragón, %group-color%Lawen |
| **%group-color%Wenumapu** | Maza | 2 | 2–3% | 40 s | El cielo y la tierra colisionan: golpe devastador que sacude a todos los enemigos cercanos. |

### ⛔ Incompatibilidades

Para evitar combinaciones abusivas, estos encantamientos **no se pueden tener juntos** en el mismo objeto:

- **%group-color%Marksman** ✕ %group-color%Piercing
- **%group-color%Poseidon** ✕ %group-color%Piercing
- **%group-color%Archer** ✕ %group-color%Piercing
- **%group-color%Piercing** ✕ %group-color%Archer, %group-color%Marksman, %group-color%Poseidon
- **%group-color%Lawen** ✕ %group-color%Inmortalidad, %group-color%Sombra Quimera, %group-color%Pulso de Dragón, %group-color%Técnica Inversa
<!-- AUTO:fin encantamientos -->

---

## 🎁 Items Especiales del Plugin

Todos estos items tienen **textura personalizada** en el servidor. Ademas de los encantamientos, el plugin incluye items que modifican el sistema:

| Item (nombre en servidor) | Nombre original del plugin | Funcion |
|---------------------------|---------------------------|---------|
| **Encantamiento Aleatorio** | Random Enchantment Book | Haz clic derecho para limpiar el libro y revelar un encantamiento aleatorio de la rareza indicada |
| **Gema de Suerte** | Magic Dust | Arrastra sobre un **libro** antes de aplicarlo: reduce su Tasa de Destruccion segun la rareza de la gema |
| **Paquete Arcano** | Secret Dust | Paquete misterioso que al abrirse puede contener una Gema de Suerte (resultado aleatorio) |
| **Piedra Abandonada** | Mystery Dust | Item sin valor practico que puede obtenerse del Tinkerer en tiradas bajas |
| **Runa de la Proteccion** | White Scroll | Arrastra sobre el **objeto** antes de encantar: protege el objeto de ser destruido si un encantamiento falla |
| **Runa de Extraccion** | Black Scroll | Extrae un encantamiento aleatorio del objeto y lo convierte en libro (95% exito, 5% destruccion del objeto) |
| **Libro Universal** | Slot Increaser | Agrega +1 ranura de encantamiento al objeto sin riesgo (hasta el maximo de 13 ranuras) |
| **Runa del Alma** | Soul Tracker | Arrastra sobre un arma o herramienta para activar el rastreo de almas recolectadas de kills |
| **Gema de Alma** | Soul Gem | Aplica a un objeto con la Runa del Alma activa para añadirle almas directamente |
| **Runa de la Revelacion** | Transmog Scroll | Arrastra sobre un objeto: ordena sus encantamientos por rareza en el lore y añade un contador de encantamientos al nombre |
| **Runa del Ligado al Alma** | Holy White Scroll | Arrastra sobre armadura o armas: da 100% de probabilidad de no perder el objeto al morir |
| **Pluma Renombradora** | Item Nametag | Permite escribir un nombre personalizado (con colores) a cualquier objeto encantado |
| **Pergamino Minero** | BlockTrak | Registra el numero de bloques rotos con la herramienta; el contador aparece en el lore |
| **Pergamino Pescador** | FishTrak | Registra el numero de peces capturados con la cana de pescar |
| **Pergamino Guerrero** | StatTrak | Registra el numero de eliminaciones de jugadores con el arma |
| **Pergamino Cazador** | MobTrak | Registra el numero de mobs eliminados con el arma |
| **Tomo de Armas** | Weapon Enchantment Orb | Aumenta las ranuras de encantamiento de un arma en varios puntos; tiene Tasa de Exito (puede fallar) |
| **Tomo de Armadura** | Armor Enchantment Orb | Aumenta las ranuras de encantamiento de una pieza de armadura; tiene Tasa de Exito |
| **Tomo de Herramientas** | Tool Enchantment Orb | Aumenta las ranuras de encantamiento de una herramienta; tiene Tasa de Exito |
| **Totem de Renovacion** | Randomization Scroll | Arrastra sobre un **libro de encantamiento** para rerollear su Tasa de Destruccion por una nueva aleatoria |
| **Libro Cosmico** | Cosmo Book | Libro de rareza cosmica exclusivo de eventos y administracion; contiene encantamientos especiales |
