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
| 🌎 Overworld (mobs vanilla) | 607 | 1 | 30 |
| 🔥 Nether (mobs vanilla) | 326 | 3 | 30 |
| 🌌 End (mobs vanilla) | 423 | 5 | 30 |

Los **mobs custom** del servidor (los de MythicMobs) usan su propia escala, un poco más lenta:

| Dimensión | Bloques por nivel |
|---|---:|
| 🌎 Overworld | 1.087 |
| 🔥 Nether | 543 |
| 🌌 End | 722 |
| 🌀 Wallmapu | 224 |

Al nivel 30 (el máximo) un mob vanilla del Overworld tiene hasta **+150% de vida** (2,5 veces), **+75% de daño**, **+110% de experiencia** y **+150% de drops** respecto a uno de nivel 1. Entre medio el aumento es proporcional al nivel.

***

## 🎯 A quién afecta

- ✅ Mobs hostiles vanilla: zombis, esqueletos, creepers, arañas, endermans y similares.
- ✅ Mobs custom de los dungeons y del Wallmapu.
- ❌ Jefes, animales y mobs neutrales.
- ❌ Mobs que salen de spawners o de huevos: siempre son de nivel 1.

***

## 💡 Consejos

- **Antes de alejarte, equípate:** a 5.000 bloques del spawn los zombis ya rondan el nivel 8-9.
- **Los spawners no escalan:** son una forma segura de farmear aunque estés lejos.
- **El Nether y el End suben más rápido** que el Overworld; no los subestimes.
- Los drops y la experiencia mejoran con el nivel, así que el riesgo se paga.
