# 🌱 PyroFarming

**PyroFarming** es el sistema de agricultura personalizada del servidor. Cultiva más de **20 plantas únicas** y **9 arbustos** usando **Growstations** (estaciones de cultivo), vende tus cosechas y sube de nivel para desbloquear cultivos más valiosos.

***

## ¿Cómo funciona?

1. Consigue una **Growstation** (crafteable o comprable en `/farm shop`)
2. Colócala en el suelo y plántale una semilla
3. La planta crece automáticamente, incluso cuando estás desconectado
4. Cosecha cuando esté lista y vende en `/farm shop`
5. Gana **XP de farming** y **Elysium** (moneda del plugin) con cada cosecha
6. Sube de nivel para desbloquear plantas y arbustos más valiosos

Abre el menú principal con `/farm` o haciendo **Shift + clic** con una azada.

***

## Growstation

La Growstation es la "maceta especial" donde crecen las plantas. Se craftea así:

```
S S S
S M S
S S S
```

`S` = Semilla de trigo | `M` = Maceta de flores

Las Growstations **no son destruidas por explosiones ni pistones**. Para recogerla, agáchate y rompe el bloque.

***

## Plantas

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

## Arbustos

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

## Árbol de Habilidades

Al nivel 25 puedes craftear un **Archivo de Habilidades** que desbloquea el árbol de habilidades de farming. Se craftea con lechugas, chiles y un Atril.

El árbol tiene 4 rangos que mejoran tus cultivos:

| Rango | Nivel requerido | Costo en Elysium |
|---|---|---|
| 2 | 25 | 15,000 |
| 3 | 60 | 36,000 |
| 4 | 95 | 60,000 |

Cada rango también requiere entregar plantas específicas de alto nivel.

***

## Mercado de Farming

El mercado de `/farm market` incluye una **tienda rotativa** que renueva su stock **3 veces al día**: a las 00:00, 08:00 y 16:00. Requiere nivel 15 para acceder. Tiene stock limitado por ítem y por jugador.

***

## Torneos

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

## Comandos

| Comando | Descripción |
|---|---|
| `/farm` | Abrir el menú principal de PyroFarming |
| `/farm shop` | Tienda: comprar semillas y vender cosechas |
| `/farm codex` | Ver el registro de todas las plantas |
| `/farm market` | Abrir el mercado rotativo |
| `/farm stats` | Ver tus estadísticas de farming |
| `/farm tournament` | Ver info del torneo activo |

***

{% hint style="info" %}
Las plantas de nivel alto producen múltiples ítems por cosecha y son mucho más rentables. Invierte en subir de nivel cuanto antes para acceder a los cultivos más valiosos.
{% endhint %}
