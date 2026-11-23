"""SEO / technical gate for the whole static site: every number must be 0 before a release.

    python scripts/seo_gate.py            # prints the report, exit code 1 if a blocking check fails

Checks (published HTML = every tracked .html outside the app folders):
  inventory per language and page type; ?lang= links in HTML and sitemaps; canonical / hreflang / x-default;
  html lang/dir; local images, og:image and the 512 px logo as share image; <h1> count on indexable pages;
  title / description lengths of food and supplement pages; boilerplate of food pages and unique words of
  supplement pages; JSON-LD syntax; inline JavaScript syntax (Node); duplicate ids; Arabic text on en/nl/sv pages;
  sitemap index and section files against the disk and vercel.json redirects.
"""
import collections
import html as htmllib
import json
import os
import re
import statistics
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_urls  # noqa: E402

SITE = site_urls.SITE
ARABIC = re.compile(r'[؀-ۿ]+(?:\s+[؀-ۿ]+)*')
os.chdir(ROOT)
files = [f for f in subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '*.html'],
                                   capture_output=True, text=True, encoding='utf-8').stdout.split('\n')
         if f and not f.startswith(('WiboHealth', 'wibo_health', 'review/', 'scratchpad/', 'screenshots/'))]
files = sorted(set(files))


def kind(f):
    p = f.split('/')
    lang = p[0] if p[0] in ('en', 'nl', 'sv') else 'ar'
    rest = p[1:] if lang != 'ar' else p
    if rest[0] in ('foods', 'supplements'):
        return lang, rest[0] + ('-index' if rest[-1] == 'index.html' else '')
    if rest[0] == 'articles' or (len(rest) == 1 and rest[0] in {m.lstrip('/') for m in site_urls.ROOT_PAGES} and
                                 rest[0].replace('.html', '') in ('insulin-resistance', 'leptin-resistance', 'cortisol-stress',
                                                                  'intermittent-fasting', 'magnesium-types', 'bone-health-minerals', 'thyroid-health')):
        return lang, 'article'
    if rest[0] == 'diabetes' or rest[-1] == 'diabetes.html':
        return lang, 'diabetes'
    if 'calculator' in rest[-1] and rest[-1] != 'calorie-tracker.html':
        return lang, 'calculator'
    return lang, 'page'


def url_of(f):
    return SITE + ('/' if f == 'index.html' else '/' + f)


def file_of(url):
    path = url[len(SITE):] if url.startswith(SITE) else url
    path = path.split('#')[0]
    if '?' in path:
        return None
    return 'index.html' if path in ('', '/') else path.lstrip('/')


R = collections.OrderedDict()
FAIL = []


def report(name, value, blocking=True, detail=None):
    R[name] = (value, detail)
    if blocking and value:
        FAIL.append(name)


pages = {}
for f in files:
    s = (ROOT / f).read_text(encoding='utf-8', errors='replace')
    head = s[:s.find('<body')] if '<body' in s else s
    robots = re.search(r'<meta\s+name="robots"\s+content="([^"]*)"', s)
    pages[f] = dict(
        src=s, lang=kind(f)[0], kind=kind(f)[1],
        noindex=bool(robots and 'noindex' in robots.group(1)),
        canon=re.findall(r'<link rel="canonical" href="([^"]+)"', head),
        alts=re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', head),
        html_lang=(re.search(r'<html[^>]*\blang="([^"]+)"', s) or [None, None])[1],
        html_dir=(re.search(r'<html[^>]*\bdir="([^"]+)"', s) or [None, None])[1],
        title=htmllib.unescape((re.search(r'<title[^>]*>(.*?)</title>', s, re.S) or [None, ''])[1].strip()),
        desc=htmllib.unescape((re.search(r'<meta name="description"[^>]*content="([^"]*)"', s) or [None, ''])[1]),
        h1=len(re.findall(r'<h1\b', s)),
    )
# files whose URL vercel.json answers with a 301 are never served (e.g. /fatty-liver.html, /scanner.html)
REDIRECTED = {'fatty-liver.html', 'scanner.html'}
idx = [f for f, p in pages.items() if not p['noindex'] and f not in REDIRECTED]

# ---- inventory
inv = collections.Counter((p['lang'], p['kind']) for p in pages.values())
R['inventory'] = (len(pages), dict(sorted((f'{k[0]}/{k[1]}', v) for k, v in inv.items())))

# ---- ?lang=
def strip_scripts(s):
    return re.sub(r'<script\b.*?</script>', ' ', s, flags=re.S)
ql = [(f, m) for f, p in pages.items() for m in re.findall(r'(?:href|src|action)="([^"]*[?&]lang=[^"]*)"', strip_scripts(p['src']))]
report('internal ?lang= links (HTML attributes)', len(ql), detail=ql[:5])
ql_js = [(f, m) for f, p in pages.items() for m in re.findall(r'["\'`][^"\'`]*\?lang=[^"\'`]*["\'`]', ' '.join(re.findall(r'<script\b[^>]*>(.*?)</script>', p['src'], re.S)))]
report('?lang= URLs inside page scripts', len(ql_js), detail=ql_js[:5])

# ---- sitemaps
index = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
sm_files = re.findall(r'<loc>' + re.escape(SITE) + r'/([^<]+)</loc>', index) if '<sitemapindex' in index else ['sitemap.xml']
locs, sm_alts = [], {}
for fn in sm_files:
    t = (ROOT / fn).read_text(encoding='utf-8')
    for block in re.findall(r'<url>(.*?)</url>', t, re.S):
        loc = re.search(r'<loc>([^<]+)</loc>', block).group(1)
        locs.append(loc)
        sm_alts[loc] = re.findall(r'hreflang="([^"]+)" href="([^"]+)"', block)
report('sitemap URLs with ?lang=', sum('?' in l for l in locs))
report('sitemap URLs without a file', sum(1 for l in locs if not file_of(l) or not (ROOT / file_of(l)).exists()),
       detail=[l for l in locs if not file_of(l) or not (ROOT / file_of(l)).exists()][:5])
report('sitemap duplicate URLs', len(locs) - len(set(locs)))
report('sitemap URLs that are noindex', sum(1 for l in locs if file_of(l) in pages and pages[file_of(l)]['noindex']))
not_listed = [f for f in idx if url_of(f) not in set(locs) and f not in ('404.html',)]
report('indexable pages missing from the sitemaps', len(not_listed), detail=not_listed[:10])
alt_unlisted = sorted({h for v in sm_alts.values() for _, h in v} - set(locs))
report('sitemap hreflang targets not listed as <loc>', len(alt_unlisted), detail=alt_unlisted[:5])
R['sitemap files'] = ({fn: len(re.findall('<loc>', (ROOT / fn).read_text(encoding='utf-8'))) for fn in sm_files}, None)

# ---- vercel.json: no sitemap URL is caught by a redirect; ?lang URLs of root pages go to their static page
cfg = json.loads((ROOT / 'vercel.json').read_text(encoding='utf-8'))


def to_regex(src):
    out, i = '', 0
    while i < len(src):
        m = re.match(r':(\w+)(\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))?(\+|\*|\?)?', src[i:])
        if src[i] == ':' and m:
            body = m.group(2)[1:-1] if m.group(2) else '[^/]+'
            out += {'+': f'(?:{body})(?:/(?:{body}))*', '*': f'(?:(?:{body})(?:/(?:{body}))*)?'}.get(m.group(3), f'(?:{body})')
            i += len(m.group(0))
            continue
        if src[i] == '\\':
            out += src[i:i + 2]
            i += 2
            continue
        out += re.escape(src[i]) if src[i] in '.^$|[]{}' else src[i]
        i += 1
    return re.compile('^' + out + '$')


rules = [(to_regex(r['source']), r) for r in cfg['redirects']]


def redirect(path, query=None):
    for rx, r in rules:
        if r.get('has') and not all(query and query.get(h['key']) == h.get('value') for h in r['has'] if h['type'] == 'query'):
            continue
        if rx.match(path):
            return r['destination']
    return None


caught = [l for l in locs if redirect(l[len(SITE):] or '/')]
report('sitemap URLs caught by a vercel.json redirect', len(caught), detail=caught[:5])
bad_lang = []
for master, c in site_urls.ROOT_PAGES.items():
    for lang in ('en', 'nl', 'sv'):
        want = site_urls.url_in(master, lang)
        got = redirect(master, {'lang': lang})
        if want != master and got != want:
            bad_lang.append((master, lang, got, want))
report('old ?lang= URLs without a correct 301', len(bad_lang), detail=bad_lang[:5])
report('catch-all soft redirects (/en/*, /nl/*, /sv/*)', sum(1 for r in cfg['redirects'] if re.match(r'^/(en|nl|sv)/:path', r['source'])))

# ---- canonical / hreflang / lang
can_err, hl_err, xd_err, lang_err = [], [], [], []
for f in idx:
    p = pages[f]
    if len(p['canon']) != 1 or p['canon'][0] != url_of(f):
        can_err.append((f, p['canon']))
    want_lang = p['lang']
    if (p['html_lang'] or '')[:2] != want_lang or p['html_dir'] != ('rtl' if want_lang == 'ar' else 'ltr'):
        lang_err.append((f, p['html_lang'], p['html_dir']))
    alts = dict()
    for l, h in p['alts']:
        alts.setdefault(l, []).append(h)
    if not alts:
        continue
    if url_of(f) not in [h for v in alts.values() for h in v]:
        hl_err.append((f, 'self missing'))
    for l, hs in alts.items():
        for h in hs:
            if '?' in h:
                hl_err.append((f, l, h, '?lang'))
                continue
            t = file_of(h)
            if t not in pages:
                hl_err.append((f, l, h, 'no file'))
                continue
            if l == 'x-default':
                continue
            tp = pages[t]
            if url_of(f) not in [hh for ll, hh in tp['alts']]:
                hl_err.append((f, l, h, 'not reciprocal'))
            if tp['canon'] and tp['canon'][0] != h:
                hl_err.append((f, l, h, 'target canonical differs'))
            if (tp['html_lang'] or '')[:2] != l:
                hl_err.append((f, l, h, f'target lang {tp["html_lang"]}'))
    xd = alts.get('x-default', [])
    en = alts.get('en', [])
    if len(alts) > 1 and (len(xd) != 1 or (en and xd[0] != en[0])):
        xd_err.append((f, xd, en))
report('canonical errors (indexable pages)', len(can_err), detail=can_err[:5])
report('hreflang errors', len(hl_err), detail=hl_err[:5])
report('x-default not pointing to the English page', len(xd_err), detail=xd_err[:5])
report('<html lang>/dir mismatches', len(lang_err), detail=lang_err[:5])

# ---- images, og:image, share logo
img_missing, og_missing, og_logo = [], [], []
for f, p in pages.items():
    for src in re.findall(r'<img\b[^>]*\ssrc="([^"$]+)"', strip_scripts(p['src'])):
        if src.startswith(('http', 'data:')) or '{' in src:
            continue
        path = src.split('?')[0]
        target = path.lstrip('/') if path.startswith('/') else os.path.normpath(os.path.join(os.path.dirname(f), path))
        if not (ROOT / target).exists():
            img_missing.append((f, src))
    og = re.search(r'<meta property="og:image" content="([^"]+)"', p['src'])
    if og and not p['noindex']:
        t = file_of(og.group(1))
        if not t or not (ROOT / t).exists():
            og_missing.append((f, og.group(1)))
        if og.group(1).endswith('/images/logo.png'):
            og_logo.append(f)
report('broken local images', len(img_missing), detail=img_missing[:5])
report('og:image pointing to a missing file', len(og_missing), detail=og_missing[:5])
report('pages sharing the 512 px logo as og:image', len(og_logo), detail=og_logo[:5])

# ---- h1
h1_bad = [(f, pages[f]['h1']) for f in idx if pages[f]['h1'] != 1 and f != '404.html']
report('indexable pages without exactly one <h1>', len(h1_bad), detail=h1_bad[:10])

# ---- titles / descriptions of food and supplement pages
for k, (tmin, tmax) in (('foods', (45, 58)), ('supplements', (48, 58))):
    ps = [p for p in pages.values() if p['kind'] == k]
    tl = [len(p['title']) for p in ps]
    dl = [len(p['desc']) for p in ps]
    report(f'{k}: titles over 60 characters', sum(x > 60 for x in tl))
    report(f'{k}: descriptions over 160 characters', sum(x > 160 for x in dl))
    report(f'{k}: titles outside {tmin}-{tmax} / descriptions outside 125-155', (sum(not tmin <= x <= tmax for x in tl), sum(not 125 <= x <= 155 for x in dl)),
           blocking=False)
    R[f'{k}: title / description length (min-median-max)'] = (
        f'{min(tl)}-{statistics.median(tl)}-{max(tl)} / {min(dl)}-{statistics.median(dl)}-{max(dl)}', None)
    dup_t = [t for t, c in collections.Counter(p['title'] for p in ps).items() if c > 1]
    report(f'{k}: duplicate titles', len(dup_t), detail=dup_t[:3])

# ---- content: boilerplate share of food pages, unique words of supplement pages
def visible(s):
    s = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<header\b.*?</header>|<footer\b.*?</footer>|<nav\b.*?</nav>', ' ', s, flags=re.S)
    return ' '.join(htmllib.unescape(re.sub(r'<[^>]+>', ' ', s)).split())


for k in ('foods', 'supplements'):
    for lang in ('ar', 'en', 'nl', 'sv'):
        ps = [p for p in pages.values() if p['kind'] == k and p['lang'] == lang]
        if not ps:
            continue
        texts = [visible(p['src']) for p in ps]
        sh = [set(' '.join(w[i:i + 5]) for i in range(len(w) - 4)) for w in (re.sub(r'\d+([.,]\d+)?', '#', t).split() for t in texts)]
        df = collections.Counter()
        for x in sh:
            df.update(x)
        thr = len(ps) * 0.2
        share = [sum(1 for g in x if df[g] >= thr) / max(1, len(x)) for x in sh]
        sents = [set(s.strip() for s in re.split(r'(?<=[.!?؟])\s+', t) if len(s.split()) >= 4) for t in texts]
        sdf = collections.Counter()
        for x in sents:
            sdf.update(x)
        nb = [sum(len(s.split()) for s in x if sdf[s] < len(ps) * 0.3) for x in sents]
        R[f'{k}/{lang}: words (median), non-template words (median/min), 5-gram template share (median)'] = (
            f'{statistics.median(len(t.split()) for t in texts)} | {statistics.median(nb)}/{min(nb)} | {statistics.median(share):.0%}', None)
        if k == 'supplements':
            report(f'supplements/{lang}: pages under 300 non-template words', sum(x < 300 for x in nb), blocking=False)

# ---- structured data, ids, inline JS
ld_err, dup_ids = [], []
scripts = []
for f, p in pages.items():
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', p['src'], re.S):
        try:
            json.loads(b)
        except Exception as e:
            ld_err.append((f, str(e)[:60]))
    ids = re.findall(r'\sid="([^"]+)"', strip_scripts(p['src']))
    d = [i for i, c in collections.Counter(ids).items() if c > 1]
    if d:
        dup_ids.append((f, d[:3]))
    if p['kind'] in ('page', 'article', 'diabetes', 'calculator') or f in ('foods/apple.html', 'en/foods/apple.html', 'supplements/5-htp.html', 'sv/supplements/5-htp.html', 'foods/index.html'):
        for i, (attrs, js) in enumerate(re.findall(r'<script\b([^>]*)>(.*?)</script>', p['src'], re.S)):
            if 'src=' in attrs or ('type=' in attrs and 'javascript' not in attrs and 'module' not in attrs):
                continue                     # external scripts and data blocks (JSON-LD) are not inline JavaScript
            scripts.append((f'{f}#{i}', js))
report('JSON-LD syntax errors', len(ld_err), detail=ld_err[:5])
report('pages with duplicate id attributes', len(dup_ids), detail=dup_ids[:5])
node = subprocess.run(['node', '-e', 'const vm=require("vm");let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const a=JSON.parse(s);'
                       'const bad=[];for(const [n,c] of a){try{new vm.Script(c)}catch(e){bad.push(n+": "+e.message)}}process.stdout.write(JSON.stringify(bad))})'],
                      input=json.dumps(scripts).encode('utf-8'), capture_output=True)
js_bad = json.loads(node.stdout.decode('utf-8') or '[]')
report(f'inline JavaScript syntax errors ({len(scripts)} scripts checked)', len(js_bad), detail=js_bad[:5])

# ---- Arabic on en/nl/sv pages (visible text, alt/title/aria-label/placeholder, meta); the AR language link and
# JSON-LD alternateName (multilingual names) are allowed
leaks = []
for f, p in pages.items():
    if p['lang'] == 'ar':
        continue
    body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->', ' ', p['src'], flags=re.S)
    attrs = ' '.join(v for tag in re.findall(r'<[a-z][^>]*>', body) if 'hreflang="ar"' not in tag and 'lang="ar"' not in tag
                     for v in re.findall(r'\b(?:alt|title|aria-label|placeholder|content)="([^"]*)"', tag))
    text = re.sub(r'<[^>]+>', ' ', body)
    found = ARABIC.findall(text + ' ' + attrs)
    if found:
        leaks.append((f, found[:3]))
report('en/nl/sv pages with Arabic text', len(leaks), detail=leaks[:5])

# ---- noindex pages
R['noindex pages'] = (sorted(f for f, p in pages.items() if p['noindex']), None)

# ---- print
for k, (v, d) in R.items():
    mark = 'FAIL' if k in FAIL else '    '
    print(f'{mark} {k}: {v}' + (f'\n       e.g. {d}' if d and k in FAIL else ''))
print('\nGATE:', 'FAILED (' + ', '.join(FAIL) + ')' if FAIL else 'PASSED')
sys.exit(1 if FAIL else 0)
