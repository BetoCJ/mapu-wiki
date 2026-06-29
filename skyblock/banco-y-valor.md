# 💰 Banco y Valor de Isla

Cada isla tiene su propio **banco** compartido entre todos sus miembros, y un **valor** calculado automáticamente según lo que hay construido sobre ella. Ambos sistemas determinan tu posición en el ranking del servidor.

***

## Banco de Isla

El banco guarda tres tipos de recursos que cualquier miembro con permisos puede depositar o retirar:

| Recurso | Nombre en el menú | Cantidad inicial |
|---|---|---|
| 💵 **Dinero** | Monedas del Lof | $1,000 |
| ❖ **Cristales** | Cristales de Püllü (Almas) | 100 |
| ✨ **Experiencia** | Sabiduría Celestial | 100 |

Los **Cristales** son la moneda premium de la isla: se obtienen completando labores, subiendo de nivel y comprando el ítem especial **Cristal del Wenu Mapu**. Se usan junto al dinero normal para pagar casi todas las mejoras de tu cumbre.

### Comandos

| Comando | Descripción |
|---|---|
| `/is deposit [nombre] [cantidad]` | Depositar en el banco de tu isla |
| `/is withdraw [nombre] [cantidad]` | Retirar del banco de tu isla |
| `/is bank` | Ver el banco de tu isla |

***

## Valor de Isla (Island Value)

Tu isla tiene un **valor** que se recalcula automáticamente cada 20 segundos (con un recálculo forzado cada 10 segundos) en base a todos los bloques y generadores colocados sobre ella. Este valor determina tu posición en el ranking de `/is top`.

### Bloques de mayor valor

| Bloque | Valor |
|---|---|
| Huevo de Dragón | 10,000 |
| Faro (Beacon) | 5,000 |
| Bloque de Netherite | 2,500 |
| Bloque de Esmeralda | 300 |
| Bloque de Diamante | 200 |
| Bloque de Oro | 50 |
| Obsidiana Llorosa / Linterna del Mar | 5 |
| Tolva | 10 |

### Bloques de bajo valor

| Bloque | Valor |
|---|---|
| Obsidiana | 2.0 |
| Tierra / Arena | 0.01 |
| Piedra | 0.01 |
| Adoquín | 0.005 |

{% hint style="info" %}
Puedes revisar el desglose completo de valores con `/isblockvalues blocks` o `/isblockvalues spawners`.
{% endhint %}

***

## Ranking de Islas

```
/is top
```

Muestra las mejores islas del servidor, ordenadas por **Valor** o por **Experiencia** (nivel de cumbre). La visibilidad de tu valor en el ranking depende de la configuración "Visibilidad del Valor" de tu isla (ver [Tu Isla](islas.md)).
