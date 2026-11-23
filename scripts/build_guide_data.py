"""Slim data files for the two interactive guides (foods.html, supplements.html) and their cache-busting versions.

    python scripts/build_guide_data.py        (also run by generate_root_pages.py before it writes the pages)

js/data.js (550 KB) and js/supplements-data.js (993 KB) stay the sources of truth (other generators read them).
The guides no longer load them; they fetch, after the first paint, only what their cards, search and filters need:

    data/foods-index.json         the fields foods.html uses (names in ar/en/nl, group, category labels, GI, nutrition)
    data/supplements-index.json   names, summaries, tags, category and group of every supplement (cards and search)
    data/supplements-full.json    the full records; fetched only when a reader opens a supplement or the comparison

The guides' code lives in js/foods-guide.js and js/supplements-guide.js (loaded with defer). This script stamps
?v=<content hash> on those files and on the JSON URLs in the Arabic masters; generate_root_pages.py copies them into
the /en/, /nl/ and /sv/ versions.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FOOD_FIELDS = ('id', 'name', 'nameEn', 'nameNl', 'image', 'icon', 'category', 'categoryNl', 'categoryEn', 'group',
               'gi', 'gi_status', 'nutrition', 'cuisine')
SUPP_FIELDS = ('id', 'slug', 'name', 'englishName', 'nameNl', 'category', 'icon', 'summary', 'summaryEn', 'summaryNl',
               'tags', 'tagsEn', 'tagsNl', 'groupLabel')


def read_js_array(path, name):
    """The array a data file assigns to `name`, evaluated by Node (any valid JS literal works)."""
    code = ('const fs=require("fs"),vm=require("vm");const c={window:{}};vm.createContext(c);'
            f'vm.runInContext(fs.readFileSync({json.dumps(str(path))},"utf8")+";this.__d={name};",c);'
            'process.stdout.write(JSON.stringify(c.__d));')
    out = subprocess.run(['node', '-e', code], capture_output=True, check=True)
    return json.loads(out.stdout.decode('utf-8'))


def write_json(path, data):
    text = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    path.parent.mkdir(exist_ok=True)
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8', newline='\n')
    return hashlib.sha1(text.encode('utf-8')).hexdigest()[:8]


def short_hash(path):
    return hashlib.sha1(path.read_bytes()).hexdigest()[:8]


def stamp(page, script, data_attrs):
    """src="/js/<script>?v=..." and its data-* URLs (data-index, data-full) with content hashes."""
    path = ROOT / page
    text = path.read_text(encoding='utf-8')
    tag = re.search(r'<script src="/js/%s(?:\?v=[^"]*)?"[^>]*></script>' % re.escape(script), text)
    if not tag:
        sys.exit(f'build_guide_data: {page}: <script src="/js/{script}"> not found')
    new_tag = re.sub(r'src="/js/%s(?:\?v=[^"]*)?"' % re.escape(script),
                     f'src="/js/{script}?v={short_hash(ROOT / "js" / script)}"', tag.group(0))
    for attr, (url, ver) in data_attrs.items():
        new_tag = re.sub(r'%s="[^"]*"' % attr, f'{attr}="{url}?v={ver}"', new_tag)
    if new_tag != tag.group(0):
        path.write_text(text.replace(tag.group(0), new_tag), encoding='utf-8', newline='\n')


def columnar(records, fields, lookups=()):
    """{"f": fields, "l": {field: [distinct values]}, "r": rows}: the field names once, repeated values (category labels,
    group labels) as an index into a lookup list. js/*-guide.js turn it back into the same objects."""
    tables = {k: [] for k in lookups}
    rows = []
    for rec in records:
        row = []
        for k in fields:
            v = rec.get(k)
            if k in tables and v is not None:
                key = json.dumps(v, ensure_ascii=False, sort_keys=True)
                keys = [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in tables[k]]
                if key not in keys:
                    tables[k].append(v)
                    keys.append(key)
                v = keys.index(key)
            row.append(v)
        while row and row[-1] is None:
            row.pop()
        rows.append(row)
    return {'f': list(fields), 'l': tables, 'r': rows}


def build():
    foods = read_js_array(ROOT / 'js' / 'data.js', 'foodsDatabase')
    for f in foods:                                  # the three category labels travel together
        f['categoryAll'] = [f.get('category'), f.get('categoryNl'), f.get('categoryEn')]
    fields = [k for k in FOOD_FIELDS if k not in ('category', 'categoryNl', 'categoryEn')] + ['categoryAll']
    fv = write_json(ROOT / 'data' / 'foods-index.json', columnar(foods, fields, ('categoryAll', 'group', 'gi_status', 'icon')))
    supps = read_js_array(ROOT / 'js' / 'supplements-data.js', 'supplementsData')
    sv = write_json(ROOT / 'data' / 'supplements-index.json', columnar(supps, SUPP_FIELDS, ('category', 'groupLabel', 'icon')))
    full = write_json(ROOT / 'data' / 'supplements-full.json', supps)
    stamp('foods.html', 'foods-guide.js', {'data-index': ('/data/foods-index.json', fv)})
    stamp('supplements.html', 'supplements-guide.js', {'data-index': ('/data/supplements-index.json', sv),
                                                       'data-full': ('/data/supplements-full.json', full)})
    sizes = {p: (ROOT / 'data' / p).stat().st_size for p in ('foods-index.json', 'supplements-index.json', 'supplements-full.json')}
    return sizes


if __name__ == '__main__':
    print(build())
