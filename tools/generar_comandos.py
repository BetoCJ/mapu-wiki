#!/usr/bin/env python3
"""Genera la guia de comandos a partir de UNA sola fuente: wiki/tools/comandos.yml

Salidas:
  - wiki/el-servidor/comandos.md             (seccion AUTO:comandos)
  - bot/GUIA_TOWNY.md                        (seccion AUTO:comandos, el resto se conserva)
  - bot/servidor-towny/comandos.json         (lo lee guia_comandos.js para el canal #comandos)

Valida que los nombres sean unicos (sin distinguir mayusculas), que existan los campos
obligatorios y que los embeds de Discord respeten los limites de longitud.
No toca los cogs del bot.

Uso:  python generar_comandos.py [--dry-run]
"""
import argparse
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import miniyaml  # noqa: E402
from generar_wiki import inyecta, WIKI, RAIZ  # noqa: E402

FUENTE = AQUI / 'comandos.yml'
GUIA = RAIZ / 'bot' / 'GUIA_TOWNY.md'
JSON_OUT = RAIZ / 'bot' / 'servidor-towny' / 'comandos.json'
PAG = WIKI / 'el-servidor' / 'comandos.md'

COLORES = {'naranja', 'verde', 'oro', 'azul', 'rosa', 'gris', 'blurple', 'morado'}
MODOS = {'towny', 'skyblock', 'ambos', 'discord'}
MODO_TXT = {'towny': 'Towny', 'skyblock': 'Skyblock', 'ambos': 'Towny y Skyblock', 'discord': 'Discord'}


def lista_discord(cmds):
    """Mismo formato que usa guia_comandos.js."""
    filas = []
    for c in cmds:
        al = c.get('alias') or []
        extra = (' · también ' + ', '.join(f'`{a}`' for a in al)) if al else ''
        filas.append(f'`{c["name"]}` — {c["descripcion"]}{extra}')
    return '\n'.join(filas)


def todos_los_comandos(embeds):
    for e in embeds:
        for c in e.get('comandos') or []:
            yield e, None, c
        for s in e.get('secciones') or []:
            for c in s.get('comandos') or []:
                yield e, s, c


def validar(datos):
    errores = []
    embeds = datos.get('embeds')
    if not isinstance(embeds, list) or not embeds:
        raise SystemExit('comandos.yml: falta la lista "embeds"')
    vistos, ids = {}, set()
    for e in embeds:
        if e.get('id') in ids:
            errores.append(f'embed repetido: {e.get("id")}')
        ids.add(e.get('id'))
        if e.get('color') not in COLORES:
            errores.append(f'embed {e.get("id")}: color invalido {e.get("color")!r} (usa {sorted(COLORES)})')
        if not e.get('titulo'):
            errores.append(f'embed {e.get("id")}: falta titulo')
    for e, s, c in todos_los_comandos(embeds):
        for campo in ('name', 'descripcion', 'permiso', 'modo'):
            if not c.get(campo):
                errores.append(f'{e["id"]}: comando sin "{campo}": {c}')
        if c.get('modo') not in MODOS:
            errores.append(f'{c.get("name")}: modo invalido {c.get("modo")!r} (usa {sorted(MODOS)})')
        clave = str(c.get('name', '')).strip().lower()
        if clave in vistos:
            errores.append(f'nombre repetido: {c["name"]!r} (en {vistos[clave]} y en {e["id"]})')
        vistos[clave] = e['id']
    # un alias no puede ser el name de otro comando
    nombres = set(vistos)
    for e, s, c in todos_los_comandos(embeds):
        for a in c.get('alias') or []:
            if str(a).strip().lower() in nombres:
                errores.append(f'alias {a!r} de {c["name"]!r} ya existe como comando')
    # limites de Discord
    for e in embeds:
        if e.get('modo') == 'texto':
            if len(e.get('descripcion') or '') > 4096:
                errores.append(f'embed {e["id"]}: descripcion > 4096')
            continue
        desc = e.get('descripcion') or ''
        if e.get('comandos'):
            desc = (desc + '\n\n' if desc else '') + lista_discord(e['comandos'])
        total = len(e['titulo']) + len(desc)
        if len(desc) > 4096:
            errores.append(f'embed {e["id"]}: descripcion > 4096 ({len(desc)})')
        for s in e.get('secciones') or []:
            v = lista_discord(s['comandos'])
            total += len(s.get('nombre', '')) + len(v)
            if len(v) > 1024:
                errores.append(f'embed {e["id"]} / {s.get("nombre")}: campo > 1024 ({len(v)}); parte la seccion')
        if total > 6000:
            errores.append(f'embed {e["id"]}: total > 6000 ({total})')
    if errores:
        print('ERRORES en comandos.yml:')
        for x in errores:
            print('  -', x)
        raise SystemExit(1)
    return vistos


def limpia_md(t):
    return re.sub(r'<#\d+>', '#canal', str(t)).replace('|', '\\|').replace('\n', ' ')


def gen_json(datos):
    embeds = datos['embeds']
    plano = []
    for e, s, c in todos_los_comandos(embeds):
        plano.append(dict(name=c['name'], descripcion=c['descripcion'], permiso=c['permiso'], modo=c['modo'],
                          alias=c.get('alias') or [], embed=e['id'], seccion=(s or {}).get('nombre')))
    return json.dumps(dict(_aviso='Archivo generado desde wiki/tools/comandos.yml. No editar a mano.',
                           embeds=embeds, comandos=plano), ensure_ascii=False, indent=2) + '\n'


def tabla(cmds):
    L = ['| Comando | Descripción | Quién puede | Modo |', '|---|---|---|---|']
    for c in cmds:
        al = c.get('alias') or []
        nombre = f'`{c["name"]}`' + (' · ' + ' · '.join(f'`{a}`' for a in al) if al else '')
        permiso = 'Todos' if str(c['permiso']).lower() == 'todos' else c['permiso']
        L.append(f'| {nombre} | {limpia_md(c["descripcion"])} | {limpia_md(permiso)} | {MODO_TXT[c["modo"]]} |')
    return L


def gen_wiki(datos):
    L = ['## 📜 Lista de comandos (generado)', '',
         '> Esta lista se genera desde `wiki/tools/comandos.yml`, la misma fuente que usa la guía del canal '
         '#comandos de Discord. Para actualizarla: `python wiki/tools/generar_comandos.py`.', '']
    for e in datos['embeds']:
        if e.get('modo') == 'texto':
            continue
        L.append(f"### {limpia_md(e.get('titulo_wiki') or e['titulo'])}")
        L.append('')
        if e.get('descripcion') and e.get('modo') == 'discord':
            L += [limpia_md(e['descripcion'].split('\n')[0]), '']
        if e.get('comandos'):
            L += tabla(e['comandos']) + ['']
        for s in e.get('secciones') or []:
            L += [f'**{limpia_md(s["nombre"])}**', ''] + tabla(s['comandos']) + ['']
    return '\n'.join(L)


def gen_guia(datos):
    n = sum(1 for _ in todos_los_comandos(datos['embeds']))
    L = ['## 7. Guía de comandos (canal #comandos)', '',
         f'La guía del canal **📖・comandos** y la wiki salen de una sola fuente, `wiki/tools/comandos.yml` ({n} comandos).',
         '', '1. Edita `wiki/tools/comandos.yml` (nombre, descripción, permiso/rango y modo; los nombres deben ser únicos).',
         '2. Ejecuta `python wiki/tools/generar_comandos.py` (con `--dry-run` solo valida). Regenera esta sección, '
         '`wiki/el-servidor/comandos.md` y `bot/servidor-towny/comandos.json`.',
         '3. Publica en Discord con `node bot/servidor-towny/guia_comandos.js <carpeta-del-bot>` '
         '(con `SOLO_REVISAR=1` solo comprueba los límites de Discord). El script lee `comandos.json`.', '',
         '| Grupo | Comandos |', '|---|---|']
    for e in datos['embeds']:
        if e.get('modo') == 'texto':
            continue
        cs = [c['name'] for _, _, c in todos_los_comandos([e])]
        L.append(f'| {limpia_md(e["titulo"])} | ' + ', '.join(f'`{c}`' for c in cs) + ' |')
    return '\n'.join(L)


def escribe(ruta, texto, dry):
    viejo = ruta.read_text(encoding='utf-8') if ruta.exists() else None
    rel = ruta.relative_to(RAIZ).as_posix()
    if viejo == texto:
        print(('[dry-run] ' if dry else '') + f'sin cambios {rel}')
    elif dry:
        print(f'[dry-run] {rel}: cambiaria')
    else:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(texto, encoding='utf-8', newline='\n')
        print(f'escrito {rel}')


PAG_TITULO = """# ⌨️ Comandos

Esta es la lista de comandos del servidor y del bot de Discord. También está publicada en el canal **#comandos** del Discord, y dentro del juego puedes usar `/tutoriales`.

***

"""


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    datos = miniyaml.cargar(FUENTE)
    nombres = validar(datos)
    print(f'comandos.yml valido: {len(nombres)} comandos, {len(datos["embeds"])} grupos, nombres unicos')
    inyecta(PAG, 'comandos', gen_wiki(datos), a.dry_run, PAG_TITULO)
    inyecta(GUIA, 'comandos', gen_guia(datos), a.dry_run)
    escribe(JSON_OUT, gen_json(datos), a.dry_run)


if __name__ == '__main__':
    main()
