"""Check sitemap.xml: every <loc> and hreflang alternate must be a live, indexable page.

Local checks (always):
  - the URL maps to an existing file in the repo
  - no redirect rule in vercel.json matches it (a sitemap URL must not redirect)
  - the page's canonical points to itself and the page is not noindex
Live checks (with --live): HEAD each URL without following redirects; only 200 passes.

Usage: python scripts/check_sitemap.py [--live]
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://wibohealth.com'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9', 'x': 'http://www.w3.org/1999/xhtml'}


def vercel_redirects():
    """vercel.json sources as regexes (path-to-regexp subset used in this repo)."""
    rules = []
    for r in json.loads((ROOT / 'vercel.json').read_text(encoding='utf-8')).get('redirects', []):
        src = r['source']
        # :name(regex) -> (regex), :name* -> .*, :name -> [^/]+
        src = re.sub(r':\w+\(((?:[^()]|\([^()]*\))*)\)', r'(\1)', src)
        src = re.sub(r':\w+\*', '.*', src)
        src = re.sub(r':\w+', '[^/]+', src)
        rules.append((r['source'], re.compile('^' + src + '$')))
    return rules


def local_file(path):
    if path in ('', '/'):
        return ROOT / 'index.html'
    return ROOT / path.lstrip('/')


def main():
    live = '--live' in sys.argv
    tree = ET.parse(ROOT / 'sitemap.xml')
    locs, alternates = [], set()
    for url in tree.getroot().findall('s:url', NS):
        locs.append(url.find('s:loc', NS).text.strip())
        for alt in url.findall('x:link', NS):
            alternates.add(alt.get('href').strip())
    all_urls = sorted(set(locs) | alternates)
    errors = []

    dupes = {u for u in locs if locs.count(u) > 1} if len(set(locs)) != len(locs) else set()
    for u in sorted(dupes):
        errors.append(f'duplicate <loc>: {u}')
    for u in sorted(alternates - set(locs)):
        errors.append(f'hreflang alternate not listed as <loc>: {u}')

    rules = vercel_redirects()
    canon_re = re.compile(r'<link rel="canonical" href="([^"]+)"')
    for u in all_urls:
        if not u.startswith(SITE + '/'):
            errors.append(f'foreign host: {u}')
            continue
        path = u[len(SITE):]
        hit = next((src for src, rx in rules if rx.match(path)), None)
        if hit:
            errors.append(f'redirected by vercel.json rule {hit!r}: {u}')
        f = local_file(path)
        if not f.is_file():
            errors.append(f'missing file (404): {u}')
            continue
        html = f.read_text(encoding='utf-8', errors='replace')
        m = canon_re.search(html)
        if m and m.group(1) != u:
            errors.append(f'canonical mismatch: {u} -> {m.group(1)}')
        if re.search(r'<meta[^>]+name="robots"[^>]+noindex', html, re.I):
            errors.append(f'noindex page in sitemap: {u}')

    print(f'{len(locs)} <loc> entries, {len(all_urls)} distinct URLs incl. hreflang alternates')

    if live:
        opener = build_opener(type('NoRedirect', (HTTPRedirectHandler,), {'redirect_request': lambda *a, **k: None}))

        def head(u):
            try:
                with opener.open(Request(u, method='HEAD', headers={'User-Agent': 'WiBo-sitemap-check'}), timeout=20) as r:
                    return u, r.status, None
            except HTTPError as e:
                return u, e.code, e.headers.get('Location')
            except Exception as e:  # network error
                return u, None, str(e)

        with ThreadPoolExecutor(max_workers=8) as pool:
            for u, status, info in pool.map(head, all_urls):
                if status != 200:
                    errors.append(f'live HTTP {status}{" -> " + info if info else ""}: {u}')
        print('live check done')

    for e in errors:
        print('ERROR', e)
    print('OK' if not errors else f'{len(errors)} problem(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
