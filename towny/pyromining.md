# ⛏️ PyroMining

**PyroMining** es el sistema de minería avanzada del servidor. Al romper minerales puedes obtener recursos especiales: gemas, artefactos, polvo misterioso, runas y más. También incluye mobs únicos y jefes que solo aparecen en la mina.

***

## ¿Cómo funciona?

Mina normalmente en el overworld o el nether. Al romper ciertos minerales, existen probabilidades independientes de obtener:

- **Gemas** — ítems valiosos con distintas calidades
- **Fluxes** — recurso especial vendible o consumible
- **Artefactos** — ítems misteriosos identificables para revelar su contenido
- **Polvo Misterioso** — se refina para obtener materiales raros
- **Zeta** — moneda exclusiva del plugin que se acumula al minar

Usa `/mine` para abrir el menú principal y ver tus stats, tienda y diario.

***

## Gemas

Las gemas caen al romper minerales específicos. Cada gema tiene una **calidad** que afecta su precio de venta.

| Tier | Mineral fuente | Probabilidad | Precio base |
|---|---|---|---|
| Tier 1 | Carbón | 15% | $50 |
| Tier 2 | Redstone | 10% | $75 |
| Tier 3 | Cuarzo del Nether | 8% | $100 |
| Tier 4 | Lapislázuli | 6% | $150 |
| Tier 5 | Esmeralda | 4% | $200 |
| Tier 6 | Diamante | 2% | $250 |

### Calidades de gema

| Calidad | Multiplicador de precio |
|---|---|
| Ruined (Arruinada) | ×0.70 |
| Badly Damaged (Muy dañada) | ×0.80 |
| Damaged (Dañada) | ×0.90 |
| Worn (Desgastada) | ×1.2 |
| Pristine (Perfecta) | ×1.5 |

***

## Fluxes

Los Fluxes son ítems vendibles o utilizables que caen con un **5% de probabilidad** al minar.

| Tipo | Donde cae | Precio de venta |
|---|---|---|
| **Basic Flux** | Overworld (carbón, lapislázuli, diamante, redstone, esmeralda) | $50 |
| **Blazed Flux** | Nether (cuarzo) | $35 |

***

## Artefactos

Los artefactos caen con un **0.8% de probabilidad** al romper cualquier mineral. Son ítems no identificados que deben llevarse a la **estación identificadora** para revelar su contenido. El tiempo de identificación varía por rareza.

| Rareza | Probabilidad | Tiempo de identificación | Precio de venta |
|---|---|---|---|
| Basic | 42% | 20 min | $50 |
| Unusual | 21% | 40 min | $80 |
| Epic | 14% | 60 min | $150 |
| Exceptional | 10% | 90 min | $300 |
| Legendary | 6% | 120 min | $400 |
| Fabled | 4% | 160 min | $500 |
| Mythic | 2.4% | 200 min | $600 |
| Celestial | 0.5% | 240 min | $750 |
| Divine | 0.1% | 280 min | $1,000 |

***

## Polvo Misterioso

El **Polvo Misterioso** cae con un **1% de probabilidad** al minar. Al refinarlo, produce uno de los siguientes materiales:

| Resultado | Probabilidad |
|---|---|
| Rune Dust | 75% |
| Ancient Relic | 7% |
| Shattered Orb | 10% |
| Oracleite | 4% |

***

## Zeta

La **Zeta** es la moneda del plugin. Se acumula automáticamente al romper minerales y se usa para mejoras y contenido avanzado.

| Mineral | Zeta obtenida |
|---|---|
| Carbón | 30 |
| Hierro | 40 |
| Cobre | 35 |
| Oro | 90 |
| Redstone | 70 |
| Lapislázuli | 130 |
| Diamante | 350 |
| Esmeralda | 400 |
| Cuarzo del Nether | 30 |

***

## Guardianes de Runas

Al hacer **clic derecho** en un **bloque de Redstone** (mineral), puede aparecer un **Guardián de Runa**, un mob especial con 200 HP que tiene probabilidad de soltar runas reales al morir. Hay un cooldown de **45 segundos** entre invocaciones.

***

## Oráculos

Al usar **Oracleite Cargado** en un **bloque de Esmeralda** (mineral), se puede invocar un **Oráculo**, un jefe de alto nivel con 3 fases. Requiere nivel mínimo de minería según la fase.

| Fase | Nivel mínimo | HP | Drops principales |
|---|---|---|---|
| Fase 1 | 40 | 1,100 | Mythic Artifact, Hell Rune, Rune Dust |
| Fase 2 | 45 | 1,600 | Celestial Artifact, Ancient Relic, Light Rune |
| Fase 3 | 50 | 2,000 | Divine Artifact, Abyssal Shard, Astral Rune |

Hay un cooldown de **1 hora** entre invocaciones. La muerte de un Oráculo se anuncia en el chat global.

***

## Comandos

| Comando | Descripción |
|---|---|
| `/mine` | Abrir el menú principal de PyroMining |
| `/mine shop` | Tienda: vender gemas, artefactos y más |
| `/mine stats` | Ver tus estadísticas de minería |
| `/mine journal` | Ver el diario de artefactos descubiertos |
| `/mine artifacts` | Ver tus artefactos actuales |

***

{% hint style="info" %}
Los artefactos más raros (Celestial, Divine) valen hasta $1,000 sin identificar. Identificarlos puede revelar recompensas mucho más valiosas.
{% endhint %}
