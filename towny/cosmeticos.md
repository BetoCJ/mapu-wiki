# 🎨 Cosméticos

Mapucraft tiene un sistema completo de **cosméticos visuales** que no afectan el juego. Personaliza tu personaje con partículas, mascotas, ítems 3D exclusivos y más.

Accede al menú en `/warp cosmeticos`.

***

## 💎 MapuPoints y Coins

Los cosméticos y algunos ítems exclusivos se adquieren con **MapuPoints** o **Coins**, las monedas premium del servidor.

| | |
|---|---|
| **MapuPoints** | Se ganan votando en `/vote` (+1 por voto) y participando en eventos |
| **Coins** | Se obtienen canjeando MapuPoints (20 MP = 1 Coin) |
| **Conversión** | 20 MapuPoints = 1 Coin |

### 🔄 ¿Cómo canjear?

Dirígete al NPC de **Canje de Coins** en el spawn principal. Ahí puedes convertir tus MapuPoints acumulados en Coins y adquirir cosméticos o ítems exclusivos del Comerciante de Ítems.

***

## 🧊 Ítems Personalizados 3D

En `/warp personalizados` encontrarás ítems con modelos 3D exclusivos del servidor. Estos ítems tienen apariencias únicas creadas por el equipo de Mapucraft.

{% hint style="warning" %}
**Requieren Java Edition + Paquete de Recursos.** Al entrar al warp se te pedirá aceptar el texturepack. Si no lo aceptas, verás los ítems como objetos vanilla normales.
{% endhint %}

- Son cosméticos visuales — **no otorgan ventajas de juego**
- Al morir puedes **perder los ítems**, no son indestructibles
- ¿Quieres sugerir un modelo? Escribe en el canal **#modelos3d** del Discord

***

## 📜 Comandos

| Comando | Descripción |
|---|---|
| `/warp cosmeticos` | Ir a la tienda de cosméticos |
| `/warp personalizados` | Ver ítems 3D exclusivos |
| `/points balance` | Ver tus MapuPoints actuales |
| `/points pay [jugador] [cantidad]` | Transferir MapuPoints a otro jugador |

***

## 🐾 Mascotas — MyPet

Mapucraft usa el plugin **MyPet** para el sistema de mascotas. Puedes domesticar mobs del mundo y convertirlos en compañeros permanentes que te siguen, suben de nivel y pueden aprender habilidades.

***

### Cómo conseguir una mascota

Hay dos formas de obtener una mascota:

**1. Domesticar un mob en el mundo**

Usa una **correa (lead)** sobre un mob compatible mientras se cumplen sus requisitos de domesticación. Los requisitos varían según el tipo de mob:

| Requisito | Descripción |
|---|---|
| `LowHp` | El mob debe tener vida baja antes de poder engancharlo con la correa |
| `Tamed` | El mob ya debe estar domesticado previamente (ej. lobo, gato, caballo) |
| `HeartLinked` | El mob debe estar vinculado a un corazón (exclusivo del Creaking) |
| `UserCreated` | El mob debe ser creado por el jugador (ej. Golem de Hierro/Cobre construido) |
| `Impossible` | No se puede domesticar en el mundo (solo disponible en la tienda) |

**2. Comprar una mascota en la tienda**

Accede al NPC de mascotas en el servidor y compra directamente con la moneda del servidor. Esto permite conseguir mascotas que normalmente tienen requisitos difíciles o imposibles.

***

### Sistema de hambre

Las mascotas tienen un sistema de hambre activo. Si no las alimentas, su salud se reduce con el tiempo.

- El hambre disminuye cada **60 segundos**
- Cada vez que alimentas a tu mascota recupera **6 puntos de saturación**
- Si la saturación llega a 0, la mascota empieza a recibir **1 de daño por tick** (pasados 5 minutos de hambre extrema)
- El hambre puede **matar** a tu mascota si la descuidas completamente
- Puedes activar la opción de **alimentar desde tu inventario** automáticamente
- Cada mascota tiene su propia comida — consulta la tabla de tipos de mascota

***

### Límites por rango

El número de ranuras de mascotas que puedes tener activas depende de tu rango en el servidor. Puedes almacenar hasta **45 mascotas en total**, pero solo puedes tener activas las que tu rango permite.

| Rango | Ranuras activas |
|---|---|
| Winka | Sin acceso a mascotas |
| Che | 6 ranuras |
| KumeChe | 7 ranuras |
| Weupife | 8 ranuras |
| Machife | 10 ranuras |

El almacenamiento máximo es de **45 mascotas** por jugador (entre activas y guardadas).

***

### Árboles de habilidades

Al subir de nivel, tu mascota gana puntos de habilidad que puedes invertir en un árbol. Existen **5 árboles** disponibles. Solo puedes elegir uno por mascota (cambiar de árbol tiene un costo del 5% del nivel).

| Árbol | Icono | Mascotas compatibles | Habilidades principales |
|---|---|---|---|
| **Combat** | Hacha de piedra | Mobs hostiles y de combate (Zombie, Skeleton, Creeper, Enderman, Warden, Wolf, etc.) | Aumento de daño (+0.3/nivel hasta 20 niveles), aumento de vida (+2 HP/nivel hasta 100 niveles), espinas (reflejo de daño), knockback, mochila, control |
| **Utility** | Cofre trampa | Cualquier mascota (`*`) | Inventario grande (hasta +7 filas de mochila), aumento de vida, aumento de daño, recolección de items (pickup), veneno |
| **PvP** | Espada de diamante | Mobs hostiles y de combate (mismos que Combat) | Aumento de daño, sprint, ralentizar al enemigo, fuego, baliza (Resistance + Strength), aumento de vida, curación |
| **Ride** | Silla de montar | Monturas (Horse, Donkey, Mule, SkeletonHorse, ZombieHorse, Llama, TraderLlama, Camel, Strider, Pig) | Montura (velocidad +5%, salto +1.25), vuelo al nivel 10, ataque a distancia (bolas de nieve), inventario, recolección, sprint, espinas, baliza (Regeneration + WaterBreathing), aumento de vida |
| **Farm** | Libro escribible | Cualquier mascota (`*`) | Ataques cuerpo a cuerpo y a distancia, inventario (2 filas desde nivel 1), espinas, veneno, control, aumento de vida y daño, recolección |

Todos los árboles permiten hasta **nivel 100** de mascota. La habilidad de vida escala +2 HP por cada punto invertido, pudiendo llegar a +200 HP extra al máximo.

***

### Tipos de mascotas disponibles

Todas las mascotas listadas están disponibles en el servidor. La columna "Cómo domesticar" indica el requisito para engancharlas con una correa en el mundo (o si solo se obtienen en la tienda).

| Mob | HP base | Velocidad | Comida | Cómo domesticar |
|---|---|---|---|---|
| Allay | 10 | 0.34 | Manzana | Vida baja |
| Armadillo | 18 | 0.28 | Ojo de araña | Vida baja |
| Axolotl | 14 | 0.32 | Pez tropical | Vida baja |
| Abeja (Bee) | 6 | 0.34 | Flores variadas | Vida baja |
| Blaze | 24 | 0.30 | Pólvora | Vida baja |
| Bogged | 26 | 0.30 | Hueso | Vida baja |
| Breeze | 22 | 0.34 | Pólvora | Vida baja |
| Murciélago (Bat) | 8 | 0.40 | Ojo de araña | Vida baja |
| Camello (Camel) | 30 | 0.32 | Bacalao | Ya domesticado |
| Gato (Cat) | 14 | 0.35 | Bacalao | Ya domesticado |
| Araña de Cueva (CaveSpider) | 16 | 0.36 | Carne podrida | Vida baja |
| Pollo (Chicken) | 8 | 0.28 | Semillas de trigo | Vida baja |
| Bacalao (Cod) | 6 | 0.28 | Alga marina | Vida baja |
| Vaca (Cow) | 20 | 0.28 | Trigo | Vida baja |
| Gólem de Cobre (CopperGolem) | 35 | 0.25 | Lingote de cobre | Construido por el jugador |
| Creaking | 20 | 0.28 | Grumo de resina | Corazón vinculado |
| Creeper | 20 | 0.26 | Pólvora | Vida baja |
| Delfín (Dolphin) | 24 | 0.36 | Bacalao | Vida baja |
| Burro (Donkey) | 26 | 0.30 | Azúcar, trigo, manzana | Ya domesticado |
| Ahogado (Drowned) | 28 | 0.30 | Carne podrida | Vida baja |
| Guardián Anciano (ElderGuardian) | 45 | 0.25 | Azúcar | Vida baja |
| Dragón del End (EnderDragon) | 200 | 0.30 | Piedra del End | Solo tienda |
| Enderman | 30 | 0.32 | Arena de almas | Vida baja |
| Endermite | 10 | 0.32 | Azúcar | Vida baja |
| Evocador (Evoker) | 26 | 0.30 | Manzana | Vida baja |
| Zorro (Fox) | 14 | 0.35 | Bayas dulces | Vida baja |
| Rana (Frog) | 10 | 0.32 | Bola de slime | Vida baja |
| Ghast | 22 | 0.30 | Pólvora | Solo tienda |
| Gigante (Giant) | 60 | 0.22 | Carne podrida | Vida baja |
| Calamar Brillante (GlowSquid) | 10 | 0.28 | Bacalao | Vida baja |
| Cabra (Goat) | 24 | 0.32 | Trigo | Vida baja |
| Guardián (Guardian) | 28 | 0.30 | Azúcar | Vida baja |
| Hoglin | 34 | 0.32 | Hongo carmesí | Vida baja |
| Caballo (Horse) | 28 | 0.40 | Azúcar, trigo, manzana | Ya domesticado |
| Husk | 24 | 0.28 | Carne podrida | Vida baja |
| Ilusionista (Illusioner) | 24 | 0.30 | Manzana | Vida baja |
| Gólem de Hierro (IronGolem) | 45 | 0.25 | Lingote de hierro | Construido por el jugador |
| Llama (Llama) | 24 | 0.28 | Trigo | Ya domesticada |
| Cubo de Magma (MagmaCube) | 18 | 0.30 | Redstone | Vida baja |
| Mooshroom | 20 | 0.28 | Trigo | Vida baja |
| Mula (Mule) | 26 | 0.32 | Azúcar, trigo, manzana | Ya domesticada |
| Ocelote (Ocelot) | 14 | 0.38 | Bacalao, salmón | Vida baja |
| Panda | 24 | 0.26 | Bambú | Vida baja |
| Loro (Parrot) | 6 | 0.35 | Galleta, bayas dulces | Ya domesticado |
| Phantom | 16 | 0.35 | Carne podrida | Vida baja |
| Cerdo (Pig) | 18 | 0.30 | Zanahoria | Vida baja |
| Piglin | 26 | 0.30 | Pepita de oro | Vida baja |
| Piglin Bruto (PiglinBrute) | 36 | 0.30 | Pepita de oro | Vida baja |
| Saqueador (Pillager) | 28 | 0.30 | Manzana | Vida baja |
| Oso Polar (PolarBear) | 30 | 0.30 | Bacalao | Vida baja |
| Pez Globo (Pufferfish) | 6 | 0.28 | Alga marina | Vida baja |
| Conejo (Rabbit) | 6 | 0.40 | Zanahoria | Vida baja |
| Devastador (Ravager) | 50 | 0.28 | Carne de res, cordero | Vida baja |
| Salmón (Salmon) | 6 | 0.28 | Alga marina | Vida baja |
| Oveja (Sheep) | 16 | 0.28 | Trigo | Vida baja |
| Pez Plateado (Silverfish) | 8 | 0.40 | Azúcar | Vida baja |
| Esqueleto (Skeleton) | 24 | 0.30 | Hueso | Vida baja |
| Caballo Esqueleto (SkeletonHorse) | 24 | 0.38 | Hueso | Vida baja |
| Slime | 16 | 0.30 | Azúcar | Vida baja |
| Sniffer | 22 | 0.26 | Semillas de flor antorcha | Ya domesticado |
| Muñeco de Nieve (Snowman) | 14 | 0.26 | Zanahoria, bola de nieve | Vida baja |
| Araña (Spider) | 22 | 0.34 | Carne podrida | Vida baja |
| Calamar (Squid) | 10 | 0.28 | Bacalao | Vida baja |
| Descarriado (Stray) | 24 | 0.28 | Hueso | Vida baja |
| Caminante (Strider) | 22 | 0.30 | Hueso | Vida baja |
| Renacuajo (Tadpole) | 4 | 0.24 | Bola de slime | Vida baja |
| Llama Comerciante (TraderLlama) | 24 | 0.28 | Trigo | Ya domesticada |
| Pez Tropical (TropicalFish) | 6 | 0.28 | Alga marina | Vida baja |
| Tortuga (Turtle) | 20 | 0.22 | Alga marina | Vida baja |
| Vex | 12 | 0.38 | Manzana | Vida baja |
| Aldeano (Villager) | 18 | 0.28 | Manzana | Vida baja |
| Vindicador (Vindicator) | 32 | 0.30 | Manzana | Vida baja |
| Comerciante Errante (WanderingTrader) | 18 | 0.28 | Manzana | Vida baja |
| Warden | 150 | 0.28 | Hueso | Vida baja |
| Bruja (Witch) | 26 | 0.30 | Estofado de champiñones | Vida baja |
| Wither | 150 | 0.30 | Hueso | Solo tienda |
| Esqueleto Wither (WitherSkeleton) | 34 | 0.30 | Hueso | Vida baja |
| Lobo (Wolf) | 26 | 0.34 | Carne de res, cordero | Ya domesticado |
| Zoglin | 34 | 0.32 | Hongo carmesí | Vida baja |
| Zombi (Zombie) | 24 | 0.28 | Carne podrida | Vida baja |
| Caballo Zombi (ZombieHorse) | 24 | 0.30 | Carne podrida | Vida baja |
| Piglin Zombificado (ZombifiedPiglin) | 24 | 0.30 | Carne podrida | Vida baja |
| Aldeano Zombi (ZombieVillager) | 24 | 0.28 | Carne podrida | Vida baja |

***

### Comandos de mascotas

| Comando | Descripción |
|---|---|
| `/petinfo` | Ver información de tu mascota activa (nivel, HP, hambre, árbol de habilidades) |
| `/petname [nombre]` | Ponerle nombre a tu mascota (máximo 32 caracteres) |
| `/petinv` | Abrir el inventario/mochila de tu mascota (si tiene la habilidad Backpack) |
| `/petskill` | Ver y gestionar el árbol de habilidades de tu mascota |
| `/petoption` | Configurar opciones de comportamiento de tu mascota |
| `/petcall` | Llamar a tu mascota si se alejó o desapareció |
| `/petsendaway` | Enviar a tu mascota de vuelta (ocultarla temporalmente) |
| `/petrelease` | Liberar a tu mascota permanentemente (¡cuidado, es irreversible!) |
| `/petstore` | Guardar tu mascota activa en el almacenamiento |
| `/petswitch` | Cambiar entre tus mascotas almacenadas |
| `/petshop` | Abrir la tienda de mascotas del servidor |
