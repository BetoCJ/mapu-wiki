# 📈 Escalado de Mobs

En el Overworld, el Nether y el End los mobs hostiles tienen **nivel**, y suben mientras más te alejas del centro del mundo (`0,0`). Cerca del spawn los monstruos son suaves; en los bordes son un verdadero desafío, con mejores drops y más experiencia.

{% hint style="info" %}
El escalado se activó en la versión **suave** el 24 de octubre y se ajustó el 27 de octubre (mobs un 15% más fuertes a la misma distancia). Si ves que algo se siente muy fácil o muy duro, avísanos en el [Discord](https://discord.gg/YDJKpgEU3m).
{% endhint %}

***

## 🧮 Cómo se calcula el nivel

Cada cierta distancia desde el `0,0` el nivel sube en 1. Cuanto más pequeño es el número, más rápido sube.

| Dimensión | Bloques por nivel | Nivel mínimo | Nivel máximo |
|---|---:|---:|---:|
| 🌎 Overworld (mobs vanilla) | 552 | 1 | 30 |
| 🔥 Nether (mobs vanilla) | 296 | 3 | 30 |
| 🌌 End (mobs vanilla) | 385 | 5 | 30 |

El **End** empieza a subir de nivel recién a los **1.000 bloques** del centro (antes de eso, nivel 5). En el **Wallmapu** los mobs vanilla **no** escalan; ahí solo suben de nivel los mobs custom.

Los **mobs custom** del servidor (los de MythicMobs) usan su propia escala, un poco más lenta:

| Dimensión | Bloques por nivel |
|---|---:|
| 🌎 Overworld | 988 |
| 🔥 Nether | 494 |
| 🌌 End | 656 |
| 🌀 Wallmapu | 204 |

Al nivel 30 (el máximo) un mob vanilla del Overworld tiene hasta **+150% de vida** (2,5 veces), **+75% de daño**, **+110% de experiencia** y **+150% de drops** respecto a uno de nivel 1. Entre medio el aumento es proporcional al nivel.

***

## 📊 Qué mejora con el nivel

El aumento es **lineal**: nivel 1 no suma nada y nivel 30 suma el máximo. Valores aproximados:

| Nivel | Vida | Daño | Drops | Experiencia |
|---:|---:|---:|---:|---:|
| 5 | +21% | +10% | +21% | +15% |
| 10 | +47% | +23% | +47% | +34% |
| 15 | +72% | +36% | +72% | +53% |
| 20 | +98% | +49% | +98% | +72% |
| 25 | +124% | +62% | +124% | +91% |
| 30 | +150% | +75% | +150% | +110% |

Además, al nivel 30 el mob se mueve un 25% más rápido, tiene un 30% de resistencia al empuje, un 40% más de rango de visión y los creepers hacen un 80% más de daño de explosión.

**Los drops no cambian de tipo, solo de cantidad.** Un mob de nivel alto suelta los mismos objetos de siempre, pero más unidades. No hay botín especial por nivel.

- Los **ahogados, evokers, shulkers y ravagers** no mejoran sus drops con el nivel (sí su vida, daño y experiencia).
- El nombre del mob muestra su nivel con color: 1-6 verde, 7-12 azul, 13-18 amarillo, 19-24 rojo y 25-30 morado.

***

## 🚫 Límite por chunk (anti-farmeo)

Si matas muchos mobs en la misma zona, los bonos se apagan: tras **30 muertes** en un chunk (contando los 3 chunks vecinos) los drops extra y la experiencia extra se desactivan durante **10 minutos**. Los drops normales de vanilla se mantienen. Esto evita las granjas de mobs masivas en un solo punto.

***

## 🎯 A quién afecta

- ✅ Mobs hostiles vanilla: zombis, esqueletos, creepers, arañas, endermans y similares.
- ✅ Mobs custom de los dungeons y del Wallmapu.
- ❌ Jefes (Ender Dragon, Wither, Warden, Elder Guardian), animales y mobs neutrales o aliados (piglins, zombified piglins, golems de hierro y de nieve).
- ❌ Mascotas y mobs domesticados.
- ❌ Mobs que salen de spawners (incluidos los trial spawners) o de huevos: siempre son de nivel 1, sin bonos de vida, daño, drops ni experiencia.
- ❌ Mobs de otros plugins (Citizens, Shopkeepers, MyPet…): nivel 1 fijo. Los de MythicMobs tienen su propio nivel.

***

## 💡 Consejos

- **Antes de alejarte, equípate:** a 5.000 bloques del spawn los zombis ya rondan el nivel 9-10.
- **Los spawners no escalan:** son una forma segura de farmear aunque estés lejos.
- **El Nether y el End suben más rápido** que el Overworld; no los subestimes.
- Los drops y la experiencia mejoran con el nivel, así que el riesgo se paga.
