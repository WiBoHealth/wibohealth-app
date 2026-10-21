"""Generate static, crawlable supplement pages in three languages.

    python scripts/generate_supplement_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    supplements/<slug>.html       Arabic (x-default)
    en/supplements/<slug>.html    English
    nl/supplements/<slug>.html    Dutch
    js/supplement-pages.js        slugs that have a static page (used by the supplements.html modal)
    sitemap.xml                   block between <!-- SUPPLEMENT-PAGES:START --> and <!-- SUPPLEMENT-PAGES:END -->

Source: js/supplements-data.js. Only records that carry `references` (the clinically vetted ones) get a page.
Content is attributed to the published sources (EFSA / NIH / PubMed), never to a named reviewer, and uses
structure/function wording only. Design system, header and footer come from generate_food_pages.py.
"""
import json
import re
from pathlib import Path

from generate_food_pages import BASE_CSS, LOGO_SVG, PAGE_CSS, SITE, LANGS, UI, esc, nav_html, site_link

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
    <script src="/js/consent.js?v=1" defer></script>"""   # GA4 property of wibohealth.com, first thing in every <head>


ROOT = Path(__file__).resolve().parent.parent

T = {
    'ar': dict(
        dir='rtl', title='{name}: الجرعة والفوائد والتداخلات الدوائية | WiBo Health',
        desc='{name}: {desc} الجرعة الموصى بها: {dose}. التحذيرات والتداخلات الدوائية وفق EFSA وNIH.',
        guide='دليل المكملات', role='الدور الوظيفي والفوائد', dose='الجرعة وطريقة الاستخدام',
        rec='الجرعة الموصى بها', forms='أفضل الأشكال المتوفرة', timing='أفضل وقت للاستخدام', freq='التكرار', warnings='تحذيرات مهمة',
        inter='التداخلات الدوائية', refs='المراجع العلمية', related='مكملات ذات صلة', open_guide='عرض في دليل المكملات',
        sources='📚 المصادر والأبحاث المنشورة: الهيئة الأوروبية لسلامة الأغذية (EFSA) • المعاهد الوطنية للصحة (NIH - ODS) • قواعد بيانات PubMed / Cochrane',
        updated='آخر تحديث للمحتوى: {date} · المحتوى مستند إلى المصادر والأبحاث المنشورة (EFSA / NIH / PubMed)',
        disclaimer='⚖️ إخلاء مسؤولية طبي: المعلومات والبيانات الواردة هنا هي لأغراض التثقيف الصحي والإرشاد الغذائي فقط، ولا تُعتبر تشخيصاً طبياً ولا تُغني بأي حال عن الاستشارة الطبية المباشرة من طبيبك أو الصيدلي. استشر طبيبك دائماً قبل البدء بأي مكمل، خصوصاً في حالات الحمل والرضاعة أو عند استخدام أدوية مزمنة.',
        date='17 أكتوبر 2026', footer_supp='دليل المكملات'),
    'en': dict(
        dir='ltr', title='{name}: Dosage, Benefits & Drug Interactions | WiBo Health',
        desc='{name}: {desc} Recommended dose: {dose}. Warnings and drug interactions based on EFSA and NIH.',
        guide='Supplements Guide', role='Function & benefits', dose='Dosage & how to use',
        rec='Recommended dose', forms='Best forms to choose', timing='Best time to take', freq='Frequency', warnings='Important warnings',
        inter='Drug interactions', refs='Scientific references', related='Related supplements', open_guide='View in the supplements guide',
        sources='📚 Published sources and research: European Food Safety Authority (EFSA) • National Institutes of Health (NIH - ODS) • PubMed / Cochrane databases',
        updated='Content last updated: {date} · Based on published sources and research (EFSA / NIH / PubMed)',
        disclaimer='⚖️ Medical disclaimer: The information and data provided here are for health education and nutritional guidance only. They are not a medical diagnosis and never replace a direct consultation with your doctor or pharmacist. Always consult your doctor before starting any supplement, especially during pregnancy or breastfeeding or when taking long-term medication.',
        date='17 October 2026', footer_supp='Supplements Guide'),
    'nl': dict(
        dir='ltr', title='{name}: dosering, voordelen en interacties | WiBo Health',
        desc='{name}: {desc} Aanbevolen dosis: {dose}. Waarschuwingen en interacties met medicijnen volgens EFSA en NIH.',
        guide='Supplementengids', role='Functie & voordelen', dose='Dosering & gebruik',
        rec='Aanbevolen dosis', forms='Beste vormen om te kiezen', timing='Beste moment van inname', freq='Frequentie', warnings='Belangrijke waarschuwingen',
        inter='Interacties met medicijnen', refs='Wetenschappelijke bronnen', related='Verwante supplementen', open_guide='Bekijk in de supplementengids',
        sources='📚 Gepubliceerde bronnen en onderzoek: Europese Autoriteit voor Voedselveiligheid (EFSA) • National Institutes of Health (NIH - ODS) • PubMed / Cochrane-databanken',
        updated='Inhoud laatst bijgewerkt: {date} · Gebaseerd op gepubliceerde bronnen en onderzoek (EFSA / NIH / PubMed)',
        disclaimer='⚖️ Medische disclaimer: De informatie en gegevens hier zijn uitsluitend bedoeld voor gezondheidsvoorlichting en voedingsadvies. Ze vormen geen medische diagnose en vervangen nooit een direct consult bij je behandelend arts of apotheker. Overleg altijd met je arts voordat je met een supplement begint, vooral tijdens zwangerschap of borstvoeding of bij langdurig medicijngebruik.',
        date='17 oktober 2026', footer_supp='Supplementengids'),
}
SUF = {'ar': '', 'en': 'En', 'nl': 'Nl'}
NAME = {'ar': 'name', 'en': 'englishName', 'nl': 'nameNl'}

EXTRA_CSS = """
        .dose-table td:first-child { color: var(--text-muted); font-weight: 700; width: 38%; }
        .ref-list { margin: 10px 0 22px; padding-inline-start: 22px; display: grid; gap: 8px; }
        .ref-list li { color: var(--text-muted); font-size: 0.92rem; overflow-wrap: anywhere; }
        .guide-link { display: inline-flex; align-items: center; gap: 8px; margin: 4px 0 22px; padding: 10px 18px; border-radius: 30px;
            border: 1px solid var(--primary); color: var(--primary); font-weight: 800; text-decoration: none; }
        .guide-link:hover { background: var(--primary-glow); }
"""


def load_supplements():
    text = (ROOT / 'js' / 'supplements-data.js').read_text(encoding='utf-8')
    array = text[text.index('const supplementsData = ') + len('const supplementsData = '):text.rindex('];') + 1]
    # the file is written as JSON with unquoted keys (see the clean-up scripts): quote them back
    return json.loads(re.sub(r'^(\s*)([A-Za-z_]\w*): ', r'\1"\2": ', array, flags=re.M))


def page_url(slug, lang, absolute=True):
    path = f'/supplements/{slug}.html' if lang == 'ar' else f'/{lang}/supplements/{slug}.html'
    return SITE + path if absolute else path


def clip(text, limit):
    text = ' '.join(text.split())
    return text if len(text) <= limit else text[:limit].rsplit(' ', 1)[0].rstrip('،,;؛.') + '…'


def build(s, lang, vetted):
    t, u, suf = T[lang], UI[lang], SUF[lang]
    name = s[NAME[lang]] or s['name']
    subtitle = s['englishName'] if lang != 'en' and s['englishName'] != name else ''
    desc_txt = s['summary' + suf]
    dose = s['dosage' + suf]
    title = t['title'].format(name=name)
    meta_desc = clip(t['desc'].format(name=name, desc=clip(desc_txt, 90), dose=dose['recommended']), 300)
    urls = {l: page_url(s['slug'], l) for l in LANGS}
    guide_href = site_link('/supplements.html', lang) + '#' + s['slug']

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": title,
        "description": meta_desc,
        "inLanguage": lang,
        "about": {"@type": "Thing", "name": s['englishName'], "alternateName": [s['name'], s['nameNl']]},
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "author": {"@type": "Organization", "name": "WiBo Health", "url": SITE},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "citation": [{"@type": "CreativeWork", "name": r} for r in s['references']],
        "lastReviewed": s.get('reviewed', '2026-10-17'),
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + site_link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": t['guide'], "item": SITE + site_link('/supplements.html', lang)},
            {"@type": "ListItem", "position": 3, "name": name, "item": urls[lang]}]},
    }

    group = s['groupLabel'][lang]
    related = [r for r in vetted if r['id'] != s['id'] and r['groupLabel']['ar'] == s['groupLabel']['ar']]
    related += [r for r in vetted if r['id'] != s['id'] and r not in related and r['category'] == s['category']]
    related_html = ''.join(
        f'<li><a href="{page_url(r["slug"], lang, absolute=False)}">{esc(r[NAME[lang]] or r["name"])}'
        f'<span>{esc(r["groupLabel"][lang])}</span></a></li>' for r in related[:4])

    nav = nav_html(lang, active='/supplements.html')
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(s["slug"], l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧')))
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in LANGS)
    warnings_html = ''.join(f'<div class="tip warn"><p>{esc(w)}</p></div>' for w in s['warnings' + suf])
    refs_html = ''.join(f'<li>{esc(r)}</li>' for r in s['references'])
    forms_txt = s.get('forms' + suf)
    forms_html = (f'<h2 class="section-title"><i class="fas fa-capsules"></i> <span>{t["forms"]}</span></h2>'
                  f'<div class="tip-list"><div class="tip"><p>{esc(forms_txt)}</p></div></div>') if forms_txt else ''
    footer_links = ' <span>•</span> '.join(
        f'<a href="{site_link(p, lang)}">{label}</a>' for p, label in
        [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/supplements.html', t['footer_supp']),
         ('/methodology.html', u['methodology']), ('/partners.html', u['partners']), ('/privacy.html', u['privacy'])])

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{t["dir"]}" data-theme="dark">
<head>
{GA_TAG}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(meta_desc)}">
    <link rel="canonical" href="{urls[lang]}">
{hreflang}
    <link rel="alternate" hreflang="x-default" href="{urls['ar']}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(meta_desc)}">
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

    <main class="page-wrapper food-page supplement-page">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{site_link('/', lang)}">{u["home"]}</a> › <a href="{site_link('/supplements.html', lang)}">{t["guide"]}</a> › <span>{esc(name)}</span>
            </nav>

            <div class="food-hero">
                <div class="food-emoji" aria-hidden="true">{s.get("icon") or "💊"}</div>
                <div class="food-hero-text">
                    <h1>{esc(name)}</h1>
                    {f'<div class="food-subtitle">{esc(subtitle)}</div>' if subtitle else ''}
                    <span class="group-chip">{esc(group)}</span>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-star"></i> <span>{t["role"]}</span></h2>
            <p class="lead">{esc(desc_txt)}</p>

            <h2 class="section-title"><i class="fas fa-prescription-bottle"></i> <span>{t["dose"]}</span></h2>
            <table class="nutrition-table dose-table">
                <tbody>
                    <tr><td>{t["rec"]}</td><td>{esc(dose["recommended"])}</td></tr>
                    <tr><td>{t["timing"]}</td><td>{esc(dose["timing"])}</td></tr>
                    <tr><td>{t["freq"]}</td><td>{esc(dose["frequency"])}</td></tr>
                </tbody>
            </table>

            {forms_html}
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>{t["warnings"]}</span></h2>
            <div class="tip-list">{warnings_html}</div>

            <h2 class="section-title"><i class="fas fa-pills"></i> <span>{t["inter"]}</span></h2>
            <div class="tip-list"><div class="tip"><p>{esc(s["interactions" + suf])}</p></div></div>

            <a class="guide-link" href="{guide_href}"><i class="fas fa-capsules"></i> {t["open_guide"]}</a>
            {f'<h2 class="section-title"><i class="fas fa-layer-group"></i> <span>{t["related"]}</span></h2><ul class="alt-list">{related_html}</ul>' if related_html else ''}

            <h2 class="section-title"><i class="fas fa-book-medical"></i> <span>{t["refs"]}</span></h2>
            <ol class="ref-list">{refs_html}</ol>

            <div class="source-strip">{t["sources"]}</div>
            <p class="reviewed">{t["updated"].format(date=t["date"])}</p>
            <p class="disclaimer-box">{t["disclaimer"]}</p>
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
    vetted = [s for s in load_supplements() if s.get('references')]
    for lang in LANGS:
        out_dir = ROOT / ('supplements' if lang == 'ar' else f'{lang}/supplements')
        out_dir.mkdir(parents=True, exist_ok=True)
        keep = {f'{s["slug"]}.html' for s in vetted}
        for old in out_dir.glob('*.html'):          # a supplement that lost its page must not linger
            if old.name not in keep:
                old.unlink()
        for s in vetted:
            (out_dir / f'{s["slug"]}.html').write_text(build(s, lang, vetted), encoding='utf-8', newline='\n')

    (ROOT / 'js' / 'supplement-pages.js').write_text(
        '// Generated by scripts/generate_supplement_pages.py - do not edit by hand.\n'
        '// Slugs of supplements that have a static page (/supplements/<slug>.html, /en/supplements/..., /nl/supplements/...).\n'
        f'window.SUPP_PAGES = {json.dumps({s["slug"]: 1 for s in vetted}, separators=(",", ":"))};\n',
        encoding='utf-8', newline='\n')

    sm_path = ROOT / 'sitemap.xml'
    sm = sm_path.read_text(encoding='utf-8')
    eol = '\r\n' if '\r\n' in sm else '\n'
    sm = re.sub(r'\s*<!-- SUPPLEMENT-PAGES:START -->.*?<!-- SUPPLEMENT-PAGES:END -->', '', sm, flags=re.S)
    block = ['  <!-- SUPPLEMENT-PAGES:START -->']
    for s in vetted:
        for lang in LANGS:
            block += ['  <url>', f'    <loc>{page_url(s["slug"], lang)}</loc>', f'    <lastmod>{s.get("reviewed", "2026-10-17")}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.6</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(s["slug"], l)}"/>' for l in LANGS]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(s["slug"], "ar")}"/>', '  </url>']
    block.append('  <!-- SUPPLEMENT-PAGES:END -->')
    sm = sm.replace('</urlset>', eol.join(block) + eol + '</urlset>', 1)
    sm_path.write_text(sm, encoding='utf-8', newline='')
    print(f'supplement pages written: {len(vetted) * len(LANGS)} ({len(vetted)} supplements x {len(LANGS)} languages)')


if __name__ == '__main__':
    main()
