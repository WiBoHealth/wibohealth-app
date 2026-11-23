"""Generate the standalone calculator pages (one page per calculator, three languages plus Swedish).

    python scripts/generate_calculator_pages.py

Output (re-running rebuilds everything):
    <slug>.html        Arabic (x-default), e.g. bmi-calculator.html
    en/<slug>.html     English
    nl/<slug>.html     Dutch
    sv/<slug>.html     Swedish (copy in calc_sv.py; links use generate_article_pages.link, so pages without a Swedish
                       version open in English)
    sitemap-pages.xml  block between <!-- CALCULATOR-PAGES:START --> and <!-- CALCULATOR-PAGES:END -->

Source: scripts/calculator_content.py. Each page = a working calculator + a long-form clinical guide + FAQ.
Editorial policy as for the articles: author and publisher are the WiBo Health organisation, never a named person.
Design system, header and footer come from generate_food_pages.py / generate_article_pages.py, and the olive dark
theme comes from css/unified-header.css, so these pages match the rest of the site.
vercel.json must exempt the en/ and nl/ calculator pages from the /en and /nl redirects.
"""
import json
import re
from pathlib import Path

from calculator_content import CALCS, T
from calculator_hub import CATEGORIES, HUB, HUB_CSS
from generate_article_pages import EXTRA_CSS as ARTICLE_CSS, SV, UI_SV, link, nav as site_nav
from generate_food_pages import BASE_CSS, LOGO_SVG, PAGE_CSS, SITE, LANGS, UI, esc, mark_english_links, replace_sitemap_block, sv_slugs

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
    <script src="/js/consent.js?v=4" defer></script>"""   # GA4 property of wibohealth.com, first thing in every <head>


ROOT = Path(__file__).resolve().parent.parent
BY_KEY = {c['key']: c for c in CALCS}
ALL_LANGS = LANGS + (SV,)
NAMES = {'ar': 'العربية', 'nl': 'Nederlands', 'en': 'English', SV: 'Svenska'}


def langs_of(calc):
    return tuple(l for l in ALL_LANGS if l in calc['content'])


def ui(lang):
    return UI_SV if lang == SV else UI[lang]

CALC_CSS = """
        .field-hint { display: block; margin-top: 5px; font-size: 0.8rem; color: var(--text-muted); line-height: 1.5; }
        .table-scroll { overflow-x: auto; max-width: 100%; -webkit-overflow-scrolling: touch; }
        .gl-table { font-size: 0.86rem; }
        .gl-table th, .gl-table td { padding: 8px 6px; }
        .gl-table td:first-child { min-width: 88px; }
        .gl-table td:not(:first-child) { white-space: nowrap; }
        .gl-table th { font-size: 0.8rem; line-height: 1.3; vertical-align: bottom; }
        .gl-results { list-style: none; margin: 6px 0 0; padding: 4px; border: 1px solid var(--border-color); border-radius: 12px; background: var(--bg-input); max-height: 300px; overflow-y: auto; }
        .gl-results button { width: 100%; text-align: start; padding: 9px 10px; border: 0; border-radius: 8px; background: none; color: inherit; font: inherit; cursor: pointer; }
        .gl-results button:hover, .gl-results button:focus { background: var(--primary-glow); }
        .gl-msg { padding: 9px 10px; color: var(--text-muted); }
        .gl-items { display: grid; gap: 8px; }
        .gl-empty { margin: 0; color: var(--text-muted); font-size: 0.92rem; }
        .gl-item { display: grid; grid-template-columns: 1fr auto auto; gap: 8px; align-items: center; padding: 8px 10px; border: 1px solid var(--border-color); border-radius: 12px; }
        .gl-item a { color: var(--primary); font-weight: 700; overflow-wrap: anywhere; }
        .gl-item label { display: flex; align-items: center; gap: 4px; white-space: nowrap; }
        .gl-item input { width: 84px; padding: 6px 8px; }
        .gl-remove { width: 34px; height: 34px; border-radius: 50%; border: 1px solid var(--border-color); background: none; color: inherit; font-size: 1.1rem; cursor: pointer; }
        .gl-band { font-weight: 800; }
        .gl-low { color: #15803d; } .gl-medium { color: #b45309; } .gl-high { color: #b91c1c; }
        .gl-note { margin: 10px 0 0; font-size: 0.88rem; color: var(--text-muted); }
        .gl-note:empty { display: none; }
        .gl-note a { color: var(--primary); }
        .next-steps { margin-top: 14px; padding: 14px 16px; border-radius: 14px; border: 1px solid var(--primary-glow); background: var(--bg-input); }
        .next-steps:empty { display: none; }
        .next-steps h3 { font-size: 1rem; margin: 0 0 6px; }
        .next-steps ul { margin: 0; padding-inline-start: 20px; display: grid; gap: 4px; }
        .next-steps .next-consult { margin: 0 0 8px; }
        .next-steps a { color: var(--primary); font-weight: 700; }
        .calc-page .disclaimer-box { background: none; border: 0; padding: 0; margin: 28px 0 0; font-size: 0.78rem;
            color: var(--text-muted); line-height: 1.6; box-shadow: none; }
        .page-wrapper.calc-page { max-width: 920px; }
        .calc-page .lead { font-size: 1.12rem; }
        .calc-nav { display: flex; flex-wrap: wrap; gap: 8px; margin: 4px 0 20px; }
        .calc-nav a { display: inline-flex; align-items: center; gap: 7px; padding: 7px 14px; border-radius: 999px; font-size: 0.85rem;
            font-weight: 700; text-decoration: none; color: var(--text-main); background: var(--bg-input); border: 1px solid var(--border-color); }
        .calc-nav a:hover { border-color: var(--primary); }
        .calc-nav a.current { background: rgba(16, 185, 129, 0.14); border-color: rgba(16, 185, 129, 0.45); }
        .calc-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 28px;
            box-shadow: var(--shadow); margin: 8px 0 30px; }
        .calc-card-head { display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;
            margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid var(--border-color); }
        .calc-card-title { display: flex; align-items: center; gap: 12px; font-size: 1.2rem; font-weight: 900; margin: 0; }
        .calc-card-title i { width: 42px; height: 42px; border-radius: 12px; background: rgba(16, 185, 129, 0.12); color: var(--primary);
            display: inline-flex; align-items: center; justify-content: center; font-size: 1.15rem; }
        .clinical-badge { font-size: 0.75rem; padding: 4px 10px; border-radius: 999px; background: rgba(6, 182, 212, 0.12);
            color: var(--secondary); font-weight: 700; border: 1px solid rgba(6, 182, 212, 0.25); }
        .form-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 16px; margin-bottom: 20px; }
        .form-group { display: flex; flex-direction: column; gap: 7px; }
        .form-group.wide { grid-column: 1 / -1; }
        .form-label { font-size: 0.9rem; font-weight: 700; color: var(--text-muted); }
        .form-control { width: 100%; padding: 13px 16px; background: var(--bg-input); border: 1px solid var(--border-color);
            border-radius: var(--radius-md); color: var(--text-main); font-size: 1rem; font-family: inherit; outline: none; }
        .form-control:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2); }
        /* long option labels (activity levels) must not widen the field on phones (WebKit sizes a select to its longest option) */
        .form-group { min-width: 0; }
        select.form-control { min-width: 0; max-width: 100%; white-space: normal; text-overflow: ellipsis; }
        select.form-control option { background: var(--bg-main); color: var(--text-main); }
        html[data-theme="dark"] select.form-control option { background: #121810; }
        .calc-submit-btn { width: 100%; padding: 15px; background: #047857; color: #fff; border: 0; border-radius: var(--radius-md);
            font-size: 1.05rem; font-weight: 800; cursor: pointer; font-family: inherit; display: flex; align-items: center;
            justify-content: center; gap: 10px; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.25); }
        .calc-submit-btn:hover { background: #065f46; }
        .result-view { display: none; margin-top: 24px; padding: 22px; border-radius: var(--radius-lg); background: var(--bg-input);
            border: 1px solid var(--border-color); }
        .result-view.active { display: block; }
        .result-main { text-align: center; }
        .result-heading { color: var(--text-muted); font-size: 0.95rem; }
        .result-big-value { font-size: 3rem; font-weight: 900; line-height: 1.1; margin: 8px 0; color: #047857; direction: ltr; }
        html[data-theme="dark"] .result-big-value { color: #6ee7b7; }
        .result-status-pill { display: inline-block; padding: 6px 18px; border-radius: 999px; font-size: 0.95rem; font-weight: 800; }
        .status-optimal { background: rgba(16, 185, 129, 0.15); color: #047857; border: 1px solid rgba(16, 185, 129, 0.35); }
        .status-warning { background: rgba(245, 158, 11, 0.15); color: #b45309; border: 1px solid rgba(245, 158, 11, 0.35); }
        .status-danger { background: rgba(239, 68, 68, 0.12); color: #b91c1c; border: 1px solid rgba(239, 68, 68, 0.35); }
        .status-info { background: rgba(59, 130, 246, 0.12); color: #1d4ed8; border: 1px solid rgba(59, 130, 246, 0.35); }
        html[data-theme="dark"] .status-optimal { color: #6ee7b7; }
        html[data-theme="dark"] .status-warning { color: #fcd34d; }
        html[data-theme="dark"] .status-danger { color: #fca5a5; }
        html[data-theme="dark"] .status-info { color: #93c5fd; }
        .result-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; margin-top: 18px;
            padding-top: 18px; border-top: 1px solid var(--border-color); }
        .breakdown-box { background: var(--bg-card); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-color); text-align: center; }
        .breakdown-label { font-size: 0.82rem; color: var(--text-muted); margin-bottom: 6px; font-weight: 700; }
        .breakdown-val { font-size: 1.3rem; font-weight: 900; color: var(--text-main); direction: ltr; unicode-bidi: isolate; }
        .breakdown-sub { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; }
        .clinical-note-box { margin-top: 16px; padding: 13px 16px; border-radius: var(--radius-md); background: rgba(6, 182, 212, 0.08);
            border: 1px solid rgba(6, 182, 212, 0.25); color: var(--text-main); font-size: 0.92rem; display: flex; gap: 10px; align-items: flex-start; }
        .clinical-note-box i { margin-top: 4px; color: var(--secondary); }
        html[data-theme="dark"] .clinical-note-box i { color: #7dd3fc; }
        .formula-box { background: var(--bg-input); border: 1px solid var(--border-color); border-inline-start: 4px solid var(--primary);
            border-radius: var(--radius-sm); padding: 14px 18px; margin: 10px 0 18px; font-weight: 800; text-align: center;
            font-family: ui-monospace, Consolas, monospace; font-size: 0.98rem; overflow-x: auto; }
        .table-wrap { overflow-x: auto; max-width: 100%; margin: 10px 0 22px; border: 1px solid var(--border-color); border-radius: var(--radius-md); }
        .data-table { width: 100%; border-collapse: collapse; font-size: 0.95rem; min-width: 460px; }
        .data-table th, .data-table td { padding: 11px 14px; border-bottom: 1px solid var(--border-color); text-align: start; vertical-align: top; }
        .data-table th { font-weight: 800; background: rgba(16, 185, 129, 0.08); color: var(--text-main); }
        .data-table tr:last-child td { border-bottom: 0; }
        .data-table .dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-inline-end: 8px; vertical-align: middle; }
        .dot.g { background: #10b981; } .dot.y { background: #f59e0b; } .dot.o { background: #f97316; } .dot.r { background: #ef4444; } .dot.b { background: #38bdf8; }
        .food-links { display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0 22px; }
        .food-links a { padding: 7px 14px; border-radius: 999px; font-size: 0.88rem; font-weight: 700; text-decoration: none;
            color: var(--text-main); background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); }
        .food-links a:hover { border-color: var(--primary); }
        .faq-list { display: grid; gap: 10px; margin: 10px 0 24px; }
        .faq-list details { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 0 16px; }
        .faq-list summary { cursor: pointer; font-weight: 800; padding: 14px 0; list-style: none; display: flex; justify-content: space-between; gap: 12px; }
        .faq-list summary::-webkit-details-marker { display: none; }
        .faq-list summary::after { content: "+"; color: var(--primary); font-weight: 900; }
        .faq-list details[open] summary::after { content: "−"; }
        .faq-list details p { margin: 0 0 14px; color: var(--text-muted); }
        .related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 10px 0 24px; }
        .related-card { display: flex; flex-direction: column; gap: 6px; padding: 16px; border-radius: var(--radius-md); text-decoration: none;
            background: var(--bg-input); border: 1px solid var(--border-color); color: var(--text-main); }
        .related-card:hover { border-color: var(--primary); }
        .related-card i { color: var(--primary); font-size: 1.2rem; }
        html[data-theme="dark"] .related-card i, html[data-theme="dark"] .calc-card-title i { color: #6ee7b7; }
        .related-card strong { font-size: 1rem; }
        .related-card span { color: var(--text-muted); font-size: 0.88rem; }
        .boodi-funnel-card { margin: 26px 0; background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(6, 182, 212, 0.06));
            border: 1px solid rgba(16, 185, 129, 0.25); border-radius: var(--radius-lg); padding: 22px 24px; display: flex;
            align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; }
        .boodi-funnel-card h2 { font-size: 1.15rem; font-weight: 900; margin: 0 0 6px; }
        .boodi-funnel-card p { color: var(--text-muted); margin: 0; font-size: 0.95rem; max-width: 560px; }
        .funnel-btn { display: inline-flex; align-items: center; gap: 10px; padding: 12px 22px; background: #047857; color: #fff;
            font-weight: 800; text-decoration: none; border-radius: var(--radius-md); }
        .funnel-btn:hover { background: #065f46; }
        @media (max-width: 640px) { .calc-card { padding: 20px; } .result-big-value { font-size: 2.4rem; } }
"""


def page_url(calc, lang, absolute=True):
    path = f'/{calc["slug"]}.html' if lang == 'ar' else f'/{lang}/{calc["slug"]}.html'
    return SITE + path if absolute else path


SV_FOOD_SLUGS = sv_slugs()


def food_url(slug, lang):
    if lang == SV and slug not in SV_FOOD_SLUGS:      # foods without a Swedish page open in English
        lang = 'en'
    return f'/foods/{slug}.html' if lang == 'ar' else f'/{lang}/foods/{slug}.html'


def render_body(html, lang):
    """Content links foods as {food:slug}, site pages as {site:/path} and sibling calculators as {calc:key}."""
    html = re.sub(r'\{food:([a-z0-9-]+)\}', lambda m: food_url(m.group(1), lang), html)
    html = re.sub(r'\{calc:([a-z]+)\}', lambda m: page_url(BY_KEY[m.group(1)], lang, absolute=False), html)
    return re.sub(r'\{site:([^}]+)\}', lambda m: link(m.group(1), lang), html)


def opt(value, label, selected=False):
    return f'<option value="{value}"{" selected" if selected else ""}>{esc(label)}</option>'


def field(fid, label, control, wide=False):
    return (f'<div class="form-group{" wide" if wide else ""}"><label class="form-label" for="{fid}">{esc(label)}</label>'
            f'{control}</div>')


def num(fid, ph, lo, hi, step):
    return (f'<input type="number" id="{fid}" class="form-control" inputmode="decimal" min="{lo}" max="{hi}" step="{step}" '
            f'required placeholder="{esc(ph)}">')


def sex_select(fid, w):
    return f'<select id="{fid}" class="form-control">{opt("male", w["male"])}{opt("female", w["female"])}</select>'


def widget(calc, lang):
    """Form + empty result view. All result text is filled in by the page script from the same strings."""
    w = calc['content'][lang]['ui']
    k = calc['key']
    if k == 'bmi':
        fields = field('f_weight', w['lbl_weight'], num('f_weight', w['ph_weight'], 20, 350, 0.1)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 80, 250, 0.5))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">0.0</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["ideal_label"])}</div>'
                  '<div class="breakdown-val" id="r_range">--</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["prime_label"])}</div>'
                  '<div class="breakdown-val" id="r_prime">--</div></div></div>')
    elif k == 'tdee':
        acts = ''.join(opt(v, label, v == '1.55') for v, label in zip(('1.2', '1.375', '1.55', '1.725', '1.9'), w['acts']))
        fields = field('f_sex', w['lbl_sex'], sex_select('f_sex', w)) + \
                 field('f_age', w['lbl_age'], num('f_age', w['ph_age'], 18, 100, 1)) + \
                 field('f_weight', w['lbl_weight'], num('f_weight', w['ph_weight'], 30, 300, 0.1)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 120, 240, 0.5)) + \
                 field('f_activity', w['lbl_activity'], f'<select id="f_activity" class="form-control">{acts}</select>', wide=True)
        boxes = ''.join(f'<div class="breakdown-box"><div class="breakdown-label">{esc(w[b + "_label"])}</div>'
                        f'<div class="breakdown-val" id="r_{b}">--</div><div class="breakdown-sub">{esc(w[b + "_sub"])}</div></div>'
                        for b in ('bmr', 'deficit', 'surplus'))
        macros = ''.join(f'<div class="breakdown-box"><div class="breakdown-label">{esc(w[m])}</div>'
                         f'<div class="breakdown-val" id="r_{m}">--</div><div class="breakdown-sub" id="r_{m}_kcal"></div></div>'
                         for m in ('protein', 'fat', 'carbs'))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  f'<div class="result-big-value" id="r_main">0</div><div class="result-heading">{esc(w["kcal_day"])}</div></div>'
                  f'<div class="result-grid">{boxes}</div>'
                  f'<h3 style="margin:20px 0 0;font-size:1rem">{esc(w["macros_header"])}</h3><div class="result-grid" style="border-top:0;padding-top:10px">{macros}</div>')
    elif k == 'water':
        acts = ''.join(opt(v, label, v == '350') for v, label in zip(('0', '350', '650', '1000'), w['acts']))
        status = ''.join(opt(v, label) for v, label in zip(('0', '300', '700'), w['status_opts']))
        fields = field('f_sex', w['lbl_sex'], sex_select('f_sex', w)) + \
                 field('f_weight', w['lbl_weight'], num('f_weight', w['ph_weight'], 30, 250, 0.1)) + \
                 field('f_activity', w['lbl_activity'], f'<select id="f_activity" class="form-control">{acts}</select>') + \
                 field('f_status', w['lbl_status'], f'<select id="f_status" class="form-control">{status}</select>')
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">0.0 L</div><div class="result-status-pill status-info" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["efsa_label"])}</div>'
                  f'<div class="breakdown-val" id="r_efsa">--</div><div class="breakdown-sub">{esc(w["efsa_sub"])}</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["drinks_label"])}</div>'
                  f'<div class="breakdown-val" id="r_drinks">--</div><div class="breakdown-sub">{esc(w["drinks_sub"])}</div></div></div>')
    elif k == 'hba1c':
        units = opt('pct', w['u_pct'], lang in ('ar', 'en')) + opt('mmol', w['u_mmol'], lang in ('nl', SV))
        fields = field('f_value', w['lbl_value'], num('f_value', w['ph_value'], 3, 200, 0.1)) + \
                 field('f_unit', w['lbl_unit'], f'<select id="f_unit" class="form-control">{units}</select>')
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["eag_label"])}</div>'
                  f'<div class="breakdown-val" id="r_eag">--</div><div class="breakdown-sub">{esc(w["eag_sub"])}</div></div></div>')
    elif k == 'glucose':
        units = opt('mgdl', w['u_mgdl'], lang in ('ar', 'en')) + opt('mmol', w['u_mmol'], lang in ('nl', SV))
        when = opt('fast', w['w_fast'], True) + opt('after', w['w_after']) + opt('any', w['w_any'])
        fields = field('f_value', w['lbl_value'], num('f_value', w['ph_value'], 0.5, 1000, 0.1)) + \
                 field('f_unit', w['lbl_unit'], f'<select id="f_unit" class="form-control">{units}</select>') + \
                 field('f_when', w['lbl_when'], f'<select id="f_when" class="form-control">{when}</select>', wide=True)
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>')
    elif k == 'findrisc':
        yn = lambda fid, q, yes_first=False: field(fid, w[q], f'<select id="{fid}" class="form-control">'
                                                         f'{opt("1", w["yes"]) + opt("0", w["no"]) if yes_first else opt("0", w["no"]) + opt("1", w["yes"])}</select>', wide=True)
        fam = opt('none', w['fam_none']) + opt('second', w['fam_second']) + opt('first', w['fam_first'])
        fields = field('f_sex', w['sex'], sex_select('f_sex', w)) + \
                 field('f_age', w['age'], num('f_age', '45', 18, 110, 1)) + \
                 field('f_weight', w['weight'], num('f_weight', '80', 30, 300, 0.1)) + \
                 field('f_height', w['height'], num('f_height', '170', 120, 230, 0.5)) + \
                 field('f_waist', w['waist'], num('f_waist', '92', 40, 220, 0.5), wide=True) + \
                 yn('f_active', 'active', yes_first=True) + yn('f_veg', 'veg', yes_first=True) + yn('f_bp', 'bp') + yn('f_glu', 'glucose') + \
                 field('f_family', w['family'], f'<select id="f_family" class="form-control">{fam}</select>', wide=True)
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["risk_label"])}</div>'
                  '<div class="breakdown-val" id="r_risk">--</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["bmi_label"])}</div>'
                  '<div class="breakdown-val" id="r_bmi">--</div></div></div>')
    elif k == 'homa':   # glucose required; triglycerides and insulin optional (2026-11-23): TyG and/or HOMA-IR
        ins = opt('uiu', w['u_uiu'], True) + opt('pmol', w['u_pmol'])
        glu = opt('mgdl', w['u_mgdl'], lang in ('ar', 'en')) + opt('mmol', w['u_mmol'], lang in ('nl', SV))
        tgu = opt('mgdl', w['u_mgdl'], lang in ('ar', 'en')) + opt('mmol', w['u_mmol'], lang in ('nl', SV))
        opt_num = lambda fid, ph, lo, hi: num(fid, ph, lo, hi, 0.01).replace(' required', '')
        hint = lambda key: f'<small class="field-hint">{esc(w[key])}</small>'
        fields = field('f_glu', w['lbl_glu'], num('f_glu', w['ph_glu'], 1, 1000, 0.1)) + \
                 field('f_glu_u', '', f'<select id="f_glu_u" class="form-control" aria-label="{esc(w["lbl_glu"])}">{glu}</select>') + \
                 field('f_tg', w['lbl_tg'], opt_num('f_tg', w['ph_tg'], 0.1, 5000) + hint('hint_tg')) + \
                 field('f_tg_u', '', f'<select id="f_tg_u" class="form-control" aria-label="{esc(w["lbl_tg"])}">{tgu}</select>') + \
                 field('f_ins', w['lbl_ins'], opt_num('f_ins', w['ph_ins'], 0.5, 1000) + hint('hint_ins')) + \
                 field('f_ins_u', '', f'<select id="f_ins_u" class="form-control" aria-label="{esc(w["lbl_ins"])}">{ins}</select>')
        result = (f'<div class="result-main"><div class="result-heading" id="r_heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid" id="box_sec"><div class="breakdown-box"><div class="breakdown-label" id="r_sec_label">{esc(w["tyg_label"])}</div>'
                  '<div class="breakdown-val" id="r_sec">--</div><div class="breakdown-sub" id="r_sec_sub"></div></div></div>')
    elif k == 'deficit':
        acts = ''.join(opt(v, label, v == '1.375') for v, label in zip(('1.2', '1.375', '1.55', '1.725', '1.9'), TDEE_UI[lang]['acts']))
        paces = ''.join(opt(v, label, v == '0.5') for v, label in zip(('0.25', '0.5', '0.75'), w['paces']))
        fields = field('f_sex', w['lbl_sex'], sex_select('f_sex', w)) + \
                 field('f_age', w['lbl_age'], num('f_age', w['ph_age'], 18, 100, 1)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 120, 240, 0.5)) + \
                 field('f_weight', w['lbl_weight'], num('f_weight', w['ph_weight'], 35, 350, 0.1)) + \
                 field('f_target', w['lbl_target'], num('f_target', w['ph_target'], 30, 350, 0.1), wide=True) + \
                 field('f_activity', w['lbl_activity'], f'<select id="f_activity" class="form-control">{acts}</select>', wide=True) + \
                 field('f_pace', w['lbl_pace'], f'<select id="f_pace" class="form-control">{paces}</select>', wide=True)
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  f'<div class="result-big-value" id="r_main">--</div><div class="result-heading">{esc(w["kcal_day"])}</div>'
                  '<div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["date_label"])}</div>'
                  '<div class="breakdown-val" id="r_date">--</div><div class="breakdown-sub" id="r_weeks"></div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["tdee_label"])}</div><div class="breakdown-val" id="r_tdee">--</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["lose_label"])}</div><div class="breakdown-val" id="r_lose">--</div></div></div>')
    elif k == 'protein':
        acts = ''.join(opt(v, label, v == '1.375') for v, label in zip(('1.2', '1.375', '1.55', '1.725', '1.9'), TDEE_UI[lang]['acts']))
        goals = ''.join(opt(v, label, v == 'general') for v, label in zip(('general', 'loss', 'muscle', 'glp1'), w['goals']))
        kcal = num('f_kcal', w['ph_kcal'], 800, 6000, 10).replace(' required', '')
        fields = field('f_sex', w['lbl_sex'], sex_select('f_sex', w)) + \
                 field('f_age', w['lbl_age'], num('f_age', w['ph_age'], 18, 100, 1)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 120, 240, 0.5)) + \
                 field('f_weight', w['lbl_weight'], num('f_weight', w['ph_weight'], 35, 350, 0.1)) + \
                 field('f_goal', w['lbl_goal'], f'<select id="f_goal" class="form-control">{goals}</select>', wide=True) + \
                 field('f_activity', w['lbl_activity'], f'<select id="f_activity" class="form-control">{acts}</select>', wide=True) + \
                 field('f_kcal', w['lbl_kcal'], kcal, wide=True)
        macros = ''.join(f'<div class="breakdown-box"><div class="breakdown-label">{esc(w[m + "_label"])}</div>'
                         f'<div class="breakdown-val" id="r_{m}">--</div></div>' for m in ('kcal', 'fat', 'carbs'))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["meal_label"])}</div><div class="breakdown-val" id="r_meal">--</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["basis_label"])}</div><div class="breakdown-val" id="r_basis">--</div></div></div>'
                  f'<h3 style="margin:20px 0 0;font-size:1rem">{esc(w["macros_header"])}</h3><div class="result-grid" style="border-top:0;padding-top:10px">{macros}</div>')
    elif k == 'bodyfat':
        hip = num('f_hip', w['ph_hip'], 50, 250, 0.5).replace(' required', '')
        fields = field('f_sex', w['lbl_sex'], sex_select('f_sex', w)) + \
                 field('f_age', w['lbl_age'], num('f_age', w['ph_age'], 18, 100, 1)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 120, 240, 0.5)) + \
                 field('f_weight', w['lbl_weight'], num('f_weight', w['ph_weight'], 35, 350, 0.1)) + \
                 field('f_neck', w['lbl_neck'], num('f_neck', w['ph_neck'], 20, 70, 0.5), wide=True) + \
                 field('f_waist', w['lbl_waist'], num('f_waist', w['ph_waist'], 40, 220, 0.5), wide=True) + \
                 field('f_hip', w['lbl_hip'], hip, wide=True).replace('<div class="form-group wide">', '<div class="form-group wide" id="grp_hip" hidden>', 1)
        boxes = ''.join(f'<div class="breakdown-box"><div class="breakdown-label">{esc(w[b + "_label"])}</div>'
                        f'<div class="breakdown-val" id="r_{b}">--</div></div>' for b in ('fatkg', 'leankg', 'range', 'hw'))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid">{boxes}</div>')
    elif k == 'gl':
        fields = (f'<div class="form-group wide"><label class="form-label" for="f_search">{esc(w["lbl_search"])}</label>'
                  f'<input type="search" id="f_search" class="form-control" autocomplete="off" placeholder="{esc(w["ph_search"])}" '
                  'aria-controls="gl_results"><ul class="gl-results" id="gl_results" role="listbox" hidden></ul></div>'
                  f'<div class="form-group wide"><div class="gl-items" id="gl_items"><p class="gl-empty">{esc(w["empty"])}</p></div></div>')
        heads = ''.join(f'<th>{esc(w[h])}</th>' for h in ('th_food', 'th_gl', 'th_gi', 'th_grams', 'th_carbs'))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">--</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="table-scroll"><table class="nutrition-table gl-table"><thead><tr>{heads}</tr></thead><tbody id="r_rows"></tbody></table></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["day_label"])}</div><div class="breakdown-val" id="r_day">--</div></div>'
                  f'<div class="breakdown-box" id="box_top"><div class="breakdown-label">{esc(w["top_label"])}</div><div class="breakdown-val" id="r_top">--</div>'
                  '<div class="breakdown-sub" id="r_swap"></div></div></div>'
                  '<p class="gl-note" id="r_est"></p><p class="gl-note" id="r_zero"></p>')
    else:  # whtr
        fields = field('f_waist', w['lbl_waist'], num('f_waist', w['ph_waist'], 40, 220, 0.5)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 90, 240, 0.5))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">0.00</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["target_label"])}</div>'
                  '<div class="breakdown-val" id="r_target">--</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["diff_label"])}</div>'
                  '<div class="breakdown-val" id="r_diff">--</div></div></div>')
    if lang in ('nl', SV):                  # empty-state value with the decimal comma the page script uses
        result = result.replace('id="r_main">0.0', 'id="r_main">0,0')
    return f'''<section class="calc-card" id="calculator" aria-labelledby="calc-title">
                <div class="calc-card-head">
                    <h2 class="calc-card-title" id="calc-title"><i class="fas {calc["icon"]}" aria-hidden="true"></i> {esc(w["card_title"])}</h2>
                    <span class="clinical-badge">{esc(calc["badge"])}</span>
                </div>
                <form id="calcForm" novalidate>
                    <div class="form-grid">{fields}</div>
                    <button type="submit" class="calc-submit-btn"><i class="fas fa-calculator" aria-hidden="true"></i> {esc(w["btn"])}</button>
                </form>
                <div class="result-view" id="resultView" aria-live="polite">{result}
                    <div class="clinical-note-box"><i class="fas fa-circle-info" aria-hidden="true"></i><span id="r_note"></span></div>{'' if k in ('bmi', 'tdee', 'water', 'whtr') else chr(10) + '                    <div class="next-steps" id="r_next"></div>'}
                </div>
            </section>'''


LOGIC = {
    # Each engine reads the form, fills the result view and returns nothing. S = this page's strings, fmt = number formatter.
    'bmi': r"""
        var w = val('f_weight'), h = val('f_height');
        if (!w || !h) return false;
        var m = h / 100, bmi = w / (m * m), cls, tip, st;
        if (bmi < 18.5) { cls = 'under'; st = 'status-warning'; }
        else if (bmi < 25) { cls = 'normal'; st = 'status-optimal'; }
        else if (bmi < 30) { cls = 'over'; st = 'status-warning'; }
        else if (bmi < 35) { cls = 'ob1'; st = 'status-danger'; }
        else if (bmi < 40) { cls = 'ob2'; st = 'status-danger'; }
        else { cls = 'ob3'; st = 'status-danger'; }
        tip = S['tip_' + (cls.indexOf('ob') === 0 ? 'obese' : cls)];
        set('r_main', fmt(bmi, 1)); pill(S['st_' + cls], st); set('r_note', tip);
        set('r_range', fmt(18.5 * m * m, 1) + ' – ' + fmt(24.9 * m * m, 1) + ' kg');
        set('r_prime', fmt(bmi / 25, 2));
        return true;""",
    'tdee': r"""
        var sex = document.getElementById('f_sex').value, a = val('f_age'), w = val('f_weight'), h = val('f_height'),
            pal = parseFloat(document.getElementById('f_activity').value);
        if (!a || !w || !h) return false;
        var bmr = 10 * w + 6.25 * h - 5 * a + (sex === 'male' ? 5 : -161), tdee = bmr * pal;
        var deficit = Math.max(Math.round(bmr), Math.round(tdee * 0.8)), surplus = Math.round(tdee * 1.15);
        // protein 1.2-1.6 g/kg (aligned with the protein calculator), adjusted weight when BMI >= 30; split on 1.4 g/kg
        var pw = window.WiboCalc ? WiboCalc.proteinWeight(w, h) : w, pLo = Math.round(pw * 1.2), pHi = Math.round(pw * 1.6);
        var pG = Math.round(pw * 1.4), pK = pG * 4, fK = Math.round(deficit * 0.25), fG = Math.round(fK / 9),
            cK = Math.max(0, deficit - pK - fK), cG = Math.round(cK / 4);
        set('r_main', fmt(Math.round(tdee), 0)); set('r_bmr', fmt(Math.round(bmr), 0) + ' kcal');
        set('r_deficit', fmt(deficit, 0) + ' kcal'); set('r_surplus', fmt(surplus, 0) + ' kcal');
        set('r_protein', pLo + '–' + pHi + ' g'); set('r_protein_kcal', fmt(pK, 0) + ' kcal');
        set('r_fat', fG + ' g'); set('r_fat_kcal', fmt(fK, 0) + ' kcal');
        set('r_carbs', cG + ' g'); set('r_carbs_kcal', fmt(cK, 0) + ' kcal');
        set('r_note', cK < 400 ? S['tip_lowcarb'] : S['tip']);
        return true;""",
    'water': r"""
        var sex = document.getElementById('f_sex').value, w = val('f_weight'),
            extra = parseFloat(document.getElementById('f_activity').value),
            status = sex === 'female' ? parseFloat(document.getElementById('f_status').value) : 0;
        if (!w) return false;
        var lo = (w * 30 + extra + status) / 1000, hi = (w * 35 + extra + status) / 1000;
        var efsa = ((sex === 'male' ? 2500 : 2000) + status) / 1000;
        set('r_main', fmt(lo, 1) + ' – ' + fmt(hi, 1) + ' L');
        pill(S['cups'].replace('{a}', Math.round(lo * 4)).replace('{b}', Math.round(hi * 4)), 'status-info');
        set('r_efsa', fmt(efsa, 1) + ' L'); set('r_drinks', '≈ ' + fmt(efsa * 0.8, 1) + ' L');
        set('r_note', w > 100 ? S['tip_heavy'] : S['tip']);
        return true;""",
    'whtr': r"""
        var wa = val('f_waist'), h = val('f_height');
        if (!wa || !h) return false;
        var r = wa / h, cls, st;
        if (r < 0.4) { cls = 'low'; st = 'status-info'; }
        else if (r < 0.5) { cls = 'healthy'; st = 'status-optimal'; }
        else if (r < 0.6) { cls = 'increased'; st = 'status-warning'; }
        else { cls = 'high'; st = 'status-danger'; }
        set('r_main', fmt(r, 2)); pill(S['st_' + cls], st); set('r_note', S['tip_' + cls]);
        set('r_target', '< ' + fmt(h * 0.5, 1) + ' cm');
        var d = wa - h * 0.5;
        set('r_diff', d > 0 ? '−' + fmt(d, 1) + ' cm' : S['ok_diff']);
        return true;""",
    # diabetes tools: formulas from js/calc-formulas.js (WiboCalc, tested); next(band) fills the "next steps" card
    'hba1c': r"""
        var v = val('f_value'), unit = document.getElementById('f_unit').value, C = window.WiboCalc;
        if (!v || !C) return false;
        var pct = unit === 'pct' ? v : C.hba1cMmolToPercent(v), mmol = unit === 'pct' ? C.hba1cPercentToMmol(v) : v;
        if (pct < 3 || pct > 20) return false;
        var band = C.hba1cBand(mmol), st = { normal: 'status-optimal', prediabetes: 'status-warning', diabetes: 'status-danger' }[band];
        set('r_main', fmt(pct, 1) + '% = ' + fmt(Math.round(mmol), 0) + ' mmol/mol');
        set('r_eag', fmt(Math.round(C.eagMgdl(pct)), 0) + ' mg/dL · ' + fmt(C.eagMmol(pct), 1) + ' mmol/L');
        pill(S['st_' + band], st); set('r_note', S['tip_' + band]); next(band);
        return true;""",
    'glucose': r"""
        var v = val('f_value'), unit = document.getElementById('f_unit').value, when = document.getElementById('f_when').value, C = window.WiboCalc;
        if (!v || !C) return false;
        var mmol = unit === 'mmol' ? v : C.mgdlToMmol(v), mg = unit === 'mmol' ? C.mmolToMgdl(v) : v;
        set('r_main', unit === 'mmol' ? fmt(Math.round(mg), 0) + ' mg/dL' : fmt(mmol, 1) + ' mmol/L');
        var band, st;
        if (C.fastingGlucoseBand(mmol) === 'low') band = 'low';
        else if (when === 'fast') band = C.fastingGlucoseBand(mmol);
        else if (when === 'after') band = C.afterMealBand(mmol);
        else band = 'conv';
        st = { low: 'status-danger', normal: 'status-optimal', prediabetes: 'status-warning', diabetes: 'status-danger', conv: 'status-info' }[band];
        pill(S['st_' + band], st);
        set('r_note', band === 'low' || band === 'conv' ? S['tip_' + band] : S['tip_' + when + '_' + band]);
        next(band);
        return true;""",
    'findrisc': r"""
        var C = window.WiboCalc, age = val('f_age'), w = val('f_weight'), h = val('f_height'), waist = val('f_waist');
        if (!C || !age || !w || !h || !waist) return false;
        var b = C.bmi(w, h), r = C.findrisc({ age: age, bmi: b, waist: waist, sex: document.getElementById('f_sex').value === 'female' ? 'f' : 'm',
            active: document.getElementById('f_active').value === '1', vegDaily: document.getElementById('f_veg').value === '1',
            bpMeds: document.getElementById('f_bp').value === '1', highGlucose: document.getElementById('f_glu').value === '1',
            family: document.getElementById('f_family').value });
        var st = { low: 'status-optimal', slight: 'status-info', moderate: 'status-warning', high: 'status-danger', veryhigh: 'status-danger' }[r.band];
        set('r_main', r.score + ' / 26'); pill(S['st_' + r.band], st); set('r_risk', S['risk_' + r.band]);
        set('r_bmi', fmt(b, 1)); set('r_note', S['tip_' + r.band]); next(r.band);
        return true;""",
    'homa': r"""
        var C = window.WiboCalc, glu = val('f_glu'), tg = val('f_tg'), ins = val('f_ins'), box = document.getElementById('box_sec');
        if (!C || !glu) return false;
        var gm = document.getElementById('f_glu_u').value === 'mmol' ? glu : C.mgdlToMmol(glu);
        var t = tg ? C.tyg(document.getElementById('f_tg_u').value === 'mmol' ? tg : tg / 88.57, gm) : null;
        if (!tg && !ins) {          // glucose alone cannot estimate insulin resistance
            set('r_heading', S['res_heading']); set('r_main', '--'); pill(S['st_need'], 'status-warning');
            set('r_note', S['tip_need']); box.hidden = true; next('need'); return true;
        }
        box.hidden = false;
        if (ins) {                  // HOMA-IR is the main result, TyG beside it
            if (document.getElementById('f_ins_u').value === 'pmol') ins = ins / 6;
            var h = C.homaIr(ins, gm), band = C.homaBand(h), st = { low: 'status-optimal', borderline: 'status-warning', high: 'status-danger' }[band];
            set('r_heading', S['res_heading']); set('r_main', fmt(h, 2)); pill(S['st_' + band], st); set('r_note', S['tip_' + band]);
            set('r_sec_label', S['tyg_label']); set('r_sec', t === null ? '--' : fmt(t, 2));
            set('r_sec_sub', t === null ? S['tyg_none'] : t < 8.5 ? S['tyg_low'] : S['tyg_high']);
            next(band);
        } else {                    // no insulin test: TyG is the main result
            var tb = t < 8.5 ? 'low' : 'high';
            set('r_heading', S['res_heading_tyg']); set('r_main', fmt(t, 2));
            pill(S['st_tyg_' + tb], tb === 'low' ? 'status-optimal' : 'status-warning'); set('r_note', S['tip_tyg_' + tb]);
            set('r_sec_label', S['homa_label']); set('r_sec', '--'); set('r_sec_sub', S['homa_none']);
            next(tb === 'low' ? 'low' : 'borderline');
        }
        return true;""",
    # batch C (2026-11-23): formulas from js/calc-formulas.js
    'deficit': r"""
        var C = window.WiboCalc, sx = document.getElementById('f_sex').value === 'female' ? 'f' : 'm',
            age = val('f_age'), h = val('f_height'), w = val('f_weight'), t = val('f_target');
        if (!C || !age || !h || !w || !t) return false;
        ['r_date', 'r_weeks', 'r_tdee', 'r_lose'].forEach(function (id) { set(id, id === 'r_weeks' ? '' : '--'); });
        if (t >= w) { set('r_main', '--'); pill(S['st_warn'], 'status-warning'); set('r_note', S['tip_invalid']); next(''); return true; }
        var p = C.weightLossPlan({ sex: sx, age: age, height: h, weight: w, target: t,
            pal: parseFloat(document.getElementById('f_activity').value), pace: parseFloat(document.getElementById('f_pace').value) });
        set('r_main', fmt(p.intake, 0)); set('r_tdee', fmt(Math.round(p.tdee / 10) * 10, 0) + ' kcal'); set('r_lose', fmt(p.toLose, 1) + ' ' + S['kg']);
        if (p.reached) {
            var d = new Date(); d.setDate(d.getDate() + p.weeks * 7);
            set('r_date', d.toLocaleDateString(DATE_LOCALE, { month: 'long', year: 'numeric' })); set('r_weeks', S['weeks_txt'].replace('{n}', p.weeks));
        }
        var notes = [];
        if (!p.reached) notes.push(S['tip_stall']);
        if (p.floorApplied) notes.push(S['tip_floor'].replace('{floor}', fmt(C.FLOOR[sx], 0)));
        else if (p.belowBmr) notes.push(S['tip_bmr'].replace('{bmr}', fmt(Math.round(p.bmr / 10) * 10, 0)));
        if (p.fastPace) notes.push(S['tip_fast']);
        if (p.targetBmi < 18.5) { var r = C.healthyWeightRange(h); notes.push(S['tip_lowtarget'].replace('{lo}', fmt(Math.ceil(r[0]), 0)).replace('{hi}', fmt(Math.floor(r[1]), 0))); }
        pill(notes.length ? S['st_warn'] : S['st_plan'], notes.length ? 'status-warning' : 'status-info');
        set('r_note', notes.concat([S['tip_base']]).join(' ')); next('plan');
        return true;""",
    'protein': r"""
        var C = window.WiboCalc, sx = document.getElementById('f_sex').value === 'female' ? 'f' : 'm',
            age = val('f_age'), h = val('f_height'), w = val('f_weight'), goal = document.getElementById('f_goal').value, kcal = val('f_kcal');
        if (!C || !age || !h || !w) return false;
        var b = C.bmi(w, h), pw = C.proteinWeight(w, h), r = C.proteinPerKg(goal, age), lo = Math.round(pw * r[0]), hi = Math.round(pw * r[1]);
        set('r_main', lo === hi ? lo + ' g' : lo + '–' + hi + ' g');
        pill(S['perkg'].replace('{v}', r[0] === r[1] ? fmt(r[0], 2) : fmt(r[0], 1) + '–' + fmt(r[1], 1)), 'status-info');
        var mid = (lo + hi) / 2;
        set('r_meal', Math.round(mid / 3) + ' g'); set('r_basis', fmt(pw, 1) + ' kg · ' + (b >= 30 ? S['basis_adj'] : S['basis_actual']));
        if (!kcal) {
            var tdee = C.bmr(sx, age, w, h) * parseFloat(document.getElementById('f_activity').value);
            kcal = goal === 'loss' || goal === 'glp1' ? Math.max(C.FLOOR[sx], tdee - 550) : tdee;
        }
        kcal = Math.round(kcal / 10) * 10;
        var pK = Math.round(mid) * 4, fK = kcal * 0.3, cK = Math.max(0, kcal - pK - fK);
        set('r_kcal', fmt(kcal, 0) + ' kcal'); set('r_fat', Math.round(fK / 9) + ' g'); set('r_carbs', Math.round(cK / 4) + ' g');
        var tip = goal === 'general' ? (age >= 65 ? S['tip_general65'] : S['tip_general']) : S['tip_' + goal];
        set('r_note', tip + (b >= 30 ? ' ' + S['tip_adj'].replace('{w}', fmt(pw, 1)) : '')); next('ok');
        return true;""",
    'bodyfat': r"""
        var C = window.WiboCalc, sx = document.getElementById('f_sex').value === 'female' ? 'f' : 'm',
            age = val('f_age'), h = val('f_height'), w = val('f_weight'), neck = val('f_neck'), waist = val('f_waist'), hip = val('f_hip');
        if (!C || !age || !h || !w || !neck || !waist || (sx === 'f' && !hip)) return false;
        var pct = C.navyBodyFat(sx, h, neck, waist, hip);
        ['r_fatkg', 'r_leankg', 'r_range', 'r_hw'].forEach(function (id) { set(id, '--'); });
        if (!(pct > 0 && pct < 75)) { set('r_main', '--'); pill(S['tip_invalid'], 'status-warning'); set('r_note', S['tip_invalid']); next(''); return true; }
        var band = C.bodyFatBand(sx, age, pct), row = C.bodyFatRow(sx, age), hw = C.healthyWeightRange(h);
        var st = { verylow: 'status-danger', low: 'status-warning', healthy: 'status-optimal', high: 'status-warning', veryhigh: 'status-danger' }[band];
        set('r_main', fmt(pct, 1) + '%'); pill(S['st_' + band], st);
        set('r_fatkg', fmt(w * pct / 100, 1) + ' kg'); set('r_leankg', fmt(w * (1 - pct / 100), 1) + ' kg');
        set('r_range', row[0] + '–' + row[1] + '%'); set('r_hw', fmt(Math.ceil(hw[0]), 0) + '–' + fmt(Math.floor(hw[1]), 0) + ' kg');
        set('r_note', S['tip_' + band]); next(band);
        return true;""",
    'gl': r"""
        var C = window.WiboCalc, G = window.WiboGL;
        if (!C || !G || !G.items.length) { if (G) G.hint(); return false; }
        var total = 0, rows = '', top = null, est = false, zero = false;
        G.items.forEach(function (it) {
            var f = it.f, gi = f[6], carbs = f[8] * it.g / 100, gl = C.glycemicLoad(gi, f[8], 0, it.g);
            total += gl; if (gi !== null && f[7]) est = true; if (gi === null || !f[8]) zero = true;
            if (gl > 0 && (!top || gl > top.gl)) top = { f: f, gl: gl };
            rows += '<tr><td>' + G.link(f) + '</td><td><span class="gl-band gl-' + C.glBand(gl) + '">' + fmt(gl, 1) + '</span></td><td>' +
                (gi === null ? '–' : gi) + '</td><td>' + fmt(it.g, 0) + ' g</td><td>' + fmt(carbs, 1) + ' g</td></tr>';
        });
        document.getElementById('r_rows').innerHTML = rows;
        var band = C.glBand(total, 'meal'), st = { low: 'status-optimal', medium: 'status-warning', high: 'status-danger' }[band];
        set('r_main', fmt(Math.round(total), 0)); pill(S['st_' + band], st);
        set('r_day', S['day_txt'].replace('{p}', Math.round(total / 80 * 100)));
        var box = document.getElementById('box_top'); box.hidden = !top;
        if (top) {
            set('r_top', G.name(top.f) + ' (' + fmt(top.gl, 1) + ')');
            var swap = G.swap(top.f); document.getElementById('r_swap').innerHTML = swap ? S['swap_txt'].replace('{b}', G.link(swap)) : G.esc(S['no_swap']);
        }
        document.getElementById('r_est').innerHTML = est ? S['est_note'] : '';
        set('r_zero', zero ? S['zero_note'] : '');
        set('r_note', S['tip_meal']); next('meal');
        return true;""",
}
NEW_TOOLS = ('hba1c', 'glucose', 'findrisc', 'homa', 'deficit', 'protein', 'bodyfat', 'gl')
# page set-up that runs once (not on submit): the hip field for women, and the meal builder of the glycemic load tool
INIT = {
    'bodyfat': r"""
            var sexSel = document.getElementById('f_sex'), hipGrp = document.getElementById('grp_hip'), hipIn = document.getElementById('f_hip');
            function hipToggle() { var f = sexSel.value === 'female'; hipGrp.hidden = !f; hipIn.required = f; }
            sexSel.addEventListener('change', hipToggle); hipToggle();""",
    'gl': r"""
            var NAME = {NAME_COL}, PREFIX = '{PREFIX}', DATA = '/data/gl-foods.json?v={GL_VER}', data = null, loading = null;
            var q = document.getElementById('f_search'), box = document.getElementById('gl_results'), list = document.getElementById('gl_items');
            function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
            function norm(s) {
                // Latin accents and Arabic harakat/hamza marks dropped (NFD splits alef with hamza into alef + mark)
                return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f\u064b-\u065f\u0670\u0640]/g, '')
                    .replace(/\u0629/g, '\u0647').replace(/\u0649/g, '\u064a');
            }
            function name(f) { return f[NAME]; }
            function link(f) { return '<a href="' + PREFIX + '/foods/' + f[1] + '.html">' + esc(name(f)) + '</a>'; }
            function load() {
                if (data) return Promise.resolve(data);
                if (!loading) loading = fetch(DATA).then(function (r) { return r.json(); }).then(function (d) {
                    data = d; d.forEach(function (f) { f.k = norm(f[NAME]) + ' ' + norm(f[3]); }); return d; });
                return loading;
            }
            var G = window.WiboGL = { items: [], name: name, link: link, esc: esc };
            // swap: same food type, low GI (<= 55) and lower than the food, at least half its carbs; measured GI first,
            // then the closest carbohydrate content (a like-for-like replacement, e.g. white rice -> pasta)
            G.swap = function (f) {
                if (!data || f[6] === null) return null;
                var best = null, bestKey = null;
                data.forEach(function (c) {
                    if (c[11] !== f[11] || c[0] === f[0] || c[6] === null || c[6] > 55 || c[6] >= f[6] || c[8] < f[8] * 0.5) return;
                    var key = [c[7], Math.abs(c[8] - f[8])];
                    if (!best || key[0] < bestKey[0] || (key[0] === bestKey[0] && key[1] < bestKey[1])) { best = c; bestKey = key; }
                });
                return best;
            };
            G.hint = function () { box.hidden = false; box.innerHTML = '<li class="gl-msg">' + esc(S['empty']) + '</li>'; q.focus(); };
            function render() {
                if (!G.items.length) { list.innerHTML = '<p class="gl-empty">' + esc(S['empty']) + '</p>'; return; }
                list.innerHTML = G.items.map(function (it, i) {
                    return '<div class="gl-item">' + link(it.f) + '<label><input type="number" class="form-control" inputmode="decimal" min="1" max="2000" step="1" value="' +
                        it.g + '" data-i="' + i + '" aria-label="' + esc(S['grams']) + '"> g</label><button type="button" class="gl-remove" data-rm="' + i +
                        '" aria-label="' + esc(S['remove']) + '">×</button></div>';
                }).join('');
            }
            function add(f) {
                if (G.items.length >= 8) { box.hidden = false; box.innerHTML = '<li class="gl-msg">' + esc(S['max_items']) + '</li>'; return; }
                G.items.push({ f: f, g: f[9] || 100 }); render(); q.value = ''; box.hidden = true; box.innerHTML = '';
            }
            function search() {
                var t = norm(q.value.trim());
                if (t.length < 2) { box.hidden = true; return; }
                box.hidden = false;
                if (!data) box.innerHTML = '<li class="gl-msg">' + esc(S['loading']) + '</li>';
                load().then(function (d) {
                    if (norm(q.value.trim()) !== t) return;
                    var hits = d.filter(function (f) { return f.k.indexOf(t) >= 0; })
                        .sort(function (a, b) { return (norm(name(a)).indexOf(t) === 0 ? 0 : 1) - (norm(name(b)).indexOf(t) === 0 ? 0 : 1) || name(a).length - name(b).length; })
                        .slice(0, 8);
                    box.innerHTML = hits.length ? hits.map(function (f) {
                        return '<li><button type="button" data-id="' + f[0] + '">' + esc(name(f)) + '</button></li>'; }).join('')
                        : '<li class="gl-msg">' + esc(S['no_match']) + '</li>';
                });
            }
            q.addEventListener('focus', load); q.addEventListener('input', search);
            q.addEventListener('keydown', function (e) {
                if (e.key !== 'Enter') return;
                var first = box.querySelector('button[data-id]');
                if (first) { e.preventDefault(); first.click(); }
            });
            box.addEventListener('click', function (e) {
                var b = e.target.closest('button[data-id]'); if (!b) return;
                var id = +b.getAttribute('data-id'); add(data.filter(function (f) { return f[0] === id; })[0]);
            });
            list.addEventListener('input', function (e) {
                var i = e.target.getAttribute('data-i'); if (i === null) return;
                var g = parseFloat(String(e.target.value).replace(',', '.')); if (g > 0) G.items[+i].g = g;
            });
            list.addEventListener('click', function (e) {
                var b = e.target.closest('button[data-rm]'); if (!b) return;
                G.items.splice(+b.getAttribute('data-rm'), 1); render();
            });""",
}
import hashlib  # noqa: E402
FORMULAS_VER = hashlib.sha1((ROOT / 'js' / 'calc-formulas.js').read_bytes()).hexdigest()[:8]
TDEE_UI = {l: next(c for c in CALCS if c['key'] == 'tdee')['content'][l]['ui'] for l in ALL_LANGS}


def write_gl_data():
    """data/gl-foods.json for the glycemic load tool (published foods only); returns its short hash for ?v=."""
    from calc_nutrition import gl_foods
    raw = json.dumps(gl_foods(), ensure_ascii=False, separators=(',', ':'))
    path = ROOT / 'data' / 'gl-foods.json'
    if not path.exists() or path.read_text(encoding='utf-8') != raw:
        path.write_text(raw, encoding='utf-8', newline='\n')
    return hashlib.sha1(raw.encode('utf-8')).hexdigest()[:8]


GL_VER = write_gl_data()


def script(calc, lang):
    w = calc['content'][lang]['ui']
    if calc['key'] in NEW_TOOLS:      # every string of the tool (links resolved for this language)
        strings = {k: (render_body(v, lang) if '{' in v else v) for k, v in w.items() if isinstance(v, str)}
    else:
        strings = {k: v for k, v in w.items() if k.startswith(('st_', 'tip', 'cups', 'ok_'))}
    locale = {'ar': 'en-US', 'en': 'en-GB', 'nl': 'nl-NL', SV: 'sv-SE'}[lang]
    date_locale = {'ar': 'ar-u-nu-latn', 'en': 'en-GB', 'nl': 'nl-NL', SV: 'sv-SE'}[lang]
    formulas = (f'    <script src="/js/calc-formulas.js?v={FORMULAS_VER}" defer></script>\n'
                if calc['key'] in NEW_TOOLS + ('tdee',) else '')
    init = INIT.get(calc['key'], '')
    if calc['key'] == 'gl':
        init = (init.replace('{NAME_COL}', str({'ar': 2, 'en': 3, 'nl': 4, SV: 5}[lang]))
                .replace('{PREFIX}', '' if lang == 'ar' else '/' + lang).replace('{GL_VER}', GL_VER))
    return f'''{formulas}    <script>
        (function () {{
            var S = {json.dumps(strings, ensure_ascii=False)}, DATE_LOCALE = '{date_locale}';
            function next(band) {{ var n = document.getElementById('r_next'); if (n) n.innerHTML = S['nx_' + band] || ''; }}
            function val(id) {{ var v = parseFloat(String(document.getElementById(id).value).replace(',', '.')); return v > 0 ? v : 0; }}
            function set(id, text) {{ var el = document.getElementById(id); if (el) el.textContent = text; }}
            function fmt(n, d) {{ return n.toLocaleString('{locale}', {{ minimumFractionDigits: d, maximumFractionDigits: d }}); }}
            function pill(text, cls) {{ var p = document.getElementById('r_pill'); if (p) {{ p.textContent = text; p.className = 'result-status-pill ' + cls; }} }}
            function run() {{{LOGIC[calc["key"]]}
            }}{init}
            var form = document.getElementById('calcForm');
            form.addEventListener('submit', function (e) {{
                e.preventDefault();
                if (!form.reportValidity()) return;
                if (run()) {{ var v = document.getElementById('resultView'); v.classList.add('active'); v.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }}); }}
            }});
        }})();
    </script>'''


def build(calc, lang):
    t, u, c = T[lang], ui(lang), calc['content'][lang]
    urls = {l: page_url(calc, l) for l in langs_of(calc)}
    hub = link('/calculators.html', lang)

    faq_schema = {"@type": "FAQPage", "@id": urls[lang] + '#faq', "inLanguage": lang,
                  "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}}
                                 for q, a in c['faq']]}
    page_schema = {
        "@type": "MedicalWebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": c['title'],
        "headline": c['h1'],
        "description": c['desc'],
        "inLanguage": lang,
        "datePublished": calc['published'],
        "dateModified": calc['modified'],
        "lastReviewed": calc['modified'],
        "medicalAudience": [{"@type": "Patient"}],
        "about": [{"@type": "MedicalCondition" if a.get('condition') else "Thing", "name": a['name']} for a in c['about']],
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "author": {"@type": "Organization", "name": "WiBo Health", "url": SITE},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "citation": [{"@type": "CreativeWork", "name": r} for r in calc['references']],
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": t['hub'], "item": SITE + hub},
            {"@type": "ListItem", "position": 3, "name": c['crumb'], "item": urls[lang]}]},
    }
    schema = {"@context": "https://schema.org", "@graph": [page_schema, faq_schema]}

    nav = site_nav(lang, active='/calculators.html')
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(calc, l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}" title="{NAMES[l]}" aria-label="{NAMES[l]}">{l.upper()}</a>'
        for l in ('ar', 'nl', 'en', SV) if l in urls)
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in ALL_LANGS if l in urls)
    calc_nav = ''.join(f'<a href="{page_url(o, lang, absolute=False)}"{" class=\"current\" aria-current=\"page\"" if o is calc else ""}>'
                       f'<i class="fas {o["icon"]}" aria-hidden="true"></i> {esc(o["content"][lang]["short"])}</a>' for o in CALCS)
    faq_html = ''.join(f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in c['faq'])
    related = ''.join(f'<a class="related-card" href="{page_url(o, lang, absolute=False)}"><i class="fas {o["icon"]}" aria-hidden="true"></i>'
                      f'<strong>{esc(o["content"][lang]["short"])}</strong><span>{esc(o["content"][lang]["blurb"])}</span></a>'
                      for o in CALCS if o is not calc)
    related += (f'<a class="related-card" href="{link("/foods.html", lang)}"><i class="fas fa-apple-whole" aria-hidden="true"></i>'
                f'<strong>{esc(t["foods_title"])}</strong><span>{esc(t["foods_blurb"])}</span></a>')
    refs_html = ''.join(f'<li>{esc(r)}</li>' for r in calc['references'])
    items = [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/calculators.html', t['hub']), ('/#articles', t['footer_articles']),
             ('/methodology.html', u['methodology']), ('/partners.html', u['partners']), ('/privacy.html', u['privacy'])]
    if lang == SV:                                       # the Swedish about, contact and legal pages
        items = [('/', u['nav'][0]), ('/calculators.html', t['hub']), ('/#articles', t['footer_articles']),
                 ('/about.html', 'Om oss'), ('/contact.html', 'Kontakt'), ('/privacy.html', 'Integritetspolicy'),
                 ('/terms.html', 'Användarvillkor'), ('/sv/medicinsk-ansvarsfriskrivning.html', 'Medicinsk ansvarsfriskrivning')]
    footer_links = ' <span>•</span> '.join(f'<a href="{link(p, lang)}">{label}</a>' for p, label in items)

    main = f'''    <main class="page-wrapper food-page article-page calc-page">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{link('/', lang)}">{u["home"]}</a> › <a href="{hub}">{t["hub"]}</a> › <span>{esc(c["crumb"])}</span>
            </nav>
            <span class="group-chip">{esc(c["cat"])}</span>
            <h1>{esc(c["h1"])}</h1>
            <div class="article-meta"><span><i class="fas fa-user-shield" aria-hidden="true"></i> {t["reviewed"]}</span><span><i class="fas fa-book-medical" aria-hidden="true"></i> {esc(calc["badge"])}</span></div>
            <p class="lead">{c["lead"]}</p>
            <nav class="calc-nav" aria-label="{esc(t["hub"])}">{calc_nav}</nav>

            {widget(calc, lang)}

{render_body(c["body"], lang)}

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>{t["faq"]}</span></h2>
            <div class="faq-list">{render_body(faq_html, lang)}</div>

            <h2 class="section-title"><i class="fas fa-calculator"></i> <span>{t["related"]}</span></h2>
            <div class="related-grid">{related}</div>

            <section class="boodi-funnel-card">
                <div><h2>{t["boodi_title"]}</h2><p>{t["boodi_text"]}</p></div>
                <a href="{link('/boodi.html', lang)}" class="funnel-btn"><i class="fas fa-barcode" aria-hidden="true"></i> {t["boodi_cta"]}</a>
            </section>

            <h2 class="section-title"><i class="fas fa-book-medical"></i> <span>{t["refs"]}</span></h2>
            <ol class="ref-list">{refs_html}</ol>
            <p class="disclaimer-box">{c["disclaimer"]}</p>
        </article>
    </main>
'''
    return shell(lang, title=c['title'], desc=c['desc'], urls=urls, schema=schema, nav=nav, lang_links=lang_links,
                 hreflang=hreflang, footer_links=footer_links, main=main, scripts=script(calc, lang))


def shell(lang, *, title, desc, urls, schema, nav, lang_links, hreflang, footer_links, main, scripts=''):
    """The page around `main`: head (SEO, schema, styles), header, footer; shared by the calculators and the hub."""
    t, u = T[lang], ui(lang)
    c = dict(title=title, desc=desc)
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{t["dir"]}" data-theme="dark">
<head>
{GA_TAG}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(c["title"])}</title>
    <meta name="description" content="{esc(c["desc"])}">
    <link rel="canonical" href="{urls[lang]}">
{hreflang}
    <link rel="alternate" hreflang="x-default" href="{urls['en']}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="WiBo Health">
    <meta property="og:title" content="{esc(c["title"])}">
    <meta property="og:description" content="{esc(c["desc"])}">
    <meta property="og:url" content="{urls[lang]}">
    <meta property="og:image" content="{SITE}/images/icon-512.png">
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL', sv='sv_SE')[lang]}">
    <meta name="twitter:card" content="summary">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=4)}
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"></noscript>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#070806">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/icon-192.png">
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
    <!-- Theme boot: one theme for the whole site (saved choice, else the OS setting), set before the first paint -->
    <script>(function(h){{var t;try{{t=localStorage.getItem('wibo_theme')}}catch(e){{}}if(t!=='dark'&&t!=='light'){{t=window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';try{{localStorage.setItem('wibo_theme',t)}}catch(e){{}}}}h.setAttribute('data-theme',t)}})(document.documentElement);</script>
    <style>html.theme-transitioning,html.theme-transitioning *,html.theme-transitioning *::before,html.theme-transitioning *::after{{transition:none!important;animation-duration:0s!important}}</style>
    <script>document.addEventListener('click',function(e){{var t=e.target&&e.target.closest&&e.target.closest('.theme-toggle,.theme-toggle-btn,#themeToggle,#themeToggleBtn,#darkModeToggle,[onclick*="toggleTheme"]');if(!t)return;var h=document.documentElement;h.classList.add('theme-transitioning');cancelAnimationFrame(window.__tsw);window.__tsw=requestAnimationFrame(function(){{window.__tsw=requestAnimationFrame(function(){{h.classList.remove('theme-transitioning')}})}})}},true);</script>
    <style>
{BASE_CSS}{PAGE_CSS}{ARTICLE_CSS}{CALC_CSS}    </style>
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

{main}
    <footer>
        <div class="footer-links">{footer_links}</div>
        <p>{u["footer_rights"]}</p>
    </footer>

{scripts}
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


HUB_MODIFIED = '2026-11-23'   # last change to the hub page


def hub_url(lang, absolute=True):
    path = '/calculators.html' if lang == 'ar' else f'/{lang}/calculators.html'
    return SITE + path if absolute else path


def build_hub(lang):
    """calculators.html in `lang`: the tools grouped in sections (scripts/calculator_hub.py); each card links its page."""
    t, u, h = T[lang], ui(lang), HUB[lang]
    urls = {l: hub_url(l) for l in ALL_LANGS}
    tools = [c for c in CALCS if lang in langs_of(c)]
    sections = [(cat, [c for c in tools if c.get('category', 'body') == cat]) for cat in CATEGORIES]
    sections = [(cat, items) for cat, items in sections if items]
    tabs = ''.join(f'<a href="#cat-{cat}">{esc(h["tabs"][cat])}</a>' for cat, _ in sections)
    body = ''
    for cat, items in sections:
        cards = ''.join(
            f'<a class="hub-card" href="{page_url(c, lang, absolute=False)}"><i class="fas {c["icon"]}" aria-hidden="true"></i>'
            f'<strong>{esc(c["content"][lang]["short"])}</strong><span>{esc(c["content"][lang]["blurb"])}</span>'
            f'<em>{esc(h["open"])} →</em></a>' for c in items)
        body += (f'<section class="hub-section" id="cat-{cat}"><h2 class="section-title">{esc(h["tabs"][cat])}</h2>'
                 f'<div class="hub-grid">{cards}</div></section>\n')
    related = ''.join(f'<a class="related-card" href="{link(p, lang)}"><i class="fas fa-link" aria-hidden="true"></i>'
                      f'<strong>{esc(n)}</strong><span>{esc(d)}</span></a>' for p, n, d in h['links'])
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": urls[lang] + '#webpage', "url": urls[lang], "name": h['title'],
         "description": h['desc'], "inLanguage": lang, "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": page_url(c, lang), "name": c['content'][lang]['short']}
             for i, c in enumerate([c for _, items in sections for c in items])]},
         "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + link('/', lang)},
             {"@type": "ListItem", "position": 2, "name": h['h1'], "item": urls[lang]}]}}]}
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{hub_url(l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}" title="{NAMES[l]}" aria-label="{NAMES[l]}">{l.upper()}</a>' for l in ('ar', 'nl', 'en', SV))
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in ALL_LANGS)
    main = f'''    <main class="page-wrapper food-page article-page calc-page calc-hub">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb"><a href="{link('/', lang)}">{u["home"]}</a> › <span>{esc(h["h1"])}</span></nav>
            <h1>{esc(h["h1"])}</h1>
            <p class="lead">{esc(h["intro"])}</p>
            <nav class="hub-tabs" aria-label="{esc(h["h1"])}">{tabs}</nav>
{body}
            <h2 class="section-title"><i class="fas fa-link"></i> <span>{esc(h["related"])}</span></h2>
            <div class="related-grid">{related}</div>
            <p class="small-print">{esc(h["note"])}</p>
        </article>
    </main>
'''
    page = shell(lang, title=h['title'], desc=h['desc'], urls=urls, schema=schema, nav=site_nav(lang, active='/calculators.html'),
                 lang_links=lang_links, hreflang=hreflang, footer_links=footer_links_of(lang), main=main)
    return page.replace('    </style>\n    <link rel="stylesheet" href="/css/unified-header.css">',
                        HUB_CSS + '    </style>\n    <link rel="stylesheet" href="/css/unified-header.css">', 1)


def footer_links_of(lang):
    t, u = T[lang], ui(lang)
    items = [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/calculators.html', t['hub']), ('/#articles', t['footer_articles']),
             ('/methodology.html', u['methodology']), ('/partners.html', u['partners']), ('/privacy.html', u['privacy'])]
    if lang == SV:
        items = [('/', u['nav'][0]), ('/calculators.html', t['hub']), ('/#articles', t['footer_articles']),
                 ('/about.html', 'Om oss'), ('/contact.html', 'Kontakt'), ('/privacy.html', 'Integritetspolicy'),
                 ('/terms.html', 'Användarvillkor'), ('/sv/medicinsk-ansvarsfriskrivning.html', 'Medicinsk ansvarsfriskrivning')]
    return ' <span>•</span> '.join(f'<a href="{link(p, lang)}">{label}</a>' for p, label in items)


def main():
    for lang in ALL_LANGS:                               # the hub (calculators.html) in every language
        out = (ROOT if lang == 'ar' else ROOT / lang) / 'calculators.html'
        out.write_text(mark_english_links(build_hub(lang), lang), encoding='utf-8', newline='\n')
    for lang in ALL_LANGS:
        out_dir = ROOT if lang == 'ar' else ROOT / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        for calc in CALCS:
            if lang in langs_of(calc):
                (out_dir / f'{calc["slug"]}.html').write_text(mark_english_links(build(calc, lang), lang), encoding='utf-8', newline='\n')

    block = []
    for lang in ALL_LANGS:                               # the hub
        block += ['  <url>', f'    <loc>{hub_url(lang)}</loc>', f'    <lastmod>{HUB_MODIFIED}</lastmod>', '    <priority>0.9</priority>']
        block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{hub_url(l)}"/>' for l in ALL_LANGS]
        block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{hub_url("en")}"/>', '  </url>']
    for calc in CALCS:
        for lang in langs_of(calc):
            block += ['  <url>', f'    <loc>{page_url(calc, lang)}</loc>', f'    <lastmod>{calc["modified"]}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.9</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(calc, l)}"/>' for l in langs_of(calc)]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(calc, "en")}"/>', '  </url>']
    replace_sitemap_block('CALCULATOR-PAGES', block)
    print(f'calculator pages written: {sum(len(langs_of(c)) for c in CALCS)} ({len(CALCS)} calculators, '
          f'{sum(SV in langs_of(c) for c in CALCS)} with Swedish)')


if __name__ == '__main__':
    main()
