"""Validate the JSON-LD of the live site pages.

Checks every <script type="application/ld+json"> block in foods.html, food-details.html, the
static food pages (foods/, en/foods/, nl/foods/), the supplement pages (supplements/, en/..., nl/...) and the
article pages (articles/, en/..., nl/...):
  - the block parses as JSON (an empty block is an error too)
  - no "Product" type anywhere, and no offers / aggregateRating / review / price fields
  - the food and supplement index pages (foods/index.html, ...) carry a CollectionPage
  - every static food page carries a MedicalWebPage with author (Dr. Wassim Habib) and publisher
  - every supplement, article and calculator page carries a MedicalWebPage authored by the WiBo Health organisation,
    cites its sources, and never names a personal reviewer (legal requirement for supplement and article content);
    the only exception is NAMED_AUTHOR_PAGES, which must carry Dr. Wassim Habib as Person author and reviewedBy
  - JSON-LD may be a single node or an @graph of nodes
It also scans the .js / .html sources for a schema "@type": "Product" built at runtime.

Usage: python scripts/validate_schema.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Articles the user explicitly chose to sign with the doctor's name (2026-10-20): Person author + reviewedBy instead of the organisation
# and the prediabetes guide (2026-10-22, second exception)
NAMED_AUTHOR_PAGES = {'diabetes/gestational-diabetes.html', 'en/diabetes/gestational-diabetes.html', 'nl/diabetes/zwangerschapsdiabetes.html',
                      'diabetes/prediabetes.html', 'en/diabetes/prediabetes.html', 'nl/diabetes/prediabetes.html',
                      'sv/diabetes/prediabetes.html', 'sv/diabetes/graviditetsdiabetes.html'}   # Swedish versions (2026-10-23)
# every Swedish article is signed by Dr. Wassim Habib (decision 2026-10-23)
NAMED_AUTHOR_PAGES |= {f'sv/articles/{p.name}' for p in (ROOT / 'sv' / 'articles').glob('*.html')}
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
    # index.html in the food and supplement folders is the static index (generate_directory_pages.py): a CollectionPage
    indexes = [ROOT / d / 'index.html' for d in ('foods', 'en/foods', 'nl/foods', 'supplements', 'en/supplements', 'nl/supplements')]
    static = [p for d in ('foods', 'en/foods', 'nl/foods') for p in sorted((ROOT / d).glob('*.html')) if p not in indexes]
    # supplement and article pages are authored by the WiBo Health organisation and must never name a person
    supp = [p for d in ('supplements', 'en/supplements', 'nl/supplements', 'articles', 'en/articles', 'nl/articles',
                        'diabetes', 'en/diabetes', 'nl/diabetes', 'sv/diabetes', 'sv/articles')
            for p in sorted((ROOT / d).glob('*.html')) if p not in indexes]
    # the standalone calculator pages follow the same organisation-only authorship rule
    supp += [p for d in ('.', 'en', 'nl') for p in sorted((ROOT / d).glob('*-calculator.html'))]
    errors, blocks = [], 0
    for page in pages + static + supp + [p for p in indexes if p.exists()]:
        rel = page.relative_to(ROOT).as_posix()
        found_types = set()
        text = page.read_text(encoding='utf-8')
        named = rel in NAMED_AUTHOR_PAGES
        if page in supp and not named and re.search(r'Wassim|وسيم', text):
            errors.append(f'{rel}: supplement/article page names a personal reviewer')
        for raw in LD_RE.findall(text):
            blocks += 1
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                errors.append(f'{rel}: invalid JSON-LD ({e})')
                continue
            nodes = data.get('@graph', [data]) if isinstance(data, dict) else [data]
            found_types.update(n.get('@type') for n in nodes if isinstance(n, dict))
            for path, k, v in walk(data):
                if k == '@type' and (v == 'Product' or (isinstance(v, list) and 'Product' in v)):
                    errors.append(f'{rel}: Product at {path}')
                if k in BANNED_KEYS:
                    errors.append(f'{rel}: commerce field {k!r} at {path}')
            for node in nodes:
                if not isinstance(node, dict) or node.get('@type') != 'MedicalWebPage':
                    continue
                if page in static:
                    if (node.get('author') or {}).get('name') != 'Dr. Wassim Habib':
                        errors.append(f'{rel}: author missing')
                    if (node.get('publisher') or {}).get('name') != 'WiBo Health':
                        errors.append(f'{rel}: publisher missing')
                if page in supp:
                    author = node.get('author') or {}
                    if named:
                        for role in ('author', 'reviewedBy'):
                            person = node.get(role) or {}
                            if person.get('@type') != 'Person' or person.get('name') != 'Dr. Wassim Habib':
                                errors.append(f'{rel}: {role} must be Dr. Wassim Habib (named-author article)')
                    elif author.get('@type') != 'Organization' or author.get('name') != 'WiBo Health':
                        errors.append(f'{rel}: author must be the WiBo Health organisation')
                    if not node.get('citation'):
                        if 'content="noindex' in text:   # a draft placeholder may wait for its sources
                            print(f'note {rel}: draft without citation (required before publishing)')
                        else:
                            errors.append(f'{rel}: no citation')
        if page in static + supp and 'MedicalWebPage' not in found_types:
            errors.append(f'{rel}: no MedicalWebPage block')
        if page in indexes and 'CollectionPage' not in found_types:
            errors.append(f'{rel}: no CollectionPage block')

    sources = [p for p in ROOT.glob('*.html')] + [p for p in (ROOT / 'js').glob('*.js')] + \
              [p for d in ('en', 'nl', 'sv') for p in (ROOT / d).glob('*.html')]
    for src in sources:
        text = src.read_text(encoding='utf-8', errors='replace')
        for m in RUNTIME_PRODUCT_RE.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            errors.append(f'{src.relative_to(ROOT).as_posix()}:{line}: runtime "@type": "Product"')

    print(f'{len(pages) + len(static) + len(supp)} pages, {blocks} JSON-LD blocks, {len(sources)} source files scanned')
    for e in errors:
        print('ERROR', e)
    print('OK: no Product schema, all JSON-LD valid' if not errors else f'{len(errors)} problem(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
