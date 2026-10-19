# ⚙️ MapuCore

**MapuCore** es el plugin propio de Mapucraft. Reúne varias automatizaciones en un solo menú: personalizar tus ítems, reclamar lo que compras en la tienda y más. Escribe **`/mapucraft`** para abrirlo.

***

## 🧰 Qué puedes hacer

| Opción | Comando | Qué hace |
|---|---|---|
| 🎨 **Modelos** | `/mapucraft modelo` o `/modelo` | Aplica un **modelo custom** (skin 3D) a un ítem. Quitarlo es definitivo: el modelo no se recupera |
| 🧱 **Materiales** | `/mapucraft materiales` o `/materiales` | Eliges un bloque de construcción y recibes una **shulker llena** de ese material |
| 🏷️ **Nombre** | `/mapucraft nombre` | Cambia el nombre de un ítem escribiéndolo por chat (con colores `&`) |
| 📜 **Lore** | `/mapucraft lore` | Escribe la descripción de un ítem, línea por línea |
| ✨ **Desencantar** | `/mapucraft desencantar` | Quita encantamientos de un ítem |
| 🐛 **Spawners** | `/mapucraft spawner` | Reclama los spawners que compraste |
| 🔑 **Llaves a elección** | `/mapucraft llaves` | Elige qué llave quieres de las que tienes disponibles |
| 🏡 **Claims bonus** | `/mapucraft claims` | Suma claims extra a tu town |
| 🌟 **Nombre especial** | Vale de rango Especial | Elige tu nombre en mapudungun |

Las opciones de personalización se pagan con **dinero del servidor**. Estos son los precios actuales (pueden cambiar):

| Servicio | Precio |
|---|---:|
| Aplicar un modelo | $40.000 |
| Shulker de materiales | $65.000 |
| Cambiar el nombre | $60.000 |
| Escribir lore | $50.000 |
| Desencantar | $50.000 |

***

## 🎨 Modelos

Los modelos son skins 3D para tus armas y herramientas. Necesitas **tener el modelo** (se compra con MapuPoints en `/warp modelos`) y un **Ticket** del `/adminshop`. Solo funcionan con modelos del servidor, y **no puedes poner un modelo encima de otro**.

## ✍️ Nombre y lore

- Tienes **60 segundos** para escribir el texto por chat.
- El nombre admite hasta **64 caracteres**; el lore, hasta **8 líneas** de 64.
- Usa colores con `&` (por ejemplo `&6Mi espada`). Si una línea no lleva color, sale en blanco.

***

## 🐛 Spawners

Cuando compras un pack de spawners en la [tienda](../webs/tienda.md), el saldo se acredita solo. Luego usa `/mapucraft spawner` y elige el mob de cada spawner:

| Pack | Mobs que puedes elegir |
|---|---|
| **Normal** | Creeper, zombie, esqueleto, vaca, cerdo y pollo |
| **Premium** | Cualquier mob que pueda funcionar como spawner, excepto el **Ender Dragon**, el **Guardián Anciano** y el **Wither** |

## 🔑 Llaves a elección

Con `/mapucraft llaves` se abre un menú con las cajas disponibles y eliges la llave que quieres. Es una de las recompensas del [Battle Pass](battlepass.md).

## 🏡 Claims bonus

`/mapucraft claims` te pide **por chat el nombre de tu town**. Si el nombre lleva espacios, escríbelos con **guion bajo** (`Mi_Pueblo`). Los claims se suman a los de tu town.

***

## 🌟 Nombre especial

El **Vale Rango Especial** entrega sus recompensas y te deja elegir un **nombre en mapudungun** que se muestra como prefijo durante **30 días**. Los nombres disponibles son:

Ayewun · Colocolo · Galvarino · Kaikaivilu · Kolchau · Küyen · Liwen · Llampuzken · Llinki · Mawün · Millangeru · Nahuel · Newen · Ngendengun · Ngünechen · Nguru · Rayen · Spit · Chiway · Kultrunka · Lifko · Llanka · Pangi

***

## 📨 Para el staff y la tienda

Estas recompensas se entregan con comandos de consola (o desde Tebex y el [Battle Pass](battlepass.md)):

| Recompensa | Comando | Cómo la reclama el jugador |
|---|---|---|
| Spawners | `/mapucraft spawner dar <jugador> <normal\|premium> <cantidad>` | `/mapucraft spawner` abre el menú para elegir el mob |
| Llaves a elección | `/mapucraft llaves dar <jugador> <cantidad>` | `/mapucraft llaves` abre el menú para elegir la llave |
| Claims bonus | `/mapucraft claims dar <jugador> <cantidad>` | `/mapucraft claims` pide por chat el nombre de la town |
