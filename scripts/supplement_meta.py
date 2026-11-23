"""<title>, meta description and the dose comparison block of a supplement page (rule of 2026-11-23).

Titles 48-58 characters with the search words of each language (dosage, benefits, side effects), no brand.
Descriptions 125-155 characters: the approved summary, the recommended dose, warnings/interactions.
The comparison block puts the dose, timing and frequency of up to three related supplements (same group) next to
this one, each linking to its page. Only existing, approved fields are used; nothing new is claimed.
"""
import html
import re

TITLE_MIN, TITLE_MAX = 48, 58
DESC_MIN, DESC_MAX = 125, 155

TITLES = {
    'en': ['{n}: Dosage, Benefits & Side Effects Explained', '{n}: Dosage, Benefits & Side Effects',
           '{n}: Dose, Benefits & Side Effects', '{n}: Dosage & Side Effects', '{n}: Dosage & Benefits', '{n}: Dosage'],
    'nl': ['{n}: dosering, werking en bijwerkingen uitgelegd', '{n}: dosering, werking en bijwerkingen',
           '{n}: dosering en bijwerkingen', '{n}: dosering en werking', '{n}: dosering'],
    'sv': ['{n}: dosering, effekt och biverkningar förklarat', '{n}: dosering, effekt och biverkningar',
           '{n}: dosering och biverkningar', '{n}: dosering och effekt', '{n}: dosering'],
    'ar': ['{n}: الجرعة الصحيحة والفوائد والأعراض الجانبية', '{n}: الجرعة والفوائد والأعراض الجانبية',
           '{n}: الجرعة والأعراض الجانبية', '{n}: الجرعة والفوائد', '{n}: الجرعة'],
}
DOSE = {'en': 'Dose: {d}.', 'nl': 'Dosis: {d}.', 'sv': 'Dos: {d}.', 'ar': 'الجرعة: {d}.'}
TAILS = {
    'en': ['Warnings and drug interactions (EFSA, NIH).', 'Warnings and drug interactions.', 'Warnings inside.', ''],
    'nl': ['Waarschuwingen en interacties (EFSA, NIH).', 'Waarschuwingen en interacties.', 'Met waarschuwingen.', ''],
    'sv': ['Varningar och interaktioner (EFSA, NIH).', 'Varningar och interaktioner.', 'Med varningar.', ''],
    'ar': ['مع التحذيرات والتداخلات الدوائية (EFSA وNIH).', 'مع التحذيرات والتداخلات الدوائية.', 'مع التحذيرات.', ''],
}
ELLIPSIS = '…'


def _names(name):
    out = [name, re.sub(r'\s*\([^)]*\)', '', name).strip()]
    words = out[-1].split()
    out += [' '.join(words[:k]) for k in range(len(words) - 1, 0, -1)]
    return list(dict.fromkeys(n.rstrip(' ,،-–:') for n in out if n))


def title(lang, name):
    for nm in _names(name):
        for pat in TITLES[lang]:
            t = pat.format(n=nm)
            if TITLE_MIN <= len(t) <= TITLE_MAX:
                return t
    for nm in _names(name):                 # very short names: the longest pattern under the maximum
        for pat in TITLES[lang]:
            t = pat.format(n=nm)
            if len(t) <= TITLE_MAX:
                return t
    return TITLES[lang][-1].format(n=_names(name)[-1])[:TITLE_MAX]


def _clip(text, budget):
    """The summary cut to `budget` characters at a word boundary (whole sentence when it fits)."""
    text = ' '.join(text.split())
    if len(text) <= budget:
        return text
    for end in ('. ', '؛ ', '; ', ', ', '، '):
        i = text.rfind(end, 0, budget)
        if i > budget * 0.6:
            return text[:i + 1].rstrip(',،;؛') .rstrip() if end.startswith('.') else text[:i].rstrip() + ELLIPSIS
    cut = text[:budget - 1]
    cut = cut[:cut.rfind(' ')] if ' ' in cut else cut
    return cut.rstrip(' ,،;:') + ELLIPSIS


def desc(lang, name, summary, dose):
    """{name}: {summary} Dose: {dose}. {tail} - 125 to 155 characters."""
    dose = ' '.join(dose.split()).rstrip('.')
    for nm in _names(name):
        for tail in TAILS[lang]:
            for d in (dose, re.sub(r'\s*\([^)]*\)', '', dose)):
                fixed = f'{nm}: ' + ' ' + DOSE[lang].format(d=d) + (' ' + tail if tail else '')
                budget = DESC_MAX - len(fixed)
                if budget < 25:
                    continue
                s = _clip(summary, budget)
                if not s.endswith(('.', '!', '?', ELLIPSIS, '؟')):
                    s += '.'
                out = f'{nm}: {s} ' + DOSE[lang].format(d=d) + (' ' + tail if tail else '')
                if DESC_MIN <= len(out) <= DESC_MAX:
                    return out
    # long dose lines: name + dose + tail only
    for nm in _names(name):
        for tail in TAILS[lang]:
            out = f'{nm}: ' + DOSE[lang].format(d=_clip(dose, DESC_MAX - len(nm) - 12 - len(tail))) + (' ' + tail if tail else '')
            if len(out) <= DESC_MAX:
                return out
    raise ValueError(f'supplement_meta.desc: nothing fits for {name!r} [{lang}]')


COMPARE = {
    'en': dict(title='Dose compared with related supplements', cols=('Supplement', 'Recommended dose', 'When', 'How often'),
               this='this page', note='From the dosage sections of each page; follow the label and your doctor or pharmacist.'),
    'nl': dict(title='Dosering vergeleken met verwante supplementen', cols=('Supplement', 'Aanbevolen dosis', 'Wanneer', 'Hoe vaak'),
               this='deze pagina', note='Uit de doseringsrubriek van elke pagina; volg het etiket en je arts of apotheker.'),
    'sv': dict(title='Dosering jämfört med liknande kosttillskott', cols=('Kosttillskott', 'Rekommenderad dos', 'När', 'Hur ofta'),
               this='denna sida', note='Från doseringsavsnittet på varje sida; följ förpackningen och din läkare eller farmaceut.'),
    'ar': dict(title='مقارنة الجرعة مع مكملات مشابهة', cols=('المكمل', 'الجرعة الموصى بها', 'التوقيت', 'التكرار'),
               this='هذه الصفحة', note='من قسم الجرعة في كل صفحة؛ اتبع تعليمات العبوة وإرشادات طبيبك أو الصيدلي.'),
}


def compare_html(lang, this_name, this_dose, rows, icon):
    """rows: [(name, url, dose dict)] of up to three related supplements."""
    t = COMPARE[lang]
    e = html.escape
    def cells(d):
        return ''.join(f'<td>{e(d.get(k) or "–")}</td>' for k in ('recommended', 'timing', 'frequency'))
    body = [f'<tr class="is-this"><th scope="row">{e(this_name)} <span>({e(t["this"])})</span></th>{cells(this_dose)}</tr>']
    body += [f'<tr><th scope="row"><a href="{url}">{e(n)}</a></th>{cells(d)}</tr>' for n, url, d in rows]
    head = ''.join(f'<th scope="col">{e(c)}</th>' for c in t['cols'])
    return (f'<section class="facts-block" aria-labelledby="dose-compare-title">'
            f'<h2 class="section-title" id="dose-compare-title">{icon} <span>{e(t["title"])}</span></h2>'
            f'<div class="table-scroll"><table class="nutrition-table dose-table facts-compare"><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div><p class="table-note">{e(t["note"])}</p></section>')
