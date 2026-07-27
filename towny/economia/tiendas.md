# 🛒 Tiendas y Mercado

Mapucraft cuenta con varios sistemas para que los jugadores compren y vendan ítems entre sí. Cada uno tiene su propio propósito y ventajas.

***

## 🏬 QuickShop — Tiendas físicas

El sistema **QuickShop** permite crear tiendas físicas en el mundo colocando un cofre. Cualquier jugador puede montarse su propia tienda y vender ítems a quienes pasen por ahí.

### 🛍️ ¿Cómo comprar?

1. Encuentra una tienda en el mundo o en el mercado principal
2. Haz **clic derecho** sobre el cartel de la tienda
3. Confirma la compra en el chat

### 🏗️ ¿Cómo crear una tienda?

1. Coloca un cofre con el ítem que quieres vender
2. Sostén el ítem en tu mano principal
3. Haz **clic derecho** sobre el cofre
4. Sigue las instrucciones del chat para fijar precio y cantidad

### ℹ️ Información

|                                   |                  |
| ********************************* | ***************- |
| **Plugin**                        | QuickShop-Hikari |
| **Costo de crear tienda**         | $1,000           |
| **Límite de tiendas por jugador** | 50               |
| **Mercado principal**             | `/warp mercado`  |

### 📜 Comandos

| Comando           | Descripción                                  |
| ***************-- | ******************************************-- |
| `/qs find [ítem]` | Buscar tiendas que venden un ítem específico |

{% hint style="info" %}
El mercado principal está en `/warp comercio`, donde puedes alquilar un local para instalar tus tiendas.
{% endhint %}

***

## 🔨 Auction House — /ah

El **Auction House** es una casa de subastas global donde cualquier jugador puede publicar ítems a la venta y cualquier otro puede comprarlos, sin importar dónde estén en el servidor.

### ⚙️ ¿Cómo funciona?

- Usa `/ah` para abrir el menú de la casa de subastas
- Desde ahí puedes explorar todos los ítems publicados por otros jugadores y comprar lo que necesites
- Para vender, sostén el ítem en la mano y escribe el precio en el comando

### 📜 Comandos

| Comando             | Descripción                         |
| ******************- | *********************************-- |
| `/ah`               | Abrir la casa de subastas           |
| `/ah sell [precio]` | Publicar el ítem en mano a la venta |
| `/ah cancel`        | Cancelar tus publicaciones activas  |
| `/ah expired`       | Recoger ítems que no se vendieron   |

***

## 🏪 Mercado del Servidor — /mercado

El `/mercado` (también `/market`) es el **mercado oficial del servidor**, administrado por el sistema NasCraft. A diferencia de las tiendas de jugadores, aquí compras y vendes directamente con el servidor, sin depender de que otro jugador tenga stock.

### Como funcionan los precios

El mercado usa un sistema de **precios dinamicos**: el precio de cada item cambia en funcion de la oferta y la demanda de todos los jugadores del servidor.

- **Si muchos compran** un item, su precio sube.
- **Si muchos venden** un item, su precio baja.
- **El precio nunca es fijo.** Cada 60 segundos el sistema aplica una pequeña variacion aleatoria (llamada "ruido") que hace que los precios fluctuen ligeramente incluso sin actividad de jugadores.

Esto significa que especializarte en un recurso y venderlo constantemente acabara bajando su precio en el mercado. Es una economia viva que responde a lo que hacen los jugadores.

#### Impuestos

Todas las transacciones llevan una pequeña comision:

| Accion  | Impuesto por defecto |
| ------- | -------------------- |
| Comprar | 3%                   |
| Vender  | 8%                   |

Algunos items pueden tener impuestos diferentes configurados de forma individual.

### Categorias disponibles

El mercado esta organizado en 17 categorias:

| # | Categoria | Ejemplos de items |
| - | --------- | ----------------- |
| 1 | Edad de Piedra | Adoquin, piedra, andesita, diorita, granito |
| 2 | En las profundidades | Deepslate, amatista, sculk, obsidiana |
| 3 | Aun mas profundo | Basalto, piedra negra, lagrima de ghast, vara de blaze, cuarzo |
| 4 | El Fin | Piedra del Fin, bloque de purpura, concha de shulker, perla de ender |
| 5 | Mojado | Arena, fragmentos de prisma, bacalao, salmon, corazon del mar, corales |
| 6 | Tecnologia | Redstone, lampara de redstone, TNT, pistones, sensor sculk |
| 7 | En los bosques | Troncos (roble, abedul, pino, jungla, acacia, roble oscuro, manglar, cerezo), hongos |
| 8 | Botin | Carne podrida, huesos, flechas, hilo, polvora, membrana fantasma |
| 9 | Valiosos | Diamante, esmeralda, estrella del Nether, manzana dorada |
| 10 | Combustible | Carbon, bloque de alga seca |
| 11 | Lingotes y Ladrillos | Hierro bruto, hierro, cobre, oro, netherita, lapislazuli, ladrillo |
| 12 | Agricultura | Manzana, zanahoria, papa, remolacha, trigo, calabaza, sandia, cana de azucar, bambu |
| 13 | Ganaderia | Carne de vaca, cerdo, oveja, pollo, conejo, huevo, cuero |
| 14 | Tierra y Otros | Tierra, grava, arena roja, bloque de cesped, lana blanca, barro, arcilla, nieve, hielo |
| 15 | Decoracion | Terracota (todos los colores), farol, farol de alma |
| 16 | Concretos | Concreto en los 16 colores (tambien en polvo) |
| 17 | Huevos de Mobs | Huevos de spawn de mas de 60 tipos de mobs |

### Precios de referencia

Los precios cambian con el tiempo, pero estos son los valores iniciales de algunos items representativos:

| Item | Precio inicial |
| ---- | -------------- |
| Cobblestone | $0.05 |
| Madera (cualquier tipo) | $1.00 |
| Carbon | $2.00 |
| Redstone | $2.00 |
| Hierro bruto | $5.00 |
| Diamante | $30.00 |
| Oro bruto | $20.00 |
| Obsidiana | $100.00 |
| Manzana dorada | $100.00 |
| Corazon del mar | $600.00 |
| Huevo de mob comun (ej. zombie) | $1,000.00 |
| Huevo de mob medio (ej. enderman) | $5,000.00 |
| Huevo de mob exotico (ej. Blaze) | $10,000.00 |
| Huevo de jefe (Warden, Guardián Anciano) | $20,000.00 |

> Los precios mostrados son los valores de partida. El precio real en el momento de tu compra o venta puede ser mayor o menor dependiendo de la actividad reciente del mercado.

### Limites del mercado

| Parametro | Valor |
| --------- | ----- |
| Precio maximo de un item | $500,000 |
| Precio minimo de un item | $0.01 |
| Historial de transacciones guardado | 60 dias |

### Comandos

| Comando      | Descripcion                                |
| ------------ | ------------------------------------------ |
| `/mercado`   | Abrir el menu del mercado del servidor     |
| `/market`    | Alias del mismo comando                    |
| `/sell`      | Menu rapido para vender items              |
| `/nsellall`  | Vender todos los items del inventario que admita el mercado |
| `/nsellhand` | Vender el item que tienes en la mano       |
| `/nalerts`   | Gestionar alertas de precio                |
