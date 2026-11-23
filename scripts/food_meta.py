"""<title>, meta description and the "key numbers" facts block of a food page, from the food's own numbers.

Rule (Dr. Wassim Habib, 2026-11-23): titles 45-58 characters in every language, the local name first, a number
(kcal per 100 g, GI) and a blood-sugar question; no brand in the title (Google shows the site name). Descriptions
125-155 characters with the per-100 g and per-portion numbers and a comparison hook. Every number comes from
js/data.js; no new health claims (questions and plain facts only).

The facts block adds what the nutrition table does not show: energy density, where the calories come from,
protein per 100 kcal, fibre per gram of carbohydrate, glycemic load per 100 g and per portion, and the three most
similar foods of the same group side by side (each linking to its page, so every food is linked from its peers).
"""
import html
import re

TITLE_MIN, TITLE_MAX = 45, 58
DESC_MIN, DESC_MAX = 125, 155

# patterns from the longest to the shortest; the first one that lands in 45-58 characters is used
TITLES = {
    'gi': {
        'en': ['{n} Calories & GI: {kcal} kcal, GI {gi} – Does It Raise Blood Sugar?',
               '{n}: {kcal} kcal & GI {gi} – Does It Raise Blood Sugar?',
               '{n}: {kcal} kcal, GI {gi} – Effect on Blood Sugar',
               '{n}: {kcal} kcal, GI {gi} – Blood Sugar Impact',
               '{n}: {kcal} kcal, GI {gi} – Blood Sugar?',
               '{n}: {kcal} kcal, GI {gi}'],
        'nl': ['{n} calorieën en GI: {kcal} kcal, GI {gi} – stijgt je bloedsuiker?',
               '{n}: {kcal} kcal en GI {gi} – stijgt je bloedsuiker?',
               '{n}: {kcal} kcal, GI {gi} – effect op je bloedsuiker',
               '{n}: {kcal} kcal, GI {gi} – en je bloedsuiker?',
               '{n}: {kcal} kcal per 100 g, GI {gi}',
               '{n}: {kcal} kcal, GI {gi}'],
        'sv': ['{n} kalorier och GI: {kcal} kcal, GI {gi} – höjer det blodsockret?',
               '{n}: {kcal} kcal och GI {gi} – höjer det blodsockret?',
               '{n}: {kcal} kcal, GI {gi} – effekt på blodsockret',
               '{n}: {kcal} kcal, GI {gi} – och blodsockret?',
               '{n}: {kcal} kcal, GI {gi}'],
        'ar': ['سعرات {n}: {kcal} سعرة ومؤشر جلايسيمي {gi} – ماذا عن سكر الدم؟',
               '{n}: {kcal} سعرة ومؤشر جلايسيمي {gi} – ماذا عن سكر الدم؟',
               '{n}: {kcal} سعرة والمؤشر الجلايسيمي {gi} – وسكر الدم؟',
               '{n}: {kcal} سعرة، مؤشر جلايسيمي {gi}',
               '{n}: {kcal} سعرة، GI {gi}'],
    },
    'lowcarb': {      # under 5 g available carbohydrate: the GI does not apply
        'en': ['{n} Calories: {kcal} kcal, {avail} g Carbs – Blood Sugar Friendly?',
               '{n}: {kcal} kcal, {avail} g Carbs – Blood Sugar Friendly?',
               '{n}: {kcal} kcal, {avail} g Carbs – Effect on Blood Sugar',
               '{n}: {kcal} kcal, {avail} g Carbs – Blood Sugar?',
               '{n}: {kcal} kcal, {avail} g Carbs'],
        'nl': ['{n} calorieën: {kcal} kcal, {avail} g koolhydraten – en je bloedsuiker?',
               '{n}: {kcal} kcal, {avail} g koolhydraten – en je bloedsuiker?',
               '{n}: {kcal} kcal, {avail} g koolhydraten – bloedsuiker?',
               '{n}: {kcal} kcal en {avail} g koolhydraten per 100 g',
               '{n}: {kcal} kcal, {avail} g koolhydraten'],
        'sv': ['{n} kalorier: {kcal} kcal, {avail} g kolhydrater – och blodsockret?',
               '{n}: {kcal} kcal, {avail} g kolhydrater – och blodsockret?',
               '{n}: {kcal} kcal, {avail} g kolhydrater – blodsocker?',
               '{n}: {kcal} kcal, {avail} g kolhydrater'],
        'ar': ['سعرات {n}: {kcal} سعرة و{avail} غ كربوهيدرات – ماذا عن سكر الدم؟',
               '{n}: {kcal} سعرة و{avail} غ كربوهيدرات – ماذا عن سكر الدم؟',
               '{n}: {kcal} سعرة و{avail} غ كربوهيدرات – وسكر الدم؟',
               '{n}: {kcal} سعرة و{avail} غ كربوهيدرات'],
    },
}
TITLES['nogi'] = TITLES['lowcarb']     # carbohydrate food without a published GI: the same carb-first wording,
TITLES['nogi'] = {l: [p for p in v if 'Friendly' not in p] for l, v in TITLES['lowcarb'].items()}   # without "friendly"

DESC_BASE = {
    'gi': {
        'en': ['{n}: {kcal} kcal per 100 {u} and {pk} kcal per {p} {u} serving. Glycemic index {gi} ({level}), glycemic load {gl}.',
               '{n}: {kcal} kcal per 100 {u}, {pk} kcal per serving. GI {gi} ({level}), glycemic load {gl}.',
               '{n}: {kcal} kcal/100 {u}, GI {gi} ({level}), GL {gl}.'],
        'nl': ['{n}: {kcal} kcal per 100 {u} en {pk} kcal per portie van {p} {u}. Glykemische index {gi} ({level}), glykemische lading {gl}.',
               '{n}: {kcal} kcal per 100 {u}, {pk} kcal per portie. GI {gi} ({level}), glykemische lading {gl}.',
               '{n}: {kcal} kcal/100 {u}, GI {gi} ({level}), GL {gl}.'],
        'sv': ['{n}: {kcal} kcal per 100 {u} och {pk} kcal per portion om {p} {u}. Glykemiskt index {gi} ({level}), glykemisk belastning {gl}.',
               '{n}: {kcal} kcal per 100 {u}, {pk} kcal per portion. GI {gi} ({level}), glykemisk belastning {gl}.',
               '{n}: {kcal} kcal/100 {u}, GI {gi} ({level}), GL {gl}.'],
        'ar': ['{n}: {kcal} سعرة لكل 100 {u} و{pk} سعرة في حصة {p} {u}. المؤشر الجلايسيمي {gi} ({level}) والحمل الجلايسيمي {gl}.',
               '{n}: {kcal} سعرة لكل 100 {u} و{pk} سعرة في الحصة. المؤشر الجلايسيمي {gi} ({level})، الحمل {gl}.',
               '{n}: {kcal} سعرة/100 {u}، المؤشر الجلايسيمي {gi} ({level}).'],
    },
    'lowcarb': {
        'en': ['{n}: {kcal} kcal and {protein} g protein per 100 {u}, {pk} kcal per {p} {u} serving. Only {avail} g available carbs, so GI does not apply.',
               '{n}: {kcal} kcal and {protein} g protein per 100 {u}. {avail} g available carbs, so GI does not apply.',
               '{n}: {kcal} kcal/100 {u}, {avail} g carbs: GI does not apply.'],
        'nl': ['{n}: {kcal} kcal en {protein} g eiwit per 100 {u}, {pk} kcal per portie van {p} {u}. {avail} g beschikbare koolhydraten, dus geen GI.',
               '{n}: {kcal} kcal en {protein} g eiwit per 100 {u}. {avail} g beschikbare koolhydraten, dus geen GI.',
               '{n}: {kcal} kcal/100 {u}, {avail} g koolhydraten: geen GI.'],
        'sv': ['{n}: {kcal} kcal och {protein} g protein per 100 {u}, {pk} kcal per portion om {p} {u}. {avail} g tillgängliga kolhydrater, så GI gäller inte.',
               '{n}: {kcal} kcal och {protein} g protein per 100 {u}. {avail} g tillgängliga kolhydrater, så GI gäller inte.',
               '{n}: {kcal} kcal/100 {u}, {avail} g kolhydrater: GI gäller inte.'],
        'ar': ['{n}: {kcal} سعرة و{protein} غ بروتين لكل 100 {u}، و{pk} سعرة في حصة {p} {u}. الكربوهيدرات المتاحة {avail} غ، فلا ينطبق المؤشر الجلايسيمي.',
               '{n}: {kcal} سعرة و{protein} غ بروتين لكل 100 {u}. الكربوهيدرات المتاحة {avail} غ، فلا ينطبق المؤشر الجلايسيمي.',
               '{n}: {kcal} سعرة/100 {u}، {avail} غ كربوهيدرات: لا ينطبق المؤشر.'],
    },
    'nogi': {
        'en': ['{n}: {kcal} kcal and {avail} g available carbs per 100 {u}, {pk} kcal per {p} {u} serving. No published GI value yet.',
               '{n}: {kcal} kcal and {avail} g available carbs per 100 {u}. No published GI value yet.',
               '{n}: {kcal} kcal/100 {u}, {avail} g carbs, no published GI.'],
        'nl': ['{n}: {kcal} kcal en {avail} g beschikbare koolhydraten per 100 {u}, {pk} kcal per portie van {p} {u}. Nog geen gepubliceerde GI.',
               '{n}: {kcal} kcal en {avail} g beschikbare koolhydraten per 100 {u}. Nog geen gepubliceerde GI.',
               '{n}: {kcal} kcal/100 {u}, {avail} g koolhydraten, geen GI.'],
        'sv': ['{n}: {kcal} kcal och {avail} g tillgängliga kolhydrater per 100 {u}, {pk} kcal per portion om {p} {u}. Inget publicerat GI ännu.',
               '{n}: {kcal} kcal och {avail} g tillgängliga kolhydrater per 100 {u}. Inget publicerat GI ännu.',
               '{n}: {kcal} kcal/100 {u}, {avail} g kolhydrater, inget GI.'],
        'ar': ['{n}: {kcal} سعرة و{avail} غ كربوهيدرات متاحة لكل 100 {u}، و{pk} سعرة في حصة {p} {u}. لا توجد قيمة منشورة للمؤشر الجلايسيمي بعد.',
               '{n}: {kcal} سعرة و{avail} غ كربوهيدرات متاحة لكل 100 {u}. لا توجد قيمة منشورة للمؤشر بعد.',
               '{n}: {kcal} سعرة/100 {u}، {avail} غ كربوهيدرات.'],
    },
}
# hooks after the numbers, longest first; {alt} = the most similar food of the same group
HOOKS = {
    'en': ['Compare it with {alt} and find smarter swaps.', 'See how it compares with {alt}.', 'Compare it with {alt}.',
           'Tips and smarter swaps inside.', 'Plus smarter swaps.', 'See swaps.'],
    'nl': ['Vergelijk met {alt} en vind slimmere keuzes.', 'Zie hoe het zich verhoudt tot {alt}.', 'Vergelijk met {alt}.',
           'Met tips en slimmere keuzes.', 'Met slimmere keuzes.', 'Met tips.'],
    'sv': ['Jämför med {alt} och hitta smartare byten.', 'Se hur det står sig mot {alt}.', 'Jämför med {alt}.',
           'Med tips och smartare byten.', 'Med smartare byten.', 'Med tips.'],
    'ar': ['قارنه مع {alt} واكتشف البدائل الأذكى.', 'شاهد مقارنته مع {alt}.', 'قارنه مع {alt}.',
           'مع نصائح وبدائل أذكى.', 'مع بدائل أذكى.', 'مع نصائح.'],
}
FILL = {'en': ' Full nutrition facts.', 'nl': ' Volledige voedingswaarde.', 'sv': ' Fullständigt näringsvärde.', 'ar': ' مع القيم الغذائية كاملة.'}
JOINS = {'ar': ('مع',), 'en': ('with', 'and', '&', 'in', 'on'), 'nl': ('met', 'en', '&', 'in', 'op'), 'sv': ('med', 'och', '&', 'i', 'på')}


def _names(name, lang):
    """The name, then shorter forms: without (brackets), cut before a joining word, then word by word."""
    out = [name]
    short = re.sub(r'\s*\([^)]*\)', '', name).strip() or name   # a comma part stays: "Aprikoser, torkade"
    out.append(short)
    words = short.split()
    for k in range(len(words) - 1, 0, -1):
        if words[k].lower() in JOINS[lang] or (lang == 'ar' and words[k][:1] in 'وب' and len(words[k]) > 3):
            out.append(' '.join(words[:k]))
    for k in range(len(words) - 1, 0, -1):
        out.append(' '.join(words[:k]).rstrip(' ,،-–&'))
    return list(dict.fromkeys(n for n in out if n))


def title(mode, lang, name, taken=None, **v):
    """45-58 characters: the longest pattern that fits; a pattern with the blood-sugar question is preferred with the
    full or bracket-free name, before a plain numbers-only title. `taken` (a set per language) keeps titles unique:
    a title already used by another food is skipped for the next candidate."""
    names = _names(name, lang)
    hooked = [p for p in TITLES[mode][lang] if '–' in p]
    candidates = [pat.format(n=nm, **v) for pat in hooked for nm in names[:2]]
    candidates += [pat.format(n=nm, **v) for nm in names for pat in TITLES[mode][lang]]
    fitting = [t for t in dict.fromkeys(candidates) if TITLE_MIN <= len(t) <= TITLE_MAX]
    for t in fitting:
        if taken is None or t not in taken:
            if taken is not None:
                taken.add(t)
            return t
    # a very long single word: the shortest pattern with the shortest name, cut to the limit
    t = TITLES[mode][lang][-1].format(n=names[-1], **v)[:TITLE_MAX].rstrip(' ,،-–')
    if taken is not None:
        taken.add(t)
    return t


def desc(mode, lang, name, alt, **v):
    """125-155 characters: the numbers, then the longest hook that fits."""
    for nm in _names(name, lang):
        for base in DESC_BASE[mode][lang]:
            b = base.format(n=nm, **v)
            if len(b) > DESC_MAX:
                continue
            for hook in HOOKS[lang]:
                if '{alt}' in hook and not alt:
                    continue
                d = b + ' ' + hook.format(alt=alt or '')
                if DESC_MIN <= len(d) <= DESC_MAX:
                    return d
            if len(b) + len(FILL[lang]) <= DESC_MAX:
                d = b + FILL[lang]
                for hook in HOOKS[lang]:
                    if '{alt}' in hook:
                        continue
                    if DESC_MIN <= len(d + ' ' + hook) <= DESC_MAX:
                        return d + ' ' + hook
                if DESC_MIN <= len(d) <= DESC_MAX:
                    return d
    raise ValueError(f'food_meta.desc: nothing fits for {name!r} [{lang}]')


# ---------------------------------------------------------------------------------------------------------------
# facts block
# ---------------------------------------------------------------------------------------------------------------
FACTS = {
    'en': dict(title='Key numbers at a glance', density='Energy density', per_g='kcal per gram',
               bands=('very low', 'low', 'medium', 'high'), split='Calories from carbs / protein / fat',
               pdens='Protein', pdens_u='g per 100 kcal', fibre='Fibre per carbohydrate',
               fibre_v='1 g fibre per {r} g carbohydrate', fibre_none='no fibre', gl='Glycemic load',
               gl_v='{a} per 100 {u} · {b} per {p} {u} portion', near='Most similar foods in this group',
               cols=('Food', 'kcal', 'Carbs', 'Protein', 'GI'), this='this food',
               note='Computed from the values per 100 {u} on this page; for orientation only.'),
    'nl': dict(title='De belangrijkste cijfers', density='Energiedichtheid', per_g='kcal per gram',
               bands=('zeer laag', 'laag', 'gemiddeld', 'hoog'), split='Calorieën uit koolhydraten / eiwit / vet',
               pdens='Eiwit', pdens_u='g per 100 kcal', fibre='Vezels per koolhydraat',
               fibre_v='1 g vezels per {r} g koolhydraten', fibre_none='geen vezels', gl='Glykemische lading',
               gl_v='{a} per 100 {u} · {b} per portie van {p} {u}', near='Meest vergelijkbare producten in deze groep',
               cols=('Product', 'kcal', 'Koolh.', 'Eiwit', 'GI'), this='dit product',
               note='Berekend uit de waarden per 100 {u} op deze pagina; alleen ter oriëntatie.'),
    'sv': dict(title='Nyckeltal i korthet', density='Energitäthet', per_g='kcal per gram',
               bands=('mycket låg', 'låg', 'medel', 'hög'), split='Kalorier från kolhydrater / protein / fett',
               pdens='Protein', pdens_u='g per 100 kcal', fibre='Fiber per kolhydrat',
               fibre_v='1 g fiber per {r} g kolhydrater', fibre_none='inga fibrer', gl='Glykemisk belastning',
               gl_v='{a} per 100 {u} · {b} per portion om {p} {u}', near='Mest liknande livsmedel i gruppen',
               cols=('Livsmedel', 'kcal', 'Kolh.', 'Protein', 'GI'), this='detta livsmedel',
               note='Beräknat från värdena per 100 {u} på sidan; endast som vägledning.'),
    'ar': dict(title='أهم الأرقام باختصار', density='كثافة الطاقة', per_g='سعرة لكل غرام',
               bands=('منخفضة جداً', 'منخفضة', 'متوسطة', 'مرتفعة'), split='مصدر السعرات: كربوهيدرات / بروتين / دهون',
               pdens='البروتين', pdens_u='غ لكل 100 سعرة', fibre='الألياف مقابل الكربوهيدرات',
               fibre_v='1 غ ألياف لكل {r} غ كربوهيدرات', fibre_none='لا ألياف', gl='الحمل الجلايسيمي',
               gl_v='{a} لكل 100 {u} · {b} في حصة {p} {u}', near='أقرب الأطعمة إليه في المجموعة',
               cols=('الطعام', 'سعرات', 'كربوهيدرات', 'بروتين', 'GI'), this='هذا الطعام',
               note='محسوبة من القيم لكل 100 {u} في هذه الصفحة، للاسترشاد فقط.'),
}


def density_band(kcal_per_g):
    """Energy density bands (Rolls / British Nutrition Foundation): <0.6, 0.6-1.5, 1.5-4, >4 kcal/g."""
    return 0 if kcal_per_g < 0.6 else 1 if kcal_per_g < 1.5 else 2 if kcal_per_g <= 4 else 3


def nearest(food, peers, n=3):
    """The n foods of the same group with the closest nutrient profile (kcal/10, carbs, protein, fat, fibre)."""
    def dist(f):
        return ((f['kcal'] - food['kcal']) / 10) ** 2 + sum((f[k] - food[k]) ** 2 for k in ('carbs', 'protein', 'fat', 'fiber'))
    return sorted((f for f in peers if f['id'] != food['id']), key=lambda f: (dist(f), f['id']))[:n]


def facts_html(food, lang, near, *, fmt, name_of, url_of, gi_of, unit, portion, gl100, glp, icon):
    t = FACTS[lang]
    e = html.escape
    kcal = food['kcal']
    dens = kcal / 100
    rows = [(t['density'], f'{fmt(dens)} {t["per_g"]} ({t["bands"][density_band(dens)]})')]
    energy = [food['carbs'] * 4, food['protein'] * 4, food['fat'] * 9]
    total = sum(energy)
    if total > 0:
        pct = [round(x * 100 / total) for x in energy]
        rows.append((t['split'], ' / '.join(f'{p}%' for p in pct)))
    if kcal >= 5:
        rows.append((t['pdens'], f'{fmt(food["protein"] * 100 / kcal)} {t["pdens_u"]}'))
    if food['carbs'] >= 1:
        rows.append((t['fibre'], t['fibre_v'].format(r=fmt(food['carbs'] / food['fiber'])) if food['fiber'] > 0 else t['fibre_none']))
    if gl100 is not None:
        rows.append((t['gl'], t['gl_v'].format(a=fmt(gl100), b=fmt(glp), p=portion, u=unit)))
    table = ''.join(f'<tr><th scope="row">{e(k)}</th><td>{e(v)}</td></tr>' for k, v in rows)
    def gi_cell(f):
        g = gi_of(f)
        return str(int(g)) if g is not None else '–'
    cmp_rows = [f'<tr class="is-this"><th scope="row">{e(name_of(food))} <span>({e(t["this"])})</span></th>'
                f'<td>{round(kcal)}</td><td>{fmt(food["avail"])} g</td><td>{fmt(food["protein"])} g</td><td>{gi_cell(food)}</td></tr>']
    cmp_rows += [f'<tr><th scope="row"><a href="{url_of(f)}">{e(name_of(f))}</a></th><td>{round(f["kcal"])}</td>'
                 f'<td>{fmt(f["avail"])} g</td><td>{fmt(f["protein"])} g</td><td>{gi_cell(f)}</td></tr>' for f in near]
    head = ''.join(f'<th scope="col">{e(c)}</th>' for c in t['cols'])
    return (f'<section class="facts-block" aria-labelledby="facts-title">'
            f'<h2 class="section-title" id="facts-title">{icon("scale")} <span>{e(t["title"])}</span></h2>'
            f'<table class="nutrition-table facts-table"><tbody>{table}</tbody></table>'
            f'<h3 class="facts-sub">{e(t["near"])}</h3>'
            f'<div class="table-scroll"><table class="nutrition-table facts-compare"><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(cmp_rows)}</tbody></table></div>'
            f'<p class="table-note">{e(t["note"].format(u=unit))}</p></section>')


# styles of the key numbers block, appended to css/food-page.css by generate_food_pages.write_assets()
FACTS_CSS = """
        /* key numbers block (scripts/food_meta.py, 2026-11-23) */
        .facts-block .facts-sub { font-size: 1rem; font-weight: 800; margin: 18px 0 8px; }
        .facts-block .table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
        .facts-table th { width: 46%; font-weight: 600; }
        .facts-compare { min-width: 420px; }
        .facts-compare th a { color: var(--primary); text-decoration: none; font-weight: 700; }
        .facts-compare th a:hover { text-decoration: underline; }
        .facts-compare .is-this th span { font-weight: 400; color: var(--text-muted); }
        .facts-compare td { text-align: center; white-space: nowrap; }
"""
