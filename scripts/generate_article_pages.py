"""Generate static, crawlable article pages in three languages, plus Swedish where an article has Swedish copy.

    python scripts/generate_article_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    articles/<slug>.html       Arabic (x-default)
    en/articles/<slug>.html    English
    nl/articles/<slug>.html    Dutch
    <section>.html, en/<section>.html, nl/<section>.html          hub page of a section (e.g. diabetes.html)
    <section>/<slug>.html, en/<section>/..., nl/<section>/...      articles that belong to a section
    sv/...                     Swedish, only for articles and sections whose content has an `sv` entry (hreflang and
                               sitemap then list sv too); Swedish pages link to the English version of untranslated pages
    legacy=dict(ar='/x.html')  an article that only has Swedish copy here and is the sv version of an older hand-written
                               ?lang page: the generator writes the Swedish page and adds hreflang ar/sv/x-default, an SV
                               flag and ?lang=sv forwarding to that page (marked blocks, safe to re-run)
    sitemap.xml                block between <!-- ARTICLE-PAGES:START --> and <!-- ARTICLE-PAGES:END -->

An article with section='diabetes' is written under that section's folder and its breadcrumb runs through the hub.
draft=True (article or section) writes the page with noindex and keeps it out of the sitemap, so a placeholder can
live on the site before its content is ready.

Source: scripts/article_content.py. Editorial policy: the author and publisher are the WiBo Health organization,
never a named person; structure/function wording only. Design system, header and footer come from
generate_food_pages.py, so the pages match the food and supplement pages.
"""
import json
import re
from pathlib import Path

from article_content import ARTICLES, SECTIONS
from site_pages_sv import SITE_PAGES_SV
from generate_food_pages import BASE_CSS, LOGO_SVG, PAGE_CSS, SITE, LANGS, UI, esc, nav_html, replace_sitemap_block, site_link

GA_TAG = """    <!-- Google tag (gtag.js) with Consent Mode v2: everything stays denied until the visitor accepts (js/consent.js) -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('consent', 'default', {'ad_storage': 'denied', 'ad_user_data': 'denied', 'ad_personalization': 'denied', 'analytics_storage': 'denied', 'wait_for_update': 500});
      try { if (localStorage.getItem('wibo_consent') === 'granted') gtag('consent', 'update', {'ad_storage': 'granted', 'ad_user_data': 'granted', 'ad_personalization': 'granted', 'analytics_storage': 'granted'}); } catch (e) {}
    </script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-WG6S4KXXJS"></script>
    <script>
      gtag('js', new Date());

      gtag('config', 'G-WG6S4KXXJS');
    </script>
    <script src="/js/consent.js?v=3" defer></script>"""   # GA4 property of wibohealth.com, first thing in every <head>


ROOT = Path(__file__).resolve().parent.parent
SV = 'sv'
ALL_LANGS = LANGS + (SV,)   # Swedish is opt-in per article / section; the food generator's LANGS stay ar/en/nl

# generate_food_pages.UI has no Swedish: the strings the article shell needs
UI_SV = dict(dir='ltr', nav=('Hem', 'Livsmedelsguide', 'Kalkylatorer', 'Kosttillskott', 'Artiklar', 'boodi-appen 💚'),
             home='Hem', theme='Byt tema', footer_rights='© 2026 WiBo Health Group. Alla rättigheter förbehållna.',
             methodology='Metod och vetenskapliga källor', partners='Samarbeten', privacy='Integritet', diabetes='Diabetes')


def ui(lang):
    return UI_SV if lang == SV else UI[lang]


def langs_of(item):
    """Languages an article or section exists in (ar/en/nl always, sv when it has Swedish copy)."""
    return tuple(l for l in ALL_LANGS if l in item['content'])


def alt_langs(a):
    """hreflang languages of an article: its own pages plus the legacy page it is the Swedish version of."""
    return tuple(l for l in ALL_LANGS if l in a['content'] or l in a.get('legacy', {}))


def site_page_url(p, absolute=True):
    """A Swedish site page (doctor, about, legal, contact): /sv/<slug>.html."""
    path = f'/sv/{p["slug"]}.html'
    return SITE + path if absolute else path


def sv_page_of(path):
    """The Swedish page that stands in for a legacy page (e.g. /insulin-resistance.html, /privacy.html), or None."""
    bare = path.split('#')[0].split('?')[0]
    frag = '#' + path.split('#', 1)[1] if '#' in path else ''
    for a in ARTICLES:
        if a.get('legacy', {}).get('ar') == bare and SV in a['content']:
            return page_url(a, SV, absolute=False) + frag
    for p in SITE_PAGES_SV:
        if p['legacy'] == bare:
            return site_page_url(p, absolute=False) + frag
    return None


def link(path, lang):
    """site_link() for every language: the Swedish homepage is static, pages with a Swedish version open in Swedish,
    the rest in English."""
    if lang != SV:
        return site_link(path, lang)
    if path in ('/', '/#articles'):
        return '/sv/index.html' + path[1:]
    if path.startswith('/sv/'):
        return path
    return sv_page_of(path) or site_link(path, 'en')


def nav(lang, active=None):
    """nav_html() for every language; the Swedish header points at /sv/ pages where they exist, English elsewhere."""
    if lang != SV:
        return nav_html(lang, active=active)
    u = UI_SV
    items = list(zip(['/', '/foods.html', '/calculators.html', '/supplements.html', '/#articles'], u['nav'][:5]))
    items += [('/diabetes.html', u['diabetes']), ('/boodi.html', u['nav'][5]), ('/partners.html', u['partners'])]
    out = []
    for path, label in items:
        href = '/sv/diabetes.html' if path == '/diabetes.html' else link(path, SV)
        cls = 'nav-link' + {'/partners.html': ' nav-partners', '/diabetes.html': ' nav-diabetes'}.get(path, '') + (' active' if path == active else '')
        out.append(f'                <a href="{href}" class="{cls}">{label}</a>')
    return '\n'.join(out)


T = {
    'ar': dict(dir='rtl', section='المقالات الصحية', published='نُشر في {date} · فريق WiBo Health', published_on='نُشر في {date}',
               refs='المصادر العلمية', footer_articles='المقالات', draft='مسودة · قيد الإعداد',
               months=('يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'),
               read='اقرأ المقال', soon='قريباً'),
    'en': dict(dir='ltr', section='Health articles', published='Published {date} · WiBo Health team', published_on='Published {date}',
               refs='Scientific sources', footer_articles='Articles', draft='Draft · in preparation',
               months=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December'),
               read='Read the article', soon='Coming soon'),
    'nl': dict(dir='ltr', section='Gezondheidsartikelen', published='Gepubliceerd op {date} · WiBo Health-team', published_on='Gepubliceerd op {date}',
               refs='Wetenschappelijke bronnen', footer_articles='Artikelen', draft='Concept · in voorbereiding',
               months=('januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober',
                       'november', 'december'),
               read='Lees het artikel', soon='Binnenkort'),
    'sv': dict(dir='ltr', section='Hälsoartiklar', published='Publicerad {date} · WiBo Health-teamet', published_on='Publicerad {date}',
               refs='Vetenskapliga källor', footer_articles='Artiklar', draft='Utkast · under arbete',
               months=('januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober',
                       'november', 'december'),
               read='Läs artikeln', soon='Kommer snart'),
}

EXTRA_CSS = """
        /* Open editorial layout: the article flows on the page background in a reading column, not inside a card */
        .page-wrapper.article-page { max-width: 850px; margin: 34px auto 70px; padding: 0 20px; }
        .article-page .about-card { background: none; border: 0; border-radius: 0; box-shadow: none; padding: 0; }
        .article-page .about-card p, .article-page .check-list li, .article-page .steps li { font-size: 1.06rem; line-height: 1.95; }
        .article-page .lead { font-size: 1.14rem; }
        .article-page h2.section-title { margin-top: 30px; }
        .article-hero-img { width: 100%; height: auto; aspect-ratio: 16 / 9; object-fit: cover; border-radius: var(--radius-md);
            box-shadow: var(--shadow); margin: 6px 0 18px; display: block; background: var(--bg-input); }
        /* portrait cover (hero_portrait=True): the whole photo, centred, never cropped */
        .article-hero-img.article-hero-portrait { aspect-ratio: auto; object-fit: contain; max-width: 580px; width: 100%; height: auto;
            border-radius: 16px; margin: 20px auto; display: block; }
        .article-meta { display: flex; flex-wrap: wrap; gap: 10px 16px; align-items: center; color: var(--text-muted); font-size: 0.88rem;
            font-weight: 600; margin-bottom: 18px; }
        .article-page h1 { font-size: 2rem; font-weight: 900; line-height: 1.35; margin-bottom: 10px; }
        .article-page p { margin: 0 0 14px; }
        .article-page h3 { font-size: 1.1rem; font-weight: 800; margin: 18px 0 8px; }
        .article-figure { margin: 18px 0 22px; }
        .article-figure img { width: 100%; height: auto; border-radius: var(--radius-md); display: block; box-shadow: var(--shadow); }
        .article-figure.figure-narrow { max-width: 600px; margin-inline: auto; }   /* portrait photos and square charts */
        .article-figure figcaption { color: var(--text-muted); font-size: 0.85rem; margin-top: 8px; text-align: center; }
        .check-list { list-style: none; padding: 0; margin: 10px 0 22px; display: grid; gap: 10px; }
        .check-list li { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 12px 16px; }
        .check-list li strong { color: var(--text-main); }
        .rule-cards, .cereal-cards, .recipe-cards { display: grid; gap: 14px; margin: 12px 0 24px;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
        .rule-card { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 16px 18px; }
        .rule-card .rule-num { font-size: 1.6rem; font-weight: 900; color: var(--primary); line-height: 1.2; }
        .rule-card h3 { margin: 4px 0 6px; }
        .rule-card p { color: var(--text-muted); margin: 0; font-size: 0.95rem; }
        .tier-title { display: flex; align-items: center; gap: 10px; font-size: 1.15rem; font-weight: 900; margin: 22px 0 6px; }
        .tier-dot { width: 14px; height: 14px; border-radius: 50%; flex-shrink: 0; }
        .tier-gold .tier-dot { background: #10b981; } .tier-ok .tier-dot { background: #f39c12; } .tier-avoid .tier-dot { background: #e74c3c; }
        .cereal-card { background: var(--bg-input); border: 1px solid var(--border-color); border-top: 4px solid #10b981;
            border-radius: var(--radius-md); padding: 16px 18px; display: flex; flex-direction: column; gap: 8px; }
        .cereal-card.ok { border-top-color: #f39c12; } .cereal-card.avoid { border-top-color: #e74c3c; }
        .cereal-card h3 { margin: 0; }
        .cereal-card p { color: var(--text-muted); margin: 0; font-size: 0.95rem; }
        .chip-row { display: flex; flex-wrap: wrap; gap: 6px; }
        .chip { padding: 4px 10px; border-radius: 999px; font-size: 0.8rem; font-weight: 700; background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.25); color: var(--text-main); }
        .chip.hi { background: rgba(231, 76, 60, 0.1); border-color: rgba(231, 76, 60, 0.35); }
        .chip.mid { background: rgba(243, 156, 18, 0.12); border-color: rgba(243, 156, 18, 0.4); }
        .card-link { color: var(--primary); font-weight: 800; text-decoration: none; font-size: 0.9rem; margin-top: auto; }
        .card-link:hover { text-decoration: underline; }
        .steps { margin: 10px 0 22px; padding: 0; list-style: none; counter-reset: step; display: grid; gap: 10px; }
        .steps li { counter-increment: step; background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-sm);
            padding: 12px 16px 12px 16px; position: relative; padding-inline-start: 52px; }
        .steps li::before { content: counter(step); position: absolute; inset-inline-start: 14px; top: 12px; width: 26px; height: 26px;
            border-radius: 50%; background: var(--primary); color: #fff; font-weight: 900; display: flex; align-items: center; justify-content: center; font-size: 0.85rem; }
        .allergy-box { border: 2px solid #f39c12; background: rgba(243, 156, 18, 0.08); border-radius: var(--radius-md); padding: 18px 20px; margin: 24px 0; }
        .allergy-box h2 { font-size: 1.15rem; font-weight: 900; margin: 0 0 10px; color: var(--text-main); }
        .allergy-box ul { margin: 0; padding-inline-start: 20px; display: grid; gap: 8px; }
        .allergy-box li { color: var(--text-main); }
        .recipe-card { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 16px 18px; }
        .recipe-card h3 { margin: 0 0 8px; }
        .recipe-card p { color: var(--text-muted); font-size: 0.95rem; margin: 0 0 8px; }
        .recipe-card p:last-child { margin: 0; }
        .ref-list { margin: 10px 0 22px; padding-inline-start: 22px; display: grid; gap: 8px; }
        .ref-list li { color: var(--text-muted); font-size: 0.92rem; overflow-wrap: anywhere; }
        /* Brand watermark in the corner of an in-article photo: <div class="wm-frame"><img ...></div> */
        .wm-frame { position: relative; }
        .wm-frame::after { content: ''; position: absolute; inset-inline-end: 12px; bottom: 12px; width: 40px; height: 40px;
            background: url('/images/brand/wibo-logo-64.webp') center / contain no-repeat; opacity: 0.85;
            filter: drop-shadow(0 1px 3px rgba(0, 0, 0, 0.45)); pointer-events: none; }
        .article-page p a, .article-page .check-list a, .article-page .steps a { color: var(--primary); font-weight: 700; text-decoration: none; }
        .article-page p a:hover, .article-page .check-list a:hover, .article-page .steps a:hover { text-decoration: underline; }
        .rule-card bdi { white-space: nowrap; }
        .rule-num small { font-size: 0.8rem; font-weight: 700; color: var(--text-muted); }
        .article-byline { font-weight: 700; margin: 0 0 10px; color: var(--text-main); }
        .article-byline i { color: var(--primary); }
        .article-byline a { color: inherit; text-decoration: none; }
        .article-byline a:hover { color: var(--primary); }
        .draft-chip { padding: 3px 10px; border-radius: 999px; font-size: 0.8rem; font-weight: 800; background: rgba(243, 156, 18, 0.12);
            border: 1px solid rgba(243, 156, 18, 0.4); color: var(--text-main); }
        .hub-cards { display: grid; gap: 16px; margin: 16px 0 26px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
        .hub-card { background: var(--bg-input); border: 1px solid var(--border-color); border-top: 4px solid var(--primary);
            border-radius: var(--radius-md); padding: 18px; display: flex; flex-direction: column; gap: 8px; text-decoration: none; color: inherit; }
        .hub-card:hover { border-color: var(--primary); }
        .hub-card h3 { margin: 0; }
        .hub-card p { color: var(--text-muted); margin: 0; font-size: 0.95rem; }
        /* card with a thumbnail: photo beside the text, stacked above it on phones */
        .hub-card.has-thumb { flex-direction: row; align-items: center; gap: 20px; grid-column: 1 / -1; }   /* one full-width row each */
        .hub-thumb { flex: 0 0 clamp(180px, 34%, 300px); aspect-ratio: 16 / 10; border-radius: var(--radius-sm); overflow: hidden; background: var(--border-color); }
        .hub-thumb img { display: block; width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease; }
        .hub-card.has-thumb:hover .hub-thumb img { transform: scale(1.03); }
        .hub-card-body { display: flex; flex-direction: column; gap: 8px; min-width: 0; }
        .hub-card-body .group-chip { align-self: flex-start; }
        @media (max-width: 640px) {
            .hub-card.has-thumb { flex-direction: column; align-items: stretch; gap: 14px; }
            .hub-thumb { flex-basis: auto; width: 100%; }
        }
        @media (max-width: 640px) { .article-page h1 { font-size: 1.55rem; } }
"""


def section_dir(a):
    return SECTIONS[a['section']]['dir'] if a.get('section') else 'articles'


def is_draft(a):
    return bool(a.get('draft') or (a.get('section') and SECTIONS[a['section']].get('draft')))


def page_url(a, lang, absolute=True):
    folder = section_dir(a)
    if lang in a.get('legacy', {}):                     # the older hand-written page this article is a translation of
        path = a['legacy'][lang]
    else:
        path = f'/{folder}/{a["slugs"][lang]}.html' if lang == 'ar' else f'/{lang}/{folder}/{a["slugs"][lang]}.html'
    return SITE + path if absolute else path


def hub_url(sec, lang, absolute=True):
    path = f'/{sec["dir"]}.html' if lang == 'ar' else f'/{lang}/{sec["dir"]}.html'
    return SITE + path if absolute else path


def food_url(slug, lang):
    lang = 'en' if lang == SV else lang      # no Swedish food pages yet: the English one
    return f'/foods/{slug}.html' if lang == 'ar' else f'/{lang}/foods/{slug}.html'


def date_text(iso, lang):
    y, m, d = (int(x) for x in iso.split('-'))
    return f'{d} {T[lang]["months"][m - 1]} {y}'


def render_body(html, lang):
    """Content may link foods as {food:slug} and site pages as {site:/path}; resolve them for the language."""
    html = re.sub(r'\{food:([a-z0-9-]+)\}', lambda m: food_url(m.group(1), lang), html)
    return re.sub(r'\{site:([^}]+)\}', lambda m: link(m.group(1), lang), html)


def shell(lang, *, title, desc, urls, schema, main, draft, og_type='website', image=None, image_alt='', extra_head='',
          active='/#articles', switch=None):
    """Full page around `main`: head and SEO tags, header with language links (to `urls`, one per language the page
    exists in; `switch` may add ?lang links that are not hreflang alternates) and footer; shared by articles and hubs."""
    t, u = T[lang], ui(lang)
    nav_links = nav(lang, active=active)
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{(switch or urls)[l][len(SITE):]}" '
        f'hreflang="{l}" lang="{l}" title="{name}" aria-label="{name}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag, name in (('ar', '🇪🇬', 'العربية'), ('nl', '🇳🇱', 'Nederlands'), ('en', '🇬🇧', 'English'), (SV, '🇸🇪', 'Svenska'))
        if l in (switch or urls))
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in ALL_LANGS if l in urls)
    items = [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/#articles', t['footer_articles']),
             ('/methodology.html', u['methodology']), ('/partners.html', u['partners']), ('/privacy.html', u['privacy'])]
    if lang == SV:                                       # the Swedish about, contact and legal pages
        items = [('/', u['nav'][0]), ('/#articles', t['footer_articles']), ('/about.html', 'Om oss'),
                 ('/contact.html', 'Kontakt'), ('/privacy.html', 'Integritetspolicy'), ('/terms.html', 'Användarvillkor'),
                 ('/sv/medicinsk-ansvarsfriskrivning.html', 'Medicinsk ansvarsfriskrivning'), ('/partners.html', u['partners'])]
    footer_links = ' <span>•</span> '.join(f'<a href="{link(p, lang)}">{label}</a>' for p, label in items)
    x_default = f'\n    <link rel="alternate" hreflang="x-default" href="{urls["ar"]}">' if 'ar' in urls else ''
    robots = '\n    <meta name="robots" content="noindex, follow">' if draft else ''
    og_image = (f'\n    <meta property="og:image" content="{image}">\n    <meta property="og:image:alt" content="{esc(image_alt)}">'
                if image else '')

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{t["dir"]}" data-theme="dark">
<head>
{GA_TAG}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">{robots}
    <link rel="canonical" href="{urls[lang]}">
{hreflang}{x_default}
    <meta property="og:type" content="{og_type}">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{urls[lang]}">{og_image}
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL', sv='sv_SE')[lang]}">{extra_head}
    <meta name="twitter:card" content="{'summary_large_image' if image else 'summary'}">
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
    <style>html.theme-transitioning,html.theme-transitioning *,html.theme-transitioning *::before,html.theme-transitioning *::after{{transition:none!important;animation-duration:0s!important}}</style>
    <script>document.addEventListener('click',function(e){{var t=e.target&&e.target.closest&&e.target.closest('.theme-toggle,.theme-toggle-btn,#themeToggle,#themeToggleBtn,#darkModeToggle,[onclick*="toggleTheme"]');if(!t)return;var h=document.documentElement;h.classList.add('theme-transitioning');cancelAnimationFrame(window.__tsw);window.__tsw=requestAnimationFrame(function(){{window.__tsw=requestAnimationFrame(function(){{h.classList.remove('theme-transitioning')}})}})}},true);</script>
    <style>
{BASE_CSS}{PAGE_CSS}{EXTRA_CSS}    </style>
    <link rel="stylesheet" href="/css/unified-header.css">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="{link('/', lang)}" class="brand-link">
                {LOGO_SVG}
                <span class="brand-title">WiBo Health</span>
            </a>
            <nav class="nav-links-bar">
{nav_links}
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

    <main class="page-wrapper food-page article-page">
{main}
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
        try {{ localStorage.setItem('preferred_language', '{lang}'); localStorage.setItem('wibo_language', '{lang}'); }} catch (e) {{}}
    </script>
</body>
</html>
'''


def crumb_parent(a, lang):
    """(name, href) of the breadcrumb level above an article: its section hub, else the homepage article list."""
    if a.get('section'):
        sec = SECTIONS[a['section']]
        return sec['content'][lang]['crumb'], hub_url(sec, lang, absolute=False)
    return T[lang]['section'], link('/#articles', lang)


FAQ_RE = re.compile(r'<div class="faq-item"><h3>(.*?)</h3><p>(.*?)</p></div>', re.S)


def plain(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html)).strip()


def faq_graph(page, body, url):
    """Wrap the page node in an @graph with a FAQPage whose questions are the body's faq-item blocks (one source of truth)."""
    qa = [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}}
          for q, ans in FAQ_RE.findall(body)]
    assert qa, f'faq_schema set but no faq-item blocks in {url}'
    ctx = page.pop('@context')
    faq = {"@type": "FAQPage", "@id": url + '#faq', "url": url, "inLanguage": page['inLanguage'],
           "isPartOf": {"@id": page['@id']}, "mainEntity": qa}
    return {"@context": ctx, "@graph": [page, faq]}


# Named medical author: only for articles with named_author=True (an explicit, per-article exception to the organisation-only
# policy, mirrored in validate_schema.py). Same Person node as the food pages.
DOCTOR = {"@type": "Person", "@id": f"{SITE}/doctor.html#wassim-habib", "name": "Dr. Wassim Habib", "jobTitle": "Medical Doctor",
          "description": "Founder of WiBo Health", "url": f"{SITE}/doctor.html",
          "worksFor": {"@type": "Organization", "name": "WiBo Health", "url": SITE}}
# Swedish pages: the role as approved for Sweden (2026-10-23), no job title that reads as a Swedish licence ("läkare")
DOCTOR_SV = dict(DOCTOR, jobTitle="Grundare och Medicinskt Ansvarig, WiBo Health Group", description="Grundare av WiBo Health")


def build(a, lang):
    t, u, c = T[lang], ui(lang), a['content'][lang]
    urls = {l: page_url(a, l) for l in alt_langs(a)}
    switch = dict(urls)
    if a.get('legacy'):                                  # its EN/NL live on the legacy page via ?lang (not hreflang)
        switch.update({l: SITE + site_link(a['legacy']['ar'], l) for l in LANGS if l not in switch})
    hero = f"{SITE}/images/{a['hero']}" if a.get('hero') else None
    parent_name, parent_href = crumb_parent(a, lang)
    draft = is_draft(a)
    named = c.get('named_author', a.get('named_author'))   # may differ per language (Swedish pages are signed)
    doctor = DOCTOR_SV if lang == SV else DOCTOR
    references = c.get('references', a['references'])   # a language may list its own sources (Swedish: WHO 2013, Socialstyrelsen)

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": c['title'],
        "headline": c['h1'],
        "description": c['desc'],
        "inLanguage": lang,
        "image": {"@type": "ImageObject", "url": hero, "width": a['hero_size'][0], "height": a['hero_size'][1]} if hero else None,
        "datePublished": a['published'],
        "dateModified": a['modified'],
        "lastReviewed": a['modified'],
        "about": [{"@type": "Thing", "name": n} for n in c['about']],
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "author": doctor if named else {"@type": "Organization", "name": "WiBo Health", "url": SITE},
        "reviewedBy": doctor if named else None,
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "citation": [{"@type": "CreativeWork", "name": r} for r in references],
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": parent_name, "item": SITE + parent_href},
            {"@type": "ListItem", "position": 3, "name": c['h1'], "item": urls[lang]}]},
    }
    schema.update(a.get('schema_extra', {}).get(lang, {}))   # article-specific fields (e.g. medical audience)
    schema = {k: v for k, v in schema.items() if v not in (None, [])}
    if a.get('faq_schema'):
        schema = faq_graph(schema, render_body(c['body'], lang), urls[lang])

    refs_html = ''.join(f'<li>{esc(r)}</li>' for r in references)
    refs = (f'''            <h2 class="section-title"><i class="fas fa-book-medical"></i> <span>{t["refs"]}</span></h2>
            <ol class="ref-list">{refs_html}</ol>
''' if refs_html else '')
    hero_cls = 'article-hero-img article-hero-portrait' if a.get('hero_portrait') else 'article-hero-img'
    hero_img = (f'''            <img class="{hero_cls}" src="/images/{a['hero']}" alt="{esc(c["hero_alt"])}" width="{a['hero_size'][0]}" height="{a['hero_size'][1]}" fetchpriority="high" decoding="async">
''' if hero else '')
    draft_chip = f'<span class="draft-chip">{t["draft"]}</span>' if draft else ''
    byline = (f'''
            <p class="article-byline"><i class="fas fa-user-doctor"></i> <a href="{link('/doctor.html', lang)}">{esc(c["byline"])}</a></p>'''
              if named else '')
    published = (t['published_on'] if named else t['published']).format(date=date_text(a['published'], lang))
    main = f'''        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{link('/', lang)}">{u["home"]}</a> › <a href="{parent_href}">{esc(parent_name)}</a> › <span>{esc(c["crumb"])}</span>
            </nav>
            <span class="group-chip">{esc(c["cat"])}</span>
            <h1>{esc(c["h1"])}</h1>{byline}
            <div class="article-meta"><span><i class="fas fa-calendar"></i> {published}</span>{draft_chip}</div>
{hero_img}
{render_body(c["body"], lang)}

{refs}            <p class="disclaimer-box">{c["disclaimer"]}</p>
        </article>'''
    extra_head = f'\n    <meta property="article:published_time" content="{a["published"]}">'
    if hero:
        extra_head += f'\n    <link rel="preload" as="image" href="/images/{a["hero"]}" fetchpriority="high">'
    return shell(lang, title=c['title'], desc=c['desc'], urls=urls, schema=schema, main=main, draft=draft,
                 og_type='article', image=hero, image_alt=c.get('hero_alt', ''), extra_head=extra_head,
                 active=f'/{section_dir(a)}.html' if a.get('section') else '/#articles', switch=switch)


def hub_card(a, lang, t):
    """One article card on a section hub; an article with a `thumb` shows it beside the text (lazy, hero as 2x source)."""
    c = a['content'][lang]
    chip = f'<span class="group-chip">{esc(c["cat"])}</span>'
    text = (f'<h3>{esc(c["h1"])}</h3>', f'<p>{esc(c["summary"])}</p>',
            f'<span class="card-link">{t["soon"] if is_draft(a) else t["read"]}</span>')
    href = page_url(a, lang, absolute=False)
    if not a.get('thumb'):
        return f'                <a class="hub-card" href="{href}">\n' + ''.join(
            f'                    {part}\n' for part in (chip,) + text) + '                </a>'
    (tw, th) = a['thumb_size']
    # 2x source: the hero when it has the card's landscape shape, else a dedicated `thumb_2x` (a portrait hero would be cropped)
    hi, hw = a.get('thumb_2x') or (a['hero'], a['hero_size'][0])
    img = (f'<img src="/images/{a["thumb"]}" srcset="/images/{a["thumb"]} {tw}w, /images/{hi} {hw}w" '
           f'sizes="(max-width: 640px) 92vw, 300px" alt="{esc(c["hero_alt"])}" width="{tw}" height="{th}" loading="lazy" decoding="async">')
    return (f'                <a class="hub-card has-thumb" href="{href}">\n'
            f'                    <div class="hub-thumb">{img}</div>\n'
            f'                    <div class="hub-card-body">\n'
            + ''.join(f'                        {part}\n' for part in (chip,) + text)
            + '                    </div>\n                </a>')


def build_hub(key, lang):
    """Section landing page: intro plus one card per article of the section."""
    sec, t, u = SECTIONS[key], T[lang], ui(lang)
    c = sec['content'][lang]
    urls = {l: hub_url(sec, l) for l in langs_of(sec)}
    members = [a for a in ARTICLES if a.get('section') == key and lang in a['content']]
    cards = '\n'.join(hub_card(a, lang, t) for a in members)
    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": c['title'],
        "description": c['desc'],
        "inLanguage": lang,
        "about": [{"@type": "Thing", "name": n} for n in c['about']],
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "hasPart": [{"@type": "MedicalWebPage", "name": a['content'][lang]['h1'], "url": page_url(a, lang)}
                    for a in members if not is_draft(a)],
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": c['crumb'], "item": urls[lang]}]},
    }
    schema = {k: v for k, v in schema.items() if v not in (None, [])}
    main = f'''        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{link('/', lang)}">{u["home"]}</a> › <span>{esc(c["crumb"])}</span>
            </nav>
            <h1>{esc(c["h1"])}</h1>
            <p class="lead">{c["intro"]}</p>
            <div class="hub-cards">
{cards}
            </div>
            <p class="disclaimer-box">{c["disclaimer"]}</p>
        </article>'''
    return shell(lang, title=c['title'], desc=c['desc'], urls=urls, schema=schema, main=main, draft=sec.get('draft'),
                 active=f'/{sec["dir"]}.html')


def link_legacy_page(legacy_ar, sv):
    """Make a hand-written ?lang page (e.g. /insulin-resistance.html) point at its Swedish version `sv`: hreflang
    ar/sv/x-default after the canonical, an SV link after the EN language button (in the style of that page's switcher)
    and ?lang=sv forwarding in the language boot script. Re-running replaces them."""
    path = ROOT / legacy_ar.lstrip('/')
    raw = path.read_bytes()
    bom, text = raw.startswith(b'\xef\xbb\xbf'), raw.decode('utf-8-sig')
    crlf = '\r\n' in text
    t = text.replace('\r\n', '\n')
    ar = SITE + legacy_ar
    t = re.sub(r'    <!-- SV-ALTERNATES:START.*?<!-- SV-ALTERNATES:END -->\n', '', t, flags=re.S)
    t = re.sub(r'^ *<a class="lang-btn" data-sv-link[^\n]*\n', '', t, flags=re.M)
    t = re.sub(r'^ *if \(q === \'sv\'\)[^\n]*// sv-forward\n', '', t, flags=re.M)
    block = (f'    <!-- SV-ALTERNATES:START (scripts/generate_article_pages.py) -->\n'
             f'    <link rel="alternate" hreflang="ar" href="{ar}">\n'
             f'    <link rel="alternate" hreflang="sv" href="{SITE}{sv}">\n'
             f'    <link rel="alternate" hreflang="x-default" href="{ar}">\n'
             f'    <!-- SV-ALTERNATES:END -->\n')
    t, n1 = re.subn(r'^ *<link rel="canonical"[^>]*>\n', lambda m: m.group(0) + block, t, count=1, flags=re.M)
    def sv_link(m):                                      # same look as the page's own EN button
        inner = m.group(2)
        label = ('<span>🇸🇪</span> <span>SV</span>' if '<span>' in inner else
                 '🇸🇪' if re.fullmatch(r'\s*\S{1,4}\s*', inner) else 'Svenska')
        return (m.group(0) + m.group(1) +
                f'<a class="lang-btn" data-sv-link href="{sv}" hreflang="sv" lang="sv" title="Svenska">{label}</a>\n')
    t, n2 = re.subn(r'^( *)<button\b[^>]*\bclass="lang-btn"[^>]*\bdata-lang(?:-toggle)?="en"[^>]*>(.*?)</button>\n',
                    sv_link, t, count=1, flags=re.M | re.S)
    t, n3 = re.subn(r"^( *)(var q = \(new URLSearchParams\(location\.search\)\.get\('lang'\) \|\| ''\)\.toLowerCase\(\), s = null;\n)",
                    lambda m: m.group(1) + m.group(2) + m.group(1) +
                    f"if (q === 'sv') {{ location.replace('{sv}'); return; }}   // sv-forward\n", t, count=1, flags=re.M)
    assert (n1, n2, n3) == (1, 1, 1), f'{path.name}: canonical/EN button/boot script not found {(n1, n2, n3)}'
    if crlf:
        t = t.replace('\n', '\r\n')
    out = (b'\xef\xbb\xbf' if bom else b'') + t.encode('utf-8')
    if out != raw:
        path.write_bytes(out)


ORG = {"@type": "Organization", "name": "WiBo Health Group", "url": SITE + '/',
       "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}}


def build_site_page(p):
    """A Swedish doctor / about / legal / contact page (scripts/site_pages_sv.py) in the article shell."""
    url = site_page_url(p)
    urls = {'ar': SITE + p['legacy'], SV: url} if p['legacy'] else {SV: url}
    switch = dict(urls)
    if p['legacy']:                                      # EN/NL live on the legacy page via ?lang (not hreflang)
        switch.update({l: SITE + site_link(p['legacy'], l) for l in ('en', 'nl')})
    elif p.get('switch_ar'):                             # a related page that is not an hreflang alternate (e.g. noindex)
        switch['ar'] = SITE + p['switch_ar']
    image = f"{SITE}/images/{p['image']}" if p.get('image') else None
    schema = {
        "@context": "https://schema.org",
        "@type": {'profile': 'ProfilePage', 'about': 'AboutPage', 'contact': 'ContactPage', 'collection': 'CollectionPage'}.get(p['kind'], 'WebPage'),
        "@id": url + '#webpage', "url": url, "name": p['title'], "description": p['desc'], "inLanguage": SV,
        "dateModified": p['modified'],
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "publisher": ORG,
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": UI_SV['home'], "item": SITE + link('/', SV)},
            {"@type": "ListItem", "position": 2, "name": p['crumb'], "item": url}]},
    }
    if p['kind'] == 'profile':
        schema['mainEntity'] = dict(DOCTOR_SV, image=image, url=url)
    elif p['kind'] == 'about':
        schema['about'] = ORG
    elif p['kind'] == 'contact':
        schema['mainEntity'] = dict(ORG, email='support@wibohealth.com', telephone='+31645844585', contactPoint=[{
            "@type": "ContactPoint", "contactType": "customer support", "email": "support@wibohealth.com",
            "telephone": "+31645844585", "availableLanguage": ["Arabic", "Dutch", "English"]}])
    img = (f'''            <img class="article-hero-img article-hero-portrait" src="/images/{p['image']}" alt="{esc(p['image_alt'])}" width="500" height="500" style="max-width:260px;border-radius:50%" decoding="async">
''' if image else '')
    note = f'            <p class="disclaimer-box">{p["footer_note"]}</p>\n' if p.get('footer_note') else ''
    main = f'''        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{link('/', SV)}">{UI_SV["home"]}</a> › <span>{esc(p["crumb"])}</span>
            </nav>
            <h1>{esc(p["h1"])}</h1>
{img}{p["body"]}{note}        </article>'''
    return shell(SV, title=p['title'], desc=p['desc'], urls=urls, schema=schema, main=main, draft=False,
                 og_type='profile' if p['kind'] == 'profile' else 'website', image=image,
                 image_alt=p.get('image_alt', ''), active=None, switch=switch)


def lang_dir(lang, folder=''):
    return ROOT / (folder if lang == 'ar' else f'{lang}/{folder}'.rstrip('/'))


def main():
    folders = {'articles'} | {s['dir'] for s in SECTIONS.values()}
    for lang in ALL_LANGS:
        mine = [a for a in ARTICLES if lang in langs_of(a)]
        for folder in folders:
            out_dir = lang_dir(lang, folder)
            keep = {f'{a["slugs"][lang]}.html' for a in mine if section_dir(a) == folder}
            if not keep and not out_dir.exists():       # no empty sv/articles folder
                continue
            out_dir.mkdir(parents=True, exist_ok=True)
            for old in out_dir.glob('*.html'):          # an article that was removed must not linger
                if old.name not in keep:
                    old.unlink()
        for a in mine:
            (lang_dir(lang, section_dir(a)) / f'{a["slugs"][lang]}.html').write_text(build(a, lang), encoding='utf-8', newline='\n')
        for key, sec in SECTIONS.items():               # a hub sits next to its folder: diabetes.html + diabetes/
            if lang in langs_of(sec):
                (lang_dir(lang) / f'{sec["dir"]}.html').write_text(build_hub(key, lang), encoding='utf-8', newline='\n')

    for a in ARTICLES:
        if a.get('legacy') and SV in a['content'] and not is_draft(a):
            link_legacy_page(a['legacy']['ar'], page_url(a, SV, absolute=False))
    for p in SITE_PAGES_SV:                              # Swedish doctor, about, legal and contact pages
        (ROOT / 'sv' / f'{p["slug"]}.html').write_text(build_site_page(p), encoding='utf-8', newline='\n')
        if p['legacy']:
            link_legacy_page(p['legacy'], site_page_url(p, absolute=False))

    # drafts (articles or whole sections) stay out of the sitemap until they are published
    entries = [(lambda l, sec=sec: hub_url(sec, l), max((a['modified'] for a in ARTICLES if a.get('section') == k), default=None), None,
                langs_of(sec)) for k, sec in SECTIONS.items() if not sec.get('draft')]
    entries += [(lambda l, a=a: page_url(a, l), a['modified'], a.get('hero'), alt_langs(a)) for a in ARTICLES if not is_draft(a)]
    entries += [(lambda l, p=p: SITE + p['legacy'] if l == 'ar' else site_page_url(p), p['modified'], None,
                 ('ar', SV) if p['legacy'] else (SV,)) for p in SITE_PAGES_SV]

    image_ns = 'xmlns:image' in (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
    block = []
    for url_of, modified, hero, langs in entries:
        for lang in langs:
            block += ['  <url>', f'    <loc>{url_of(lang)}</loc>']
            block += [f'    <lastmod>{modified}</lastmod>'] if modified else []
            block += ['    <changefreq>monthly</changefreq>', '    <priority>0.8</priority>']
            if hero and image_ns:
                block.append(f'    <image:image><image:loc>{SITE}/images/{hero}</image:loc></image:image>')
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{url_of(l)}"/>' for l in langs]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url_of("ar")}"/>'] if 'ar' in langs else []
            block += ['  </url>']
    replace_sitemap_block('ARTICLE-PAGES', block)
    sitemap = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
    for a in ARTICLES:                                   # a legacy page now lives in this block: no second hand-written entry
        if a.get('legacy') and not is_draft(a):
            loc = f'<loc>{page_url(a, "ar")}</loc>'
            assert sitemap.count(loc) == 1, f'{loc} appears {sitemap.count(loc)} times in sitemap.xml: remove the hand-written entry'
    for p in SITE_PAGES_SV:
        if p['legacy']:
            loc = f'<loc>{SITE}{p["legacy"]}</loc>'
            assert sitemap.count(loc) == 1, f'{loc} appears {sitemap.count(loc)} times in sitemap.xml: remove the hand-written entry'
    drafts = sum(is_draft(a) for a in ARTICLES)
    print(f'article pages written: {sum(len(langs_of(a)) for a in ARTICLES)} ({len(ARTICLES)} articles, '
          f'{sum(SV in langs_of(a) for a in ARTICLES)} with Swedish, {drafts} draft); '
          f'section hubs: {sum(len(langs_of(s)) for s in SECTIONS.values())}')


if __name__ == '__main__':
    main()
