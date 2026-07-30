# 💰 Comercio y Mercaderes

El sistema de **Comercio** (Trading) de ValhallaMMO reemplaza por completo el comercio vanilla con aldeanos. Ya no son máquinas expendedoras con precios fijos: ahora los aldeanos tienen **estado de ánimo**, te **recuerdan** cómo los tratas, suben de nivel, ofrecen **servicios** además de tratos, y sus precios **cambian** según la oferta, la demanda y tu relación con ellos.

Además, existe una skill propia de **Comercio** que subes comerciando y que desbloquea ventajas cada vez más potentes.

{% hint style="info" %}
No necesitas ningún objeto especial ni permiso. Cualquier aldeano con profesión al que te acerques ya usa este sistema. Haz clic derecho sobre él para abrir su menú.
{% endhint %}

***

## 🔄 Vanilla vs Plugin: qué cambia

Si ya conoces el comercio normal de Minecraft, esta tabla resume lo que hace distinto el plugin:

| Aspecto | 🟫 Minecraft Vanilla | 🟩 Con ValhallaMMO |
|---|---|---|
| **Precio** | Fijo (salvo pequeña variación por descuento de heroísmo) | **Dinámico**: cambia según demanda, felicidad, reputación y renombre |
| **Descuentos** | Solo con "Héroe de la Aldea" o curar a un zombi aldeano | Hasta **-30%** acumulando felicidad + reputación + renombre, más tu carisma |
| **Repetir un trato** | Se puede hasta agotar el stock del día | La **demanda** sube el precio si compras lo mismo muchas veces seguidas |
| **Estado de ánimo** | No existe | El aldeano tiene **felicidad** (-10 a +10); si es muy infeliz **se niega a comerciar** |
| **Memoria del aldeano** | No te recuerda | Guarda **reputación** (contigo) y **renombre** (con toda la zona) a largo plazo |
| **Servicios** | Solo comprar/vender | Además: **entrenar** skills, **reparar/encantar** objetos y **pedidos** a granel |
| **Subir de rango** | Comerciando, desbloquea tratos | Igual, pero además **te da XP** de la skill de Comercio (más cuanto mayor su rango) |
| **Beneficio para ti** | Solo el objeto comprado | El objeto **+ XP de Comercio + perks** que mejoran precios, calidad y servicios |
| **Golpear/matar aldeanos** | Baja un poco el precio local temporalmente | Penaliza **reputación y renombre** de toda la zona, puede volverse **imperdonable** |
| **Decorar el puesto** | No influye | Decoración, luz y espacio **suben la felicidad** y por tanto bajan precios |

**En una frase:** en vanilla el aldeano es una máquina de precios fijos; con el plugin es un **personaje con memoria y humor** al que conviene cuidar, y comerciar bien te hace **progresar** (skill, perks y mejores precios).

***

## 🧑‍🌾 Cómo funciona un mercader

Al hacer clic derecho sobre un aldeano se abre su menú personalizado. Dentro puede haber varias secciones según su profesión:

* **Comerciar** (Trading): comprar y vender objetos, como siempre pero con precios dinámicos.
* **Servicios**: acciones que el aldeano hace por ti a cambio de un pago (entrenar, mejorar, encantar, pedir a granel).

Cada aldeano pertenece a una **profesión** y tiene un **rango** que sube con el uso.

### 📈 Rangos del mercader

Los mercaderes suben de rango a medida que comercias con ellos. Cada rango desbloquea **tratos nuevos y mejores**, y te da más XP de la skill de Comercio.

| Rango | EXP del mercader requerida | XP de Comercio que te da |
|---|---|---|
| Novato (Novice) | 0 | x1.0 |
| Aprendiz (Apprentice) | 40 | x1.1 |
| Oficial (Journeyman) | 160 | x1.3 |
| Experto (Expert) | 320 | x1.6 |
| Maestro (Master) | 640 | x2.0 |

Cuanto más alto el rango del mercader, mejores tratos ofrece y más XP ganas al comerciar con él. Por eso conviene **fidelizar** a unos pocos aldeanos y hacerlos subir en vez de saltar de uno a otro.

***

## 🏪 Las 12 profesiones

Cada profesión vende cosas distintas y ofrece servicios distintos. Estos son los mercaderes del servidor y lo que hacen:

| Profesión | Bloque de trabajo | Servicios que ofrece |
|---|---|---|
| Granjero (Farmer) | Compostador | Comerciar, Entrenar Farming, Pedidos |
| Pastor (Shepherd) | Telar | Comerciar, Entrenar Farming, Pedidos |
| Carnicero (Butcher) | Ahumador | Comerciar, Entrenar Farming, Pedidos |
| Pescador (Fisherman) | Barril | Comerciar, Entrenar Fishing, Reparar cañas, Pedidos |
| Peletero (Leatherworker) | Caldero | Comerciar, Entrenar Light Armor, Pedidos |
| Albañil (Mason) | Cortador de piedra | Comerciar, Entrenar Mining, Pedidos |
| Herrero de armas (Weaponsmith) | Piedra de afilar | Comerciar, Entrenar Smithing/Light/Heavy Weapons, Reparar herramientas, Pedidos |
| Herrero de herramientas (Toolsmith) | Mesa de herrería | Comerciar, Entrenar Smithing/Digging/Woodcutting, Reparar herramientas, Pedidos |
| Armero (Armorer) | Alto horno | Comerciar, Entrenar Smithing/Light/Heavy Weapons, Reparar armadura, Pedidos |
| Fletcher (Fletcher) | Mesa de flechas | Comerciar, Entrenar Archery, Reparar arcos y ballestas, Pedidos |
| Clérigo (Cleric) | Soporte de pociones | Comerciar, Entrenar Alchemy, Pedidos |
| Bibliotecario (Librarian) | Atril | Comerciar, Entrenar Enchanting, Encantar objetos (nivel 10/20/30), Pedidos |

{% hint style="warning" %}
Los servicios de **entrenar** una skill que esté desactivada en el servidor (por ejemplo Enchanting) no tendrán efecto aunque el mercader los liste.
{% endhint %}

***

## 🛠️ Los servicios en detalle

Los servicios son la gran novedad frente al comercio vanilla. En Minecraft normal un aldeano **solo compra y vende**; aquí, además, **trabaja para ti**: te entrena, te repara y encanta objetos, y te consigue pedidos grandes. Estos son los tipos:

### 🟢 Comerciar

El trato clásico: entregas unos objetos y recibes otros. La diferencia es que el **precio no es fijo** (ver sección de precios más abajo) y que el stock se agota con el uso.

### 🔵 Entrenar (Training)

Pagas al mercader y él te da **XP directa de una skill** relacionada con su profesión. Es una forma de subir skills gastando recursos en vez de tiempo.

* El coste y la cantidad de XP escalan con el **rango del mercader** (un Maestro entrena mucho mejor que un Novato).
* Requiere haber desbloqueado el perk **Aprendizaje** (nivel 20 de Comercio).

### ⚪ Mejorar (Upgrading): reparar y encantar

Los mercaderes con herrería o atril pueden **modificar tus objetos** a cambio de un pago:

| Servicio | Quién lo ofrece |
|---|---|
| Reparar Herramientas y Armas | Herrero de armas, Herrero de herramientas |
| Reparar Armadura | Armero |
| Reparar Arcos y Ballestas | Fletcher |
| Reparar Cañas de Pescar | Pescador |
| Encantar al Nivel 10 / 20 / 30 | Bibliotecario |

* Requiere el perk **Trabajadores de Servicios** (nivel 40 de Comercio).
* Con el perk **Descuento VIP** (nivel 60) los servicios salen más baratos.

### 🟡 Pedir (Ordering)

Haces un **pedido a granel** de objetos que el mercader consigue con el tiempo. No lo recibes al instante: tarda unos **días del juego** en estar listo, y luego vuelves a recogerlo.

* Está disponible desde el **nivel 0** de Comercio con casi todas las profesiones.
* Con el perk **Entrega Express** (nivel 40) los pedidos llegan más rápido y puedes pedir más cantidad.

***

## 😀 Estado de ánimo (Felicidad)

Cada aldeano tiene un valor de **felicidad** entre **-10 y +10**. Un aldeano contento te hace **mejores precios**; uno muy infeliz **se niega a comerciar**.

Haz **shift + clic** sobre el mercader para ver el desglose de su felicidad. Estas son las fuentes:

| Factor | Sube la felicidad si... | Baja si... |
|---|---|---|
| 🪟 Espacio | Tiene mucho espacio para moverse (50+ bloques) | Está encerrado (menos de 25 bloques) |
| 🖼️ Confort | Hay decoraciones y objetos bonitos cerca (5+) | El entorno es soso (menos de 2) |
| 💡 Luz | Está en zona iluminada (luz 5+) | Está a oscuras (luz menor a 2) |
| 👥 Compañía | Hay otros aldeanos cerca | Está solo, o hay demasiados (masificado) |
| 🤝 Seguridad | Ha comerciado hace poco | Lleva mucho sin comerciar |
| ❤️ Salud | Está sano | Está herido |
| 😨 Estrés | Sin zombis ni incursiones cerca | Amenazado por zombis o jugadores |
| 🫱 Confianza | No le has hecho daño | Lo golpeaste hace poco |

**Objetos "bonitos" que dan confort:** cuadros, marcos, soportes de armadura, linternas, estanterías, mesas de encantar, cofres, faroles, campanas, mascotas (perros, gatos, loros), animales de granja, abejas, golems de hierro, y más. Decora el puesto de tus mercaderes para tenerlos felices.

{% hint style="danger" %}
Si un aldeano baja de **-3 de felicidad** deja de comerciar contigo hasta que mejore. Y si un aldeano está por debajo de **-5**, dejarán de aparecer golems de hierro para protegerlo.
{% endhint %}

***

## 🎖️ Reputación y Renombre

Además de la felicidad puntual, cada mercader recuerda tu historial con dos valores de largo plazo:

* **Reputación** (-100 a +100): tu relación **personal** con ese aldeano concreto.
* **Renombre** (-100 a +100): tu fama con **todos los aldeanos cercanos** a la vez.

### Cómo cambian

| Acción | Efecto |
|---|---|
| Comerciar | +0.5 reputación |
| Curar a un aldeano zombi (primera vez) | +70 reputación, +5 renombre |
| Ganar una incursión (héroe de la aldea) | +20 renombre |
| Hacer feliz a un aldeano | +1 renombre |
| Golpear a un aldeano repetidamente | -5 reputación, -5 renombre |
| Matar a un aldeano | -50 reputación, -50 renombre a todos los cercanos |
| Matar a un bebé aldeano | -75 reputación y renombre |
| Matar a un golem de hierro | -15 reputación, -25 renombre |

{% hint style="danger" %}
Si tu reputación o renombre cae por debajo de **-999** con un aldeano, se vuelve **imperdonable**: ya no podrás recuperar su confianza. Trata bien a los aldeanos.
{% endhint %}

***

## 💵 Cómo se calcula el precio

El precio final de un trato pasa por varias capas, en este orden:

1. **Precio base** del trato.
2. **Demanda**: cada vez que compras un trato, su "demanda" sube y el precio también. La demanda decae con el tiempo (0.5 por día, máximo 24). Comprar lo mismo muchas veces seguidas lo encarece; conviene rotar.
3. **Descuento por relación**: hasta **-30%** cuando el aldeano está perfectamente feliz y confía en ti. Se reparte así:
   * Hasta ±10% según **felicidad** (-10 a +10)
   * Hasta ±10% según **reputación** (-100 a +100)
   * Hasta ±10% según **renombre** (-100 a +100)
4. **Descuento de Carisma**: tu propio stat de descuento del sistema (mejora con perks de Comercio).

En resumen: **un mercader feliz, con el que tienes buena reputación y renombre, y al que no le saturas la demanda, te vende mucho más barato.**

{% hint style="info" %}
Cuanto más descuento consigues, **más XP de Comercio ganas** por ese trato (hasta 4x el porcentaje de descuento). Comprar barato no solo ahorra: también sube tu skill más rápido.
{% endhint %}

***

## 🤝 La skill de Comercio

Subes la skill de **Comercio** comerciando con mercaderes. La XP depende del rango del mercader y del descuento que consigas. Su árbol de perks tiene dos ramas: una enfocada en **mercancía** (rama A) y otra en **servicios** (rama B).

Consulta el árbol completo con `/val skilltree trading`. El detalle de cada perk está en la [página de Skills](skills.md).

**Resumen de lo que desbloquea:**

| Nivel | Perk | Efecto |
|---|---|---|
| 0 | Comprador en Masa | Compras más unidades antes de agotar el stock |
| 20 | Carisma Amistoso | Los mercaderes suben de nivel más rápido y ofrecen más tratos |
| 20 | Aprendizaje | Desbloquea el servicio de **Entrenar** skills |
| 40 | Entrega Express | Pedidos más rápidos y en mayor cantidad |
| 40 | Trabajadores de Servicios | Desbloquea los servicios de **reparar y mejorar** |
| 60 | Mercancía de Calidad | Objetos del mercader de mayor calidad, más stock |
| 60 | Descuento VIP | Servicios más baratos |
| 80 | Gratitud | Probabilidad (0-10%) de recibir un **regalo** al comerciar |
| 80 | Artesanos | Objetos del mercader de mayor calidad |
| 100 | Mercado Negro | Tratos exclusivos y poderosos con mercaderes Maestros |

***

## ✅ Consejos rápidos

* **Fideliza pocos mercaderes** y hazlos subir a Maestro en vez de comerciar con muchos.
* **Decora sus puestos** (cuadros, faroles, mascotas) y mantenlos iluminados y con espacio para tenerlos felices.
* **No los golpees nunca** y protégelos de los zombis: el renombre negativo afecta a todos los aldeanos de la zona.
* **Rota tus compras** para no disparar la demanda de un mismo trato.
* Busca **descuentos altos**: ahorras recursos y subes Comercio más rápido a la vez.
* Sube Comercio a nivel 20 y 40 cuanto antes para desbloquear **Entrenar** y **Servicios**, que son las funciones más útiles.
