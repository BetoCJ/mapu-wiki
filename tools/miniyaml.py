"""Parser YAML minimo (subconjunto) para las configs de plugins y comandos.yml.

Soporta: mapas y listas por indentacion, escalares (cadenas con/sin comillas,
numeros, booleanos, null), `[]`/`{}` vacios, listas en linea simples `[a, b]`,
comentarios `#` y continuacion de escalares en varias lineas (se pliegan).
No soporta anclas, tags ni bloques `|`/`>` complejos (se leen como texto plegado).
Si PyYAML esta instalado, `cargar()` lo usa; si no, usa este parser.
"""
import re

try:  # pragma: no cover
    import yaml as _yaml
except Exception:  # PyYAML no esta en el venv del bot
    _yaml = None


def _quita_comentario(s):
    out, q = [], None
    for i, ch in enumerate(s):
        if q:
            if ch == q:
                # '' dentro de comillas simples es escape
                if q == "'" and s[i + 1:i + 2] == "'":
                    out.append(ch)
                    continue
                q = None
        elif ch in ('"', "'") and (i == 0 or s[i - 1] in ' [{,:-'):
            q = ch
        elif ch == '#' and (i == 0 or s[i - 1] in ' \t'):
            break
        out.append(ch)
    return ''.join(out).rstrip()


def _escalar(v):
    v = v.strip()
    if v == '':
        return None
    if v[0] == "'" and v[-1] == "'" and len(v) >= 2:
        return v[1:-1].replace("''", "'")
    if v[0] == '"' and v[-1] == '"' and len(v) >= 2:
        return re.sub('[\\\\](.)', lambda m: {'n': '\n', 't': '\t'}.get(m.group(1), m.group(1)), v[1:-1])
    if v == '[]':
        return []
    if v == '{}':
        return {}
    if v[0] == '[' and v[-1] == ']':
        return [_escalar(x) for x in _split_flow(v[1:-1])]
    low = v.lower()
    if low in ('true', 'yes'):
        return True
    if low in ('false', 'no'):
        return False
    if low in ('null', '~'):
        return None
    if re.fullmatch(r'[-+]?\d+', v):
        return int(v)
    if re.fullmatch(r'[-+]?(\d+\.\d*|\.\d+|\d+)([eE][-+]?\d+)?', v):
        return float(v)
    return v


def _split_flow(s):
    partes, cur, q, prof = [], '', None, 0
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in ('"', "'"):
            q = ch
            cur += ch
        elif ch in '[{':
            prof += 1
            cur += ch
        elif ch in ']}':
            prof -= 1
            cur += ch
        elif ch == ',' and prof == 0:
            partes.append(cur)
            cur = ''
        else:
            cur += ch
    if cur.strip():
        partes.append(cur)
    return partes


def _clave_valor(texto):
    """Devuelve (clave, resto) si `texto` es 'clave: valor'; si no, None."""
    if texto[:1] in ('"', "'"):
        q = texto[0]
        i = 1
        while i < len(texto):
            if texto[i] == q:
                if q == "'" and texto[i + 1:i + 2] == "'":
                    i += 2
                    continue
                break
            i += 1
        resto = texto[i + 1:]
        if resto.startswith(':') and (len(resto) == 1 or resto[1] == ' '):
            return _escalar(texto[:i + 1]), resto[1:].strip()
        return None
    m = re.match(r'^([^\s:][^:]*?|[^\s:]):(?:\s+(.*)|$)', texto)
    if m:
        return m.group(1).strip(), (m.group(2) or '').strip()
    return None


class _P:
    def __init__(self, texto):
        self.l = []
        for crudo in texto.replace('\t', '  ').splitlines():
            if not crudo.strip() or crudo.lstrip().startswith('#'):
                continue
            s = _quita_comentario(crudo)
            if s.strip():
                self.l.append((len(s) - len(s.lstrip(' ')), s.strip()))
        self.i = 0

    def peek(self):
        return self.l[self.i] if self.i < len(self.l) else None

    def bloque(self, indent):
        p = self.peek()
        if p is None:
            return None
        if p[1].startswith('- ') or p[1] == '-':
            return self.lista(p[0])
        return self.mapa(p[0])

    def _continuacion(self, valor, indent):
        # lineas con mas indentacion tras un escalar se pliegan al valor
        while self.peek() and self.peek()[0] > indent:
            valor += ' ' + self.peek()[1]
            self.i += 1
        return valor

    def mapa(self, indent):
        d = {}
        while True:
            p = self.peek()
            if p is None or p[0] < indent or (p[0] == indent and p[1].startswith('-')):
                break
            if p[0] > indent:
                self.i += 1  # linea huerfana
                continue
            kv = _clave_valor(p[1])
            if kv is None:
                self.i += 1
                continue
            k, resto = kv
            self.i += 1
            if resto == '' or resto in ('|', '>', '|-', '>-'):
                sig = self.peek()
                if resto in ('|', '>', '|-', '>-'):
                    d[k] = self._continuacion('', indent).strip()
                elif sig and (sig[0] > indent or (sig[0] == indent and sig[1].startswith('-'))):
                    d[k] = self.bloque(sig[0])
                else:
                    d[k] = None
            else:
                d[k] = _escalar(self._continuacion(resto, indent))
        return d

    def lista(self, indent):
        out = []
        while True:
            p = self.peek()
            if p is None or p[0] != indent or not (p[1].startswith('- ') or p[1] == '-'):
                break
            resto = p[1][1:].strip()
            self.i += 1
            if resto == '':
                sig = self.peek()
                out.append(self.bloque(sig[0]) if sig and sig[0] > indent else None)
                continue
            kv = _clave_valor(resto)
            if kv is not None and not resto.startswith(('[', '{')):
                # elemento mapa: reinsertar la linea con indentacion virtual
                virt = indent + 2
                self.i -= 1
                self.l[self.i] = (virt, resto)
                out.append(self.mapa(virt))
            else:
                out.append(_escalar(self._continuacion(resto, indent)))
        return out


def parsear(texto):
    p = _P(texto)
    r = p.bloque(0)
    return {} if r is None else r


def cargar(ruta):
    with open(ruta, encoding='utf-8') as f:
        texto = f.read()
    if _yaml is not None:
        try:
            return _yaml.safe_load(texto) or {}
        except Exception:
            pass
    return parsear(texto)
