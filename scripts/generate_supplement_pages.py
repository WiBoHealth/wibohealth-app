"""Generate static, crawlable supplement pages in three languages, plus Swedish for the supplements in supplement_sv.PUBLISH.

    python scripts/generate_supplement_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    supplements/<slug>.html       Arabic (x-default)
    en/supplements/<slug>.html    English
    nl/supplements/<slug>.html    Dutch
    sv/supplements/<slug>.html    Swedish (supplement_sv.PUBLISH; copy translated from the approved data in supplement_sv.py)
    js/supplement-pages.js        slugs that have a static page (used by the supplements.html modal)
    sitemap.xml                   block (replaced in place) between <!-- SUPPLEMENT-PAGES:START --> and <!-- SUPPLEMENT-PAGES:END -->

Source: js/supplements-data.js, plus per-language search snippets (title / desc) in
scripts/supplement_pages_overrides.json. Only records that carry `references` (the clinically vetted ones) get a page.
Content is attributed to the published sources (EFSA / NIH / PubMed), never to a named reviewer, and uses
structure/function wording only. Design system, header and footer come from generate_food_pages.py.
"""
import hashlib
import json
import re
from pathlib import Path

from generate_food_pages import (BASE_CSS, LOGO_SVG, SITE, LANGS, ALL_LANGS, SV, UI, any_link, dir_url, esc, nav_html,
                                 replace_sitemap_block, site_link)
import supplement_sv as SSV

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

T = {
    'ar': dict(
        dir='rtl', title='{name}: الجرعة والفوائد والتداخلات الدوائية | WiBo Health',
        desc='{name}: {desc} الجرعة الموصى بها: {dose}. التحذيرات والتداخلات الدوائية وفق EFSA وNIH.',
        guide='دليل المكملات', role='الدور الوظيفي والفوائد', dose='الجرعة وطريقة الاستخدام',
        rec='الجرعة الموصى بها', forms='أفضل الأشكال المتوفرة', timing='أفضل وقت للاستخدام', freq='التكرار', warnings='تحذيرات مهمة',
        inter='التداخلات الدوائية', sources_food='مصادر غذائية طبيعية', refs='المراجع العلمية', related='مكملات ذات صلة', open_guide='عرض في دليل المكملات',
        sources='📚 المصادر والأبحاث المنشورة: الهيئة الأوروبية لسلامة الأغذية (EFSA) • المعاهد الوطنية للصحة (NIH - ODS) • قواعد بيانات PubMed / Cochrane',
        updated='آخر تحديث للمحتوى: {date} · المحتوى مستند إلى المصادر والأبحاث المنشورة (EFSA / NIH / PubMed)',
        disclaimer='⚖️ إخلاء مسؤولية طبي: المعلومات والبيانات الواردة هنا هي لأغراض التثقيف الصحي والإرشاد الغذائي فقط، ولا تُعتبر تشخيصاً طبياً ولا تُغني بأي حال عن الاستشارة الطبية المباشرة من طبيبك أو الصيدلي. استشر طبيبك دائماً قبل البدء بأي مكمل، خصوصاً في حالات الحمل والرضاعة أو عند استخدام أدوية مزمنة.',
        date='17 أكتوبر 2026', footer_supp='دليل المكملات'),
    'en': dict(
        dir='ltr', title='{name}: Dosage, Benefits & Drug Interactions | WiBo Health',
        desc='{name}: {desc} Recommended dose: {dose}. Warnings and drug interactions based on EFSA and NIH.',
        guide='Supplements Guide', role='Function & benefits', dose='Dosage & how to use',
        rec='Recommended dose', forms='Best forms to choose', timing='Best time to take', freq='Frequency', warnings='Important warnings',
        inter='Drug interactions', sources_food='Natural food sources', refs='Scientific references', related='Related supplements', open_guide='View in the supplements guide',
        sources='📚 Published sources and research: European Food Safety Authority (EFSA) • National Institutes of Health (NIH - ODS) • PubMed / Cochrane databases',
        updated='Content last updated: {date} · Based on published sources and research (EFSA / NIH / PubMed)',
        disclaimer='⚖️ Medical disclaimer: The information and data provided here are for health education and nutritional guidance only. They are not a medical diagnosis and never replace a direct consultation with your doctor or pharmacist. Always consult your doctor before starting any supplement, especially during pregnancy or breastfeeding or when taking long-term medication.',
        date='17 October 2026', footer_supp='Supplements Guide'),
    'nl': dict(
        dir='ltr', title='{name}: dosering, voordelen en interacties | WiBo Health',
        desc='{name}: {desc} Aanbevolen dosis: {dose}. Waarschuwingen en interacties met medicijnen volgens EFSA en NIH.',
        guide='Supplementengids', role='Functie & voordelen', dose='Dosering & gebruik',
        rec='Aanbevolen dosis', forms='Beste vormen om te kiezen', timing='Beste moment van inname', freq='Frequentie', warnings='Belangrijke waarschuwingen',
        inter='Interacties met medicijnen', sources_food='Natuurlijke voedingsbronnen', refs='Wetenschappelijke bronnen', related='Verwante supplementen', open_guide='Bekijk in de supplementengids',
        sources='📚 Gepubliceerde bronnen en onderzoek: Europese Autoriteit voor Voedselveiligheid (EFSA) • National Institutes of Health (NIH - ODS) • PubMed / Cochrane-databanken',
        updated='Inhoud laatst bijgewerkt: {date} · Gebaseerd op gepubliceerde bronnen en onderzoek (EFSA / NIH / PubMed)',
        disclaimer='⚖️ Medische disclaimer: De informatie en gegevens hier zijn uitsluitend bedoeld voor gezondheidsvoorlichting en voedingsadvies. Ze vormen geen medische diagnose en vervangen nooit een direct consult bij je behandelend arts of apotheker. Overleg altijd met je arts voordat je met een supplement begint, vooral tijdens zwangerschap of borstvoeding of bij langdurig medicijngebruik.',
        date='17 oktober 2026', footer_supp='Supplementengids'),
}
T[SV] = SSV.UI
SUF = {'ar': '', 'en': 'En', 'nl': 'Nl'}
NAME = {'ar': 'name', 'en': 'englishName', 'nl': 'nameNl'}



# --- back button and quick search, shared with generate_directory_pages.py ----------------------------------------------
# where "back" goes when the reader did not come from the guide or an index: the guide in the page language
# (Swedish has no interactive guide: the Swedish index)
GUIDE_URL = {'ar': '/supplements.html', 'en': '/supplements.html?lang=en', 'nl': '/supplements.html?lang=nl',
             SV: '/sv/supplements/index.html'}
BACK = {'ar': 'العودة لدليل المكملات', 'en': 'Back to supplements', 'nl': 'Terug naar supplementengids',
        SV: 'Tillbaka till kosttillskottsguiden'}
SEARCH = {
    'ar': ('ابحث عن أي مكمل: عربي، English، Nederlands، Svenska', 'لا يوجد مكمل بهذا الاسم'),
    'en': ('Search any supplement: Arabic, English, Nederlands, Svenska', 'No supplement found'),
    'nl': ('Zoek een supplement: Arabisch, Engels, Nederlands, Zweeds', 'Geen supplement gevonden'),
    SV: ('Sök kosttillskott: arabiska, engelska, nederländska, svenska', 'Inget kosttillskott hittades'),
}


def asset_ver(name):
    return hashlib.sha1((ROOT / 'js' / name).read_bytes()).hexdigest()[:8]


def search_html(lang):
    """Quick search box (js/supplement-search.js); its names load on first use."""
    ph, none = SEARCH[lang]
    return (f'<div class="supp-search" data-lang="{lang}" data-none="{esc(none)}" '
            f'data-src="/js/supplement-search-data.js?v={asset_ver("supplement-search-data.js")}">'
            f'<i class="fas fa-magnifying-glass" aria-hidden="true"></i>'
            f'<input type="search" placeholder="{esc(ph)}" aria-label="{esc(ph)}" autocomplete="off">'
            f'<ul class="supp-search-results" hidden></ul></div>')


def search_script():
    return f'<script src="/js/supplement-search.js?v={asset_ver("supplement-search.js")}" defer></script>'


SEARCH_CSS = """
        .supp-search { position: relative; flex: 1 1 260px; min-width: 0; margin: 0 0 12px; }
        .supp-search > i { position: absolute; top: 50%; transform: translateY(-50%); inset-inline-start: 14px; color: var(--text-muted); pointer-events: none; }
        .supp-search input { width: 100%; box-sizing: border-box; padding: 10px 14px; padding-inline-start: 40px; border-radius: 999px;
            border: 1px solid var(--border-color); background: var(--bg-input); color: var(--text-main); font: inherit; font-size: 0.92rem; }
        .supp-search input:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px var(--primary-glow); }
        .supp-search-results { position: absolute; z-index: 20; inset-inline: 0; top: calc(100% + 6px); margin: 0; padding: 6px; list-style: none;
            background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 14px; box-shadow: var(--shadow); max-height: 320px; overflow-y: auto; }
        .supp-search-results a { display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 10px; color: var(--text-main);
            text-decoration: none; font-weight: 700; font-size: 0.9rem; }
        .supp-search-results a:hover, .supp-search-results a:focus { background: var(--primary-glow); }
        .supp-search-results a span { font-size: 20px; line-height: 1; }
        .supp-search-results .none { padding: 8px 10px; color: var(--text-muted); font-size: 0.88rem; }
"""


# --- comparison on the supplement indexes (js/supplement-compare.js), shared with generate_directory_pages.py ----------
COMPARE_HINT = {
    'ar': '⚖️ قارن بين المكملات واكتشف مدى التوافق والتعارض بينها (علّم على مكملين أو أكثر)',
    'en': '⚖️ Compare supplements: check compatibility & interactions (select 2 or more)',
    'nl': '⚖️ Vergelijk supplementen: bekijk compatibiliteit en interacties',
    SV: '⚖️ Jämför kosttillskott och se kompatibilitet och interaktioner (välj 2 eller fler)',
}
COMPARE_UI = {
    'ar': dict(compare='قارن', clear='مسح', close='إغلاق', title='مقارنة المكملات', pick='اختر للمقارنة',
               hint='اختر مكملاً آخر على الأقل', max='يمكنك مقارنة 5 مكملات كحد أقصى',
               note='استشر طبيبك أو الصيدلي دائماً قبل الجمع بين عدة مكملات.'),
    'en': dict(compare='Compare', clear='Clear', close='Close', title='Supplement comparison', pick='Select to compare',
               hint='Select at least one more', max='You can compare up to 5 supplements',
               note='Always consult your doctor or pharmacist before combining several supplements.'),
    'nl': dict(compare='Vergelijk', clear='Wissen', close='Sluiten', title='Supplementen vergelijken', pick='Selecteer om te vergelijken',
               hint='Selecteer er nog minstens één', max='U kunt maximaal 5 supplementen vergelijken',
               note='Overleg altijd met je arts of apotheker voordat je meerdere supplementen combineert.'),
    SV: dict(compare='Jämför', clear='Rensa', close='Stäng', title='Jämförelse av kosttillskott', pick='Välj för att jämföra',
             hint='Välj minst ett till', max='Du kan jämföra högst 5 kosttillskott',
             note='Rådgör alltid med din läkare eller farmaceut innan du kombinerar flera kosttillskott.'),
}


# medical disclaimer and sources under the supplement indexes (approved texts, 2026-10-27)
DIR_DISCLAIMER = {
    'ar': '⚖️ إخلاء مسؤولية طبية: المعلومات الواردة في دليل المكملات مخصصة للتثقيف الصحي والتوجيه الغذائي فقط، ولا تُعد بديلاً '
          'عن استشارة الطبيب أو الصيدلي المختص. استشر دائماً مقدم الرعاية الصحية قبل استخدام أي مكمل، خاصة أثناء الحمل، الرضاعة، '
          'أو عند تناول أدوية مزمنة.',
    'en': '⚖️ Medical Disclaimer: The information in this supplement directory is for educational and nutritional guidance purposes '
          'only and does not substitute for professional medical advice, diagnosis, or treatment from a physician or pharmacist. '
          'Always consult a healthcare provider before starting any supplement, especially during pregnancy, nursing, or with '
          'ongoing medication.',
    'nl': '⚖️ Medische disclaimer: De informatie in deze gids is uitsluitend bedoeld voor educatieve doeleinden en vervangt geen '
          'professioneel medisch advies. Raadpleeg altijd een arts of apotheker.',
    SV: '⚖️ Medicinsk ansvarsfriskrivning: Informationen i kosttillskottsregistret är endast avsedd som allmän hälsoupplysning och '
        'kostvägledning och ersätter aldrig professionell medicinsk rådgivning eller diagnos från läkare eller farmaceut. Rådgör '
        'alltid med din vårdgivare innan du använder kosttillskott, särskilt vid graviditet, amning eller samtidig medicinering.',
}
DIR_SOURCES = {
    'ar': '📚 المصادر العلمية المعتمدة: تعتمد المراجعات السريرية للجرعات والتحذيرات على أبحاث منشورة من: هيئة سلامة الغذاء '
          'الأوروبية (EFSA)، معاهد الصحة الوطنية الأمريكية (NIH)، وقاعدة بيانات الأبحاث الطبية (PubMed).',
    'en': '📚 Scientific Sources: Clinical guidance on dosage, warnings, and interactions is based on published data from EFSA, NIH, '
          'and PubMed.',
    'nl': '📚 Wetenschappelijke bronnen: Gebaseerd op gepubliceerde gegevens van EFSA, NIH en PubMed.',
    SV: '📚 Vetenskapliga källor: Den kliniska informationen om dosering och varningar baseras på publicerade källor från EFSA, NIH '
        'och PubMed.',
}


def disclaimer_html(lang):
    return (f'<aside class="supp-disclaimer"><p>{esc(DIR_DISCLAIMER[lang])}</p>'
            f'<p>{esc(DIR_SOURCES[lang])}</p></aside>')


def compare_hint_html(lang):
    return f'<p class="supp-compare-hint">{esc(COMPARE_HINT[lang])}</p>'


def compare_pick_html(slug, lang):
    return f'<input type="checkbox" class="supp-pick" value="{slug}" aria-label="{esc(COMPARE_UI[lang]["pick"])}">'


def compare_shell_html(lang):
    """The bar that appears once a supplement is ticked, and the comparison window."""
    u, t = COMPARE_UI[lang], T[lang]
    labels = dict(u, rec=t['rec'], timing=t['timing'], freq=t['freq'], warnings=t['warnings'], inter=t['inter'])
    data_ui = esc(json.dumps(labels, ensure_ascii=False))
    src = f'/js/supplement-compare-{lang}.js?v={asset_ver(f"supplement-compare-{lang}.js")}'
    return (f'<div id="suppCompare" data-lang="{lang}" data-src="{src}" data-ui="{data_ui}">'
            f'<div class="supp-compare-bar" hidden><span class="hint">{esc(u["hint"])}</span>'
            f'<button type="button" class="go"><i class="fas fa-scale-balanced" aria-hidden="true"></i> {esc(u["compare"])} (<span class="n">0</span>)</button>'
            f'<button type="button" class="clear">{esc(u["clear"])}</button></div>'
            f'<div class="supp-compare-modal" role="dialog" aria-modal="true" aria-label="{esc(u["title"])}" hidden>'
            f'<div class="supp-compare-panel"><div class="supp-compare-head"><h2>{esc(u["title"])}</h2>'
            f'<button type="button" class="close" aria-label="{esc(u["close"])}"><i class="fas fa-xmark" aria-hidden="true"></i></button></div>'
            f'<div class="supp-compare-body"></div>'
            f'<p class="supp-compare-note"><i class="fas fa-user-doctor" aria-hidden="true"></i> {esc(u["note"])}</p></div></div></div>'
            f'<script src="/js/supplement-compare.js?v={asset_ver("supplement-compare.js")}" defer></script>')


COMPARE_CSS = """
        .supp-compare-hint { margin: 0 0 14px; padding: 10px 14px; border-radius: 14px; font-weight: 700; font-size: 0.92rem; line-height: 1.5;
            color: var(--text-main); background: linear-gradient(135deg, rgba(16, 185, 129, 0.14), rgba(14, 165, 233, 0.14));
            border: 1px solid rgba(16, 185, 129, 0.35); border-inline-start: 4px solid var(--primary); }
        .supplements-directory .dir-list li { position: relative; }
        .supp-pick { position: absolute; top: 7px; inset-inline-end: 7px; z-index: 2; width: 20px; height: 20px; margin: 0; cursor: pointer;
            appearance: none; -webkit-appearance: none; border-radius: 6px; border: 1.5px solid #fff; background: rgba(255, 255, 255, 0.92);
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.18); }
        .supp-pick:checked { background: #064e3b url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5'/%3E%3C/svg%3E") center / 14px no-repeat; }
        .supp-pick:focus-visible { outline: 3px solid #fff; outline-offset: 2px; }
        .supp-compare-bar { position: fixed; z-index: 1500; bottom: 18px; inset-inline: 0; margin: 0 auto; width: fit-content; max-width: calc(100% - 24px);
            display: flex; align-items: center; gap: 8px; padding: 8px 10px; border-radius: 999px; background: var(--bg-card);
            border: 1px solid var(--border-color); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25); }
        .supp-compare-bar[hidden] { display: none; }
        .supp-compare-bar .hint { font-size: 0.82rem; color: var(--text-muted); padding-inline: 6px; }
        .supp-compare-bar button { border: 0; border-radius: 999px; padding: 8px 16px; font: inherit; font-weight: 800; font-size: 0.9rem; cursor: pointer; }
        .supp-compare-bar .go { color: #fff; background: linear-gradient(135deg, #10b981, #0ea5e9); }
        .supp-compare-bar .go:disabled { opacity: 0.5; cursor: default; }
        .supp-compare-bar .clear { background: var(--bg-input); color: var(--text-main); }
        .supp-compare-modal { position: fixed; inset: 0; z-index: 2000; background: rgba(2, 6, 23, 0.6); display: flex; align-items: flex-start;
            justify-content: center; padding: 24px 12px; overflow-y: auto; }
        .supp-compare-modal[hidden] { display: none; }
        .supp-compare-panel { width: 100%; max-width: 1100px; background: var(--bg-card); color: var(--text-main); border-radius: 18px;
            border: 1px solid var(--border-color); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35); overflow: hidden; }
        .supp-compare-head { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 12px 16px; color: #fff;
            background: linear-gradient(135deg, #10b981, #0ea5e9); }
        .supp-compare-head h2 { margin: 0; font-size: 1.05rem; color: #fff; }
        .supp-compare-head .close { border: 0; background: rgba(255, 255, 255, 0.2); color: #fff; width: 34px; height: 34px; border-radius: 50%; cursor: pointer; font-size: 16px; }
        .supp-compare-scroll { overflow-x: auto; }
        .supp-compare-body table { width: 100%; border-collapse: collapse; font-size: 0.86rem; line-height: 1.55; }
        .supp-compare-body th, .supp-compare-body td { padding: 10px 12px; border-bottom: 1px solid var(--border-color); vertical-align: top;
            text-align: start; min-width: 170px; overflow-wrap: anywhere; }
        .supp-compare-body thead th { text-align: center; }
        .supp-compare-body thead th .ic { display: block; font-size: 26px; line-height: 1.2; }
        .supp-compare-body thead th a { color: var(--primary); font-weight: 800; text-decoration: none; }
        .supp-compare-body thead th small { display: block; color: var(--text-muted); font-weight: 600; }
        .supp-compare-body tbody th { min-width: 120px; color: var(--text-muted); font-weight: 800; white-space: nowrap; background: var(--bg-input);
            position: sticky; inset-inline-start: 0; z-index: 1; }          /* the row names stay in view while the table scrolls */
        @media (max-width: 600px) {
            .supp-compare-body tbody th { min-width: 0; white-space: normal; width: 92px; font-size: 0.8rem; }
            .supp-compare-body th, .supp-compare-body td { min-width: 150px; padding: 8px 10px; }
            .supp-compare-body tbody th { min-width: 92px; }
        }
        .supp-compare-body ul { margin: 0; padding-inline-start: 18px; }
        .supp-compare-body .loading { padding: 20px; text-align: center; }
        .supp-compare-note { margin: 0; padding: 12px 16px; font-size: 0.86rem; font-weight: 700; line-height: 1.55; color: var(--text-main);
            border-top: 1px solid var(--border-color); background: rgba(245, 158, 11, 0.1); }
        .supp-compare-note i { color: #f59e0b; margin-inline-end: 4px; }
        .supp-disclaimer { margin: 22px 0 4px; padding: 14px 18px; border-radius: 16px; border: 1px solid var(--border-color);
            background: var(--bg-input); display: grid; gap: 8px; }
        .supp-disclaimer p { margin: 0; font-size: 0.86rem; line-height: 1.7; color: var(--text-muted); overflow-wrap: anywhere; }
        .supp-disclaimer p:first-child { color: var(--text-main); }
        /* solid surfaces: the theme's card colours are see-through in dark mode */
        .supp-compare-panel, .supp-compare-bar { background: #ffffff; }
        .supp-compare-body tbody th { background: #f1f5f9; }
        .supp-compare-bar .clear { background: #f1f5f9; }
        html[data-theme="dark"] .supp-compare-panel, html[data-theme="dark"] .supp-compare-bar { background: #0f172a; }
        html[data-theme="dark"] .supp-compare-body tbody th, html[data-theme="dark"] .supp-compare-bar .clear { background: #1e293b; }
"""

def langs_of(slug):
    """Languages a supplement page exists in: ar/en/nl always, sv for the supplements in supplement_sv.PUBLISH."""
    return ALL_LANGS if slug in SSV.PUBLISH else LANGS


def field(s, key, lang):
    """A text field of the record in `lang`; Swedish comes from supplement_sv.COPY, with its approved Swedish warnings
    (legal status) first."""
    if lang != SV:
        return s.get(key + SUF[lang])
    value = SSV.COPY[s['slug']].get(key)
    return SSV.EXTRA_WARNINGS.get(s['slug'], []) + value if key == 'warnings' else value


def supp_name(s, lang):
    return SSV.NAMES[s['slug']] if lang == SV else (s[NAME[lang]] or s['name'])


def group_label(s, lang):
    return SSV.GROUP_LABELS[s['groupLabel']['en']] if lang == SV else s['groupLabel'][lang]

EXTRA_CSS = """
        .dose-table td:first-child { color: var(--text-muted); font-weight: 700; width: 38%; }
        .ref-list { margin: 10px 0 22px; padding-inline-start: 22px; display: grid; gap: 8px; }
        .ref-list li { color: var(--text-muted); font-size: 0.92rem; overflow-wrap: anywhere; }
        .guide-link { display: inline-flex; align-items: center; gap: 8px; margin: 4px 0 22px; padding: 10px 18px; border-radius: 30px;
            border: 1px solid var(--primary); color: var(--primary); font-weight: 800; text-decoration: none; }
        .guide-link:hover { background: var(--primary-glow); }
        /* related supplements: a long name moves the group label to its own line instead of pushing it off a phone screen */
        .alt-list a { flex-wrap: wrap; row-gap: 2px; min-width: 0; overflow-wrap: anywhere; }
        .alt-list a > span { white-space: normal; margin-inline-start: auto; text-align: end; }
        /* very long names and dose lines wrap on 320px screens instead of widening the page */
        .food-hero-text { min-width: 0; }
        .food-hero-text h1 { overflow-wrap: anywhere; }
        .dose-table { table-layout: fixed; }
        .dose-table td { overflow-wrap: anywhere; }
        .tip p, .lead { overflow-wrap: anywhere; hyphens: auto; }      /* long Dutch and Swedish compound words */
        /* back to the guide and quick search, above the breadcrumb */
        .supp-top { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 0 12px; }
        .supp-back { display: inline-flex; align-items: center; gap: 7px; margin: 0 0 12px; padding: 8px 14px; border-radius: 999px;
            border: 1px solid var(--primary-glow); background: var(--bg-input); color: var(--primary); font-size: 0.9rem; font-weight: 700;
            text-decoration: none; line-height: 1.3; white-space: nowrap; }
        .supp-back:hover { background: var(--primary); border-color: var(--primary); color: #fff; }
        .supp-back:focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }
"""

# the page styles the supplement markup is built on (not the food page styles, which changed with template v2)
_css = (ROOT / 'scripts' / 'supplement_page.css').read_text(encoding='utf-8')
SUPP_PAGE_CSS = _css[_css.index('*/\n') + 3:]


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


def clip_sentence(text, limit, longest=200):
    """Whole sentences of text that fit in limit (the first one may run to `longest`). A first sentence longer than
    that ends at its last clause break (; ، , : or an opening bracket) inside `longest`, with a full stop, so the
    snippet never stops mid-phrase."""
    text = ' '.join(text.split())
    sentences = re.split(r'(?<=[.!?؟])\s+', text)
    if len(sentences[0]) > longest:
        head = text[:longest]
        cut = max(head.rfind(c) for c in ';؛،,:(')
        return head[:cut].rstrip() + '.' if cut > 30 else clip(text, longest)
    out = sentences[0]
    for sentence in sentences[1:]:
        if len(out) + len(sentence) + 1 > limit:
            break
        out += ' ' + sentence
    return out


SNIPPETS = json.loads((ROOT / 'scripts' / 'supplement_pages_overrides.json').read_text(encoding='utf-8')).get(
    'supplements', {}) if (ROOT / 'scripts' / 'supplement_pages_overrides.json').exists() else {}


def build(s, lang, vetted):
    t, u = T[lang], UI[lang]
    L = lambda path: any_link(path, lang)              # Swedish: /sv/ pages where they exist, English elsewhere
    name = supp_name(s, lang)
    subtitle = s['englishName'] if lang != 'en' and s['englishName'] != name else ''
    desc_txt = field(s, 'summary', lang)
    dose = field(s, 'dosage', lang)
    title = t['title'].format(name=name)
    meta_desc = t['desc'].format(name=name, desc=clip_sentence(desc_txt, 110), dose=dose['recommended'])
    meta_desc = clip_sentence(meta_desc, 400, longest=400)     # whole sentences only: a long dose line drops the closing ones
    snip = SNIPPETS.get(s['slug'], {})
    title = snip.get('title', {}).get(lang) or title
    meta_desc = snip.get('desc', {}).get(lang) or meta_desc
    urls = {l: page_url(s['slug'], l) for l in langs_of(s['slug'])}
    guide_href = L('/supplements.html') + '#' + s['slug']

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": title,
        "description": meta_desc,
        "inLanguage": lang,
        # the supplement itself, from the same vetted fields the page shows
        "about": {"@type": "DietarySupplement", "name": s['englishName'], "alternateName": [s['name'], s['nameNl']],
                  "description": desc_txt,
                  "recommendedIntake": {"@type": "RecommendedDoseSchedule", "name": dose['recommended'],
                                        "frequency": dose['frequency']},
                  "safetyConsideration": ' '.join(w.rstrip('.') + '.' for w in field(s, 'warnings', lang)) + ' ' + field(s, 'interactions', lang)},
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "author": {"@type": "Organization", "name": "WiBo Health", "url": SITE},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "citation": [{"@type": "CreativeWork", "name": r} for r in s['references']],
        "lastReviewed": SSV.REVIEWED if lang == SV else s.get('reviewed', '2026-10-17'),
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + L('/')},
            {"@type": "ListItem", "position": 2, "name": t['guide'], "item": dir_url('supplements', lang)},
            {"@type": "ListItem", "position": 3, "name": name, "item": urls[lang]}]},
    }

    group = group_label(s, lang)
    related = [r for r in vetted if r['id'] != s['id'] and r['groupLabel']['ar'] == s['groupLabel']['ar']]
    related += [r for r in vetted if r['id'] != s['id'] and r not in related and r['category'] == s['category']]
    # on a Swedish page, a related supplement without a Swedish page opens in English
    rel_lang = lambda r: lang if lang in langs_of(r['slug']) else 'en'
    related_html = ''.join(
        f'<li><a href="{page_url(r["slug"], rel_lang(r), absolute=False)}">{esc(supp_name(r, rel_lang(r)))}'
        f'<span>{esc(group_label(r, rel_lang(r)))}</span></a></li>' for r in related[:4])

    if lang == SV:
        from generate_article_pages import nav as sv_nav
        nav = sv_nav(lang, active='/supplements.html')
    else:
        nav = nav_html(lang, active='/supplements.html')
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(s["slug"], l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}">{l.upper()}</a>'
        for l in ('ar', 'nl', 'en', SV) if l in urls)
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in urls)
    warnings_html = ''.join(f'<div class="tip warn"><p>{esc(w)}</p></div>' for w in field(s, 'warnings', lang))
    refs_html = ''.join(f'<li>{esc(r)}</li>' for r in s['references'])
    forms_txt = field(s, 'forms', lang)
    forms_html = (f'<h2 class="section-title"><i class="fas fa-capsules"></i> <span>{t["forms"]}</span></h2>'
                  f'<div class="tip-list"><div class="tip"><p>{esc(forms_txt)}</p></div></div>') if forms_txt else ''
    natural = field(s, 'naturalSources', lang)
    natural_html = (f'<h2 class="section-title"><i class="fas fa-seedling"></i> <span>{t["sources_food"]}</span></h2>'
                    f'<div class="tip-list"><div class="tip"><p>{esc(natural)}</p></div></div>') if natural else ''
    footer_links = ' <span>•</span> '.join(
        f'<a href="{href}">{label}</a>' for href, label in
        [(L('/'), u['nav'][0]), (dir_url('foods', lang, absolute=False), u['nav'][1]),
         (dir_url('supplements', lang, absolute=False), t['footer_supp']), (L('/methodology.html'), u['methodology']),
         (L('/partners.html'), u['partners']), (L('/privacy.html'), u['privacy'])])

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
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL', sv='sv_SE')[lang]}">
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
{BASE_CSS}{SUPP_PAGE_CSS}{EXTRA_CSS}{SEARCH_CSS}    </style>
    <link rel="stylesheet" href="/css/unified-header.css">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="{L('/')}" class="brand-link">
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
            <div class="supp-top">
                <a class="supp-back" href="{GUIDE_URL[lang]}" data-back><i class="fas {'fa-arrow-right' if lang == 'ar' else 'fa-arrow-left'}" aria-hidden="true"></i> {BACK[lang]}</a>
                {search_html(lang)}
            </div>
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{L('/')}">{u["home"]}</a> › <a href="{dir_url('supplements', lang, absolute=False)}">{t["guide"]}</a> › <span>{esc(name)}</span>
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
            {natural_html}
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>{t["warnings"]}</span></h2>
            <div class="tip-list">{warnings_html}</div>

            <h2 class="section-title"><i class="fas fa-pills"></i> <span>{t["inter"]}</span></h2>
            <div class="tip-list"><div class="tip"><p>{esc(field(s, "interactions", lang))}</p></div></div>

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
        // Back: a reader who came from the guide or a supplement index goes back in history (same place in the list)
        document.addEventListener('click', function (e) {{
            var a = e.target.closest && e.target.closest('a[data-back]');
            if (!a || e.button || e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
            var ref = null;
            try {{ ref = new URL(document.referrer); }} catch (err) {{ return; }}
            if (ref.origin === location.origin && /^\\/(supplements(\\.html)?|((en|nl|sv)\\/)?supplements\\/index\\.html)$/.test(ref.pathname)
                    && history.length > 1) {{
                e.preventDefault();
                history.back();
            }}
        }});
    </script>
    {search_script()}
</body>
</html>
'''


def main():
    vetted = [s for s in load_supplements() if s.get('references')]
    # names in the four languages for the quick search of the static pages (js/supplement-search.js)
    (ROOT / 'js' / 'supplement-search-data.js').write_text(
        '// Generated by scripts/generate_supplement_pages.py - do not edit by hand.\n'
        '// [slug, Arabic, English, Dutch, Swedish (or null), icon] for js/supplement-search.js.\n'
        'window.SUPP_SEARCH = ' + json.dumps([[s['slug'], s['name'], s['englishName'], s['nameNl'],
                                                SSV.NAMES.get(s['slug']) if s['slug'] in SSV.PUBLISH else None, s.get('icon') or '💊']
                                               for s in vetted], ensure_ascii=False, separators=(',', ':')) + ';\n',
        encoding='utf-8', newline='\n')

    # per-language data of the comparison on the supplement indexes (js/supplement-compare.js)
    for lang in ALL_LANGS:
        rows = {s['slug']: [supp_name(s, lang), s.get('icon') or '💊', group_label(s, lang), field(s, 'dosage', lang)['recommended'],
                            field(s, 'dosage', lang)['timing'], field(s, 'dosage', lang)['frequency'], field(s, 'warnings', lang),
                            field(s, 'interactions', lang)]
                for s in vetted if lang in langs_of(s['slug'])}
        (ROOT / 'js' / f'supplement-compare-{lang}.js').write_text(
            '// Generated by scripts/generate_supplement_pages.py - do not edit by hand.\n'
            '// slug -> [name, icon, area, recommended dose, timing, frequency, [warnings], interactions] for js/supplement-compare.js.\n'
            'window.SUPP_COMPARE = ' + json.dumps(rows, ensure_ascii=False, separators=(',', ':')) + ';\n',
            encoding='utf-8', newline='\n')

    missing = SSV.PUBLISH - {s['slug'] for s in vetted}
    assert not missing, f'supplement_sv.PUBLISH: no vetted record for {missing}'
    written = 0
    for lang in ALL_LANGS:
        out_dir = ROOT / ('supplements' if lang == 'ar' else f'{lang}/supplements')
        out_dir.mkdir(parents=True, exist_ok=True)
        pages = [s for s in vetted if lang in langs_of(s['slug'])]
        keep = {f'{s["slug"]}.html' for s in pages} | {'index.html'}   # index.html: generate_directory_pages.py
        for old in out_dir.glob('*.html'):          # a supplement that lost its page must not linger
            if old.name not in keep:
                old.unlink()
        for s in pages:
            (out_dir / f'{s["slug"]}.html').write_text(build(s, lang, vetted), encoding='utf-8', newline='\n')
            written += 1

    (ROOT / 'js' / 'supplement-pages.js').write_text(
        '// Generated by scripts/generate_supplement_pages.py - do not edit by hand.\n'
        '// Slugs of supplements that have a static page (/supplements/<slug>.html, /en/supplements/..., /nl/supplements/...).\n'
        f'window.SUPP_PAGES = {json.dumps({s["slug"]: 1 for s in vetted}, separators=(",", ":"))};\n',
        encoding='utf-8', newline='\n')

    # approved Swedish names, so the search of supplements.html also finds a supplement by its Swedish name
    (ROOT / 'js' / 'supplement-names-sv.js').write_text(
        '// Generated by scripts/generate_supplement_pages.py - do not edit by hand.\n'
        '// Slug -> approved Swedish name (scripts/supplement_sv.py), for the search of supplements.html.\n'
        f'window.SUPP_NAMES_SV = {json.dumps({s["slug"]: SSV.NAMES[s["slug"]] for s in vetted if s["slug"] in SSV.PUBLISH}, ensure_ascii=False, separators=(",", ":"))};\n',
        encoding='utf-8', newline='\n')

    block = []
    for s in vetted:
        for lang in langs_of(s['slug']):
            lastmod = SSV.REVIEWED if lang == SV else s.get("reviewed", "2026-10-17")
            block += ['  <url>', f'    <loc>{page_url(s["slug"], lang)}</loc>', f'    <lastmod>{lastmod}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.6</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(s["slug"], l)}"/>' for l in langs_of(s['slug'])]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(s["slug"], "ar")}"/>', '  </url>']
    replace_sitemap_block('SUPPLEMENT-PAGES', block)
    print(f'supplement pages written: {written} ({len(vetted)} supplements x {len(LANGS)} languages, '
          f'{len(SSV.PUBLISH)} also in Swedish)')


if __name__ == '__main__':
    main()
