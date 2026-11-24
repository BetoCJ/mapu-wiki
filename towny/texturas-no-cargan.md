# 🎨 Mis texturas no cargan (modo texturas ligero)

_Actualizado el 23/11/2026._

Algunas tarjetas gráficas o drivers antiguos (por ejemplo AMD o Intel viejos en Windows, y algunos equipos con Linux) no pueden dibujar las **armaduras 3D** de Mapucraft. Cuando eso pasa, Minecraft descarta **todo** el paquete de texturas del servidor y se ve vanilla: mobs raros, ítems sin textura, menús sin íconos.

Para eso existe el **modo texturas ligero**: las armaduras personalizadas se ven **planas**, pero **el resto de las texturas funciona normal**.

## ¿Se activa solo?
Sí. Si tu equipo falla al cargar las texturas, el servidor lo detecta y te reenvía el paquete en modo ligero. En computadores lentos puede tardar unos minutos en terminar de cargar: espera con la pantalla de carga.

## Comandos
| Comando | Qué hace |
|---|---|
| `/texturasligero ligero` (o `/modoligero ligero`) | Activa el modo ligero a mano. |
| `/texturasligero completo` | Vuelve al modo completo con armaduras 3D. |
| `/texturasligero estado` | Te dice en qué modo estás. |
| `/texturas` | Vuelve a pedir el paquete de texturas del servidor. |

Cada cambio de modo recarga tus texturas, así que hay una pequeña espera entre uno y otro.

## Si sigue sin cargar
1. Actualiza el driver de tu tarjeta gráfica (AMD, Intel o NVIDIA) desde la página del fabricante. En Linux, actualiza Mesa/tu distribución.
2. Prueba `/texturasligero ligero` y reentra al servidor.
   - Si juegas con **Iris/shaders** (por ejemplo Complementary), desactiva el shaderpack mientras cargan las texturas: compilar los shaders bloquea el juego varios segundos y el servidor puede desconectarte por tiempo de espera.
   - Es normal que el primer ingreso tarde varios minutos en equipos lentos; si te desconecta, vuelve a entrar y el servidor te activa el modo ligero solo.
3. Abre un ticket en el [Discord](https://discord.gg/YDJKpgEU3m) y adjunta el archivo `logs/latest.log` de **la sesión en que entraste al servidor** (si cerraste el juego y lo abriste de nuevo, usa el archivo con fecha de esa sesión dentro de `logs`).

## Preguntas frecuentes
- **¿Pierdo algo en modo ligero?** Solo el efecto 3D de las armaduras personalizadas; se ven en versión plana. Todo lo demás es igual.
- **¿Afecta a Bedrock?** No: en Bedrock las texturas van por otro camino y no necesitas esto.
- **¿Lo puedo desactivar?** Sí, con `/texturasligero completo`.
