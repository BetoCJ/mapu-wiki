# 🥋 Sumo

_Actualizado el 23/11/2026._

El **Sumo** es un minijuego de empujones: dos jugadores se enfrentan **solo con los puños** sobre una plataforma y gana quien deja al rival **fuera de la plataforma**. Nadie pierde vida ni ítems: todos pelean en igualdad, sin armas, habilidades, encantamientos ni amuletos.

{% hint style="success" %}
🆕 **Desde el 20 de noviembre.** Desde el 23 de noviembre también puedes **apostar como espectador** a quién gana una pelea ajena.
{% endhint %}

***

## 🚪 Cómo entrar

| | |
|---|---|
| **Warp** | `/warp sumo` (también está en la página 1 del menú `/warps`) |
| **Menú** | `/sumo` (o `/mapusumo`) |
| **Cartel** | Clic derecho en un cartel **[Sumo]** para entrar; otro clic para salir; **shift + clic** abre el menú de arenas |
| **Modo actual** | Duelos **1v1**. El sumo también admite **torneos** de eliminación directa cuando el staff los organiza |

1. Ve a `/warp sumo` y haz clic derecho en el cartel **[Sumo]** (o usa `/sumo unirse <arena>`).
2. Cuando hay dos jugadores, los dos pasan a la plataforma y ven una cuenta de **5-4-3-2-1**.
3. ¡A empujar! El primero que cae de la plataforma pierde.
4. Al terminar vuelves a donde estabas con **todo lo tuyo**: inventario, armadura, experiencia, vida, hambre y efectos.

***

## 📏 Reglas de la pelea

* Se pelea **solo con los puños**. Los golpes **no hacen daño**: solo empujan. Correr al golpear empuja más.
* Durante la partida no puedes usar ítems, comandos (salvo `/sumo`), teletransportes, perlas de ender, élitros, pociones ni comida. Tus amuletos y habilidades no funcionan dentro de la arena.
* Cada pelea dura como máximo **60 segundos**. Si se acaba el tiempo se repite **una vez**; si vuelve a empatar, gana quien pasó **menos tiempo fuera de la zona central** de la plataforma.
* En un torneo, los eliminados miran desde la sala de espera y el campeón se anuncia en el chat.
* Si te desconectas o abandonas **en plena pelea**, pierdes. Si el servidor se cae a mitad de partida, al volver a entrar se te devuelve todo.

{% hint style="info" %}
**Qué cuenta para el ranking:** una pelea de menos de 5 segundos no cuenta; entre las mismas dos cuentas solo cuentan unas pocas peleas seguidas (como máximo 3 cada 30 minutos); y las peleas entre cuentas que juegan desde la misma conexión **nunca** cuentan.
{% endhint %}

***

## 🏆 Ranking y estadísticas

| Comando | Qué hace |
|---|---|
| `/sumo top` | Abre el ranking (menú con pestañas) |
| `/sumo top <métrica> [página]` | El ranking en el chat. Métricas: `victorias`, `racha` (actual), `racha-maxima`, `torneos`, `derrotas`, `ko`, `ganancias` |
| `/sumo stats [jugador]` | Tus estadísticas (o las de otro), incluidas las ganancias y pérdidas en apuestas |

En la zona del sumo hay **hologramas** con el top que se actualizan solos.

{% hint style="info" %}
**Premios:** por ahora ganar un duelo **no entrega dinero**: se juega por el ranking y por las apuestas. Si el staff agrega premios, se anunciará.
{% endhint %}

***

## 💰 Apuestas entre los duelistas

En los **duelos 1v1** los dos jugadores pueden apostar dinero antes de pelear. **Es opcional**: si nadie apuesta, el duelo empieza igual de rápido.

1. Al juntarse los dos se abre una ventana corta (unos **12 segundos**) con los botones **[Apostar]** y **[Jugar sin apostar]**.
2. Uno **propone** un monto (botones de 100, 500, 1.000, 5.000 o 10.000, otro monto por chat o `/sumo apostar <monto>`; acepta `2500`, `2.500` o `2k`).
3. El otro ve cuánto ganaría y puede **Aceptar**, **Rechazar** o **Contraofertar** (máximo 3 ofertas en total). Una oferta sin respuesta vence a los 30 segundos y el duelo sigue sin apuesta.
4. **No se cobra nada hasta que los dos aceptan el mismo monto.**
5. El ganador se lleva el **pozo menos un 5 % de comisión**. Ejemplo: apuestan $1.000 cada uno → pozo $2.000 → comisión $100 → el ganador recibe **$1.900**.

| | |
|---|---|
| **Monto mínimo** | $100 |
| **Monto máximo** | $1.000.000 |
| **Comisión** | 5 % del pozo (se elimina, nadie la recibe) |
| **Apuestas activas** | 1 por jugador a la vez |

* **Se devuelve todo, sin comisión,** si el duelo se cancela sin un ganador válido: lo cancela el staff, hay un error, se reinicia el servidor, o alguien sale **antes** de que empiece el combate.
* Si un empate se tiene que decidir al azar, también se devuelve todo.
* Dos cuentas que juegan desde la **misma conexión** no pueden apostar entre sí.

| Comando | Qué hace |
|---|---|
| `/sumo apostar <monto>` | Proponer una apuesta |
| `/sumo apostar aceptar` | Aceptar la oferta |
| `/sumo apostar rechazar` | Rechazar (el duelo empieza sin apuesta) |
| `/sumo apostar cancelar` | Retirar tu oferta |
| `/sumo apostar sin` | Jugar sin apostar |

***

## 👀 Apuestas de espectador

Cualquiera que esté mirando puede apostar a **quién gana una pelea ajena** (duelos y cada pelea de un torneo).

| Comando | Qué hace |
|---|---|
| `/sumo apostar` | Muestra las peleas abiertas para elegir |
| `/sumo apostar <jugador> <monto>` | Apuesta a que ese jugador gana |

| | |
|---|---|
| **Monto mínimo** | $100 |
| **Tope** | $50.000 por pelea (por jugador y por conexión) |
| **Apuestas por pelea** | Una |
| **Distancia** | Tienes que estar cerca: en la sala del sumo o a menos de 64 bloques de la arena |
| **Cierre** | Las apuestas se cierran **apenas empieza el combate** |

* El pozo de quienes acertaron se reparte **en proporción a lo que apostó cada uno**, con una comisión del 5 % que **nunca** te deja por debajo de lo que pusiste si aciertas.
* No puedes apostar a tu propio duelo, ni desde la misma conexión que uno de los luchadores.
* Si la pelea no llega a jugarse de verdad (abandono, empate decidido al azar o una pelea que no cuenta), **se devuelve todo sin comisión**.

***

## ❓ Preguntas frecuentes

**¿Pierdo mis cosas si caigo o me desconecto?**
No. Todo se guarda antes de entrar y se te devuelve al salir, incluso si el servidor se cae.

**¿Puedo usar mis amuletos o mi armadura?**
No. Dentro del sumo todos pelean igual: sin ítems, sin amuletos y sin habilidades.

**¿Por qué mi victoria no subió en el top?**
Puede que la pelea haya durado menos de 5 segundos, que ya hayas peleado varias veces seguidas con la misma persona o que juegues desde la misma conexión que tu rival.

**Aposté y el duelo se canceló, ¿qué pasa con mi dinero?**
Se devuelve completo y sin comisión.

***

→ Ver también: [Mini-juegos](minijuegos.md) · [Warps](../el-servidor/warps.md) · [Comandos](../el-servidor/comandos.md)
