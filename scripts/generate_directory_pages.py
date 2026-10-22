"""Generate static, crawlable index pages that link every food and supplement page in three languages.

    python scripts/generate_directory_pages.py

Run it after generate_food_pages.py and generate_supplement_pages.py (it reads the slug maps they write).

Output:
    foods/index.html, en/foods/index.html, nl/foods/index.html                    every food page, grouped by food group
    supplements/index.html, en/supplements/index.html, nl/supplements/index.html  every supplement page, grouped by area
    sitemap.xml   block between <!-- DIRECTORY-PAGES:START --> and <!-- DIRECTORY-PAGES:END -->

foods.html and supplements.html build their cards in JavaScript, and /en/*.html and /nl/*.html hubs redirect to /,
so without these pages the 3,000+ static pages are only reachable through the sitemap and each other.
The food and supplement pages link here from their breadcrumb and footer.
"""
import json
import re
from pathlib import Path

from generate_food_pages import (BASE_CSS, FOOD_GROUP_LABELS, LANGS, LOGO_SVG, PAGE_CSS, SITE, UI, dir_url, esc,
                                 load_foods, nav_html, replace_sitemap_block, site_link)
from generate_supplement_pages import GA_TAG, NAME as SUPP_NAME, load_supplements

ROOT = Path(__file__).resolve().parent.parent
UPDATED = '2026-10-22'

T = {
    'foods': {
        'ar': dict(title='فهرس الأطعمة: {n} صفحة بالسعرات ومؤشر الجلايسيمي | WiBo Health', h1='فهرس الأطعمة',
                   desc='كل صفحات دليل الأطعمة في مكان واحد ({n} طعاماً)، مرتبة حسب المجموعة الغذائية: السعرات الحرارية والبروتين والكربوهيدرات ومؤشر الجلايسيمي.',
                   intro='كل صفحات دليل الأطعمة في مكان واحد، مرتبة حسب المجموعة الغذائية. لكل طعام صفحة خاصة بالسعرات الحرارية والبروتين والكربوهيدرات، ومؤشر الجلايسيمي والحمل الجلايسيمي عند توفرهما.',
                   cta='افتح الدليل التفاعلي للبحث والمقارنة', count='{n} طعاماً'),
        'en': dict(title='Food Index: {n} foods with calories and glycemic index | WiBo Health', h1='Food index',
                   desc='Every page of the food guide in one place ({n} foods), sorted by food group: calories, protein, carbohydrates and glycemic index.',
                   intro='Every page of the food guide in one place, sorted by food group. Each food has its own page with calories, protein and carbohydrates, plus the glycemic index and glycemic load where available.',
                   cta='Open the interactive guide to search and compare', count='{n} foods'),
        'nl': dict(title='Voedingsindex: {n} voedingsmiddelen met calorieën en glykemische index | WiBo Health', h1='Voedingsindex',
                   desc='Alle pagina\'s van de voedingswijzer op één plek ({n} voedingsmiddelen), per voedingsgroep: calorieën, eiwit, koolhydraten en glykemische index.',
                   intro='Alle pagina\'s van de voedingswijzer op één plek, gesorteerd per voedingsgroep. Elk voedingsmiddel heeft een eigen pagina met calorieën, eiwit en koolhydraten, en waar beschikbaar de glykemische index en glykemische lading.',
                   cta='Open de interactieve gids om te zoeken en te vergelijken', count='{n} voedingsmiddelen'),
    },
    'supplements': {
        'ar': dict(title='فهرس المكملات الغذائية: {n} مكملاً بالجرعات والتداخلات الدوائية | WiBo Health', h1='فهرس المكملات الغذائية',
                   desc='كل صفحات دليل المكملات في مكان واحد ({n} مكملاً)، مرتبة حسب المجال: الجرعة الموصى بها والتحذيرات والتداخلات الدوائية وفق EFSA وNIH.',
                   intro='كل صفحات دليل المكملات في مكان واحد، مرتبة حسب المجال. لكل مكمل صفحة خاصة بالجرعة الموصى بها وأفضل الأشكال والتحذيرات والتداخلات الدوائية، مع المراجع العلمية المنشورة (EFSA / NIH / PubMed).',
                   cta='افتح دليل المكملات التفاعلي', count='{n} مكملاً', guide='دليل المكملات'),
        'en': dict(title='Supplement Index: {n} supplements with dosage and drug interactions | WiBo Health', h1='Supplement index',
                   desc='Every page of the supplements guide in one place ({n} supplements), sorted by area: recommended dose, warnings and drug interactions based on EFSA and NIH.',
                   intro='Every page of the supplements guide in one place, sorted by area. Each supplement has its own page with the recommended dose, the best forms, warnings and drug interactions, with the published scientific references (EFSA / NIH / PubMed).',
                   cta='Open the interactive supplements guide', count='{n} supplements', guide='Supplements Guide'),
        'nl': dict(title='Supplementenindex: {n} supplementen met dosering en interacties | WiBo Health', h1='Supplementenindex',
                   desc='Alle pagina\'s van de supplementengids op één plek ({n} supplementen), per gebied: aanbevolen dosis, waarschuwingen en interacties met medicijnen volgens EFSA en NIH.',
                   intro='Alle pagina\'s van de supplementengids op één plek, gesorteerd per gebied. Elk supplement heeft een eigen pagina met de aanbevolen dosis, de beste vormen, waarschuwingen en interacties met medicijnen, met de gepubliceerde wetenschappelijke bronnen (EFSA / NIH / PubMed).',
                   cta='Open de interactieve supplementengids', count='{n} supplementen', guide='Supplementengids'),
    },
}

EXTRA_CSS = """
        .dir-jump { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 22px; }
        .dir-jump a { text-decoration: none; }
        .dir-list { grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }
        .dir-list a { font-weight: 700; }
        .dir-list span { white-space: normal; text-align: end; font-size: 0.85rem; }
        .guide-link { display: inline-flex; align-items: center; gap: 8px; margin: 4px 8px 22px 0; padding: 10px 18px; border-radius: 30px;
            border: 1px solid var(--primary); color: var(--primary); font-weight: 800; text-decoration: none; }
        .guide-link:hover { background: var(--primary-glow); }
"""


def item_url(kind, slug, lang):
    return f'/{kind}/{slug}.html' if lang == 'ar' else f'/{lang}/{kind}/{slug}.html'


def read_slug_map(js_file, var):
    text = (ROOT / 'js' / js_file).read_text(encoding='utf-8')
    return json.loads(re.search(r'window\.%s = (\{.*\});' % var, text).group(1))


def food_sections():
    """[(anchor, {lang: label}, [(slug, {lang: name}, {lang: subtitle})])] in the foods.html filter-bar order."""
    foods, slugs = load_foods(), read_slug_map('food-pages.js', 'FOOD_PAGES')
    sections = {key: [] for key in FOOD_GROUP_LABELS}
    for fid, slug in slugs.items():
        f = foods[int(fid)]
        names = {l: f[l] or f['en'] for l in LANGS}
        subs = {'ar': f['en'], 'en': f['nl'], 'nl': f['en']}
        sections[f['group']].append((slug, names, {l: subs[l] if subs[l] != names[l] else '' for l in LANGS}))
    return [(key, FOOD_GROUP_LABELS[key], items) for key, items in sections.items() if items]


def supplement_sections():
    """One A-Z section: the ~70 area labels hold two or three supplements each, so the area goes beside the name."""
    pages = read_slug_map('supplement-pages.js', 'SUPP_PAGES')
    items = [(s['slug'], {l: s[SUPP_NAME[l]] or s['name'] for l in LANGS}, s['groupLabel'])
             for s in load_supplements() if s.get('references') and s['slug'] in pages]
    return [('a-z', {'ar': 'كل المكملات أبجدياً', 'en': 'All supplements A–Z', 'nl': 'Alle supplementen A–Z'}, items)]


def build(kind, lang, sections):
    t, u = T[kind][lang], UI[lang]
    n = sum(len(items) for _, _, items in sections)
    title, desc = t['title'].format(n=n), t['desc'].format(n=n)
    urls = {l: dir_url(kind, l) for l in LANGS}
    hub = '/foods.html' if kind == 'foods' else '/supplements.html'
    hub_label = u['guide'] if kind == 'foods' else t['guide']
    other = 'supplements' if kind == 'foods' else 'foods'

    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": title,
        "description": desc,
        "inLanguage": lang,
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "dateModified": UPDATED,
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + site_link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": t['h1'], "item": urls[lang]}]},
    }

    for_lang = lambda items: sorted(items, key=lambda it: it[1][lang].casefold())
    jump = ''.join(f'<a class="group-chip" href="#{anchor}">{esc(labels[lang])} ({len(items)})</a>'
                   for anchor, labels, items in sections) if len(sections) > 1 else ''
    body = '\n'.join(
        f'            <h2 class="section-title" id="{anchor}"><span>{esc(labels[lang])}</span></h2>\n'
        f'            <ul class="alt-list dir-list">' + ''.join(
            f'<li><a href="{item_url(kind, slug, lang)}">{esc(names[lang])}'
            + (f'<span>{esc(subs[lang])}</span>' if subs[lang] else '') + '</a></li>'
            for slug, names, subs in for_lang(items)) + '</ul>'
        for anchor, labels, items in sections)

    nav = nav_html(lang, active=hub)
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{dir_url(kind, l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧')))
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in LANGS)
    footer_links = ' <span>•</span> '.join(
        f'<a href="{href}">{label}</a>' for href, label in
        [(site_link('/', lang), u['nav'][0]), (dir_url('foods', lang, absolute=False), T['foods'][lang]['h1']),
         (dir_url('supplements', lang, absolute=False), T['supplements'][lang]['h1']),
         (site_link('/methodology.html', lang), u['methodology']), (site_link('/partners.html', lang), u['partners']),
         (site_link('/privacy.html', lang), u['privacy'])])

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{u["dir"]}" data-theme="dark">
<head>
{GA_TAG}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{urls[lang]}">
{hreflang}
    <link rel="alternate" hreflang="x-default" href="{urls['ar']}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{urls[lang]}">
    <meta property="og:image" content="{SITE}/images/logo.png">
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL')[lang]}">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=4)}
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#0f172a">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/icon-192.png">
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
    <!-- Theme boot: one theme for the whole site (saved choice, else the OS setting), set before the first paint -->
    <script>(function(h){{var t;try{{t=localStorage.getItem('wibo_theme')}}catch(e){{}}if(t!=='dark'&&t!=='light'){{t=window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';try{{localStorage.setItem('wibo_theme',t)}}catch(e){{}}}}h.setAttribute('data-theme',t)}})(document.documentElement);</script>
    <style>
{BASE_CSS}{PAGE_CSS}{EXTRA_CSS}    </style>
    <link rel="stylesheet" href="/css/unified-header.css">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="{site_link('/', lang)}" class="brand-link">
                {LOGO_SVG}
                <span class="brand-title">WiBo Health</span>
            </a>
            <nav class="nav-links-bar">
{nav}
            </nav>
            <div class="header-actions">
                <button type="button" class="theme-toggle-btn" onclick="toggleTheme()" title="{u["theme"]}" aria-label="{u["theme"]}">
                    <i class="fas fa-sun" id="themeIcon"></i>
                </button>
                <div class="lang-switcher-container">
{lang_links}
                </div>
            </div>
        </div>
    </header>

    <main class="page-wrapper food-page directory-page">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{site_link('/', lang)}">{u["home"]}</a> › <span>{esc(t["h1"])}</span>
            </nav>
            <h1>{esc(t["h1"])}</h1>
            <p class="lead">{esc(t["intro"])} <strong>{esc(t["count"].format(n=n))}</strong></p>
            <a class="guide-link" href="{site_link(hub, lang)}"><i class="fas fa-magnifying-glass"></i> {esc(t["cta"])}</a>
            <a class="guide-link" href="{dir_url(other, lang, absolute=False)}"><i class="fas fa-list"></i> {esc(T[other][lang]["h1"])}</a>
            {f'<nav class="dir-jump" aria-label="{esc(hub_label)}">{jump}</nav>' if jump else ''}
{body}
        </article>
    </main>

    <footer>
        <div class="footer-links">{footer_links}</div>
        <p>{u["footer_rights"]}</p>
    </footer>

    <script>
        function applyTheme(theme) {{
            document.documentElement.setAttribute('data-theme', theme);
            var icon = document.getElementById('themeIcon');
            if (icon) icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
        }}
        function toggleTheme() {{
            var next = (document.documentElement.getAttribute('data-theme') || 'dark') === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            try {{ localStorage.setItem('wibo_theme', next); }} catch (e) {{}}
        }}
        applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
    </script>
</body>
</html>
'''


def main():
    kinds = {'foods': food_sections(), 'supplements': supplement_sections()}
    lines = []
    for kind, sections in kinds.items():
        for lang in LANGS:
            out = ROOT / dir_url(kind, lang, absolute=False).lstrip('/')
            out.write_text(build(kind, lang, sections), encoding='utf-8', newline='\n')
            lines += ['  <url>', f'    <loc>{dir_url(kind, lang)}</loc>', f'    <lastmod>{UPDATED}</lastmod>',
                      '    <changefreq>weekly</changefreq>', '    <priority>0.8</priority>']
            lines += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{dir_url(kind, l)}"/>' for l in LANGS]
            lines += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{dir_url(kind, "ar")}"/>', '  </url>']
        print(f'{kind}: {sum(len(i) for _, _, i in sections)} links in {len(sections)} sections x {len(LANGS)} languages')
    replace_sitemap_block('DIRECTORY-PAGES', lines)


if __name__ == '__main__':
    main()
