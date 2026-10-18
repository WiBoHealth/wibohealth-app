"""Content for the standalone calculator pages (see generate_calculator_pages.py).

Each calculator lives in its own module (calc_bmi.py, calc_tdee.py, calc_water.py, calc_whtr.py) with AR / EN / NL
copy: SEO title and description, lead, the widget strings, a long-form clinical guide (body HTML), FAQ and references.
Body placeholders: {food:slug} links a food page, {calc:key} a sibling calculator, {site:/path} a regular site page.
Editorial policy: author and publisher are the WiBo Health organisation; no personal names.
"""
from calc_bmi import BMI
from calc_tdee import TDEE
from calc_water import WATER
from calc_whtr import WHTR

CALCS = [BMI, TDEE, WATER, WHTR]

# Page chrome shared by every calculator page, per language.
T = {
    'ar': dict(
        dir='rtl', hub='الحاسبات الصحية', reviewed='إعداد ومراجعة فريق WiBo Health الطبي · 18 أكتوبر 2026',
        faq='أسئلة شائعة', related='حاسبات وأدوات مرتبطة', refs='المصادر العلمية', footer_articles='المقالات',
        foods_title='دليل الأطعمة', foods_blurb='المؤشر الجلايسيمي والسعرات لأكثر من 700 صنف.',
        boodi_title='تطبيق بودي: افحص طعامك قبل أن تأكله 💚',
        boodi_text='الأرقام وحدها لا تكفي؛ ما تأكله يحدد استجابة الإنسولين وسكر الدم. امسح باركود منتجات السوبرماركت لتعرف مؤشرها الجلايسيمي ومكوناتها وبدائلها الصحية.',
        boodi_cta='اكتشف تطبيق بودي'),
    'en': dict(
        dir='ltr', hub='Health calculators', reviewed='Prepared and reviewed by the WiBo Health medical team · 18 October 2026',
        faq='Frequently asked questions', related='Related calculators and tools', refs='Scientific sources', footer_articles='Articles',
        foods_title='Food guide', foods_blurb='Glycaemic index and calories for more than 700 foods.',
        boodi_title='The Boodi app: check your food before you eat it 💚',
        boodi_text='Numbers alone are not enough: what you eat drives your insulin and blood-sugar response. Scan supermarket barcodes to see a product’s glycaemic index, ingredients and healthier alternatives.',
        boodi_cta='Discover the Boodi app'),
    'nl': dict(
        dir='ltr', hub='Gezondheidscalculators', reviewed='Opgesteld en beoordeeld door het medische team van WiBo Health · 18 oktober 2026',
        faq='Veelgestelde vragen', related='Gerelateerde calculators en tools', refs='Wetenschappelijke bronnen', footer_articles='Artikelen',
        foods_title='Voedingsgids', foods_blurb='Glykemische index en calorieën van meer dan 700 producten.',
        boodi_title='De Boodi-app: check je eten voordat je het eet 💚',
        boodi_text='Cijfers alleen zijn niet genoeg: wat je eet bepaalt je insuline- en bloedsuikerreactie. Scan barcodes in de supermarkt en zie de glykemische index, ingrediënten en gezondere alternatieven.',
        boodi_cta='Ontdek de Boodi-app'),
}
