"""Swedish copy for the static food pages (/sv/foods/<slug>.html), read by generate_food_pages.py.

Names follow Livsmedelsverket's naming style (food, then preparation) as approved by Dr. Wassim Habib (2026-10-24).
NAMES[id] = (display name for headings, form used inside sentences). Values stay those of js/data.js, as on the
AR/EN/NL pages; only the wording is Swedish. Health wording keeps to the approved site rules (EU 1924/2006: no
cure or prevention claims, no satiety claims for nutrients), Swedish decimal comma, no religious terms.

PUBLISH lists the foods that get a Swedish page (all of NAMES).
"""

# the Swedish copy as approved for publication; also the "Senast granskad" date and the sitemap lastmod
REVIEWED = '2026-10-24'
REVIEWED_TXT = '24 oktober 2026'

# foods with a Swedish page: 1-50 (samples approved 2026-10-24); set below NAMES

NAMES = {
    1: ('Vitt ris, kokt', 'kokt vitt ris'),
    2: ('Fullkornsris, kokt', 'kokt fullkornsris'),
    3: ('Vitt bröd', 'vitt bröd'),
    4: ('Fullkornsbröd av vete', 'fullkornsbröd av vete'),
    5: ('Pasta, vit, kokt', 'kokt vit pasta'),
    6: ('Fullkornspasta, kokt', 'kokt fullkornspasta'),
    7: ('Havregrynsgröt', 'havregrynsgröt'),
    8: ('Quinoa, kokt', 'kokt quinoa'),
    9: ('Bulgur, kokt', 'kokt bulgur'),
    10: ('Couscous, kokt', 'kokt couscous'),
    11: ('Majs, kokt', 'kokt majs'),
    12: ('Kornbröd', 'kornbröd'),
    13: ('Havrebröd', 'havrebröd'),
    14: ('Basmatiris, kokt', 'kokt basmatiris'),
    15: ('Freekeh (grönskördat vete)', 'freekeh'),
    16: ('Hirs, kokt', 'kokt hirs'),
    17: ('Havrekli', 'havrekli'),
    18: ('Linser, bruna/gröna, kokta', 'kokta bruna eller gröna linser'),
    19: ('Kikärter, kokta', 'kokta kikärter'),
    20: ('Bondbönor, kokta', 'kokta bondbönor'),
    21: ('Vita bönor, kokta', 'kokta vita bönor'),
    22: ('Kidneybönor, kokta', 'kokta kidneybönor'),
    23: ('Svartögda bönor, kokta', 'kokta svartögda bönor'),
    24: ('Edamamebönor, kokta', 'kokta edamamebönor'),
    25: ('Lupinbönor, kokta', 'kokta lupinbönor'),
    26: ('Potatis, kokt', 'kokt potatis'),
    27: ('Sötpotatis, ugnsbakad', 'ugnsbakad sötpotatis'),
    28: ('Pommes frites', 'pommes frites'),
    29: ('Potatismos', 'potatismos'),
    30: ('Tomat, färsk', 'färsk tomat'),
    31: ('Gurka', 'gurka'),
    32: ('Zucchini (squash)', 'zucchini'),
    33: ('Aubergine, grillad', 'grillad aubergine'),
    34: ('Morot', 'morot'),
    35: ('Broccoli, ångkokt', 'ångkokt broccoli'),
    36: ('Blomkål', 'blomkål'),
    37: ('Spenat, färsk', 'färsk spenat'),
    38: ('Jutemalva (molokhia)', 'jutemalva'),
    39: ('Okra', 'okra'),
    40: ('Champinjoner', 'champinjoner'),
    41: ('Kronärtskocka', 'kronärtskocka'),
    42: ('Grön sparris', 'grön sparris'),
    43: ('Rödbeta', 'rödbeta'),
    44: ('Ruccola', 'ruccola'),
    45: ('Lök, gul/röd', 'gul eller röd lök'),
    46: ('Vitlök', 'vitlök'),
    47: ('Grön paprika', 'grön paprika'),
    48: ('Äpple', 'äpple'),
    49: ('Banan', 'banan'),
    50: ('Apelsin', 'apelsin'),
    # batch 2 (51-100)
    51: ('Vattenmelon', 'vattenmelon'),
    52: ('Jordgubbar, färska', 'färska jordgubbar'),
    53: ('Vindruvor', 'vindruvor'),
    54: ('Ananas, färsk', 'färsk ananas'),
    55: ('Mango, färsk', 'färsk mango'),
    56: ('Blåbär', 'blåbär'),
    57: ('Hallon', 'hallon'),
    58: ('Körsbär', 'körsbär'),
    59: ('Avokado', 'avokado'),
    60: ('Fikon, färska', 'färska fikon'),
    61: ('Granatäpple, kärnor', 'granatäpplekärnor'),
    62: ('Dadlar, färska', 'färska dadlar'),
    63: ('Dadlar, torkade', 'torkade dadlar'),
    64: ('Kiwi', 'kiwi'),
    65: ('Persika', 'persika'),
    66: ('Päron', 'päron'),
    67: ('Cantaloupemelon', 'cantaloupemelon'),
    68: ('Russin', 'russin'),
    69: ('Mjölk, 3,5 % fett', 'mjölk med 3,5 % fett'),
    70: ('Skummjölk', 'skummjölk'),
    71: ('Grekisk yoghurt, 10 % fett', 'grekisk yoghurt med 10 % fett'),
    72: ('Labneh (silad yoghurt)', 'labneh'),
    73: ('Mozzarella', 'mozzarella'),
    74: ('Cheddarost, lagrad', 'lagrad cheddarost'),
    75: ('Goudaost', 'goudaost'),
    76: ('Keso', 'keso'),
    77: ('Halloumi', 'halloumi'),
    78: ('Smör', 'smör'),
    79: ('Kefir', 'kefir'),
    80: ('Mandlar, råa', 'råa mandlar'),
    81: ('Valnötter', 'valnötter'),
    82: ('Cashewnötter, rostade', 'rostade cashewnötter'),
    83: ('Pistaschnötter', 'pistaschnötter'),
    84: ('Hasselnötter', 'hasselnötter'),
    85: ('Chiafrön', 'chiafrön'),
    86: ('Linfrön', 'linfrön'),
    87: ('Pumpafrön', 'pumpafrön'),
    88: ('Solrosfrön', 'solrosfrön'),
    89: ('Jordnötter, rostade', 'rostade jordnötter'),
    90: ('Jordnötssmör, 100 % jordnötter', 'jordnötssmör'),
    91: ('Kycklingbröst, grillat', 'grillat kycklingbröst'),
    92: ('Nötbiff, grillad', 'grillad nötbiff'),
    93: ('Lammkött, grillat', 'grillat lammkött'),
    94: ('Lax, grillad', 'grillad lax'),
    95: ('Lax, rökt', 'rökt lax'),
    96: ('Torsk', 'torsk'),
    97: ('Makrill', 'makrill'),
    98: ('Tonfisk i vatten, konserverad', 'konserverad tonfisk i vatten'),
    99: ('Sardiner i olja, konserverade', 'konserverade sardiner i olja'),
    100: ('Räkor, grillade', 'grillade räkor'),
}
PUBLISH = set(NAMES)
# foods 1-50 went live with the computed Swedish copy (approved 2026-10-24) although the other languages carry
# food-specific copy; every later food needs its Swedish version in OVERRIDES
COMPUTED_COPY = set(range(1, 51))

# names that take a plural pronoun in the sentences ({det}/{dem}: "de"/"dem" instead of "det")
PLURAL = {18, 19, 20, 21, 22, 23, 24, 25, 28, 40,
          52, 53, 56, 57, 58, 60, 61, 62, 63, 68, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 99, 100}

# js/food-categories.js master groups (breadcrumb section on the food page)
GROUP_LABELS = {
    'fruits': 'Frukt och bär', 'vegetables': 'Grönsaker och sallader', 'grains_bakery': 'Bröd, spannmål och alternativ',
    'proteins_legumes': 'Protein, kött och baljväxter', 'dairy_alternatives': 'Mejeri, ost och alternativ',
    'fats_nuts': 'Fetter, nötter och oljor', 'meals_cuisines': 'Rätter, maträtter och soppor',
    'snacks_desserts': 'Snacks, desserter och sötningsmedel', 'beverages': 'Drycker', 'pantry_spices': 'Kryddor, såser och skafferi',
}

# generate_food_pages.GROUPS (group chip and ranking sentence)
GROUPS = {
    'grain': 'Spannmål och stärkelse', 'tuber': 'Potatis och rotfrukter', 'legume': 'Baljväxter', 'fruit': 'Frukt',
    'dried': 'Dadlar och torkad frukt', 'dairy_drink': 'Mjölk och mejeridrycker', 'dairy_solid': 'Mejeri och ost',
    'protein': 'Kött, fisk och ägg', 'fat': 'Fetter', 'nuts': 'Nötter och frön', 'arabic': 'Arabiska rätter',
    'fastfood': 'Snabbmat', 'sweets': 'Sötsaker och desserter', 'mexican': 'Mexikanska rätter',
    'latin': 'Latinamerikanska rätter', 'italian': 'Italienska rätter', 'spanish': 'Spanska rätter', 'french': 'Franska rätter',
    'greek': 'Grekiska rätter', 'turkish': 'Turkiska rätter', 'moroccan': 'Marockanska rätter', 'indian': 'Indiska rätter',
    'asian': 'Asiatiska rätter', 'bakery': 'Bröd och bakverk', 'sandwich': 'Smörgåsar', 'home': 'Soppor och husmanskost',
    'salad': 'Sallader', 'spice': 'Kryddor och örter', 'pantry': 'Specialingredienser', 'condiment': 'Såser, inlagt och oliver',
    'alcohol': 'Alkoholhaltiga drycker', 'veg': 'Grönsaker', 'drink': 'Drycker',
}

CARB_NOTE = ('Vid diabetes eller insulinresistens rekommenderas det alltid att utgå från måltidens totala glykemiska '
             'belastning (GL) i stället för att enbart förlita sig på det glykemiska indexet.')
NA_NOTE = 'Det här livsmedlet behöver inget glykemiskt index, men det du äter till avgör måltidens effekt på blodsockret.'

# (consumption advice, preparation, important note) for the groups of foods 1-50
TIPS = {
    'grain': ('Ät det som en del av en balanserad måltid i en måttlig portion, tillsammans med en proteinkälla och fiberrika '
              'grönsaker för att dämpa blodsockerstegringen.',
              'Välj fullkornsvarianter när det går och undvik att koka för länge: lång koktid höjer GI, medan nedkylning och '
              'återuppvärmning av kokta stärkelserika livsmedel kan sänka glukossvaret något.', CARB_NOTE),
    'tuber': ('Räkna det som måltidens stärkelsekälla snarare än som en grönsak, och ta en mindre portion om du också äter '
              'bröd eller ris.',
              'Att koka eller ugnsbaka med skalet på är bättre än att fritera eller mosa: mosning höjer GI och fritering '
              'tillför mycket energi och fett.', CARB_NOTE),
    'legume': ('Baljväxter hör till de bästa källorna till kostfiber och vegetabiliskt protein och kan delvis ersätta ris '
               'eller bröd i en måltid.',
               'Blötlägg dem väl före kokning och koka tills de är mjuka; skölj konserverade baljväxter för att minska saltet.',
               CARB_NOTE),
    'fruit': ('Ät hela frukten, gärna med skalet, i stället för juice: fibrerna bromsar sockerupptaget.',
              'Ät den färsk och i säsong; att kombinera den med en näve nötter eller yoghurt kan dämpa glukossvaret.', CARB_NOTE),
    'veg': ('Grönsaker är rika på vatten och kostfiber och kan gärna fylla halva tallriken.',
            'Ät den rå eller lätt ångkokt för att bevara vitaminerna, och använd lite olja vid tillagningen.', NA_NOTE),
}

UI = dict(
    dir='ltr', title='{name}: kalorier, glykemiskt index och näringsvärde | WiBo Health',
    desc_measured='{name}: {kcal} kcal per 100 g, glykemiskt index {gi} ({level}) enligt Atkinson 2021 och glykemisk belastning '
                  '{gl} per portion om {p} g. Fullständigt näringsvärde, tips och alternativ.',
    desc_reviewed='{name}: {kcal} kcal per 100 g, glykemiskt index {gi} ({level}, kliniskt granskad uppskattning) och glykemisk '
                  'belastning {gl} per portion om {p} g. Fullständigt näringsvärde, tips och alternativ.',
    desc_na='{name}: {kcal} kcal och {protein} g protein per 100 g. Glykemiskt index är inte tillämpligt (under 5 g tillgängliga '
            'kolhydrater). Fullständigt näringsvärde, tips och alternativ.',
    home='Hem', guide='Livsmedelsguide', gi='Glykemiskt index', gi_short='GI',   # gi_short: alternatives list (fits 320 px)
    gl='Glykemisk belastning', kcal='Kalorier', protein='Protein',
    per100='per 100 g', per_portion='per portion om {p} g', na='Ej tillämpligt',
    # badge; GI in running text (ett index: lågt) and GL in running text (en belastning: låg)
    levels=('Lågt', 'Medelhögt', 'Högt'), levels_txt=('lågt', 'medelhögt', 'högt'), levels_gl=('låg', 'medelhög', 'hög'),
    gram='g', kcal_unit='kcal', tips='💡 Smarta kostråd',
    tip_titles=('Råd om konsumtion', 'Bästa tillagningssätt', 'Viktig kostnotering'),
    table='Näringsvärde', nutrient='Näringsämne', col100='Per 100 g', colp='Per vanlig portion ({p} g)',
    rows=('Kalorier', 'Protein', 'Kolhydrater', 'Tillgängliga kolhydrater', 'Fett', 'Kostfiber'),
    ii_row='Insulinindex', ii_tested='kliniskt testat (Holt / Bao)',
    compare='Jämförelse och smarta alternativ', alt_lower='Alternativ med lägre GI:', alt_same='Närliggande livsmedel i samma familj:',
    alt_family='Smarta alternativ i samma familj:',
    lowest_note='Det här är ett av livsmedlen med lägst GI i sin grupp.',
    rank_measured='{Det} hamnar på plats {rank} av {m} uppmätta livsmedel i gruppen {group} efter glykemiskt index (lägst först).',
    rank_protein='{Det} ger {v} g protein per 100 kcal och hamnar på plats {rank} av {m} i gruppen {group} (högst först).',
    rank_kcal='{Det} innehåller {v} kcal per 100 g och hamnar på plats {rank} av {m} i gruppen {group} (lägst först).',
    lead_measured='100 g {name} innehåller {kcal} kcal och {avail} g tillgängliga kolhydrater. Det glykemiska indexet är {gi} '
                  '({level}), medelvärdet av {studies} i de internationella GI-tabellerna (Atkinson 2021). En vanlig portion om '
                  '{p} g har en glykemisk belastning på {gl} ({gl_level}).',
    lead_reviewed='100 g {name} innehåller {kcal} kcal och {avail} g tillgängliga kolhydrater. Det glykemiska indexet är {gi} '
                  '({level}), en kliniskt granskad uppskattning och ingen laboratoriemätning. En vanlig portion om {p} g har en '
                  'glykemisk belastning på {gl} ({gl_level}).',
    gi_reviewed='Kliniskt granskad uppskattning',
    rank_reviewed='Bland livsmedlen i gruppen {group} som har ett glykemiskt index ({m}) hamnar {det} på plats {rank} (lägst först).',
    src_reviewed='📚 Det glykemiska indexet för det här livsmedlet är en kliniskt granskad uppskattning från WiBo Healths medicinska '
                 'team, ingen laboratoriemätning från de internationella GI-tabellerna (Atkinson 2021).',
    reviewed_team='Granskad av WiBo Healths medicinska team · Senast granskad {date}',
    lead_na='100 g {name} innehåller {kcal} kcal och {protein} g protein. Eftersom {det} innehåller mindre än 5 g tillgängliga '
            'kolhydrater per 100 g är glykemiskt index inte tillämpligt, och den direkta effekten på blodsockret är liten.',
    boodi_title='Skanna streckkoder i butiken med boodi-appen 💚',
    boodi_text='boodi analyserar förpackade produkter direkt, granskar ingredienserna och föreslår alternativ med mindre socker '
               'från samma hylla.',
    boodi_btn='Upptäck boodi-appen',
    src_gi='📚 Vetenskapliga källor: Internationella GI-tabeller (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
    src_value='Godkänt värde: medelvärdet av {studies} (intervall {lo}–{hi}), evidensgrad {grade}.',
    src_ii='📚 Källor för insulinindex: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
    src_link='Metod och detaljer →',
    disclaimer='Ansvarsfriskrivning: informationen är vägledning för kost och levnadsvanor och är ingen medicinteknisk produkt för '
               'diagnostik enligt EU-förordningen MDR 2017/745. Den ersätter inte råd från hälso- och sjukvården.',
    # one review line for every Swedish food page, as approved (2026-10-24)
    reviewed='Granskad av <a href="{doctor}">Dr. Wassim Habib</a> | Grundare och Medicinskt Ansvarig, WiBo Health Group · '
             'Senast granskad {date}',
    portion_note='Den vanliga portionen är ungefärlig och avsedd för jämförelse.',
    theme='Byt tema', footer_rights='© 2026 WiBo Health Group. Alla rättigheter förbehållna.',
    nav=('Hem', 'Livsmedelsguide', 'Kalkylatorer', 'Kosttillskott', 'Artiklar', 'boodi-appen 💚'), privacy='Integritetspolicy',
    partners='Samarbeten', diabetes='Diabetes', methodology='Metod och vetenskapliga källor', doctor='Dr. Wassim Habib')

FAQ = dict(
    title='Vanliga frågor',
    q=('Passar {name} vid viktnedgång?', 'Hur påverkar {name} blodsockret?', 'Vad är näringsvärdet i en vanlig portion {name}?'),
    w_high='{Name} ger {kcal} kcal per 100 g, vilket är mycket energi; i en plan för viktnedgång passar {det} bara i små, avvägda '
           'mängder. En portion om {p} g ger {kcal_p} kcal.',
    w_low='Ja, i vanliga mängder. {Name} innehåller {kcal} kcal per 100 g, så en rejäl portion ger måltiden volym utan många '
          'kalorier.',
    w_protein='{Det} kan vara en del av en plan för viktnedgång: {det} ger {ppk} g protein per 100 kcal, och en portion om {p} g ger '
              '{kcal_p} kcal.',
    w_fiber='{Det} passar med måtta: {det} innehåller {fiber} g kostfiber per 100 g, och en portion om {p} g ger {kcal_p} kcal.',
    w_general='{Det} passar i en balanserad kost om du tänker på portionen: en portion om {p} g ger {kcal_p} kcal, och det viktigaste '
              'är ditt totala dagliga intag och resten av måltiden.',
    s_measured='Det glykemiska indexet är {gi} ({level}) enligt Atkinson 2021. En vanlig portion om {p} g har en glykemisk '
               'belastning på {gl} ({gl_level}){advice}',
    s_reviewed='Det glykemiska indexet är {gi} ({level}), en kliniskt granskad uppskattning och ingen laboratoriemätning. En vanlig '
               'portion om {p} g har en glykemisk belastning på {gl} ({gl_level}){advice}',
    s_advice=(', så den här portionens effekt på blodsockret är begränsad.',
              ', så det är bäst att kombinera {dem} med protein eller fiberrika grönsaker.',
              ', så det är bäst att minska eller dela upp portionen och kombinera den med protein och fiber.'),
    s_na='{Name} innehåller bara {avail} g tillgängliga kolhydrater per 100 g, så glykemiskt index är inte tillämpligt och den '
         'direkta effekten på blodsockret är liten. Måltidens effekt beror på vad du äter till, till exempel bröd, ris eller sötade såser.',
    s_na_zero='{Name} innehåller nästan inga tillgängliga kolhydrater, så glykemiskt index är inte tillämpligt och den direkta '
              'effekten på blodsockret är liten. Måltidens effekt beror på vad du äter till, till exempel bröd, ris eller sötade såser.',
    portion='En vanlig portion om {p} g {name} ger ungefär {kcal_p} kcal, {prot_p} g protein, {carb_p} g kolhydrater, {fat_p} g '
            'fett och {fib_p} g kostfiber.')

REFS_UI = dict(
    title='Referenser och vetenskapliga källor',
    measured='Värdet för glykemiskt index kommer från de internationella tabellerna: ',
    reviewed='Det glykemiska indexet för det här livsmedlet är en kliniskt granskad uppskattning från WiBo Healths medicinska team, '
             'ingen laboratoriemätning från de internationella GI-tabellerna (Atkinson 2021). GI-indelningen (lågt ≤ 55 · '
             'medelhögt 56–69 · högt ≥ 70) följer: ',
    na='Glykemiskt index är inte tillämpligt eftersom livsmedlet innehåller mindre än 5 g tillgängliga kolhydrater per 100 g, '
       'och ett GI-test kräver 25–50 g tillgängliga kolhydrater, enligt: ',
    iso='GI-indelning och testmetod: ',
    fao='Definition av tillgängliga kolhydrater och glykemisk belastning: ',
    ii='Insulinindex: ')


def studies_word(n):
    return '1 studie' if n == 1 else f'{n} studier'


# Swedish versions of the food-specific copy in food_pages_overrides.json (lead, two tips, and title/desc/faq where the
# other languages have them). Adapted to the Swedish rules: nutrients as plain facts ("innehåller"), health claims only
# in the authorised EU 432/2012 wording with their conditions of use, Livsmedelsverket advice where it applies, GI and GL
# words that match the badge bands, no religious or cultural-occasion references.
OVERRIDES = {
    51: dict(lead='En svalkande sommarfrukt som till cirka 92 % består av vatten och innehåller färgämnet lykopen. Det glykemiska '
                  'indexet är 50 (lågt), och tack vare den höga vattenhalten har en skiva på 280 g en glykemisk belastning på 10,6 (medelhög).',
             tips=('Håll dig till en måttlig portion, ungefär en skiva, och undvik att äta stora mängder på en gång.',
                   'Ät den kyld tillsammans med en bit halloumi eller lite keso för ett balanserat sommarmellanmål med både sötma och protein.')),
    52: dict(lead='Ett omtyckt bär med lite naturligt socker och ett lågt glykemiskt index (40). Jordgubbar innehåller C-vitamin och '
                  'antocyaniner, färgämnena som ger bären deras röda färg.',
             tips=('En portion på 150 g har en låg glykemisk belastning (3,6); njut av en skål som efterrätt eller blanda dem med grekisk '
                   'yoghurt och chiafrön.',
                   'Ät dem färska och väl sköljda, och undvik att doppa dem i socker eller att välja frysta jordgubbar i sockerlag.')),
    53: dict(lead='Vindruvor innehåller polyfenoler som resveratrol och har ett lågt glykemiskt index (50). Eftersom de små druvorna är så '
                  'lätta att äta i stora mängder är det klokt att tänka på portionen.',
             tips=('En måttlig portion är en liten klase, ungefär en handfull (cirka 15 druvor). Ät dem i lugn takt i stället för framför en skärm.',
                   'Prova att frysa druvorna; de blir ett kallt mellanmål som räcker längre, så att några stycken känns som tillräckligt.')),
    54: dict(lead='En tropisk frukt som innehåller enzymet bromelain. Det glykemiska indexet är medelhögt (61), så portionens storlek spelar roll.',
             tips=('Passar som efterrätt efter en proteinrik måltid; håll dig till en färsk skiva och undvik konserverad ananas i sockerlag.',
                   'Stek en skiva ananas i en torr panna i en minut med en nypa kanel; värmen lyfter fram den naturliga sötman så att du inte '
                   'behöver tillsatt socker.')),
    55: dict(lead='Många tror att mango är olämplig vid diabetes eftersom den är så söt, men enligt de internationella GI-tabellerna är det '
                  'glykemiska indexet lågt (44). Det avgörande är portionens storlek.',
             tips=('Ät en halv mango i bitar efter en proteinrik måltid eller med några nötter, och undvik färdig mangojuice med tillsatt socker.',
                   'Ät den färsk i bitar med fibrerna kvar, och prova frysta mangobitar som ett kallt alternativ till glass på sommaren.')),
    56: dict(lead='Blåbär innehåller blå antocyaniner och kostfiber och har ett lågt glykemiskt index (53). En portion på 100 g har en '
                  'glykemisk belastning på bara 6,1 (låg).',
             tips=('Ett gott tillskott till morgonens havregrynsgröt eller yoghurt; en liten näve om dagen kan ersätta söta mellanmål.',
                   'Ät dem färska eller frysta, hela i stället för som juice, så att du får med alla fibrer.')),
    57: dict(lead='Hallon hör till de fiberrikaste frukterna: 100 g innehåller 6,5 g kostfiber, vilket ger lite tillgängligt socker och ett '
                  'lågt glykemiskt index (32).',
             tips=('Ett bra val om du vill gå ner i vikt och ändå njuta av söt-syrliga bär; en portion på 100 g har en glykemisk belastning '
                   'på bara 1,8 (låg).',
                   'Ät dem färska med en näve valnötter eller råa mandlar, eller mosa dem med en gaffel och chiafrön till en enkel sylt utan '
                   'kokning och utan tillsatt socker.')),
    58: dict(lead='Körsbär har ett av de lägsta glykemiska indexen bland frukter (22) och innehåller antocyaniner och små mängder melatonin.',
             tips=('Ett gott sommarmellanmål, även på kvällen; en portion på 120 g har en låg glykemisk belastning (3,7).',
                   'Ät dem färska och hela, i lugn takt, och undvik konserverade cocktailbär i koncentrerad sockerlag.')),
    59: dict(lead='En frukt som bryter mot de vanliga fruktreglerna: av 9 g kolhydrater per 100 g är 7 g kostfiber. Avokado innehåller '
                  'kalium och främst omättat fett.',
             tips=('Ett bra alternativ till majonnäs och färdiga såser; mosa en halv avokado till frukostäggen eller bred den på en skiva fullkornsbröd.',
                   'Droppa lite citronsaft på den direkt när du skär upp den, så behåller den sin gröna färg och smak; krydda gärna med en '
                   'nypa salt och spiskummin.')),
    60: dict(lead='En klassisk medelhavsfrukt med naturlig sötma som innehåller kostfiber, kalcium och kalium. Det glykemiska indexet är '
                  'medelhögt (61), så det är klokt att tänka på hur många du äter.',
             tips=('En måttlig portion är ett eller två färska fikon; ät dem gärna med en skiva getost eller en sked labneh för att dämpa '
                   'blodsockerstegringen.',
                   'Ät hela fikonet med det tunna skalet efter att du sköljt det försiktigt. Färska fikon har betydligt lägre '
                   'sockerkoncentration än torkade.')),
    61: dict(lead='Granatäpplets kärnor innehåller polyfenoler och kostfiber och har ett lågt glykemiskt index (53).',
             tips=('Ät hela kärnorna och tugga de krispiga, fiberrika fröna, och undvik färdig eller silad granatäpplejuice utan fibrer, '
                   'som höjer blodsockret snabbare.',
                   'Strö två matskedar kärnor över en grön sallad eller grekisk yoghurt för en frisk sötma och ett gott knaprigt inslag.')),
    62: dict(lead='En traditionell frukt som innehåller kalium och kostfiber. Det glykemiska indexet är lågt (47), men sockret och energin '
                  'är koncentrerade: en portion på 70 g har en hög glykemisk belastning (22,5), så portionen är det viktigaste.',
             tips=('En lämplig portion vid diabetes eller viktnedgång är en till tre dadlar; drick gärna osötat kaffe eller te till.',
                   'Kombinera en färsk dadel med en halv tesked tahini eller en valnöt; fettet kan dämpa blodsockerstegringen.')),
    63: dict(lead='Torkningen tar bort vatten och koncentrerar socker och mineraler i varje dadel, men det glykemiska indexet är fortfarande '
                  'lågt (52). En portion på 40 g har en medelhög glykemisk belastning (13,9), så räkna mängden.',
             tips=('Ät en eller två dadlar en halvtimme före träning, eller som ett naturligt alternativ till eftermiddagens sötsaker.',
                   'Fyll en torkad dadel med en rå, osaltad mandel; knastret från mandeln och sötman från dadeln ger en god godisbit.')),
    64: dict(lead='Kiwi innehåller C-vitamin, kostfiber och enzymet aktinidin och har ett lågt glykemiskt index (52).',
             tips=('En kiwi efter lunch eller middag är en enkel efterrätt; en frukt på 75 g har en låg glykemisk belastning (4,7).',
                   'Ät den färsk, delad på mitten med en sked. Om du tycker om smaken kan du äta en väl sköljd kiwi med det tunna skalet, '
                   'som ger mer kostfiber.')),
    65: dict(lead='Sommarens doftande frukt med 39 kcal per 100 g, mycket vatten och ett lågt glykemiskt index (42).',
             tips=('Ett gott mellanmål som släcker törsten och stillar sötsuget; ät den hel med det sammetslena skalet.',
                   'Undvik konserverade persikor i sockerlag och välj färska, lite fasta persikor.')),
    66: dict(lead='Päron har ett lågt glykemiskt index (36) och innehåller mycket vatten och lösliga fibrer som pektin.',
             tips=('En bra vardagsfrukt mellan måltiderna när hungern kommer plötsligt.',
                   'Ät hela päronet med skalet efter att du sköljt det väl, och undvik konserverade päron i sockerlag.')),
    67: dict(lead='Cantaloupemelon innehåller betakaroten och består till cirka 90 % av vatten. Det glykemiska indexet är medelhögt (65), '
                  'men tack vare vattenhalten har en portion på 150 g en låg glykemisk belastning (6,9).',
             tips=('En måttlig portion är en eller två skivor; ät i lugn takt och undvik stora mängder på en gång.',
                   'Servera den kyld med några råa mandlar eller en skiva lätt saltad vit ost; protein och fett i måltiden dämpar '
                   'blodsockerstegringen.')),
    68: dict(lead='Russin är små och söta och innehåller järn och kostfiber. Det glykemiska indexet är lågt (55), men eftersom de är lätta '
                  'att äta i stora mängder och sockret är koncentrerat är portionen avgörande.',
             tips=('En lagom portion är en rågad matsked; strö den över havregrynsgröt eller en grön sallad för lite sötma.',
                   'Blötlägg en sked russin i lite varmt vatten innan du blandar dem i yoghurt eller frukost, så blir de mjukare.')),
    69: dict(lead='En näringsrik dryck som innehåller kalcium och protein. Fettet bromsar matsmältningen av mjölksockret (laktos), och det '
                  'glykemiska indexet är lågt (32).',
             tips=('Passar till frukost eller som kvällsmål; mjölkproteinet kasein tas upp långsamt.',
                   'Drick den varm eller kall utan tillsatt socker, och undvik att blanda i sötat chokladpulver eller smaksättning.')),
    70: dict(lead='För dig som räknar kalorier noga: skummjölk innehåller protein och kalcium med nästan inget fett, och det glykemiska '
                  'indexet är lågt (38).',
             tips=('Passar efter träning eller i morgonkaffet; den ger samma protein och kalcium som mjölk med 3,5 % fett med ungefär '
                   'halva energin.',
                   'Använd den till havregrynsgröt eller en enkel shake med en nypa kanel.')),
    71: dict(lead='Grekisk yoghurt silas från en del av vasslen, vilket ger mindre laktos och mer protein än vanlig yoghurt. Med 3,9 g '
                  'kolhydrater per 100 g är glykemiskt index inte tillämpligt.',
             tips=('Ett bra eftermiddagsmellanmål; ät den med några bär eller en nypa kanel.',
                   'Välj naturell grekisk yoghurt och undvik färdiga fruktyoghurtar med tillsatt socker.')),
    72: dict(lead='En klassiker på det levantinska frukostbordet: silad yoghurt med fett och protein och nästan inga snabba kolhydrater.',
             tips=('Passar som dipp till gurk- och morotsstavar och mynta i stället för bröd, eller till en skiva rostat fullkornsbröd.',
                   "Servera med za'atar, en tesked extra jungfruolivolja och några svarta oliver för en medelhavsmåltid.")),
    73: dict(lead='Den italienska osten med mjuk konsistens innehåller protein och kalcium och nästan inga kolhydrater, så den påverkar '
                  'blodsockret mycket lite.',
             tips=('Passar till frukost eller som mellanmål.',
                   'Gör en klassisk caprese med tomatskivor och basilika, ringlad med extra jungfruolivolja.')),
    74: dict(lead='En skiva cheddar innehåller mycket kalcium, protein och fett. Under den långa lagringen bryts laktosen ned, så osten är '
                  'praktiskt taget fri från kolhydrater och påverkar knappt blodsockret.',
             tips=('Ett snabbt mellanmål, men energitätheten (403 kcal per 100 g) gör att en eller två skivor räcker.',
                   'Riv lite över kokta ägg eller ångade grönsaker för en fyllig smak i stället för färdiga såser.')),
    75: dict(lead='En klassisk holländsk ost där lagringen bryter ned det mesta av laktosen. Gouda innehåller kalcium och K2-vitamin.',
             tips=('Ett mellanmål med praktiskt taget inga kolhydrater, men energitätheten (356 kcal per 100 g) gör att en eller två skivor räcker.',
                   'Ät en skiva gouda med gurkskivor eller en valnöt i stället för salta kex.')),
    76: dict(lead='Keso innehåller 11 g protein per 100 g, främst kasein, med bara 98 kcal och 4,3 g fett, och påverkar inte blodsockret nämnvärt.',
             tips=('Passar som kvällsmål eller till frukost. Protein bidrar till att bibehålla muskelmassan.',
                   "Mosa den med olivolja, svartkummin, en nypa za'atar eller spiskummin och gurkbitar till en god dipp i stället för färdiga "
                   'ostar med härdat fett.')),
    77: dict(lead='Den omtyckta osten med fast konsistens smälter inte vid uppvärmning. Den är fri från stärkelse och innehåller mycket protein.',
             tips=('Passar till sallader eller som proteinrik frukost; tänk bara på salthalten.',
                   'Stek den i en torr non-stick-panna utan olja tills den får fin färg, eller lägg den i ljummet vatten i tio minuter före '
                   'tillagning för att minska saltheten.')),
    78: dict(lead='Ett naturligt fett som innehåller A- och D-vitamin och smörsyra (butyrat). Smör innehåller inga kolhydrater och har '
                  'inget glykemiskt index.',
             tips=('Använd smör med måtta i matlagningen; fett i måltiden kan dämpa blodsockerstegringen efter stärkelserik mat.',
                   'Använd små, avmätta mängder (en tesked), eftersom smör är mycket energität (717 kcal per 100 g).')),
    79: dict(lead='En fermenterad mjölkdryck med levande mjölksyrabakterier som under fermenteringen bryter ned en stor del av laktosen. '
                  'Det glykemiska indexet är lågt (36).',
             tips=('Ett enkelt sätt att få in fermenterade mejeriprodukter i vardagen, som en del av en varierad kost.',
                   'Drick ett kallt glas på morgonen eller mellan måltiderna, och undvik smaksatt kefir, som ofta innehåller tillsatt socker.')),
    80: dict(lead='Mandlar innehåller magnesium, E-vitamin och enkelomättat fett och har ett mycket lågt glykemiskt index (15).',
             tips=('Ät en liten näve om dagen som mellanmål eller tillsammans med en dadel eller frukt; fett och protein i mandlarna dämpar '
                   'blodsockerstegringen.',
                   'Ät dem råa med det tunna bruna skalet, och undvik mandlar rostade i härdat fett eller täckta med mycket salt och socker.')),
    81: dict(lead='Valnötter innehåller den växtbaserade omega-3-fettsyran alfa-linolensyra (ALA) och har ett mycket lågt glykemiskt index '
                  '(15). Valnötter bidrar till att förbättra blodkärlens elasticitet; den gynnsamma effekten uppnås vid ett dagligt intag '
                  'av 30 g valnötter.',
             tips=('30 g om dagen (ungefär 6–7 hela valnötter) räcker; nötterna är energitäta (654 kcal per 100 g).',
                   'Strö krossade valnötter över gröna sallader eller yoghurt för en god krispighet.')),
    82: dict(lead='En av de krämigaste nötterna, med ett mycket lågt glykemiskt index (25) och främst enkelomättat fett. Cashewnötter '
                  'innehåller även mineraler som koppar, magnesium och järn.',
             tips=('Mät upp en lagom näve (cirka 30 g, 18–20 nötter), och välj torrostade eller råa cashewnötter utan tillsatt härdat fett '
                   'eller mycket salt.',
                   'Undvik honungsrostade eller sockerglaserade varianter; den naturliga smöriga smaken räcker gott.'),
             title='Cashewnötter: kalorier, näringsvärde, portioner och GI | WiBo Health',
             desc='En näve rostade cashewnötter (30 g) ger 166 kcal (553 kcal per 100 g) och har ett mycket lågt GI på 25. Läs om protein, '
                  'fett, mineraler och portionsstorlek.',
             faq=[dict(q='Hur många kalorier finns i en näve cashewnötter?',
                       a='En vanlig näve (cirka 30 g eller 18–20 nötter) ger ungefär 166 kcal, 5,4 g protein och 13 g fett, främst omättat.'),
                  dict(q='Höjer cashewnötter blodsockret snabbt?',
                       a='Nej. Med ett mycket lågt glykemiskt index (25) och en glykemisk belastning på bara 2 per portion ger '
                         'cashewnötter ingen snabb blodsockerstegring.'),
                  dict(q='Kan cashewnötter ingå i en plan för viktnedgång?',
                       a='Ja, i avmätta portioner. De är energitäta (553 kcal per 100 g), så håll dig till en näve (30 g) om dagen.')]),
    83: dict(lead='Pistaschnötternas gröna färg kommer bland annat från lutein och karotenoider. De innehåller mycket protein och har ett '
                  'mycket lågt glykemiskt index (15).',
             tips=('En portion på 30 g motsvarar ungefär 45 pistaschnötter; att skala dem för hand gör att du äter i lugnare takt.',
                   'Ät dem råa eller lätt rostade i skalet, och använd dem som topping på havregrynsgröt eller sallad i stället för söta bakverk.')),
    84: dict(lead='Hasselnötter innehåller folat, E-vitamin och enkelomättat fett och har ett mycket lågt glykemiskt index (15). E-vitamin '
                  'bidrar till att skydda cellerna mot oxidativ stress.',
             tips=('Några hasselnötter till morgonkaffet är ett enkelt mellanmål; en portion på 30 g räcker.',
                   'Gör ett eget hasselnötssmör genom att mixa nötterna med lite kakao, som ett alternativ till söta chokladkrämer.')),
    85: dict(lead='Chiafrön innehåller mycket kostfiber (34 g per 100 g) och omega-3-fettsyran ALA. De kan suga upp många gånger sin vikt i '
                  'vätska och bilda en gel, och det glykemiska indexet är mycket lågt (15).',
             tips=('Använd en matsked (cirka 15 g) om dagen i yoghurt, gröt eller ett glas vatten; för förpackade chiafrön rekommenderas '
                   'högst 15 g per dag.',
                   'Blötlägg alltid fröna i vätska (vatten, mjölk eller yoghurt) i 15 minuter innan du äter dem, så att gelen bildas.')),
    86: dict(lead='Linfrön innehåller lignaner och omega-3-fettsyran ALA, och nästan alla kolhydrater i dem är kostfiber.',
             tips=('Strö en tesked malda linfrön över sallad eller grönsakssoppa. ALA bidrar till att bibehålla normala kolesterolhalter i '
                   'blodet; den gynnsamma effekten uppnås vid ett dagligt intag av 2 g ALA.',
                   'Mal linfröna strax innan du äter dem, eftersom hela frön ofta passerar tarmen osmälta, och förvara malda linfrön i kylskåp.')),
    87: dict(lead='Pumpafrön innehåller zink, magnesium och vegetabiliskt protein och har ett lågt glykemiskt index (25). Zink bidrar till '
                  'immunsystemets normala funktion, och magnesium bidrar till normal muskelfunktion.',
             tips=('Ett bra kvällsmellanmål som inte påverkar blodsockret nämnvärt; en portion på 30 g räcker.',
                   'Ät dem råa eller lätt rostade i ugnen med en nypa salt och spiskummin, och undvik kraftigt saltade frön.')),
    88: dict(lead='Solrosfrön innehåller E-vitamin, selen och omättat fett och har ett mycket lågt glykemiskt index (20). E-vitamin bidrar '
                  'till att skydda cellerna mot oxidativ stress.',
             tips=('Ett krispigt mellanmål; att skala fröna för hand gör att du äter långsammare och lättare stannar vid en måttlig näve.',
                   'Välj osaltade eller lätt saltade frön, och strö skalade frön över sallader eller bröd.')),
    89: dict(lead='Jordnöten är egentligen en baljväxt. Den innehåller mycket vegetabiliskt protein och fett och har ett mycket lågt '
                  'glykemiskt index (14).',
             tips=('Ett prisvärt och näringsrikt mellanmål; ät dem gärna med det tunna röda skalet, som innehåller polyfenoler.',
                   'Undvik kraftigt saltade eller smaksatta jordnötter och nötter i härdat fett; välj torrostade jordnötter med skal.')),
    90: dict(lead='Jordnötssmör kombinerar krämig konsistens med protein och fett och har ett mycket lågt glykemiskt index (14).',
             tips=('Bred en matsked på äppelskivor eller rostat fullkornsbröd; tillsammans med stärkelse ger det en balanserad frukost som '
                   'dämpar blodsockerstegringen.',
                   "Välj jordnötssmör märkt '100 % jordnötter', utan palmolja eller tillsatt socker (den naturliga oljan lägger sig överst).")),
    91: dict(lead='En mager proteinkälla utan kolhydrater: 100 g innehåller 31 g protein och 3,6 g fett och påverkar inte blodsockret. '
                  'Protein bidrar till att öka muskelmassan.',
             tips=('Ät det gärna först i måltiden, före stärkelsen på tallriken; det kan dämpa blodsockerstegringen efter måltiden.',
                   'Krydda med olivolja, citron och örter som timjan och rosmarin och tillaga i ugn eller torr panna; undvik panering och fritering.')),
    92: dict(lead='Nötkött innehåller järn, zink och B12-vitamin i en form som kroppen tar upp väl. Det är fritt från stärkelse och höjer '
                  'inte blodsockret.',
             tips=('Välj magra styckningsdetaljer med lite synligt fett. Livsmedelsverket rekommenderar högst 350 g rött kött och chark i '
                   'veckan (tillagad vikt).',
                   'Grilla biffen medium så att den blir mör, och ät den med en grön sallad med citron; C-vitamin ökar järnupptaget.')),
    93: dict(lead='Ett smakrikt kött med naturligt fett. Det innehåller ingen stärkelse och påverkar inte blodsockret, men den höga energi- '
                  'och fetthalten kräver måttliga portioner.',
             tips=('Ät det med en fiberrik grön sallad. Lamm räknas som rött kött, och Livsmedelsverket rekommenderar högst 350 g rött kött '
                   'och chark i veckan (tillagad vikt).',
                   'Tillaga det i ugn eller på grill och häll bort överflödigt smält fett; undvik att steka i mycket tillsatt olja.')),
    94: dict(lead='Lax innehåller omega-3-fettsyrorna EPA och DHA men inga kolhydrater. EPA och DHA bidrar till hjärtats normala funktion; '
                  'den gynnsamma effekten uppnås vid ett dagligt intag av 250 mg EPA och DHA.',
             tips=('Livsmedelsverket rekommenderar fisk och skaldjur 2–3 gånger i veckan, och fet fisk som lax är ett bra val.',
                   'Grilla den med lite olivolja, citronsaft och färsk vitlök, och undvik att tillaga den tills den blir torr.')),
    95: dict(lead='Rökt lax kombinerar omega-3-fett med protein och innehåller ingen stärkelse, så glykemiskt index är inte tillämpligt.',
             tips=('Passar till frukost; lägg den på gurkskivor eller ett kokt ägg med dill och citron. Om du är gravid avråder '
                   'Livsmedelsverket från kallrökt och gravad fisk på grund av risken för listeria.',
                   'Tänk på salthalten från rökningen, drick tillräckligt med vatten och salta inte maten extra.')),
    96: dict(lead='En av de magraste proteinkällorna från havet: vitt, mört kött med nästan inget fett och inga kolhydrater.',
             tips=('En lätt middag; torsk ger protein av hög kvalitet utan att kännas tung före sänggåendet.',
                   'Baka den i ugn med tomatskivor, vitlök och olivolja, och undvik att fritera den i mjöl och mycket olja.')),
    97: dict(lead='Makrill är en fet fisk som innehåller omega-3-fettsyrorna EPA och DHA och D-vitamin, men inga kolhydrater.',
             tips=('Ett prisvärt alternativ till lax. EPA och DHA bidrar till hjärtats normala funktion; den gynnsamma effekten uppnås vid '
                   'ett dagligt intag av 250 mg EPA och DHA.',
                   'Grilla eller ugnsbaka den med citronskivor, spiskummin och koriander; de naturliga oljorna håller den saftig utan mycket '
                   'tillsatt olja.')),
    98: dict(lead='Ett snabbt och praktiskt val: mycket protein och lite fett, nästan utan kolhydrater.',
             tips=('En snabb lunch; blanda den i en stor sallad med gurka för en måltid under 200 kcal.',
                   'Välj tonfisk i vatten och låt den rinna av ordentligt.')),
    99: dict(lead='Små fiskar som ger kalcium när du äter de mjuka benen, tillsammans med protein och omega-3-fett, men inget socker.',
             tips=('En prisvärd snabbmåltid; en burk räcker till en måltid.',
                   'Häll av oljan från burken, ringla över extra jungfruolivolja, citronsaft och svartpeppar och ät med gurk- och paprikaskivor.')),
    100: dict(lead='Räkor ger magert protein av hög kvalitet och innehåller selen, zink och jod; 100 g ger bara 99 kcal och ingen stärkelse. '
                   'Jod bidrar till normal produktion av sköldkörtelhormoner och normal sköldkörtelfunktion.',
              tips=('Passar till snabba luncher och middagar och höjer inte blodsockret.',
                    'Stek dem i en het panna i bara 3 minuter med vitlök, färsk koriander, citronsaft och en nypa paprikapulver, och undvik '
                    'panerade räkor och majonnäs.')),
}
