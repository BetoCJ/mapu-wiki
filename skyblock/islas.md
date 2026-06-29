# 🏝️ Tu Isla

Tu isla es tu propio pedazo de cielo: una cumbre flotante que empieza diminuta y que vas expandiendo, decorando y mejorando con tu **lof** (tu equipo). Todo gira en torno al comando `/is` (alias `/island`).

***

## 🏝️ Crear tu isla

```
/is create [nombre]
```

Al crear una isla eliges uno de los **esquemas iniciales** disponibles. Los tres están desbloqueados desde el nivel 1 y son completamente gratuitos:

| Esquema | Bioma (Overworld) | Bioma (Nether) | Bioma (End) |
|---|---|---|---|
| 🏜️ **Isla de Desierto** | Desert | Nether Wastes | The End |
| 🌴 **Isla de Jungla** | Jungle | Nether Wastes | The End |
| 🍄 **Isla de Champiñón** | Mushroom Fields | Nether Wastes | The End |

Cada esquema genera automáticamente sus tres versiones (Overworld, Nether y End) al desbloquear esas dimensiones. El comando de creación tiene un **cooldown de 5 minutos**.

{% hint style="info" %}
También puedes regenerar tu isla con `/is regen [esquema]` (cooldown de 5 minutos, requiere confirmación) si quieres empezar de nuevo con otro esquema.
{% endhint %}

***

## 👑 Jerarquía de tu Lof

Dentro de cada isla existe una jerarquía de 5 rangos, desde simple visitante hasta dueño absoluto:

| Rango | Nombre | Rol |
|---|---|---|
| — | **Weche** (Visitante) | Cualquier jugador que visita tu isla sin ser miembro |
| 1 | **Kona** (Miembro) | Rango básico al unirse a la isla |
| 2 | **Ngülamfe** (Consejero) | Puede reclamar terreno, invitar, dar confianza y expulsar |
| 3 | **Lonko** (Co-Líder) | Casi control total: permisos, configuración, descripción, renombrar, regenerar |
| — | **Toki** (Dueño) | Control absoluto sobre la isla |

Los rangos se gestionan con:

```
/is promote [jugador]
/is demote [jugador]
```

***

## 🔐 Permisos por rango

Cada acción dentro de la isla tiene un **rango mínimo** requerido por defecto (configurable por el Toki o un Lonko con permiso `changePermissions`):

| Permiso | Acción | Rango mínimo por defecto |
|---|---|---|
| `blockBreak` | Romper bloques | Kona (1) |
| `blockPlace` | Colocar bloques | Kona (1) |
| `bucket` | Usar cubos (agua/lava) | Kona (1) |
| `doors` | Usar puertas y trampillas | Kona (1) |
| `killMobs` | Matar mobs | Kona (1) |
| `openContainers` | Abrir contenedores | Kona (1) |
| `redstone` | Usar botones, palancas y placas de presión | Kona (1) |
| `spawners` | Minar generadores | Kona (1) |
| `border` | Cambiar el borde de la isla | Kona (1) |
| `claim` | Reclamar terreno para la isla | Ngülamfe (2) |
| `invite` | Invitar miembros | Ngülamfe (2) |
| `trust` | Dar confianza a un jugador | Ngülamfe (2) |
| `kick` | Expulsar miembros | Ngülamfe (2) |
| `setHome` | Cambiar el hogar de la isla | Ngülamfe (2) |
| `manageWarps` | Crear, editar y eliminar warps | Ngülamfe (2) |
| `interact` | Editar letreros y marcos de objetos | Ngülamfe (2) |
| `changePermissions` | Editar los permisos de la isla | Lonko (3) |
| `demote` / `promote` | Degradar / ascender usuarios | Lonko (3) |
| `description` | Cambiar la descripción de la isla | Lonko (3) |
| `rename` | Renombrar la isla | Lonko (3) |
| `settings` | Cambiar la configuración de la isla | Lonko (3) |
| `regen` | Regenerar la isla | Lonko (3) |

Consulta y edita estos permisos con `/is permissions` o `/is setpermission [permiso] [rango] [true/false]`.

***

## ⚙️ Configuración de la isla

Con `/is settings [configuración] [valor]` el Toki o los Lonko pueden ajustar el comportamiento físico de la cumbre:

| Configuración | Valor por defecto | Efecto |
|---|---|---|
| **Tipo de Unión** | Privado | Quién puede unirse a la isla |
| **Visibilidad del Valor** | Público | Si otros jugadores ven el valor de tu isla |
| **Generación de Mobs** | Activado | Si pueden aparecer criaturas en tu isla |
| **Descomposición de Hojas** | Desactivado | Si las hojas se pudren naturalmente |
| **Formación de Hielo** | Desactivado | Si el agua se congela |
| **Propagación de Fuego** | Desactivado | Si el fuego se extiende por la madera |
| **Pisoteo de Cultivos** | Activado | Si los Konas o mobs pueden destruir sembrados al caminar |
| **Clima de la Isla** | Servidor | Clima propio de tu porción de cielo |
| **Tiempo de la Isla** | Servidor | Hora propia de tu cumbre |
| **Destrucción por Entidades** | Desactivado | Si creepers u otros mobs dañan bloques |
| **Daño de TNT** | Activado | Si las explosiones de TNT dañan bloques |
| **Visitas** | Activado | Si se permite el acceso de visitantes |

{% hint style="info" %}
El **PvP está desactivado** dentro de las islas por defecto.
{% endhint %}

***

## 🌍 Cambiar de bioma

Con `/is biomes [bioma]` (cooldown de 10 segundos) puedes adaptar el bioma de tu isla en cada dimensión:

### ☀️ Wenu Mapu (Overworld)

| Bioma | Costo |
|---|---|
| Cumbres del Pewen (Plains) | $100 |
| Cumbres de Pire (Snowy Plains) | $50 |
| Sabana de Mawida (Savanna) | $100 |

### 🔥 Minche Mapu (Nether)

| Bioma | Costo |
|---|---|
| Páramo de Kutral (Nether Wastes) | $50 |
| Bosque Carmesí Ancestral (Crimson Forest) | $1,000 |
| Bosque Deformado Místico (Warped Forest) | $100 |

### 🌑 Küyen Mapu (End)

| Bioma | Costo |
|---|---|
| Espacio Primordial (The End) | $100 |
| Cúpulas del End (End Highlands) | $150 |
| Tierras Yermas del End (End Barrens) | $150 |

***

## 📜 Comandos principales

| Comando | Descripción |
|---|---|
| `/is create [nombre]` | Crear una nueva isla (cooldown 5 min) |
| `/is home` | Teletransportarte al hogar de tu isla |
| `/is sethome` | Establecer el hogar de tu isla |
| `/is info [isla]` | Ver información de una isla |
| `/is description [desc]` | Establecer la descripción de tu isla |
| `/is rename [nombre]` | Renombrar tu isla |
| `/is invite [jugador]` | Invitar a un jugador |
| `/is join [jugador]` | Unirse a una isla |
| `/is trust [jugador]` | Dar confianza a un jugador (acceso sin ser miembro) |
| `/is kick [jugador]` | Expulsar a un jugador |
| `/is leave` | Abandonar tu isla actual |
| `/is transfer [jugador]` | Transferir la propiedad de la isla |
| `/is delete` | Eliminar tu isla (requiere confirmación) |
| `/is members` | Ver los miembros de tu isla |
| `/is promote` / `/is demote [jugador]` | Ascender / degradar a un miembro |
| `/is chat [tipo]` | Cambiar el tipo de chat (alias `/is c`) |
| `/is fly` | Activar o desactivar el vuelo en tu isla |
| `/is visit` | Visitar otras islas |
| `/is border [color]` | Cambiar el borde de tu isla (Azul, Rojo, Verde u Off) |
| `/is warps` / `/is warp [nombre]` | Ver y usar los warps de la isla |
| `/is setwarp` / `/is deletewarp` | Crear o eliminar un warp |
| `/is level` | Ver el nivel de tu isla |
| `/is logs` | Ver el historial de acciones de tu isla |
| `/is top` | Ver el ranking de islas |
