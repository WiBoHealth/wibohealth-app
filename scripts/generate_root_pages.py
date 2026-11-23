"""Static language versions of the hand-written root pages, from their own translation dictionaries.

    python scripts/generate_root_pages.py

The root pages (index.html, about.html, foods.html, the older articles, ...) are hand-written in Arabic and carry
their English/Dutch copy in an inline dictionary. Before 2026-11-23 those languages were shown on the same URL via
?lang= and JavaScript; now every language has its own static, indexable page:

    /about.html            Arabic master (edited by hand; this script only rewrites its head alternates,
                           language switcher and structured data, between markers, so re-running is safe)
    /en/about.html         English, written here: the dictionary copy pre-rendered into the HTML
    /nl/about.html         Dutch, written here
    /sv/foods.html         Swedish view of the interactive food guide (the other Swedish pages come from the
                           article / site-page / homepage generators)

URLs come from scripts/site_urls.py, titles and descriptions from scripts/root_pages_seo.py.
Also written: the ROOT-PAGES block of the sitemap (every language of every root page cluster).
Run after any change to a root page or its dictionary.
"""
import html as htmllib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import root_i18n  # noqa: E402
import site_urls  # noqa: E402
from root_pages_seo import CRUMB_HOME, SEO  # noqa: E402
import root_pages_extra as EXTRA  # noqa: E402
from generate_food_pages import JOB_TITLE, replace_sitemap_block  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = site_urls.SITE
TODAY = date.today().isoformat()
ARABIC = re.compile(r'[؀-ۿ]')
LANG_NAME = {'ar': 'العربية', 'en': 'English', 'nl': 'Nederlands', 'sv': 'Svenska'}
OG_LOCALE = {'ar': 'ar_AR', 'en': 'en_US', 'nl': 'nl_NL', 'sv': 'sv_SE'}
DEFAULT_OG = 'og-wibo-health.jpg'          # 1200x630 brand card (images/og-wibo-health.jpg)
ORG_NAME = 'WiBo Health Group'
DOCTOR_ID = f'{SITE}/doctor.html#wassim-habib'


# ----------------------------------------------------------------------------------------------------------------------
# URL mapping for a page that moves one folder down (/en/, /nl/, /sv/)
# ----------------------------------------------------------------------------------------------------------------------
def article_map():
    """Arabic path -> {lang: path} for the generated articles and section pages, read from their hreflang links."""
    out = {}
    files = list((ROOT / 'articles').glob('*.html')) + list((ROOT / 'diabetes').glob('*.html')) + [ROOT / 'diabetes.html']
    for f in files:
        head = f.read_text(encoding='utf-8')[:6000]
        alts = dict(re.findall(r'<link rel="alternate" hreflang="(ar|en|nl|sv)" href="%s([^"]+)">' % re.escape(SITE), head))
        if 'ar' in alts:
            out[alts['ar']] = alts
    return out


ARTICLES = article_map()


def map_url(url, lang):
    """A URL of an Arabic root page, as it must read on that page's `lang` version."""
    if not url or url.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:', '//', '{', '$')):
        return url
    if url.startswith(('http://', 'https://')):
        if not url.startswith(SITE + '/') and url != SITE:
            return url
        url = url[len(SITE):] or '/'
        absolute = True
    else:
        absolute = False
    path, _, frag = url.partition('#')
    path, _, query = path.partition('?')
    if not path.startswith('/'):
        path = '/' + path
    query = '&'.join(p for p in query.split('&') if p and not p.startswith('lang='))
    page = path in ('/', '/index.html') or path.endswith('.html')
    if page:
        if path in ('/', '/index.html') or site_urls.versions(path) or path in site_urls.LINK_ONLY:
            path = site_urls.url_in(path, lang)
        elif path in ARTICLES:
            path = ARTICLES[path].get(lang) or ARTICLES[path].get('en') or path
        else:
            m = re.match(r'^/(foods|supplements)/([a-z0-9-]+)\.html$', path)
            if m:
                cand = f'/{lang}/{m.group(1)}/{m.group(2)}.html'
                path = cand if (ROOT / cand.lstrip('/')).exists() else f'/en/{m.group(1)}/{m.group(2)}.html'
    out = path + ('?' + query if query else '') + ('#' + frag if frag else '')
    return SITE + out if absolute else out


def rewrite_links(page, lang):
    """Every href/src/srcset/action/poster and CSS url() of a page that is written one folder down."""
    def attr(m):
        name, q, value = m.group(1), m.group(2), m.group(3)
        if name == 'srcset':
            parts = [p.strip().split(' ', 1) for p in value.split(',')]
            return '%s=%s%s%s' % (name, q, ', '.join(' '.join([map_url(p[0], lang)] + p[1:]) for p in parts), q)
        return '%s=%s%s%s' % (name, q, map_url(value, lang), q)
    page = re.sub(r'(?<![-\w])(href|src|srcset|action|poster|data-src)=(["\'])([^"\']*)\2', attr, page)
    page = re.sub(r'url\((["\']?)(?!https?:|data:|/|#)([^)"\']+)\1\)', lambda m: 'url(%s/%s%s)' % (m.group(1), m.group(2), m.group(1)), page)
    return page


# relative URLs built in the masters' own scripts (found by checking every master): absolute + language version
JS_URLS = {}   # foods.html's URL templates moved into js/foods-guide.js with absolute paths (2026-11-23)
SCRIPT_HREF = re.compile(r'(href=\\?["\'])((?![a-z]+:|/|#)[a-zA-Z0-9_-]+\.html(?:[?#][^"\'\\]*)?)')


def fix_js_urls(page, master, lang):
    """Inside <script>: href="x.html" in the dictionaries' HTML snippets and the listed URL templates point at the
    language version (a relative URL would resolve inside /en/ or /nl/)."""
    def script(m):
        body = SCRIPT_HREF.sub(lambda h: h.group(1) + map_url(h.group(2), lang), m.group(2))
        return m.group(1) + body + m.group(3)
    page = re.sub(r'(<script\b[^>]*>)(.*?)(</script>)', script, page, flags=re.S)
    for old, target in JS_URLS.get(master, []):
        if old not in page:
            sys.exit(f'generate_root_pages: {master}: script URL {old} not found')
        page = page.replace(old, old[0] + map_url(target, lang))
    return page


def translate_extra(page, master, lang):
    """Arabic strings outside the dictionaries (scripts/root_pages_extra.py), replaced outside <script>/<style>."""
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>)', page, flags=re.S)
    def each(text, pairs, required):
        for ar, tr in pairs:
            if lang not in tr:
                continue
            if required and ar not in page:
                sys.exit(f'generate_root_pages: {master}: extra string not found: {ar[:50]}')
            text = text.replace(ar, tr[lang])
        return text
    alts = [(f'alt="{ar}"', {l: f'alt="{t}"' for l, t in tr.items()}) for ar, tr in EXTRA.ALTS.items()]
    for i in range(0, len(parts), 2):
        parts[i] = each(parts[i], EXTRA.PAGES.get(master, []), False)
        parts[i] = each(parts[i], EXTRA.COMMON + alts, False)
    for ar, tr in EXTRA.PAGES.get(master, []):
        if lang in tr and ar not in page:
            sys.exit(f'generate_root_pages: {master}: extra string not found: {ar[:50]}')
    return ''.join(parts)


# ----------------------------------------------------------------------------------------------------------------------
# Head: language, title, description, alternates, structured data
# ----------------------------------------------------------------------------------------------------------------------
def cluster(master):
    return site_urls.ROOT_PAGES[master]


def page_path(master, lang):
    return cluster(master)[lang]


def abs_url(path):
    return SITE + path


def alternates(master):
    c = cluster(master)
    lines = [f'    <link rel="alternate" hreflang="{l}" href="{abs_url(c[l])}">' for l in site_urls.LANGS if l in c]
    xd = c.get(site_urls.X_DEFAULT) or c['ar']
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{abs_url(xd)}">')
    return lines


def git_date(path):
    out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or TODAY


def text_of(fragment):
    return ' '.join(htmllib.unescape(re.sub(r'<[^>]+>', ' ', fragment)).split())


def schema(master, lang, title, desc, h1):
    """JSON-LD for one language of a root page: the page node, the publisher, the doctor where credited, breadcrumbs."""
    cfg = SEO[master]
    url = abs_url(page_path(master, lang))
    image = f"{SITE}/images/{cfg.get('image') or DEFAULT_OG}"
    org = {"@type": "Organization", "@id": f"{SITE}/#organization", "name": ORG_NAME, "url": f"{SITE}/",
           "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png", "width": 512, "height": 512},
           "email": "support@wibohealth.com"}
    doctor = {"@type": "Person", "@id": DOCTOR_ID, "name": "Dr. Wassim Habib", "jobTitle": JOB_TITLE[lang],
              "url": f"{SITE}/doctor.html", "worksFor": {"@id": f"{SITE}/#organization"}}
    kind = cfg['kind']
    page_type = {'home': 'WebPage', 'about': 'AboutPage', 'profile': 'ProfilePage', 'contact': 'ContactPage',
                 'collection': 'CollectionPage', 'article': 'MedicalWebPage', 'app': 'WebPage', 'webpage': 'WebPage'}[kind]
    node = {"@type": page_type, "@id": url + '#webpage', "url": url, "name": title, "description": desc,
            "inLanguage": lang, "isPartOf": {"@id": f"{SITE}/#website"}, "publisher": {"@id": f"{SITE}/#organization"},
            "primaryImageOfPage": {"@type": "ImageObject", "url": image}, "dateModified": git_date(master.lstrip('/') or 'index.html')}
    graph = [node, org]
    if kind == 'home':
        graph.append({"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "WiBo Health",
                      "inLanguage": list(cluster(master)), "publisher": {"@id": f"{SITE}/#organization"}})
    if kind == 'profile':
        node['mainEntity'] = {"@id": DOCTOR_ID}
        graph.append(dict(doctor, image=image))
    if kind == 'article':
        art = {"@type": "Article", "@id": url + '#article', "headline": h1 or title, "description": desc,
               "inLanguage": lang, "image": image, "mainEntityOfPage": {"@id": url + '#webpage'},
               "dateModified": node['dateModified'], "publisher": {"@id": f"{SITE}/#organization"}}
        if cfg.get('author') == 'doctor':
            art['author'] = {"@id": DOCTOR_ID}
            node['reviewedBy'] = {"@id": DOCTOR_ID}
            graph.append(doctor)
        else:
            art['author'] = {"@id": f"{SITE}/#organization"}
        graph.append(art)
    if kind == 'app':
        graph.append({"@type": "MobileApplication", "name": "boodi", "applicationCategory": "HealthApplication",
                      "operatingSystem": "Android, iOS", "publisher": {"@id": f"{SITE}/#organization"}, "url": url})
    crumbs = [(CRUMB_HOME[lang], abs_url(site_urls.url_in('/', lang)))]
    if master != '/':
        crumbs.append((h1 or title, url))
    graph.append({"@type": "BreadcrumbList", "@id": url + '#breadcrumb', "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    node['breadcrumb'] = {"@id": url + '#breadcrumb'}
    return {"@context": "https://schema.org", "@graph": graph}


def set_meta(page, attr_name, key, value):
    pat = r'<meta\s+%s="%s"[^>]*>' % (attr_name, re.escape(key))
    tag = '<meta %s="%s" content="%s">' % (attr_name, key, htmllib.escape(value, quote=True))
    return re.sub(pat, lambda m: re.sub(r'content="[^"]*"', 'content="%s"' % htmllib.escape(value, quote=True), m.group(0)), page) \
        if re.search(pat, page) else page


HEAD_START, HEAD_END = '    <!-- ROOT-HEAD:START (scripts/generate_root_pages.py) -->', '    <!-- ROOT-HEAD:END -->'


def head_block(master, lang, title, desc, h1):
    data = json.dumps(schema(master, lang, title, desc, h1), ensure_ascii=False, indent=4)
    return '\n'.join([HEAD_START, f'    <link rel="canonical" href="{abs_url(page_path(master, lang))}">'] + alternates(master) +
                     ['    <script type="application/ld+json">', data, '    </script>', HEAD_END])


def rewrite_head(page, master, lang, title, desc, h1):
    """Replace canonical, alternates and every JSON-LD block of the page with the generated block (after <title>)."""
    page = re.sub(r'\n?[ \t]*<!-- ROOT-HEAD:START.*?<!-- ROOT-HEAD:END -->', '', page, flags=re.S)
    page = re.sub(r'\n?[ \t]*<!-- SV-ALTERNATES:START.*?<!-- SV-ALTERNATES:END -->', '', page, flags=re.S)
    page = re.sub(r'\n[ \t]*<!--[^\n]*(?:hreflang|EN/NL are served)[^\n]*-->', '', page)
    page = re.sub(r'\n[ \t]*<link rel="canonical"[^>]*>', '', page)
    page = re.sub(r'\n[ \t]*<link rel="alternate" hreflang="[^"]+"[^>]*>', '', page)
    page = re.sub(r'\n[ \t]*<script type="application/ld\+json">.*?</script>', '', page, flags=re.S)
    # share image: the page's own picture, else the 1200x630 brand card
    image = f"{SITE}/images/{SEO[master].get('image') or DEFAULT_OG}"
    for key in ('og:image', 'og:image:secure_url'):
        page = set_meta(page, 'property', key, image)
    page = set_meta(page, 'name', 'twitter:image', image)
    page = re.sub(r'\n[ \t]*<meta property="og:image:(?:width|height)"[^>]*>', '', page)
    if not SEO[master].get('image'):
        page = re.sub(r'(<meta property="og:image" [^>]*>)',
                      lambda m: m.group(1) + '\n    <meta property="og:image:width" content="1200">'
                                             '\n    <meta property="og:image:height" content="630">', page, count=1)
    m = re.search(r'</title>[^\n]*\n', page)
    if not m:
        sys.exit(f'generate_root_pages: {master}: no </title>')
    return page[:m.end()] + head_block(master, lang, title, desc, h1) + '\n' + page[m.end():]


# ----------------------------------------------------------------------------------------------------------------------
# Language switcher: plain links to each language's static page (no flags, AR/EN/NL/SV)
# ----------------------------------------------------------------------------------------------------------------------
SWITCH_RUN = re.compile(r'(?:[ \t]*<(button|a)\b[^>]*\bclass="lang-btn[^"]*"[^>]*>.*?</\1>[ \t]*\n)+', re.S)


def switcher(master, lang, indent):
    """Links to the page in every language it exists in; the Swedish link of a page without a Swedish version goes
    to the closest Swedish page (e.g. the Swedish supplement index)."""
    c = dict(cluster(master))
    for l, path in site_urls.LINK_ONLY.get(master, {}).items():
        c.setdefault(l, path)
    out = []
    for l in ('ar', 'en', 'nl', 'sv'):
        if l not in c:
            continue
        active = ' active' if l == lang else ''
        current = ' aria-current="page"' if l == lang else ''
        out.append(f'{indent}<a class="lang-btn{active}" href="{c[l]}" hreflang="{l}" lang="{l}" data-lang="{l}" '
                   f'data-lang-toggle="{l}" title="{LANG_NAME[l]}"{current}>{l.upper()}</a>\n')
    return ''.join(out)


def rewrite_switcher(page, master, lang):
    if master == '/recipes.html':
        return recipes_switcher(page, lang)
    m = SWITCH_RUN.search(page)
    if not m:
        sys.exit(f'generate_root_pages: {master}: language switcher not found')
    indent = re.match(r'[ \t]*', m.group(0)).group(0)
    return page[:m.start()] + switcher(master, lang, indent) + page[m.end():]


def recipes_switcher(page, lang):
    """recipes.html has one toggle button per direction (Arabic <-> English) styled as .theme-toggle."""
    pat = re.compile(r'([ \t]*)<button class="theme-toggle" data-lang-toggle="en".*?</button>\s*\n[ \t]*'
                     r'<button class="theme-toggle" data-lang-toggle="ar".*?</button>[ \t]*\n', re.S)
    m = pat.search(page) or re.search(r'([ \t]*)<a class="theme-toggle" href="[^"]*" hreflang="(?:ar|en)"[^>]*>(?:AR|EN)</a>[ \t]*\n', page)
    if not m:
        sys.exit('generate_root_pages: recipes.html: language toggle not found')
    ind = m.group(1)
    other, label, title = ('en', 'EN', 'English') if lang == 'ar' else ('ar', 'AR', 'العربية')
    link = (f'{ind}<a class="theme-toggle" href="{cluster("/recipes.html")[other]}" hreflang="{other}" lang="{other}" '
            f'title="{title}" style="text-decoration:none;font-weight:700">{label}</a>\n')
    return page[:m.start()] + link + page[m.end():]


# ----------------------------------------------------------------------------------------------------------------------
# One page in one language
# ----------------------------------------------------------------------------------------------------------------------
def h1_text(page):
    m = re.search(r'<h1\b[^>]*>(.*?)</h1>', page, re.S)
    return text_of(m.group(1)) if m else ''


def recipes_english(page):
    """recipes.html shows [data-lang="ar"] / [data-lang="en"] twins; the English page keeps only the English ones
    visible in the HTML (the elements the scripts look up by id stay, hidden)."""
    def fix(m):
        tag = m.group(0)
        if 'data-lang="en"' in tag:
            return re.sub(r'\s*style="display: none;"', '', tag)
        return tag
    page = re.sub(r'<[a-z0-9]+\b[^>]*\bdata-lang="en"[^>]*>', fix, page)
    # Arabic twins: drop those without an id, hide those with one
    def drop(m):
        tag, name, inner = m.group(1), m.group(2), m.group(3)
        if ' id="' in tag:
            return tag[:-1] + ' style="display: none;">' + inner + f'</{name}>' if 'style=' not in tag else m.group(0)
        return ''
    page = re.sub(r'(<(span|h2|h3|p|strong|label|div)\b[^>]*\bdata-lang="ar"[^>]*>)(.*?)</\2>', drop, page, flags=re.S)
    page = re.sub(r'(<input\b[^>]*\bdata-lang="ar"[^>]*?)(\s*/?>)', lambda m: m.group(1) + ' style="display: none;"' + m.group(2)
                  if 'style=' not in m.group(1) else m.group(0), page)
    page = re.sub(r'(<input\b[^>]*\bdata-lang="en"[^>]*?)\s*style="display: none;"', r'\1', page)
    return page


DIABETES_LABEL = {'en': 'Diabetes', 'nl': 'Diabetes', 'sv': 'Diabetes'}

# ----------------------------------------------------------------------------------------------------------------------
# Static, crawlable links on the two JavaScript guides (foods.html, supplements.html): the guides draw their cards
# from js/data.js / js/supplements-data.js, so without this block their HTML held no links to the item pages.
# ----------------------------------------------------------------------------------------------------------------------
HUB_TEXT = {
    '/foods.html': {
        'ar': dict(h1='دليل الأطعمة: المؤشر الجلايسيمي ومؤشر الإنسولين والسعرات',
                   intro='ابحث في أكثر من 970 طعاماً حسب المؤشر الجلايسيمي والحمل الجلايسيمي ومؤشر الإنسولين والسعرات والبروتين والكربوهيدرات والدهون والألياف. لكل طعام صفحة مستقلة بالقيم لكل 100 غ وللحصة، مع مصدر كل قيمة (منشورة أو تقدير).',
                   groups='أقسام دليل الأطعمة', items='أطعمة شائعة', all='كل الأطعمة من الألف إلى الياء'),
        'en': dict(h1='Food guide: glycemic index, insulin index and calories',
                   intro='Search 970+ foods by glycemic index, glycemic load, insulin index, calories, protein, carbohydrates, fat and fibre. Every food has its own page with values per 100 g and per portion, and the source of each value (published or estimate).',
                   groups='Food groups', items='Popular foods', all='All foods A–Z'),
        'nl': dict(h1='Voedingswijzer: glykemische index, insuline-index en calorieën',
                   intro='Zoek in 970+ voedingsmiddelen op glykemische index, glykemische lading, insuline-index, calorieën, eiwit, koolhydraten, vet en vezels. Elk product heeft een eigen pagina met waarden per 100 g en per portie, en de bron van elke waarde (gepubliceerd of schatting).',
                   groups='Productgroepen', items='Populaire producten', all='Alle producten van A tot Z'),
        'sv': dict(h1='Livsmedelsguide: glykemiskt index, insulinindex och kalorier',
                   intro='Sök bland 970+ livsmedel efter glykemiskt index, glykemisk belastning, insulinindex, kalorier, protein, kolhydrater, fett och fibrer. Varje livsmedel har en egen sida med värden per 100 g och per portion, och källan till varje värde (publicerat eller uppskattning).',
                   groups='Livsmedelsgrupper', items='Populära livsmedel', all='Alla livsmedel A–Ö'),
    },
    '/supplements.html': {
        'ar': dict(items='مكملات شائعة', all='كل المكملات (174) من الألف إلى الياء'),
        'en': dict(items='Popular supplements', all='All 174 supplements A–Z'),
        'nl': dict(items='Populaire supplementen', all='Alle 174 supplementen van A tot Z'),
    },
}
HUB_ITEMS = 40


def hub_block(master, lang):
    """The HUB-LINKS block of foods.html / supplements.html in `lang` (pre-rendered here, no JavaScript)."""
    from generate_food_pages import FOOD_GROUP_LABELS, PILOT, food_url, load_foods, dir_url
    t = HUB_TEXT[master][lang]
    e = htmllib.escape
    out = ['<section class="hub-static" aria-labelledby="hubStaticTitle">']
    if master == '/foods.html':
        foods = load_foods()
        import food_sv as FSV
        from generate_food_pages import page_url as food_page_url
        slugs = json.loads(re.search(r'window\.FOOD_PAGES = (\{.*\});', (ROOT / 'js' / 'food-pages.js').read_text(encoding='utf-8')).group(1))
        out.append(f'<h1 id="hubStaticTitle">{e(t["h1"])}</h1><p>{e(t["intro"])}</p>')
        groups = ''.join(f'<li><a href="{dir_url("foods", lang, absolute=False)}#{g}">{e(lbl[lang])}</a></li>'
                         for g, lbl in FOOD_GROUP_LABELS.items())
        out.append(f'<h2>{e(t["groups"])}</h2><ul class="hub-links">{groups}</ul>')
        ids = sorted(PILOT)[:HUB_ITEMS]
        def nm(fid):
            if lang == 'sv':
                return FSV.NAMES[fid][0] if fid in FSV.NAMES else foods[fid]['en']
            return foods[fid][lang] or foods[fid]['en']
        items = ''.join(f'<li><a href="{food_page_url(slugs[str(fid)], lang, absolute=False)}">{e(nm(fid))}</a></li>' for fid in ids)
        out.append(f'<h2>{e(t["items"])}</h2><ul class="hub-links">{items}</ul>')
        out.append(f'<p><a class="hub-all" href="{dir_url("foods", lang, absolute=False)}">{e(t["all"])} →</a></p>')
    else:
        from generate_supplement_pages import load_supplements, page_url as supp_url, supp_name
        supps = sorted(load_supplements(), key=lambda s: s['id'])[:HUB_ITEMS]
        items = ''.join(f'<li><a href="{supp_url(s["slug"], lang, absolute=False)}">{e(supp_name(s, lang))}</a></li>' for s in supps)
        out.append(f'<h2 id="hubStaticTitle">{e(t["items"])}</h2><ul class="hub-links">{items}</ul>')
        out.append(f'<p><a class="hub-all" href="{dir_url("supplements", lang, absolute=False)}">{e(t["all"])} →</a></p>')
    out.append('</section>')
    return ''.join(out)


def fill_hub(page, master, lang):
    if master not in HUB_TEXT:
        return page
    m = re.search(r'([ \t]*)<!-- HUB-LINKS:START[^>]*-->.*?<!-- HUB-LINKS:END -->', page, re.S)
    if not m:
        sys.exit(f'generate_root_pages: {master}: HUB-LINKS markers not found')
    ind = m.group(1)
    block = f'{ind}<!-- HUB-LINKS:START (scripts/generate_root_pages.py) -->\n{ind}{hub_block(master, lang)}\n{ind}<!-- HUB-LINKS:END -->'
    return page[:m.start()] + block + page[m.end():]


def drop_twins(page, lang):
    """Copy that the master shows per language with CSS or a script (one twin per language) keeps only `lang`;
    Arabic-only blocks (the three long homepage guides marked "Arabic only") are left out of the other languages."""
    page = re.sub(r'\n *<h3 class="home-articles-h3" data-i18n="home_articles_guides">.*?\n            </div>\n(?=        </section>)',
                  '\n', page, flags=re.S)
    for other in ('ar', 'en', 'nl', 'sv'):
        if other == lang:
            continue
        page = re.sub(r'\n *<div class="meals-track" data-lang="%s" lang="%s">.*?\n *</div>\n *</div>' % (other, other), '', page, flags=re.S)
        page = re.sub(r'<span data-l="%s">[^<]*</span>' % other, '', page)
    page = page.replace('<span class="nav-diabetes-label">السكري ومتلازمة الأيض</span>',
                        f'<span class="nav-diabetes-label">{DIABETES_LABEL[lang]}</span>')
    return page


GUIDE_SCRIPTS = ('foods-guide.js', 'supplements-guide.js')


def dictionary_source(src):
    """The page plus the guide script it loads (js/foods-guide.js, js/supplements-guide.js hold their dictionaries)."""
    extra = [(ROOT / 'js' / name).read_text(encoding='utf-8') for name in GUIDE_SCRIPTS if f'/js/{name}' in src]
    return src + '\n'.join(extra)


def localise(master, lang, src):
    """The `lang` page of `master` from the Arabic source text `src`."""
    cfg = SEO[master]
    title, desc = cfg['meta'][lang]
    page = drop_twins(src, lang)
    if master == '/recipes.html':
        page = recipes_english(page)
    else:
        dsrc = dictionary_source(src)
        copy = root_i18n.extract(dsrc)[lang]
        missing = set()
        page = root_i18n.apply(page, copy, root_i18n.mode_of(dsrc), missing)
        if missing:
            sys.exit(f'generate_root_pages: {master} [{lang}]: no {lang} copy for {sorted(missing)}')
    page = re.sub(r'<html\b[^>]*>', lambda m: re.sub(r'\bdir="[^"]*"', 'dir="ltr"', re.sub(r'\blang="[^"]*"', f'lang="{lang}"', m.group(0))), page, count=1)
    page = re.sub(r'<title\b([^>]*)>.*?</title>', lambda m: '<title%s>%s</title>' % (m.group(1), htmllib.escape(title, quote=False)), page, count=1, flags=re.S)
    page = re.sub(r'<meta\s+name="description"[^>]*>', lambda m: re.sub(r'content="[^"]*"', 'content="%s"' % htmllib.escape(desc, quote=True), m.group(0)), page, count=1)
    page = re.sub(r'\n[ \t]*<meta\s+name="(?:keywords|title)"[^>]*>', '', page)
    for key, value in (('og:title', title), ('og:description', desc), ('og:url', abs_url(page_path(master, lang))),
                       ('og:locale', OG_LOCALE[lang])):
        page = set_meta(page, 'property', key, value)
    page = re.sub(r'\n[ \t]*<meta property="og:locale:alternate"[^>]*>', '', page)
    for key, value in (('twitter:title', title), ('twitter:description', desc), ('twitter:url', abs_url(page_path(master, lang)))):
        page = set_meta(page, 'name', key, value)
    page = translate_extra(page, master, lang)
    page = fill_hub(page, master, lang)
    page = rewrite_links(page, lang)
    page = fix_js_urls(page, master, lang)
    page = rewrite_switcher(page, master, lang)
    page = rewrite_head(page, master, lang, title, desc, h1_text(page))
    return page


def update_master(master, src):
    """The Arabic master: generated head block (canonical, alternates, JSON-LD) and the static language links."""
    m = re.search(r'<title\b[^>]*>(.*?)</title>', src, re.S)
    title = text_of(m.group(1))
    d = re.search(r'<meta\s+name="description"[^>]*content="([^"]*)"', src)
    desc = htmllib.unescape(d.group(1)) if d else title
    page = rewrite_switcher(src, master, 'ar')
    page = fill_hub(page, master, 'ar')
    return rewrite_head(page, master, 'ar', title, desc, h1_text(page))


def check(master, lang, page):
    """Fail on anything a crawler would get wrong."""
    body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', page, flags=re.S)
    if lang != 'ar':
        visible = re.sub(r'<[^>]+>', ' ', body)
        attrs = ' '.join(v for tag in re.findall(r'<[a-z][^>]*>', body) if 'lang-btn' not in tag and 'hreflang="ar"' not in tag
                         for v in re.findall(r'\b(?:alt|title|aria-label|placeholder|content)="([^"]*)"', tag))
        arabic = re.findall(r'[؀-ۿ]+(?:\s+[؀-ۿ]+)*', visible + ' ' + attrs)
        if arabic:
            sys.exit(f'generate_root_pages: {master} [{lang}]: Arabic text left: {arabic[:40]}')
    if '?lang=' in re.sub(r'<script\b.*?</script>', '', page, flags=re.S):
        sys.exit(f'generate_root_pages: {master} [{lang}]: a ?lang= URL is left in the HTML')
    if page.count('<h1') != 1:
        sys.exit(f'generate_root_pages: {master} [{lang}]: {page.count("<h1")} <h1> elements')
    if page.count('rel="canonical"') != 1:
        sys.exit(f'generate_root_pages: {master} [{lang}]: canonical count {page.count(chr(34) + "canonical")}')
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S):
        json.loads(block)


def check_meta():
    for master, cfg in SEO.items():
        for lang, (t, d) in cfg['meta'].items():
            assert 38 <= len(t) <= 60, f'{master} [{lang}] title {len(t)}: {t}'
            assert 120 <= len(d) <= 160, f'{master} [{lang}] description {len(d)}: {d}'
        img = ROOT / 'images' / (cfg.get('image') or DEFAULT_OG)
        assert img.exists(), f'{master}: missing image {img}'
        missing = [l for l in site_urls.ROOT_PAGES[master] if l != 'ar' and owns(master, l) and l not in cfg['meta']]
        assert not missing, f'{master}: no title/description for {missing}'


def owns(master, lang):
    """Languages written here: en/nl of every root page, plus the Swedish view of the food guide."""
    return lang in ('en', 'nl') or (master == '/foods.html' and lang == 'sv')


def read(path):
    raw = path.read_bytes().decode('utf-8-sig')
    return raw.replace('\r\n', '\n')


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_bytes().decode('utf-8-sig').replace('\r\n', '\n') if path.exists() else None
    if old != text:
        path.write_text(text, encoding='utf-8', newline='\n')
        return True
    return False


def sitemap():
    lines = []
    for master, c in site_urls.ROOT_PAGES.items():
        priority = '1.0' if master == '/' else '0.8'
        for lang, path in c.items():
            if not (ROOT / (path.lstrip('/') or 'index.html')).exists():
                sys.exit(f'generate_root_pages: sitemap: {path} does not exist')
            lines += ['  <url>', f'    <loc>{abs_url(path)}</loc>', f'    <lastmod>{git_date(path.lstrip("/") or "index.html")}</lastmod>',
                      f'    <priority>{priority}</priority>']
            lines += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(c[l])}"/>' for l in site_urls.LANGS if l in c]
            lines += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(c.get(site_urls.X_DEFAULT) or c["ar"])}"/>',
                      '  </url>']
    for path in ARABIC_ONLY_INDEXED:                   # indexable pages that exist in Arabic only (no alternates)
        lines += ['  <url>', f'    <loc>{abs_url(path)}</loc>', f'    <lastmod>{git_date(path.lstrip("/"))}</lastmod>',
                  '    <priority>0.5</priority>', '  </url>']
    replace_sitemap_block('ROOT-PAGES', lines)


ARABIC_ONLY_INDEXED = ['/diet-plan.html']


SECURITY_HEADERS = [   # moved from the Cloudflare-only _headers file (Vercel ignores it)
    {"key": "X-Content-Type-Options", "value": "nosniff"},
    {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
]


def vercel():
    """vercel.json: a 301 from every old ?lang= URL of a root page to its static page, the language folders' bare
    paths to their homepages, and no catch-all redirects (an unknown URL gets the 404 page, not a soft redirect).
    Hand-written rules for other paths are kept as they are."""
    path = ROOT / 'vercel.json'
    cfg = json.loads(path.read_text(encoding='utf-8'))
    masters = set(site_urls.ROOT_PAGES)
    def generated(r):
        src = r.get('source', '')
        if any(h.get('key') == 'lang' for h in r.get('has', [])) and src in masters:
            return True
        if src in ('/en', '/nl', '/sv'):
            return True
        return bool(re.match(r'^/(en|nl|sv)/:path', src))       # old catch-alls (soft 404s)
    keep = [r for r in cfg['redirects'] if not generated(r)]
    rules = []
    for master in site_urls.ROOT_PAGES:
        for lang in ('en', 'nl', 'sv'):
            dest = site_urls.url_in(master, lang)
            if dest == master:
                continue
            rules.append({"source": master, "has": [{"type": "query", "key": "lang", "value": lang}],
                          "destination": dest, "statusCode": 301})
    folders = [{"source": f"/{l}", "destination": site_urls.ROOT_PAGES['/'][l], "statusCode": 301} for l in ('en', 'nl', 'sv')]
    # the ?lang rules must come before "/index.html" -> "/" style rules only for their own sources; order: generated first
    cfg['redirects'] = rules + folders + keep
    headers = [h for h in cfg.get('headers', []) if h.get('source') != '/(.*)']
    cfg['headers'] = [{"source": "/(.*)", "headers": SECURITY_HEADERS}] + headers
    text = json.dumps(cfg, ensure_ascii=False, indent=2) + '\n'
    if text != path.read_text(encoding='utf-8'):
        path.write_text(text, encoding='utf-8', newline='\n')
    # every page in the sitemaps must not be caught by a redirect rule
    return cfg


def main():
    import build_guide_data
    print('guide data:', build_guide_data.build())
    check_meta()
    changed, errors = [], []
    for master in site_urls.ROOT_PAGES:
        src_path = ROOT / (master.lstrip('/') or 'index.html')
        src = read(src_path)
        master_page = update_master(master, src)
        check(master, 'ar', master_page)
        if write(src_path, master_page):
            changed.append(str(src_path.relative_to(ROOT)))
        for lang, path in site_urls.ROOT_PAGES[master].items():
            if lang == 'ar' or not owns(master, lang):
                continue
            try:
                page = localise(master, lang, master_page)
                check(master, lang, page)
            except SystemExit as e:
                errors.append(str(e))
                continue
            out = ROOT / path.lstrip('/')
            if write(out, page):
                changed.append(str(out.relative_to(ROOT)))
    if errors:
        sys.exit('\n'.join(errors))
    sitemap()
    vercel()
    print(f'root pages: {len(site_urls.ROOT_PAGES)} masters, '
          f'{sum(owns(m, l) for m, c in site_urls.ROOT_PAGES.items() for l in c if l != "ar")} language pages; '
          f'{len(changed)} files changed')


if __name__ == '__main__':
    main()
