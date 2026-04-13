# 🪙 CoinFlip

El **CoinFlip** es el sistema de apuestas de Mapucraft. Lanza una moneda contra otro jugador: 50/50, el ganador se lleva todo menos el impuesto.

Disponible en `/warp casino`.

***

## ¿Cómo funciona?

1. Usa `/cf [cantidad]` para crear una apuesta con tu monto
2. Tu oferta queda publicada en la lista de CoinFlips activos
3. Otro jugador acepta la apuesta haciendo clic en el menú
4. La moneda se lanza — 50% de probabilidad para cada lado
5. El ganador recibe el doble de lo apostado, menos el impuesto correspondiente

Puedes ver todas las apuestas activas con `/cf` o `/coinflip`.

***

## Impuesto por apuesta

El servidor retiene un porcentaje del premio según el monto apostado:

| Monto apostado | Impuesto |
|---|---|
| Menos de $100 | 5% |
| $100 – $999 | 10% |
| $1,000 en adelante | 15% |

> **Ejemplo:** apostás $10,000 y ganás → recibirías $17,000 (los $20,000 del pozo menos 15% = $3,000 de impuesto).

***

## Comandos

| Comando | Descripción |
|---|---|
| `/cf` | Abrir el menú de CoinFlip |
| `/coinflip` | Alias del comando |
| `/cf [cantidad]` | Crear una apuesta con ese monto |

***

{% hint style="warning" %}
El CoinFlip es un juego de azar puro. No existe estrategia que mejore tus probabilidades — siempre es 50/50. Apuesta solo lo que estés dispuesto a perder.
{% endhint %}
