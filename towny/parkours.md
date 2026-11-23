# 🧗 Parkours cortos

_Actualizado el 23/11/2026._

Además del [parkour grande](minijuegos.md#parkour) (`/warp parkour`), Mapucraft tiene **4 parkours cortos** con cronómetro, checkpoints, ranking propio y **premios en llaves**.

***

## 🗺️ Lista de parkours

| Parkour | Cómo entrar | Premio por completarlo |
|---|---|---|
| `parkour1` | `/mpk join parkour1` | 1 Llave Parkour (cada 72 h) |
| `parkour2` | `/mpk join parkour2` | 1 Llave Parkour (cada 72 h) |
| `parkour3` | `/mpk join parkour3` | 1 Llave Parkour (cada 72 h) |
| `parkour4` | `/mpk join parkour4` | 1 Llave Parkour (cada 72 h) |

También puedes abrir el menú con `/mpk lobby` y elegir uno. La [Caja Parkour](cajas.md) se abre en `/warp cajas`.

***

## ⚙️ Cómo se juega

1. Pisa la placa de **inicio**: empieza el cronómetro (se ve en la barra de arriba).
2. Pasa los **checkpoints en orden** (placas). Si te caes, vuelves al último.
3. Pisa la **meta** con todos los checkpoints y tu tiempo queda guardado en el top.

Al empezar recibes **4 botones en la barra** (necesitas 4 huecos libres): **Salir** (doble clic), **Empezar de 0**, **Volver al checkpoint** y **Top 10**. Se quitan solos al terminar.

### 📏 Reglas dentro del parkour

* No recibes daño, no pierdes hambre ni ítems.
* Para empezar necesitas la barra libre y **ningún efecto que cambie tu movimiento**: velocidad, salto, levitación, caída lenta, etc. Los amuletos que alteran la velocidad tampoco se permiten.
* No se pueden usar perlas de ender, cargas de viento, tridentes ni cohetes, ni comer frutas chorus, manzanas doradas u otras comidas con efectos.
* Solo funcionan los comandos del parkour (`/mpk`) y `/spawn`.
* Un tiempo menor a 10 segundos se considera trampa y no cuenta.
* Para cobrar premios necesitas algo de tiempo jugado en el servidor, y las cuentas que comparten conexión no pueden ocupar varios puestos del top.

***

## 🏆 Premios del top 3

Cada domingo a las **20:00** (hora de Chile) se reparten premios a quienes estén en el podio de **cada** parkour:

| Puesto | Premio |
|---|---|
| 🥇 1.º | 3 Llaves Parkour · 2 Llaves Navidad · 1 Llave Amuletos · 1 Llave MapuKoth |
| 🥈 2.º | 2 Llaves Parkour · 1 Llave Navidad · 1 Llave MapuKoth |
| 🥉 3.º | 1 Llave Parkour · 1 Llave Navidad · 1 Llave Amuletos |

* Si no estás conectado o tienes el inventario lleno, el premio queda pendiente y lo cobras con `/mpk claim` (fuera del parkour).
* El **top de tiempos se reinicia el día 1 de cada mes** a las 00:00 (hora de Chile). No se pierden las veces que completaste cada parkour.

{% hint style="info" %}
Los premios los define el staff y pueden cambiar. Estos son los que están configurados al 23/11/2026.
{% endhint %}

***

## 📜 Comandos

| Comando | Qué hace |
|---|---|
| `/mpk lobby` | Menú de parkours |
| `/mpk join <parkour>` | Entrar a un parkour |
| `/mpk leave` | Salir al lobby del parkour |
| `/mpk spawn` | Salir al spawn del servidor (también sirve `/spawn`) |
| `/mpk restart` | Empezar de 0 |
| `/mpk checkpoint` | Volver al último checkpoint |
| `/mpk top <parkour>` | Top 10 de un parkour |
| `/mpk stats` | Tus estadísticas |
| `/mpk menu` | Resumen de tu intento actual |
| `/mpk claim` | Cobrar premios pendientes |
| `/mpk help` | Ayuda |

***

## ❓ Preguntas frecuentes

**No me deja empezar.**
Libera 4 huecos de la barra y quítate efectos de poción o amuletos de velocidad.

**Completé el parkour y no recibí llave.**
El premio por completarlo se puede cobrar una vez cada 72 horas por parkour. Si tenías el inventario lleno, usa `/mpk claim`.

***

→ Ver también: [Mini-juegos](minijuegos.md) · [Cajas y Llaves](cajas.md)
