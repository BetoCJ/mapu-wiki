# 🌱 PyroFarming

**PyroFarming** es el sistema de agricultura personalizada del servidor. Cultiva más de **20 plantas únicas** y **9 arbustos** usando **Growstations** (estaciones de cultivo), vende tus cosechas y sube de nivel para desbloquear cultivos más valiosos.

***

## ⚙️ ¿Cómo funciona?

1. Consigue una **Growstation** (crafteable o comprable en `/farm shop`)
2. Colócala en el suelo y plántale una semilla
3. La planta crece automáticamente, incluso cuando estás desconectado
4. Cosecha cuando esté lista y vende en `/farm shop`
5. Gana **XP de farming** y **Elysium** (moneda del plugin) con cada cosecha
6. Sube de nivel para desbloquear plantas y arbustos más valiosos

Abre el menú principal con `/farm` o haciendo **Shift + clic** con una azada.

***

## 🌿 Growstation

La Growstation es la "maceta especial" donde crecen las plantas. Se craftea así:

```
S S S
S M S
S S S
```

`S` = Semilla de trigo | `M` = Maceta de flores

Las Growstations **no son destruidas por explosiones ni pistones**. Para recogerla, agáchate y rompe el bloque.

***

## 🌾 Plantas

Las plantas se desbloquean según tu nivel de farming. Cada una tiene un tiempo de crecimiento y precio de venta diferente.

| Nivel requerido | Planta |
|---|---|
| 0 | Lechuga, Cebolla, Pepino |
| 5 | Guisantes |
| 7 | Tomate |
| 10 | Pimientos |
| 12 | Calabacita |
| 15 | Ajo |
| 18 | Glicinia Helada |
| 20 | Calabacín, Wasabi |
| 25 | Chile, Flor Vixen |
| 30 | Brócoli |
| 35 | Lirio Acuático, Flor Lunar Akari |
| 38 | Repollo |
| 40 | Pluma de Lava |
| 45 | Flor del Infierno |
| 50 | Iris Piroblaze, Venus Atrapamoscas |
| 55 | Alma Helada, Flor Infernal |
| 60 | Tubérculo Sombrío |
| 70 | Corazón del Vacío |
| 80 | Orquídea Abisal |

Las plantas de nivel alto (como la Orquídea Abisal) pueden producir múltiples ítems cosechables con precios superiores a **$4,000** por unidad.

***

## 🫐 Arbustos

Los arbustos son plantas especiales que crecen directamente en el suelo. También se desbloquean por nivel.

| Nivel requerido | Arbusto |
|---|---|
| 0 | Arbusto de Mora |
| 5 | Arbusto de Fresa |
| 10 | Arbusto de Arándano |
| 20 | Arbusto de Frambuesa |
| 30 | Arbusto de Piña |
| 40 | Arbusto de Baya Fénix |
| 45 | Arbusto Destello Solar |
| 50 | Arbusto de Baya Trueno |
| 65 | Arbusto Klaxosaur |

Para recoger un arbusto, agáchate y rompe el bloque.

***

## 🌡️ Sistema de Temperatura

Cada Growstation tiene una **temperatura** y un **entorno** determinados por el bioma donde está colocada. Si la planta plantada requiere condiciones distintas, no crecerá y verás el aviso *"La Temperatura de la Growstation no es compatible con esta planta"* al revisar la Growstation.

### Escala de temperaturas

Las temperaturas van de más fría a más caliente:

| Temperatura | Tipo |
|---|---|
| FREEZING | Congelante |
| GLACIAL | Glacial |
| COLD | Fría |
| NORMAL | Normal/Templada |
| WARM | Cálida |
| HOT | Caliente |
| BOILING | Hirviente |
| ANY | Cualquier temperatura |

Cada bioma en el juego tiene asignada una temperatura. Usa `/farm temp` para ver la temperatura del bioma donde estás parado. También puedes consultar la temperatura de un bioma específico con `/farm temp <nombre_del_bioma>`.

### Temperamento

Además de la temperatura, cada planta tiene un **temperamento** que afecta qué tan exigente es con sus condiciones de crecimiento:

| Temperamento | Descripción |
|---|---|
| FRIENDLY | Tolerante, puede crecer en condiciones ligeramente diferentes a las ideales |
| NORMAL | Tolerancia estándar |
| AGGRESSIVE | Exigente, requiere condiciones muy precisas para crecer |

### Modificar la temperatura con el Compostador

Si el bioma donde tienes tus Growstations no tiene la temperatura o el entorno correcto, puedes colocar **ítems especiales** cerca de ellas para ajustar sus condiciones.

Estos ítems se fabrican abriendo el **menú del Compostador**: haz clic derecho en un **Compostador** mientras tienes una **azada** en la mano. Verás una cuadrícula con todos los ítems disponibles, su receta y el nivel requerido para fabricarlos.

#### Ítems de temperatura — Calentar

| Ítem | Efecto | Rango | Nivel requerido |
|---|---|---|---|
| Lámpara de Lava | +1 Temperatura | 5 bloques | 25 |
| Orbe de Pyrotheum | +3 Temperatura | 4 bloques | 40 |
| Corazón de Belfegor | +5 Temperatura | 3 bloques | 55 |

**Recetas:**

- **Lámpara de Lava**: 1x Cubo de Lava, 10x Polvo de Blaze, 8x Tomate, 1x Jalapeño
- **Orbe de Pyrotheum**: 2x Cubo de Lava, 16x Bloque de Magma, 4x Fragmento de Netherita, 64x Ion de Pluma de Lava, 4x Anión de Pluma de Lava
- **Corazón de Belfegor**: 3x Cubo de Lava, 2x Cráneo de Esqueleto Wither, 10x Hongo Carmesí, 1x Bloque de Netherita, 8x Lágrimas de Lilith, 1x Zoide de Pluma de Lava

#### Ítems de temperatura — Enfriar

| Ítem | Efecto | Rango | Nivel requerido |
|---|---|---|---|
| Ventilador Industrial | -1 Temperatura | 5 bloques | 25 |
| Fuego Fatuo Bajo Cero | -3 Temperatura | 4 bloques | 40 |
| Vasija de Bóreas | -5 Temperatura | 3 bloques | 55 |

**Recetas:**

- **Ventilador Industrial**: 32x Lingote de Hierro, 1x Cubo de Agua, 256x Hielo, 64x Glicinia Helada, 3x Pimiento Rojo
- **Fuego Fatuo Bajo Cero**: 48x Lingote de Hierro, 2x Cubo de Agua, 256x Hielo Compacto, 128x Glicinia Helada, 48x Wasabi
- **Vasija de Bóreas**: 64x Lingote de Hierro, 3x Cubo de Agua, 256x Hielo Azul, 16x Diamante, 16x Ojo de Ender, 192x Glicinia Helada, 2x Fénix de Hielo

#### Ítems de entorno

Algunas plantas requieren un entorno específico (Overworld, Nether o The End). Estos orbes ajustan el entorno de las Growstations cercanas:

| Ítem | Entorno | Rango | Nivel requerido | Receta |
|---|---|---|---|---|
| Orbe del Overworld | Overworld | 10 bloques | 50 | 16x Diamante, 32x Tubérculo Sombrío Tenue |
| Orbe del Nether | Nether | 10 bloques | 50 | 32x Lingote de Oro, 8x Tubérculo Sombrío Brillante, 2x Lágrimas de Lilith |
| Orbe del End | The End | 10 bloques | 50 | 6x Lingote de Netherita, 3x Tubérculo Sombrío Radiante |

#### Ítems de velocidad de crecimiento

| Ítem | Bono | Rango | Nivel requerido | Receta |
|---|---|---|---|---|
| Gólem de Agua Básico | +4% velocidad | 10 bloques | 30 | 64x Lingote de Hierro, 16x Lirio de Agua, 24x Lirio Brillante |
| Gólem de Agua Intermedio | +8% velocidad | 10 bloques | 50 | 64x Lingote de Hierro, 32x Lirio de Agua, 16x Lirio Mágico |
| Gólem de Agua Avanzado | +12% velocidad | 10 bloques | 70 | 64x Lingote de Hierro, 64x Lirio de Agua, 4x Lirio de Cristal |

{% hint style="info" %}
Los ítems colocados cerca de las Growstations tienen efecto sobre **todas** las Growstations dentro de su rango. Para fabricarlos, recuerda que varios requieren plantas de niveles altos como ingredientes, así que úsalos como objetivo de progresión.
{% endhint %}

***

## 🌳 Árbol de Habilidades

Al nivel 25 puedes craftear un **Archivo de Habilidades** que desbloquea el árbol de habilidades de farming. Se craftea con lechugas, chiles y un Atril.

El árbol tiene 4 rangos que mejoran tus cultivos:

| Rango | Nivel requerido | Costo en Elysium |
|---|---|---|
| 2 | 25 | 15,000 |
| 3 | 60 | 36,000 |
| 4 | 95 | 60,000 |

Cada rango también requiere entregar plantas específicas de alto nivel.

***

## 🛒 Mercado de Farming

El mercado de `/farm market` incluye una **tienda rotativa** que renueva su stock **3 veces al día**: a las 00:00, 08:00 y 16:00. Requiere nivel 15 para acceder. Tiene stock limitado por ítem y por jugador.

***

## 🏆 Torneos

Los torneos de cosecha se activan automáticamente **6 veces al día**: 01:00, 05:00, 08:00, 13:00, 17:00 y 21:00. Cosecha la mayor cantidad posible durante el tiempo del torneo para ganar.

| Posición | Recompensa |
|---|---|
| 🥇 1° lugar | $3,000 + 1,500 Elysium |
| 🥈 2° lugar | $1,950 + 1,000 Elysium |
| 🥉 3° lugar | $750 + 500 Elysium |
| 4° lugar | $750 + 250 Elysium |
| 5° lugar | $750 + 100 Elysium |
| Participación | +500 XP + 50 Elysium |

***

## 📜 Comandos

| Comando | Descripción |
|---|---|
| `/farm` | Abrir el menú principal de PyroFarming |
| `/farm shop` | Tienda: comprar semillas y vender cosechas |
| `/farm codex` | Ver el registro de todas las plantas |
| `/farm market` | Abrir el mercado rotativo |
| `/farm stats` | Ver tus estadísticas de farming |
| `/farm tournament` | Ver info del torneo activo |
| `/farm temp` | Ver la temperatura del bioma donde estás parado. También acepta un nombre de bioma o temperatura como argumento |

***

{% hint style="info" %}
Las plantas de nivel alto producen múltiples ítems por cosecha y son mucho más rentables. Invierte en subir de nivel cuanto antes para acceder a los cultivos más valiosos.
{% endhint %}
