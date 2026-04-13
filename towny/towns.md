# 🏘️ Towns y Naciones

**Towny** es el sistema central de protección del servidor. Permite a los jugadores crear y gestionar **pueblos (towns)** y unirse a **naciones** para reclamar tierra, protegerla del griefing y organizarse con otros jugadores.

***

## Towns

### Crear un town

Para crear tu propio town necesitas **$5,000** y estar en el lugar donde quieres establecer el primer chunk.

```
/t new [nombre]
```

Una vez creado, el chunk donde estás quedará protegido y podrás ir expandiéndote reclamando chunks adyacentes.

### Expandir tu town

Cada chunk que reclamas se llama **townblock**. El precio base por chunk es **$150**, y aumenta ligeramente con cada chunk adicional.

| | |
|---|---|
| **Precio base por chunk** | $150 |
| **Precio de outpost** | $14,990 |
| **Chunks por residente** | 8 |
| **Máximo chunks por residente** | 32 |

> Los **Outposts** son chunks reclamados que no necesitan estar pegados a tu town principal — útiles para asegurar recursos o puntos estratégicos lejanos.

### Niveles de Town

El nivel de tu town sube automáticamente al conseguir más residentes, desbloqueando un título mayor y más límites de outposts.

| Residentes | Nivel | Título del Alcalde | Outposts máximos |
|---|---|---|---|
| 0 | Ruinas | Espíritu | 4 |
| 1 | Asentamiento | Ermitaño | 8 |
| 2 | Aldea | Jefe | 12 |
| 6 | Pueblo | Barón | 16 |
| 10 | Villa | Vizconde | 20 |
| 14 | Gran Villa | Conde | 24 |
| 20 | Ciudad | Marqués | 28 |
| 24 | Gran Ciudad | Duque | 32 |
| 28 | Metrópolis | Lord | 36 |

### Tipos de Plots

Dentro de tu town puedes asignar distintos tipos de parcelas según su uso:

| Tipo | Uso |
|---|---|
| **Default** | Parcela estándar de residentes |
| **Shop** | Zona comercial para tiendas |
| **Embassy** | Permite a jugadores de otros towns residir |
| **Arena** | Zona de PvP habilitado |
| **Farm** | Zona de cultivo |
| **Inn** | Cualquier jugador puede dormir aquí |
| **Wilds** | Sin protección, como el mundo normal |
| **Bank** | Gestión bancaria del town |
| **Jail** | Zona de confinamiento |

### Upkeep

Los towns pagan un **mantenimiento diario** de **$100** al banco del servidor para seguir activos. Si el banco del town se queda sin fondos, el town puede entrar en deuda y eventualmente caer en ruinas.

Asegúrate de que tu town tenga siempre saldo suficiente con `/t deposit [cantidad]`.

***

## Naciones

Las **naciones** agrupan varios towns bajo un mismo liderazgo, permitiendo alianzas, bonificaciones de chunks y un título para el rey.

### Crear una nación

```
/n new [nombre]
```

Crear una nación cuesta **$40,000** y requiere tener un town activo.

### Niveles de Nación

| Residentes totales | Nivel | Título del Rey | Bonus de chunks |
|---|---|---|---|
| 0 | País | Líder | +10 |
| 10 | Dominio | Protector | +20 |
| 20 | Nación | Rey | +40 |
| 30 | Reino | Gran Rey | +60 |
| 40 | Imperio | Emperador | +100 |
| 60 | Imperio Supremo | Emperador Supremo | +140 |

***

## Vuelo en Town — TownyFlight

Los miembros de un town pueden activar el **vuelo** dentro de los límites de su propio town con el comando `/tf`. El vuelo se desactiva automáticamente al salir del área reclamada o al entrar en combate PvP.

| Comando | Descripción |
|---|---|
| `/tf` | Activar/desactivar el vuelo dentro de tu town |

***

## Comandos principales

### Town

| Comando | Descripción |
|---|---|
| `/t new [nombre]` | Crear un nuevo town |
| `/t` | Ver información de tu town actual |
| `/t [nombre]` | Ver información de otro town |
| `/t list` | Ver todos los towns del servidor |
| `/t spawn` | Teleportarte al spawn de tu town |
| `/t claim` | Reclamar el chunk donde estás |
| `/t unclaim` | Liberar el chunk donde estás |
| `/t deposit [cantidad]` | Depositar dinero en el banco del town |
| `/t withdraw [cantidad]` | Retirar dinero del banco del town |
| `/t invite [jugador]` | Invitar a un jugador a tu town |
| `/t kick [jugador]` | Expulsar a un jugador de tu town |
| `/t set mayor [jugador]` | Cambiar el alcalde del town |
| `/t set perm` | Configurar permisos del town |
| `/t set spawn` | Establecer el punto de spawn del town |
| `/t outpost [número]` | Teletransportarte a uno de tus outposts |
| `/t delete` | Disolver el town |

### Nación

| Comando | Descripción |
|---|---|
| `/n new [nombre]` | Crear una nueva nación |
| `/n` | Ver información de tu nación |
| `/n list` | Ver todas las naciones del servidor |
| `/n spawn` | Teleportarte al spawn de la nación |
| `/n deposit [cantidad]` | Depositar en el banco de la nación |
| `/n invite [town]` | Invitar un town a tu nación |
| `/n kick [town]` | Expulsar un town de tu nación |
| `/n ally add [nación]` | Proponer alianza con otra nación |
| `/n enemy add [nación]` | Declarar enemistad con otra nación |
| `/n delete` | Disolver la nación |

### Plot

| Comando | Descripción |
|---|---|
| `/plot claim` | Reclamar una parcela puesta a la venta |
| `/plot unclaim` | Devolver una parcela al town |
| `/plot forsale [precio]` | Poner tu parcela a la venta |
| `/plot notforsale` | Quitar tu parcela de la venta |
| `/plot set [tipo]` | Cambiar el tipo de la parcela (shop, farm, arena…) |
| `/plot set name [nombre]` | Dar nombre a una parcela |
| `/plot set perm [grupo] [acción] [on/off]` | Configurar permisos de la parcela |
| `/plot perm` | Ver los permisos actuales de la parcela |
| `/plot trust add [jugador]` | Dar acceso de confianza a un jugador en la parcela |
| `/plot trust remove [jugador]` | Revocar acceso de confianza |

### Residente

| Comando | Descripción |
|---|---|
| `/res` | Ver tu información como residente |
| `/res [jugador]` | Ver información de otro jugador |
| `/t join [nombre]` | Unirse a un town con invitación abierta |
| `/t leave` | Abandonar tu town actual |
