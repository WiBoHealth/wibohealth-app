"""Generate the standalone calculator pages (one page per calculator, three languages plus Swedish).

    python scripts/generate_calculator_pages.py

Output (re-running rebuilds everything):
    <slug>.html        Arabic (x-default), e.g. bmi-calculator.html
    en/<slug>.html     English
    nl/<slug>.html     Dutch
    sv/<slug>.html     Swedish (copy in calc_sv.py; links use generate_article_pages.link, so pages without a Swedish
                       version open in English)
    sitemap.xml        block between <!-- CALCULATOR-PAGES:START --> and <!-- CALCULATOR-PAGES:END -->

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
from generate_article_pages import EXTRA_CSS as ARTICLE_CSS, SV, UI_SV, link, nav as site_nav
from generate_food_pages import BASE_CSS, LOGO_SVG, PAGE_CSS, SITE, LANGS, UI, esc

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
BY_KEY = {c['key']: c for c in CALCS}
ALL_LANGS = LANGS + (SV,)
NAMES = {'ar': 'العربية', 'nl': 'Nederlands', 'en': 'English', SV: 'Svenska'}


def langs_of(calc):
    return tuple(l for l in ALL_LANGS if l in calc['content'])


def ui(lang):
    return UI_SV if lang == SV else UI[lang]

CALC_CSS = """
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


def food_url(slug, lang):
    lang = 'en' if lang == SV else lang      # no Swedish food pages yet: the English one
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
    else:  # whtr
        fields = field('f_waist', w['lbl_waist'], num('f_waist', w['ph_waist'], 40, 220, 0.5)) + \
                 field('f_height', w['lbl_height'], num('f_height', w['ph_height'], 90, 240, 0.5))
        result = (f'<div class="result-main"><div class="result-heading">{esc(w["res_heading"])}</div>'
                  '<div class="result-big-value" id="r_main">0.00</div><div class="result-status-pill" id="r_pill"></div></div>'
                  f'<div class="result-grid"><div class="breakdown-box"><div class="breakdown-label">{esc(w["target_label"])}</div>'
                  '<div class="breakdown-val" id="r_target">--</div></div>'
                  f'<div class="breakdown-box"><div class="breakdown-label">{esc(w["diff_label"])}</div>'
                  '<div class="breakdown-val" id="r_diff">--</div></div></div>')
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
                    <div class="clinical-note-box"><i class="fas fa-circle-info" aria-hidden="true"></i><span id="r_note"></span></div>
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
        var pG = Math.round(w * 1.8), pK = pG * 4, fK = Math.round(deficit * 0.25), fG = Math.round(fK / 9),
            cK = Math.max(0, deficit - pK - fK), cG = Math.round(cK / 4);
        set('r_main', fmt(Math.round(tdee), 0)); set('r_bmr', fmt(Math.round(bmr), 0) + ' kcal');
        set('r_deficit', fmt(deficit, 0) + ' kcal'); set('r_surplus', fmt(surplus, 0) + ' kcal');
        set('r_protein', pG + ' g'); set('r_protein_kcal', fmt(pK, 0) + ' kcal');
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
}


def script(calc, lang):
    w = calc['content'][lang]['ui']
    strings = {k: v for k, v in w.items() if k.startswith(('st_', 'tip', 'cups', 'ok_'))}
    locale = {'ar': 'en-US', 'en': 'en-GB', 'nl': 'nl-NL', SV: 'sv-SE'}[lang]
    return f'''    <script>
        (function () {{
            var S = {json.dumps(strings, ensure_ascii=False)};
            function val(id) {{ var v = parseFloat(String(document.getElementById(id).value).replace(',', '.')); return v > 0 ? v : 0; }}
            function set(id, text) {{ var el = document.getElementById(id); if (el) el.textContent = text; }}
            function fmt(n, d) {{ return n.toLocaleString('{locale}', {{ minimumFractionDigits: d, maximumFractionDigits: d }}); }}
            function pill(text, cls) {{ var p = document.getElementById('r_pill'); if (p) {{ p.textContent = text; p.className = 'result-status-pill ' + cls; }} }}
            function run() {{{LOGIC[calc["key"]]}
            }}
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
        f'hreflang="{l}" lang="{l}" title="{NAMES[l]}" aria-label="{NAMES[l]}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧'), (SV, '🇸🇪')) if l in urls)
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
    <link rel="alternate" hreflang="x-default" href="{urls['ar']}">
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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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

    <main class="page-wrapper food-page article-page calc-page">
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

    <footer>
        <div class="footer-links">{footer_links}</div>
        <p>{u["footer_rights"]}</p>
    </footer>

{script(calc, lang)}
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
    for lang in ALL_LANGS:
        out_dir = ROOT if lang == 'ar' else ROOT / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        for calc in CALCS:
            if lang in langs_of(calc):
                (out_dir / f'{calc["slug"]}.html').write_text(build(calc, lang), encoding='utf-8', newline='\n')

    sm_path = ROOT / 'sitemap.xml'
    sm = sm_path.read_text(encoding='utf-8')
    eol = '\r\n' if '\r\n' in sm else '\n'
    sm = re.sub(r'\s*<!-- CALCULATOR-PAGES:START -->.*?<!-- CALCULATOR-PAGES:END -->', '', sm, flags=re.S)
    block = ['  <!-- CALCULATOR-PAGES:START -->']
    for calc in CALCS:
        for lang in langs_of(calc):
            block += ['  <url>', f'    <loc>{page_url(calc, lang)}</loc>', f'    <lastmod>{calc["modified"]}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.9</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(calc, l)}"/>' for l in langs_of(calc)]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(calc, "ar")}"/>', '  </url>']
    block.append('  <!-- CALCULATOR-PAGES:END -->')
    sm = sm.replace('</urlset>', eol.join(block) + eol + '</urlset>', 1)
    sm_path.write_text(sm, encoding='utf-8', newline='')
    print(f'calculator pages written: {sum(len(langs_of(c)) for c in CALCS)} ({len(CALCS)} calculators, '
          f'{sum(SV in langs_of(c) for c in CALCS)} with Swedish)')


if __name__ == '__main__':
    main()
