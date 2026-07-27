# ⛏️ PyroMining

**PyroMining** es el sistema de minería avanzada del servidor. Al romper minerales puedes obtener recursos especiales: gemas, artefactos, polvo misterioso, runas y más. También incluye mobs únicos y jefes que solo aparecen en la mina.

***

## ⚙️ ¿Cómo funciona?

Mina normalmente en el overworld o el nether. Al romper ciertos minerales, existen probabilidades independientes de obtener:

- **Gemas** — ítems valiosos con distintas calidades
- **Fluxes** — recurso especial vendible o consumible
- **Artefactos** — ítems misteriosos identificables para revelar su contenido
- **Polvo Misterioso** — se refina para obtener materiales raros
- **Zeta** — moneda exclusiva del plugin que se acumula al minar

Usa `/mine` para abrir el menú principal y ver tus stats, tienda y diario.

***

## 💎 Gemas

Las gemas caen al romper minerales específicos. Cada gema tiene una **calidad** que afecta su precio de venta. Al hacer clic derecho en una gema se revela su calidad, lo que puede aumentar o disminuir su valor.

| Tier | Nombre | Mineral fuente | Probabilidad | Precio base |
|---|---|---|---|---|
| Tier 1 | Peridoto | Carbón | 15% | $50 |
| Tier 2 | Rubí | Redstone | 10% | $75 |
| Tier 3 | Topacio | Cuarzo del Nether | 8% | $100 |
| Tier 4 | Amatista | Lapislázuli | 6% | $150 |
| Tier 5 | Zafiro | Esmeralda | 4% | $200 |
| Tier 6 | Ojo de Tigre | Diamante | 2% | $250 |

### ⭐ Calidades de gema

| Calidad | Multiplicador de precio |
|---|---|
| Ruined (Arruinada) | ×0.70 |
| Badly Damaged (Muy dañada) | ×0.80 |
| Damaged (Dañada) | ×0.90 |
| Worn (Desgastada) | ×1.2 |
| Pristine (Perfecta) | ×1.5 |

***

## ⚡ Fluxes

Los Fluxes son ítems vendibles o utilizables que caen con un **5% de probabilidad** al minar.

| Tipo | Donde cae | Precio de venta |
|---|---|---|
| **Basic Flux** | Overworld (carbón, lapislázuli, diamante, redstone, esmeralda) | $50 |
| **Blazed Flux** | Nether (cuarzo) | $35 |

***

## 🏺 Artefactos

Los artefactos caen con un **0.8% de probabilidad** al romper cualquier mineral. Son ítems no identificados que deben llevarse a la **estación identificadora** para revelar su contenido. El tiempo de identificación varía por rareza.

| Rareza | Probabilidad | Tiempo de identificación | Precio de venta |
|---|---|---|---|
| Basic | 42% | 20 min | $50 |
| Unusual | 21% | 40 min | $80 |
| Epic | 14% | 60 min | $150 |
| Exceptional | 10% | 90 min | $300 |
| Legendary | 6% | 120 min | $400 |
| Fabled | 4% | 160 min | $500 |
| Mythic | 2.4% | 200 min | $600 |
| Celestial | 0.5% | 240 min | $750 |
| Divine | 0.1% | 280 min | $1,000 |

***

## ✨ Polvo Misterioso

El **Polvo Misterioso** cae con un **1% de probabilidad** al minar. Debe refinarse en una **Refinería** para obtener los materiales que contiene.

### Refinería

Para crear una Refinería coloca un **Soltador (Dropper)** mirando hacia arriba y luego pon una **valla** justo encima. Después pon el Polvo Misterioso dentro e interactúa con la valla para procesarlo.

{% hint style="warning" %}
Si tienes un nivel de minería menor a 20, hay un **25% de probabilidad de que la Refinería falle** y pierdas el Polvo Misterioso.
{% endhint %}

Al refinarlo produce uno de los siguientes materiales (algunos requieren nivel mínimo):

| Resultado | Probabilidad | Nivel requerido |
|---|---|---|
| Polvo Rúnico | 75% | Cualquiera |
| Orbe Réquiem Roto | 10% | Nivel 30+ |
| Reliquia Antigua | 7% | Nivel 25+ |
| Oracleite | 4% | Nivel 20+ |

***

## 🔷 Zeta

La **Zeta** es la moneda del plugin. Se acumula automáticamente al romper minerales y se usa para mejoras y contenido avanzado.

| Mineral | Zeta obtenida |
|---|---|
| Carbón | 30 |
| Hierro | 40 |
| Cobre | 35 |
| Oro | 90 |
| Redstone | 70 |
| Lapislázuli | 130 |
| Diamante | 350 |
| Esmeralda | 400 |
| Cuarzo del Nether | 30 |

***

## 🛡️ Guardianes de Runas

Los **Guardianes de Runa** son mini-jefes con **200 HP** que sueltan runas al morir (50% de probabilidad). Para invocar uno, sostén **Polvo Rúnico** (obtenido de la Refinería) y haz **clic derecho** sobre un **mineral de Redstone**. Hay un cooldown de **45 segundos** entre invocaciones.

El guardián tiene una probabilidad del **20% de teletransportarse** al jugador si queda atrapado, resistencia al knockback de 0.7, y desaparece si nadie lo mata en **120 segundos**. También otorga XP adicional de Minecraft al morir.

{% hint style="info" %}
Necesitas al menos 3 bloques de espacio por encima del mineral para invocar un Guardián.
{% endhint %}

***

## 🔮 Oráculos

Los **Oráculos** son los jefes finales del plugin, con 3 fases progresivas. Se invocan sosteniendo **Oracleite Cargada** y haciendo clic derecho sobre un **mineral de Esmeralda**. Hay un cooldown de **1 hora** entre invocaciones y su muerte se anuncia en el chat global.

La **Oracleite Sin Cargar** se obtiene de la Refinería (Polvo Misterioso). Para cargarla, tenla en la mano secundaria y mina **35 minerales de Diamante**.

{% hint style="info" %}
Necesitas al menos 6 bloques de espacio por encima del mineral para invocar un Oráculo.
{% endhint %}

| Fase | Nombre | Elemento | Nivel mínimo | HP | Daño |
|---|---|---|---|---|---|
| Fase 1 | Radalite | Fuego | 40 | 1,100 | 14 |
| Fase 2 | Impulse | Rayo | 45 | 1,600 | 18 |
| Fase 3 | Tohka | Oscuridad | 50 | 2,000 | 28 |

### Drops por fase

| Fase | Drops principales |
|---|---|
| Fase 1 (Radalite) | Artefacto Mítico, Artefacto Fabled, Runa Infernal, Polvo Rúnico, Transmutador de Fósiles, Garra de Radalite, Lágrima de Zeta |
| Fase 2 (Impulse) | Artefacto Celestial, Artefacto Divino, Reliquia Antigua, Médula Ósea, Runa de Luz, Lágrima de Zeta |
| Fase 3 (Tohka) | Artefacto Celestial, Artefacto Divino, Fragmento Abisal, Acelerador Abisal, Runa Astral, Astralite, Lágrima de Zeta |

### Mecánicas especiales

- **Radalite (Fase 1):** Basada en fuego. Hace más daño en contacto con agua. Al morir suelta una **Runa Infernal** que se usa en otro mineral de Esmeralda para invocar a Impulse.
- **Impulse (Fase 2):** Usa ataques de rayo y daño en área. Al morir explota. Al morir suelta una **Runa de Luz** para invocar a Tohka.
- **Tohka (Fase 3):** Cambia resistencias cada 20 segundos y se vuelve inmune a todo el daño salvo la fuente que ella declare. Al perder 500 HP lanza **Lluvia de Estrellas Astral**. Al llegar a 300 HP activa **Imperio Astral**, potenciando sus stats.

***

## 📈 Niveles de Minería

Al romper minerales acumulas **XP de Minería** que sube tu nivel. El nivel mínimo recomendado para invocar Oráculos es 40, y es obligatorio para ciertas fases. Comienzas necesitando 2,000 XP y cada nivel requiere 1.125× más XP que el anterior.

| Mineral | XP obtenida |
|---|---|
| Carbón | 15 |
| Hierro | 25 |
| Cobre | 20 |
| Oro | 40 |
| Redstone | 35 |
| Lapislázuli | 50 |
| Diamante | 150 |
| Esmeralda | 200 |
| Cuarzo del Nether | 15 |

***

## 🔷 Singularidad

La **Singularidad** es un sistema de mejoras pasivas que se potencia usando **Runas** obtenidas de Guardianes de Runa. Abre el menú con `/mine singularity`.

Cada vez que mejoras la Singularidad necesitas una runa adicional del tipo requerido. No hay nivel máximo. Al mejorarla obtienes **puntos libres** para gastar en las siguientes mejoras pasivas:

| Mejora | Efecto |
|---|---|
| Mejoras Más Baratas | Reduce el coste de mejoras en el menú de Artefactos |
| Progreso de Réquiem | Más XP de Réquiem por cada Esbirro matado |
| Probabilidad de Runa | Mayor probabilidad de que los Guardianes suelten runas |
| Más Zetas | Más Zeta obtenida de todas las fuentes |
| Daño de Oráculo | Reduce el daño recibido de los Oráculos |

### Runas disponibles

Hay 7 tipos de runas que se obtienen al matar Guardianes de Runa:

| Runa |
|---|
| Runa de Naturaleza |
| Runa Fantasma |
| Runa de Agua |
| Runa de Fuego |
| Runa Hada |
| Runa de Rayo |
| Runa de Tierra |

***

## 🏺 Mejoras del Identificador de Artefactos

Dentro de `/mine artifacts` puedes comprar mejoras permanentes con Zeta para mejorar tu experiencia con artefactos y fósiles:

| Mejora | Efecto |
|---|---|
| Overclocked (Acelerado) | Reduce el tiempo de identificación de artefactos en 1% por nivel |
| Amuleto de la Suerte | +1% plano de probabilidad de obtener botín de artefactos por nivel |
| Arqueólogo | +1% plano de probabilidad de encontrar Fósiles por nivel |
| Paciencia | Reduce el tiempo de identificación de Fósiles en 1 minuto por nivel |
| Susurro Final | +0.5% de probabilidad de encontrar Orbes Réquiem en artefactos de Tier 3+ por nivel |

***

## 🦴 Fósiles y Vasijas

### Fósiles

Los **Fósiles** son partes de criaturas extintas que se obtienen al identificar artefactos en `/mine artifacts`. Cada Fósil tiene una **especie** y una **parte**:

- **Especies:** Espectro, Dragón, Mantícora, Fénix
- **Partes:** Cráneo, Costilla, Espina Dorsal, Brazo, Pata, Pie, Cola, Ala

Primero obtienes un **Fósil Sin Identificar**: ponlo en un espacio vacío de `/mine artifacts` para identificarlo (toma tiempo según tu mejora Paciencia). Una vez identificado sabrás la especie y parte exacta. Necesitas las **8 partes** de la misma especie para crear una Vasija.

### Vasijas

Las **Vasijas** son encantamientos personalizados para picos. Se crean poniendo las 8 partes de un Fósil en la **Refinería**. Cada Vasija tiene un elemento y puede venir con una **Peculiaridad** única.

Para aplicar la Vasija a tu pico debes derrotar a su jefe usando **Réquiems** en el orden correcto. El jefe base tiene 150 HP + 50 por nivel de Vasija (máximo 2,000 HP). Puedes subir de nivel una Vasija añadiendo otra del mismo tipo.

| Vasija | Efecto principal | Bonus nivel máximo |
|---|---|---|
| Vasija de Nefaris | Alta probabilidad de conseguir runas de Guardianes | 60% de probabilidad de runa extra |
| Vasija de Rezoth | Al picar una mena puede soltar minerales de otra mena | 10% de probabilidad de duplicar el mineral |
| Vasija de Imperos | Mayor probabilidad de artefactos raros al minar | 5% de probabilidad de Fósil al abrir artefactos |
| Vasija de Aurora | Fundido automático de mineral de hierro y oro | 25% de probabilidad de lingote extra |
| Vasija de Nagyn | Mayor probabilidad de obtener Polvo Misterioso | 20% de probabilidad de x2 Polvo Misterioso |
| Vasija de Xostran | Mayor probabilidad de drops de Oráculos al matarlos | 20% de probabilidad de drop doble |
| Vasija de Valakas | Probabilidad de obtener Prisa Minera II al romper menas | Otorga Prisa Minera III en lugar de II |
| Vasija de Neptulus | Bonus de XP para nivel de PyroMining | 10% de probabilidad de XP triple |
| Vasija de Skylark | Los fluxes se venden más caros | 20% de probabilidad de flux extra |
| Vasija de Mementos | Alta probabilidad de drops dobles al romper minerales sin Toque de Seda | Pequeña probabilidad de drop triple |
| Vasija de Necros | Bonus de XP al desbloquear Réquiems, más aparición de Esbirros | 50% de reducción en generación de Esbirros |
| Vasija de Seraph | Zetas adicionales en todas las menas | 15% de probabilidad de Zeta triple |
| Vasija de las Variantes | Altas probabilidades de fluxes, artefactos y gemas por debajo de Y=20 | Extendido hasta Y=50 |

### Réquiems

Para dañar al jefe de una Vasija debes usar tres **Réquiems** en el orden correcto. Hay 12 Réquiems diferentes. Puedes adivinarlos o matar **Esbirros** (que aparecen al minar con un cooldown de 2 minutos) para ganar progreso que revela el Réquiem correcto para cada slot. Los Réquiems se obtienen mejorando la mejora **Susurro Final** e identificando artefactos de Tier 3 o superior.

Al matar al jefe de la Vasija recibirás **3 Orbes Réquiem Rotos**. Juntando 4 de estos puedes crear un nuevo Orbe Réquiem aleatorio.

Para eliminar todas las Vasijas de un pico y recuperarlas cuesta **100,000 Zetas** (desde `/mine vessels`).

***

## 🎁 Ítems Especiales

Estos ítems únicos se obtienen de jefes, artefactos o como drops raros:

| Ítem | Origen | Uso |
|---|---|---|
| Polvo Rúnico | Refinería (Polvo Misterioso) | Invocar Guardianes de Runa haciendo clic derecho en mineral de Redstone |
| Oracleite Sin Cargar | Refinería (Polvo Misterioso) | Cargarla minando 35 diamantes para invocar Oráculos |
| Runa Infernal | Drop de Radalite (Fase 1) | Usar en mineral de Esmeralda para invocar a Impulse |
| Runa de Luz | Drop de Impulse (Fase 2) | Usar en mineral de Esmeralda para invocar a Tohka |
| Runa Astral | Drop de Tohka (Fase 3) | Mejorar la Singularidad |
| Garra de Radalite | Drop de Radalite | Elimina el cooldown de invocación de Guardianes Rúnicos |
| Médula Ósea | Drop raro de Radalite | Arrastrar sobre un Fósil ya identificado para duplicarlo |
| Transmutador de Fósiles | Drop raro de Impulse | Arrastrar sobre 3 Fósiles para convertirlos en otro del mismo tipo |
| Fragmento Abisal | Drop raro de Tohka | Arrastrar sobre un Orbe Réquiem para duplicarlo |
| Acelerador Abisal | Drop raro de Tohka | Clic derecho para completar de golpe todos los ítems del Identificador |
| Reliquia Antigua | Oráculos / Polvo Misterioso | Arrastrar sobre un Artefacto Sellado para subir su Tier en 1 |
| Lágrima de Zeta | Drops de Oráculos / Vasijas | Vale 10,000 Zetas. Intercambiable entre jugadores |
| Orbe Réquiem Roto | Refinería / matar jefe de Vasija | Juntar 4 para crear un Orbe Réquiem aleatorio |

***

## 📜 Comandos

| Comando | Descripción |
|---|---|
| `/mine help` | Ver la lista de comandos disponibles |
| `/mine menu` | Abrir el menú principal de PyroMining |
| `/mine shop` | Tienda: vender gemas, fluxes y artefactos |
| `/mine stats [jugador]` | Ver estadísticas de minería |
| `/mine journal` | Diario del plugin: info sobre todos los ítems |
| `/mine artifacts` | Gestionar artefactos y fósiles en el identificador |
| `/mine vessels` | Gestionar vasijas del pico |
| `/mine singularity` | Abrir el menú de la Singularidad |
| `/mine blacksmith` | Abrir el menú del Herrero (próximamente) |
| `/mine zeta` | Ver tu balance de Zetas |

***

{% hint style="info" %}
Los artefactos más raros (Celestial, Divine) valen hasta $1,000 sin identificar. Identificarlos puede revelar recompensas mucho más valiosas.
{% endhint %}
