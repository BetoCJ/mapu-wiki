"""Datos completos de las mascotas especiales de Mapucraft (MyPet), desde los archivos reales del servidor.

Lee (solo lectura) en <plugins>:
  DeluxeMenus/gui_menus/mascotas_especiales_*.yml  -> tienda: mascota, rareza (precio), descripcion
  MyPet/pet-config.yml                              -> stats base por tipo (vida, velocidad, vuela, comida)
  MyPet/skilltrees/*.st.json                        -> arboles de habilidades (con herencia y niveles)

Reglas de nivel de MyPet 4.1 (verificadas en LevelRule$Dynamic.check): "N" = nivel N; "%m" = cada m niveles;
">s" = desde el nivel s (inclusive); "<e" = hasta el nivel e (inclusive); se cumple si (nivel - s) % m == 0.

Uso como modulo:  from mypet_datos import cargar, a_json
Uso por consola:  python mypet_datos.py <carpeta plugins> [salida.json]
"""
import glob
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import miniyaml  # noqa: E402

NIVEL_MAX = 100
RAREZAS = {120: 'Común', 250: 'Rara', 450: 'Épica', 800: 'Legendaria'}

EFECTOS = {
    'Speed': 'Velocidad', 'Haste': 'Prisa', 'Strength': 'Fuerza', 'JumpBoost': 'Salto', 'Regeneration': 'Regeneración',
    'Resistance': 'Resistencia', 'FireResistance': 'Resistencia al fuego', 'WaterBreathing': 'Respiración acuática',
    'NightVision': 'Visión nocturna', 'Absorption': 'Absorción', 'Invisibility': 'Invisibilidad', 'Luck': 'Suerte',
    'HealthBoost': 'Vida extra', 'Saturation': 'Saturación', 'Slowness': 'Lentitud', 'Weakness': 'Debilidad',
    'DolphinsGrace': 'Gracia del delfín', 'SlowFalling': 'Caída lenta', 'Glowing': 'Resplandor',
    'ConduitPower': 'Poder del canalizador', 'HeroOfTheVillage': 'Héroe de la aldea',
}
POCIONES = {
    'harming': 'Daño instantáneo', 'healing': 'Curación', 'poison': 'Veneno', 'regeneration': 'Regeneración',
    'weakness': 'Debilidad', 'slowness': 'Lentitud', 'swiftness': 'Velocidad', 'strength': 'Fuerza',
    'fire_resistance': 'Resistencia al fuego', 'invisibility': 'Invisibilidad', 'leaping': 'Salto',
    'night_vision': 'Visión nocturna', 'water_breathing': 'Respiración acuática', 'turtle_master': 'Maestro tortuga',
    'wind_charged': 'Carga de viento', 'weaving': 'Tejido', 'oozing': 'Supuración', 'infested': 'Infestación',
    'luck': 'Suerte', 'slow_falling': 'Caída lenta',
}
PROYECTILES = {
    'Arrow': 'flechas', 'SmallFireball': 'bolas de fuego pequeñas', 'LargeFireball': 'bolas de fuego grandes',
    'DragonFireball': 'bolas de fuego del dragón', 'EnderPearl': 'perlas de Ender', 'Snowball': 'bolas de nieve',
    'WitherSkull': 'cráneos de Wither', 'Egg': 'huevos', 'Trident': 'tridentes', 'ShulkerBullet': 'proyectiles de Shulker',
    'LlamaSpit': 'escupitajos', 'WindCharge': 'cargas de viento', 'Fireball': 'bolas de fuego', 'SpectralArrow': 'flechas espectrales',
}
HERRAMIENTAS = {
    'crafting': 'mesa de trabajo', 'smithing': 'mesa de herrería', 'anvil': 'yunque', 'grindstone': 'piedra de afilar',
    'stonecutter': 'cortapiedras', 'loom': 'telar', 'cartography': 'mesa de cartografía',
}
COMIDA = {
    'amethyst shard': 'fragmento de amatista', 'apple': 'manzana', 'bamboo': 'bambú', 'beef': 'carne de vaca',
    'blaze powder': 'polvo de blaze', 'bone': 'hueso', 'bone meal': 'harina de hueso', 'brown mushroom': 'hongo marrón',
    'carrot': 'zanahoria', 'chicken': 'pollo', 'chorus fruit': 'fruta de chorus', 'cod': 'bacalao', 'cookie': 'galleta',
    'copper ingot': 'lingote de cobre', 'crimson fungus': 'hongo carmesí', 'glow berries': 'bayas luminosas',
    'glowstone dust': 'polvo de piedra luminosa', 'gold ingot': 'lingote de oro', 'golden apple': 'manzana dorada',
    'hay block': 'bloque de heno', 'iron ingot': 'lingote de hierro', 'lapis lazuli': 'lapislázuli',
    'magma cream': 'crema de magma', 'melon slice': 'rodaja de sandía', 'mutton': 'cordero',
    'phantom membrane': 'membrana de phantom', 'porkchop': 'chuleta de cerdo', 'pumpkin pie': 'pastel de calabaza',
    'rabbit': 'conejo', 'redstone': 'polvo de redstone', 'rotten flesh': 'carne podrida', 'salmon': 'salmón',
    'sculk': 'sculk', 'slime ball': 'bola de slime', 'spider eye': 'ojo de araña', 'sugar': 'azúcar',
    'sweet berries': 'bayas dulces', 'wheat': 'trigo', 'wheat seeds': 'semillas de trigo',
}
NOMBRE_HAB = {
    'Damage': 'Daño', 'Life': 'Vida extra', 'Armor': 'Armadura', 'Thorns': 'Espinas', 'Shield': 'Escudo', 'Bleed': 'Sangrado',
    'Fire': 'Fuego', 'Poison': 'Veneno', 'Wither': 'Wither', 'Slow': 'Ralentización', 'Knockback': 'Empuje',
    'Lightning': 'Rayo', 'Stomp': 'Pisotón', 'Ranged': 'Ataque a distancia', 'Ride': 'Montura', 'Sprint': 'Carrera',
    'Climb': 'Escalar', 'Control': 'Control', 'Pickup': 'Recolección', 'Backpack': 'Mochila', 'Beacon': 'Faro',
    'Camouflage': 'Camuflaje', 'Fishing': 'Pesca', 'Mining': 'Minería', 'Lumberjack': 'Leñador', 'Taunt': 'Provocar',
    'Sniff': 'Olfato', 'Toolbox': 'Caja de herramientas', 'Heal': 'Curación', 'Potion': 'Pociones',
}
ORDEN_HAB = list(NOMBRE_HAB)


# ------------------------------------------------------------------ reglas de nivel
def niveles(clave):
    """Niveles (1..NIVEL_MAX) en los que se aplica una clave de mejora."""
    clave = str(clave)
    if '%' in clave:
        m = re.search(r'%(\d+)', clave)
        s = re.search(r'>(\d+)', clave)
        e = re.search(r'<(\d+)', clave)
        mod = max(1, int(m.group(1)))
        ini = int(s.group(1)) if s else 0
        fin = int(e.group(1)) if e else 0
        out = []
        for n in range(1, NIVEL_MAX + 1):
            if ini > 1 and n < ini:
                continue
            if fin > 0 and n > fin:
                continue
            if (n - ini) % mod == 0:
                out.append(n)
        return out
    return [int(x) for x in clave.split(',') if x.strip().isdigit() and 1 <= int(x) <= NIVEL_MAX]


def _num(v):
    try:
        return float(str(v).replace('+', ''))
    except ValueError:
        return None


# ------------------------------------------------------------------ acumulado de un arbol
def acumular(arbol):
    """{habilidad: {'props': {...}, 'desde': nivel}} con las mejoras PROPIAS del arbol hasta NIVEL_MAX."""
    res = {}
    for hab, cfg in (arbol.get('Skills') or {}).items():
        props, desde = {}, None
        for clave, up in (cfg.get('Upgrades') or {}).items():
            lv = niveles(clave)
            if not lv:
                continue
            desde = min(lv) if desde is None else min(desde, min(lv))
            for p, val in (up or {}).items():
                veces = len(lv)
                if p == 'Buffs' and isinstance(val, dict):
                    b = props.setdefault('Buffs', {})
                    for ef, v in val.items():
                        n = _num(v)
                        b[ef] = (b.get(ef, 0) + n * veces) if n is not None else True
                elif p in ('potions', 'drops') and isinstance(val, list):
                    lst = props.setdefault(p, [])
                    for it in val:
                        if it not in lst:
                            lst.append(it)
                elif isinstance(val, bool):
                    props[p] = props.get(p, False) or val
                elif isinstance(val, str) and _num(val) is not None and val.strip()[:1] in '+-':
                    props[p] = props.get(p, 0) + _num(val) * veces
                elif isinstance(val, (int, float)):
                    props[p] = props.get(p, 0) + val * veces
                else:
                    props[p] = val
        res[hab] = dict(props=props, desde=desde or 1)
    return res


def _f(x):
    """Numero compacto: 3, 2,5 (sin ceros sobrantes)."""
    x = round(float(x), 2)
    return str(int(x)) if x == int(x) else str(x).replace('.', ',')


def _item(s):
    return str(s).replace('minecraft:', '').replace('_', ' ').capitalize()


def texto_hab(hab, p):
    """Frase en español de una habilidad con sus valores acumulados; None si no hay nada que mostrar."""
    g = lambda k: p.get(k, 0)  # noqa: E731
    if hab == 'Damage':
        return f'+{_f(g("Damage"))} de daño'
    if hab == 'Life':
        return f'+{_f(g("Health"))} de vida'
    if hab == 'Armor':
        return f'+{_f(g("armor"))} de armadura y +{_f(g("toughness"))} de dureza'
    if hab == 'Thorns':
        return f'{_f(g("Chance"))}% de probabilidad de devolver el {_f(g("Reflection"))}% del daño recibido'
    if hab == 'Shield':
        return f'{_f(g("Chance"))}% de probabilidad de desviar el {_f(g("Redirect"))}% del daño que recibes hacia la mascota'
    if hab == 'Bleed':
        return f'{_f(g("Chance"))}% de probabilidad de causar sangrado ({_f(g("Damage"))} de daño, {_f(g("Duration"))} s)'
    if hab in ('Fire', 'Poison', 'Wither', 'Slow'):
        verbo = {'Fire': 'prender fuego', 'Poison': 'envenenar', 'Wither': 'aplicar Wither', 'Slow': 'ralentizar'}[hab]
        return f'{_f(g("Chance"))}% de probabilidad de {verbo} al objetivo por {_f(g("Duration"))} s'
    if hab == 'Knockback':
        return f'{_f(g("Chance"))}% de probabilidad de empujar al objetivo'
    if hab == 'Lightning':
        return f'{_f(g("Chance"))}% de probabilidad de lanzar un rayo de {_f(g("Damage"))} de daño'
    if hab == 'Stomp':
        return f'{_f(g("Chance"))}% de probabilidad de dar un pisotón de {_f(g("Damage"))} de daño en 2,5 bloques'
    if hab == 'Ranged':
        pr = PROYECTILES.get(str(p.get('Projectile', 'Arrow')), str(p.get('Projectile', 'proyectiles')))
        return f'dispara {pr} con {_f(g("Damage"))} de daño'
    if hab == 'Ride':
        t = 'se puede montar'
        if g('Speed'):
            t += f' (+{_f(g("Speed"))}% de velocidad'
            t += f', +{_f(g("JumpHeight"))} de salto)' if g('JumpHeight') else ')'
        elif g('JumpHeight'):
            t += f' (+{_f(g("JumpHeight"))} de salto)'
        return t
    if hab == 'Sprint':
        return 'corre hacia sus objetivos'
    if hab == 'Climb':
        return 'escala paredes por su cuenta'
    if hab == 'Control':
        return 'se puede dirigir con un ítem'
    if hab == 'Pickup':
        t = f'recoge objetos en {_f(g("Range"))} bloques'
        return t + (' y experiencia' if p.get('Exp') else '')
    if hab == 'Backpack':
        r = int(g('Rows'))
        return f'mochila de {r} fila(s) ({9 * r} espacios)'
    if hab == 'Beacon':
        bf = p.get('Buffs') or {}
        ef = ', '.join(EFECTOS.get(k, k) + (f' {int(v)}' if v is not True and v > 1 else '') for k, v in bf.items())
        return f'faro con {ef or "efectos"} (alcance {_f(g("Range"))} bloques, {_f(g("Duration"))} s, hasta {int(g("Count"))} efecto(s))'
    if hab == 'Camouflage':
        return f'se vuelve invisible tras {_f(g("Delay"))} s sin moverse'
    if hab in ('Fishing', 'Mining', 'Lumberjack'):
        acc = {'Fishing': 'pesca en agua cercana', 'Mining': 'mina menas cercanas', 'Lumberjack': 'tala árboles cercanos'}[hab]
        t = f'{acc} (alcance {_f(g("range"))}, cada {_f(g("interval"))} s'
        return t + (', sin herramienta)' if p.get('toolless') else ')')
    if hab == 'Taunt':
        return f'provoca a mobs hostiles (alcance {_f(g("range"))}, cada {_f(g("interval"))} s)'
    if hab == 'Sniff':
        return f'olfatea un objeto cada {_f(g("interval"))} s'
    if hab == 'Toolbox':
        return 'abre ' + ', '.join(v for k, v in HERRAMIENTAS.items() if p.get(k))
    if hab == 'Heal':
        return f'+{_f(g("Health"))} de vida por pulso (el intervalo se acorta {_f(abs(g("Timer")))} s en total)'
    if hab == 'Potion':
        ps = [POCIONES.get(str(x.get('type', '')).replace('minecraft:', ''), _item(x.get('type', ''))) for x in (p.get('potions') or [])]
        return 'lanza pociones: ' + ', '.join(ps) if ps else None
    return None


def limpia_md(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^<>]{1,40}>', '', str(s))).strip()


# ------------------------------------------------------------------ carga
def cargar(plugins):
    plugins = Path(plugins)
    # tienda
    tienda = {}
    for f in sorted(glob.glob(str(plugins / 'DeluxeMenus' / 'gui_menus' / 'mascotas_especiales_*.yml')),
                    key=lambda x: int(re.search(r'_(\d+)\.yml', x).group(1))):
        m = miniyaml.cargar(f)
        for k, v in (m.get('items') or {}).items():
            cmds = v.get('left_click_commands') or []
            cr = [c for c in cmds if 'petadmin create' in str(c)]
            if not cr:
                continue
            tipo = str(cr[0]).split('mypet:')[-1].strip()
            precio = next((int(str(c).split()[-1]) for c in cmds if 'points take' in str(c)), 0)
            lore = v.get('lore') or []
            tienda[tipo] = dict(id=tipo, nombre=limpia_md(re.sub(r'&.', '', str(v.get('display_name', k)))),
                                precio=precio, rareza=RAREZAS.get(precio, '?'),
                                desc=limpia_md(re.sub(r'&.', '', str(lore[0]))) if lore else '')
    # tipos
    pets = miniyaml.cargar(plugins / 'MyPet' / 'pet-config.yml')['MyPet']['Pets']
    bajos = {k.lower(): k for k in pets}
    # arboles
    arboles = {}
    for f in glob.glob(str(plugins / 'MyPet' / 'skilltrees' / '*.st.json')):
        d = json.load(open(f, encoding='utf8'), strict=False)
        arboles[d['ID']] = d
    return dict(tienda=tienda, pets=pets, bajos=bajos, arboles=arboles)


def clasifica(a):
    if 'NoSkilltree' in (a.get('Requirements') or []):
        return 'base'
    if int(a.get('RequiredLevel', 20)) >= 50:
        return 'mitico'
    if str(a.get('Name', '')).startswith('✦'):
        return 'firma'
    return 'ascension'


def requisitos(a):
    """Lista de ids de arboles desde los que se puede llegar (O logico)."""
    out = []
    for r in a.get('Requirements') or []:
        if r.startswith('Skilltree:'):
            out += r.split(':')[1:]
    return out


def construir(datos):
    """Estructura final: arboles (con habilidades propias) y mascotas (stats + ids de arboles)."""
    A = datos['arboles']
    arboles = {}

    def total(aid, vistos=()):
        """Habilidades del arbol sumando las de los arboles que hereda (cadena Inheritance)."""
        mio = acumular(A[aid])
        padre = (A[aid].get('Inheritance') or {}).get('Skilltree')
        if not padre or padre not in A or padre in vistos or aid in vistos:
            return mio
        res = total(padre, vistos + (aid,))
        for hab, info in mio.items():
            if hab not in res:
                res[hab] = info
                continue
            props = res[hab]['props']
            for p, v in info['props'].items():
                if p == 'Buffs':
                    b = props.setdefault('Buffs', {})
                    for ef, n in v.items():
                        b[ef] = True if (n is True or b.get(ef) is True) else b.get(ef, 0) + n
                elif p in ('potions', 'drops'):
                    lst = props.setdefault(p, [])
                    lst += [x for x in v if x not in lst]
                elif isinstance(v, bool):
                    props[p] = props.get(p, False) or v
                elif isinstance(v, (int, float)) and isinstance(props.get(p, 0), (int, float)) and not isinstance(props.get(p, 0), bool):
                    props[p] = props.get(p, 0) + v
                else:
                    props[p] = v
            res[hab]['desde'] = min(res[hab]['desde'], info['desde'])
        return res

    for aid, a in A.items():
        hab = []
        tot = total(aid)
        for info in tot.values():  # las probabilidades no pasan de 100 %
            for p in ('Chance', 'Redirect', 'Reflection'):
                if p in info['props']:
                    info['props'][p] = min(100, info['props'][p])
        for h, info in sorted(tot.items(), key=lambda kv: ORDEN_HAB.index(kv[0]) if kv[0] in ORDEN_HAB else 99):
            t = texto_hab(h, info['props'])
            if t:
                hab.append(dict(n=NOMBRE_HAB.get(h, h), t=t, nv=info['desde']))
        arboles[aid] = dict(
            id=aid, n=limpia_md(a.get('Name', aid)).replace('✦ ', '').strip(), firma=str(a.get('Name', '')).startswith('✦'),
            t=clasifica(a), nv=int(a.get('RequiredLevel', 1)), orden=int(a.get('Order', 0)),
            desde=requisitos(a), hereda=(a.get('Inheritance') or {}).get('Skilltree'),
            d=[limpia_md(x) for x in (a.get('Description') or []) if limpia_md(x)], h=hab)
    # tipo -> arboles
    por_tipo = {}
    for aid, a in A.items():
        for mt in a.get('MobTypes') or []:
            por_tipo.setdefault(mt.lower(), []).append(aid)
    mascotas = {}
    for tipo, t in datos['tienda'].items():
        pc = datos['pets'].get(datos['bajos'].get(tipo, ''), {})
        ids = sorted(por_tipo.get(tipo, []), key=lambda i: (['base', 'ascension', 'firma', 'mitico'].index(arboles[i]['t']), arboles[i]['orden']))
        mascotas[tipo] = dict(
            id=tipo, nombre=t['nombre'], rareza=t['rareza'], precio=t['precio'], desc=t['desc'],
            hp=pc.get('HP'), vel=pc.get('Speed'), vuela=bool(pc.get('CanFly')),
            comida=[COMIDA.get(str(x).replace('_', ' '), str(x).replace('_', ' ')) for x in (pc.get('Food') or [])], arboles=ids)
    return dict(nivel_max=NIVEL_MAX, arboles=arboles, mascotas=mascotas)


def a_json(plugins):
    return construir(cargar(plugins))


if __name__ == '__main__':
    res = a_json(sys.argv[1])
    print('mascotas', len(res['mascotas']), 'arboles', len(res['arboles']))
    if len(sys.argv) > 2:
        ruta = Path(sys.argv[2])
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(json.dumps(res, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        print('escrito', ruta, ruta.stat().st_size, 'bytes')
