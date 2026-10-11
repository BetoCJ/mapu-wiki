# Herramientas de la wiki

Generadores en Python (solo librería estándar, no necesitan PyYAML: traen un parser YAML mínimo en `miniyaml.py`) que mantienen al día partes de la wiki a partir de los datos reales del servidor.

Solo reescriben lo que está entre estos marcadores; todo el texto escrito a mano alrededor se conserva:

```
<!-- AUTO:inicio nombre -->
...contenido generado...
<!-- AUTO:fin nombre -->
```

Si la página no tiene los marcadores, la sección se agrega al final. Son idempotentes: ejecutarlos dos veces seguidas no cambia nada la segunda vez. **Nunca se leen contraseñas, tokens ni webhooks**: solo cajas, recetas y precios.

## Cómo ejecutarlos

Desde la carpeta `MAPUCRAFT`:

```
bot\.venv\Scripts\python.exe wiki\tools\generar_wiki.py --dry-run     # ver qué cambiaría, sin escribir
bot\.venv\Scripts\python.exe wiki\tools\generar_wiki.py               # escribir todo
bot\.venv\Scripts\python.exe wiki\tools\generar_wiki.py --solo cajas  # cajas | crafteos | mercado
bot\.venv\Scripts\python.exe wiki\tools\generar_comandos.py           # guía de comandos
```

Cualquier Python 3.8+ sirve. Los scripts leen la copia local `Towny-26-3\plugins` (solo lectura).

## Cuándo ejecutarlos

| Cambiaste... | Descarga la carpeta del plugin y ejecuta | Páginas que se actualizan |
|---|---|---|
| Cajas, llaves o premios (ExcellentCrates) | `generar_wiki.py --solo cajas` | `towny/cajas.md` (sección `cajas`) |
| Recetas (CraftEnhance, `recipes.db`) | `generar_wiki.py --solo crafteos` | `towny/crafteos.md` (sección `crafteos`) |
| Precios o ítems del mercado (Nascraft) | `generar_wiki.py --solo mercado` | `towny/economia/mercado.md` (sección `mercado`) |
| Un comando nuevo o cambiado | editar `comandos.yml` y ejecutar `generar_comandos.py` | `el-servidor/comandos.md`, `bot/GUIA_TOWNY.md`, `bot/servidor-towny/comandos.json` |

Flujo recomendado después de cambiar un plugin: bajar la carpeta actualizada a `Towny-26-3\plugins`, ejecutar con `--dry-run`, revisar el diff y ejecutar de verdad.

## Guía de comandos (`comandos.yml`)

Es la **fuente única** de los comandos. Cada comando tiene `name` (único, es lo que se muestra), `descripcion`, `permiso` (rango o permiso necesario, `todos` si no pide nada), `modo` (`towny`, `skyblock`, `ambos` o `discord`) y opcionalmente `alias`. El generador valida que los nombres no se repitan, que los campos existan y que cada embed respete los límites de Discord (4096 en descripción, 1024 por campo, 6000 en total).

Para actualizar el canal de Discord, `bot/servidor-towny/guia_comandos.js` lee `comandos.json` (no hay textos duplicados en el JS). `SOLO_REVISAR=1 node guia_comandos.js <carpeta-del-bot>` solo comprueba los límites sin publicar.

## Qué no se genera

- **Rangos**: LuckPerms solo guarda los grupos y sus permisos, y no hay menú de rangos en DeluxeMenus; los requisitos de `/rankup` no están en los archivos locales. `towny/rangos.md` sigue siendo manual.
- **Skyblock**: no hay configs locales de ese modo, así que ninguna página de `skyblock/` se genera. Ver `PENDIENTES.md`.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `generar_wiki.py` | Cajas, crafteos y mercado |
| `generar_comandos.py` | Guía de comandos (wiki, `GUIA_TOWNY.md` y JSON del bot) |
| `comandos.yml` | Fuente única de comandos |
| `miniyaml.py` | Parser YAML mínimo (usa PyYAML si está instalado) |
| `PENDIENTES.md` | Revisiones pendientes, sobre todo de Skyblock |
