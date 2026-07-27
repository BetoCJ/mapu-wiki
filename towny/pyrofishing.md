# 🎣 PyroFishing

**PyroFishing** es el sistema de pesca personalizado del servidor. Al pescar en cualquier cuerpo de agua puedes atrapar más de **126 peces únicos** organizados en 6 niveles de rareza, venderlos, completar tu Codex y participar en torneos.

***

## ⚙️ ¿Cómo funciona?

1. Toma una caña de pescar y lánzala al agua normalmente
2. Al atrapar algo, puede salir un **pez personalizado** en lugar del pez vanilla
3. Los peces se guardan en tu inventario como ítems especiales
4. Abre el menú con **Shift + clic** sosteniendo la caña, o con `/fish`
5. Vende tus peces en `/fish shop` para ganar dinero
6. Completa el **Codex** capturando cada especie al menos una vez

Pescar también te da **XP de pesca** y **Entropía**, la moneda especial del plugin usada para mejoras de caña (aumentos).

***

## 🐟 Niveles de peces

Los peces están organizados en 6 niveles de rareza. Los más raros se anuncian en el chat global al ser atrapados.

| Nivel | Peces | XP por captura | Entropía | Precio de venta | Probabilidad |
|---|---|---|---|---|---|
| 🟤 **Bronze** | 34 peces | 75 XP | 40 | $4.50 | 60% |
| ⚪ **Silver** | 21 peces | 150 XP | 70 | $22.50 | 15% |
| 🟡 **Gold** | 18 peces | 300 XP | 80 | $50.00 | 5% |
| 🔵 **Diamond** | 15 peces | 700 XP | 100 | $100.00 | 1% |
| 🔴 **Platinum** | 24 peces | 1,500 XP | 325 | $300.00 | 0.2% |
| 🟣 **Mythical** | 14 peces | 6,500 XP | 1,000 | $900.00 | 0.04% |

Capturar un pez **Platinum** o **Mythical** se anuncia automáticamente a todo el servidor.

{% hint style="info" %}
Existe un **Pez del Dia** en la tienda que rota cada 6 horas y se vende a **1.5x** su precio normal.
{% endhint %}

### 📋 Ejemplos de peces por nivel

| Nivel | Ejemplos |
|---|---|
| Bronze | Tuna, Piranha, Koi, Bass, Shrimp, Atlantic Cod, Sardine, Squid... |
| Silver | Eel, Manta Ray, Octopus, Neon Tetra, Red Snapper, Tiger Trout... |
| Gold | Shark, Angler Fish, Viper Fish, Lava Eel, Colossal Catfish... |
| Diamond | Ancient Fish, Savage Shark, Void Salmon, Grand Swordfish, Ghostfish... |
| Platinum | Man o' War, Rainbow Trout, Great White Shark, Death Manta, Galaxy Rasbora... |
| Mythical | Ayanami Fish, Zero Two Fish, Amaterasu Fish, Ichigo Fish... |

***

## 🪱 Cebos

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

## 🏆 Torneos

Los torneos de pesca se activan automáticamente **cada 2 horas** (requiere al menos 4 jugadores en linea). Duran **10 minutos** y el tipo rota entre 9 modalidades diferentes.

### Tipos de torneo

| Tipo | Objetivo |
|---|---|
| **Longest Length** | Atrapa el pez mas largo |
| **Shortest Length** | Atrapa el pez mas corto |
| **Total Length** | Acumula la mayor longitud total de peces |
| **Most Catch** | Atrapa la mayor cantidad de peces |
| **Random Catch** | Atrapa la mayor cantidad de un pez especifico anunciado |
| **Crab Killing** | Mata la mayor cantidad de cangrejos |
| **Base Entropy Earned** | Gana la mayor cantidad de Entropia |
| **Longest Cast** | Pesca desde la mayor distancia posible |
| **Most Biomes** | Pesca en la mayor cantidad de biomas distintos |

### Premios

| Posicion | Recompensa |
|---|---|
| 🥇 1° lugar | $3,000 |
| 🥈 2° lugar | $1,950 |
| 🥉 3° lugar | $750 |
| Participacion | +150 Entropia |

El progreso del torneo se muestra en la barra de jefe (boss bar) en todo momento. Al terminar, se lanzan fuegos artificiales en la posicion de los ganadores.

***

## 🦀 Cangrejos

Al pescar tienes un **4% de probabilidad** de atrapar un **Cangrejo** en lugar de un pez. Los cangrejos son mobs hostiles con 30 puntos de vida que sueltan materiales especiales necesarios para fabricar aumentos.

| Material | Uso |
|---|---|
| Garra de Cangrejo | Receta de aumentos |
| Escama de Cangrejo | Receta de aumentos |
| Cola de Delfin | Receta de aumentos |
| Tentaculo de Calamar | Receta de aumentos |

***

## ⚒️ Aumentos

Los aumentos son mejoras permanentes que se aplican a tu caña de pescar. Se fabrican con materiales especiales y cuestan **Entropia**. Cada aumento tiene multiples niveles y requiere un nivel minimo de pesca.

| Aumento | Efecto | Nivel req. | Costo Entropia | Niveles max. |
|---|---|---|---|---|
| **Solar Rage** | +% de dinero al vender peces | 35 | 75,000 | 5 |
| **Biome Disruption** | % de probabilidad de atrapar peces de cualquier bioma | 16 | 60,000 | 3 |
| **Hot Spot** | % de probabilidad de atrapar 2 peces a la vez | 10 | 50,000 | 13 |
| **Saturate** | % de probabilidad de saciarte al pescar | 12 | 35,000 | 5 |
| **Intellect** | Multiplicador de XP de pesca al atrapar | 25 | 50,000 | 10 |
| **Call of the Storm** | % de atrapar 2 peces mientras llueve | 12 | 40,000 | 5 |
| **Precision Cutting** | +% de Entropia al destripar peces | 22 | 70,000 | 8 |
| **Crab Bait** | Multiplicador de probabilidad de atrapar cangrejos | 25 | 40,000 | 5 |
| **Master Fisherman** | Bonus a la probabilidad de atrapar peces de mejor nivel | 45 | 120,000 | 20 |
| **Sage** | Multiplicador de XP del plugin al atrapar peces | 12 | 57,500 | 10 |
| **Perception** | Multiplicador de Entropia al atrapar peces | 28 | 75,000 | 7 |
| **Trophy** | +% de probabilidad de beneficio al pesar peces | 35 | 60,000 | 6 |

{% hint style="info" %}
Los materiales para fabricar aumentos se obtienen de cangrejos, delfines y calamares. El aumento **Master Fisherman** es el mas costoso y poderoso, disponible desde nivel 45 con 20 niveles de mejora.
{% endhint %}

***

## ⚖️ Escamas (Pesar Peces)

El sistema de escamas te permite **apostar** el valor de un pez eligiendo un nivel de riesgo. Cada pez tiene un peso aleatorio y segun el nivel que elijas puedes ganar o perder dinero respecto al precio base.

| Nivel de riesgo | Probabilidad de ganar | Variacion de precio |
|---|---|---|
| **Bajo** | 70% | +/- 20% |
| **Medio** | 60% | +/- 40% |
| **Alto** | 50% | +/- 60% |
| **Extremo** | 40% | +/- 80% |

***

## 🔪 Destripado de Peces

La estacion de destripado te permite destripar peces a cambio de **Entropia**. Es una forma adicional de obtener Entropia sin vender los peces.

| Nivel | Entropia por destripado |
|---|---|
| Bronze | 20 |
| Silver | 60 |
| Gold | 150 |
| Diamond | 200 |
| Platinum | 800 |

{% hint style="info" %}
El aumento **Precision Cutting** incrementa la Entropia obtenida al destripar peces hasta en un 40% en nivel maximo.
{% endhint %}

***

## 📦 Entregas

El sistema de entregas te da misiones de pesca periodicas. Al pescar **180 peces en total** desbloqueas nuevas entregas de distintos tipos (comun, poco comun, raro, mistico). Las entregas otorgan materiales de aumento como Garras de Cangrejo, Colas de Delfin, Cristales de Entropia y Cebos Especiales.

Las entregas tienen un tiempo de entrega que va desde **30 minutos** (comun) hasta **15 horas** (mistico).

***

## 🎣 Pesca en Grupo (Party Fishing)

Si pescas cerca de otros jugadores (radio de **18 bloques**) todos reciben bonificaciones de XP y Entropia. El bonus aumenta con hasta **5 jugadores** pescando juntos para obtener el maximo beneficio.

***

## 🗿 Totems de Pesca

Los totems son estructuras multibloque que se construyen y activan para obtener mejoras pasivas de pesca. Se gestionan con `/fish totem`. Las pasivas del totem se desbloquean al alcanzar ciertos niveles de pesca y requieren ranuras del totem para activarse.

| Pasiva | Nivel requerido | Ranuras | Efecto |
|---|---|---|---|
| **Experienced Fisherman** | 20 | 1 | Multiplicador de XP x1.5 |
| **Little Critters** | 40 | 2 | +20% probabilidad de cangrejos |
| **Fish School** | 40 | 3 | 30% de atrapar peces adicionales |
| **Random Drops** | 55 | 4 | 15% de drops aleatorios |
| **Treasure Hunter** | 60 | 3 | Bonus en descubrimiento de peces |
| **Mythical Waters** | 60 | 5 | +20% de probabilidad de peces miticos |
| **Entropy Horder** | 60 | 6 | Multiplicador de Entropia x1.25 |

***

## ⭐ Habilidades

El sistema de habilidades (`/fish skills`) ofrece pasivas adicionales para potenciar la pesca. Se desbloquean progresando en el plugin.

| Habilidad | Descripcion |
|---|---|
| **Better Gutting** | Mejora el rendimiento del destripado |
| **Luck of the Catch** | Aumenta la suerte al pescar |
| **Master Augmenter** | Mejoras al usar aumentos |
| **Totem Leader** | Mejoras como lider de totem |
| **Divine Judgement** | Habilidad especial de juicio |
| **Tribal Shout** | Amplifica el rango del totem |
| **Combo Catcher** | Bonus por capturas consecutivas |
| **Augment Infusion** | Infusion mejorada de aumentos |

***

## 📜 Comandos

| Comando | Descripcion |
|---|---|
| `/fish` | Abrir el menu principal de PyroFishing |
| `/fish shop` | Tienda: comprar cebos y vender peces |
| `/fish codex` | Ver el registro de todos los peces atrapados |
| `/fish stats` | Ver tus estadisticas de pesca |
| `/fish tournament` | Ver info del torneo activo |
| `/fish skills` | Ver y gestionar tus habilidades de pesca |
| `/fish totem` | Ver y gestionar tu totem de pesca |
| `/fish bag` | Abrir tu bolsa de peces |
| `/fish deliveries` | Ver tus entregas activas |
| `/fish augment` | Menu de aumentos para tu cana |

***

{% hint style="info" %}
Usar cebos de mayor nivel aumenta tus posibilidades de encontrar peces raros. Los peces Platinum y Mythical valen mucho mas en la tienda.
{% endhint %}
