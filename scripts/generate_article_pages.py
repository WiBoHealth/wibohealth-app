"""Generate static, crawlable article pages in three languages.

    python scripts/generate_article_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    articles/<slug>.html       Arabic (x-default)
    en/articles/<slug>.html    English
    nl/articles/<slug>.html    Dutch
    sitemap.xml                block between <!-- ARTICLE-PAGES:START --> and <!-- ARTICLE-PAGES:END -->

Source: scripts/article_content.py. Editorial policy: the author and publisher are the WiBo Health organization,
never a named person; structure/function wording only. Design system, header and footer come from
generate_food_pages.py, so the pages match the food and supplement pages.
"""
import json
import re
from pathlib import Path

from article_content import ARTICLES
from generate_food_pages import BASE_CSS, LOGO_SVG, PAGE_CSS, SITE, LANGS, UI, esc, site_link

ROOT = Path(__file__).resolve().parent.parent

T = {
    'ar': dict(dir='rtl', section='المقالات الصحية', minutes='دقائق قراءة', published='نُشر في {date} · فريق WiBo Health',
               date='17 أكتوبر 2026', refs='المصادر العلمية', footer_articles='المقالات'),
    'en': dict(dir='ltr', section='Health articles', minutes='min read', published='Published {date} · WiBo Health team',
               date='17 October 2026', refs='Scientific sources', footer_articles='Articles'),
    'nl': dict(dir='ltr', section='Gezondheidsartikelen', minutes='min leestijd', published='Gepubliceerd op {date} · WiBo Health-team',
               date='17 oktober 2026', refs='Wetenschappelijke bronnen', footer_articles='Artikelen'),
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
        .article-meta { display: flex; flex-wrap: wrap; gap: 10px 16px; align-items: center; color: var(--text-muted); font-size: 0.88rem;
            font-weight: 600; margin-bottom: 18px; }
        .article-page h1 { font-size: 2rem; font-weight: 900; line-height: 1.35; margin-bottom: 10px; }
        .article-page p { margin: 0 0 14px; }
        .article-page h3 { font-size: 1.1rem; font-weight: 800; margin: 18px 0 8px; }
        .article-figure { margin: 18px 0 22px; }
        .article-figure img { width: 100%; height: auto; border-radius: var(--radius-md); display: block; box-shadow: var(--shadow); }
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
        @media (max-width: 640px) { .article-page h1 { font-size: 1.55rem; } }
"""


def page_url(slugs, lang, absolute=True):
    path = f'/articles/{slugs[lang]}.html' if lang == 'ar' else f'/{lang}/articles/{slugs[lang]}.html'
    return SITE + path if absolute else path


def food_url(slug, lang):
    return f'/foods/{slug}.html' if lang == 'ar' else f'/{lang}/foods/{slug}.html'


def render_body(html, lang):
    """Content may link foods as {food:slug} and site pages as {site:/path}; resolve them for the language."""
    html = re.sub(r'\{food:([a-z0-9-]+)\}', lambda m: food_url(m.group(1), lang), html)
    return re.sub(r'\{site:([^}]+)\}', lambda m: site_link(m.group(1), lang), html)


def build(a, lang):
    t, u, c = T[lang], UI[lang], a['content'][lang]
    urls = {l: page_url(a['slugs'], l) for l in LANGS}
    hero = f"{SITE}/images/{a['hero']}"

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": c['title'],
        "headline": c['h1'],
        "description": c['desc'],
        "inLanguage": lang,
        "image": {"@type": "ImageObject", "url": hero, "width": a['hero_size'][0], "height": a['hero_size'][1]},
        "datePublished": a['published'],
        "dateModified": a['modified'],
        "lastReviewed": a['modified'],
        "about": [{"@type": "Thing", "name": n} for n in c['about']],
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "author": {"@type": "Organization", "name": "WiBo Health", "url": SITE},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "citation": [{"@type": "CreativeWork", "name": r} for r in a['references']],
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + site_link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": t['section'], "item": SITE + site_link('/#articles', lang)},
            {"@type": "ListItem", "position": 3, "name": c['h1'], "item": urls[lang]}]},
    }

    nav_paths = ['/', '/foods.html', '/calculators.html', '/supplements.html', '/#articles', '/boodi.html']
    nav = '\n'.join(f'                <a href="{site_link(p, lang)}" class="nav-link{" active" if p == "/#articles" else ""}">{label}</a>'
                    for p, label in zip(nav_paths, u['nav']))
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(a["slugs"], l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧')))
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in LANGS)
    refs_html = ''.join(f'<li>{esc(r)}</li>' for r in a['references'])
    footer_links = ' <span>•</span> '.join(
        f'<a href="{site_link(p, lang)}">{label}</a>' for p, label in
        [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/#articles', t['footer_articles']),
         ('/methodology.html', u['methodology']), ('/privacy.html', u['privacy'])])

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{t["dir"]}" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(c["title"])}</title>
    <meta name="description" content="{esc(c["desc"])}">
    <link rel="canonical" href="{urls[lang]}">
{hreflang}
    <link rel="alternate" hreflang="x-default" href="{urls['ar']}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{esc(c["title"])}">
    <meta property="og:description" content="{esc(c["desc"])}">
    <meta property="og:url" content="{urls[lang]}">
    <meta property="og:image" content="{hero}">
    <meta property="og:image:alt" content="{esc(c["hero_alt"])}">
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL')[lang]}">
    <meta property="article:published_time" content="{a['published']}">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=4)}
    </script>
    <link rel="preload" as="image" href="/images/{a['hero']}" fetchpriority="high">
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

    <main class="page-wrapper food-page article-page">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{site_link('/', lang)}">{u["home"]}</a> › <a href="{site_link('/#articles', lang)}">{t["section"]}</a> › <span>{esc(c["crumb"])}</span>
            </nav>
            <span class="group-chip">{esc(c["cat"])}</span>
            <h1>{esc(c["h1"])}</h1>
            <div class="article-meta"><span><i class="fas fa-clock"></i> {a["minutes"]} {t["minutes"]}</span><span>{t["published"].format(date=t["date"])}</span></div>
            <img class="article-hero-img" src="/images/{a['hero']}" alt="{esc(c["hero_alt"])}" width="{a['hero_size'][0]}" height="{a['hero_size'][1]}" fetchpriority="high" decoding="async">

{render_body(c["body"], lang)}

            <h2 class="section-title"><i class="fas fa-book-medical"></i> <span>{t["refs"]}</span></h2>
            <ol class="ref-list">{refs_html}</ol>
            <p class="disclaimer-box">{c["disclaimer"]}</p>
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
        try {{ localStorage.setItem('preferred_language', '{lang}'); localStorage.setItem('wibo_language', '{lang}'); }} catch (e) {{}}
    </script>
</body>
</html>
'''


def main():
    for lang in LANGS:
        out_dir = ROOT / ('articles' if lang == 'ar' else f'{lang}/articles')
        out_dir.mkdir(parents=True, exist_ok=True)
        keep = {f'{a["slugs"][lang]}.html' for a in ARTICLES}
        for old in out_dir.glob('*.html'):          # an article that was removed must not linger
            if old.name not in keep:
                old.unlink()
        for a in ARTICLES:
            (out_dir / f'{a["slugs"][lang]}.html').write_text(build(a, lang), encoding='utf-8', newline='\n')

    sm_path = ROOT / 'sitemap.xml'
    sm = sm_path.read_text(encoding='utf-8')
    eol = '\r\n' if '\r\n' in sm else '\n'
    sm = re.sub(r'\s*<!-- ARTICLE-PAGES:START -->.*?<!-- ARTICLE-PAGES:END -->', '', sm, flags=re.S)
    block = ['  <!-- ARTICLE-PAGES:START -->']
    for a in ARTICLES:
        for lang in LANGS:
            block += ['  <url>', f'    <loc>{page_url(a["slugs"], lang)}</loc>', f'    <lastmod>{a["modified"]}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.8</priority>',
                      f'    <image:image><image:loc>{SITE}/images/{a["hero"]}</image:loc></image:image>' if 'xmlns:image' in sm else None]
            block = [b for b in block if b is not None]
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(a["slugs"], l)}"/>' for l in LANGS]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(a["slugs"], "ar")}"/>', '  </url>']
    block.append('  <!-- ARTICLE-PAGES:END -->')
    sm = sm.replace('</urlset>', eol.join(block) + eol + '</urlset>', 1)
    sm_path.write_text(sm, encoding='utf-8', newline='')
    print(f'article pages written: {len(ARTICLES) * len(LANGS)} ({len(ARTICLES)} articles x {len(LANGS)} languages)')


if __name__ == '__main__':
    main()
