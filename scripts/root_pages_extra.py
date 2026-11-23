"""Arabic strings of the root pages that are not in the pages' translation dictionaries (image alts, button titles,
footer lines, meta author), with their translations. generate_root_pages.py replaces them outside <script>/<style>
on the /en/, /nl/ (and Swedish food guide) pages and fails if Arabic is left over.

Every entry: (arabic, {lang: translation}); the Arabic must appear in the page (checked).
COMMON entries are tried on every page (no error when absent).
"""

THEME = {'en': 'Toggle theme', 'nl': 'Thema wisselen', 'sv': 'Byt tema'}
CREDIT = {'en': 'Built with', 'nl': 'Gemaakt met', 'sv': 'Utvecklad med'}
CREDIT_FOR = {'en': 'for boodi', 'nl': 'voor boodi', 'sv': 'för boodi'}

COMMON = [
    ('title="المظهر"', {l: f'title="{v}"' for l, v in THEME.items()}),
    ('title="تبديل المظهر"', {l: f'title="{v}"' for l, v in THEME.items()}),
    ('title="تغيير المظهر"', {l: f'title="{v}"' for l, v in THEME.items()}),
    ('💚 مُطور بـ ', {l: f'💚 {v} ' for l, v in CREDIT.items()}),
    (' من أجل بودي', {l: f' {v}' for l, v in CREDIT_FOR.items()}),
    ('من أجل بودي', CREDIT_FOR),
    ('<meta name="author" content="فريق ويبو هيلث الطبي">', {l: '<meta name="author" content="WiBo Health">' for l in THEME}),
    ('title="المفضلة"', {'en': 'title="Favourites"', 'nl': 'title="Favorieten"', 'sv': 'title="Favoriter"'}),
    ('<meta name="author" content="فريق WiBo Health الطبي">', {l: '<meta name="author" content="WiBo Health">' for l in THEME}),
    ('<meta name="author" content="فريق ويبو هيلث الطبي | WiBo Health">', {l: '<meta name="author" content="WiBo Health">' for l in THEME}),
    ('<meta name="author" content="د. وسيم حبيب | فريق ويبو هيلث الطبي">',
     {l: '<meta name="author" content="Dr. Wassim Habib | WiBo Health">' for l in THEME}),
    ('alt="د. وسيم حبيب - مؤسس WiBo Health | Dr. Wassim Habib"',
     {'en': 'alt="Dr. Wassim Habib – founder of WiBo Health"', 'nl': 'alt="Dr. Wassim Habib – oprichter van WiBo Health"',
      'sv': 'alt="Dr. Wassim Habib – grundare av WiBo Health"'}),
]

ALTS = {   # image alts by the Arabic text
    'تطبيق بودي الرسمي - WiBo Health Group': {'en': 'The official boodi app – WiBo Health Group', 'nl': 'De officiële boodi-app – WiBo Health Group'},
    'شعار تطبيق بودي': {'en': 'boodi app logo', 'nl': 'Logo van de boodi-app'},
    'خمول الغدة الدرقية وبطء الحرق': {'en': 'Sluggish thyroid and slow metabolism', 'nl': 'Trage schildklier en langzame stofwisseling'},
    'ليش عم آكل وما عم أشبع': {'en': 'Why do I eat but never feel full?', 'nl': 'Waarom eet ik en word ik nooit verzadigd?'},
    'الصيام المتقطع وخرافات السوشيال ميديا': {'en': 'Intermittent fasting and social media myths', 'nl': 'Periodiek vasten en mythes op social media'},
    'كذبة الكالسيوم وصحة العظام': {'en': 'The calcium myth and bone health', 'nl': 'De calciummythe en botgezondheid'},
    'دليل مستويات السكر التراكمي HbA1c': {'en': 'Guide to HbA1c levels', 'nl': 'Overzicht van HbA1c-waarden'},
    'ممارسة الرياضة وتحسين حساسية الإنسولين': {'en': 'Exercise and better insulin sensitivity', 'nl': 'Beweging en een betere insulinegevoeligheid'},
    'الجوع الليلي ومقاومة هرمون الشبع': {'en': 'Night-time hunger and resistance to the satiety hormone',
                                       'nl': 'Nachtelijke honger en resistentie tegen het verzadigingshormoon'},
    'آلية عمل هرمون اللبتين وحاجز الدهون الثلاثية بالدماغ': {'en': 'How leptin works and the triglyceride barrier in the brain',
                                                           'nl': 'Hoe leptine werkt en de triglyceridenbarrière in de hersenen'},
    'الغدة الكظرية وإفراز الكورتيزول': {'en': 'The adrenal gland and cortisol release', 'nl': 'De bijnier en de afgifte van cortisol'},
    'نمط الحياة والاسترخاء لتخفيض الكورتيزول': {'en': 'Lifestyle and relaxation to lower cortisol', 'nl': 'Leefstijl en ontspanning om cortisol te verlagen'},
    'الصيام المتقطع ونشاط الجسم والحيوية': {'en': 'Intermittent fasting, energy and vitality', 'nl': 'Periodiek vasten, energie en vitaliteit'},
    'عملية الالتهام الذاتي والتنظيف الخلوي Autophagy': {'en': "Autophagy: the body's cellular clean-up", 'nl': 'Autofagie: de cellulaire schoonmaak van het lichaam'},
    'المغنيسيوم وجودة النوم والاسترخاء': {'en': 'Magnesium, sleep quality and relaxation', 'nl': 'Magnesium, slaapkwaliteit en ontspanning'},
    'بنية جزيء المغنيسيوم ومسارات الامتصاص': {'en': 'The magnesium molecule and its absorption pathways', 'nl': 'Het magnesiummolecuul en de opnameroutes'},
    'بلورات ملح الهملايا والملح البحري والعظام': {'en': 'Himalayan salt crystals, sea salt and bones', 'nl': 'Himalayazoutkristallen, zeezout en botten'},
    'الحيوية والنشاط وصحة العظام في الطبيعة': {'en': 'Vitality, activity and bone health outdoors', 'nl': 'Vitaliteit, beweging en botgezondheid in de natuur'},
    'نشاط الغدة الدرقية وحيوية الجسم': {'en': "Thyroid activity and the body's vitality", 'nl': 'Schildklieractiviteit en de vitaliteit van het lichaam'},
    'تحول هرمونات الغدة الدرقية T4 إلى T3': {'en': 'Conversion of the thyroid hormone T4 into T3', 'nl': 'Omzetting van het schildklierhormoon T4 naar T3'},
}

PAGES = {
    '/': [
        ('aria-label="النصيحة التالية"', {'en': 'aria-label="Next tip"', 'nl': 'aria-label="Volgende tip"'}),
        ('📚 المصادر العلمية', {'en': '📚 Scientific sources', 'nl': '📚 Wetenschappelijke bronnen'}),
        ('جميع المعلومات الغذائية والصحية في هذا الموقع مستمدة من مصادر علمية موثوقة بما في ذلك:',
         {'en': 'All nutrition and health information on this site is based on trusted scientific sources, including:',
          'nl': 'Alle voedings- en gezondheidsinformatie op deze site is gebaseerd op betrouwbare wetenschappelijke bronnen, waaronder:'}),
        ('(قاعدة بيانات وزارة الزراعة الأمريكية)،', {'en': '(the US Department of Agriculture database),',
                                                    'nl': '(de databank van het Amerikaanse ministerie van Landbouw),'}),
        ('</strong>،', {'en': '</strong>,', 'nl': '</strong>,'}),
        ('وغيرها من المراجع الطبية المعتمدة.', {'en': 'and other recognised medical references.', 'nl': 'en andere erkende medische referenties.'}),
    ],
    '/supplements.html': [
        ('placeholder="ابحث بالعربي أو English أو Nederlands أو Svenska..."',
         {'en': 'placeholder="Search in English, Arabic, Dutch or Swedish..."', 'nl': 'placeholder="Zoek in het Nederlands, Engels, Arabisch of Zweeds..."'}),
    ],
    '/calculators.html': [
        ('id="waterCupsPill">0 أكواب<', {'en': 'id="waterCupsPill">0 cups<', 'nl': 'id="waterCupsPill">0 glazen<'}),
    ],
    '/recipes.html': [
        ('placeholder="🔍 ابحث عن وصفة..."', {'en': 'placeholder="🔍 Search for a recipe..."'}),
    ],
    '/thyroid-health.html': [
        ('?subject=طلب%20خطة%20إعادة%20ضبط%20الغدة%20والهرمونات',
         {'en': '?subject=Question%20about%20thyroid%20and%20hormones', 'nl': '?subject=Vraag%20over%20schildklier%20en%20hormonen'}),
    ],
}
