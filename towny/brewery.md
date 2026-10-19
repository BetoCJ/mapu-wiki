# 🍺 Brewery

**Brewery** es el sistema de elaboración de bebidas del servidor. Fermenta ingredientes en un caldero, destílalos y envejécelos en barriles para crear más de **150 bebidas**: desde la típica chicha chilena hasta cócteles internacionales y elixires del Nether y el End.

{% hint style="info" %}
🗓️ **Disponible desde la apertura (24 de octubre).** Las bebidas con ingredientes del Nether o del End requieren que esas dimensiones estén abiertas. → [Hoja de ruta](hoja-de-ruta.md)
{% endhint %}

***

## ⚙️ ¿Cómo funciona?

Cada bebida pasa por hasta **3 pasos**, según su receta.

### 1️⃣ Fermentar en el caldero

1. Llena un **caldero** de agua y ponle una **fuente de calor** debajo: fuego, fuego de alma, lava, bloque de magma, fogata o fogata de alma.
2. Agrega los ingredientes de la receta con **clic derecho** (uno por uno, en las cantidades exactas).
3. Controla el tiempo con un **reloj**: haz clic derecho al caldero con él en la mano y verás cuánto lleva cocinándose.
4. Cuando el tiempo coincida con la receta, saca la bebida con **botellas de cristal vacías** (3 botellas por tanda). Si te pasas o te quedas corto, la calidad baja o sale otra bebida.

Mientras hierve, las **partículas** del caldero cambian de color: sirven para calcular el momento justo.

### 2️⃣ Destilar (si la receta lo pide)

Coloca la bebida en una **mesa de pociones**. Cada destilación dura **40 segundos** por defecto (algunas recetas más) y cada receta pide un número exacto de destilaciones. Más destilaciones, más alcohol.

### 3️⃣ Envejecer en barril (si la receta lo pide)

- Puedes usar un **barril de Minecraft** (guarda hasta 6 bebidas; cuenta como roble) o un **tonel de Brewery**, hecho con bloques de madera y un **cartel que diga «Tonel»** (también sirve «Barrel»).
- El **tipo de madera** importa: cada receta pide una madera concreta (o cualquiera).
- **1 año de añejado = 20 minutos reales.** Una bebida de 18 años necesita 6 horas en el barril.
- Pasarte de tiempo o usar la madera equivocada puede arruinar la bebida.

### 🔒 Sellar (opcional)

La **mesa de sellado** (un ahumador, se fabrica con 2 botellas de cristal sobre 4 tablones) deja sellada una bebida para guardarla o regalarla sin que se vea su contenido de alcohol.

***

## ⭐ Calidad

Cada bebida tiene **3 niveles de calidad** (mala, normal y buena) y se muestra con **1 a 5 estrellas**. La calidad depende de qué tan exactos fueron el tiempo de cocción, el número de destilaciones y los años de añejado. La calidad cambia el **nombre**, el **sabor** (lore) y la **fuerza de los efectos**.

Cada receta tiene una **dificultad de 1 a 10**: cuanto más alta, más precisión necesitas para lograr una bebida buena.

***

## 🥴 Borrachera

Las bebidas con alcohol te emborrachan. Cuanto más alto el nivel, peores los efectos:

- 🚶 **Te tambaleas** al caminar.
- 💬 **Tu chat se distorsiona** («hola» pasa a «ooola»). Escribe entre `*asteriscos*` o `[corchetes]` para que ese trozo no se altere.
- 🤢 **Vomitas** (aparecen bloques de arena de almas que desaparecen solos).
- 🔑 **Entrar al juego cuesta**: si te desconectas muy borracho, puede que necesites varios intentos para volver a entrar.
- 🛏️ Si bebiste demasiado, al volver a conectarte puedes despertar en **tu cama**.
- 🤕 La **resaca** dura hasta **7 días** después de desconectarte.

Para bajar el alcohol come **pan**, **papa al horno** o una **botella de miel**, o bebe un **balde de leche**. Algunas bebidas sin alcohol (café, mate) incluso lo reducen.

***

## 🍷 Todas las bebidas

<!-- AUTO:inicio brewery -->
Hay **155 bebidas** en 8 categorías. Esta lista se genera sola desde el archivo de recetas, así que siempre coincide con el servidor. **Cocción** son minutos reales en el caldero; **Destilar** es el número de destilaciones; **Barril** es la madera y los años de añejado (1 año = 20 minutos reales); **Alc.** es el alcohol que sube al beberla perfecta.

| Categoría | Bebidas |
|---|---:|
| Especiales (Nether, End y brujería) | 3 |
| Bebidas chilenas y latinoamericanas | 22 |
| Cervezas | 12 |
| Vinos, fermentados e hidromieles | 16 |
| Destilados | 20 |
| Licores | 8 |
| Cócteles | 49 |
| Sin alcohol y refrescos | 25 |

### Especiales (Nether, End y brujería)

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Poción del Nether** | Verruga del Nether ×5, Polvo de blaze ×3, Crema de magma ×2 | 10 min | 4 | carmesí, 6 años | 35 | Resist. al fuego, Fuerza, Veneno |
| **Elixir del End** | Fruto de chorus ×6, Perla de ender ×2, Azúcar ×3 | 12 min | 3 | distorsionado, 10 años | 30 | Visión nocturna, Velocidad, Náusea |
| **Brebaje de Bruja** | Ojo de araña ×3, Champiñón rojo ×4, Ojo de araña fermentado ×2 | 8 min | 3 | — | 20 | Visión nocturna, Invisibilidad, Veneno |

### Bebidas chilenas y latinoamericanas

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Pisco Sour** | Trigo ×6, Azúcar ×3, Huevo ×1 | 5 min | 2 | — | 15 | Velocidad |
| **Terremoto** | Manzana ×4, Azúcar ×2, Bola de nieve ×2, Helecho ×1 | 4 min | — | — | 14 | Lentitud, Náusea |
| **Cola de Mono** | Balde de leche ×2, Cacao ×3, Azúcar ×3, Trigo ×4 | 6 min | — | — | 12 | Regeneración |
| **Piscola** | Azúcar ×2, Trigo ×3, Cacao ×1 | 3 min | — | cualquiera, 1 años | 15 | — |
| **Vaina** | Cacao ×2, Huevo ×1, Azúcar ×2 | 3 min | — | cualquiera, 1 años | 12 | — |
| **Araucano** | Helecho ×3, Algas ×2, Azúcar ×1 | 5 min | 2 | roble, 5 años | 28 | Veneno |
| **Mote con Huesillo** | Trigo ×4, Manzana ×2, Azúcar ×4 | 6 min | — | cualquiera, 1 años | — | — |
| **Borgoña** | Bayas dulces ×5, Azúcar ×2 | 4 min | — | cualquiera, 2 años | 10 | — |
| **Melón con Vino** | Rodaja de melón ×1, Bayas dulces ×4, Azúcar ×2 | 3 min | — | cualquiera, 1 años | 11 | — |
| **Jote** | Bayas dulces ×3, Azúcar ×1, Carbón vegetal ×1 | 2 min | — | cualquiera, 1 años | 8 | — |
| **Serena Libre** | Rodaja de melón ×3, Azúcar ×2 | 3 min | 1 | cualquiera, 1 años | 12 | — |
| **Pihuelo** | Trigo ×3, Azúcar ×2 | 4 min | — | cualquiera, 2 años | 10 | — |
| **Pajarete** | Bayas dulces ×5, Azúcar ×4 | 6 min | — | roble, 4 años | 14 | — |
| **Enguindado** | Bayas dulces ×4, Azúcar ×3 | 7 min | — | roble, 6 años | 16 | — |
| **Candola** | Bayas dulces ×4, Azúcar ×3, Polvo de blaze ×1 | 5 min | — | cualquiera, 2 años | 11 | — |
| **Chuflay** | Azúcar ×2, Helecho ×1 | 2 min | — | cualquiera, 1 años | 10 | — |
| **Navegado** | Bayas dulces ×5, Azúcar ×3, Polvo de blaze ×1 | 6 min | — | cualquiera, 2 años | 12 | — |
| **Mango Sour** | Rodaja de melón ×2, Azúcar ×3, Huevo ×1 | 4 min | 1 | cualquiera, 1 años | 14 | — |
| **Ruso Blanco** | Balde de leche ×1, Cacao ×2, Azúcar ×3 | 3 min | 1 | cualquiera, 1 años | 15 | — |
| **Chicha** | Trigo ×8, Azúcar ×3, Bayas dulces ×2 | 7 min | — | cualquiera, 3 años | 9 | Regeneración |
| **Chicha de Uva** | Bayas dulces ×5, Azúcar ×3 | 8 min | — | cualquiera, 5 años | 10 | — |
| **Clery** | Bayas dulces ×3, Azúcar ×2, Manzana ×2 | 4 min | — | cualquiera, 1 años | 10 | — |

### Cervezas

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Cerveza de Trigo** | Trigo ×3 | 8 min | — | abedul, 2 años | 5 | — |
| **Cerveza** | Trigo ×6 | 8 min | — | cualquiera, 3 años | 6 | — |
| **Cerveza Oscura** | Trigo ×6, Cacao ×1 | 8 min | 3 | roble oscuro, 8 años | 7 | — |
| **Cerveza de Calabaza** | Trigo ×4, Calabaza ×2 | 9 min | — | cualquiera, 4 años | 6 | Absorción |
| **Cerveza de Miel** | Trigo ×4, Botella de miel ×2 | 8 min | — | roble, 3 años | 6 | Absorción |
| **Cerveza de Jengibre** | Trigo ×4, Helecho ×3, Azúcar ×2 | 6 min | — | cualquiera, 2 años | 4 | Velocidad |
| **Escudo** | Trigo ×4, Azúcar ×1 | 4 min | — | cualquiera, 2 años | 5 | — |
| **Cristal** | Trigo ×5 | 3 min | — | cualquiera, 1 años | 4 | — |
| **Baltica** | Trigo ×6, Pepita de hierro ×1 | 4 min | — | cualquiera, 1 años | 5 | — |
| **Becker** | Trigo ×5, Azúcar ×1 | 3 min | — | cualquiera, 1 años | 4 | — |
| **Royal Guard** | Trigo ×6, Azúcar ×1 | 5 min | — | abedul, 3 años | 5 | — |
| **Kross Golden** | Trigo ×7 | 6 min | — | roble, 4 años | 6 | — |

### Vinos, fermentados e hidromieles

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Vino Tinto** | Bayas dulces ×5 | 5 min | — | cualquiera, 20 años | 8 | — |
| **Vino Blanco** | Manzana ×4, Azúcar ×2 | 6 min | — | abedul, 15 años | 7 | — |
| **Vino de Manzana** | Manzana ×8, Azúcar ×3 | 7 min | — | roble, 12 años | 8 | — |
| **Vino de Bayas** | Bayas dulces ×10, Azúcar ×3 | 6 min | — | roble oscuro, 14 años | 9 | — |
| **Champán** | Bayas dulces ×6, Azúcar ×4, Botella de miel ×1 | 8 min | — | abedul, 18 años | 10 | Velocidad, Salto |
| **Sangría** | Bayas dulces ×5, Manzana ×2, Azúcar ×3 | 6 min | — | cualquiera, 2 años | 7 | Regeneración |
| **Tinto de Verano** | Bayas dulces ×3, Bola de slime ×1, Azúcar ×2 | 2 min | — | cualquiera, 1 años | 7 | — |
| **Rebujito** | Trigo ×3, Bola de slime ×1, Helecho ×1 | 3 min | — | cualquiera, 1 años | 9 | — |
| **Kalimotxo** | Bayas dulces ×3, Cacao ×1, Azúcar ×2 | 2 min | — | cualquiera, 1 años | 8 | — |
| **Sidra de Manzana** | Manzana ×14 | 7 min | — | cualquiera, 3 años | 7 | — |
| **Sake** | Trigo ×8, Caña de azúcar ×3 | 10 min | 2 | bambú, 6 años | 15 | Velocidad, Regeneración |
| **Umeshu** | Bayas dulces ×8, Azúcar ×4, Trigo ×5 | 10 min | 1 | abedul, 12 años | 12 | Regeneración |
| **Pulque** | Cactus ×6, Azúcar ×2, Botella de miel ×1 | 4 min | — | cualquiera, 1 años | 8 | Saturación |
| **Hidromiel** | Caña de azúcar ×6 | 3 min | — | roble, 4 años | 9 | — |
| **Hidromiel Dulce de Manzana** | Caña de azúcar ×6, Manzana ×2 | 4 min | — | roble, 4 años | 11 | Resp. acuática |
| **Hidromiel de Bayas** | Botella de miel ×3, Bayas dulces ×5 | 5 min | — | roble, 5 años | 10 | Regeneración, Saturación |

### Destilados

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Whiskey** | Trigo ×10 | 10 min | 2 | abeto, 18 años | 26 | — |
| **Whiskey Ardiente** | Trigo ×10, Polvo de blaze ×2 | 12 min | 3 | abeto, 18 años | 28 | — |
| **Bourbon** | Trigo ×12, Azúcar ×2 | 12 min | 2 | roble, 20 años | 28 | Fuerza |
| **Ron Especiado** | Caña de azúcar ×18 | 6 min | 2 | roble, 14 años | 30 | Resist. al fuego, Veneno |
| **Cachaza** | Caña de azúcar ×14 | 8 min | 2 | roble, 3 años | 25 | Velocidad |
| **Vodka** | Papa ×10 | 15 min | 3 | — | 20 | Debilidad, Veneno |
| **Vodka Dorado** | Papa ×10, Pepita de oro ×2 | 18 min | 3 | — | 20 | Debilidad, Veneno |
| **Vodka de Melón** | Rodaja de melón ×8, Papa ×6 | 16 min | 3 | — | 18 | Velocidad |
| **Vodka de Champiñón** | Papa ×10, Champiñón rojo ×3, Champiñón marrón ×3 | 18 min | 5 | — | 18 | Debilidad, Náusea, Visión nocturna, Ceguera, Lentitud |
| **Ginebra** | Trigo ×9, Flores azules ×6, Manzana ×1 | 6 min | 2 | — | 20 | — |
| **Tequila** | Cactus ×8 | 15 min | 2 | abedul, 12 años | 20 | — |
| **Absenta** | Algas ×15 | 3 min | 6 | — | 42 | Veneno |
| **Absenta Verde** | Algas ×17, Papa venenosa ×2 | 5 min | 6 | — | 46 | Veneno, Daño, Visión nocturna |
| **Brandy** | Bayas dulces ×10, Azúcar ×2 | 12 min | 3 | roble, 15 años | 18 | Resistencia |
| **Coñac** | Bayas dulces ×12 | 14 min | 4 | roble, 24 años | 22 | Absorción |
| **Grappa** | Bayas dulces ×14 | 10 min | 4 | cualquiera, 4 años | 30 | Resist. al fuego |
| **Licor de Manzana** | Manzana ×12 | 16 min | 3 | acacia, 6 años | 14 | — |
| **Shochu** | Papa ×8, Trigo ×4 | 14 min | 3 | — | 25 | Resist. al fuego |
| **Licor Casero** | Trigo ×12, Azúcar ×6 | 5 min | 5 | — | 45 | Ceguera, Náusea, Veneno, Velocidad |
| **Espíritu de Remolacha** | Remolacha ×8, Azúcar ×2 | 8 min | 3 | cualquiera, 4 años | 15 | Salud extra |

### Licores

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Licor de Diente de León** | Diente de león ×8, Azúcar ×3 | 5 min | 2 | cualquiera, 3 años | 12 | Regeneración |
| **Licor de Amapola** | Amapola ×6, Trigo ×3 | 6 min | 2 | cualquiera, 5 años | 13 | Lentitud, Regeneración |
| **Licor de Bambú** | Bambú ×10, Azúcar ×3 | 7 min | 2 | bambú, 6 años | 14 | Salto |
| **Amaretto** | Trigo ×6, Cacao ×4, Azúcar ×3 | 8 min | 3 | roble, 10 años | 16 | Regeneración |
| **Licor de Cereza** | Bayas dulces ×8, Azúcar ×4 | 6 min | 2 | cerezo, 8 años | 14 | Regeneración, Velocidad |
| **Licor de Café** | Cacao ×10, Azúcar ×4, Balde de leche ×1 | 5 min | 2 | roble oscuro, 6 años | 15 | Velocidad, Prisa |
| **Limoncello** | Azúcar ×6, Trigo ×4 | 10 min | 2 | cualquiera, 4 años | 25 | Prisa |
| **Ponche de Huevo** | Huevo ×5, Azúcar ×2, Balde de leche ×1 | 2 min | — | cualquiera, 3 años | 10 | — |

### Cócteles

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Piña Colada** | Rodaja de melón ×6, Caña de azúcar ×4, Balde de leche ×1 | 3 min | 1 | — | 8 | Resp. acuática |
| **Ponche de Frutas** | Manzana ×3, Bayas dulces ×3, Rodaja de melón ×3, Azúcar ×2 | 4 min | — | cualquiera, 1 años | 5 | Regeneración, Saturación |
| **Matcha Highball** | Helecho ×4, Trigo ×6, Bola de nieve ×1 | 3 min | — | — | 10 | Salto, Velocidad |
| **Margarita** | Cactus ×4, Azúcar ×2, Bola de nieve ×1 | 3 min | — | — | 16 | Velocidad |
| **Mojito** | Caña de azúcar ×4, Helecho ×3, Azúcar ×2, Bola de nieve ×2 | 3 min | — | — | 12 | Salto, Regeneración |
| **Café Irlandés** | Cacao ×6, Trigo ×4, Azúcar ×2, Balde de leche ×1 | 4 min | — | — | 14 | Regeneración, Absorción |
| **Moscow Mule** | Papa ×4, Helecho ×2, Bola de nieve ×2 | 3 min | — | — | 12 | Velocidad, Resist. al fuego |
| **Daiquiri** | Caña de azúcar ×3, Bayas dulces ×3 | 3 min | 1 | cualquiera, 1 años | 12 | — |
| **Cosmopolitan** | Papa ×2, Bayas dulces ×2 | 3 min | 1 | cualquiera, 1 años | 14 | — |
| **Martini** | Trigo ×3, Helecho ×1, Algas ×1 | 4 min | 2 | abedul, 2 años | 18 | — |
| **Manhattan** | Trigo ×4, Bayas dulces ×1 | 5 min | 2 | roble, 3 años | 20 | — |
| **Negroni** | Helecho ×2, Bayas dulces ×2, Algas ×1 | 4 min | 1 | abedul, 2 años | 22 | — |
| **Old Fashioned** | Trigo ×4, Azúcar ×1, Zanahoria ×1 | 4 min | 2 | roble, 3 años | 24 | — |
| **Bloody Mary** | Papa ×3, Remolacha ×2, Polvo de blaze ×1 | 4 min | 1 | cualquiera, 1 años | 12 | Veneno |
| **Mai Tai** | Caña de azúcar ×4, Bayas dulces ×1 | 4 min | 1 | cualquiera, 1 años | 18 | — |
| **Caipirinha** | Caña de azúcar ×4, Azúcar ×2, Helecho ×1 | 3 min | — | cualquiera, 1 años | 15 | — |
| **White Russian** | Papa ×3, Cacao ×2, Balde de leche ×1 | 4 min | 1 | cualquiera, 1 años | 16 | — |
| **Black Russian** | Papa ×3, Cacao ×3 | 4 min | 1 | cualquiera, 1 años | 20 | — |
| **Espresso Martini** | Papa ×3, Cacao ×4 | 5 min | 2 | cualquiera, 1 años | 18 | — |
| **Aperol Spritz** | Helecho ×2, Bayas dulces ×2 | 3 min | — | cualquiera, 1 años | 11 | — |
| **Gin Tonic** | Trigo ×3, Helecho ×2, Bola de nieve ×1 | 4 min | 2 | cualquiera, 1 años | 14 | — |
| **Cuba Libre** | Caña de azúcar ×3, Azúcar ×2, Helecho ×1 | 3 min | 1 | cualquiera, 1 años | 14 | — |
| **Tequila Sunrise** | Cactus ×3, Bayas dulces ×2, Azúcar ×1 | 4 min | 1 | cualquiera, 1 años | 14 | — |
| **Long Island Iced Tea** | Papa ×1, Cactus ×1, Caña de azúcar ×1, Trigo ×1 | 6 min | 2 | cualquiera, 1 años | 26 | — |
| **Paloma** | Cactus ×3, Rodaja de melón ×1, Azúcar ×1 | 3 min | 1 | cualquiera, 1 años | 15 | — |
| **Michelada** | Trigo ×4, Polvo de blaze ×1, Bola de slime ×1 | 2 min | — | cualquiera, 1 años | 6 | — |
| **Dark 'n' Stormy** | Caña de azúcar ×4, Helecho ×1, Bola de slime ×1 | 4 min | 1 | cualquiera, 2 años | 17 | — |
| **Blue Hawaiian** | Caña de azúcar ×3, Lapislázuli ×1, Rodaja de melón ×2 | 3 min | — | cualquiera, 1 años | 14 | — |
| **Zombie** | Caña de azúcar ×6, Bayas dulces ×2, Azúcar ×2 | 5 min | 2 | cualquiera, 3 años | 28 | — |
| **Huracán** | Caña de azúcar ×5, Rodaja de melón ×2, Manzana ×1 | 4 min | 1 | cualquiera, 2 años | 22 | — |
| **B-52** | Cacao ×2, Balde de leche ×1, Bayas dulces ×2 | 6 min | — | — | 20 | — |
| **Jägerbomb** | Helecho ×4, Azúcar ×4, Pepita de oro ×1 | 3 min | — | — | 22 | Velocidad |
| **Agua de Valencia** | Trigo ×2, Papa ×2, Rodaja de melón ×2, Azúcar ×2 | 4 min | 1 | cualquiera, 1 años | 18 | — |
| **Ponche Crema** | Balde de leche ×2, Huevo ×1, Caña de azúcar ×3, Azúcar ×2 | 5 min | 1 | cualquiera, 2 años | 15 | — |
| **Coquito** | Balde de leche ×2, Caña de azúcar ×4, Helecho ×1 | 4 min | 1 | cualquiera, 2 años | 17 | — |
| **Pimm's Cup** | Bayas dulces ×2, Manzana ×1, Helecho ×1, Bola de slime ×1 | 3 min | — | cualquiera, 1 años | 11 | — |
| **Fernet con Cola** | Helecho ×5, Cacao ×1, Azúcar ×2 | 4 min | 1 | cualquiera, 2 años | 16 | — |
| **Campari Orange** | Tinte rojo ×1, Rodaja de melón ×2, Azúcar ×1 | 3 min | 1 | cualquiera, 1 años | 12 | — |
| **Shot de Tequila** | Cactus ×4, Bola de slime ×1 | 2 min | 1 | cualquiera, 1 años | 20 | — |
| **Mint Julep** | Trigo ×4, Helecho ×2, Azúcar ×2 | 4 min | 1 | cualquiera, 2 años | 18 | — |
| **Amaretto Sour** | Cacao ×1, Azúcar ×2, Huevo ×1 | 3 min | — | — | 10 | Regeneración |
| **Pisco Punch** | Caña de azúcar ×5, Bayas dulces ×3, Azúcar ×2 | 4 min | — | — | 12 | Velocidad |
| **French 75** | Trigo ×3, Flores azules ×1, Azúcar ×2 | 3 min | 1 | — | 15 | — |
| **Tom Collins** | Trigo ×4, Flores azules ×2, Azúcar ×1 | 2 min | — | — | 11 | Prisa |
| **Gimlet** | Trigo ×4, Flores azules ×2, Algas ×1 | 2 min | — | — | 14 | — |
| **Sidecar** | Bayas dulces ×6, Azúcar ×3 | 6 min | 2 | — | 18 | — |
| **Rusty Nail** | Trigo ×8, Botella de miel ×1 | 8 min | 2 | — | 22 | — |
| **Penicillin** | Trigo ×8, Botella de miel ×2 | 7 min | 2 | — | 20 | Regeneración, Salud extra |
| **Bramble** | Trigo ×4, Flores azules ×2, Bayas dulces ×5 | 3 min | — | — | 13 | — |

### Sin alcohol y refrescos

| Bebida | Ingredientes | Cocción | Destilar | Barril | Alc. | Efectos |
|---|---|---:|---:|---|---:|---|
| **Café** | Cacao ×12, Balde de leche ×2 | 2 min | — | — | -6 | Regeneración, Velocidad |
| **Chocolate Caliente** | Cacao ×3 | 2 min | — | — | — | Prisa |
| **Chocolate con Leche** | Cacao ×5, Balde de leche ×2, Azúcar ×2 | 3 min | — | — | — | Regeneración, Saturación |
| **Café Helado** | Cacao ×8, Bola de nieve ×4, Balde de leche ×1 | 1 min | — | — | -8 | Regeneración, Velocidad |
| **Sopa de Papa** | Papa ×5, Algas ×3 | 3 min | — | — | — | Curación |
| **Té Helado** | Helecho ×4, Azúcar ×3, Bola de nieve ×2 | 2 min | — | — | — | Velocidad, Regeneración |
| **Limonada** | Azúcar ×4, Helecho ×2, Bola de nieve ×2 | 1 min | — | — | — | Velocidad, Regeneración |
| **Agua de Jamaica** | Amapola ×4, Bayas dulces ×3, Azúcar ×3 | 3 min | — | — | — | Regeneración |
| **Mate Cocido** | Helecho ×6, Azúcar ×1 | 2 min | — | — | -4 | Velocidad, Prisa, Regeneración |
| **Piña Colada Virgen** | Rodaja de melón ×4, Azúcar ×2, Balde de leche ×1, Bola de nieve ×2 | 2 min | — | — | — | Saturación |
| **Monster Energy** | Azúcar ×5, Cactus ×1, Bola de slime ×1 | 2 min | — | — | — | Velocidad |
| **Red Bull** | Azúcar ×4, Pepita de oro ×1 | 2 min | — | — | — | Velocidad |
| **Coca Cola** | Azúcar ×5, Cacao ×1 | 1 min | — | — | — | — |
| **Sprite** | Azúcar ×3, Helecho ×1 | 1 min | — | — | — | — |
| **Fanta** | Azúcar ×4, Zanahoria ×1 | 1 min | — | — | — | — |
| **Pepsi** | Azúcar ×4, Cacao ×1 | 1 min | — | — | — | — |
| **7Up** | Azúcar ×3, Bola de slime ×1 | 1 min | — | — | — | — |
| **Dr Pepper** | Azúcar ×4, Bayas dulces ×1 | 1 min | — | — | — | — |
| **Mountain Dew** | Azúcar ×5, Cactus ×1 | 1 min | — | — | — | — |
| **Crush** | Azúcar ×4, Zanahoria ×2 | 1 min | — | — | — | — |
| **Kem Piña** | Azúcar ×4, Esponja ×1 | 1 min | — | — | — | — |
| **Bilz** | Azúcar ×4, Tinte rojo ×1 | 1 min | — | — | — | — |
| **Pap** | Azúcar ×4, Tinte amarillo ×1 | 1 min | — | — | — | — |
| **Limon Soda** | Azúcar ×3, Bola de slime ×1, Bola de nieve ×1 | 1 min | — | — | — | — |
| **Sangrita** | Remolacha ×3, Polvo de blaze ×1, Rodaja de melón ×1 | 2 min | — | — | — | Resist. al fuego |
<!-- AUTO:fin brewery -->

***

## 📜 Comandos

El comando principal es **`/breweryx`**, y también funcionan **`/brewery`** y **`/brew`**.

| Comando | Descripción |
|---|---|
| `/brew info` | Muestra tu nivel de borrachera actual |
| `/brew unlabel` | Quita partes de la etiqueta de la bebida que tienes en la mano |
| `/brew version` | Información del plugin |

{% hint style="info" %}
El tiempo de cocción, las destilaciones y los años de añejado deben ser **exactos**. Experimenta con una tanda pequeña, mira el reloj y anota los tiempos que te funcionan.
{% endhint %}
