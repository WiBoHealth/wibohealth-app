# Swedish copy for the static Swedish homepage (/sv/index.html), built by generate_sv_homepage.py.
# T mirrors the keys of the `translations` dictionary in index.html (ar/en/nl); the generator fails if a key is missing.
# Clinical wording: HbA1c in mmol/mol, glucose in mmol/l; GI bands as on the food pages (≤55 low, 56–69 medium, ≥70 high).
# No cure/prevention claims on foods (EU 1924/2006), no religious terms (neutral wording rule).
# Article and tool links go to the English pages until their Swedish versions exist, and say so in the button text;
# the diabetes guides have Swedish pages (/sv/diabetes/).

META = dict(
    title='WiBo Health – din guide till blodsocker, glykemiskt index och sund mat',
    description=('Glykemiskt index och insulinindex för hundratals livsmedel, kalkylatorer för BMI, kaloribehov och '
                 'vätskebehov, guider om prediabetes och graviditetsdiabetes samt boodi, appen som skannar '
                 'streckkoder och ingredienser. Medicinskt granskat innehåll.'),
    keywords=('glykemiskt index, GI-värde, insulinindex, blodsocker, prediabetes, HbA1c mmol/mol, '
              'graviditetsdiabetes, BMI-kalkylator, kaloribehov, kostråd, hälsosam mat'),
    og_title='WiBo Health – din guide till blodsocker och sund mat',
    og_description=('Glykemiskt index och insulinindex för hundratals livsmedel, hälsokalkylatorer och '
                    'medicinskt granskade guider om prediabetes och graviditetsdiabetes.'),
    twitter_title='WiBo Health – din guide till blodsocker och sund mat',
    twitter_description='GI-värden, hälsokalkylatorer och medicinskt granskade guider om blodsocker.',
)

T = {
    'nav_home': 'Hem',
    'nav_scanner': '📷 Streckkodsskanner',
    'nav_foods': 'Livsmedelsguide',
    'nav_calculators': 'Kalkylatorer',
    'nav_recipes': 'Recept',
    'nav_articles': 'Artiklar',
    'nav_supplements': 'Kosttillskott',
    'nav_doctor': 'WiBo Healths medicinska team',
    'nav_my_articles': '✍️ Från det medicinska teamet',
    'nav_body_program': '🌟 Specialprogram',
    'nav_free_diet': 'Gratis kostplan 🎁',
    'nav_boodi_app': 'boodi-appen 💚',
    'logo_subtitle': 'Din guide till sund och balanserad mat',
    'floating_scanner_text': 'Skanna streckkod (ingrediensskanner)',
    'new_badge': 'NYHET 🔥',
    'scanner_banner_title': '✨ Exklusivt: boodis smarta streckkods- och ingrediensskanner!',
    'scanner_banner_desc': ('Skanna en vara i butiken och se direkt ingredienser, allergener och näringsvärden – '
                            'och hitta alternativ med mindre socker på samma hylla'),
    'scanner_banner_btn': 'Upptäck appen 📲',
    'compare_title': '🆕 Exklusivt: jämför kosttillskott!',
    'compare_desc': 'Välj 2–5 kosttillskott och jämför dem sida vid sida – användning, doser, varningar och interaktioner med läkemedel',
    'compare_btn': 'Testa nu',

    'leptin_banner_title': '🔥 Veckans artikel: Varför äter jag men blir aldrig mätt? (Leptingåtan)',
    'leptin_banner_desc': 'Om hjärnan som slutar lyssna på mättnadssignalen, sanningen om fruktsocker och hur du dämpar sötsuget på kvällen',
    'leptin_banner_btn': 'Läs guiden (på engelska) 🩺',

    'card_badge_hba1c': 'Ny medicinsk artikel 🩺',
    'card_title_hba1c': 'HbA1c och insulinresistens',
    'card_desc_hba1c': 'Förstå dina provsvar, de dolda tecknen på insulinresistens och hur kroppen kan bli känsligare för insulin igen.',
    'card_btn_hba1c': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'card_badge_fatty_liver': 'Medicinsk guide 🩺',
    'card_title_fatty_liver': 'Fettlever och fruktos',
    'card_desc_fatty_liver': 'Hur levern omvandlar flytande socker till bukfett, och hur levnadsvanor kan hjälpa levern att återhämta sig.',
    'card_btn_fatty_liver': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'card_badge_cortisol': 'Hormonguide 🩺',
    'card_title_cortisol': 'Kortisol och stressmage',
    'card_desc_cortisol': 'Stresshormonet bakom envisa viktplatåer och bukfett – och hur det skiljer sig från läkemedlet kortison.',
    'card_btn_cortisol': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'card_badge_magnesium': 'Kosttillskottsguide 💊',
    'card_title_magnesium': 'Magnesiumformer – vilken passar dig?',
    'card_desc_magnesium': 'Osäker på vilket magnesium du ska köpa? Så väljer du rätt form för sömn, muskler eller stress.',
    'card_btn_magnesium': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'card_badge_bones': 'Skeletthälsa 🦴',
    'card_title_bones': 'Kalciummyten och benskörhet',
    'card_desc_bones': 'Skelettet behöver mer än kalcium: om D-vitamin, spårämnen, fetter och rörelse.',
    'card_btn_bones': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'card_badge_fasting': 'Medicinsk guide 🔥',
    'card_title_fasting': 'Periodisk fasta och myterna i sociala medier',
    'card_desc_fasting': 'Vad forskningen säger om tillväxthormon och autofagi, myten om frukosten och hur du hanterar huvudvärk vid fasta.',
    'card_btn_fasting': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'card_badge_thyroid': 'Medicinsk guide 🦋',
    'card_title_thyroid': 'Trög sköldkörtel och långsam ämnesomsättning',
    'card_desc_thyroid': 'Om omvandlingen från T4 till T3, vad ett TSH-prov visar och inte visar, och selenets och zinkens roll.',
    'card_btn_thyroid': 'Läs artikeln (på engelska) <i class="fa-solid fa-arrow-right"></i>',
    'stat_recipes': 'Recept',
    'stat_articles': 'Artiklar',
    'stat_supplements': 'Kosttillskott',
    'browse_foods': 'Utforska livsmedel',
    'get_free_diet': 'Få en gratis kostplan',
    'install_app': 'Installera appen på din telefon',
    'feature_gi_title': 'Glykemiskt index (GI)',
    'feature_gi_desc': ('Ett mått från 0 till 100 på hur snabbt ett livsmedel höjer blodsockret. '
                        'Livsmedel med lågt GI (55 eller lägre) ger en jämnare blodsockerkurva.'),
    'feature_ii_title': 'Insulinindex (II)',
    'feature_ii_desc': ('Ett mått på hur mycket insulin kroppen frisätter efter ett livsmedel. '
                        'Bra att känna till vid diabetes och när du vill hålla vikten.'),
    'feature_nutrition_title': 'Näringsinnehåll',
    'feature_nutrition_desc': 'En databas med energi, protein, kolhydrater, fett och fiber för alla livsmedel.',
    'info_title': 'Förstå hälsomåtten',
    'info_gi_box': 'Glykemiskt index',
    'info_gi_low': 'Lågt (0–55): tas upp långsamt, ger ett jämnare blodsocker',
    'info_gi_medium': 'Medel (56–69): måttlig upptagning',
    'info_gi_high': 'Högt (70+): tas upp snabbt och höjer blodsockret fort',
    'info_ii_box': 'Insulinindex',
    'info_ii_low': 'Lågt (0–55): liten insulinfrisättning',
    'info_ii_medium': 'Medel (56–69): måttlig insulinfrisättning',
    'info_ii_high': 'Högt (70+): hög insulinfrisättning',
    'info_why_title': 'Varför spelar det roll?',
    'info_why_1': '✓ Hålla en sund vikt',
    'info_why_2': '✓ Stöd i vardagen vid diabetes',
    'info_why_3': '✓ Jämnare energi under dagen',
    'info_why_4': '✓ Goda vanor för hälsan på lång sikt',
    'cta_title': 'Börja din hälsoresa nu',
    'cta_subtitle': 'Se hälsomåtten för dina favoritlivsmedel',
    'cta_btn1': 'Få en gratis kostplan för en vecka! 🎁',
    'cta_btn2': 'Utforska livsmedel',
    'cta_btn3': 'Räkna ut ditt dagliga behov',
    'cta_btn4': 'Hälsosamma recept',
    'cta_btn5': 'Hälsoartiklar',
    'cta_btn6': 'Om WiBo Healths medicinska team',
    'footer_about': 'Om oss',
    'footer_contact': 'Kontakt',
    'nav_partners': 'Samarbeten',
    'footer_partners': 'Samarbeten',
    'footer_food_index': 'Livsmedelsregister',
    'footer_supp_index': 'Kosttillskottsregister',
    'footer_privacy': 'Integritetspolicy',
    'footer_terms': 'Användarvillkor',
    'footer_calorie_tracker': 'Kalorispårare',
    'trust_title': 'Medicinsk granskning',
    'trust_text': ('Det medicinska innehållet på WiBo Health granskas under ledning av Dr. Wassim Habib, grundare och '
                   'medicinskt ansvarig för WiBo Health Group, med stöd i dokumenterade kliniska källor som de '
                   'internationella GI-tabellerna och studier om insulinindex.'),
    'trust_btn': 'Möt vår medicinskt ansvarige',
    'footer_doctor': 'Medicinskt ansvarig',
    'footer_delete_account': 'Radera konto',
    'footer_rights': '© 2026 WiBo Health. Alla rättigheter förbehållna.',
    'pulse_badge': '⚡ Höjdpunkter',
    'pulse_c1': 'Kalkylator för kroppsmasseindex (BMI)',
    'pulse_c2': 'Kalkylator för dagligt kaloribehov (TDEE)',
    'pulse_c3': 'Kalkylator för midja-längd-kvot (WHtR)',
    'pulse_c4': 'Kalkylator för dagligt vätskebehov (EFSA)',
    'pulse_a1': 'Leptingåtan: varför äter jag men blir aldrig mätt?',
    'pulse_a2': 'HbA1c och insulinresistens',
    'pulse_a3': 'Dold fettlever och fruktos',
    'pulse_a4': 'Kortisol och stressmage',
    'pulse_a5': 'Magnesiumformer: så väljer du rätt',
    'pulse_a6': 'Kalcium och benskörhet – det du inte hört',
    'pulse_a7': 'Periodisk fasta och myterna i sociala medier',
    'pulse_a8': 'Trög sköldkörtel och långsam ämnesomsättning',
    'meals_badge': '🍳 Vad blir det till middag?',
    'meals_search_ph': 'Sök din maträtt… (t.ex. köttbullar, knäckebröd, salmon, oatmeal)',
    'meals_search_btn': 'Sök 🔍',
    'tip_label': 'Dagens tips',
    'home_articles_title': '📚 Hälsoartiklar',
    'home_articles_sub': 'Artiklar och medicinska guider som granskas av WiBo Healths medicinska team (just nu på engelska)',
    'home_articles_guides': 'Grundläggande kostguider',
    'home_articles_read': 'Läs artikeln',
    'home_articles_ar_only': '(artikeltexten är på arabiska)',
    'feat_cereal_href': '/en/articles/healthy-sugar-free-breakfast-cereals.html',
    'feat_latest_href': '/sv/diabetes/prediabetes.html',
    'feat_latest_cat': '🆕 Ny guide / Diabetes och metabol hälsa',
    'feat_latest_title': 'Prediabetes: så bromsar du utvecklingen och sänker ditt HbA1c innan det blir diabetes',
    'feat_latest_sum': ('HbA1c mellan 39 och 47 mmol/mol? Det är ännu inte diabetes. Förstå dina värden och börja en '
                        '12-veckorsplan med mat, rörelse och sömn för att komma tillbaka till normala nivåer.'),
    'feat_latest_alt': 'Balanserad frukost som stöd för blodsockret och insulinkänsligheten – WiBo Health',
    'feat_latest_btn': 'Läs hela guiden',
    'feat_gest_href': '/sv/diabetes/graviditetsdiabetes.html',
    'feat_gest_cat': '🩺 Diabetes och metabol hälsa',
    'feat_gest_title': 'Graviditetsdiabetes: normala blodsockervärden och vad du kan äta',
    'feat_gest_sum': 'Det är inte ditt fel. Vad provsvaren betyder, en trafikljuslista för maten och din dag steg för steg',
    'feat_gest_alt': 'Leende gravid kvinna i ett soligt kök med en skål bär och en avokado',
    'feat_gest_btn': 'Läs hela guiden',
    'pulse_c1_href': '/en/bmi-calculator.html',
    'pulse_c2_href': '/en/tdee-calculator.html',
    'pulse_c3_href': '/en/whtr-calculator.html',
    'pulse_c4_href': '/en/water-calculator.html',
    'feat_cereal_cat': '🌾 Ny artikel / Exklusiv guide',
    'feat_cereal_title': 'Frukostflingor utan socker: din guide till en pigg start på dagen',
    'feat_cereal_sum': 'Så avslöjar du sockret i butikens flingor, och de bästa vardagsvalen för en mättnad som håller',
    'feat_cereal_btn': 'Läs guiden (på engelska)',
    'feat_cereal_alt': 'Kvinna som äter en skål fullkornshavre med bär',
    'ha_l1': 'Medicinsk inköpsguide och glykemiskt index (på arabiska)',
    'ha_l2': 'Periodisk fasta och myterna i sociala medier',
    'ha_l3': 'HbA1c och insulinresistens',
    'ha_l4': 'Dold fettlever och insulinresistens',
    'ha_l5': 'Leptin och mättnad',
    'ha_l6': 'Trög sköldkörtel och långsam ämnesomsättning',
    'ha_l7': 'Kortisol, stresshormonet',
    'ha_l8': 'Magnesiumformer: vilken ska du välja?',
    'ha_l9': 'Skeletthälsa och mineraler',
    'ha_1_cat': 'Diabetes',
    'ha_1_title': 'Diabetes och bra mat',
    'ha_1_sum': 'En guide till att hantera diabetes med balanserad kost',
    'ha_2_cat': 'Hälsosam kost',
    'ha_2_title': 'Kostfiber och hälsan',
    'ha_2_sum': 'Varför fiber är viktigt och var du hittar det',
    'ha_3_cat': 'Hälsosam kost',
    'ha_3_title': 'Protein och musklerna',
    'ha_3_sum': 'Proteinets roll i kosten och dess olika källor',
}

# alt text by image src (the Arabic alts in index.html have no i18n key)
ALT = {
    'images/leptin-hero.jpeg': 'Varför äter jag men blir aldrig mätt?',
    'images/exercise-insulin.jpg': 'HbA1c och insulinresistens',
    'images/fatty-liver-lifestyle.jpeg': 'Fettlever och fruktos',
    'images/cortisol-lifestyle.jpeg': 'Kortisol och stressmage',
    'images/magnesium-lifestyle.jpeg': 'Guide till magnesiumformer',
    'images/himalayan-salt-bones.jpeg': 'Kalcium och skeletthälsa',
    'images/fasting-hero.jpeg': 'Periodisk fasta och myterna i sociala medier',
    'images/thyroid-hero.jpeg': 'Trög sköldkörtel och långsam ämnesomsättning',
    'images/dr-wassim.webp': 'Dr. Wassim Habib – grundare och medicinskt ansvarig, WiBo Health Group',
}

# "Vad blir det till middag?" strip: Nordic dishes that have an English food page (GI bands as on those pages)
MEALS = [
    ('/en/foods/swedish-meatballs-kottbullar-with-cream-gravy.html', '🧆', 'Köttbullar med gräddsås', 'GI lågt', 25),
    ('/en/foods/swedish-whole-rye-crispbread-knackebrod.html', '🌾', 'Fullkornsknäckebröd av råg', 'GI lågt', 48),
    ('/en/foods/nordic-gravlax-cured-salmon-with-fresh-dill.html', '🐟', 'Gravad lax med dill', 'GI ej tillämpligt', None),
    ('/en/foods/oatmeal.html', '🥣', 'Havregrynsgröt', 'GI lågt', 55),
    ('/en/foods/lentil-soup.html', '🍲', 'Linssoppa', 'GI lågt', 30),
    ('/en/foods/wild-swedish-lingonberry-jam-low-sugar.html', '🫐', 'Lingonsylt med mindre socker', 'GI lågt', 45),
    ('/en/foods/swedish-cardamom-cinnamon-bun-kanelbulle.html', '🥐', 'Kanelbulle', 'GI medel', 65),
    ('/en/foods/swedish-hasselback-accordion-roasted-potatoes.html', '🥔', 'Hasselbackspotatis', 'GI högt', 72),
]

TIPS = [
    'Livsmedel med lågt glykemiskt index hjälper till att hålla blodsockret jämnt efter måltiden.',
    'Ett glas vatten ungefär 20 minuter före maten kan hjälpa dig att känna dig mätt på en mindre portion.',
    'En promenad på 15 minuter efter maten hjälper musklerna att ta hand om blodsockret och dämpar ökningen.',
    'Börja måltiden med grönsaker och protein och ät stärkelsen sist – den ordningen dämpar blodsockertoppen.',
    'Fyll halva tallriken med grönsaker: fibrerna mättar och ger ett lugnare sockerupptag.',
    'Välj hel frukt i stället för juice: fibrerna i frukten bromsar sockrets väg ut i blodet.',
    'God sömn, 7 till 8 timmar, hjälper till att reglera aptiten och hungerhormonerna nästa dag.',
]

FOOTER_SOURCES = (
    '<h4 style="color: #10b981; margin-bottom: 15px; font-size: 1.1em;">📚 Vetenskapliga källor</h4>\n'
    '            <p style="color: #95a5a6; font-size: 0.85em; line-height: 1.8; max-width: 800px; margin: 0 auto;">\n'
    '                Närings- och hälsoinformationen på webbplatsen bygger på vetenskapliga källor, bland annat\n'
    '                <br>\n'
    '                <strong style="color: #ecf0f1;">USDA FoodData Central</strong> (USA:s jordbruksdepartements livsmedelsdatabas),\n'
    '                <strong style="color: #ecf0f1;">National Institutes of Health (NIH)</strong>,\n'
    '                <strong style="color: #ecf0f1;">World Health Organization (WHO)</strong>,\n'
    '                <strong style="color: #ecf0f1;">Mayo Clinic</strong>,\n'
    '                <strong style="color: #ecf0f1;">Harvard Medical School</strong>,\n'
    '                <strong style="color: #ecf0f1;">PubMed/NCBI</strong>\n'
    '                och andra erkända medicinska referenser.\n'
    '            </p>\n'
    '            <p style="color: #95a5a6; font-size: 0.85em; line-height: 1.8; max-width: 800px; margin: 16px auto 0;">\n'
    '                <strong style="color: #ecf0f1;">Medicinsk ansvarsfriskrivning:</strong> Innehållet på WiBo Health är avsett\n'
    '                som allmän information och utbildning. Det ersätter inte råd, diagnos eller behandling från legitimerad\n'
    '                hälso- och sjukvårdspersonal. Kontakta din vårdcentral eller ring 1177 för sjukvårdsrådgivning.\n'
    '                Vid akut fara – ring 112.\n'
    '            </p>'
)
