# 🎣 PyroFishing

**PyroFishing** es el sistema de pesca personalizado del servidor. Al pescar en cualquier cuerpo de agua puedes atrapar más de **126 peces únicos** organizados en 6 niveles de rareza, venderlos, completar tu Codex y participar en torneos.

***

## ¿Cómo funciona?

1. Toma una caña de pescar y lánzala al agua normalmente
2. Al atrapar algo, puede salir un **pez personalizado** en lugar del pez vanilla
3. Los peces se guardan en tu inventario como ítems especiales
4. Abre el menú con **Shift + clic** sosteniendo la caña, o con `/fish`
5. Vende tus peces en `/fish shop` para ganar dinero
6. Completa el **Codex** capturando cada especie al menos una vez

Pescar también te da **XP de pesca** y **Entropía**, la moneda especial del plugin usada para mejoras de caña (aumentos).

***

## Niveles de peces

Los peces están organizados en 6 niveles de rareza. Los más raros se anuncian en el chat global al ser atrapados.

| Nivel | Peces | XP por captura | Entropía |
|---|---|---|---|
| 🟤 **Bronze** | 34 peces | 75 XP | 40 |
| ⚪ **Silver** | 21 peces | 150 XP | 70 |
| 🟡 **Gold** | 18 peces | 300 XP | 80 |
| 🔵 **Diamond** | 15 peces | 700 XP | 100 |
| 🔴 **Platinum** | 24 peces | 1,500 XP | 325 |
| 🟣 **Mythical** | 14 peces | 6,500 XP | 1,000 |

Capturar un pez **Platinum** o **Mythical** se anuncia automáticamente a todo el servidor.

### Ejemplos de peces por nivel

| Nivel | Ejemplos |
|---|---|
| Bronze | Tuna, Piranha, Koi, Bass, Shrimp, Atlantic Cod, Sardine, Squid... |
| Silver | Eel, Manta Ray, Octopus, Neon Tetra, Red Snapper, Tiger Trout... |
| Gold | Shark, Angler Fish, Viper Fish, Lava Eel, Colossal Catfish... |
| Diamond | Ancient Fish, Savage Shark, Void Salmon, Grand Swordfish, Ghostfish... |
| Platinum | Man o' War, Rainbow Trout, Great White Shark, Death Manta, Galaxy Rasbora... |
| Mythical | Ayanami Fish, Zero Two Fish, Amaterasu Fish, Ichigo Fish... |

***

## Cebos

Los cebos se aplican a la caña de pescar arrastrándolos sobre ella. Cada cebo tiene usos limitados y desbloquea peces específicos de ciertos niveles.

| Cebo | Nivel mínimo | Precio | Usos | Peces que atrae |
|---|---|---|---|---|
| 🌿 **Cebo Básico** | 1 | $310 | 75 | Bronze comunes |
| 💧 **Cebo de Río** | 5 | $620 | 50 | Bronze / Silver |
| 🌊 **Cebo Oceánico** | 12 | $1,350 | 40 | Silver / Gold |
| ✨ **Cebo Brillante** | 20 | $2,750 | 30 | Gold / Diamond |
| 💜 **Cebo de Élite** | 30 | $4,800 | 20 | Diamond / Platinum |
| 🌟 **Cebo Mítico** | 40 | $6,300 | 10 | Platinum / Mythical |

Los cebos se compran en `/fish shop`.

***

## Torneos

Los torneos de pesca se activan automáticamente **cada 2 horas**. Durante el torneo, compite por atrapar la mayor cantidad (o el pez más valioso) antes de que se acabe el tiempo.

| Posición | Recompensa |
|---|---|
| 🥇 1° lugar | $3,000 |
| 🥈 2° lugar | $1,950 |
| 🥉 3° lugar | $750 |
| Participación | +150 Entropía |

***

## Comandos

| Comando | Descripción |
|---|---|
| `/fish` | Abrir el menú principal de PyroFishing |
| `/fish shop` | Tienda: comprar cebos y vender peces |
| `/fish codex` | Ver el registro de todos los peces atrapados |
| `/fish stats` | Ver tus estadísticas de pesca |
| `/fish tournament` | Ver info del torneo activo |

***

{% hint style="info" %}
Usar cebos de mayor nivel aumenta tus posibilidades de encontrar peces raros. Los peces Platinum y Mythical valen mucho más en la tienda.
{% endhint %}
