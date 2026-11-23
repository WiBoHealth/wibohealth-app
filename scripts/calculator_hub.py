"""The calculators hub (calculators.html, en/, nl/, sv/calculators.html), built by generate_calculator_pages.py.

One light page with three sections (tabs as anchor links, so every tool is a plain crawlable link):
    diabetes  - Diabetes and blood sugar tools
    body      - Nutrition and body tools
    tests     - "Test yourself" quizzes
A section is shown only when it has at least one published tool. Each tool keeps its own page (one URL per tool and
language, written by the generator); the hub only links them. A tool's section comes from calc['category'] (default
'body'). The note about consulting a doctor is small print at the bottom of the page.
"""

CATEGORIES = ('diabetes', 'body', 'tests')

HUB = {
    'ar': dict(
        title='حاسبات صحية: السكر التراكمي والسعرات والبروتين والدهون',
        desc='حاسبات صحية مجانية بالعربية: السكر التراكمي، خطر السكري، مقاومة الإنسولين، الحمل الجلايسيمي، السعرات، البروتين، نسبة الدهون وكتلة الجسم، مع شرح مبسط لكل نتيجة.',
        h1='الحاسبات الصحية',
        intro='اختر الحاسبة التي تحتاجها. كل حاسبة في صفحة خاصة بها مع شرح للنتيجة ومصادرها العلمية. الحساب يتم على جهازك فقط، ولا نحفظ أي رقم تدخله.',
        tabs={'diabetes': 'السكري وسكر الدم', 'body': 'التغذية والجسم', 'tests': 'اختبر نفسك'},
        open='افتح الحاسبة', related='روابط مفيدة',
        links=[('/diabetes.html', 'السكري ومتلازمة الأيض', 'أدلة ما قبل السكري وسكري الحمل بلغة بسيطة.'),
               ('/foods.html', 'دليل الأطعمة', 'المؤشر الجلايسيمي والسعرات لأكثر من 970 طعاماً.')],
        note='هذه الحاسبات للتثقيف الصحي فقط ولا تُغني عن استشارة الطبيب.'),
    'en': dict(
        title='Free Health Calculators: Blood Sugar, Calories and Body Fat',
        desc='Free health calculators: HbA1c, diabetes risk, insulin resistance, glycemic load, calories, protein, body fat and BMI, each with a plain explanation.',
        h1='Health calculators',
        intro='Pick the calculator you need. Each one has its own page with an explanation of the result and its scientific sources. Everything is calculated on your device; we do not store anything you enter.',
        tabs={'diabetes': 'Diabetes and blood sugar', 'body': 'Nutrition and body', 'tests': 'Test yourself'},
        open='Open the calculator', related='Useful links',
        links=[('/diabetes.html', 'Diabetes', 'Plain-language guides to prediabetes and gestational diabetes.'),
               ('/foods.html', 'Food guide', 'Glycemic index and calories for more than 970 foods.')],
        note='These calculators are for health education only and do not replace advice from your doctor.'),
    'nl': dict(
        title='Gratis gezondheidscalculators: bloedsuiker, calorieën en vet',
        desc='Gratis gezondheidscalculators: HbA1c, diabetesrisico, insulineresistentie, glykemische lading, calorieën, eiwit, vetpercentage en BMI, met duidelijke uitleg.',
        h1='Gezondheidscalculators',
        intro='Kies de calculator die je nodig hebt. Elke calculator heeft een eigen pagina met uitleg over de uitkomst en de wetenschappelijke bronnen. Alles wordt op je eigen apparaat berekend; we bewaren niets van wat je invult.',
        tabs={'diabetes': 'Diabetes en bloedsuiker', 'body': 'Voeding en lichaam', 'tests': 'Test jezelf'},
        open='Open de calculator', related='Handige links',
        links=[('/diabetes.html', 'Diabetes', 'Duidelijke gidsen over prediabetes en zwangerschapsdiabetes.'),
               ('/foods.html', 'Voedingswijzer', 'Glykemische index en calorieën van meer dan 970 producten.')],
        note='Deze calculators zijn alleen bedoeld als gezondheidsvoorlichting en vervangen geen advies van je arts.'),
    'sv': dict(
        title='Gratis hälsokalkylatorer: blodsocker, kalorier och fett',
        desc='Gratis hälsokalkylatorer: HbA1c, diabetesrisk, insulinresistens, glykemisk belastning, kalorier, protein, fettprocent och BMI, med enkel förklaring.',
        h1='Hälsokalkylatorer',
        intro='Välj den kalkylator du behöver. Varje kalkylator har en egen sida med en förklaring av resultatet och de vetenskapliga källorna. Allt räknas ut på din egen enhet; vi sparar inget av det du skriver in.',
        tabs={'diabetes': 'Diabetes och blodsocker', 'body': 'Kost och kropp', 'tests': 'Testa dig själv'},
        open='Öppna kalkylatorn', related='Användbara länkar',
        links=[('/diabetes.html', 'Diabetes', 'Enkla guider om prediabetes och graviditetsdiabetes.'),
               ('/foods.html', 'Livsmedelsguide', 'Glykemiskt index och kalorier för fler än 970 livsmedel.')],
        note='Kalkylatorerna är endast avsedda som hälsoinformation och ersätter inte råd från din läkare.'),
}

HUB_CSS = """
        .hub-tabs { display: flex; flex-wrap: wrap; gap: 8px; margin: 18px 0 6px; }
        .hub-tabs a { padding: 8px 16px; border-radius: 999px; border: 1px solid var(--primary-glow); background: var(--bg-input);
            color: var(--primary); font-weight: 800; text-decoration: none; font-size: 0.92rem; }
        .hub-tabs a:hover { background: var(--primary); color: #fff; }
        .hub-section { scroll-margin-top: 90px; }
        .hub-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; margin: 10px 0 8px; }
        .hub-card { display: flex; flex-direction: column; gap: 6px; padding: 18px; border-radius: 16px; border: 1px solid var(--border-color);
            background: var(--bg-input); text-decoration: none; color: inherit; transition: border-color 0.2s, transform 0.2s; }
        .hub-card:hover { border-color: var(--primary); transform: translateY(-2px); }
        .hub-card i { font-size: 1.4rem; color: var(--primary); }
        .hub-card strong { font-size: 1.05rem; }
        .hub-card span { color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; }
        .hub-card em { margin-top: auto; color: var(--primary); font-style: normal; font-weight: 800; font-size: 0.88rem; }
        .small-print { margin-top: 30px; font-size: 0.78rem; color: var(--text-muted); line-height: 1.6; }
"""
