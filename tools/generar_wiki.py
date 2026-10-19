#!/usr/bin/env python3
"""Genera secciones de la wiki a partir de las configs locales de los plugins.

Reescribe SOLO lo que hay entre `<!-- AUTO:inicio nombre -->` y `<!-- AUTO:fin nombre -->`.
Si la pagina no tiene los marcadores, agrega la seccion al final. Es idempotente.

Uso:
    python generar_wiki.py                 # todo
    python generar_wiki.py --solo cajas    # cajas | crafteos | mercado | encantamientos | mascotas | battlepass
    python generar_wiki.py --dry-run       # solo muestra que cambiaria
Nunca lee contrasenas ni tokens: solo cajas, recetas y precios.
"""
import argparse
import difflib
import gzip
import re
import sqlite3
import struct
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import miniyaml  # noqa: E402

WIKI = AQUI.parent
RAIZ = WIKI.parent
PLUGINS = RAIZ / 'Towny-26-3' / 'plugins'

# ---------------------------------------------------------------- utilidades


def limpia(txt):
    """Quita codigos de color (&x, §x, <tags>) y espacios sobrantes."""
    if txt is None:
        return ''
    txt = str(txt)
    # texto ofuscado (§k + letras repetidas, solo decoracion)
    txt = re.sub(r'[§�]k([a-z])\1*(?=[§�\s]|$)', '', txt)
    txt = re.sub('(?:&[0-9a-fk-orA-FK-OR]|[§�].)', '', txt)
    txt = re.sub('<[^<>]{1,60}>', '', txt)
    return re.sub(r'\s+', ' ', txt).strip()


def titulo(clave):
    return clave.replace('minecraft:', '').replace('_', ' ').strip().title()


def num(x, dec=2):
    s = f'{x:.{dec}f}'.rstrip('0').rstrip('.')
    return s or '0'


def md(txt):
    return str(txt).replace('|', '\\|').replace('\n', ' ')


def inyecta(pagina, nombre, cuerpo, dry, titulo_si_falta=None):
    """Reemplaza el bloque AUTO `nombre` en `pagina` (o lo agrega al final)."""
    ini = f'<!-- AUTO:inicio {nombre} -->'
    fin = f'<!-- AUTO:fin {nombre} -->'
    bloque = f'{ini}\n{cuerpo.rstrip()}\n{fin}'
    viejo = pagina.read_text(encoding='utf-8') if pagina.exists() else None
    if viejo is None:
        nuevo = (titulo_si_falta or '') + bloque + '\n'
    elif ini in viejo and fin in viejo:
        a, b = viejo.index(ini), viejo.index(fin) + len(fin)
        nuevo = viejo[:a] + bloque + viejo[b:]
    else:
        nuevo = viejo.rstrip('\n') + '\n\n***\n\n' + bloque + '\n'
    cambia = nuevo != viejo
    try:
        rel = pagina.relative_to(WIKI).as_posix()
    except ValueError:
        rel = pagina.relative_to(RAIZ).as_posix()
    if dry:
        if cambia:
            diff = list(difflib.unified_diff((viejo or '').splitlines(), nuevo.splitlines(), rel, rel, lineterm='', n=0))
            print(f'[dry-run] {rel}: cambiaria ({len(diff)} lineas de diff)')
            for ln in diff[:12]:
                print('   ', ln[:140])
        else:
            print(f'[dry-run] {rel}: sin cambios')
    elif cambia:
        pagina.parent.mkdir(parents=True, exist_ok=True)
        pagina.write_text(nuevo, encoding='utf-8', newline='\n')
        print(f'escrito {rel} ({nuevo.count(chr(10))} lineas)')
    else:
        print(f'sin cambios {rel}')
    return cambia

# --------------------------------------------------------------------- cajas


def _snbt_bloque(s, i):
    """Devuelve el trozo SNBT equilibrado que empieza en s[i] ('{', '[' o comillas)."""
    if s[i] in '"\'':
        q = s[i]
        j = i + 1
        while j < len(s) and s[j] != q:
            j += 2 if s[j] == '\\' else 1
        return s[i:j + 1]
    abre = s[i]
    cierra = '}' if abre == '{' else ']'
    prof, j, q = 0, i, None
    while j < len(s):
        c = s[j]
        if q:
            if c == '\\':
                j += 1
            elif c == q:
                q = None
        elif c in '"\'':
            q = c
        elif c == abre:
            prof += 1
        elif c == cierra:
            prof -= 1
            if prof == 0:
                return s[i:j + 1]
        j += 1
    return s[i:]


def nombre_item(valor):
    """Saca nombre y cantidad de un SNBT de ExcellentCrates."""
    valor = str(valor or '')
    cant = re.search(r'count:(\d+)', valor)
    cant = int(cant.group(1)) if cant else 1
    ident = re.search(r'id:"([^"]+)"', valor)
    ident = ident.group(1) if ident else ''
    m = re.search(r'"minecraft:custom_name":', valor)
    nombre = ''
    if m:
        j = m.end()
        while j < len(valor) and valor[j] == ' ':
            j += 1
        trozo = _snbt_bloque(valor, j)
        textos = re.findall(r'text:"((?:[^"\\]|\\.)*)"', trozo)
        if not textos and trozo[:1] in '"\'':
            textos = [trozo[1:-1]]
        nombre = limpia(''.join(textos))
        nombre = re.sub(r"[^\w\s.,:()\-+/%'¡!¿?$⛃]", '', nombre).strip()
    if not nombre:
        nombre = titulo(ident) or '(sin nombre)'
    return nombre, cant


def nombre_premio(r, rid=''):
    if r.get('Name'):
        return limpia(r['Name']), 1
    pd = (r.get('PreviewData') or {}).get('Data') or {}
    n, c = nombre_item(pd.get('Value'))
    if n == 'Player Head' and rid:
        n = titulo(rid)
    if n == '(sin nombre)':
        for it in (r.get('ItemsData') or {}).values():
            n, c = nombre_item(((it or {}).get('Data') or {}).get('Value'))
            break
    return n, c


def gen_cajas():
    base = PLUGINS / 'ExcellentCrates'
    cfg = miniyaml.cargar(base / 'config.yml')
    rar = (cfg.get('Rewards') or {}).get('Rarities') or {}
    nom_rar = {k: limpia(v.get('Name', k)) for k, v in rar.items()}
    orden_rar = list(nom_rar)
    llaves = {}
    for f in sorted((base / 'keys').glob('*.yml')):
        llaves[f.stem] = limpia(miniyaml.cargar(f).get('Name', f.stem))
    cajas = []
    for f in sorted((base / 'crates').glob('*.yml')):
        d = miniyaml.cargar(f)
        lista = ((d.get('Rewards') or {}).get('List')) or {}
        costos = d.get('Costs') or {}
        kid = next((c.get('KeyId') for c in costos.values() if isinstance(c, dict) and c.get('KeyId')), None)
        premios = []
        total = sum(float(r.get('Weight', 0) or 0) for r in lista.values())
        for rid, r in lista.items():
            n, c = nombre_premio(r, rid)
            w = float(r.get('Weight', 0) or 0)
            premios.append((n, c, str(r.get('Rarity', '')), w, (w / total * 100) if total else 0))
        cajas.append(dict(id=f.stem, nombre=limpia(d.get('Name', f.stem)), llave=llaves.get(kid, kid) if kid else None,
                          premios=premios, total=total))
    L = ['## 📊 Tablas completas de premios (generado)', '',
         '> Esta sección se genera automáticamente desde la configuración de las cajas. '
         'La probabilidad es el peso del premio dividido por el peso total de la caja. '
         'Para actualizarla: `python wiki/tools/generar_wiki.py --solo cajas`.', '',
         f'Cajas registradas: **{len(cajas)}**. Rarezas: ' + ' · '.join(nom_rar[k] for k in orden_rar) + '.', '']
    MAX = 60
    for c in cajas:
        L.append(f'### {c["nombre"]}')
        L.append('')
        L.append(f'Llave: **{c["llave"] or "—"}** · Premios: **{len(c["premios"])}**')
        L.append('')
        if not c['premios']:
            L += ['_Sin premios configurados._', '']
            continue
        resumen = {}
        for _, _, ra, w, p in c['premios']:
            n, s = resumen.get(ra, (0, 0))
            resumen[ra] = (n + 1, s + p)
        L += ['| Rareza | Premios | Probabilidad total |', '|---|---|---|']
        claves = sorted(resumen, key=lambda k: orden_rar.index(k) if k in orden_rar else 99)
        for k in claves:
            n, s = resumen[k]
            L.append(f'| {md(nom_rar.get(k, k or "—"))} | {n} | {num(s)}% |')
        L.append('')
        ordenados = sorted(c['premios'], key=lambda x: (x[3], x[0]))
        L += ['| Premio | Rareza | Probabilidad |', '|---|---|---|']
        for n, cant, ra, w, p in ordenados[:MAX]:
            etiqueta = md(n) + (f' x{cant}' if cant > 1 else '')
            L.append(f'| {etiqueta} | {md(nom_rar.get(ra, ra or "—"))} | {num(p)}% |')
        if len(ordenados) > MAX:
            L.append(f'| _… y {len(ordenados) - MAX} premios más (los más comunes)_ | | |')
        L.append('')
    return '\n'.join(L), dict(cajas=len(cajas), premios=sum(len(c['premios']) for c in cajas))

# ------------------------------------------------------------------ crafteos


def _cantidad(blob):
    try:
        d = gzip.decompress(blob)
    except Exception:
        return 1
    m = re.search(rb'\x03\x00\x05count(.{4})', d, re.S)
    return struct.unpack('>i', m.group(1))[0] if m else 1


def gen_crafteos():
    ruta = PLUGINS / 'CraftEnhance' / 'recipes.db'
    con = sqlite3.connect(f'file:{ruta.as_posix()}?mode=ro', uri=True)
    cats = {}
    txt = (PLUGINS / 'CraftEnhance' / 'categorys.yml').read_text(encoding='utf-8')
    for m in re.finditer(r'display_name:\s*(.+)\n\s+name:\s*(\S+)', txt):
        cats[m.group(2)] = limpia(m.group(1).strip('\'"'))
    recetas = con.execute('select id,category,shapeless,hidden from recipes').fetchall()
    items = {}
    for rid, slot, name, blob, tipo in con.execute('select recipe_id,slot,name,item_nbt,type from items'):
        items.setdefault(rid, {})[slot] = (limpia(name), _cantidad(blob), tipo)
    mundos = {}
    for rid, w in con.execute('select recipe_id,world from allowed_worlds'):
        mundos.setdefault(rid, []).append(w)

    def legible(n):
        if n.upper() == 'AIR':
            return '—'
        return titulo(n) if re.fullmatch(r'[A-Z0-9_]+', n) else n

    por_cat = {}
    for rid, cat, shapeless, hidden in recetas:
        it = items.get(rid, {})
        res = it.get(9)
        if not res:
            continue
        por_cat.setdefault(cat, []).append((rid, res, it, bool(shapeless), bool(hidden)))
    L = ['## 📜 Recetas del servidor (generado)', '',
         '> Esta sección se genera automáticamente desde CraftEnhance. Cada receta muestra la cuadrícula de '
         'la mesa de crafteo fila por fila (de arriba hacia abajo); `—` es una casilla vacía. '
         'Los ingredientes con nombre propio son ítems custom del servidor. '
         'Para actualizarla: `python wiki/tools/generar_wiki.py --solo crafteos`.', '',
         f'Total de recetas: **{sum(len(v) for v in por_cat.values())}** en **{len(por_cat)}** categorías.', '']
    for cat in sorted(por_cat, key=lambda c: (c == 'default', cats.get(c, c).lower())):
        rs = sorted(por_cat[cat], key=lambda r: (r[1][0].lower(), r[0]))
        L.append(f'### {md(cats.get(cat, cat.title()))} ({len(rs)})')
        L.append('')
        for rid, res, it, shapeless, hidden in rs:
            nombre = md(legible(res[0]))
            cant = f' x{res[1]}' if res[1] > 1 else ''
            filas = []
            for r in range(3):
                celdas = []
                for c in range(3):
                    g = it.get(r * 3 + c)
                    if not g or g[0].upper() == 'AIR':
                        celdas.append('—')
                    else:
                        celdas.append(md(legible(g[0])) + (f' x{g[1]}' if g[1] > 1 else ''))
                filas.append(celdas)
            filas = [f for f in filas if any(x != '—' for x in f)]
            forma = ' / '.join(' · '.join(f) for f in filas) if filas else '—'
            extra = ''
            if mundos.get(rid):
                extra = f' _(solo en {", ".join(sorted(mundos[rid]))})_'
            L.append(f'- **{nombre}**{cant}{extra}: {forma}')
        L.append('')
    return '\n'.join(L), dict(recetas=sum(len(v) for v in por_cat.values()), categorias=len(por_cat))

# ------------------------------------------------------------------ mercado


def gen_mercado():
    base = PLUGINS / 'Nascraft'
    items = miniyaml.cargar(base / 'items.yml').get('items') or {}
    cats = miniyaml.cargar(base / 'categories.yml').get('categories') or {}
    precio, alias, hijos = {}, {}, {}
    for k, v in items.items():
        v = v or {}
        precio[k] = float(v.get('initial-price', 0) or 0)
        alias[k] = v.get('alias')
        for hk, hv in (v.get('child') or {}).items():
            hv = hv or {}
            precio[hk] = precio[k] * float(hv.get('multiplier', 1) or 1)
            alias[hk] = hv.get('alias')
            hijos.setdefault(k, []).append(hk)

    def nom(k):
        return limpia(alias.get(k)) or titulo(k)

    def fmt(p):
        return '$' + (f'{p:,.2f}' if p < 100 else f'{p:,.0f}')

    usados = set()
    L = ['## 💹 Precios base por categoría (generado)', '',
         '> Esta sección se genera automáticamente desde Nascraft. Son los precios **iniciales**; '
         'el precio real sube o baja según la oferta y la demanda (ver `/market`). '
         'Las variantes (losas, escaleras, etc.) se derivan del ítem principal. '
         'Para actualizarla: `python wiki/tools/generar_wiki.py --solo mercado`.', '']
    total_items = 0
    for cid in sorted(cats, key=lambda x: int(x) if str(x).isdigit() else 999):
        c = cats[cid] or {}
        lista = [i for i in (c.get('items') or []) if i in precio]
        if not lista:
            continue
        L.append(f'### {md(limpia(c.get("display-name", cid)))}')
        L += ['', '| Ítem | Precio base |', '|---|---|']
        for k in lista:
            usados.add(k)
            L.append(f'| {md(nom(k))} | {fmt(precio[k])} |')
            total_items += 1
            for h in hijos.get(k, []):
                usados.add(h)
                L.append(f'| ↳ {md(nom(h))} | {fmt(precio[h])} |')
                total_items += 1
        L.append('')
    resto = [k for k in items if k not in usados]
    if resto:
        L += ['### Otros', '', '| Ítem | Precio base |', '|---|---|']
        for k in resto:
            L.append(f'| {md(nom(k))} | {fmt(precio[k])} |')
            total_items += 1
            for h in hijos.get(k, []):
                if h not in usados:
                    usados.add(h)
                    L.append(f'| ↳ {md(nom(h))} | {fmt(precio[h])} |')
                    total_items += 1
        L.append('')
    return '\n'.join(L), dict(items=total_items, categorias=len(cats))

# ------------------------------------------------------------ encantamientos

APLICA = {
    'ALL_SWORD': 'Espadas', 'ALL_AXE': 'Hachas', 'ALL_PICKAXE': 'Picos', 'ALL_SPADE': 'Palas', 'ALL_SHOVEL': 'Palas',
    'ALL_HOE': 'Azadas', 'ALL_HELMET': 'Cascos', 'ALL_CHESTPLATE': 'Pecheras', 'ALL_LEGGINGS': 'Pantalones',
    'ALL_BOOTS': 'Botas', 'ALL_ARMOR': 'Armadura', 'BOW': 'Arco', 'CROSSBOW': 'Ballesta', 'TRIDENT': 'Tridente',
    'FISHING_ROD': 'Caña de pescar', 'ELYTRA': 'Élitros', 'MACE': 'Maza', 'ALL_SPEAR': 'Lanzas', 'ALL_TOOLS': 'Herramientas',
}
GRUPOS_AE = [
    ('SIMPLE', '⚪ Simple', 'Básicos de utilidad y combate menor.'),
    ('UNIQUE', '🟢 Único', 'Efectos moderados y debuffs.'),
    ('ELITE', '🔵 Elite', 'Habilidades de combate especializadas.'),
    ('ULTIMATE', '🟣 Ultimate', 'Poderosos, con efectos de área.'),
    ('LEGENDARY', '🟡 Legendario', 'Raros y muy fuertes.'),
    ('FABLED', '🔴 Fabled', 'Los más poderosos del servidor. No salen de la mesa de encantamientos.'),
]
NOVEDADES_AE = {'mawida', 'rayen', 'lawen', 'weichafe', 'kintu', 'perforante', 'raiz', 'ruka', 'lafken'}


def _aplica(lista):
    out = []
    for a in lista or []:
        t = APLICA.get(str(a).upper(), titulo(str(a)))
        if t not in out:
            out.append(t)
    if 'Armadura' in out:
        out = [x for x in out if x not in ('Cascos', 'Pecheras', 'Pantalones', 'Botas')]
    return ', '.join(out) or '—'


def _rango(vals, sufijo='', cero='—'):
    vals = [float(v) for v in vals]
    a, b = min(vals), max(vals)
    if b == 0:
        return cero
    return (num(a) if a == b else f'{num(a)}–{num(b)}') + sufijo


def gen_encantamientos():
    d = miniyaml.cargar(PLUGINS / 'AdvancedEnchantments' / 'enchantments.yml')
    disp = {k: limpia(re.sub(r'%[A-Za-z_-]+%', '', str(v.get('display') or ''))) or titulo(k) for k, v in d.items()}
    por = {g[0]: [] for g in GRUPOS_AE}
    for k, v in d.items():
        por.setdefault(str(v.get('group', 'SIMPLE')).upper(), []).append(k)
    L = [f'Hay **{len(d)} encantamientos personalizados** en total. Esta lista se genera sola desde la configuración real del servidor, '
         'así que siempre está al día. **Prob.** es la probabilidad de activarse (mínimo–máximo según el nivel), '
         '**Espera** el enfriamiento en segundos y 🆕 marca los nuevos de la temporada 2.', '']
    L += ['| Rareza | Encantamientos |', '|---|---:|']
    for g, nombre, _ in GRUPOS_AE:
        L.append(f'| {nombre} | {len(por.get(g, []))} |')
    L.append('')
    incompat = []
    for g, nombre, desc in GRUPOS_AE:
        ks = por.get(g, [])
        if not ks:
            continue
        L += [f'### {nombre}', '', f'{desc}', '', '| Encantamiento | Aplica a | Niv. | Prob. | Espera | Qué hace |', '|---|---|---:|---:|---:|---|']
        for k in sorted(ks, key=lambda x: disp[x].lower()):
            v = d[k]
            niv = v.get('levels') or {}
            chs = [(l or {}).get('chance', 100) for l in niv.values()] or [100]
            cds = [(l or {}).get('cooldown', 0) for l in niv.values()] or [0]
            efs = ' '.join(str(e) for l in niv.values() for e in ((l or {}).get('effects') or []))
            desc_k = limpia(v.get('description')) or '—'
            extra = []
            m = re.search(r'REMOVE_SOULS:(\d+)', efs)
            if m:
                extra.append(f'👻 gasta {m.group(1)} almas')
            if 'ADD_SOULS' in efs:
                extra.append('👻 genera almas')
            st = v.get('settings') or {}
            if isinstance(st, dict) and st.get('disable-in-enchanter'):
                extra.append('🎁 solo por eventos o admin')
            na = st.get('not-applyable-with') if isinstance(st, dict) else None
            if na:
                incompat.append((disp[k], [disp.get(x, titulo(x)) for x in na]))
                extra.append('⛔ no combina con ' + ', '.join(disp.get(x, titulo(x)) for x in na))
            nombre_k = ('🆕 ' if k in NOVEDADES_AE else '') + f'**{md(disp[k])}**'
            L.append(f'| {nombre_k} | {md(_aplica(v.get("applies")))} | {len(niv)} | {_rango(chs, "%")} | {_rango(cds, " s")} | '
                     f'{md(desc_k)}{" · " + md(" · ".join(extra)) if extra else ""} |')
        L.append('')
    if incompat:
        L += ['### ⛔ Incompatibilidades', '',
              'Para evitar combinaciones abusivas, estos encantamientos **no se pueden tener juntos** en el mismo objeto:', '']
        vistos = set()
        for a, otros in incompat:
            clave = frozenset([a] + otros)
            if clave in vistos:
                continue
            vistos.add(clave)
            L.append(f'- **{md(a)}** ✕ {", ".join(md(o) for o in otros)}')
        L.append('')
    return '\n'.join(L), dict(encantamientos=len(d))


# ----------------------------------------------------------------- mascotas

RAREZAS_PET = {1: ('🟢 Comunes', 'Común'), 2: ('🔵 Raras', 'Rara'), 3: ('🟣 Épicas', 'Épica'), 4: ('🟡 Legendarias', 'Legendaria')}


def gen_mascotas():
    por = {1: [], 2: [], 3: [], 4: []}
    for n in (1, 2, 3, 4):
        m = miniyaml.cargar(PLUGINS / 'DeluxeMenus' / 'gui_menus' / f'mascotas_especiales_{n}.yml')
        for k, v in (m.get('items') or {}).items():
            cmds = v.get('left_click_commands') or []
            if not any('petadmin create' in str(c) for c in cmds):
                continue
            precio = next((int(str(c).split()[-1]) for c in cmds if 'points take' in str(c)), 0)
            lore = v.get('lore') or []
            por[n].append((limpia(v.get('display_name')), limpia(lore[0]) if lore else '', precio))
    total = sum(len(x) for x in por.values())
    L = [f'Hay **{total} mascotas especiales** a la venta. Cada una se compra con **MapuPoints** en `/mascotasespeciales` '
         'y se puede ver girando en 3D en [servidor.mapucraft.com/mascotas](https://servidor.mapucraft.com/mascotas).', '']
    L += ['| Rareza | Precio | Mascotas |', '|---|---:|---:|']
    for n in (1, 2, 3, 4):
        precio = por[n][0][2] if por[n] else 0
        L.append(f'| {RAREZAS_PET[n][0]} | {precio} MapuPoints | {len(por[n])} |')
    L.append('')
    for n in (1, 2, 3, 4):
        if not por[n]:
            continue
        L += [f'### {RAREZAS_PET[n][0]} · {por[n][0][2]} MapuPoints', '', '| Mascota | Descripción |', '|---|---|']
        for nom, desc, _ in sorted(por[n], key=lambda x: x[0].lower()):
            L.append(f'| **{md(nom)}** | {md(desc)} |')
        L.append('')
    return '\n'.join(L), dict(mascotas=total)


# --------------------------------------------------------------- battlepass

def gen_battlepass():
    bp = PLUGINS / 'BattlePass'
    rew = miniyaml.cargar(bp / 'rewards.yml')
    libre = miniyaml.cargar(bp / 'passes' / 'free.yml')['tiers']
    prem = miniyaml.cargar(bp / 'passes' / 'premium.yml')['tiers']
    st = miniyaml.cargar(bp / 'settings.yml')

    def r_txt(rids):
        partes = []
        for r in rids or []:
            for ln in (rew.get(r, {}).get('lore-addon') or []):
                t = limpia(ln).lstrip('✦➠>').strip()
                t = t.replace('(MapuCore)', '').strip()
                partes.append(t)
        return ' + '.join(partes) or '—'

    ini = st['current-season']['start-date']
    L = [f'Temporada actual: inicia el **{ini}** · **{len(prem)} niveles** (gratis y premium).', '',
         '| Nivel | Puntos del nivel | Total | 🆓 Gratis | 💎 Premium |', '|---:|---:|---:|---|---|']
    acum = 0
    for n in sorted(prem, key=lambda x: int(x)):
        pts = int(prem[n].get('required-points', 0))
        acum += pts
        f = libre.get(n) or {}
        hito = '⭐ ' if (('locked-tier-item' in prem[n]) or ('locked-tier-item' in f)) else ''
        L.append(f'| {hito}**{n}** | {pts} | {acum} | {md(r_txt(f.get("rewards")))} | {md(r_txt(prem[n].get("rewards")))} |')
    L += ['', '> ⭐ = nivel destacado: tiene un ícono propio en el menú del pase.', '']
    return '\n'.join(L), dict(niveles=len(prem))


def gen_bp_misiones():
    bp = PLUGINS / 'BattlePass' / 'quests'
    L = ['### 🗓️ Misiones semanales', '', '| Semana | 🆓 Gratis | 💎 Premium |', '|---:|---|---|']
    for n in range(1, 11):
        f = bp / f'week-{n}-quests.yml'
        if not f.exists():
            continue
        q = miniyaml.cargar(f).get('quests') or {}
        gr = [limpia(v.get('name')).title() for v in q.values() if v.get('exclusive') != 'premium']
        pr = [limpia(v.get('name')).title() for v in q.values() if v.get('exclusive') == 'premium']
        L.append(f'| **{n}** | {md(", ".join(gr))} | {md(", ".join(pr))} |')
    eventos = sorted(bp.glob('event-*-quests.yml'))
    if eventos:
        L += ['', '### 🎉 Eventos del pase', '', '| Evento | Fechas | Misiones |', '|---|---|---:|']
        for f in eventos:
            d = miniyaml.cargar(f)
            c = d.get('category') or {}
            L.append(f'| {md(limpia(c.get("name")))} | {c.get("start", {}).get("date")} → {c.get("end", {}).get("date")} | {len(d.get("quests") or {})} |')
    dq = miniyaml.cargar(bp / 'daily-quests.yml').get('quests') or {}
    L += ['', f'Las **misiones diarias** salen de un grupo de **{len(dq)}** misiones y se reparten por dificultad: 2 fáciles, 2 normales y 1 difícil cada día.', '']
    return '\n'.join(L), dict(diarias=len(dq))


# --------------------------------------------------------------------- main


PAG_MERCADO = """# 💹 Mercado Global

El **mercado global** de Mapucraft funciona con precios que se mueven según la oferta y la demanda: si muchos jugadores venden un ítem, su precio baja; si lo compran, sube. Ábrelo con `/market`.

Abajo tienes el precio **base** de cada ítem. Úsalo como referencia: el precio del momento puede ser distinto.

***

"""


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry-run', action='store_true', help='no escribe, solo muestra los cambios')
    ap.add_argument('--solo', choices=['cajas', 'crafteos', 'mercado', 'encantamientos', 'mascotas', 'battlepass'], action='append')
    a = ap.parse_args()
    quiere = set(a.solo or ['cajas', 'crafteos', 'mercado', 'encantamientos', 'mascotas', 'battlepass'])
    if 'cajas' in quiere:
        cuerpo, st = gen_cajas()
        inyecta(WIKI / 'towny' / 'cajas.md', 'cajas', cuerpo, a.dry_run)
        print('  ', st)
    if 'crafteos' in quiere:
        cuerpo, st = gen_crafteos()
        inyecta(WIKI / 'towny' / 'crafteos.md', 'crafteos', cuerpo, a.dry_run)
        print('  ', st)
    if 'mercado' in quiere:
        cuerpo, st = gen_mercado()
        inyecta(WIKI / 'towny' / 'economia' / 'mercado.md', 'mercado', cuerpo, a.dry_run, PAG_MERCADO)
        print('  ', st)
    if 'encantamientos' in quiere:
        cuerpo, st = gen_encantamientos()
        inyecta(WIKI / 'towny' / 'encantamientos.md', 'encantamientos', cuerpo, a.dry_run)
        print('  ', st)
    if 'mascotas' in quiere:
        cuerpo, st = gen_mascotas()
        inyecta(WIKI / 'towny' / 'mascotas.md', 'mascotas', cuerpo, a.dry_run)
        print('  ', st)
    if 'battlepass' in quiere:
        cuerpo, st = gen_battlepass()
        inyecta(WIKI / 'towny' / 'battlepass.md', 'battlepass-niveles', cuerpo, a.dry_run)
        print('  ', st)
        cuerpo, st = gen_bp_misiones()
        inyecta(WIKI / 'towny' / 'battlepass.md', 'battlepass-misiones', cuerpo, a.dry_run)
        print('  ', st)
    # Rangos: LuckPerms no guarda los requisitos y no hay menu de rangos en DeluxeMenus -> se omite.


if __name__ == '__main__':
    main()
