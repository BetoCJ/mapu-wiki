# Skills — ValhallaMMO

El sistema de **Skills** (ValhallaMMO) reemplaza las habilidades vanilla y añade 14 habilidades con árboles de perks propios. Cada skill sube de nivel realizando su actividad correspondiente y desbloquea mejoras pasivas únicas mediante un sistema de puntos de habilidad.

---

## ¿Cómo funciona?

- Al subir de nivel en cualquier skill, el skill **Power** recibe XP automáticamente.
- Al subir **Power**, obtienes **puntos de habilidad** que puedes gastar en los árboles de perks.
- Cada skill tiene su propio árbol de perks con nodos que se desbloquean gastando puntos.
- Los perks son permanentes y se pueden combinar estratégicamente.

---

## Habilidades disponibles

| Skill | Cómo subir | Mejoras destacadas |
|---|---|---|
| **Mining** | Minar bloques | Drops extra, vein mining, blast mining, velocidad |
| **Woodcutting** | Talar árboles | Drops extra, tala encadenada, velocidad |
| **Digging** | Cavar tierra y arena | Drops extra, arqueología, velocidad |
| **Farming** | Cosechar, criar animales, esquilar | Drops extra, cosecha automática |
| **Fishing** | Pescar | Drops extra, velocidad de pesca |
| **Alchemy** | Preparar pociones manualmente | Calidad de pociones, efectos mejorados |
| **Smithing** | Usar equipo (durabilidad consumida) | Calidad de crafteo, mejoras a ítems |
| **Enchanting** | Encantar objetos | Esencia de encantamiento, amplificación |
| **Light Weapons** | Usar espadas y herramientas ligeras | Daño, velocidad, sangrado, parry |
| **Heavy Weapons** | Usar hachas y mazas | Daño pesado, machaqueo |
| **Light Armor** | Recibir daño con armadura ligera | Evasión, velocidad de movimiento |
| **Heavy Armor** | Recibir daño con armadura pesada | Resistencia, reducción de daño |
| **Archery** | Disparar con arco o ballesta | Daño, alcance, perforación, precisión |
| **Power** | Subir cualquier otro skill | Puntos de habilidad, crít, sangrado base |

Todos los skills tienen **nivel máximo 100**, excepto Power que llega hasta **256**.

---

## Sistema de Perks (Árbol de Habilidades)

Cada skill tiene un árbol de perks visual que se navega en el juego. Los nodos tienen:

- **Nivel requerido** del skill para desbloquearlos.
- **Costo en puntos** (gastados desde Power).
- **Requisitos de otros perks** — algunos perks solo se desbloquean tras desbloquear otro.

Los puntos de habilidad se obtienen subiendo **Power**. Para acceder al árbol de un skill usa `/val skilltree [skill]`.

---

## Sistema de Combate (ValhallaMMO)

ValhallaMMO reemplaza el sistema de combate vanilla con mecánicas propias:

| Mecánica | Descripción |
|---|---|
| **Crítico** | Golpes críticos personalizados con probabilidad y daño por stats |
| **Sangrado** | Daño de sangrado por ticks, acumulable hasta 4 stacks |
| **Parry** | Bloqueo activo: éxito debuffa al enemigo, fallo te vulnera |
| **Evasión** | Esquivar ataques si el jugador enfrenta al atacante |
| **Stun** | Aturdimiento con Lentitud, Ceguera y Debilidad por varios ticks |
| **Oneshot protection** | Protección contra oneshots (requiere superar 3x tu HP para ignorarla) |

El daño físico sigue una fórmula personalizada. La armadura ligera ofrece más evasión; la pesada más absorción.

---

## ValhallaTrinkets

Los **Trinkets** son accesorios equipables que otorgan bonificaciones pasivas permanentes. Se obtienen por diversas fuentes (crafteo especial, drops, eventos) y se equipan en ranuras dedicadas.

Ejemplos de atributos:

| Trinket | Bonus principal |
|---|---|
| Amuleto de Vitalidad | +2 corazones de vida máxima |
| Pureza | +45% resistencia al veneno |
| Fuerza de Gungnir | +0.75 alcance de ataque |
| Collar Divino | +6 inmunidad plana |

Cada trinket puede tener un **tipo único**, lo que significa que solo puedes equipar uno del mismo tipo a la vez.

---

## Comandos

| Comando | Descripción |
|---|---|
| `/val` | Menú principal de ValhallaMMO |
| `/val skills` | Ver todos tus skills y niveles actuales |
| `/val stats` | Ver tus estadísticas personales de combate |
| `/val skilltree [skill]` | Abrir el árbol de perks de un skill específico |
