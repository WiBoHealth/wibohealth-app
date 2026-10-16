"""Validate the JSON-LD of the live site pages.

Checks every <script type="application/ld+json"> block in foods.html, food-details.html and the
static food pages (foods/, en/foods/, nl/foods/):
  - the block parses as JSON (an empty block is an error too)
  - no "Product" type anywhere, and no offers / aggregateRating / review / price fields
  - every static food page carries a MedicalWebPage with author and publisher
It also scans the .js / .html sources for a schema "@type": "Product" built at runtime.

Usage: python scripts/validate_schema.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANNED_KEYS = {'offers', 'aggregateRating', 'review', 'price', 'priceCurrency'}
LD_RE = re.compile(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', re.S)
RUNTIME_PRODUCT_RE = re.compile(r'["\']@type["\']\s*:\s*["\']Product["\']')


def walk(node, path='$'):
    if isinstance(node, dict):
        for k, v in node.items():
            yield path, k, v
            yield from walk(v, f'{path}.{k}')
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f'{path}[{i}]')


def main():
    pages = [ROOT / 'foods.html', ROOT / 'food-details.html']
    static = [p for d in ('foods', 'en/foods', 'nl/foods') for p in sorted((ROOT / d).glob('*.html'))]
    errors, blocks = [], 0
    for page in pages + static:
        rel = page.relative_to(ROOT).as_posix()
        found_types = set()
        for raw in LD_RE.findall(page.read_text(encoding='utf-8')):
            blocks += 1
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                errors.append(f'{rel}: invalid JSON-LD ({e})')
                continue
            found_types.add(data.get('@type'))
            for path, k, v in walk(data):
                if k == '@type' and (v == 'Product' or (isinstance(v, list) and 'Product' in v)):
                    errors.append(f'{rel}: Product at {path}')
                if k in BANNED_KEYS:
                    errors.append(f'{rel}: commerce field {k!r} at {path}')
            if data.get('@type') == 'MedicalWebPage' and page in static:
                if (data.get('author') or {}).get('name') != 'Dr. Wassim Habib':
                    errors.append(f'{rel}: author missing')
                if (data.get('publisher') or {}).get('name') != 'WiBo Health':
                    errors.append(f'{rel}: publisher missing')
        if page in static and 'MedicalWebPage' not in found_types:
            errors.append(f'{rel}: no MedicalWebPage block')

    sources = [p for p in ROOT.glob('*.html')] + [p for p in (ROOT / 'js').glob('*.js')] + \
              [p for d in ('en', 'nl') for p in (ROOT / d).glob('*.html')]
    for src in sources:
        text = src.read_text(encoding='utf-8', errors='replace')
        for m in RUNTIME_PRODUCT_RE.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            errors.append(f'{src.relative_to(ROOT).as_posix()}:{line}: runtime "@type": "Product"')

    print(f'{len(pages) + len(static)} pages, {blocks} JSON-LD blocks, {len(sources)} source files scanned')
    for e in errors:
        print('ERROR', e)
    print('OK: no Product schema, all JSON-LD valid' if not errors else f'{len(errors)} problem(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
