# 🎟️ Lotería

_Actualizado el 23/11/2026._

La **Lotería** de Mapucraft es un sorteo con dinero del juego. Compras boletos, todo lo que se junta forma el **pozo** y, cuando llega la hora, el servidor elige un ganador al azar. Cuantos más boletos tengas, más probabilidades tienes.

***

## ⚙️ ¿Cómo funciona?

1. Abre el menú con `/loteria` (también `/lot` o `/lotto`)
2. Compra boletos desde el menú o con `/loteria comprar <cantidad>` (`max` compra todos los que puedas)
3. Todo el dinero de los boletos va al **pozo** de la ronda
4. A la hora del sorteo se elige **un ganador** al azar: cada boleto es una oportunidad, así que quien tiene más boletos tiene más probabilidades
5. El ganador recibe el pozo (menos el impuesto). Si estaba desconectado, se le avisa cuando entra

Hay una ronda abierta a la vez; apenas termina una, empieza otra.

***

## 🤖 Compra automática *(desde el 23 de noviembre)*

Para no tener que entrar a comprar en cada sorteo, activa la **compra automática**:

* `/loteria auto <boletos> [rondas]` — te asegura esa cantidad de boletos en cada ronda (durante las rondas que elijas). Si ya compraste algunos a mano, solo completa lo que falta.
* Compra **mientras estés conectado y te alcance el dinero**, con las mismas reglas que la compra normal, y nunca compra dos veces en la misma ronda.
* `/loteria auto` sin más te muestra si la tienes activa; `/loteria auto off` la cancela (los boletos que ya tienes siguen participando).

***

## ℹ️ Datos de la lotería

| | |
|---|---|
| **Precio del boleto** | $2,000 |
| **Máximo por jugador y ronda** | 100 boletos |
| **Sorteos** | Todos los días a las **14:00** y a las **21:00** (hora de Chile) |
| **Impuesto** | 10 % del pozo (se descuenta del premio) |
| **Mínimo de participantes** | 2 jugadores distintos |
| **Cierre de ventas** | 20 segundos antes del sorteo |

{% hint style="info" %}
Si a la hora del sorteo hay **menos de 2 jugadores distintos**, no se sortea: se devuelve el **100 %** del dinero a cada uno, sin impuesto.
{% endhint %}

***

## 🛡️ Reglas para participar

* Necesitas al menos **60 minutos de juego** en el servidor para comprar boletos.
* Solo se permite **una cuenta por IP** en cada ronda.
* Las compras grandes (desde $50,000) piden confirmación en el menú.

***

## 🔔 Avisos

El servidor te recuerda el sorteo en el chat (a los 60, 30, 10, 5 y 1 minuto, y con una cuenta regresiva final) y anuncia las compras de boletos agrupadas, como máximo una vez cada 5 minutos. Si te molestan, puedes silenciarlos con `/loteria avisos off` (no te impide comprar) y volver a activarlos con `/loteria avisos on`.

***

## 📜 Comandos

| Comando | Descripción |
|---|---|
| `/loteria` | Abrir el menú de la lotería |
| `/loteria comprar <cantidad\|max>` | Comprar boletos |
| `/loteria auto <boletos> [rondas]` | Activar la compra automática (`/loteria auto off` para cancelarla) |
| `/loteria info` | Ver el estado de la ronda (pozo, hora del sorteo) |
| `/loteria boletos` | Ver tus boletos y tu probabilidad de ganar |
| `/loteria participantes` | Ver quiénes participan |
| `/loteria historial` | Ver los últimos ganadores |
| `/loteria top` | Ver a los mayores ganadores |
| `/loteria avisos [on\|off]` | Silenciar o activar los recordatorios |

***

## ❓ Preguntas frecuentes

**¿Qué pasa si gano estando desconectado?**
El premio se paga igual y se te avisa cuando entras.

**¿Puedo comprar más de 100 boletos?**
No: el máximo por jugador y ronda es 100.

**¿A dónde va el impuesto?**
El 10 % del pozo se elimina (nadie lo recibe): ayuda a que el dinero del servidor no se infle.
