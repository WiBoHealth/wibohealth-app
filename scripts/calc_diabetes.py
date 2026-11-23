"""Diabetes tools (batch B, 2026-11-23): HbA1c calculator, blood sugar converter, diabetes risk test (FINDRISC),
insulin resistance calculator (HOMA-IR + TyG). Arabic approved by Dr. Wassim Habib (decisions of 2026-11-23:
both prediabetes HbA1c ranges ADA + NICE/WHO; after-meal reading with the diagnostic value for people without
diabetes and the general target for people with diabetes; IDF waist note for people of Asian origin without
changing FINDRISC points; HOMA-IR and TyG only). EN/NL/SV are translations of the Arabic.

Formulas: js/calc-formulas.js (tested by scripts/test_calc_formulas.js). TyG = ln(TG mg/dL x glucose mg/dL / 2).
Titles use the words people search for (research 2026-11-23). The consult-your-doctor note is small print at the
bottom (disclaimer); a high result shows the advice to see the doctor for a lab test in the "next steps" card.
"""

CONSULT = {
    'ar': 'يُنصح بمراجعة طبيبك لإجراء الفحص المخبري التأكيدي.',
    'en': 'We recommend seeing your doctor for a confirmatory lab test.',
    'nl': 'We raden aan om bij je huisarts een bevestigend bloedonderzoek te laten doen.',
    'sv': 'Vi rekommenderar att du kontaktar vårdcentralen för ett bekräftande blodprov.',
}
NEXT = {'ar': 'خطواتك التالية', 'en': 'Your next steps', 'nl': 'Je volgende stappen', 'sv': 'Dina nästa steg'}
SMALL = {
    'ar': 'هذه الأداة للتثقيف الصحي فقط ولا تُغني عن استشارة الطبيب. الحساب يتم على جهازك ولا نحفظ أي رقم تدخله.',
    'en': 'This tool is for health education only and does not replace advice from your doctor. Everything is calculated on your device; we do not store anything you enter.',
    'nl': 'Deze tool is alleen bedoeld als gezondheidsvoorlichting en vervangt geen advies van je arts. Alles wordt op je eigen apparaat berekend; we bewaren niets van wat je invult.',
    'sv': 'Verktyget är endast avsett som hälsoinformation och ersätter inte råd från din läkare. Allt räknas ut på din enhet; vi sparar inget av det du skriver in.',
}


def _li(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def _next(lang, links, consult=False):
    """HTML of the "next steps" card: optional doctor advice first, then links."""
    head = f'<h3>{NEXT[lang]}</h3>'
    first = f'<p class="next-consult"><strong>{CONSULT[lang]}</strong></p>' if consult else ''
    return head + first + _li(links)


def _fmt(x, d, lang):
    s = f'{x:.{d}f}'
    return s.replace('.', ',') if lang in ('nl', 'sv') else s


def hba1c_table(lang):
    head = {'ar': ('السكر التراكمي %', 'mmol/mol', 'معدل السكر mg/dL', 'معدل السكر mmol/L'),
            'en': ('HbA1c %', 'mmol/mol', 'Average glucose mg/dL', 'Average glucose mmol/L'),
            'nl': ('HbA1c %', 'mmol/mol', 'Gemiddelde glucose mg/dl', 'Gemiddelde glucose mmol/l'),
            'sv': ('HbA1c %', 'mmol/mol', 'Medelglukos mg/dl', 'Medelglukos mmol/l')}[lang]
    rows = ''
    for i in range(10, 25):
        p = i / 2
        mmol = (p - 2.15) * 10.929
        mg = 28.7 * p - 46.7
        rows += f'<tr><td>{_fmt(p, 1, lang)}</td><td>{round(mmol)}</td><td>{round(mg)}</td><td>{_fmt(mg / 18.016, 1, lang)}</td></tr>'
    return ('<div class="table-scroll"><table class="nutrition-table"><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) +
            f'</tr></thead><tbody>{rows}</tbody></table></div>')


def glucose_table(lang):
    rows = ''.join(f'<tr><td>{mg}</td><td>{_fmt(mg / 18.016, 1, lang)}</td></tr>'
                   for mg in (54, 70, 80, 90, 100, 110, 126, 140, 160, 180, 200, 250, 300, 400))
    return ('<div class="table-scroll"><table class="nutrition-table"><thead><tr><th>mg/dL</th><th>mmol/L</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')


# ======================================================================================================== HbA1c
HBA1C = {
    'key': 'hba1c', 'slug': 'hba1c-calculator', 'icon': 'fa-droplet', 'badge': 'ADA · IFCC · NICE', 'category': 'diabetes',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'American Diabetes Association. Standards of Care in Diabetes 2025: Diagnosis and Classification. Diabetes Care 2025;48(Suppl 1).',
        'Nathan DM, et al. Translating the A1C assay into estimated average glucose values (ADAG). Diabetes Care 2008;31:1473-1478.',
        'Hoelzel W, et al. IFCC reference system for HbA1c: the master equation. Clin Chem 2004;50:166-174.',
        'NICE NG28. Type 2 diabetes in adults: management (HbA1c 42-47 mmol/mol, risk of diabetes). 2022.',
        'World Health Organization. Use of glycated haemoglobin (HbA1c) in the diagnosis of diabetes mellitus. 2011.',
    ],
    'content': {
        'ar': dict(
            title='حاسبة السكر التراكمي: تحويل HbA1c ومعرفة معدل السكر',
            desc='حوّل السكر التراكمي من النسبة % إلى mmol/mol وبالعكس، واعرف معدل السكر في دمك خلال آخر 3 أشهر، مع جدول تحويل كامل وشرح النتيجة.',
            h1='حاسبة السكر التراكمي (HbA1c) ومعدل السكر في الدم', crumb='حاسبة السكر التراكمي', cat='أدوات السكري',
            short='حاسبة السكر التراكمي', blurb='حوّل HbA1c بين % و mmol/mol واعرف معدل السكر.',
            about=[{'name': 'السكر التراكمي'}, {'name': 'السكري', 'condition': True}, {'name': 'ما قبل السكري', 'condition': True}],
            lead='السكر التراكمي يعطيك صورة عن متوسط السكر في دمك خلال آخر شهرين إلى ثلاثة أشهر. بعض المختبرات تكتبه بالنسبة المئوية (مثل 6.5%)، ومختبرات أوروبا (هولندا والسويد وبريطانيا) تكتبه بـ mmol/mol (مثل 48). اكتب رقمك بأي وحدة لتعرف ما يقابله، ومعدل السكر التقريبي في دمك.',
            ui=dict(card_title='احسب سكرك التراكمي', lbl_value='قيمة السكر التراكمي', ph_value='مثال: 6.5', lbl_unit='الوحدة',
                    u_pct='% (نسبة مئوية)', u_mmol='mmol/mol', btn='احسب', res_heading='السكر التراكمي',
                    eag_label='معدل السكر التقريبي في دمك', eag_sub='خلال آخر 2 إلى 3 أشهر (تقدير)',
                    st_normal='ضمن المعدل الطبيعي', st_prediabetes='ما قبل السكري', st_diabetes='في نطاق السكري',
                    tip_normal='ضمن المعدل الطبيعي (أقل من 5.7% أو 39 mmol/mol).',
                    tip_prediabetes='أعلى من الطبيعي، وهي مرحلة «ما قبل السكري». تعتبرها الجمعية الأمريكية للسكري من 5.7% إلى 6.4% (39 إلى 47 mmol/mol)، ويعتبرها NICE ومنظمة الصحة العالمية من 6.0% إلى 6.4% (42 إلى 47). تغييرات بسيطة في الأكل والحركة تُحدث فرقاً كبيراً في هذه المرحلة.',
                    tip_diabetes='في نطاق السكري (6.5% أو 48 mmol/mol فأكثر). يُشخَّص السكري عادةً بعد تكرار التحليل.',
                    nx_normal=_next('ar', ['حافظ على الأكل المتوازن والحركة اليومية: <a href="{food:lentils}">العدس</a> وأطعمة <a href="{site:/foods/index.html}">دليل الأطعمة</a> منخفضة المؤشر الجلايسيمي.',
                                           'اعرف خطرك المستقبلي: <a href="{calc:findrisc}">اختبار خطر الإصابة بالسكري</a>.']),
                    nx_prediabetes=_next('ar', ['اقرأ <a href="{site:/diabetes/prediabetes.html}">دليل ما قبل السكري</a> لتعرف كيف توقف تقدّم الحالة.',
                                                'اختر <a href="{site:/foods/index.html}">أطعمة منخفضة المؤشر الجلايسيمي</a>.',
                                                'قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>.'], consult=True),
                    nx_diabetes=_next('ar', ['اقرأ <a href="{site:/diabetes.html}">قسم السكري ومتلازمة الأيض</a>.',
                                             'حوّل قراءات جهاز السكر: <a href="{calc:glucose}">محوّل قراءة السكر</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>ما هو السكر التراكمي؟</span></h2>
            <p>عندما يرتفع السكر في الدم يلتصق جزء منه بخلايا الدم الحمراء، وتعيش هذه الخلايا نحو 3 أشهر، لذلك يعكس التحليل متوسط السكر في هذه المدة، ولا يتأثر بوجبة الأمس.</p>
            <h2 class="section-title"><i class="fas fa-right-left"></i> <span>لماذا وحدتان مختلفتان؟</span></h2>
            <p>النسبة % هي الطريقة القديمة والأمريكية، و mmol/mol هي الوحدة الدولية المعتمدة في أوروبا. الرقمان يصفان نفس النتيجة.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>ما معنى «معدل السكر التقريبي»؟</span></h2>
            <p>هو رقم محسوب من السكر التراكمي بمعادلة دراسة ADAG، يساعدك على مقارنة التحليل بقراءات جهاز قياس السكر في البيت. هو تقدير وليس قياساً مباشراً.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>متى لا يكون السكر التراكمي دقيقاً؟</span></h2>
            <p>فقر الدم، أمراض الدم الوراثية (مثل الثلاسيميا)، فقدان دم حديث، الحمل، وأمراض الكلى المتقدمة قد تجعل النتيجة أعلى أو أقل من الحقيقة.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>جدول تحويل السكر التراكمي</span></h2>
            {TABLE}''',
            faq=[('كم السكر التراكمي الطبيعي؟', 'أقل من 5.7% (39 mmol/mol) عند أغلب البالغين غير المصابين بالسكري.'),
                 ('كم يجب أن يكون السكر التراكمي لمريض السكري؟', 'هدف شائع لكثير من البالغين هو حوالي 7% (53 mmol/mol)، لكن الهدف يختلف من شخص لآخر ويحدده الطبيب.'),
                 ('كل كم أعيد التحليل؟', 'عادةً كل 3 أشهر عند تعديل العلاج، وكل 6 أشهر عند استقرار السكر، أو حسب طبيبك.'),
                 ('هل يمكن أن ينزل السكر التراكمي بسرعة؟', 'يحتاج التغيير عادةً 8 إلى 12 أسبوعاً ليظهر كاملاً في التحليل.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='A1C Calculator: Convert HbA1c and Average Blood Sugar',
            desc='Convert HbA1c from % to mmol/mol and back, and see your average blood sugar over the past 3 months, with a full conversion chart and what your result means.',
            h1='HbA1c calculator and average blood sugar', crumb='HbA1c calculator', cat='Diabetes tools',
            short='HbA1c calculator', blurb='Convert HbA1c between % and mmol/mol and see your average glucose.',
            about=[{'name': 'HbA1c'}, {'name': 'Diabetes', 'condition': True}, {'name': 'Prediabetes', 'condition': True}],
            lead='HbA1c shows your average blood sugar over the past two to three months. Some labs report it as a percentage (for example 6.5%), while labs in Europe (the Netherlands, Sweden, the UK) report it in mmol/mol (for example 48). Enter your result in either unit to see what it equals and your approximate average blood sugar.',
            ui=dict(card_title='Calculate your HbA1c', lbl_value='HbA1c result', ph_value='e.g. 6.5', lbl_unit='Unit',
                    u_pct='% (percentage)', u_mmol='mmol/mol', btn='Calculate', res_heading='HbA1c',
                    eag_label='Your approximate average blood sugar', eag_sub='over the past 2 to 3 months (estimate)',
                    st_normal='Within the normal range', st_prediabetes='Prediabetes', st_diabetes='In the diabetes range',
                    tip_normal='Within the normal range (below 5.7% or 39 mmol/mol).',
                    tip_prediabetes='Higher than normal: the "prediabetes" stage. The American Diabetes Association uses 5.7% to 6.4% (39 to 47 mmol/mol); NICE and the WHO use 6.0% to 6.4% (42 to 47). Small changes in eating and activity make a big difference at this stage.',
                    tip_diabetes='In the diabetes range (6.5% or 48 mmol/mol and above). Diabetes is usually diagnosed after a repeat test.',
                    nx_normal=_next('en', ['Keep eating well and moving every day: <a href="{food:lentils}">lentils</a> and other low-GI foods in the <a href="{site:/foods/index.html}">food guide</a>.',
                                           'Check your future risk: <a href="{calc:findrisc}">diabetes risk test</a>.']),
                    nx_prediabetes=_next('en', ['Read the <a href="{site:/diabetes/prediabetes.html}">prediabetes guide</a> to learn how to stop it progressing.',
                                                'Choose <a href="{site:/foods/index.html}">low glycemic index foods</a>.',
                                                'Measure your <a href="{calc:whtr}">waist-to-height ratio</a>.'], consult=True),
                    nx_diabetes=_next('en', ['Read the <a href="{site:/diabetes.html}">diabetes section</a>.',
                                             'Convert your meter readings: <a href="{calc:glucose}">blood sugar converter</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>What is HbA1c?</span></h2>
            <p>When blood sugar is high, part of it sticks to red blood cells. These cells live for about 3 months, so the test reflects your average blood sugar over that time and is not affected by yesterday's meal.</p>
            <h2 class="section-title"><i class="fas fa-right-left"></i> <span>Why two different units?</span></h2>
            <p>The percentage is the older and American way; mmol/mol is the international unit used in Europe. Both numbers describe the same result.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>What does "approximate average blood sugar" mean?</span></h2>
            <p>It is calculated from HbA1c with the ADAG study equation and helps you compare the test with your home meter readings. It is an estimate, not a direct measurement.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>When is HbA1c less accurate?</span></h2>
            <p>Anaemia, inherited blood disorders (such as thalassaemia), recent blood loss, pregnancy and advanced kidney disease can make the result higher or lower than the true value.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>HbA1c conversion chart</span></h2>
            {TABLE}''',
            faq=[('What is a normal HbA1c?', 'Below 5.7% (39 mmol/mol) for most adults without diabetes.'),
                 ('What should HbA1c be for someone with diabetes?', 'A common target for many adults is about 7% (53 mmol/mol), but targets differ from person to person and are set by your doctor.'),
                 ('How often should I repeat the test?', 'Usually every 3 months when treatment is being adjusted and every 6 months when blood sugar is stable, or as your doctor advises.'),
                 ('Can HbA1c come down quickly?', 'A change usually takes 8 to 12 weeks to show fully in the test.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='HbA1c omrekenen: van % naar mmol/mol en gemiddelde suiker',
            desc='Reken je HbA1c om van % naar mmol/mol en terug, en zie je gemiddelde bloedsuiker van de afgelopen 3 maanden, met een omrekentabel en uitleg.',
            h1='HbA1c omrekenen en je gemiddelde bloedsuiker', crumb='HbA1c omrekenen', cat='Diabetestools',
            short='HbA1c omrekenen', blurb='Reken HbA1c om tussen % en mmol/mol en zie je gemiddelde glucose.',
            about=[{'name': 'HbA1c'}, {'name': 'Diabetes', 'condition': True}, {'name': 'Prediabetes', 'condition': True}],
            lead='Je HbA1c laat de gemiddelde bloedsuiker van de afgelopen twee tot drie maanden zien. Sommige laboratoria geven hem als percentage (bijvoorbeeld 6,5%), in Nederland, Zweden en het Verenigd Koninkrijk staat hij in mmol/mol (bijvoorbeeld 48). Vul je uitslag in een van beide eenheden in om te zien wat die betekent en wat je gemiddelde bloedsuiker ongeveer is.',
            ui=dict(card_title='Reken je HbA1c om', lbl_value='HbA1c-uitslag', ph_value='bijv. 48', lbl_unit='Eenheid',
                    u_pct='% (percentage)', u_mmol='mmol/mol', btn='Bereken', res_heading='HbA1c',
                    eag_label='Je gemiddelde bloedsuiker (schatting)', eag_sub='over de afgelopen 2 tot 3 maanden',
                    st_normal='Binnen de normale waarden', st_prediabetes='Prediabetes', st_diabetes='In het diabetesbereik',
                    tip_normal='Binnen de normale waarden (onder 5,7% of 39 mmol/mol).',
                    tip_prediabetes='Hoger dan normaal: de fase "prediabetes". De American Diabetes Association hanteert 5,7% tot 6,4% (39 tot 47 mmol/mol); NICE en de WHO hanteren 6,0% tot 6,4% (42 tot 47). Kleine aanpassingen in eten en bewegen maken in deze fase veel verschil.',
                    tip_diabetes='In het diabetesbereik (6,5% of 48 mmol/mol en hoger). Diabetes wordt meestal pas vastgesteld na een herhaalde meting.',
                    nx_normal=_next('nl', ['Blijf gevarieerd eten en dagelijks bewegen: <a href="{food:lentils}">linzen</a> en andere producten met een lage GI in de <a href="{site:/foods/index.html}">voedingswijzer</a>.',
                                           'Check je risico voor later: <a href="{calc:findrisc}">diabetes risicotest</a>.']),
                    nx_prediabetes=_next('nl', ['Lees de <a href="{site:/diabetes/prediabetes.html}">gids over prediabetes</a> en ontdek hoe je verdere stijging voorkomt.',
                                                'Kies <a href="{site:/foods/index.html}">producten met een lage glykemische index</a>.',
                                                'Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>.'], consult=True),
                    nx_diabetes=_next('nl', ['Lees het <a href="{site:/diabetes.html}">diabetesoverzicht</a>.',
                                             'Reken je metingen om: <a href="{calc:glucose}">bloedsuiker omrekenen</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Wat is HbA1c?</span></h2>
            <p>Als je bloedsuiker hoog is, hecht een deel ervan zich aan je rode bloedcellen. Die leven ongeveer 3 maanden, dus de meting laat je gemiddelde bloedsuiker over die periode zien en hangt niet af van de maaltijd van gisteren.</p>
            <h2 class="section-title"><i class="fas fa-right-left"></i> <span>Waarom twee eenheden?</span></h2>
            <p>Het percentage is de oudere, Amerikaanse manier; mmol/mol is de internationale eenheid die in Europa wordt gebruikt. Beide getallen beschrijven dezelfde uitslag.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>Wat betekent "gemiddelde bloedsuiker"?</span></h2>
            <p>Dit getal wordt uit je HbA1c berekend met de formule uit het ADAG-onderzoek en helpt je de uitslag te vergelijken met de metingen van je eigen meter. Het is een schatting, geen directe meting.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Wanneer is HbA1c minder betrouwbaar?</span></h2>
            <p>Bloedarmoede, erfelijke bloedziekten (zoals thalassemie), recent bloedverlies, zwangerschap en ernstige nierziekte kunnen de uitslag hoger of lager maken dan de werkelijke waarde.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>HbA1c-omrekentabel</span></h2>
            {TABLE}''',
            faq=[('Wat is een normale HbA1c?', 'Onder 5,7% (39 mmol/mol) bij de meeste volwassenen zonder diabetes.'),
                 ('Hoe hoog mag de HbA1c zijn bij diabetes?', 'Een veelgebruikt doel voor veel volwassenen is ongeveer 53 mmol/mol (7%), maar het doel verschilt per persoon en wordt door je arts bepaald.'),
                 ('Hoe vaak moet ik de HbA1c laten meten?', 'Meestal elke 3 maanden als de behandeling wordt aangepast en elke 6 maanden als je bloedsuiker stabiel is, of zoals je arts adviseert.'),
                 ('Kan de HbA1c snel dalen?', 'Een verandering heeft meestal 8 tot 12 weken nodig om volledig in de meting te verschijnen.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='HbA1c-omvandlare: procent till mmol/mol och medelsocker',
            desc='Omvandla HbA1c från procent till mmol/mol och tillbaka, och se ditt medelblodsocker de senaste 3 månaderna, med omvandlingstabell och förklaring.',
            h1='Omvandla HbA1c och se ditt medelblodsocker', crumb='HbA1c-omvandlare', cat='Diabetesverktyg',
            short='HbA1c-omvandlare', blurb='Omvandla HbA1c mellan % och mmol/mol och se ditt medelglukos.',
            about=[{'name': 'HbA1c'}, {'name': 'Diabetes', 'condition': True}, {'name': 'Prediabetes', 'condition': True}],
            lead='HbA1c visar ditt genomsnittliga blodsocker de senaste två till tre månaderna. Vissa laboratorier anger värdet i procent (till exempel 6,5 %), medan laboratorier i Europa (Sverige, Nederländerna och Storbritannien) anger det i mmol/mol (till exempel 48). Skriv in ditt värde i valfri enhet för att se vad det motsvarar och ditt ungefärliga medelblodsocker.',
            ui=dict(card_title='Räkna om ditt HbA1c', lbl_value='HbA1c-värde', ph_value='t.ex. 48', lbl_unit='Enhet',
                    u_pct='% (procent)', u_mmol='mmol/mol', btn='Beräkna', res_heading='HbA1c',
                    eag_label='Ditt ungefärliga medelblodsocker', eag_sub='de senaste 2 till 3 månaderna (uppskattning)',
                    st_normal='Inom normalintervallet', st_prediabetes='Prediabetes', st_diabetes='Inom diabetesintervallet',
                    tip_normal='Inom normalintervallet (under 5,7 % eller 39 mmol/mol).',
                    tip_prediabetes='Högre än normalt, det vill säga "prediabetes". American Diabetes Association använder 5,7–6,4 % (39–47 mmol/mol); NICE och WHO använder 6,0–6,4 % (42–47). Små förändringar i mat och rörelse gör stor skillnad i det här skedet.',
                    tip_diabetes='Inom diabetesintervallet (6,5 % eller 48 mmol/mol och högre). Diabetes fastställs oftast efter ett upprepat prov.',
                    nx_normal=_next('sv', ['Fortsätt äta varierat och röra på dig varje dag: <a href="{food:lentils}">linser</a> och andra livsmedel med lågt GI i <a href="{site:/foods/index.html}">livsmedelsguiden</a>.',
                                           'Ta reda på din framtida risk: <a href="{calc:findrisc}">diabetes risktest</a>.']),
                    nx_prediabetes=_next('sv', ['Läs <a href="{site:/diabetes/prediabetes.html}">guiden om prediabetes</a> och se hur du bromsar utvecklingen.',
                                                'Välj <a href="{site:/foods/index.html}">livsmedel med lågt glykemiskt index</a>.',
                                                'Mät din <a href="{calc:whtr}">midja-längd-kvot</a>.'], consult=True),
                    nx_diabetes=_next('sv', ['Läs <a href="{site:/diabetes.html}">diabetesavsnittet</a>.',
                                             'Omvandla dina mätarvärden: <a href="{calc:glucose}">omvandla blodsocker</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Vad är HbA1c?</span></h2>
            <p>När blodsockret är högt fastnar en del av det på de röda blodkropparna. De lever i ungefär 3 månader, så provet speglar ditt genomsnittliga blodsocker under den tiden och påverkas inte av gårdagens måltid.</p>
            <h2 class="section-title"><i class="fas fa-right-left"></i> <span>Varför två olika enheter?</span></h2>
            <p>Procent är det äldre, amerikanska sättet; mmol/mol är den internationella enhet som används i Europa. Båda talen beskriver samma resultat.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>Vad betyder "ungefärligt medelblodsocker"?</span></h2>
            <p>Det räknas fram ur HbA1c med ekvationen från ADAG-studien och hjälper dig att jämföra provet med mätningarna från din egen mätare. Det är en uppskattning, inte en direkt mätning.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>När är HbA1c mindre tillförlitligt?</span></h2>
            <p>Blodbrist, ärftliga blodsjukdomar (som talassemi), nyligen förlorat blod, graviditet och svår njursjukdom kan göra att värdet blir högre eller lägre än det verkliga.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Omvandlingstabell för HbA1c</span></h2>
            {TABLE}''',
            faq=[('Vad är ett normalt HbA1c?', 'Under 5,7 % (39 mmol/mol) för de flesta vuxna utan diabetes.'),
                 ('Vilket HbA1c bör man ha vid diabetes?', 'Ett vanligt mål för många vuxna är ungefär 53 mmol/mol (7 %), men målet skiljer sig mellan personer och bestäms av din läkare.'),
                 ('Hur ofta ska provet tas?', 'Oftast var tredje månad när behandlingen justeras och var sjätte månad när blodsockret är stabilt, eller enligt din läkares råd.'),
                 ('Kan HbA1c sjunka snabbt?', 'En förändring tar oftast 8 till 12 veckor att synas fullt ut i provet.')],
            disclaimer=SMALL['sv']),
    },
}

# ======================================================================================================== glucose
GLUCOSE = {
    'key': 'glucose', 'slug': 'blood-sugar-converter', 'icon': 'fa-right-left', 'badge': 'ADA · WHO', 'category': 'diabetes',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'American Diabetes Association. Standards of Care in Diabetes 2025: Diagnosis and Classification; Glycemic Goals. Diabetes Care 2025;48(Suppl 1).',
        'World Health Organization / IDF. Definition and diagnosis of diabetes mellitus and intermediate hyperglycaemia. 2006.',
        'Joslin Diabetes Center. Blood glucose conversion table (mg/dL to mmol/L).',
    ],
    'content': {
        'ar': dict(
            title='تحويل السكر من mg/dl إلى mmol/l: حاسبة وجدول جاهز',
            desc='حوّل قراءة السكر من mg/dL إلى mmol/L وبالعكس بضغطة واحدة، مع جدول جاهز ومعنى القراءة على الريق وبعد الأكل بساعتين.',
            h1='تحويل قراءة السكر بين mg/dL و mmol/L', crumb='تحويل قراءة السكر', cat='أدوات السكري',
            short='تحويل قراءة السكر', blurb='من mg/dL إلى mmol/L وبالعكس.',
            about=[{'name': 'سكر الدم'}, {'name': 'السكري', 'condition': True}],
            lead='أجهزة قياس السكر في الدول العربية وأمريكا تعرض القراءة غالباً بـ mg/dL، أما في هولندا والسويد وبريطانيا فتعرضها بـ mmol/L. اكتب القراءة بأي وحدة لتعرف ما يقابلها. القاعدة بسيطة: mmol/L = mg/dL ÷ 18.',
            ui=dict(card_title='حوّل قراءة السكر', lbl_value='قراءة السكر', ph_value='مثال: 126', lbl_unit='الوحدة',
                    u_mgdl='mg/dL', u_mmol='mmol/L', lbl_when='متى قست؟', w_fast='على الريق (صيام 8 ساعات)', w_after='بعد الأكل بساعتين',
                    w_any='أريد التحويل فقط', btn='حوّل', res_heading='القراءة بعد التحويل',
                    st_low='منخفضة', st_normal='طبيعية', st_prediabetes='أعلى من الطبيعي', st_diabetes='في نطاق السكري', st_conv='تم التحويل',
                    tip_low='منخفضة. إذا شعرت برجفة أو تعرّق أو دوخة فتناول سكراً سريعاً (مثل نصف كوب عصير).',
                    tip_fast_normal='طبيعية على الريق (70 إلى 99 mg/dL أو 3.9 إلى 5.5 mmol/L).',
                    tip_fast_prediabetes='أعلى من الطبيعي على الريق (100 إلى 125 mg/dL أو 5.6 إلى 6.9 mmol/L)، أي مرحلة ما قبل السكري.',
                    tip_fast_diabetes='في نطاق السكري على الريق (126 mg/dL أو 7.0 mmol/L فأكثر) إذا تكررت في يوم آخر.',
                    tip_after_normal='لغير المصابين بالسكري: أقل من 140 mg/dL (7.8 mmol/L) بعد الأكل بساعتين طبيعي. لمرضى السكري: الهدف العام أقل من 180 mg/dL (10.0 mmol/L) حسب توجيه الطبيب.',
                    tip_after_prediabetes='لغير المصابين بالسكري: من 140 إلى 199 mg/dL (7.8 إلى 11.0 mmol/L) أعلى من الطبيعي. لمرضى السكري: الهدف العام أقل من 180 mg/dL (10.0 mmol/L) حسب توجيه الطبيب.',
                    tip_after_diabetes='200 mg/dL (11.1 mmol/L) فأكثر بعد الأكل مرتفعة. لمرضى السكري: الهدف العام أقل من 180 mg/dL (10.0 mmol/L) حسب توجيه الطبيب.',
                    tip_conv='القاعدة: mmol/L = mg/dL ÷ 18، و mg/dL = mmol/L × 18.',
                    nx_low=_next('ar', ['إذا تكرر انخفاض السكر فناقش علاجك مع الطبيب.']),
                    nx_normal=_next('ar', ['اعرف متوسط سكرك لثلاثة أشهر: <a href="{calc:hba1c}">حاسبة السكر التراكمي</a>.']),
                    nx_prediabetes=_next('ar', ['اقرأ <a href="{site:/diabetes/prediabetes.html}">دليل ما قبل السكري</a>.',
                                                'قيّم خطرك: <a href="{calc:findrisc}">اختبار خطر الإصابة بالسكري</a>.'], consult=True),
                    nx_diabetes=_next('ar', ['حوّل السكر التراكمي: <a href="{calc:hba1c}">حاسبة السكر التراكمي</a>.',
                                             'اقرأ <a href="{site:/diabetes.html}">قسم السكري</a>.'], consult=True),
                    nx_conv=_next('ar', ['حاسبة <a href="{calc:hba1c}">السكر التراكمي</a> لتعرف متوسط سكرك.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-globe"></i> <span>لماذا تختلف الوحدات بين البلدان؟</span></h2>
            <p>الوحدة mg/dL تقيس وزن السكر في حجم من الدم، و mmol/L تقيس عدد جزيئاته. أمريكا ومعظم الدول العربية تستخدم mg/dL، وأوروبا وكندا وأستراليا تستخدم mmol/L. الرقمان يصفان نفس القراءة.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>جدول تحويل قراءة السكر</span></h2>
            {TABLE}
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>جهاز البيت وتحليل المختبر</span></h2>
            <p>جهاز البيت يقيس دم الإصبع، وتحليل المختبر يقيس دم الوريد (البلازما)، لذلك يُقبل فرق يصل إلى 15% تقريباً بينهما.</p>
            <h2 class="section-title"><i class="fas fa-clock"></i> <span>متى تقيس؟</span></h2>
            <p>على الريق بعد صيام 8 ساعات على الأقل، قبل الوجبات، وبعد ساعتين من بداية الأكل. اكتب الوقت مع كل قراءة لتفهمها بشكل صحيح.</p>''',
            faq=[('كم 100 mg/dL بالـ mmol/L؟', '5.6 mmol/L.'),
                 ('كم 7 mmol/L بالـ mg/dL؟', 'حوالي 126 mg/dL.'),
                 ('ما هي قراءة السكر الطبيعية على الريق؟', 'من 70 إلى 99 mg/dL (3.9 إلى 5.5 mmol/L).'),
                 ('ما هي قراءة السكر الطبيعية بعد الأكل بساعتين؟', 'لغير المصابين بالسكري أقل من 140 mg/dL (7.8 mmol/L). لمرضى السكري الهدف العام أقل من 180 mg/dL (10.0 mmol/L) حسب توجيه الطبيب.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='Blood Sugar Converter: mg/dL to mmol/L with Chart',
            desc='Convert a blood sugar reading from mg/dL to mmol/L and back in one step, with a ready chart and what fasting and 2-hour after-meal readings mean.',
            h1='Convert blood sugar between mg/dL and mmol/L', crumb='Blood sugar converter', cat='Diabetes tools',
            short='Blood sugar converter', blurb='From mg/dL to mmol/L and back.',
            about=[{'name': 'Blood glucose'}, {'name': 'Diabetes', 'condition': True}],
            lead='Meters in the US and most Arab countries show readings in mg/dL, while meters in the Netherlands, Sweden and the UK show mmol/L. Enter a reading in either unit to see what it equals. The rule is simple: mmol/L = mg/dL ÷ 18.',
            ui=dict(card_title='Convert your reading', lbl_value='Blood sugar reading', ph_value='e.g. 126', lbl_unit='Unit',
                    u_mgdl='mg/dL', u_mmol='mmol/L', lbl_when='When did you measure?', w_fast='Fasting (8 hours without food)', w_after='2 hours after a meal',
                    w_any='Just convert', btn='Convert', res_heading='Converted reading',
                    st_low='Low', st_normal='Normal', st_prediabetes='Higher than normal', st_diabetes='In the diabetes range', st_conv='Converted',
                    tip_low='Low. If you feel shaky, sweaty or dizzy, take fast sugar (such as half a glass of juice).',
                    tip_fast_normal='Normal when fasting (70 to 99 mg/dL or 3.9 to 5.5 mmol/L).',
                    tip_fast_prediabetes='Higher than normal when fasting (100 to 125 mg/dL or 5.6 to 6.9 mmol/L): the prediabetes stage.',
                    tip_fast_diabetes='In the diabetes range when fasting (126 mg/dL or 7.0 mmol/L and above) if repeated on another day.',
                    tip_after_normal='For people without diabetes, below 140 mg/dL (7.8 mmol/L) two hours after a meal is normal. For people with diabetes, the general target is below 180 mg/dL (10.0 mmol/L), as your doctor advises.',
                    tip_after_prediabetes='For people without diabetes, 140 to 199 mg/dL (7.8 to 11.0 mmol/L) is higher than normal. For people with diabetes, the general target is below 180 mg/dL (10.0 mmol/L), as your doctor advises.',
                    tip_after_diabetes='200 mg/dL (11.1 mmol/L) or more after a meal is high. For people with diabetes, the general target is below 180 mg/dL (10.0 mmol/L), as your doctor advises.',
                    tip_conv='The rule: mmol/L = mg/dL ÷ 18, and mg/dL = mmol/L × 18.',
                    nx_low=_next('en', ['If low readings happen again, discuss your treatment with your doctor.']),
                    nx_normal=_next('en', ['See your three-month average: <a href="{calc:hba1c}">HbA1c calculator</a>.']),
                    nx_prediabetes=_next('en', ['Read the <a href="{site:/diabetes/prediabetes.html}">prediabetes guide</a>.',
                                                'Check your risk: <a href="{calc:findrisc}">diabetes risk test</a>.'], consult=True),
                    nx_diabetes=_next('en', ['Convert your HbA1c: <a href="{calc:hba1c}">HbA1c calculator</a>.',
                                             'Read the <a href="{site:/diabetes.html}">diabetes section</a>.'], consult=True),
                    nx_conv=_next('en', ['The <a href="{calc:hba1c}">HbA1c calculator</a> shows your average blood sugar.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-globe"></i> <span>Why do units differ between countries?</span></h2>
            <p>mg/dL measures the weight of sugar in a volume of blood; mmol/L counts its molecules. The US and most Arab countries use mg/dL; Europe, Canada and Australia use mmol/L. Both numbers describe the same reading.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Blood sugar conversion chart</span></h2>
            {TABLE}
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Home meter versus lab test</span></h2>
            <p>A home meter measures blood from your fingertip, a lab measures blood from a vein (plasma), so a difference of up to about 15% between them is accepted.</p>
            <h2 class="section-title"><i class="fas fa-clock"></i> <span>When to measure</span></h2>
            <p>Fasting after at least 8 hours without food, before meals, and two hours after you start eating. Write down the time with each reading so you can read it correctly.</p>''',
            faq=[('What is 100 mg/dL in mmol/L?', '5.6 mmol/L.'),
                 ('What is 7 mmol/L in mg/dL?', 'About 126 mg/dL.'),
                 ('What is a normal fasting blood sugar?', '70 to 99 mg/dL (3.9 to 5.5 mmol/L).'),
                 ('What is a normal blood sugar two hours after eating?', 'Below 140 mg/dL (7.8 mmol/L) for people without diabetes. For people with diabetes, the general target is below 180 mg/dL (10.0 mmol/L), as your doctor advises.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='Bloedsuiker omrekenen: mg/dl naar mmol/l met tabel',
            desc='Reken een bloedsuikerwaarde om van mg/dl naar mmol/l en terug in één stap, met een tabel en uitleg over nuchtere waarden en 2 uur na het eten.',
            h1='Bloedsuiker omrekenen tussen mg/dl en mmol/l', crumb='Bloedsuiker omrekenen', cat='Diabetestools',
            short='Bloedsuiker omrekenen', blurb='Van mg/dl naar mmol/l en terug.',
            about=[{'name': 'Bloedglucose'}, {'name': 'Diabetes', 'condition': True}],
            lead='Meters in de VS en de meeste Arabische landen tonen de waarde in mg/dl, meters in Nederland, Zweden en het Verenigd Koninkrijk in mmol/l. Vul een waarde in een van beide eenheden in om te zien wat die is. De regel is eenvoudig: mmol/l = mg/dl ÷ 18.',
            ui=dict(card_title='Reken je waarde om', lbl_value='Bloedsuikerwaarde', ph_value='bijv. 7,0', lbl_unit='Eenheid',
                    u_mgdl='mg/dl', u_mmol='mmol/l', lbl_when='Wanneer heb je gemeten?', w_fast='Nuchter (8 uur niet gegeten)', w_after='2 uur na het eten',
                    w_any='Alleen omrekenen', btn='Omrekenen', res_heading='Omgerekende waarde',
                    st_low='Laag', st_normal='Normaal', st_prediabetes='Hoger dan normaal', st_diabetes='In het diabetesbereik', st_conv='Omgerekend',
                    tip_low='Laag. Voel je je trillerig, zweterig of duizelig, neem dan snelle suiker (bijvoorbeeld een half glas sap).',
                    tip_fast_normal='Normaal nuchter (3,9 tot 5,5 mmol/l of 70 tot 99 mg/dl).',
                    tip_fast_prediabetes='Hoger dan normaal nuchter (5,6 tot 6,9 mmol/l of 100 tot 125 mg/dl): de fase prediabetes.',
                    tip_fast_diabetes='In het diabetesbereik nuchter (7,0 mmol/l of 126 mg/dl en hoger) als dit op een andere dag opnieuw zo is.',
                    tip_after_normal='Voor mensen zonder diabetes is minder dan 7,8 mmol/l (140 mg/dl) twee uur na het eten normaal. Voor mensen met diabetes is het algemene doel onder 10,0 mmol/l (180 mg/dl), zoals je arts adviseert.',
                    tip_after_prediabetes='Voor mensen zonder diabetes is 7,8 tot 11,0 mmol/l (140 tot 199 mg/dl) hoger dan normaal. Voor mensen met diabetes is het algemene doel onder 10,0 mmol/l (180 mg/dl), zoals je arts adviseert.',
                    tip_after_diabetes='11,1 mmol/l (200 mg/dl) of meer na het eten is hoog. Voor mensen met diabetes is het algemene doel onder 10,0 mmol/l (180 mg/dl), zoals je arts adviseert.',
                    tip_conv='De regel: mmol/l = mg/dl ÷ 18, en mg/dl = mmol/l × 18.',
                    nx_low=_next('nl', ['Komen lage waarden vaker voor, bespreek je behandeling dan met je arts.']),
                    nx_normal=_next('nl', ['Bekijk je gemiddelde van drie maanden: <a href="{calc:hba1c}">HbA1c omrekenen</a>.']),
                    nx_prediabetes=_next('nl', ['Lees de <a href="{site:/diabetes/prediabetes.html}">gids over prediabetes</a>.',
                                                'Check je risico: <a href="{calc:findrisc}">diabetes risicotest</a>.'], consult=True),
                    nx_diabetes=_next('nl', ['Reken je HbA1c om: <a href="{calc:hba1c}">HbA1c omrekenen</a>.',
                                             'Lees het <a href="{site:/diabetes.html}">diabetesoverzicht</a>.'], consult=True),
                    nx_conv=_next('nl', ['Met <a href="{calc:hba1c}">HbA1c omrekenen</a> zie je je gemiddelde bloedsuiker.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-globe"></i> <span>Waarom verschillen de eenheden per land?</span></h2>
            <p>mg/dl meet het gewicht van suiker in een hoeveelheid bloed, mmol/l telt het aantal moleculen. De VS en de meeste Arabische landen gebruiken mg/dl; Europa, Canada en Australië gebruiken mmol/l. Beide getallen beschrijven dezelfde meting.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Omrekentabel bloedsuiker</span></h2>
            {TABLE}
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Eigen meter en laboratorium</span></h2>
            <p>Een meter thuis meet bloed uit je vingertop, het laboratorium meet bloed uit een ader (plasma). Daarom is een verschil tot ongeveer 15% tussen beide normaal.</p>
            <h2 class="section-title"><i class="fas fa-clock"></i> <span>Wanneer meet je?</span></h2>
            <p>Nuchter na minstens 8 uur niet eten, voor de maaltijden en twee uur nadat je begint met eten. Schrijf bij elke meting de tijd op, zodat je de waarde goed kunt beoordelen.</p>''',
            faq=[('Hoeveel is 100 mg/dl in mmol/l?', '5,6 mmol/l.'),
                 ('Hoeveel is 7 mmol/l in mg/dl?', 'Ongeveer 126 mg/dl.'),
                 ('Wat is een normale nuchtere bloedsuiker?', '3,9 tot 5,5 mmol/l (70 tot 99 mg/dl).'),
                 ('Wat is een normale bloedsuiker twee uur na het eten?', 'Onder 7,8 mmol/l (140 mg/dl) voor mensen zonder diabetes. Voor mensen met diabetes is het algemene doel onder 10,0 mmol/l (180 mg/dl), zoals je arts adviseert.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='Omvandla blodsocker: mg/dl till mmol/l med tabell',
            desc='Omvandla ett blodsockervärde från mg/dl till mmol/l och tillbaka i ett steg, med tabell och förklaring av fasteblodsocker och värdet 2 timmar efter mat.',
            h1='Omvandla blodsocker mellan mg/dl och mmol/l', crumb='Omvandla blodsocker', cat='Diabetesverktyg',
            short='Omvandla blodsocker', blurb='Från mg/dl till mmol/l och tillbaka.',
            about=[{'name': 'Blodsocker'}, {'name': 'Diabetes', 'condition': True}],
            lead='Mätare i USA och de flesta arabiska länder visar värdet i mg/dl, medan mätare i Sverige, Nederländerna och Storbritannien visar mmol/l. Skriv in ett värde i valfri enhet för att se vad det motsvarar. Regeln är enkel: mmol/l = mg/dl ÷ 18.',
            ui=dict(card_title='Omvandla ditt värde', lbl_value='Blodsockervärde', ph_value='t.ex. 7,0', lbl_unit='Enhet',
                    u_mgdl='mg/dl', u_mmol='mmol/l', lbl_when='När mätte du?', w_fast='Fastande (8 timmar utan mat)', w_after='2 timmar efter en måltid',
                    w_any='Bara omvandla', btn='Omvandla', res_heading='Omvandlat värde',
                    st_low='Lågt', st_normal='Normalt', st_prediabetes='Högre än normalt', st_diabetes='Inom diabetesintervallet', st_conv='Omvandlat',
                    tip_low='Lågt. Om du känner dig skakig, svettig eller yr, ta snabbt socker (till exempel ett halvt glas juice).',
                    tip_fast_normal='Normalt fastevärde (3,9–5,5 mmol/l eller 70–99 mg/dl).',
                    tip_fast_prediabetes='Högre än normalt fastevärde (5,6–6,9 mmol/l eller 100–125 mg/dl): prediabetes.',
                    tip_fast_diabetes='Inom diabetesintervallet fastande (7,0 mmol/l eller 126 mg/dl och högre) om det upprepas en annan dag.',
                    tip_after_normal='För personer utan diabetes är under 7,8 mmol/l (140 mg/dl) två timmar efter maten normalt. För personer med diabetes är det allmänna målet under 10,0 mmol/l (180 mg/dl), enligt din läkares råd.',
                    tip_after_prediabetes='För personer utan diabetes är 7,8–11,0 mmol/l (140–199 mg/dl) högre än normalt. För personer med diabetes är det allmänna målet under 10,0 mmol/l (180 mg/dl), enligt din läkares råd.',
                    tip_after_diabetes='11,1 mmol/l (200 mg/dl) eller mer efter maten är högt. För personer med diabetes är det allmänna målet under 10,0 mmol/l (180 mg/dl), enligt din läkares råd.',
                    tip_conv='Regeln: mmol/l = mg/dl ÷ 18, och mg/dl = mmol/l × 18.',
                    nx_low=_next('sv', ['Om låga värden kommer tillbaka, ta upp din behandling med din läkare.']),
                    nx_normal=_next('sv', ['Se ditt genomsnitt över tre månader: <a href="{calc:hba1c}">HbA1c-omvandlare</a>.']),
                    nx_prediabetes=_next('sv', ['Läs <a href="{site:/diabetes/prediabetes.html}">guiden om prediabetes</a>.',
                                                'Ta reda på din risk: <a href="{calc:findrisc}">diabetes risktest</a>.'], consult=True),
                    nx_diabetes=_next('sv', ['Räkna om ditt HbA1c: <a href="{calc:hba1c}">HbA1c-omvandlare</a>.',
                                             'Läs <a href="{site:/diabetes.html}">diabetesavsnittet</a>.'], consult=True),
                    nx_conv=_next('sv', ['<a href="{calc:hba1c}">HbA1c-omvandlaren</a> visar ditt medelblodsocker.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-globe"></i> <span>Varför skiljer sig enheterna mellan länder?</span></h2>
            <p>mg/dl mäter vikten socker i en mängd blod, mmol/l räknar antalet molekyler. USA och de flesta arabiska länder använder mg/dl; Europa, Kanada och Australien använder mmol/l. Båda talen beskriver samma mätning.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Omvandlingstabell för blodsocker</span></h2>
            {TABLE}
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Egen mätare och laboratorium</span></h2>
            <p>En mätare hemma mäter blod från fingertoppen, laboratoriet mäter blod från en ven (plasma). Därför godtas en skillnad på upp till ungefär 15 % mellan dem.</p>
            <h2 class="section-title"><i class="fas fa-clock"></i> <span>När ska man mäta?</span></h2>
            <p>Fastande efter minst 8 timmar utan mat, före måltider och två timmar efter att du börjat äta. Skriv ner tiden vid varje mätning så att du kan tolka värdet rätt.</p>''',
            faq=[('Hur mycket är 100 mg/dl i mmol/l?', '5,6 mmol/l.'),
                 ('Hur mycket är 7 mmol/l i mg/dl?', 'Ungefär 126 mg/dl.'),
                 ('Vad är ett normalt fasteblodsocker?', '3,9–5,5 mmol/l (70–99 mg/dl).'),
                 ('Vad är normalt blodsocker två timmar efter maten?', 'Under 7,8 mmol/l (140 mg/dl) för personer utan diabetes. För personer med diabetes är det allmänna målet under 10,0 mmol/l (180 mg/dl), enligt din läkares råd.')],
            disclaimer=SMALL['sv']),
    },
}

# ======================================================================================================== FINDRISC
_Q = {
    'ar': dict(sex='الجنس', male='ذكر', female='أنثى', age='كم عمرك؟', weight='الوزن (كغ)', height='الطول (سم)',
               waist='محيط الخصر عند مستوى السرة (سم)', active='هل تمارس نشاطاً بدنياً 30 دقيقة على الأقل كل يوم؟ (مشي، عمل، رياضة)',
               veg='هل تأكل الخضار أو الفواكه كل يوم؟', bp='هل تأخذ دواءً لضغط الدم؟',
               glucose='هل قال لك طبيب يوماً إن سكرك مرتفع؟ (في فحص، أو أثناء مرض، أو أثناء الحمل)',
               family='هل أحد من عائلتك مصاب بالسكري (النوع الأول أو الثاني)؟', yes='نعم', no='لا',
               fam_none='لا', fam_second='نعم: جد أو جدة أو عم أو خال أو عمة أو خالة أو ابن عم',
               fam_first='نعم: أب أو أم أو أخ أو أخت أو ابن أو ابنة'),
    'en': dict(sex='Sex', male='Male', female='Female', age='How old are you?', weight='Weight (kg)', height='Height (cm)',
               waist='Waist circumference at the level of your navel (cm)', active='Are you physically active for at least 30 minutes every day? (walking, work, sport)',
               veg='Do you eat vegetables or fruit every day?', bp='Do you take medication for high blood pressure?',
               glucose='Has a doctor ever told you that your blood sugar was high? (in a check-up, during an illness or during pregnancy)',
               family='Does anyone in your family have diabetes (type 1 or type 2)?', yes='Yes', no='No',
               fam_none='No', fam_second='Yes: grandparent, aunt, uncle or first cousin', fam_first='Yes: parent, brother, sister or child'),
    'nl': dict(sex='Geslacht', male='Man', female='Vrouw', age='Hoe oud ben je?', weight='Gewicht (kg)', height='Lengte (cm)',
               waist='Buikomvang ter hoogte van je navel (cm)', active='Beweeg je elke dag minstens 30 minuten? (wandelen, werk, sport)',
               veg='Eet je elke dag groente of fruit?', bp='Gebruik je medicijnen tegen hoge bloeddruk?',
               glucose='Heeft een arts ooit gezegd dat je bloedsuiker te hoog was? (bij een controle, tijdens ziekte of tijdens de zwangerschap)',
               family='Heeft iemand in je familie diabetes (type 1 of type 2)?', yes='Ja', no='Nee',
               fam_none='Nee', fam_second='Ja: grootouder, tante, oom, neef of nicht', fam_first='Ja: ouder, broer, zus of kind'),
    'sv': dict(sex='Kön', male='Man', female='Kvinna', age='Hur gammal är du?', weight='Vikt (kg)', height='Längd (cm)',
               waist='Midjemått i höjd med naveln (cm)', active='Rör du på dig minst 30 minuter varje dag? (promenad, arbete, träning)',
               veg='Äter du grönsaker eller frukt varje dag?', bp='Tar du läkemedel mot högt blodtryck?',
               glucose='Har en läkare någon gång sagt att ditt blodsocker var för högt? (vid en kontroll, under sjukdom eller under graviditet)',
               family='Har någon i din familj diabetes (typ 1 eller typ 2)?', yes='Ja', no='Nej',
               fam_none='Nej', fam_second='Ja: mor- eller farförälder, moster, faster, morbror, farbror eller kusin', fam_first='Ja: förälder, syskon eller barn'),
}

FINDRISC = {
    'key': 'findrisc', 'slug': 'diabetes-risk-test', 'icon': 'fa-list-check', 'badge': 'FINDRISC', 'category': 'diabetes',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'Lindström J, Tuomilehto J. The diabetes risk score: a practical tool to predict type 2 diabetes risk. Diabetes Care 2003;26:725-731.',
        'Finnish Diabetes Association. FINDRISC – Type 2 diabetes risk test.',
        'International Diabetes Federation. The IDF consensus worldwide definition of the metabolic syndrome (ethnic-specific waist values). 2006.',
    ],
    'content': {
        'ar': dict(
            title='اختبار خطر الإصابة بالسكري: هل أنت معرض للسكري؟',
            desc='أجب عن 8 أسئلة بسيطة في دقيقتين لتعرف خطر إصابتك بالسكري من النوع الثاني خلال 10 سنوات، باستخدام استبيان FINDRISC المعتمد أوروبياً.',
            h1='اختبار خطر الإصابة بالسكري من النوع الثاني', crumb='اختبار خطر الإصابة بالسكري', cat='أدوات السكري',
            short='اختبار خطر الإصابة بالسكري', blurb='8 أسئلة في دقيقتين.',
            about=[{'name': 'السكري من النوع الثاني', 'condition': True}, {'name': 'ما قبل السكري', 'condition': True}],
            lead='هذا الاختبار مبني على استبيان FINDRISC الفنلندي، وهو من أكثر الاستبيانات استخداماً في أوروبا لمعرفة احتمال الإصابة بالسكري من النوع الثاني خلال السنوات العشر القادمة. لا يحتاج أي تحليل دم، فقط شريط قياس للخصر.',
            ui=dict(card_title='أجب عن الأسئلة', btn='اعرف نتيجتي', res_heading='مجموع نقاطك', risk_label='خطر الإصابة خلال 10 سنوات',
                    risk_txt='{r} أشخاص', bmi_label='مؤشر كتلة جسمك', **_Q['ar'],
                    risk_low='1 من كل 100', risk_slight='1 من كل 25', risk_moderate='1 من كل 6', risk_high='1 من كل 3', risk_veryhigh='1 من كل 2',
                    st_low='خطر منخفض', st_slight='خطر منخفض قليلاً', st_moderate='خطر متوسط', st_high='خطر مرتفع', st_veryhigh='خطر مرتفع جداً',
                    tip_low='خطرك منخفض. استمر على الأكل المتوازن والحركة اليومية.',
                    tip_slight='خطرك أعلى قليلاً من الطبيعي. الحركة اليومية والأكل الغني بالألياف يخفضانه.',
                    tip_moderate='يُستحسن فحص السكر التراكمي أو سكر الصيام في زيارتك القادمة للطبيب.',
                    tip_high='يُنصح بفحص السكر قريباً. نزول 5% من الوزن وزيادة الحركة يخفضان الخطر بشكل واضح.',
                    tip_veryhigh='يُنصح بفحص السكر في أقرب وقت.',
                    nx_low=_next('ar', ['أعد الاختبار كل 3 سنوات تقريباً.', 'اختر <a href="{site:/foods/index.html}">أطعمة منخفضة المؤشر الجلايسيمي</a>.']),
                    nx_slight=_next('ar', ['قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>.', 'اقرأ <a href="{site:/diabetes/prediabetes.html}">دليل ما قبل السكري</a>.']),
                    nx_moderate=_next('ar', ['اقرأ <a href="{site:/diabetes/prediabetes.html}">دليل ما قبل السكري</a>.', 'إذا كان معك تحليل: <a href="{calc:hba1c}">حاسبة السكر التراكمي</a>.'], consult=True),
                    nx_high=_next('ar', ['اقرأ <a href="{site:/diabetes/prediabetes.html}">دليل ما قبل السكري</a>.', 'قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>.', 'اختر <a href="{site:/foods/index.html}">أطعمة منخفضة المؤشر الجلايسيمي</a>.'], consult=True),
                    nx_veryhigh=_next('ar', ['اقرأ <a href="{site:/diabetes/prediabetes.html}">دليل ما قبل السكري</a>.', 'إذا كان معك تحليل: <a href="{calc:hba1c}">حاسبة السكر التراكمي</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>كيف يعمل الاختبار؟</span></h2>
            <p>لكل جواب عدد من النقاط، ومجموع النقاط (من 0 إلى 26) يقدّر احتمال الإصابة بالسكري من النوع الثاني خلال 10 سنوات. الاختبار طُوّر في فنلندا ويُستخدم في برامج الوقاية في أوروبا.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>كيف تقيس محيط الخصر؟</span></h2>
            <p>قِف مستقيماً، وضع شريط القياس حول بطنك عند مستوى السرة، من دون شد، في نهاية زفير عادي.</p>
            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>ملاحظة للأشخاص من أصول آسيوية</span></h2>
            <p>يحسب الاختبار النقاط بحدود الخصر الأوروبية الأصلية (94 سم للرجال و80 سم للنساء). أما الاتحاد الدولي للسكري (IDF) فيعتبر الخطر عند الأشخاص من أصول جنوب آسيوية وصينية ويابانية يبدأ من 90 سم للرجال و80 سم للنساء. لم نغيّر نقاط الاختبار الأصلية، لكن إذا كنت من هذه الأصول وكان خصرك 90 سم أو أكثر فخذ نتيجتك بجدية أكبر.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>معنى النقاط</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>النقاط</th><th>الخطر خلال 10 سنوات</th></tr></thead><tbody>
            <tr><td>أقل من 7</td><td>منخفض (1 من كل 100)</td></tr><tr><td>7 إلى 11</td><td>منخفض قليلاً (1 من كل 25)</td></tr>
            <tr><td>12 إلى 14</td><td>متوسط (1 من كل 6)</td></tr><tr><td>15 إلى 20</td><td>مرتفع (1 من كل 3)</td></tr>
            <tr><td>أكثر من 20</td><td>مرتفع جداً (1 من كل 2)</td></tr></tbody></table></div>''',
            faq=[('هل هذا الاختبار يشخّص السكري؟', 'لا، هو يقدّر الاحتمال فقط. التشخيص يكون بتحليل دم (سكر الصيام أو السكر التراكمي).'),
                 ('كل كم أعيد الاختبار؟', 'كل 3 سنوات تقريباً، أو عند تغيّر وزنك أو صحتك.'),
                 ('هل يصلح للحامل؟', 'لا، ولا لمن عمره أقل من 18 سنة.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='Diabetes Risk Test: Are You at Risk of Type 2 Diabetes?',
            desc='Answer 8 simple questions in two minutes to see your risk of type 2 diabetes over the next 10 years, using the FINDRISC questionnaire used across Europe.',
            h1='Type 2 diabetes risk test', crumb='Diabetes risk test', cat='Diabetes tools',
            short='Diabetes risk test', blurb='8 questions in two minutes.',
            about=[{'name': 'Type 2 diabetes', 'condition': True}, {'name': 'Prediabetes', 'condition': True}],
            lead='This test is based on the Finnish FINDRISC questionnaire, one of the most widely used tools in Europe to estimate the chance of developing type 2 diabetes in the next ten years. You do not need a blood test, only a tape measure for your waist.',
            ui=dict(card_title='Answer the questions', btn='See my result', res_heading='Your score', risk_label='Risk over the next 10 years',
                    risk_txt='{r} people', bmi_label='Your BMI', **_Q['en'],
                    risk_low='1 in 100', risk_slight='1 in 25', risk_moderate='1 in 6', risk_high='1 in 3', risk_veryhigh='1 in 2',
                    st_low='Low risk', st_slight='Slightly raised risk', st_moderate='Moderate risk', st_high='High risk', st_veryhigh='Very high risk',
                    tip_low='Your risk is low. Keep eating well and moving every day.',
                    tip_slight='Your risk is slightly higher than normal. Daily activity and fibre-rich food lower it.',
                    tip_moderate='It is a good idea to check your HbA1c or fasting blood sugar at your next doctor visit.',
                    tip_high='A blood sugar test soon is recommended. Losing 5% of your weight and moving more clearly lower the risk.',
                    tip_veryhigh='A blood sugar test as soon as possible is recommended.',
                    nx_low=_next('en', ['Repeat the test about every 3 years.', 'Choose <a href="{site:/foods/index.html}">low glycemic index foods</a>.']),
                    nx_slight=_next('en', ['Measure your <a href="{calc:whtr}">waist-to-height ratio</a>.', 'Read the <a href="{site:/diabetes/prediabetes.html}">prediabetes guide</a>.']),
                    nx_moderate=_next('en', ['Read the <a href="{site:/diabetes/prediabetes.html}">prediabetes guide</a>.', 'If you have a lab result: <a href="{calc:hba1c}">HbA1c calculator</a>.'], consult=True),
                    nx_high=_next('en', ['Read the <a href="{site:/diabetes/prediabetes.html}">prediabetes guide</a>.', 'Measure your <a href="{calc:whtr}">waist-to-height ratio</a>.', 'Choose <a href="{site:/foods/index.html}">low glycemic index foods</a>.'], consult=True),
                    nx_veryhigh=_next('en', ['Read the <a href="{site:/diabetes/prediabetes.html}">prediabetes guide</a>.', 'If you have a lab result: <a href="{calc:hba1c}">HbA1c calculator</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>How does the test work?</span></h2>
            <p>Each answer gives a number of points. The total (0 to 26) estimates the chance of developing type 2 diabetes within 10 years. The test was developed in Finland and is used in prevention programmes across Europe.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>How to measure your waist</span></h2>
            <p>Stand up straight and put the tape measure around your belly at the level of your navel, without pulling it tight, at the end of a normal breath out.</p>
            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>A note for people of Asian origin</span></h2>
            <p>The test scores waist size with the original European limits (94 cm for men and 80 cm for women). The International Diabetes Federation (IDF) considers risk for people of South Asian, Chinese and Japanese origin to start at 90 cm for men and 80 cm for women. We have not changed the original points, but if you are of this origin and your waist is 90 cm or more, take your result more seriously.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>What the score means</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Score</th><th>Risk over 10 years</th></tr></thead><tbody>
            <tr><td>Below 7</td><td>Low (1 in 100)</td></tr><tr><td>7 to 11</td><td>Slightly raised (1 in 25)</td></tr>
            <tr><td>12 to 14</td><td>Moderate (1 in 6)</td></tr><tr><td>15 to 20</td><td>High (1 in 3)</td></tr>
            <tr><td>Above 20</td><td>Very high (1 in 2)</td></tr></tbody></table></div>''',
            faq=[('Does this test diagnose diabetes?', 'No, it only estimates the chance. Diabetes is diagnosed with a blood test (fasting blood sugar or HbA1c).'),
                 ('How often should I repeat the test?', 'About every 3 years, or when your weight or health changes.'),
                 ('Is it suitable during pregnancy?', 'No, and not for anyone under 18.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='Diabetes risicotest: loop jij risico op diabetes type 2?',
            desc='Beantwoord 8 eenvoudige vragen in twee minuten en zie je risico op diabetes type 2 in de komende 10 jaar, met de FINDRISC-vragenlijst die in Europa wordt gebruikt.',
            h1='Risicotest diabetes type 2', crumb='Diabetes risicotest', cat='Diabetestools',
            short='Diabetes risicotest', blurb='8 vragen in twee minuten.',
            about=[{'name': 'Diabetes type 2', 'condition': True}, {'name': 'Prediabetes', 'condition': True}],
            lead='Deze test is gebaseerd op de Finse FINDRISC-vragenlijst, een van de meest gebruikte hulpmiddelen in Europa om de kans op diabetes type 2 in de komende tien jaar in te schatten. Je hebt geen bloedonderzoek nodig, alleen een meetlint voor je buik.',
            ui=dict(card_title='Beantwoord de vragen', btn='Bekijk mijn uitslag', res_heading='Je score', risk_label='Risico in de komende 10 jaar',
                    risk_txt='{r} mensen', bmi_label='Je BMI', **_Q['nl'],
                    risk_low='1 op de 100', risk_slight='1 op de 25', risk_moderate='1 op de 6', risk_high='1 op de 3', risk_veryhigh='1 op de 2',
                    st_low='Laag risico', st_slight='Licht verhoogd risico', st_moderate='Matig verhoogd risico', st_high='Hoog risico', st_veryhigh='Zeer hoog risico',
                    tip_low='Je risico is laag. Blijf gevarieerd eten en dagelijks bewegen.',
                    tip_slight='Je risico is iets hoger dan normaal. Dagelijks bewegen en vezelrijk eten verlagen het.',
                    tip_moderate='Het is verstandig om bij je volgende bezoek aan de huisarts je HbA1c of nuchtere bloedsuiker te laten meten.',
                    tip_high='Laat je bloedsuiker binnenkort controleren. 5% gewichtsverlies en meer bewegen verlagen het risico duidelijk.',
                    tip_veryhigh='Laat je bloedsuiker zo snel mogelijk controleren.',
                    nx_low=_next('nl', ['Doe de test ongeveer elke 3 jaar opnieuw.', 'Kies <a href="{site:/foods/index.html}">producten met een lage glykemische index</a>.']),
                    nx_slight=_next('nl', ['Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>.', 'Lees de <a href="{site:/diabetes/prediabetes.html}">gids over prediabetes</a>.']),
                    nx_moderate=_next('nl', ['Lees de <a href="{site:/diabetes/prediabetes.html}">gids over prediabetes</a>.', 'Heb je een uitslag: <a href="{calc:hba1c}">HbA1c omrekenen</a>.'], consult=True),
                    nx_high=_next('nl', ['Lees de <a href="{site:/diabetes/prediabetes.html}">gids over prediabetes</a>.', 'Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>.', 'Kies <a href="{site:/foods/index.html}">producten met een lage glykemische index</a>.'], consult=True),
                    nx_veryhigh=_next('nl', ['Lees de <a href="{site:/diabetes/prediabetes.html}">gids over prediabetes</a>.', 'Heb je een uitslag: <a href="{calc:hba1c}">HbA1c omrekenen</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Hoe werkt de test?</span></h2>
            <p>Elk antwoord levert punten op. Het totaal (0 tot 26) schat de kans dat je binnen 10 jaar diabetes type 2 krijgt. De test is in Finland ontwikkeld en wordt in Europa gebruikt in preventieprogramma's.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Zo meet je je buikomvang</span></h2>
            <p>Ga rechtop staan en leg het meetlint om je buik ter hoogte van je navel, zonder aan te trekken, aan het einde van een normale uitademing.</p>
            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>Opmerking voor mensen van Aziatische afkomst</span></h2>
            <p>De test telt punten met de oorspronkelijke Europese grenzen voor buikomvang (94 cm voor mannen en 80 cm voor vrouwen). De International Diabetes Federation (IDF) gaat bij mensen van Zuid-Aziatische, Chinese en Japanse afkomst uit van een verhoogd risico vanaf 90 cm voor mannen en 80 cm voor vrouwen. De punten van de test hebben we niet veranderd, maar ben je van deze afkomst en is je buikomvang 90 cm of meer, neem je uitslag dan extra serieus.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Wat betekent je score?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Score</th><th>Risico in 10 jaar</th></tr></thead><tbody>
            <tr><td>Onder 7</td><td>Laag (1 op de 100)</td></tr><tr><td>7 tot 11</td><td>Licht verhoogd (1 op de 25)</td></tr>
            <tr><td>12 tot 14</td><td>Matig verhoogd (1 op de 6)</td></tr><tr><td>15 tot 20</td><td>Hoog (1 op de 3)</td></tr>
            <tr><td>Boven 20</td><td>Zeer hoog (1 op de 2)</td></tr></tbody></table></div>''',
            faq=[('Stelt deze test diabetes vast?', 'Nee, hij schat alleen de kans in. Diabetes wordt vastgesteld met bloedonderzoek (nuchtere bloedsuiker of HbA1c).'),
                 ('Hoe vaak moet ik de test doen?', 'Ongeveer elke 3 jaar, of als je gewicht of gezondheid verandert.'),
                 ('Is de test geschikt tijdens de zwangerschap?', 'Nee, en ook niet voor mensen jonger dan 18.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='Diabetes risktest: löper du risk för typ 2-diabetes?',
            desc='Svara på 8 enkla frågor på två minuter och se din risk för typ 2-diabetes de kommande 10 åren, med FINDRISC-formuläret som används i hela Europa.',
            h1='Risktest för typ 2-diabetes', crumb='Diabetes risktest', cat='Diabetesverktyg',
            short='Diabetes risktest', blurb='8 frågor på två minuter.',
            about=[{'name': 'Typ 2-diabetes', 'condition': True}, {'name': 'Prediabetes', 'condition': True}],
            lead='Testet bygger på det finska FINDRISC-formuläret, ett av de mest använda verktygen i Europa för att uppskatta risken att få typ 2-diabetes de kommande tio åren. Du behöver inget blodprov, bara ett måttband för midjan.',
            ui=dict(card_title='Svara på frågorna', btn='Visa mitt resultat', res_heading='Dina poäng', risk_label='Risk de kommande 10 åren',
                    risk_txt='{r} personer', bmi_label='Ditt BMI', **_Q['sv'],
                    risk_low='1 av 100', risk_slight='1 av 25', risk_moderate='1 av 6', risk_high='1 av 3', risk_veryhigh='1 av 2',
                    st_low='Låg risk', st_slight='Något förhöjd risk', st_moderate='Måttlig risk', st_high='Hög risk', st_veryhigh='Mycket hög risk',
                    tip_low='Din risk är låg. Fortsätt äta varierat och röra på dig varje dag.',
                    tip_slight='Din risk är något högre än normalt. Daglig rörelse och fiberrik mat sänker den.',
                    tip_moderate='Det är bra att kontrollera HbA1c eller fasteblodsocker vid ditt nästa läkarbesök.',
                    tip_high='Ett blodsockerprov snart rekommenderas. Att gå ner 5 % i vikt och röra sig mer sänker risken tydligt.',
                    tip_veryhigh='Ett blodsockerprov så snart som möjligt rekommenderas.',
                    nx_low=_next('sv', ['Gör om testet ungefär vart tredje år.', 'Välj <a href="{site:/foods/index.html}">livsmedel med lågt glykemiskt index</a>.']),
                    nx_slight=_next('sv', ['Mät din <a href="{calc:whtr}">midja-längd-kvot</a>.', 'Läs <a href="{site:/diabetes/prediabetes.html}">guiden om prediabetes</a>.']),
                    nx_moderate=_next('sv', ['Läs <a href="{site:/diabetes/prediabetes.html}">guiden om prediabetes</a>.', 'Har du ett provsvar: <a href="{calc:hba1c}">HbA1c-omvandlare</a>.'], consult=True),
                    nx_high=_next('sv', ['Läs <a href="{site:/diabetes/prediabetes.html}">guiden om prediabetes</a>.', 'Mät din <a href="{calc:whtr}">midja-längd-kvot</a>.', 'Välj <a href="{site:/foods/index.html}">livsmedel med lågt glykemiskt index</a>.'], consult=True),
                    nx_veryhigh=_next('sv', ['Läs <a href="{site:/diabetes/prediabetes.html}">guiden om prediabetes</a>.', 'Har du ett provsvar: <a href="{calc:hba1c}">HbA1c-omvandlare</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Hur fungerar testet?</span></h2>
            <p>Varje svar ger ett antal poäng. Summan (0 till 26) uppskattar risken att få typ 2-diabetes inom 10 år. Testet utvecklades i Finland och används i förebyggande program i Europa.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Så mäter du midjan</span></h2>
            <p>Stå rak och lägg måttbandet runt magen i höjd med naveln, utan att dra åt, i slutet av en vanlig utandning.</p>
            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>Om du har asiatiskt ursprung</span></h2>
            <p>Testet ger poäng för midjemåttet med de ursprungliga europeiska gränserna (94 cm för män och 80 cm för kvinnor). International Diabetes Federation (IDF) räknar med förhöjd risk från 90 cm för män och 80 cm för kvinnor hos personer med sydasiatiskt, kinesiskt eller japanskt ursprung. Vi har inte ändrat testets poäng, men om du har detta ursprung och ditt midjemått är 90 cm eller mer bör du ta resultatet på större allvar.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Vad betyder poängen?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Poäng</th><th>Risk på 10 år</th></tr></thead><tbody>
            <tr><td>Under 7</td><td>Låg (1 av 100)</td></tr><tr><td>7 till 11</td><td>Något förhöjd (1 av 25)</td></tr>
            <tr><td>12 till 14</td><td>Måttlig (1 av 6)</td></tr><tr><td>15 till 20</td><td>Hög (1 av 3)</td></tr>
            <tr><td>Över 20</td><td>Mycket hög (1 av 2)</td></tr></tbody></table></div>''',
            faq=[('Ställer testet diagnosen diabetes?', 'Nej, det uppskattar bara risken. Diabetes fastställs med blodprov (fasteblodsocker eller HbA1c).'),
                 ('Hur ofta ska jag göra testet?', 'Ungefär vart tredje år, eller när din vikt eller hälsa förändras.'),
                 ('Passar testet under graviditet?', 'Nej, och inte heller för personer under 18 år.')],
            disclaimer=SMALL['sv']),
    },
}

# ======================================================================================================== HOMA-IR + TyG
HOMA = {
    'key': 'homa', 'slug': 'insulin-resistance-calculator', 'icon': 'fa-syringe', 'badge': 'HOMA-IR · TyG', 'category': 'diabetes',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'Matthews DR, et al. Homeostasis model assessment: insulin resistance and beta-cell function from fasting plasma glucose and insulin. Diabetologia 1985;28:412-419.',
        'Simental-Mendía LE, et al. The product of fasting glucose and triglycerides as surrogate for identifying insulin resistance. Metab Syndr Relat Disord 2008;6:299-304.',
        'Gastaldelli A. Measuring and estimating insulin resistance in clinical and research settings. Obesity 2022;30:1549-1563.',
    ],
    'content': {
        'ar': dict(
            title='حساب مقاومة الإنسولين HOMA-IR: هل نتيجتك طبيعية؟',
            desc='احسب مؤشر مقاومة الإنسولين HOMA-IR من تحليل الإنسولين والسكر على الريق، ومؤشر TyG من الدهون الثلاثية، مع شرح مبسط لمعنى الرقم.',
            h1='حساب مقاومة الإنسولين (HOMA-IR) من تحليل الدم', crumb='حساب مقاومة الإنسولين', cat='أدوات السكري',
            short='حساب مقاومة الإنسولين', blurb='من تحليل الإنسولين والسكر على الريق.',
            about=[{'name': 'مقاومة الإنسولين', 'condition': True}, {'name': 'HOMA-IR'}],
            lead='مقاومة الإنسولين تعني أن الجسم يحتاج كمية أكبر من الإنسولين ليُبقي السكر طبيعياً. إذا كان معك تحليل «إنسولين صائم» و«سكر صائم» من نفس العينة، فاكتب الرقمين لتعرف مؤشر HOMA-IR. وإذا كان معك تحليل الدهون الثلاثية، نحسب لك أيضاً مؤشر TyG.',
            ui=dict(card_title='اكتب نتائج تحليلك', lbl_ins='الإنسولين الصائم', u_uiu='µU/mL (أو mIU/L)', u_pmol='pmol/L', ph_ins='مثال: 10',
                    lbl_glu='السكر الصائم', u_mgdl='mg/dL', u_mmol='mmol/L', ph_glu='مثال: 95',
                    lbl_tg='الدهون الثلاثية (اختياري)', ph_tg='مثال: 150', btn='احسب', res_heading='مؤشر HOMA-IR',
                    tyg_label='مؤشر TyG (من الدهون الثلاثية)', tyg_none='اكتب الدهون الثلاثية لحسابه',
                    tyg_low='لا يشير غالباً إلى مقاومة', tyg_high='قد يشير إلى مقاومة إنسولين',
                    st_low='لا مقاومة واضحة', st_borderline='بداية مقاومة محتملة', st_high='مقاومة إنسولين محتملة',
                    tip_low='لا يشير إلى مقاومة إنسولين واضحة.', tip_borderline='قد يشير إلى بداية مقاومة للإنسولين.',
                    tip_high='يشير غالباً إلى مقاومة إنسولين، ويُفهم مع باقي تحاليلك.',
                    nx_low=_next('ar', ['قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a> لتكمل الصورة.']),
                    nx_borderline=_next('ar', ['اقرأ <a href="{site:/insulin-resistance.html}">مقال السكر التراكمي ومقاومة الإنسولين</a>.', 'اختر <a href="{site:/foods/index.html}">أطعمة غنية بالألياف ومنخفضة المؤشر الجلايسيمي</a>.']),
                    nx_high=_next('ar', ['اقرأ <a href="{site:/insulin-resistance.html}">مقال السكر التراكمي ومقاومة الإنسولين</a>.', 'اعرف سكرك التراكمي: <a href="{calc:hba1c}">حاسبة السكر التراكمي</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>ما هي مقاومة الإنسولين بكلام بسيط؟</span></h2>
            <p>الإنسولين هو «المفتاح» الذي يُدخل السكر إلى الخلايا. عند مقاومة الإنسولين تصبح الأقفال أصعب، فيُفرز البنكرياس كمية أكبر ليبقى السكر طبيعياً. مع الوقت قد يتعب البنكرياس ويرتفع السكر.</p>
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>كيف تستعد للتحليل؟</span></h2>
            <p>صيام من 8 إلى 12 ساعة، وأن يكون السكر والإنسولين من نفس عينة الدم.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>متى لا تصلح الحاسبة؟</span></h2>
            <p>لمن يأخذ حقن الإنسولين، لأن الإنسولين في الدم يكون من الحقن. وبعض الأدوية قد تغيّر النتيجة.</p>
            <h2 class="section-title"><i class="fas fa-calculator"></i> <span>كيف تُحسب النتائج؟</span></h2>
            <p><strong>HOMA-IR</strong> = الإنسولين الصائم (µU/mL) × السكر الصائم (mmol/L) ÷ 22.5. لا يوجد حد واحد متفق عليه عالمياً، وتختلف القيم بين المختبرات وبين الشعوب، لذلك نعرض النتيجة كدليل للفهم وليس كتشخيص: أقل من 2 مطمئن غالباً، ومن 2 إلى 2.9 قد يشير إلى بداية مقاومة، و3 فأكثر يشير غالباً إلى مقاومة.</p>
            <p><strong>مؤشر TyG</strong> = ln (الدهون الثلاثية mg/dL × السكر الصائم mg/dL ÷ 2). بهذه المعادلة تكون القيم عادة بين 8 و9 تقريباً، واستخدمت الدراسات حدوداً بين 8.3 و8.8 تقريباً لمقاومة الإنسولين؛ نعرض 8.5 فأكثر كإشارة محتملة. هذا المؤشر مفيد عندما لا يتوفر تحليل الإنسولين.</p>
            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>ماذا يساعد على تحسين حساسية الإنسولين؟</span></h2>
            <p>الحركة اليومية، وتقليل دهون البطن، والأكل الغني بالألياف ومنخفض المؤشر الجلايسيمي. اقرأ المزيد في <a href="{site:/insulin-resistance.html}">مقال السكر التراكمي ومقاومة الإنسولين</a>.</p>''',
            faq=[('كم HOMA-IR الطبيعي؟', 'أغلب المصادر تعتبر أقل من 2 مطمئناً، لكن لا يوجد حد عالمي واحد.'),
                 ('هل أحتاج تحليل الإنسولين لأعرف مقاومة الإنسولين؟', 'ليس دائماً؛ محيط الخصر والدهون الثلاثية والسكر التراكمي تعطي صورة جيدة أيضاً.'),
                 ('هل تصلح الحاسبة لمن يأخذ الإنسولين؟', 'لا، لأن الإنسولين في الدم يكون من الحقن.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='HOMA-IR Calculator: Is Your Insulin Resistance Normal?',
            desc='Calculate HOMA-IR from your fasting insulin and fasting blood sugar, and the TyG index from triglycerides, with a plain explanation of what the number means.',
            h1='Insulin resistance calculator (HOMA-IR) from a blood test', crumb='Insulin resistance calculator', cat='Diabetes tools',
            short='Insulin resistance calculator', blurb='From fasting insulin and fasting blood sugar.',
            about=[{'name': 'Insulin resistance', 'condition': True}, {'name': 'HOMA-IR'}],
            lead='Insulin resistance means your body needs more insulin to keep blood sugar normal. If you have a "fasting insulin" and a "fasting glucose" result from the same blood sample, enter both to see your HOMA-IR. If you also have a triglyceride result, we calculate the TyG index too.',
            ui=dict(card_title='Enter your lab results', lbl_ins='Fasting insulin', u_uiu='µU/mL (or mIU/L)', u_pmol='pmol/L', ph_ins='e.g. 10',
                    lbl_glu='Fasting blood sugar', u_mgdl='mg/dL', u_mmol='mmol/L', ph_glu='e.g. 95',
                    lbl_tg='Triglycerides (optional)', ph_tg='e.g. 150', btn='Calculate', res_heading='HOMA-IR',
                    tyg_label='TyG index (from triglycerides)', tyg_none='Enter triglycerides to calculate it',
                    tyg_low='Usually no sign of resistance', tyg_high='May point to insulin resistance',
                    st_low='No clear resistance', st_borderline='Possible early resistance', st_high='Likely insulin resistance',
                    tip_low='No sign of clear insulin resistance.', tip_borderline='May point to early insulin resistance.',
                    tip_high='Usually points to insulin resistance; read it together with your other results.',
                    nx_low=_next('en', ['Measure your <a href="{calc:whtr}">waist-to-height ratio</a> to complete the picture.']),
                    nx_borderline=_next('en', ['Read the <a href="{site:/insulin-resistance.html}">HbA1c and insulin resistance guide</a>.', 'Choose <a href="{site:/foods/index.html}">fibre-rich, low glycemic index foods</a>.']),
                    nx_high=_next('en', ['Read the <a href="{site:/insulin-resistance.html}">HbA1c and insulin resistance guide</a>.', 'Check your HbA1c: <a href="{calc:hba1c}">HbA1c calculator</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Insulin resistance in plain words</span></h2>
            <p>Insulin is the "key" that lets sugar into your cells. With insulin resistance the locks get harder to open, so the pancreas makes more insulin to keep blood sugar normal. Over time the pancreas can tire and blood sugar rises.</p>
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>How to prepare for the test</span></h2>
            <p>Fast for 8 to 12 hours, and make sure glucose and insulin are measured in the same blood sample.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>When the calculator does not apply</span></h2>
            <p>If you inject insulin, because the insulin in your blood then comes from the injections. Some medicines can also change the result.</p>
            <h2 class="section-title"><i class="fas fa-calculator"></i> <span>How the results are calculated</span></h2>
            <p><strong>HOMA-IR</strong> = fasting insulin (µU/mL) × fasting glucose (mmol/L) ÷ 22.5. There is no single cut-off agreed worldwide, and values differ between labs and populations, so we show the result as a guide, not a diagnosis: below 2 is usually reassuring, 2 to 2.9 may point to early resistance, and 3 or more usually points to resistance.</p>
            <p><strong>TyG index</strong> = ln (triglycerides mg/dL × fasting glucose mg/dL ÷ 2). With this formula values are usually around 8 to 9; studies have used limits of about 8.3 to 8.8 for insulin resistance, and we show 8.5 or more as a possible sign. The index is useful when no insulin test is available.</p>
            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>What helps insulin sensitivity?</span></h2>
            <p>Daily movement, less belly fat, and fibre-rich, low glycemic index food. Read more in the <a href="{site:/insulin-resistance.html}">HbA1c and insulin resistance guide</a>.</p>''',
            faq=[('What is a normal HOMA-IR?', 'Most sources consider below 2 reassuring, but there is no single worldwide cut-off.'),
                 ('Do I need an insulin test to know about insulin resistance?', 'Not always; waist size, triglycerides and HbA1c also give a good picture.'),
                 ('Can I use the calculator if I take insulin?', 'No, because the insulin in your blood then comes from the injections.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='HOMA-IR berekenen: heb je insulineresistentie?',
            desc='Bereken je HOMA-IR uit je nuchtere insuline en nuchtere bloedsuiker, en de TyG-index uit je triglyceriden, met een duidelijke uitleg van de uitkomst.',
            h1='Insulineresistentie berekenen (HOMA-IR) uit bloedwaarden', crumb='Insulineresistentie berekenen', cat='Diabetestools',
            short='Insulineresistentie berekenen', blurb='Uit nuchtere insuline en nuchtere bloedsuiker.',
            about=[{'name': 'Insulineresistentie', 'condition': True}, {'name': 'HOMA-IR'}],
            lead='Insulineresistentie betekent dat je lichaam meer insuline nodig heeft om je bloedsuiker normaal te houden. Heb je een uitslag van "nuchtere insuline" en "nuchtere glucose" uit hetzelfde bloedmonster, vul dan beide in om je HOMA-IR te zien. Heb je ook een uitslag voor triglyceriden, dan berekenen we ook de TyG-index.',
            ui=dict(card_title='Vul je bloedwaarden in', lbl_ins='Nuchtere insuline', u_uiu='µU/ml (of mIU/l)', u_pmol='pmol/l', ph_ins='bijv. 10',
                    lbl_glu='Nuchtere bloedsuiker', u_mgdl='mg/dl', u_mmol='mmol/l', ph_glu='bijv. 5,3',
                    lbl_tg='Triglyceriden (optioneel)', ph_tg='bijv. 1,7', btn='Bereken', res_heading='HOMA-IR',
                    tyg_label='TyG-index (uit triglyceriden)', tyg_none='Vul triglyceriden in om hem te berekenen',
                    tyg_low='Meestal geen teken van resistentie', tyg_high='Kan wijzen op insulineresistentie',
                    st_low='Geen duidelijke resistentie', st_borderline='Mogelijk beginnende resistentie', st_high='Waarschijnlijk insulineresistentie',
                    tip_low='Geen teken van duidelijke insulineresistentie.', tip_borderline='Kan wijzen op beginnende insulineresistentie.',
                    tip_high='Wijst meestal op insulineresistentie; bekijk dit samen met je andere uitslagen.',
                    nx_low=_next('nl', ['Meet je <a href="{calc:whtr}">taille-lengteverhouding</a> voor een compleet beeld.']),
                    nx_borderline=_next('nl', ['Lees de <a href="{site:/insulin-resistance.html}">gids over HbA1c en insulineresistentie</a>.', 'Kies <a href="{site:/foods/index.html}">vezelrijke producten met een lage glykemische index</a>.']),
                    nx_high=_next('nl', ['Lees de <a href="{site:/insulin-resistance.html}">gids over HbA1c en insulineresistentie</a>.', 'Bekijk je HbA1c: <a href="{calc:hba1c}">HbA1c omrekenen</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Insulineresistentie in gewone woorden</span></h2>
            <p>Insuline is de "sleutel" die suiker je cellen in laat. Bij insulineresistentie gaan de sloten moeilijker open, dus maakt de alvleesklier meer insuline om je bloedsuiker normaal te houden. Na verloop van tijd kan de alvleesklier vermoeid raken en stijgt de bloedsuiker.</p>
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Zo bereid je je voor op het bloedonderzoek</span></h2>
            <p>Wees 8 tot 12 uur nuchter en zorg dat glucose en insuline in hetzelfde bloedmonster worden gemeten.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Wanneer is de calculator niet bruikbaar?</span></h2>
            <p>Als je insuline spuit, omdat de insuline in je bloed dan van de injecties komt. Ook sommige medicijnen kunnen de uitslag beïnvloeden.</p>
            <h2 class="section-title"><i class="fas fa-calculator"></i> <span>Zo worden de uitkomsten berekend</span></h2>
            <p><strong>HOMA-IR</strong> = nuchtere insuline (µU/ml) × nuchtere glucose (mmol/l) ÷ 22,5. Er is geen wereldwijd afgesproken grens en de waarden verschillen per laboratorium en bevolkingsgroep. Daarom tonen we de uitkomst als hulpmiddel en niet als diagnose: onder 2 is meestal geruststellend, 2 tot 2,9 kan wijzen op beginnende resistentie en 3 of hoger wijst meestal op resistentie.</p>
            <p><strong>TyG-index</strong> = ln (triglyceriden mg/dl × nuchtere glucose mg/dl ÷ 2). Met deze formule liggen de waarden meestal rond 8 tot 9; onderzoeken gebruikten grenzen van ongeveer 8,3 tot 8,8 voor insulineresistentie, en wij tonen 8,5 of hoger als mogelijk teken. De index is handig als er geen insulinemeting is.</p>
            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>Wat helpt je insulinegevoeligheid?</span></h2>
            <p>Dagelijks bewegen, minder buikvet en vezelrijk eten met een lage glykemische index. Lees meer in de <a href="{site:/insulin-resistance.html}">gids over HbA1c en insulineresistentie</a>.</p>''',
            faq=[('Wat is een normale HOMA-IR?', 'De meeste bronnen vinden onder 2 geruststellend, maar er is geen wereldwijde grens.'),
                 ('Heb ik een insulinemeting nodig om insulineresistentie te herkennen?', 'Niet altijd; buikomvang, triglyceriden en HbA1c geven ook een goed beeld.'),
                 ('Kan ik de calculator gebruiken als ik insuline spuit?', 'Nee, omdat de insuline in je bloed dan van de injecties komt.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='HOMA-IR-kalkylator: har du insulinresistens?',
            desc='Räkna ut HOMA-IR från fasteinsulin och fasteblodsocker, och TyG-index från triglycerider, med en enkel förklaring av vad värdet betyder.',
            h1='Räkna ut insulinresistens (HOMA-IR) från blodprov', crumb='Räkna ut insulinresistens', cat='Diabetesverktyg',
            short='Räkna ut insulinresistens', blurb='Från fasteinsulin och fasteblodsocker.',
            about=[{'name': 'Insulinresistens', 'condition': True}, {'name': 'HOMA-IR'}],
            lead='Insulinresistens betyder att kroppen behöver mer insulin för att hålla blodsockret normalt. Om du har provsvar för "fasteinsulin" och "fasteglukos" från samma blodprov kan du skriva in båda och se ditt HOMA-IR. Har du också ett värde för triglycerider räknar vi även ut TyG-index.',
            ui=dict(card_title='Skriv in dina provsvar', lbl_ins='Fasteinsulin', u_uiu='µU/ml (eller mIU/l)', u_pmol='pmol/l', ph_ins='t.ex. 10',
                    lbl_glu='Fasteblodsocker', u_mgdl='mg/dl', u_mmol='mmol/l', ph_glu='t.ex. 5,3',
                    lbl_tg='Triglycerider (valfritt)', ph_tg='t.ex. 1,7', btn='Beräkna', res_heading='HOMA-IR',
                    tyg_label='TyG-index (från triglycerider)', tyg_none='Skriv in triglycerider för att räkna ut det',
                    tyg_low='Oftast inget tecken på resistens', tyg_high='Kan tyda på insulinresistens',
                    st_low='Ingen tydlig resistens', st_borderline='Möjlig tidig resistens', st_high='Trolig insulinresistens',
                    tip_low='Inget tecken på tydlig insulinresistens.', tip_borderline='Kan tyda på tidig insulinresistens.',
                    tip_high='Tyder oftast på insulinresistens; tolka det tillsammans med dina andra provsvar.',
                    nx_low=_next('sv', ['Mät din <a href="{calc:whtr}">midja-längd-kvot</a> för en fullständig bild.']),
                    nx_borderline=_next('sv', ['Läs <a href="{site:/insulin-resistance.html}">guiden om HbA1c och insulinresistens</a>.', 'Välj <a href="{site:/foods/index.html}">fiberrika livsmedel med lågt glykemiskt index</a>.']),
                    nx_high=_next('sv', ['Läs <a href="{site:/insulin-resistance.html}">guiden om HbA1c och insulinresistens</a>.', 'Se ditt HbA1c: <a href="{calc:hba1c}">HbA1c-omvandlare</a>.'], consult=True)),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Insulinresistens med enkla ord</span></h2>
            <p>Insulin är "nyckeln" som släpper in socker i cellerna. Vid insulinresistens blir låsen trögare, så bukspottkörteln tillverkar mer insulin för att hålla blodsockret normalt. Med tiden kan bukspottkörteln tröttas ut och blodsockret stiga.</p>
            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Så förbereder du dig inför provet</span></h2>
            <p>Var fastande i 8 till 12 timmar och se till att glukos och insulin mäts i samma blodprov.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>När passar kalkylatorn inte?</span></h2>
            <p>Om du tar insulin, eftersom insulinet i blodet då kommer från injektionerna. Vissa läkemedel kan också påverka resultatet.</p>
            <h2 class="section-title"><i class="fas fa-calculator"></i> <span>Så räknas resultaten ut</span></h2>
            <p><strong>HOMA-IR</strong> = fasteinsulin (µU/ml) × fasteglukos (mmol/l) ÷ 22,5. Det finns ingen gräns som hela världen är överens om, och värdena skiljer sig mellan laboratorier och befolkningsgrupper. Därför visar vi resultatet som vägledning och inte som diagnos: under 2 är oftast lugnande, 2 till 2,9 kan tyda på tidig resistens och 3 eller mer tyder oftast på resistens.</p>
            <p><strong>TyG-index</strong> = ln (triglycerider mg/dl × fasteglukos mg/dl ÷ 2). Med den här formeln ligger värdena oftast kring 8 till 9; studier har använt gränser på ungefär 8,3 till 8,8 för insulinresistens, och vi visar 8,5 eller mer som ett möjligt tecken. Indexet är användbart när det inte finns något insulinprov.</p>
            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>Vad hjälper insulinkänsligheten?</span></h2>
            <p>Daglig rörelse, mindre bukfett och fiberrik mat med lågt glykemiskt index. Läs mer i <a href="{site:/insulin-resistance.html}">guiden om HbA1c och insulinresistens</a>.</p>''',
            faq=[('Vad är ett normalt HOMA-IR?', 'De flesta källor anser att under 2 är lugnande, men det finns ingen gemensam gräns i världen.'),
                 ('Behöver jag ett insulinprov för att veta om jag har insulinresistens?', 'Inte alltid; midjemått, triglycerider och HbA1c ger också en bra bild.'),
                 ('Kan jag använda kalkylatorn om jag tar insulin?', 'Nej, eftersom insulinet i blodet då kommer från injektionerna.')],
            disclaimer=SMALL['sv']),
    },
}

# ------------------------------------------------------------------------------------------------------------------
# 2026-11-23 (Dr. Wassim Habib): fasting insulin becomes optional. Many patients have no insulin test, so fasting
# glucose + triglycerides (routine tests) give the TyG index as the main result; with insulin, HOMA-IR stays the main
# result. Fields renamed so "fasting insulin" is not read as an insulin dose.
_HOMA_UPDATE = {
    'ar': dict(
        blurb='من تحليل السكر على الريق مع الدهون الثلاثية أو الإنسولين.',
        lead='مقاومة الإنسولين تعني أن الجسم يحتاج كمية أكبر من الإنسولين ليُبقي السكر طبيعياً. اكتب نتيجة تحليل السكر على الريق مع الدهون الثلاثية لنحسب لك مؤشر TyG، وهما من التحاليل الروتينية. وإذا كان معك أيضاً تحليل الإنسولين على الريق من نفس العينة نحسب لك مؤشر HOMA-IR.',
        ui=dict(lbl_glu='تحليل السكر على الريق', lbl_tg='الدهون الثلاثية (من تحليل الدهون)', hint_tg='موجودة في تحليل الدهون الروتيني.',
                lbl_ins='تحليل الإنسولين على الريق (من المختبر، اختياري)',
                hint_ins='الرقم من ورقة التحليل، وليس جرعة الإنسولين. اتركه فارغاً إذا لم تُجرِ هذا التحليل.',
                res_heading_tyg='مؤشر TyG (من السكر والدهون الثلاثية)', homa_label='مؤشر HOMA-IR (من الإنسولين)',
                homa_none='أضف تحليل الإنسولين إن كان معك',
                st_tyg_low='لا يشير غالباً إلى مقاومة', st_tyg_high='قد يشير إلى مقاومة إنسولين', st_need='نحتاج تحليلاً آخر',
                tip_tyg_low='مؤشر TyG أقل من 8.5، ولا يشير غالباً إلى مقاومة إنسولين.',
                tip_tyg_high='مؤشر TyG من 8.5 فأكثر، وقد يشير إلى مقاومة إنسولين. يُفهم مع محيط الخصر وباقي تحاليلك.',
                tip_need='السكر وحده لا يكفي لتقدير مقاومة الإنسولين. أضف الدهون الثلاثية أو تحليل الإنسولين.',
                nx_need=_next('ar', ['ليس معك تحاليل؟ قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>، فمحيط الخصر من أوضح علامات مقاومة الإنسولين.',
                                     'أو أجب عن <a href="{calc:findrisc}">اختبار خطر الإصابة بالسكري</a>، ولا يحتاج أي تحليل.'])),
        faq=('ليس معي تحليل إنسولين، هل أستطيع استخدام الحاسبة؟', 'نعم. بتحليل السكر على الريق والدهون الثلاثية نحسب لك مؤشر TyG، وهما من التحاليل الروتينية.')),
    'en': dict(
        blurb='From fasting blood sugar with triglycerides or insulin.',
        lead='Insulin resistance means your body needs more insulin to keep blood sugar normal. Enter your fasting blood sugar and triglycerides, two routine tests, and we calculate the TyG index. If you also have a fasting insulin test from the same blood sample, we calculate HOMA-IR too.',
        ui=dict(lbl_glu='Fasting blood sugar test', lbl_tg='Triglycerides (from your lipid test)', hint_tg='Part of the routine lipid (cholesterol) test.',
                lbl_ins='Fasting insulin (lab test, optional)',
                hint_ins='The number on your lab report, not your insulin dose. Leave it empty if you have not had this test.',
                res_heading_tyg='TyG index (from blood sugar and triglycerides)', homa_label='HOMA-IR (from insulin)',
                homa_none='Add your insulin test if you have one',
                st_tyg_low='Usually no sign of resistance', st_tyg_high='May point to insulin resistance', st_need='One more test needed',
                tip_tyg_low='Your TyG index is below 8.5 and usually does not point to insulin resistance.',
                tip_tyg_high='Your TyG index is 8.5 or more and may point to insulin resistance; read it together with your waist size and other results.',
                tip_need='Blood sugar alone is not enough to estimate insulin resistance. Add your triglycerides or an insulin test.',
                nx_need=_next('en', ['No lab tests? Measure your <a href="{calc:whtr}">waist-to-height ratio</a>; waist size is one of the clearest signs of insulin resistance.',
                                     'Or answer the <a href="{calc:findrisc}">diabetes risk test</a>, which needs no blood test.'])),
        faq=('I have no insulin test. Can I still use the calculator?', 'Yes. With your fasting blood sugar and triglycerides we calculate the TyG index; both are routine tests.')),
    'nl': dict(
        blurb='Uit nuchtere bloedsuiker met triglyceriden of insuline.',
        lead='Insulineresistentie betekent dat je lichaam meer insuline nodig heeft om je bloedsuiker normaal te houden. Vul je nuchtere bloedsuiker en triglyceriden in, twee standaardbepalingen, en we berekenen de TyG-index. Heb je ook een nuchtere insulinewaarde uit hetzelfde bloedmonster, dan berekenen we ook je HOMA-IR.',
        ui=dict(lbl_glu='Nuchtere bloedsuiker (bloedonderzoek)', lbl_tg='Triglyceriden (uit je cholesteroltest)', hint_tg='Onderdeel van de standaard cholesteroltest.',
                lbl_ins='Nuchtere insuline (bloedonderzoek, optioneel)',
                hint_ins='Het getal op je uitslag, niet je insulinedosis. Laat leeg als deze bepaling niet is gedaan.',
                res_heading_tyg='TyG-index (uit bloedsuiker en triglyceriden)', homa_label='HOMA-IR (uit insuline)',
                homa_none='Vul je insulinewaarde in als je die hebt',
                st_tyg_low='Meestal geen teken van resistentie', st_tyg_high='Kan wijzen op insulineresistentie', st_need='Nog een waarde nodig',
                tip_tyg_low='Je TyG-index is lager dan 8,5 en wijst meestal niet op insulineresistentie.',
                tip_tyg_high='Je TyG-index is 8,5 of hoger en kan wijzen op insulineresistentie; bekijk dit samen met je buikomvang en je andere uitslagen.',
                tip_need='Bloedsuiker alleen is niet genoeg om insulineresistentie in te schatten. Vul ook je triglyceriden of een insulinewaarde in.',
                nx_need=_next('nl', ['Geen bloedwaarden? Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>; je buikomvang is een van de duidelijkste tekenen van insulineresistentie.',
                                     'Of doe de <a href="{calc:findrisc}">diabetes risicotest</a>, daarvoor is geen bloedonderzoek nodig.'])),
        faq=('Ik heb geen insulinewaarde. Kan ik de calculator toch gebruiken?', 'Ja. Met je nuchtere bloedsuiker en triglyceriden berekenen we de TyG-index; beide zijn standaardbepalingen.')),
    'sv': dict(
        blurb='Från fasteblodsocker med triglycerider eller insulin.',
        lead='Insulinresistens betyder att kroppen behöver mer insulin för att hålla blodsockret normalt. Skriv in ditt fasteblodsocker och dina triglycerider, två vanliga rutinprover, så räknar vi ut TyG-index. Har du också ett provsvar för fasteinsulin från samma blodprov räknar vi även ut HOMA-IR.',
        ui=dict(lbl_glu='Fasteblodsocker (blodprov)', lbl_tg='Triglycerider (från blodfettsprovet)', hint_tg='Ingår i det vanliga blodfettsprovet.',
                lbl_ins='Fasteinsulin (blodprov, valfritt)',
                hint_ins='Siffran på ditt provsvar, inte din insulindos. Lämna tomt om du inte har tagit det här provet.',
                res_heading_tyg='TyG-index (från blodsocker och triglycerider)', homa_label='HOMA-IR (från insulin)',
                homa_none='Lägg till ditt insulinprov om du har ett',
                st_tyg_low='Oftast inget tecken på resistens', st_tyg_high='Kan tyda på insulinresistens', st_need='Ett prov till behövs',
                tip_tyg_low='Ditt TyG-index är under 8,5 och tyder oftast inte på insulinresistens.',
                tip_tyg_high='Ditt TyG-index är 8,5 eller mer och kan tyda på insulinresistens; tolka det tillsammans med ditt midjemått och dina andra provsvar.',
                tip_need='Blodsocker ensamt räcker inte för att uppskatta insulinresistens. Lägg till triglycerider eller ett insulinprov.',
                nx_need=_next('sv', ['Inga provsvar? Mät din <a href="{calc:whtr}">midja-längd-kvot</a>; midjemåttet är ett av de tydligaste tecknen på insulinresistens.',
                                     'Eller gör <a href="{calc:findrisc}">diabetes risktest</a>, som inte kräver något blodprov.'])),
        faq=('Jag har inget insulinprov. Kan jag ändå använda kalkylatorn?', 'Ja. Med ditt fasteblodsocker och dina triglycerider räknar vi ut TyG-index; båda är vanliga rutinprover.')),
}
for _lang, _u in _HOMA_UPDATE.items():
    _c = HOMA['content'][_lang]
    _c['blurb'], _c['lead'] = _u['blurb'], _u['lead']
    _c['ui'].update(_u['ui'])
    _c['faq'] = [_u['faq']] + _c['faq']
HOMA['modified'] = '2026-11-23'

for _lang, _c in HBA1C['content'].items():
    _c['body'] = _c['body'].replace('{TABLE}', hba1c_table(_lang))
for _lang, _c in GLUCOSE['content'].items():
    _c['body'] = _c['body'].replace('{TABLE}', glucose_table(_lang))

DIABETES_TOOLS = [HBA1C, GLUCOSE, FINDRISC, HOMA]
