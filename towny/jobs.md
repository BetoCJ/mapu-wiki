# 💼 Jobs

El sistema de **Jobs** (empleos) te permite ganar dinero realizando distintas actividades en el servidor. Elige el trabajo que más se adapte a tu estilo de juego y sube de nivel para aumentar tus ganancias.

> Puedes tener hasta **3 trabajos** activos al mismo tiempo. El nivel máximo de cada trabajo es **200**.

***

## 💼 Trabajos disponibles

| Trabajo | Actividad principal |
|---|---|
| ⛏️ **Minero** | Minar minerales y menas |
| 🌾 **Granjero** | Cultivar y cosechar |
| 🪵 **Leñador** | Talar y plantar árboles |
| 🏹 **Cazador** | Matar animales y monstruos |
| 🎣 **Pescador** | Pescar |
| 🔨 **Constructor** | Construir estructuras |
| 🧪 **Cervecero** | Preparar pociones |
| ⚒️ **Artesano** | Fabricar ítems en mesa de crafteo |
| 🪣 **Excavador** | Terraformar el mundo |
| ✨ **Encantador** | Encantar armas y herramientas |
| 🗺️ **Explorador** | Explorar el mapa |
| ⚔️ **Herrero de Armas** | Fabricar y reparar armas |

***

## 📜 Comandos

| Comando | Descripción |
|---|---|
| `/jobs browse` | Ver todos los trabajos disponibles |
| `/jobs join [trabajo]` | Unirte a un trabajo |
| `/jobs leave [trabajo]` | Abandonar un trabajo |
| `/jobs info [trabajo]` | Ver información y pagos de un trabajo |
| `/jobs stats` | Ver tus estadísticas y niveles |
| `/jobs top` | Ver el ranking de niveles |
| `/jobs quests` | Ver tus misiones diarias activas |
| `/jobs toggle` | Activar o desactivar el chat del trabajo |

***

## 📈 Sistema de niveles

Cada trabajo tiene **nivel máximo 200**. Al realizar acciones del trabajo ganas experiencia de ese trabajo, lo que sube tu nivel. A mayor nivel, mayor ingreso por acción.

### Progresión de ingresos

Los pagos por acción **aumentan con el nivel** mediante la siguiente ecuación (igual en todos los trabajos):

```
ingreso = baseincome + (baseincome * (nivel-1) * 0.005)
```

Esto significa que el pago sube aproximadamente un **0.5% por nivel** sobre el ingreso base. Al llegar al nivel 200 ganarás cerca del doble que al nivel 1.

### Penalización por múltiples trabajos

Tener más de un trabajo activo aplica una pequeña penalización sobre el ingreso:

```
ingreso final = ingreso * (1 - (numjobs - 1) * 0.03)
```

Con 2 trabajos recibes un **3% menos** por trabajo. Con 3 trabajos un **6% menos** por trabajo.

### Recompensas por nivel

Todos los trabajos otorgan una recompensa en dinero cada 5 niveles:

| Nivel | Recompensa |
|---|---|
| 5 | $1,000 |
| 10 | $2,000 |
| 15 | $3,000 |
| 20 | $4,000 |
| 25 | $5,000 |
| 30 | $6,000 |
| 35 | $7,000 |
| 40 | $8,000 |
| 45 | $9,000 |
| 50 | $10,000 |
| ... | +$1,000 por cada 5 niveles |
| 200 | $40,000 |

Al alcanzar el **nivel 200** (nivel máximo) también recibes una recompensa especial de **$5,000** adicionales y se anuncia en el servidor.

{% hint style="info" %}
El pago de recompensas por nivel es automático. No necesitas reclamar nada.
{% endhint %}

***

## 📅 Misiones diarias

Cada trabajo tiene misiones diarias que puedes completar para ganar dinero extra. Las misiones se reinician todos los días a las **4:00 AM**. Puedes saltarte una misión por día con `/jobs quests`.

La cantidad de misiones diarias varía por trabajo:

| Trabajo | Misiones diarias máximas |
|---|---|
| Minero | 1 |
| Granjero | 3 |
| Leñador | 1 |
| Cazador | 1 |
| Pescador | 3 |
| Constructor | 1 |
| Cervecero | 1 |
| Artesano | 1 |
| Excavador | 1 |
| Encantador | 1 |
| Explorador | 1 |
| Herrero de Armas | 1 |

***

## ⛏️ Minero

Gana dinero minando minerales y menas. Es uno de los trabajos más completos en variedad de bloques pagados.

### Pagos por acción (ingreso base)

| Bloque | Ingreso base |
|---|---|
| Piedra, Granito, Diorita, Andesita | $0.375 |
| Pizarra profunda | $0.463 |
| Sandstone | $0.115 |
| Carbón | $1.725 |
| Carbón profundo | $1.300 |
| Cobre | $1.012 |
| Cobre profundo | $1.588 |
| Hierro | $1.013 |
| Hierro profundo | $1.588 |
| Oro | $1.275 |
| Oro profundo | $1.450 |
| Lapislázuli | $1.313 |
| Lapislázuli profundo | $1.888 |
| Redstone | $1.438 |
| Redstone profundo | $1.013 |
| Cuarzo del Nether | $1.438 |
| Diamante | $1.250 |
| Diamante profundo | $1.875 |
| Esmeralda | $1.225 |
| Esmeralda profunda | $1.263 |
| Obsidiana | $2.875 |
| Prismarina | $1.438 |
| Netherrack | $0.058 |

{% hint style="info" %}
Los minerales de pizarra profunda suelen pagar más que sus equivalentes normales.
{% endhint %}

***

## 🌾 Granjero

Gana dinero cosechando cultivos maduros, recogiendo flores, frutos y plantando semillas.

### Pagos por acción (ingreso base)

**Cosechar (Break):**

| Cultivo / Bloque | Ingreso base |
|---|---|
| Trigo maduro | $1.00 |
| Remolacha madura | $1.00 |
| Planta de chorus / flor | $1.00 |
| Cacao maduro | $2.00 |
| Zanahoria madura | $0.50 |
| Patata madura | $0.50 |
| Calabaza | $0.30 |
| Melón | $0.30 |
| Caña de azúcar | $0.10 |
| Seta (roja o marrón) | $0.50 |
| Flor de almohadilla, amapola, orquídea... | $1.00 |
| Algas / plantas acuáticas | $0.50–$1.00 |
| Nether wart | $0.50 |
| Cactus | $0.50 |

**Plantar (Place):**

| Semilla / Cultivo | Ingreso base |
|---|---|
| Trigo, Zanahoria, Patata, Remolacha | $0.50 |
| Cacao | $0.50 |
| Tallo de calabaza / melón | $0.50 |

**Recolectar (Collect):**

| Ítem | Ingreso base |
|---|---|
| Bayas dulces (maduras) | $0.30 |
| Bayas luminosas | $0.30 |
| Harina de hueso | $1.00 |
| Botella de miel | $1.50 |
| Panal de abeja | $1.50 |

{% hint style="warning" %}
Plantar caña de azúcar resta $1.00. La caña se cosecha, no se planta para ganar.
{% endhint %}

***

## 🪵 Leñador

Gana dinero talando troncos de árboles.

### Pagos por acción (ingreso base)

| Bloque | Ingreso base |
|---|---|
| Tronco (roble, abeto, abedul, jungla, acacia, roble oscuro, cerezo, pálido) | $0.375 |
| Tronco descortezado (cualquier variante) | $0.288 |

{% hint style="info" %}
Los troncos descortezados pagan ligeramente menos que los normales.
{% endhint %}

***

## 🏹 Cazador

Gana dinero matando mobs. Incluye tanto animales pacíficos como monstruos hostiles y jefes.

### Pagos por acción (ingreso base)

| Mob | Ingreso base |
|---|---|
| Pollo, Cerdo, Oveja, Vaca Seta | $0.30 |
| Vaca | $0.40 |
| Lobo | $0.60 |
| Enderman, Fantasma, Husk, Zombie Ahogado | $0.30 |
| Zombie, Esqueleto, Araña | $0.60 |
| Creeper | $0.90 |
| Blaze, Araña de cueva, Pez de plata, Muñeco de nieve | $0.20–$0.60 |
| Calamar, Conejo, Guardian | $0.20 |
| Pillager, Vindicator, Evocador, Ilusionista, Devastador, Bruja | $1.20 |
| Ghast, Golem de Hierro, Guardian Anciano | $1.80 |
| Guardián del Fin (Warden) | $19.00 |
| Wither | $26.00 |
| Dragón del End | $300.00 |
| Jugador | $1.80 |

{% hint style="warning" %}
El pago del Cazador escala un **0.3% por nivel** (ligeramente menor que otros trabajos). Con múltiples trabajos la penalización es de 2% por trabajo adicional.
{% endhint %}

***

## 🎣 Pescador

Gana dinero pescando en ríos y océanos.

### Pagos por acción (ingreso base)

| Pez | Ingreso base |
|---|---|
| Bacalao (Cod) | $1.75 |
| Salmón | $3.60 |
| Pez tropical | $3.75 |
| Pez globo | $5.75 |

{% hint style="info" %}
El Pescador tiene 3 misiones diarias disponibles, más que la mayoría de trabajos.
{% endhint %}

***

## 🔨 Constructor

Gana dinero colocando bloques para construir estructuras.

### Pagos por acción (ingreso base, Place)

| Bloque | Ingreso base |
|---|---|
| Piedra, Toba, Bloque de nieve, Andesita, Granito, Diorita | $1.15 |
| Ladrillos de piedra, Adoquín | $0.575 |
| Tierra, Hierba, Arena, Grava | $0.15 |

{% hint style="info" %}
El Constructor tiene una larga lista de bloques pagados, incluyendo madera, ladrillo de nether, bloques de cuarzo, corales, bambú y mucho más. Usa `/jobs info Constructor` en el juego para ver la lista completa.
{% endhint %}

***

## 🧪 Cervecero

Gana dinero preparando pociones en el soporte de elaboración.

### Pagos por acción (ingreso base, Brew)

| Ingrediente | Ingreso base |
|---|---|
| Verruga del Nether | $8.60 |
| Redstone | $8.60 |
| Pólvora | $8.60 |
| Azúcar | $10.75 |
| Polvo de piedra luminosa | $12.90 |
| Ojo de araña | $18.05 |
| Crema de magma | $18.20 |
| Ojo de araña fermentado | $18.20 |
| Rebanada de melón brillante | $18.20 |
| Piel de tortuga | $21.50 |
| Membrana de Phantom | $21.50 |
| Zanahoria dorada | $22.50 |
| Polvo de Blaze | $22.50 |
| Lágrima de Ghast | $30.70 |
| Pie de conejo | $30.10 |
| Aliento de Dragón | $43.00 |

***

## ⚒️ Artesano

Gana dinero fabricando ítems en la mesa de crafteo y fundiendo en el horno.

### Pagos por acción (ingreso base, Craft)

| Ítem | Ingreso base |
|---|---|
| Palo | $0.05 |
| Mesa de crafteo | $0.25 |
| Vidrio (sin teñir) | $0.05 |
| Vidrio teñido | $0.10 |
| Cofre | $0.50 |
| Libro | $0.40 |
| Horno | $0.40 |
| Cama | $1.00 |
| Vagoneta de presión, Vagoneta | $1.00 |
| Escalera de bloques | $1.00 |
| Espadín de madera | $0.05 |
| Carril impulsado / detector / activador | $1.50–$2.00 |
| Dispensador | $1.50 |
| Vagoneta trampa | $0.60 |
| Soporte de elaboración | $1.00 |
| Caldera | $2.50 |
| Tolva | $2.50 |
| Reloj | $2.50 |
| Linterna del mar | $2.50 |
| Pastel | $3.00 |
| Yunque | $7.50 |
| Mesa de encantamientos | $10.00 |
| Baliza | $25.00 |
| Tocadiscos | $4.00 |

**Fundir (Smelt):** Solo recompensa por fundir pollo cocinado ($1.00).

***

## 🪣 Excavador

Gana dinero rompiendo bloques de tierra, arena y materiales similares al terraformar.

### Pagos por acción (ingreso base, Break)

| Bloque | Ingreso base |
|---|---|
| Tierra | $0.23 |
| Bloque de hierba | $0.288 |
| Grava | $0.305 |
| Arena, Arena del Alma, Suelo del Alma | $0.345 |
| Arcilla, Arena roja, Tierra gruesa | $0.805 |

***

## ✨ Encantador

Gana dinero encantando armas, herramientas y armaduras en la mesa de encantamientos o con libros.

### Pagos por acción (ingreso base, Enchant)

| Ítem encantado | Ingreso base |
|---|---|
| Espada de madera | $0.575 |
| Espada de hierro | $1.15 |
| Espada de oro | $1.725 |
| Espada de diamante | $4.025 |
| Pico / Hacha de diamante | $4.60 |
| Peto de hierro | $1.725 |
| Peto de oro | $2.30 |
| Peto de diamante | $5.75 |
| Leggings de diamante | $5.75 |

**Encantamientos específicos también pagan:**

| Encantamiento | Ingreso base |
|---|---|
| Eficiencia I | $0.288 |
| Eficiencia II | $0.575 |
| Eficiencia III | $0.863 |
| Eficiencia IV | $1.15 |
| Irrompibilidad I | $0.288 |
| Irrompibilidad II | $0.575 |
| Irrompibilidad III | $0.863 |
| Toque de seda | $2.30 |
| Botín I | $1.725 |

***

## 🗺️ Explorador

Gana dinero descubriendo chunks nuevos del mapa que aún no has explorado.

### Pagos por acción (ingreso base, Explore)

El pago depende de cuántos jugadores ya exploraron ese chunk:

| Jugadores que ya exploraron el chunk | Ingreso base |
|---|---|
| 1° en explorar | $1.30 |
| 2° en explorar | $1.00 |
| 3° en explorar | $0.85 |
| 4° en explorar | $0.575 |
| 5° en explorar | $0.115 |

{% hint style="info" %}
Los chunks explorados se guardan en la base de datos y persisten entre reinicios del servidor. Cada chunk solo puede ser "nuevo" una vez por jugador, por lo que el ingreso disminuye conforme más personas exploran las mismas zonas.
{% endhint %}

***

## ⚔️ Herrero de Armas

Gana dinero fabricando y reparando armas y armaduras.

### Pagos por acción (ingreso base)

**Fabricar (Craft):**

| Ítem | Ingreso base |
|---|---|
| Espada de madera | $0.575 |
| Espada de hierro | $2.30 |
| Espada de oro | $3.45 |
| Espada de diamante | $4.60 |
| Peto de cuero | $2.30 |
| Peto de hierro | $2.20 |
| Peto de oro | $6.80 |
| Peto de diamante | $6.40 |
| Leggings de cuero | $2.01 |
| Leggings de hierro | $4.05 |
| Leggings de oro | $6.08 |
| Leggings de diamante | $6.10 |
| Casco de tortuga | $6.50 |
| Pico de diamante | $3.90 |
| Hacha de diamante | $3.90 |

**Reparar (Repair) en yunque:**

| Arma | Ingreso base |
|---|---|
| Espada de madera | $0.575 |
| Espada de hierro | $1.15 |
| Espada de oro | $1.725 |
| Espada de diamante | $1.30 |

**Fundir (Smelt):**

| Ítem | Ingreso base |
|---|---|
| Lingote de hierro | $0.748 |
| Lingote de oro | $1.875 |
| Diamante (fundido) | $2.025 |
