"""Partners page update approved by Dr. Wassim Habib (2026-11-08): real figures (900+ foods in 4 languages, 174
supplements), Boodi as a partner waitlist, "halal" kept here as a commercial exception, tied to concrete ingredient
criteria and to the optional (opt-in toggle) halal check in the Boodi app. Each 'before' must occur exactly once.
Usage: python -X utf8 -I scripts/partners_update_2026_11_08.py   (from the repo root)"""
from pathlib import Path

P = Path(__file__).resolve().parent.parent / 'partners.html'

AR = {
    'reach_1': 'أكثر من 900 صنف غذائي مدقق بأربع لغات (العربية والإنجليزية والهولندية والسويدية) في أكثر من 3,700 صفحة متخصصة، إلى جانب دليل مستقل يضم 174 مكملاً غذائياً.',
    'edge_2_tail': 'يغطي 174 مكملاً بأربع لغات.',
    'opp_2': 'تطبيق بودي: قائمة الانتظار مفتوحة الآن، مع فرصة حصرية للانضمام كشريك مؤسس عند الإطلاق التجاري. وبعد الإطلاق يمكن للعلامات الشريكة رعاية نتائج المسح والوصول إلى مستخدمي التطبيق في هولندا وأوروبا.',
    'opp_3': 'بعد إطلاق تطبيق بودي، تُدرج منتجاتك في محرك الفحص بعد مطابقتها للمعايير السريرية (المؤشر الجلايسيمي، السكريات، المكونات) ومعايير الحلال، وهي معايير مكونات محددة وقابلة للتحقق: خلو المنتج من مشتقات الخنزير والجيلاتين الحيواني والكحول، ومراجعة الإضافات (E). فحص معايير الحلال في تطبيق بودي ميزة اختيارية بالكامل يتيحها التطبيق عبر زر تبديل (Toggle Switch) لمن يرغب في تفعيلها، مما يمنح الشركاء وصولاً دقيقاً للمستهلكين المهتمين بهذا التصنيف.',
    'opp_5_figures': '(174 مكملاً و696 صفحة بأربع لغات)',
    'meta': 'شراكات ورعاية مع WiBo Health وتطبيق Boodi: جمهور مهتم بالسكري والوزن والمنتجات الحلال، أكثر من 900 صنف غذائي بأربع لغات و174 مكملاً غذائياً. أرسل مقترحك.',
    'stat_pages': 'صفحة غذائية متخصصة',
    'stat_langs': 'لغات: العربية، الإنجليزية، الهولندية، السويدية',
}
R = [
    # head
    ('content="شراكات ورعاية مع WiBo Health وتطبيق Boodi: جمهور مهتم بالسكري والوزن والمنتجات الحلال، أكثر من 650 صنفاً غذائياً و1,950 صفحة بثلاث لغات. أرسل مقترحك."',
     f'content="{AR["meta"]}"'),
    ('content="Partner with WiBo Health and the Boodi app: 650+ verified foods, 1,950 pages in Arabic, English and Dutch, GI, GL and insulin index data, and a dedicated supplements guide."',
     'content="Partner with WiBo Health and the Boodi app: 900+ foods in Arabic, English, Dutch and Swedish, GI, GL and insulin index data, and a guide to 174 supplements."'),
    ('"inLanguage": ["ar", "en", "nl"],', '"inLanguage": ["ar", "en", "nl", "sv"],'),
    # stats (HTML)
    ('<div class="stat-num">650+</div>', '<div class="stat-num">900+</div>'),
    ('<div class="stat-num">1,950</div>', '<div class="stat-num">3,700+</div>'),
    ('<div class="stat"><div class="stat-num">3</div><div class="stat-label" data-i18n="stat_langs">لغات: العربية، الإنجليزية، الهولندية</div></div>',
     f'<div class="stat"><div class="stat-num">4</div><div class="stat-label" data-i18n="stat_langs">{AR["stat_langs"]}</div></div>'),
    # Arabic defaults in the HTML
    ('<p data-i18n="reach_1_desc">أكثر من 650 صنفاً غذائياً مدققاً و1,950 صفحة متخصصة بثلاث لغات (العربية، الإنجليزية، الهولندية)، إلى جانب دليل مستقل يضم 174 مكملاً غذائياً.</p>',
     f'<p data-i18n="reach_1_desc">{AR["reach_1"]}</p>'),
    ('(Nutraceuticals &amp; Dietary Supplements) يغطي 174 مكملاً بثلاث لغات.</p>', f'(Nutraceuticals &amp; Dietary Supplements) {AR["edge_2_tail"]}</p>'),
    ('<p data-i18n="opp_2_desc">رعاية نتائج المسح وإبراز علامتك التجارية لمستخدمي تطبيق Boodi في هولندا وأوروبا، مع فرصة الانضمام كشريك مؤسس مع إطلاق التطبيق.</p>',
     f'<p data-i18n="opp_2_desc">{AR["opp_2"]}</p>'),
    ('<p data-i18n="opp_3_desc">إدراج منتجاتك في محرك الفحص بعد مطابقتها للمعايير السريرية (المؤشر الجلايسيمي، السكريات، المكونات) ومعايير الحلال (مشتقات الخنزير، الجيلاتين، الكحول، الإضافات E).</p>',
     f'<p data-i18n="opp_3_desc">{AR["opp_3"]}</p>'),
    ('<p data-i18n="opp_5_desc">قسم شراكات رئيسي ومستقل لشركات المكملات والفيتامينات: رعاية أقسام دليل المكملات (174 مكملاً و522 صفحة بثلاث لغات)',
     f'<p data-i18n="opp_5_desc">قسم شراكات رئيسي ومستقل لشركات المكملات والفيتامينات: رعاية أقسام دليل المكملات {AR["opp_5_figures"]}'),
    # Arabic dictionary
    ("'meta_desc': 'شراكات ورعاية مع WiBo Health وتطبيق Boodi: جمهور مهتم بالسكري والوزن والمنتجات الحلال، أكثر من 650 صنفاً غذائياً و1,950 صفحة بثلاث لغات. أرسل مقترحك.',",
     f"'meta_desc': '{AR['meta']}',"),
    ("'stat_langs': 'لغات: العربية، الإنجليزية، الهولندية',", f"'stat_langs': '{AR['stat_langs']}',"),
    ("'reach_1_desc': 'أكثر من 650 صنفاً غذائياً مدققاً و1,950 صفحة متخصصة بثلاث لغات (العربية، الإنجليزية، الهولندية)، إلى جانب دليل مستقل يضم 174 مكملاً غذائياً.',",
     f"'reach_1_desc': '{AR['reach_1']}',"),
    ("(Nutraceuticals &amp; Dietary Supplements) يغطي 174 مكملاً بثلاث لغات.',", f"(Nutraceuticals &amp; Dietary Supplements) {AR['edge_2_tail']}',"),
    ("'opp_2_desc': 'رعاية نتائج المسح وإبراز علامتك التجارية لمستخدمي تطبيق Boodi في هولندا وأوروبا، مع فرصة الانضمام كشريك مؤسس مع إطلاق التطبيق.',",
     f"'opp_2_desc': '{AR['opp_2']}',"),
    ("'opp_3_desc': 'إدراج منتجاتك في محرك الفحص بعد مطابقتها للمعايير السريرية (المؤشر الجلايسيمي، السكريات، المكونات) ومعايير الحلال (مشتقات الخنزير، الجيلاتين، الكحول، الإضافات E).',",
     f"'opp_3_desc': '{AR['opp_3']}',"),
    ("'opp_5_desc': 'قسم شراكات رئيسي ومستقل لشركات المكملات والفيتامينات: رعاية أقسام دليل المكملات (174 مكملاً و522 صفحة بثلاث لغات)",
     f"'opp_5_desc': 'قسم شراكات رئيسي ومستقل لشركات المكملات والفيتامينات: رعاية أقسام دليل المكملات {AR['opp_5_figures']}"),
    # English dictionary
    ("'meta_desc': 'Partner with WiBo Health and the Boodi app: an audience focused on diabetes, weight loss and halal products, 650+ verified foods and 1,950 pages in three languages.',",
     "'meta_desc': 'Partner with WiBo Health and the Boodi app: an audience focused on diabetes, weight loss and halal products, 900+ foods in four languages and 174 supplements.',"),
    ("'stat_langs': 'languages: Arabic, English, Dutch',", "'stat_langs': 'languages: Arabic, English, Dutch, Swedish',"),
    ("'reach_1_desc': 'More than 650 verified foods and 1,950 dedicated pages in three languages (Arabic, English and Dutch), plus a separate guide covering 174 dietary supplements.',",
     "'reach_1_desc': 'More than 900 verified foods in four languages (Arabic, English, Dutch and Swedish) across more than 3,700 dedicated pages, plus a separate guide covering 174 dietary supplements.',"),
    ("covering 174 supplements in three languages.',", "covering 174 supplements in four languages.',"),
    ("'opp_2_desc': 'Sponsor scan results and showcase your brand to Boodi app users in the Netherlands and across Europe, with the chance to join as a founding partner at launch.',",
     "'opp_2_desc': 'The Boodi app: the waitlist is open now, with an exclusive chance to join as a founding partner at the commercial launch. After launch, partner brands can sponsor scan results and reach app users in the Netherlands and across Europe.',"),
    ("'opp_3_desc': 'List your products in our scanning engine once they meet our clinical criteria (glycemic index, sugars, ingredients) and halal criteria (pork derivatives, gelatin, alcohol, E-number additives).',",
     "'opp_3_desc': 'Once the Boodi app launches, your products can be listed in our scanning engine after they meet our clinical criteria (glycemic index, sugars, ingredients) and halal criteria, which are specific, verifiable ingredient criteria: no pork derivatives, no animal gelatin and no alcohol, with E-number additives reviewed. The halal check in the Boodi app is a fully optional feature that users can switch on with a toggle, giving partners precise access to consumers interested in this category.',"),
    ("(174 supplements, 522 pages in three languages)", "(174 supplements, 696 pages in four languages)"),
    # Dutch dictionary
    ("'meta_desc': 'Word partner van WiBo Health en de Boodi-app: een publiek gericht op diabetes, afvallen en halal producten, 650+ gecontroleerde voedingsmiddelen en 1.950 pagina\\'s in drie talen.',",
     "'meta_desc': 'Word partner van WiBo Health en de Boodi-app: een publiek gericht op diabetes, afvallen en halal producten, 900+ voedingsmiddelen in vier talen en 174 supplementen.',"),
    ("'stat_langs': 'talen: Arabisch, Engels, Nederlands',", "'stat_langs': 'talen: Arabisch, Engels, Nederlands, Zweeds',"),
    ("'reach_1_desc': 'Meer dan 650 gecontroleerde voedingsmiddelen en 1.950 gespecialiseerde pagina\\'s in drie talen (Arabisch, Engels en Nederlands), plus een aparte gids met 174 voedingssupplementen.',",
     "'reach_1_desc': 'Meer dan 900 gecontroleerde voedingsmiddelen in vier talen (Arabisch, Engels, Nederlands en Zweeds) op meer dan 3.700 gespecialiseerde pagina\\'s, plus een aparte gids met 174 voedingssupplementen.',"),
    ("met 174 supplementen in drie talen.',", "met 174 supplementen in vier talen.',"),
    ("'opp_2_desc': 'Sponsor scanresultaten en breng uw merk onder de aandacht van Boodi-gebruikers in Nederland en Europa, met de kans om bij de lancering founding partner te worden.',",
     "'opp_2_desc': 'De Boodi-app: de wachtlijst is nu open, met een exclusieve kans om bij de commerciële lancering founding partner te worden. Na de lancering kunnen partnermerken scanresultaten sponsoren en Boodi-gebruikers in Nederland en Europa bereiken.',"),
    ("'opp_3_desc': 'Neem uw producten op in onze scanengine zodra ze voldoen aan onze klinische criteria (glykemische index, suikers, ingrediënten) en halalcriteria (varkensderivaten, gelatine, alcohol, E-nummers).',",
     "'opp_3_desc': 'Na de lancering van de Boodi-app kunnen uw producten in onze scanengine worden opgenomen zodra ze voldoen aan onze klinische criteria (glykemische index, suikers, ingrediënten) en halalcriteria: concrete, controleerbare ingrediëntcriteria, namelijk geen varkensderivaten, geen dierlijke gelatine en geen alcohol, met beoordeling van E-nummers. De halalcontrole in de Boodi-app is een volledig optionele functie die gebruikers met een schakelaar (toggle) kunnen aanzetten, zodat partners consumenten met interesse in deze categorie gericht bereiken.',"),
    ("(174 supplementen, 522 pagina\\'s in drie talen)", "(174 supplementen, 696 pagina\\'s in vier talen)"),
]

text = P.read_bytes().decode('utf-8')
for old, new in R:
    assert text.count(old) == 1, (old[:80], text.count(old))
    text = text.replace(old, new)
P.write_bytes(text.encode('utf-8'))
print('partners.html:', len(R), 'replacements')
