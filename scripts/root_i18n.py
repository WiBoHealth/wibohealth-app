"""Read the translation dictionaries of the hand-written root pages and apply them to the HTML.

Each root page (index.html, about.html, ...) carries its copy for every language in an inline JS object
(e.g. `const translations = { ar: {...}, en: {...}, nl: {...} }`) and marks translatable elements with
data-i18n="key" (plus data-i18n-alt / -href / -placeholder / -ph for attributes). These helpers
  - extract that object (evaluated by Node, so any valid JS literal works),
  - write a language's copy into the HTML, as the page's own script does in the browser, so the static
    /en/ and /nl/ pages are complete without JavaScript.
Used by scripts/generate_root_pages.py.
"""
import html as htmllib
import json
import re
import subprocess

DICT_NAMES = ('translations', 'i18nDictionary', 'foodsTranslations')


def _match_brace(s, i):
    """s[i] == '{' -> index just after the matching '}' (skips strings, template literals and comments)."""
    depth, j, n = 0, i, len(s)
    while j < n:
        c = s[j]
        if c in '"\'`':
            q = c
            j += 1
            while j < n and s[j] != q:
                if s[j] == '\\':
                    j += 1
                j += 1
        elif s.startswith('//', j) and s[j - 1] != ':':
            j = s.find('\n', j)
            if j < 0:
                break
        elif s.startswith('/*', j):
            j = s.find('*/', j) + 1
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    raise ValueError('unbalanced braces in dictionary')


def dictionary_span(page):
    """(name, start, end) of the page's translation object literal `{...}` in the page source."""
    for name in DICT_NAMES:
        m = re.search(r'(?:const|let|var)\s+%s\s*=\s*\{' % name, page)
        if m:
            start = m.end() - 1
            return name, start, _match_brace(page, start)
    raise LookupError('no translation dictionary found')


def extract(page):
    """{lang: {key: text}} of the page's translation dictionary."""
    _, start, end = dictionary_span(page)
    literal = page[start:end]
    out = subprocess.run(['node', '-e', 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{'
                          'const o=(0,eval)("("+s+")");process.stdout.write(JSON.stringify(o));})'],
                         input=literal.encode('utf-8'), capture_output=True, check=True)
    return json.loads(out.stdout.decode('utf-8'))


TAG = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9-]*)((?:[^>"\']|"[^"]*"|\'[^\']*\')*)>')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
RAW = {'script', 'style', 'textarea', 'title'}


def _element_end(page, open_end, tag):
    """Index of the '<' of the closing tag that matches an element whose start tag ends at open_end."""
    if tag in RAW:
        return page.index('</%s' % tag, open_end)
    depth, pos = 1, open_end
    while True:
        m = TAG.search(page, pos)
        if not m:
            raise ValueError('no closing </%s>' % tag)
        closing, name = m.group(1) == '/', m.group(2).lower()
        pos = m.end()
        if name in RAW and not closing:
            pos = page.index('</%s' % name, pos)
            continue
        if name != tag or name in VOID or m.group(3).rstrip().endswith('/'):
            continue
        depth += -1 if closing else 1
        if depth == 0:
            return m.start()


def _set_attr(tag_text, name, value):
    value = htmllib.escape(value, quote=True)
    if re.search(r'(?<![-\w])%s="[^"]*"' % name, tag_text):
        return re.sub(r'(?<![-\w])%s="[^"]*"' % name, lambda _: '%s="%s"' % (name, value), tag_text, count=1)
    return tag_text[:-1].rstrip('/').rstrip() + ' %s="%s"%s' % (name, value, ' />' if tag_text.endswith('/>') else '>')


ATTRS = (('data-i18n-alt', 'alt'), ('data-i18n-href', 'href'), ('data-i18n-placeholder', 'placeholder'),
         ('data-i18n-ph', 'placeholder'), ('data-i18n-title', 'title'), ('data-i18n-aria', 'aria-label'))


def apply(page, copy, mode, missing):
    """Write `copy` ({key: text}) into every data-i18n element and attribute of `page`.
    mode 'html' sets the element's HTML (the page's script uses innerHTML), 'text' its text (textContent).
    Keys without a translation are added to `missing` and left as they are."""
    out, pos = [], 0
    for m in TAG.finditer(page):
        if m.group(1) or m.start() < pos:
            continue
        attrs = m.group(3)
        if 'data-i18n' not in attrs:
            continue
        tag_text, name = m.group(0), m.group(2).lower()
        for data_attr, target in ATTRS:
            k = re.search(r'(?<![-\w])%s="([^"]+)"' % data_attr, tag_text)
            if k:
                if k.group(1) in copy:
                    tag_text = _set_attr(tag_text, target, _plain(copy[k.group(1)]))
                    if target == 'placeholder' and 'aria-label=' in tag_text:
                        tag_text = _set_attr(tag_text, 'aria-label', _plain(copy[k.group(1)]))
                else:
                    missing.add(k.group(1))
        k = re.search(r'(?<![-\w])data-i18n="([^"]+)"', tag_text)
        if not k:
            out.append(page[pos:m.start()] + tag_text)
            pos = m.end()
            continue
        key = k.group(1)
        if key not in copy:
            missing.add(key)
            out.append(page[pos:m.start()] + tag_text)
            pos = m.end()
            continue
        if name in VOID:
            out.append(page[pos:m.start()] + tag_text)
            pos = m.end()
            continue
        end = _element_end(page, m.end(), name)
        value = copy[key]
        inner = (_plain(value) if name == 'title' else htmllib.escape(value, quote=False)) if (mode == 'text' or name == 'title') else value
        out.append(page[pos:m.start()] + tag_text + inner)
        pos = end
    out.append(page[pos:])
    return ''.join(out)


def _plain(value):
    """Text of an HTML snippet (for attributes and <title>)."""
    return htmllib.unescape(re.sub(r'<[^>]+>', '', value))


def mode_of(page):
    """'html' if the page's own script writes data-i18n copy with innerHTML, else 'text'."""
    m = re.search(r"querySelectorAll\(['\"]\[data-i18n\]['\"]\)\.forEach\((.{0,600})", page, re.S)
    if not m:
        return 'text'
    body = m.group(1)
    i, t = body.find('innerHTML'), body.find('textContent')
    if i < 0:
        return 'text'
    return 'html' if t < 0 or i < t else 'text'
