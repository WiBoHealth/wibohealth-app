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

# foods with a Swedish page: 1-200 (1-50 samples approved 2026-10-24); set below NAMES

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
    101: ('Ägg, kokt', 'kokt ägg'),
    102: ('Omelett med smör', 'omelett med smör'),
    103: ('Nötlever, grillad', 'grillad nötlever'),
    104: ('Hummus med tahini', 'hummus med tahini'),
    105: ('Falafel, friterad', 'friterad falafel'),
    106: ('Ful medames med olivolja och spiskummin', 'ful medames'),
    107: ('Baba ganoush (aubergineröra)', 'baba ganoush'),
    108: ('Tabbouleh med persilja', 'tabbouleh'),
    109: ('Fattoush med granatäpplesirap och olivolja', 'fattoush'),
    110: ('Molokhia med kyckling', 'molokhia med kyckling'),
    111: ('Kycklingshawarma', 'kycklingshawarma'),
    112: ('Shawarma med nötkött', 'shawarma med nötkött'),
    113: ('Shish taouk, grillad', 'grillad shish taouk'),
    114: ('Kofta, kolgrillad', 'kolgrillad kofta'),
    115: ('Kibbeh, friterad', 'friterad kibbeh'),
    116: ('Kibbeh nayeh (rå kibbeh)', 'rå kibbeh'),
    117: ('Vinbladsdolmar med olivolja (yalanji)', 'vinbladsdolmar'),
    118: ('Zucchini fylld med köttfärs och ris', 'fylld zucchini'),
    119: ('Mansaf med lammkött', 'mansaf'),
    120: ('Maqluba med kyckling och aubergine', 'maqluba'),
    121: ('Mujaddara med bulgur och olivolja', 'mujaddara'),
    122: ('Fatteh med kikärter, yoghurt och nötter', 'fatteh med kikärter'),
    123: ('Sayadieh, fisk med ris och stekt lök', 'sayadieh'),
    124: ('Musakhan med kyckling', 'musakhan'),
    125: ('Shakshuka med ägg och tomat', 'shakshuka'),
    126: ('Linssoppa, gul', 'gul linssoppa'),
    127: ('Koshari, egyptisk', 'egyptisk koshari'),
    128: ('Olivolja, extra jungfru', 'extra jungfruolivolja'),
    129: ('Ghee (skirat smör)', 'ghee'),
    130: ('Kokosolja, jungfru', 'jungfrukokosolja'),
    131: ('Tahini (sesampasta)', 'tahini'),
    132: ('Kaffe, svart (espresso)', 'svart kaffe'),
    133: ('Grönt te', 'grönt te'),
    134: ('Matcha, japansk', 'matcha'),
    135: ('Mandeldryck, osötad', 'osötad mandeldryck'),
    136: ('Ayran (saltad yoghurtdryck)', 'ayran'),
    137: ('Kokosvatten, naturellt', 'naturellt kokosvatten'),
    138: ('Apelsinjuice, färskpressad', 'färskpressad apelsinjuice'),
    139: ('Granatäpplejuice, naturell', 'naturell granatäpplejuice'),
    140: ('Cola, vanlig (med socker)', 'vanlig cola'),
    141: ('Big Mac', 'Big Mac'),
    142: ('Kycklingnuggets (6 st)', 'kycklingnuggets'),
    143: ('Friterad kyckling (KFC)', 'friterad kyckling'),
    144: ('Pizza margherita (bit)', 'pizza margherita'),
    145: ('Pizza med pepperoni (bit)', 'pizza med pepperoni'),
    146: ('Subway-smörgås med teriyakikyckling', 'Subway-smörgås med teriyakikyckling'),
    147: ('Coleslaw (vitkålssallad)', 'coleslaw'),
    148: ('Baklava med pistage', 'baklava'),
    149: ('Knafeh nabulsieh med ost', 'knafeh'),
    150: ('Basbousa med ghee', 'basbousa'),
    151: ('Maamoul med dadlar och fänkålsfrö', 'maamoul med dadlar'),
    152: ('Sesamhalva med nötter', 'sesamhalva'),
    153: ('Mahalabia med mjölk och mastix', 'mahalabia'),
    154: ('Rispudding med kanel', 'rispudding'),
    155: ('Mörk choklad 85 %', 'mörk choklad 85 %'),
    156: ('Smörcroissant', 'smörcroissant'),
    157: ('Cheesecake, New York', 'cheesecake'),
    158: ('Taco med nötfärs', 'taco med nötfärs'),
    159: ('Burrito med kyckling och bönor', 'burrito med kyckling och bönor'),
    160: ('Quesadilla med smält ost', 'quesadilla med ost'),
    161: ('Kycklingfajitas med paprika och lök', 'kycklingfajitas'),
    162: ('Nachos med ost', 'nachos med ost'),
    163: ('Guacamole', 'guacamole'),
    164: ('Tomatsalsa, stark', 'stark tomatsalsa'),
    165: ('Chili con carne', 'chili con carne'),
    166: ('Lasagne med köttfärs och béchamel', 'lasagne'),
    167: ('Spaghetti carbonara', 'spaghetti carbonara'),
    168: ('Spaghetti bolognese', 'spaghetti bolognese'),
    169: ('Fettuccine Alfredo med grädde', 'fettuccine Alfredo'),
    170: ('Svamprisotto med parmesan', 'svamprisotto'),
    171: ('Potatisgnocchi', 'potatisgnocchi'),
    172: ('Calzone (fylld, vikt pizza)', 'calzone'),
    173: ('Bruschetta med tomat och basilika', 'bruschetta'),
    174: ('Caprese (mozzarella och tomat)', 'caprese'),
    175: ('Minestrone', 'minestrone'),
    176: ('Sushi, laxrulle', 'laxsushi'),
    177: ('Sushi, California roll', 'California roll'),
    178: ('Sashimi på rå lax', 'laxsashimi'),
    179: ('Ramen med kyckling', 'kycklingramen'),
    180: ('Pad thai', 'pad thai'),
    181: ('Kyckling teriyaki', 'kyckling teriyaki'),
    182: ('Kyckling katsu, panerad', 'kyckling katsu'),
    183: ('Dumplings, ångkokta (gyoza)', 'ångkokta dumplings'),
    184: ('Vårrullar med grönsaker, friterade', 'friterade vårrullar'),
    185: ('Misosoppa', 'misosoppa'),
    186: ('Tofu, naturell', 'naturell tofu'),
    187: ('Tempeh', 'tempeh'),
    188: ('Kimchi', 'kimchi'),
    189: ('Kyckling tikka masala', 'kyckling tikka masala'),
    190: ('Palak paneer (spenat och indisk ost)', 'palak paneer'),
    191: ('Kycklingbiryani', 'kycklingbiryani'),
    192: ('Naanbröd med vitlök', 'vitlöksnaan'),
    193: ('Dal, indisk linssoppa', 'dal'),
    194: ('Baguette', 'baguette'),
    195: ('Tortillabröd', 'tortillabröd'),
    196: ('Pitabröd', 'pitabröd'),
    197: ('Fatayer med spenat', 'fatayer med spenat'),
    198: ('Fatayer med ost', 'fatayer med ost'),
    199: ('Lahmacun (sfiha med köttfärs)', 'lahmacun'),
    200: ("Manakish med za'atar och olivolja", "manakish med za'atar"),
}
PUBLISH = set(NAMES)
# foods allowed to use the computed Swedish copy where the other languages carry food-specific copy (none since
# foods 1-50 got their translated copy, 2026-10-24)
COMPUTED_COPY = set()

# names that take a plural pronoun in the sentences ({det}/{dem}: "de"/"dem" instead of "det")
PLURAL = {18, 19, 20, 21, 22, 23, 24, 25, 28, 40,
          52, 53, 56, 57, 58, 60, 61, 62, 63, 68, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 99, 100,
          117, 142, 161, 162, 171, 183, 184, 197, 198}

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
    'drink': ('Nästan fri från kalorier och socker när den dricks utan tillsatser.',
              'Undvik socker, sirap och grädde; det är de som tillför kalorier och glykemisk belastning.',
              'Innehåller koffein; drick med måtta, särskilt på kvällen, och rådfråga din läkare om du är gravid eller tar '
              'läkemedel som påverkas av koffein.'),
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
    # foods 1-50: translated from the approved Arabic copy (2026-10-24, overnight batch)
    1: dict(lead='Vitt ris är en självklar del av vardagsmaten i de flesta arabiska hem, men eftersom det smälts snabbt är det en '
                 'utmaning vid diabetes och insulinresistens. Det glykemiska indexet är medelhögt (65) och en hel portion har en hög '
                 'glykemisk belastning. Det betyder inte att du måste avstå: hemligheten ligger i hur du tillagar det och att du '
                 'kombinerar det med fibrer och protein.',
            tips=('Ät en grön sallad eller din proteinkälla tio minuter före riset; fibrerna bildar ett gelliknande nätverk som tydligt '
                  'bromsar upptaget av stärkelsen i riset.',
                  'Hemligheten med resistent stärkelse: kyl det kokta riset i kylskåpet i 12–24 timmar innan du värmer det igen. Då '
                  'ombildas stärkelsemolekylerna och mängden resistent stärkelse ökar, vilket kan ge en jämnare blodsockerkurva.')),
    2: dict(lead='Fullkornsris behåller hela kliskiktet och grodden och innehåller därför mer kostfiber och magnesium. Det uppmätta '
                 'glykemiska indexet (68, medelhögt) ligger nära vitt ris på grund av den långa koktiden, men fibrerna och '
                 'mikronäringsämnena bromsar det faktiska upptaget i kroppen.',
            tips=('Ett utmärkt val när du bygger en balanserad måltid vid insulinresistens; de rikliga fibrerna ger långvarig mättnad.',
                  'Blötlägg fullkornsriset i några timmar före kokning: det blir lättare att smälta, innehållet av fytinsyra minskar och '
                  'koktiden blir kortare, vilket bevarar fibrerna.')),
    3: dict(lead='Det vanligaste och snabbaste brödet att äta, men det tas upp snabbt eftersom det bakas på siktat mjöl utan kli och '
                 'fibrer. Det ger en snabb stegring av blodsocker och insulin och har ett högt glykemiskt index (70).',
            tips=('Undvik att äta det ensamt; fyll eller bred det alltid med en källa till fett eller protein, som kokt ägg, avokado '
                  'eller olivolja, för att bromsa upptaget.',
                  'Att rosta en skiva vitt bröd i brödrosten, eller frysa den och sedan rosta den, förändrar stärkelsemolekylerna något '
                  'och sänker det glykemiska svaret en aning.')),
    4: dict(lead='Det vinnande vardagsalternativet för dig som vill ha jämn energi: fullkornsmjöl med sina naturliga fibrer ger ett '
                 'lågt glykemiskt index (54) och en långvarig mättnad som motverkar plötsliga blodsockerfall.',
            tips=("Passar utmärkt till en mättande frukost; kontrollera ingrediensförteckningen så att mjölet är '100 % fullkornsvete' "
                  'och inte vitt mjöl färgat med karamellfärg.',
                  'Välj helst bröd som jäst långsamt med surdeg; den naturliga jäsningen bryter ned en del av stärkelsen och sänker '
                  'det glykemiska indexet ytterligare.')),
    5: dict(lead='Tvärtemot den vanliga uppfattningen att pasta får blodsockret att rusa har kokt pasta ett lågt glykemiskt index (49). '
                 'Förklaringen är att degen pressas vid tillverkningen, så att stärkelsemolekylerna blir kompakta och svåra för '
                 'matsmältningsenzymerna att bryta ned.',
            tips=('Servera den med en naturlig tomatsås, olivolja och en mager proteinkälla, och undvik färdiga såser med dolt socker '
                  'eller härdad grädde.',
                  'Al dente-regeln: koka pastan tills den är klar men fortfarande har lite tuggmotstånd, och undvik att koka den tills '
                  'den blir mjuk; fast pasta smälts betydligt långsammare.')),
    6: dict(lead='Det gyllene alternativet för pastaälskare: fibrerna från fullkornet kombineras med protein, och det glykemiska '
                 'indexet är lågt (42) tack vare den kompakta strukturen, som bromsar matsmältningen och ger en verklig mättnad utan '
                 'trötthet efter maten.',
            tips=('Kombinera den med en sås på tomat, vitlök och olivolja och bitar av grillat kycklingbröst; undvik färdiga såser med '
                  'mycket socker och härdade oljor.',
                  'Koka den al dente i 8–9 minuter och undvik att koka den för länge, så att fibrerna håller ihop och upptaget inte går '
                  'snabbare.')),
    7: dict(lead='Den klassiska hälsosamma frukosten: havregrynsgröt ger lösliga betaglukanfibrer och har ett lågt glykemiskt index (55). '
                 'Havregrynen suger upp vatten eller mjölk under kokningen och sväller, vilket ger en varm och mättande skål med ett '
                 'måttligt antal kalorier.',
            tips=('Använd vanliga havregryn och koka gröten på vatten eller lättmjölk; undvik portionspåsar med snabbgröt som innehåller '
                  'tillsatt socker och smakämnen.',
                  'Toppa med chiafrön, lite kanel och en näve färska bär för mer fibrer, utan att du behöver tillsätta raffinerat socker.'),
            title='Hur många kalorier har havregrynsgröt? Glykemiskt index och viktnedgång | WiBo Health',
            desc='En skål kokt havregrynsgröt (250 g) innehåller 170 kcal (68 kcal per 100 g) och har ett lågt glykemiskt index (55). '
                 'Läs om skillnaden mellan torra och kokta havregryn och hur gröten påverkar mättnad och blodsocker.',
            faq=[dict(q='Vad är skillnaden i kalorier mellan torra och kokta havregryn?',
                      a='Torra havregryn innehåller ungefär 380 kcal per 100 g. När de kokas på vatten suger de upp mycket vätska, så en '
                        'skål kokt gröt (250 g) ger bara omkring 170 kcal (68 kcal per 100 g kokt gröt). Kokar du gröten på mjölk ökar '
                        'energin beroende på mängd och sort.'),
                 dict(q='Hur bidrar havregrynsgröt till ett jämnt blodsocker?',
                      a='Betaglukanfibrerna bildar en mild gel i matsmältningskanalen som bromsar upptaget av kolhydrater och ger en '
                        'lugnare och jämnare energikurva.'),
                 dict(q='Är kokt havregrynsgröt ett bra val vid viktnedgång?',
                      a='Ja. Gröten sväller och binder vatten, så du får en stor skål för relativt få kalorier, vilket kan göra det '
                        'lättare att klara dig utan mellanmål de närmaste timmarna efter frukosten.')]),
    8: dict(lead='Ett gyllene frö från Anderna som skiljer sig från andra stärkelsekällor genom att vara en fullständig proteinkälla med '
                 'alla nio essentiella aminosyror. Det glykemiska indexet är lågt (52).',
            tips=('Ett bra alternativ till vitt ris för dig som tränar för att bygga muskler och håller koll på ditt HbA1c, utan att '
                  'avstå från stärkelsens mättande energi.',
                  'Skölj quinoan i en finmaskig sil under rinnande vatten före kokning för att få bort de bittra saponinerna, och koka '
                  'den i grönsaksbuljong med en nypa spiskummin.')),
    9: dict(lead='Hjälten i det traditionella levantinska köket och ett av de mest balanserade spannmålen, med ett lågt glykemiskt '
                 'index (47) och mycket kostfiber, järn och zink, vilket gör att det står sig väl jämfört med de flesta sorters ris.',
            tips=('Ett av de smartaste vardagsalternativen vid diabetes; bulgur tas upp mycket långsamt och håller dig mätt i många timmar.',
                  'Koka grov bulgur med olivolja, lök och linser (den klassiska rätten mujaddara) eller med tomater; kombinationen av '
                  'olivolja och bulgur ger en bra näringsmässig balans.')),
    10: dict(lead='Det nordafrikanska kökets juvel, gjord på mannagryn av vete. Den har lätt konsistens, tillagas snabbt och har ett '
                  'medelhögt glykemiskt index (62), vilket gör den till ett gott sätt att variera kosten när den lagas på traditionellt vis.',
             tips=('Undvik att äta den ensam; servera den på traditionellt maghrebiskt vis med mycket grönsaker som zucchini, morot och '
                   'pumpa och med kyckling eller kikärter för att sänka den glykemiska belastningen.',
                   'Ånga couscousen (i en couscousière) över grönsaksbuljong och kryddor i stället för att koka den i vatten, så håller '
                   'kornen ihop och behåller sitt värde.')),
    11: dict(lead='Gyllene korn som kombinerar naturlig sötma med komplexa kolhydrater och ett medelhögt glykemiskt index (56). Majs '
                  'innehåller kostfiber och karotenoider som lutein.',
             tips=('Räkna den som måltidens stärkelse och inte som en vanlig grönsak; en majskolv är en fullständig kolhydratportion i sig.',
                   'Koka majsen i vatten utan socker eller margarin, ät hela kornen med det fiberrika skalet och undvik konserverad majs '
                   'med tillsatt socker.')),
    12: dict(lead='Ett traditionellt bröd och ett av de bästa valen vid diabetes och insulinresistens: det glykemiska indexet är lågt '
                  '(34), och brödet innehåller lösliga betaglukanfibrer som bildar en naturlig barriär i tarmen och hjälper till att '
                  'dämpa blodsockertoppar.',
             tips=('Ett utmärkt val till vardagsfrukosten; det ger jämn energi i många timmar utan plötsliga energidippar.',
                   'Köp det från bagerier som använder äkta fullkornsmjöl av korn, och ät det med ett kokt ägg och olivolja för en '
                   'komplett frukost.')),
    13: dict(lead='Förenar brödets mjukhet med havrens fördelar; det glykemiska indexet är lågt (47), vilket gör det till ett utmärkt '
                  'alternativ till vitt bröd för dig som vill hålla koll på vikten och blodsockret.',
             tips=('En skiva till frukosten räcker ofta, tack vare de täta fibrerna som sväller i magen och ger en långvarig känsla av mättnad.',
                   'Läs etiketten och kontrollera att brödet inte innehåller tillsatt socker eller en stor andel siktat vetemjöl.')),
    14: dict(lead='Basmatiris har långa korn och en aromatisk doft och är det smartaste valet bland de vita rissorterna: det innehåller '
                  'naturligt mer amylos, en stärkelse som smälts långsamt, vilket ger ett mer måttligt glykemiskt index (61, medelhögt) '
                  'och en jämnare matsmältning.',
             tips=('Ett bra vardagsalternativ till kortkornigt ris; tillsammans med tillagade grönsaker eller baljväxter ger det '
                   'långvarig mättnad utan kraftiga blodsockertoppar.',
                   'Blötlägg basmatiriset i 30 minuter och skölj det väl före kokning, och koka det sedan på låg värme; det hjälper till '
                   'att bevara den fasta stärkelsestrukturen och den långsamma matsmältningen.')),
    15: dict(lead='En kulturskatt från Levanten: grönt vete som skördas tidigt och rostas. Det innehåller protein och järn, dubbelt så '
                  'mycket kostfiber som fullkornsris och har ett lågt glykemiskt index (43), vilket passar bra vid diabetes.',
             tips=('Ett utmärkt alternativ till vitt ris i kyckling- och kötträtter; den rökiga smaken och den fasta konsistensen gör den '
                   'till en mättande familjemåltid.',
                   'Koka den i en mager kycklingbuljong med lök, en nypa kanel och svartpeppar, på låg värme tills den har sugit upp '
                   'buljongen och blivit mjuk.')),
    16: dict(lead='Ett gammalt traditionellt spannmål som är naturligt glutenfritt och innehåller magnesium, men det glykemiska indexet '
                  'är högt (71), så det gäller att tänka på portionen och på vad du äter till.',
             tips=('Ett bra val för dig som undviker gluten, till exempel vid celiaki; ät det alltid med mycket bladgrönsaker och '
                   'protein för att bromsa upptaget.',
                   'Koka hirsen som alternativ till ris eller gör en varm gröt med olivolja, och blötlägg den i vatten i två timmar före '
                   'kokningen så blir den lättare att smälta.')),
    17: dict(lead='Havrekornets yttre, mycket koncentrerade lager och en av de rikaste källorna till lösliga fibrer, med ett medelhögt '
                  'glykemiskt index (56). Betaglukaner från havre bidrar till att bibehålla normala kolesterolhalter i blodet; den '
                  'gynnsamma effekten uppnås vid ett dagligt intag av 3 g betaglukaner från havre.',
             tips=('Tillsätt två matskedar i yoghurt, soppa eller bakning; det gör måltiden fylligare och mer mättande utan att tillföra '
                   'många kalorier.',
                   'Drick alltid två glas vatten när du äter havrekli, så att betaglukanfibrerna kan svälla och göra sitt jobb i tarmen.')),
    18: dict(lead='Kronjuvelen bland baljväxterna och ett av de bästa livsmedlen vid diabetes: linser har ett av de lägsta glykemiska '
                  'indexen (25) och innehåller mycket vegetabiliskt protein, järn och lösliga fibrer.',
             tips=('Ett idealiskt vardagslivsmedel; ät linser som varm soppa i början av måltiden eller i sallader för att hålla dig mätt länge.',
                   'Pressa en halv färsk citron över linserna; C-vitamin ökar järnupptaget, och citronen ger dessutom en härlig smak.')),
    19: dict(lead='En baljväxt med lång tradition i vår matkultur som kombinerar långsamt nedbruten stärkelse med vegetabiliskt protein '
                  'och har ett lågt glykemiskt index (37), vilket gör den till en trogen vän vid diabetes.',
             tips=('Ät kikärter hela i sallader eller som ett krispigt, ugnsrostat mellanmål med kryddor; de mättar och stoppar plötslig hunger.',
                   'Blötlägg torkade kikärter i 12–24 timmar och byt vatten innan du kokar dem; det bryter ned en del av de sockerarter '
                   'som orsakar gaser och gör proteinet lättare att ta upp.')),
    20: dict(lead='Hjälten på det traditionella frukostbordet: bondbönor kombinerar vegetabiliskt protein med mycket fibrer, och det '
                  'låga glykemiska indexet (40) bidrar till jämn energi i flera timmar.',
             tips=('En idealisk frukosträtt för dig som vill ha kontroll över aptiten och småätandet; ät bönorna med sked, med olivolja, '
                   'spiskummin och citron, i stället för att doppa ett helt bröd i dem.',
                   'Mosa dem försiktigt med pressad vitlök, citronsaft och en nypa spiskummin, som är skonsammare mot magen, och tillsätt '
                   'en sked extra jungfruolivolja.')),
    21: dict(lead='En av de baljväxter som är snällast mot blodsockret: det glykemiska indexet är lågt (31), och bönorna innehåller '
                  'naturliga ämnen som delvis bromsar de enzymer som bryter ned stärkelse, vilket hjälper till att motverka '
                  'blodsockertoppar.',
             tips=('En varm vinterlunch; ät vita bönor i sås med lite basmatiris, eller som en mustig soppa.',
                   'Blötlägg torkade bönor i 12 timmar och byt vatten för att minska gaserna, och koka dem i en naturlig sås på tomat och '
                   'vitlök med magert kött.')),
    22: dict(lead='Kidneybönor innehåller antioxidanter och lösliga fibrer och har ett lågt glykemiskt index (37), vilket ger en jämn '
                  'blodsockerkurva.',
             tips=('Utmärkta i sallader, soppor och grytor; de trögflytande fibrerna hjälper till att hålla blodsockret i schack efter måltiden.',
                   'En viktig säkerhetsregel: torkade kidneybönor ska blötläggas ordentligt och sedan koka kraftigt i minst 10 minuter för '
                   'att förstöra det giftiga lektinet innan du fortsätter tillagningen.')),
    23: dict(lead='En liten böna med stor näringskraft: den innehåller zink, järn och folat och har ett lågt glykemiskt index (33), som '
                  'är skonsamt mot magen och bidrar till ett stabilt HbA1c.',
             tips=('Utmärkta i ugnsrätter, grytor och kalla sallader; en prisvärd och komplett måltid som mättar väl.',
                   'Koka dem mjuka med en nypa spiskummin, och servera dem varma med olivolja, färsk koriander och citronsaft.')),
    24: dict(lead='Ett av de bästa gröna proteinmellanmålen: färska sojabönsbaljor med nästan ingen stärkelse, ett glykemiskt index på '
                  'högst 18 och fullständigt vegetabiliskt protein.',
             tips=('Ett perfekt mellanmål mellan måltiderna eller framför tv:n; det stillar hungern och ger något att tugga på utan '
                   'tillsatt socker eller ohälsosamt fett.',
                   'Ånga eller koka hela baljorna i bara 5 minuter med en nypa grovt havssalt, och tryck sedan ut bönorna med tänderna.')),
    25: dict(lead='Medelhavets historiska tilltugg: lupinbönor innehåller mycket protein (16,4 g per 100 g) och nästan ingen stärkelse, '
                  'och det glykemiska indexet (15) gör dem till en favorit vid ketokost och diabetes.',
             tips=('Ett smart alternativ till chips och andra snacks; en liten näve mättar förvånansvärt bra och håller hungern borta i '
                   'flera timmar.',
                   'Köp färdigkokta lupinbönor, eller blötlägg och koka dem ordentligt i vatten med salt, spiskummin och citronsaft, och ät '
                   'dem med det tunna skalet för att få med mest fibrer.')),
    26: dict(lead='Ett näringsrikt livsmedel som har fått ett oförtjänt dåligt rykte i bantningskulturen: potatis hör till de mest '
                  'mättande livsmedlen tack vare den höga vattenhalten och innehåller kalium. Den glykemiska effekten (GI 69, medelhögt) '
                  'beror helt på hur du tillagar den.',
             tips=('Ät alltid potatisen med skalet för mer fibrer, och kombinera den med en mager proteinkälla eller en grön sallad för att '
                   'bromsa flödet av glukos till blodet.',
                   'Nedkylningshemligheten: koka potatisen hel med skal och låt den svalna helt innan du äter den, till exempel i en kall '
                   'sallad med olivolja och örter. Nedkylningen bildar resistent stärkelse, som märkbart sänker det glykemiska indexet.')),
    27: dict(lead='Sötpotatis innehåller betakaroten, som kroppen omvandlar till A-vitamin. Trots den naturliga sötman gör det glykemiska '
                  'indexet (67, medelhögt) och de täta fibrerna den till ett bra val för uthållig energi.',
             tips=('Ett utmärkt alternativ till lunchens stärkelse eller som energimåltid före träning; den ger en verklig mättnad som '
                   'hjälper dig att stå emot sötsug.',
                   'Koka den helst eller ugnsbaka den lätt med skalet på, och undvik att rosta den så länge att den karamelliseras kraftigt, '
                   'eftersom det kan påskynda nedbrytningen av sockret.')),
    28: dict(lead='Den populäraste snabbmaten, men pommes frites kombinerar snabbt upptagen stärkelse med oljor som hettats upp till höga '
                  'temperaturer. Det ger ett högt glykemiskt index (75) och mycket energi som påverkar insulinet kraftigt.',
             tips=('Spara dem till enstaka tillfällen och mycket små portioner; ät en stor sallad eller grillat protein först för att bromsa '
                   'upptaget av fett och stärkelse.',
                   'Gör dem hemma: skär potatisen med skalet på och tillaga den i airfryer med en matsked olivolja för att minska '
                   'kalorierna och de oxiderade oljorna.')),
    29: dict(lead='En favorit hos både vuxna och barn, men när potatisen mosas bryts cellstrukturen ned helt, så att '
                  'matsmältningsenzymerna snabbt omvandlar den till socker. Det glykemiska indexet är högt (79), så det gäller att äta '
                  'den med eftertanke.',
             tips=('Vid insulinresistens: ät bara en liten portion, eller byt ut hälften mot blomkålsmos för att lura smaklökarna och '
                   'halvera stärkelsen.',
                   'Mosa potatisen med extra jungfruolivolja, lite vitlöksbuljong och örter i stället för margarin och mjölk; naturligt '
                   'fett hjälper till att bromsa den snabba matsmältningen.')),
    30: dict(lead='Tomaten innehåller antioxidanter, bland annat det välkända färgämnet lykopen. Den består till 95 % av vatten och har '
                  'nästan inga kalorier, vilket gör den till en grönsak du kan äta fritt och som är mycket skonsam mot blodsockret.',
             tips=('Ät tomater fritt i sallader och vardagsmåltider; det låga kolhydratinnehållet och fibrerna gör dem till ett tryggt '
                   'val vid diabetes eller viktnedgång.',
                   'Att lätt tillaga tomater med olivolja kan göra att kroppen tar upp upp till fyra gånger mer lykopen än från råa tomater.')),
    31: dict(lead='Ett av de bästa livsmedlen för att få i sig vätska: vatten och fibrer som fyller magen och svalkar kroppen med nästan '
                  'inga kalorier. Gurkan påverkar knappt insulinet eller blodsockret, hur mycket du än äter.',
             tips=('Det smarta valet för mättnad mellan måltiderna och när du är sugen på något krispigt på kvällen; doppa den i labneh '
                   'eller hummus i stället för chips och kex.',
                   'Ät den alltid med det gröna skalet, där kisel, fibrer och antioxidanter finns i högst halt.')),
    32: dict(lead='Den mest omtyckta mångsidiga grönsaken vid viktnedgång: mjuk och lätt konsistens och nästan inga kalorier gör den till '
                  'ett smart alternativ för dig som vill minska på stärkelsen utan att tallriken känns tom.',
             tips=('Utmärkt i ugnsformar och soppor; en generös mängd ger en behaglig mättnad och bidrar till en jämn blodsockernivå.',
                   'Skär den på längden i tunna band som pastaersättning (zoodles) med naturlig tomatsås, så får du samma njutning som av '
                   'pasta med en fjärdedel av stärkelsen.')),
    33: dict(lead='Auberginen innehåller antioxidanter, bland annat färgämnet nasunin i skalet. Den är mycket skonsam mot blodsockret, med '
                  'ett lågt glykemiskt index (15) och nästan inga kalorier.',
             tips=('Utmärkt som kryddig röra med tahini, vitlök och citron (baba ganoush), eller i skikt i stället för lasagneplattor och '
                   'pasta vid kost med mindre stärkelse.',
                   'Rosta hela auberginen i ugnen eller över gaslåga tills fruktköttet är mjukt, och undvik att fritera den, eftersom den '
                   'suger upp fett som en svamp.')),
    34: dict(lead='Trots den gamla myten att morötter höjer blodsockret visar mätningar att det glykemiska indexet är lågt (39) och att en '
                  'morot på 80 g har en glykemisk belastning på bara 2,2. Moroten innehåller betakaroten, som kroppen omvandlar till '
                  'A-vitamin, och A-vitamin bidrar till att bibehålla normal syn och till immunsystemets normala funktion.',
             tips=('Ett utmärkt krispigt mellanmål när du äter den rå, eller ett färgglatt tillskott som ger mer fibrer i grytor och '
                   'grönsakssoppor.',
                   'Ät den rå med hummus eller labneh; om du kokar den, låt den inte koka sönder, så behåller fibrerna sin struktur och det '
                   'glykemiska indexet förblir lågt.')),
    35: dict(lead='Jätten i den korsblommiga familjen och en källa till ämnet sulforafan. De täta fibrerna bromsar sockerupptaget och är '
                  'föda för tarmens bakterier.',
             tips=('Ät en liten tallrik i början av lunchen; fibrerna bildar en naturlig barriär i tarmen som hjälper till att förhindra '
                   'plötsliga blodsockertoppar efter måltiden.',
                   'Ånga den i bara 4–5 minuter så att den behåller sin klargröna färg och lätta krispighet, och undvik lång kokning i '
                   'vatten så att C-vitaminet och andra ämnen inte går förlorade.')),
    36: dict(lead='Ett av världens smartaste alternativ till ris och potatis: fyllig konsistens och nästan ingen stärkelse gör blomkålen '
                  'till ett trumfkort vid diabetes och lågkolhydratkost, så att du kan njuta av dina favoriträtter utan oro.',
             tips=('Ett fantastiskt vardagsalternativ: byt ut hälften av riset i måltiden mot blomkålsris för att lura ögat och magen och '
                   'direkt halvera stärkelsen.',
                   'Riv blomkålen eller mixa den i matberedare till riskornsstorlek och fräs den några minuter i panna med olivolja och lök, '
                   'eller koka och mosa den som ett utmärkt alternativ till potatismos.')),
    37: dict(lead='Världens mest kända bladgrönsak, som innehåller folat, järn och antioxidanter. Den har nästan inga kalorier och ingen '
                  'glykemisk effekt, vilket gör den idealisk för att fylla tallriken utan att påverka insulinet.',
             tips=('Ät den färsk som salladsbas med citron och olivolja, eller tillagad till huvudrätten, så att tarmbakterierna får rena fibrer.',
                   'Tillsätt alltid citronsaft till spenaten; C-vitamin ökar järnupptaget. Undvik att koka den länge i vatten, så bevaras '
                   'vitaminerna.')),
    38: dict(lead='Drottningen på det gröna bordet och en av de mest älskade traditionella rätterna: jutemalva innehåller magnesium, järn '
                  'och naturliga fibrer. Den är nästan fri från tillgängliga kolhydrater och ett fritt och tryggt val vid diabetes.',
             tips=('En underbar vardagsrätt vid diabetes eller bantning; den ger snabbt en behaglig mättnad och hjälper till att dämpa '
                   'blodsockerstegringen när den äts med en måttlig mängd ris.',
                   'Koka den i en mager kyckling- eller köttbuljong och gör den avslutande frästen av vitlök och koriander i olivolja i '
                   'stället för industriellt framställt ghee, med en skvätt färsk citron; C-vitamin ökar järnupptaget.')),
    39: dict(lead='En god vän för matsmältningen och blodsockret, känd för sin unika konsistens och sitt höga innehåll av trögflytande '
                  'fibrer. Okra innehåller mycket lite energi, och kolhydratinnehållet är så lågt att glykemiskt index inte är tillämpligt.',
             tips=('Det naturliga, trögflytande pektinet lägger sig försiktigt mot tarmväggen och hjälper till att bromsa upptaget av '
                   'stärkelse och socker när du äter okra till ris eller kött.',
                   'Koka den i naturlig tomatsås med olivolja, vitlök och koriander, och skär inte bort topparna för djupt före '
                   'tillagningen, så behåller den sin lätta konsistens.')),
    40: dict(lead='Ett genialt livsmedel som förenar köttig smak med grönsakens konsistens och nästan inga kalorier. Champinjoner '
                  'innehåller selen och B-vitaminer och saknar snabba kolhydrater, vilket gör dem till ett bra val vid insulinresistens.',
             tips=('Ett smart knep för att dryga ut måltiden: byt ut hälften av köttfärsen eller stärkelsen i ugnsrätter och soppor mot '
                   'hackade champinjoner, utan att förlora den mättande smaken.',
                   'Bryn dem i het panna med en skvätt olivolja, en pressad vitlöksklyfta och en nypa timjan. Blötlägg dem inte i vatten, '
                   'då suger de upp det och blir sladdriga; torka av dem med en fuktig duk innan du skivar dem.')),
    41: dict(lead='Kronärtskockan innehåller den präbiotiska fibern inulin, som är föda för tarmens bakterier, och har ett lågt '
                  'glykemiskt index (15).',
             tips=('Ett bra val om du vill äta mer fibrer; 100 g innehåller 5,4 g kostfiber.',
                   'Koka kronärtskockshjärtan i vatten med citron, olivolja och vitlök, och njut av dem som en fin och hälsosam förrätt.')),
    42: dict(lead='En elegant grönsak som innehåller antioxidanter som glutation samt K-vitamin. De tillgängliga kolhydraterna är nästan '
                  'noll (under 2 g), och sparrisen påverkar praktiskt taget inte blodsockret.',
             tips=('Ett fint tillbehör till grillad biff eller lax.',
                   'Fräs den i het panna i bara 3–4 minuter med en sked olivolja, lite vitlök och havssalt, så att den förblir krispig och mör.')),
    43: dict(lead='Idrottarnas favorit: rödbetor innehåller naturligt nitrat. Det glykemiska indexet är medelhögt (64), men en liten '
                  'portion på 80 g har en låg glykemisk belastning (3,5).',
             tips=('Lägg en halv kokt rödbeta i en grön sallad för färg, smak och fibrer.',
                   'Koka den med skalet, skala den när den är klar och skär den i tärningar med olivolja, äppelcidervinäger och persilja '
                   'för att bromsa matsmältningen av det naturliga sockret.')),
    44: dict(lead='Den omtyckta pepparaktiga bladgrönsaken innehåller naturligt nitrat och antioxidanter. Ingen glykemisk effekt och '
                  'nästan inga kalorier: den fyller tallriken med näring utan att påverka insulinet.',
             tips=('Gör den till en självklar följeslagare till lunch och middag; att äta den före måltiden kan hjälpa till att dämpa '
                   'måltidens blodsockertoppar.',
                   'Ät den färsk och väl sköljd med en skvätt citron, sumak och några droppar olivolja, som en fräsch sallad.')),
    45: dict(lead='Löken innehåller kvercetin och organiska svavelföreningar och har ett lågt glykemiskt index (15).',
             tips=('Grunden i matlagningen och en självklar salladsingrediens; fibrerna är föda för tarmbakterierna och bidrar till ett '
                   'stabilt blodsocker på sikt.',
                   'Ät den rå i sallader för att få med mest kvercetin, eller fräs den lätt i olivolja och undvik att steka den tills den bränns.')),
    46: dict(lead='En av naturens mest smakrika kryddor, med den bioaktiva föreningen allicin. Den lilla dagliga mängden (en eller två '
                  'klyftor) gör att den glykemiska effekten i praktiken är noll.',
             tips=('En självklar del av vardagens hälsosamma rätter, som ger mycket smak.',
                   'Pressa en vitlöksklyfta och låt den vila i luften i 5–10 minuter innan du tillagar eller äter den; under pausen bildas allicin.')),
    47: dict(lead='En utmärkt källa till C-vitamin, med ännu mer än apelsin! Grön paprika har nästan inga kalorier och högst 2,9 g '
                  'tillgängliga kolhydrater per 100 g, vilket gör den till en grönsak du kan äta fritt utan påverkan på blodsockret.',
             tips=('Ett fräscht och krispigt mellanmål som stillar suget efter salt; skär den i stavar och ät med labneh eller hummus, '
                   'eller lägg den i alla sommarsallader.',
                   'Ät den färsk och rå för att bevara det värmekänsliga C-vitaminet, eller rosta den kort i ugnsrätter och med kött utan '
                   'att tillaga den för länge.')),
    48: dict(lead='Den mest kända vardagsfrukten, som innehåller lösliga pektinfibrer och har ett lågt glykemiskt index (38), vilket gör '
                  'den till ett utmärkt fruktval vid diabetes och bantning.',
             tips=('Ät alltid hela äpplet med skalet och undvik äppeljuice; juicen höjer blodsockret snabbt eftersom pektinfibrerna saknas.',
                   'Ät äppelskivor med en nypa malen kanel eller lite naturligt jordnötssmör för ett mer mättande och balanserat mellanmål.')),
    49: dict(lead='Naturens bärbara energimellanmål: bananen innehåller kalium och B6-vitamin och har ett lågt glykemiskt index (52). '
                  'Kolhydraterna förändras när bananen mognar, från resistent stärkelse till naturligt socker, vilket gör den till ett bra '
                  'val för idrottare och för vardagens aktiviteter.',
             tips=('Vid diabetes eller insulinresistens: välj helst fasta bananer med lätt gröna toppar, som innehåller mer resistent '
                   'stärkelse som smälts långsamt.',
                   'För längre mättnad: kombinera en halv banan med en källa till fett eller protein, som naturligt jordnötssmör eller '
                   'grekisk yoghurt.'),
             title='Hur många kalorier har en banan? Kalorier efter storlek och glykemiskt index | WiBo Health',
             desc='Hur många kalorier har en banan? En medelstor banan innehåller cirka 105 kcal (89 kcal per 100 g) och har ett lågt '
                  'glykemiskt index (52). Se kalorierna efter storlek och hur bananen påverkar kosten och blodsockret.',
             faq=[dict(q='Hur många kalorier har en banan beroende på storlek?',
                       a='En liten banan (cirka 100 g) ger 89 kcal, en medelstor (118–120 g) ungefär 105–107 kcal och en stor (cirka '
                         '140 g) omkring 125 kcal.'),
                  dict(q='Passar banan vid bantning och viktnedgång?',
                       a='Ja. Bananen innehåller fibrer som pektin och resistent stärkelse, och om du räknar in en banan i ditt dagliga '
                         'energiintag passar den bra i planen.'),
                  dict(q='Vilket är bäst för blodsockret: grön eller mogen gul banan?',
                       a='Omogna, gröna bananer har ett lägre glykemiskt index och mer resistent stärkelse, medan stärkelsen i mogna, '
                         'brunprickiga bananer har omvandlats till enkla sockerarter som tas upp snabbare.')]),
    50: dict(lead='En naturlig C-vitaminbomb som innehåller citrusflavonoider och fibrer som bromsar sockerupptaget, med ett lågt '
                  'glykemiskt index (42).',
             tips=('Ät hela apelsinen med klyftorna och den tunna vita hinnan, och undvik att pressa den; ett glas juice innehåller sockret '
                   'från tre apelsiner utan fibrerna.',
                   'Skär den i bitar och ät den färsk, eller lägg de fräscha klyftorna i en grön sallad med valnötter och ruccola.')),
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
    # foods 101-200: translated from the approved Arabic copy (2026-10-24, four checked blocks of 25)
    101: dict(lead='Guldstandarden för fullvärdigt protein och ett av de livsmedel som påverkar blodsockret minst. Ägget '
                   'innehåller nästan ingen stärkelse (inget glykemiskt index), mättar väl och innehåller fettlösliga '
                   'vitaminer.',
              tips=('Ett utmärkt sätt att börja dagen till frukost; det ger en jämn blodsockerkurva under förmiddagen och '
                    'kan minska suget efter stärkelserik mat.',
                    'Koka ägget så att gulan fortfarande är lite krämig (mellankokt), för att bevara de kolinrika fetterna '
                    'och de ämnen som är känsliga för hög värme.')),
    102: dict(lead='Den klassiska, mättande frukosten: äggets fullvärdiga protein tillsammans med smörets naturliga fett, '
                   'utan stärkelse och utan glykemisk effekt, för ett stabilt blodsocker på morgonen.',
              tips=('Börja dagen med den tillsammans med en kopp te eller svart kaffe utan socker; den mättar väl ända '
                    'fram till lunch.',
                    'Vispa två ägg med lite salt och svartpeppar och stek dem på låg värme i en tesked smör; tillsätt '
                    'spenatblad eller svamp för mer fibrer och näring.')),
    103: dict(lead='Ett av naturens rikaste förråd av vitaminer och mineraler: levern är rik på A-vitamin, järn och '
                   'B-vitaminer. Den innehåller ingen nämnvärd stärkelse (ingen glykemisk effekt).',
              tips=('Ett bra val för järnintaget; ät den en gång i veckan och pressa citron över, eftersom C-vitamin ökar '
                    'järnupptaget.',
                    'Grilla eller fräs den snabbt på hög värme med vitlök, spiskummin och olivolja i bara några minuter; '
                    'för lång tillagning gör den seg och minskar de värmekänsliga vitaminerna.',
                    '⚠️ Gravida rekommenderas att inte äta mycket lever, eftersom den innehåller mycket stora mängder '
                    'A-vitamin.')),
    104: dict(lead='Kungen bland de levantinska mezerätterna och en ikon i medelhavsköket: kokta kikärter, sesamtahini och '
                   'olivolja ger en fin balans mellan fibrer och omättat fett, med ett lågt glykemiskt index (25) som '
                   'bromsar sockerupptaget.',
              tips=('En utmärkt frukost eller förrätt till vardags vid diabetes; ät den med sked eller som dipp till '
                    'gurk-, morots- och paprikastavar i stället för ett helt tunnbröd.',
                    'Gör den hemma: koka kikärterna väl och mixa dem med ren sesamtahini, citronsaft, vitlök och extra '
                    'jungfruolivolja, och undvik färdig hummus med tillsatta raffinerade vegetabiliska oljor.')),
    105: dict(lead='En krispig favorit i Levanten och Egypten, gjord främst av kikärter, bondbönor och örter. Det ger ett '
                   'lågt glykemiskt index (35) och en hel del fibrer; den enda utmaningen är att falafeln suger upp mycket '
                   'frityrolja.',
              tips=('Ät två till tre falaflar till frukost i ett litet fullkornsbröd med en stor sallad, och undvik att '
                    'äta sex eller sju på en gång för att hålla energiintaget i schack.',
                    'Tillaga dem i airfryer eller ugn med lite olivolja penslad på; du får samma goda krispighet med '
                    'ungefär hälften så mycket uppsuget fett.')),
    106: dict(lead='Frukostens ryggrad och hemligheten bakom en jämn och mättande förmiddag: bondbönor med mycket protein '
                   'och fibrer smälts långsamt och har ett lågt glykemiskt index (38), vilket ger en jämn blodsockerkurva '
                   'i flera timmar.',
              tips=('Ett självklart förstahandsval vid insulinresistens eller om du snabbt blir hungrig på morgonen; '
                    'spiskummin, citron och olivolja gör den till en fiberrik och smakrik rätt.',
                    'Mosa bönorna halvvägs med skalet kvar, där mycket av fibrerna finns, i stället för att sila bort '
                    'skalen; tillsätt vitlök, spiskummin, citron och rikligt med extra jungfruolivolja.')),
    107: dict(lead='Grillens aromatiska, rökiga smak: grillad aubergine mosad med tahini och olivolja blir en röra med '
                   'mycket lite stärkelse (GI 15) som knappt påverkar blodsockret.',
              tips=('En smakrik dipp vid bantning och diabetes; den krämiga, fylliga smaken kan ersätta majonnäs och '
                    'industriellt framställda såser.',
                    'Grilla auberginen med skalet på över kol eller gaslåga tills insidan är rökig, blanda den sedan med '
                    'ren tahini, krossad vitlök och citronsaft, och toppa med granatäpplekärnor och persilja.')),
    108: dict(lead='Den levantinska salladens drottning och en grön fiberkälla: 80 % persilja och mynta med en lätt touch '
                   'av grov bulgur, olivolja och citron. Det ger ett lågt glykemiskt index (28) och en rejäl mängd '
                   'C-vitamin.',
              tips=('Börja alltid lunchen med den; fibrerna i persiljan och olivoljan kan bromsa upptaget av stärkelsen i '
                    'huvudrätten, och salladen ger en fräsch mättnad.',
                    'Håll dig till grundregeln: mycket persilja, mynta, tomat, olivolja och citron, och bara en liten sked '
                    'blötlagd bulgur.')),
    109: dict(lead='Den färgglada salladen på det orientaliska bordet, med färska grönsaker, krispigt bröd och sumak. Det '
                   'glykemiska indexet är lågt (38), och salladen ger mycket vätska och fibrer, vilket ger en jämnare '
                   'blodsockerkurva.',
              tips=('En självklar rätt för att inleda måltiden eller lunchen; bladgrönsakerna, rädisorna och gurkan ger '
                    'rejält med volym, och fibrerna bromsar glukosupptaget.',
                    'Rosta bitar av fullkornsbröd i ugn eller airfryer med olivolja i stället för att fritera dem, och '
                    'använd 100 % naturell granatäpplesirap utan tillsatt socker.')),
    110: dict(lead='En klassisk och värmande rätt från Levanten: molokhiablad som kokas med magert kycklingkött, koriander '
                   'och vitlök. Den är nästan fri från kolhydrater (ingen glykemisk effekt) och mättar väl.',
              tips=('En komplett måltid vid diabetes och bantning; ät den med sked tillsammans med kycklingbitarna och '
                    'lite pressad citron, och nöj dig med tre eller fyra skedar vitt ris vid sidan om.',
                    'Låt den sjuda på låg värme i naturlig kycklingbuljong, smaksätt med olivolja, hackad vitlök och '
                    'torkad koriander, och tillsätt citron, eftersom C-vitamin ökar järnupptaget.')),
    111: dict(lead='Den populäraste gatumaten i arabvärlden: kryddade kycklingskivor grillade på spett, med mycket magert '
                   'protein. Det glykemiska indexet beror helt på vilket bröd den rullas in i och hur mycket (lågt, 45).',
              tips=('Det smartaste valet vid diabetes eller bantning är en shawarmatallrik: ät den kryddade kycklingen med '
                    'gaffel tillsammans med naturlig vitlökssås, inlagda grönsaker och sallad, utan det stora brödet.',
                    'Vill du äta den som wrap, välj ett litet fullkornsbröd och använd en vitlökssås gjord på grekisk '
                    'yoghurt och olivolja i stället för färdig majonnäs.')),
    112: dict(lead='Kryddade skivor av nötkött med persilja, lök, sumak och tahinisås: mycket protein och naturligt fett '
                   'med ett lågt glykemiskt index (40), och rätten mättar länge.',
              tips=('Beställ den som en tallrik grillat kött med piyazsallad (persilja, lök och sumak) och tahinisås; en '
                    'proteinrik måltid som mättar i många timmar utan någon kraftig blodsockertopp.',
                    'Tahinisås med citron är den perfekta följeslagaren till köttets fett; sesamfettet bromsar upptaget '
                    'och ger en äkta orientalisk smak.')),
    113: dict(lead='Tärningar av kycklingbröst marinerade i yoghurt, vitlök, citron och kryddor och grillade över kol: '
                   'magert protein helt utan stärkelse (det glykemiska indexet är inte tillämpligt) och mycket lättsmält.',
              tips=('Det säkraste valet på restaurang vid diabetes eller bantning; ät den med en grön sallad och baba '
                    'ganoush för en mättande och balanserad restaurangmåltid.',
                    'Grilla den över kol eller på grillen hemma tills den är genomstekt men fortfarande saftig, och '
                    'servera med grillade vitlöksklyftor och grillad lök.')),
    114: dict(lead='En blandning av köttfärs, lök, persilja och orientaliska kryddor: rikligt med protein, järn och zink '
                   'utan tillsatt stärkelse (ingen glykemisk effekt), och den mättar länge.',
              tips=('Passar utmärkt vid lågkolhydratkost och keto; protein bidrar till att öka och bibehålla muskelmassan. '
                    'Ät de grillade koftaspetten med grön sallad och yoghurt i stället för pommes frites eller vitt bröd.',
                    'Grilla dem så att överflödigt smält fett får droppa av, och se till att inget ströbröd eller mjöl '
                    'blandas i färsen.')),
    115: dict(lead='En ikon i det aleppiska och levantinska köket: ett krispigt skal av bulgur och magert kött, fyllt med '
                   'köttfärs, lök och valnötter. Det glykemiska indexet är lågt (52) tack vare den långsamt smälta '
                   'bulguren och proteinet.',
              tips=('En eller två bitar räcker gott som portion i en balanserad måltid; ät en grön sallad eller yoghurt '
                    'med gurka till för att balansera energin och fettet från friteringen.',
                    'Grädda dem i ugn eller airfryer med lite olivolja penslad på för samma krispighet utan stora mängder '
                    'olja.')),
    116: dict(lead='En förfinad traditionell rätt från Levanten: mycket färskt nöt- eller lammkött som stöts med fin '
                   'bulgur, mynta och kryddor. Den har ett lågt glykemiskt index (38) och protein av hög kvalitet.',
              tips=('En festlig rätt som passar vid diabetes och bantning; den mättar väl utan att höja blodsockret '
                    'nämnvärt, eftersom det magra köttet ger mycket protein i förhållande till den måttliga mängden '
                    'bulgur.',
                    'Servera den med extra jungfruolivolja, färsk mynta, ruccola och salladslök, och köp alltid köttet '
                    'färskt och rent från en pålitlig källa.',
                    '⚠️ Köttet måste vara helt färskt och komma från en pålitlig källa; rätten rekommenderas inte för '
                    'gravida, barn eller personer med nedsatt immunförsvar, på grund av risken för bakteriell infektion.')),
    117: dict(lead='Allas favorit på det kalla mezebordet: vinblad fyllda med ris, hackade grönsaker, olivolja och '
                   'granatäpplesirap. Fibrerna i vinbladen, olivoljan och citronen bromsar stärkelsen i riset, så att det '
                   'glykemiska indexet blir lågt (42).',
              tips=('En utmärkt kall förrätt; ät dem med måtta (4–5 dolmar), eftersom den fylliga, syrliga smaken gör att '
                    'några få räcker för att du ska känna dig behagligt mätt.',
                    'Låt dem sjuda på mycket låg värme med skivad potatis och tomat, citronsaft och olivolja, och prova '
                    'fullkornsris eller bulgur i fyllningen för mer fibrer.')),
    118: dict(lead='Den mest balanserade varma husmansrätten: ett tunt, vattenrikt zucchiniskal runt en fyllning av '
                   'köttfärs och lite ris, vilket ger ett lågt glykemiskt index (45).',
              tips=('En komplett måltid som passar vid diabetes och viktnedgång; två fyllda zucchinier i en buljong med '
                    'tomat, vitlök och mynta mättar väl utan att kännas tunga.',
                    'Gör fyllningen av 70 % mager köttfärs och bara 30 % ris, och koka den i en naturlig sås av tomat, '
                    'vitlök och torkad mynta utan sötad tomatpuré på burk.')),
    119: dict(lead='De jordanska festmåltidernas kung och en symbol för arabisk gästfrihet: ris kokat med mört lammkött, '
                   'syrlig jameedsås (fermenterad torkad yoghurt) och rostad mandel. Köttets fett och proteinet i jameeden '
                   'bromsar upptaget av stärkelsen i riset, så att det glykemiska indexet blir lågt (52).',
              tips=('Utmaningen med mansaf är den höga energitätheten; ta en måttlig portion ris (en kopp), fokusera på '
                    'köttet och den varma jameedsåsen, och ät ruccola och salladslök till.',
                    'Koka riset med lite naturligt ghee i stället för härdat fett, och drick jameedsåsen långsamt; den '
                    'fermenterade, syrliga smaken gör att måltiden känns lättare.')),
    120: dict(lead='Ett berömt paradnummer i det palestinska och levantinska köket: lager av karamelliserad aubergine, '
                   'kyckling och kryddat ris. De lösliga fibrerna i auberginen och proteinet i kycklingen bromsar upptaget '
                   'av stärkelsen i riset, så att det glykemiska indexet blir lågt (55).',
              tips=('En härlig och komplett familjerätt; ta en portion där hälften är aubergine och kyckling och en '
                    'fjärdedel ris, och ät en gurksallad med yoghurt till.',
                    'Ugnsrosta auberginskivorna med lite olivolja i stället för att fritera dem; du sparar hundratals '
                    'kalorier och slipper att de suger upp bränd olja.')),
    121: dict(lead='"De fattigas guld" och en av de mest balanserade måltiderna som finns: grov bulgur, bruna linser, '
                   'olivolja och lök kompletterar varandra till ett fullvärdigt protein med mycket fibrer och ett lågt '
                   'glykemiskt index (38).',
              tips=('En av de växtbaserade kombinationer som rekommenderas mest vid diabetes; den mättar länge och ger '
                    'jämna blodsockervärden hela dagen.',
                    'Laga den med grov bulgur i stället för vitt ris, använd extra jungfruolivolja och servera den med en '
                    'grön sallad eller en skål naturell yoghurt.')),
    122: dict(lead='Den lyxiga frukosten från Damaskus: kokta kikärter toppade med en sås av yoghurt, tahini och vitlök '
                   'samt rostat bröd. Proteinet i kikärterna och yoghurten bromsar upptaget av brödet, så att det '
                   'glykemiska indexet blir lågt (45).',
              tips=('En rik och mycket mättande frukost; rosta brödet i ugnen i stället för att steka det i ghee, fokusera '
                    'på kikärterna och yoghurten och ta bara lite bröd.',
                    'Gör såsen av naturell yoghurt, ren tahini, citronsaft och vitlök, och toppa med pinjenötter eller '
                    'lätt rostad mandel.')),
    123: dict(lead='Kustkökets pärla: brunt, smakrikt ris kokat i fiskbuljong med karamelliserad lök och kryddor, serverat '
                   'med bitar av färsk fisk. Fiskens magra protein ger riset ett lågt glykemiskt index (52).',
              tips=('En balanserad fiskmåltid som kombinerar stärkelse för energi med lätt protein från fisken; ta en '
                    'rejäl bit fisk och en måttlig mängd ris.',
                    'Karamellisera löken i olivolja på låg värme tills den får en naturlig brun färg utan att brännas, och '
                    'servera med en lätt tartarsås gjord på yoghurt, vitlök och citron.')),
    124: dict(lead='Det traditionella palestinska kökets stolthet: tabunbröd dränkt i extra jungfruolivolja med lök '
                   'karamelliserad med sumak och ugnsstekt kyckling. Den rikliga olivoljan och proteinet bromsar upptaget '
                   'av brödet, så att det glykemiska indexet blir lågt (55).',
              tips=('En rätt för högtider och sammankomster; ta en fjärdedels bröd med lök och sumak, en fjärdedels '
                    'kyckling och en skål yoghurt för att balansera fettrikedomen.',
                    'Använd äkta, oraffinerad palestinsk extra jungfruolivolja och ren, syrlig sumak, och ugnsstek '
                    'kycklingen tills den får fin färg och köttsaften rinner över löken.')),
    125: dict(lead='En mättande och älskad frukosträtt i hela arabvärlden: ägg som får sjuda långsamt i en sås av tomat, '
                   'lök, paprika och olivolja. Mycket lite kolhydrater (GI 20), mycket protein, och rätten mättar i flera '
                   'timmar.',
              tips=('En idealisk frukost vid diabetes och för dig som äter keto eller lågkolhydratkost; den ger en '
                    'ordentlig mättnad på morgonen och påverkar blodsocker och insulin mycket lite.',
                    'Ät den med sked tillsammans med en skiva rostat fullkornsbröd eller gurkskivor, och laga såsen på '
                    'olivolja och färska tomater med en nypa spiskummin, paprikapulver och lite chili.')),
    126: dict(lead='Vintervärme i en skål: mosad soppa på gula linser med lök, spiskummin, olivolja och citron. Den har '
                   'ett lågt glykemiskt index (30) och innehåller mycket lösliga fibrer.',
              tips=('En perfekt förrätt till lunch eller middag som fyller magen och dämpar storätandet; börja måltiden '
                    'med den, så äter du ofta mindre stärkelse efteråt.',
                    'Koka den på gula linser, vatten, lök, spiskummin och olivolja, och undvik för mycket potatis och '
                    'färdiga buljongtärningar med mycket salt och smakförstärkare.')),
    127: dict(lead='Kungen bland Egyptens folkrätter: en mäktig, stärkelserik blandning av ris, linser, pasta och kikärter '
                   'med tomatsås, vitlöksvinäger (daqqa) och krispig lök. Linserna och kikärterna bromsar stärkelsen, så '
                   'att det glykemiska indexet blir medelhögt (58).',
              tips=('En måltid med mycket stärkelse; vid diabetes kan du be om en portion med extra linser, kikärter och '
                    'tomatsås och hälften så mycket ris och pasta.',
                    'Ta gärna rikligt med daqqa (vinäger med vitlök) och stark tomatsås, som ger mycket smak.')),
    128: dict(lead='Medelhavskostens självklara fett: olivoljan består främst av enkelomättat fett och påverkar inte '
                   'blodsockret. Att ersätta mättat fett med omättat fett i kosten bidrar till att bibehålla normala '
                   'kolesterolhalter i blodet.',
              tips=('Ringla en till två matskedar om dagen över sallad, ful medames eller hummus; olivolja tillsammans med '
                    'stärkelse bromsar upptaget.',
                    'Använd den kall eller vid skonsam tillagning på låg värme, och undvik att hetta upp den till '
                    'rökpunkten, så bevaras de känsliga polyfenolerna.')),
    129: dict(lead='Ett traditionellt och rent fett från ko- eller fårmjölk, där vattnet, laktosen och mjölkproteinet har '
                   'tagits bort. Inga kolhydrater och ingen glykemisk effekt, och ghee tål höga stektemperaturer väl.',
              tips=('Ett bra fett för stekning och bryning med måtta i stället för härdade fetter; en tesked till ägg '
                    'eller grönsaker påverkar inte blodsockret.',
                    'Välj naturligt ghee gjort på riktigt smör utan tillsatta aromer, och använd det sparsamt eftersom det '
                    'är mycket energitätt.')),
    130: dict(lead='Ett tropiskt fett som innehåller medellånga fettsyror (MCT) och är helt fritt från kolhydrater.',
              tips=('Populärt bland dem som äter keto eller lågkolhydratkost och bland idrottare, till exempel en tesked i '
                    'morgonkaffet.',
                    'Välj kallpressad jungfrukokosolja med en lätt arom; den passar för skonsam matlagning och bakning, '
                    'men eftersom den är rik på mättat fett bör den användas med måtta.')),
    131: dict(lead='Ren sesam i krämig form: vegetabiliskt fett, kalcium och magnesium i koncentrerad form, med ett lågt '
                   'glykemiskt index (12). Tillsammans med söt mat kan tahinins fett bromsa sockerupptaget.',
              tips=('Ett bra sällskap vid diabetes när du äter dadlar eller frukt; en halv tesked tahini på en dadel '
                    'bromsar sockerflödet till blodet och dämpar en plötslig insulinstegring.',
                    'Välj tahini gjord på 100 % sesamfrön utan tillsatt vitt mjöl eller billiga vegetabiliska oljor (ett '
                    'naturligt lager sesamolja lägger sig ofta överst).')),
    132: dict(lead='Världens populäraste morgondryck. Svart kaffe innehåller klorogensyra, är fritt från kolhydrater, '
                   'nästan fritt från kalorier och påverkar inte blodsockret.',
              tips=('Drick det utan socker och utan sötade kaffegräddar, som tillför socker och kalorier.',
                    'Brygg det som bryggkaffe, espresso eller lätt arabiskt eller turkiskt kaffe, och drick ett glas '
                    'vatten till varje kopp för att få i dig tillräckligt med vätska.')),
    133: dict(lead='Grönt te innehåller katekiner, bland annat EGCG. Drycken är i princip fri från kalorier och stärkelse.',
              tips=('Gott mellan måltiderna eller en halvtimme efter lunch, och det påverkar varken blodsocker eller '
                    'insulin.',
                    'Låt de gröna tebladen dra i hett men inte kokande vatten (cirka 80 °C) i två till tre minuter, och '
                    'undvik att koka teet, eftersom garvämnena (tanninerna) då ger en bitter och sträv smak.')),
    134: dict(lead='Pulver av hela gröna teblad med katekiner (EGCG) och aminosyran L-teanin, utan socker och utan '
                   'glykemisk effekt.',
              tips=('Drick den varm på morgonen eller före träning.',
                    'Vispa matchapulvret med en bambuvisp i hett men inte kokande vatten och drick den utan socker, eller '
                    'blanda den med osötad mandeldryck som ett alternativ till kaféernas sötade latte.')),
    135: dict(lead='Ett av de mest energisnåla växtbaserade alternativen: vatten med pressad mandel där socker och '
                   'stärkelse nästan saknas, med 15 kcal per 100 g och ingen effekt på blodsockret.',
              tips=('Ett smart val vid diabetes och insulinresistens till kaffe och smoothies; den ger en krämig '
                    'konsistens utan laktos och utan snabbt socker.',
                    "Läs ingrediensförteckningen noga och kontrollera att det står 'osötad'; vanliga varianter i butiken "
                    'innehåller tillsatt socker och aromer som höjer det glykemiska indexet.')),
    136: dict(lead='En svalkande sommardryck: yoghurt utspädd med vatten och en nypa havssalt. Den är syrad, innehåller '
                   'protein och har ett lågt glykemiskt index (25).',
              tips=('Ett perfekt sällskap till mastiga måltider som grillat kött och kabsa; den släcker törsten och '
                    'innehåller inget tillsatt socker.',
                    'Gör den hemma genom att vispa naturell yoghurt med kallt vatten, en nypa salt och torkad mynta; en '
                    'naturlig törstsläckare som ersätter saltet du förlorar genom svett på sommaren.')),
    137: dict(lead='Idrottarnas naturliga elektrolytdryck: vatten från den gröna kokosnöten, som innehåller kalium och '
                   'magnesium och har ett lågt glykemiskt index (54) och få kalorier.',
              tips=('Ett bra alternativ till industriella sportdrycker efter hård träning eller på varma dagar; den ger '
                    'vätska och kalium.',
                    'Drick färskt kokosvatten direkt från frukten och undvik förpackade varianter med tillsatt rörsocker '
                    'eller konstgjorda aromer.')),
    138: dict(lead='Den vanligaste drycken på frukostbordet. Apelsinjuice innehåller mycket C-vitamin, men när apelsinen '
                   'pressas skiljs fibrerna bort och fruktsockret koncentreras i en vätska som tas upp snabbt (GI 50).',
              tips=('Ett glas juice kräver 3–4 pressade apelsiner; därför är det bättre vid diabetes och bantning att äta '
                    'en hel apelsin med klyftor och fibrer än att dricka silad juice.',
                    'Om du vill dricka den, nöj dig med ett halvt litet glas (100 ml) efter en proteinrik frukost med till '
                    'exempel ägg, och drick den inte på tom mage, så undviker du en snabb blodsockertopp.')),
    139: dict(lead='Granatäpplejuice innehåller polyfenoler, men när kärnorna med sina fibrer silas bort blir sockret mer '
                   'koncentrerat; det glykemiska indexet är lågt (53).',
              tips=('Juicen innehåller mycket polyfenoler, men vid diabetes bör den drickas med måtta: nöj dig med ett '
                    'halvt glas utspätt med vatten.',
                    'Pressa den färsk hemma och drick den direkt utan att sila bort de fina fibrerna, och undvik helt '
                    'färdiga granatäpplejuicer med tillsatt socker och färgämnen.')),
    140: dict(lead='Världens mest kända läsk: en sockerlösning som tas upp snabbt, helt utan protein, fibrer eller annat '
                   'näringsvärde, med ett medelhögt glykemiskt index (63) som belastar bukspottkörteln hårt.',
              tips=('En burk (330 ml) innehåller cirka 9 teskedar socker (36 g) som når blodet inom några minuter; undvik '
                    'den helt om du har diabetes eller fettlever.',
                    'Byt ut den mot naturligt kolsyrat vatten med citronskivor och myntablad eller osötat iste, för att '
                    'njuta av något svalkande utan sockret.')),
    141: dict(lead='Den mest beställda snabbmatshamburgaren: två köttbiffar, vitt bröd och Big Mac-sås. Fettet i köttet '
                   'och såsen bromsar nedbrytningen av brödet, så att det glykemiska indexet blir lågt (55), men kalori- '
                   'och fetthalten är hög.',
              tips=('En måltid med mycket kalorier, industriellt framställt fett och salt; om du ändå äter den, hoppa över '
                    'pommes frites och läsk och drick vatten för att hålla nere måltidens belastning.',
                    'Det smartaste knepet vid bantning och diabetes är att ta bort den övre eller mittersta brödbiten och '
                    'äta burgaren med grön sallad, så minskar kolhydraterna rejält direkt.')),
    142: dict(lead='Bitar av malet kycklingkött med ett friterat ströbrödshölje; protein- och fetthalten gör att det '
                   'glykemiska indexet blir lågt (46), men det friterade mjölhöljet i industriell frityrolja höjer '
                   'kalorierna och mängden oxiderat fett.',
              tips=('Ett val med mindre kolhydrater jämfört med en stor hamburgare eller pommes frites; hemligheten är att '
                    'undvika att doppa dem i barbecuesås och söt sås med fruktosrik majssirap.',
                    'Gör dem hemma: skär kycklingbröst i bitar, vänd dem i havre- eller mandelmjöl och grädda dem i '
                    'airfryer för att minska de härdade oljorna.')),
    143: dict(lead='Hela kycklingbitar som kryddats och friterats i den kända ströbrödsblandningen; själva kycklingköttet '
                   'innehåller ingen stärkelse, och kolhydraterna kommer bara från det krispiga skalet, med ett lågt '
                   'glykemiskt index (45), men skalet är fullt av frityrolja.',
              tips=('Proteinet bromsar blodsockerstegringen, men den stora mängden friterat fett är tung för '
                    'matsmältningen; ät en bit med coleslaw utan söt majonnäs.',
                    'Ta bort hälften av det krispiga skinnet, så slipper du ungefär hälften av den uppsugna oljan och '
                    'mjölet utan att kycklingen förlorar sin saftighet och smak.')),
    144: dict(lead='Den klassiska italienska pizzan: en deg på vitt mjöl med tomatsås och mozzarella. Ostens fett och '
                   'protein bromsar nedbrytningen av degen, med ett medelhögt glykemiskt index (60), men kalorierna ökar '
                   'snabbt.',
              tips=('En bit räcker som en balanserad portion; ät en stor grön sallad med olivolja och vinäger före pizzan '
                    'för att bromsa nedbrytningen av degen.',
                    'Välj tunn, stenugnsbakad pizza (thin crust) på fullkornsmjöl om det finns, och undvik tjocka pizzor '
                    'med ostfyllda kanter.')),
    145: dict(lead='Den mäktigaste pizzan: en bit deg täckt med mozzarella och torkad pepperonikorv. Det glykemiska '
                   'indexet är medelhögt (60) tack vare den höga fetthalten, men den innehåller mycket kalorier, mättat '
                   'fett och salt.',
              tips=('Nöj dig med en bit och drick rikligt med vatten för att balansera saltet; undvik söt läsk till, '
                    'eftersom den kraftigt ökar måltidens sockerbelastning.',
                    'Torka av oljan som ligger på ytan med en bit hushållspapper innan du äter, så blir du av med en hel '
                    'del överflödigt fett.')),
    146: dict(lead='Det mest flexibla snabbmatsvalet: kryddade skivor av kycklingbröst i Subway-bröd med grönsaker. Det '
                   'glykemiska indexet är lågt (52), och hemligheten ligger i valet av bröd och såser.',
              tips=('Beställ smörgåsen med fullkornsbröd (Wheat) och be om alla färska grönsaker som finns (sallad, tomat, '
                    'gurka, paprika) för att få mer fibrer.',
                    'Teriyakisåsen innehåller tillsatt socker; byt ut den mot olivolja, vinäger och naturlig senap för att '
                    'minska stärkelsen och det dolda sockret.')),
    147: dict(lead='Sallad av riven vitkål och morot med majonnäsdressing; fibrerna från den korsblommiga kålen är '
                   'utmärkta och det glykemiska indexet är lågt (35), men färdig dressing innehåller ofta tillsatt socker.',
              tips=('Ett mellanmål eller tillbehör med fibrer från kålen; tänk på att dressingen kan vara söt, och ta en '
                    'liten portion (en halv kopp).',
                    'Gör den hemma genom att blanda kål och morot med grekisk yoghurt, en sked naturlig majonnäs, '
                    'citronsaft och lite senap utan tillsatt socker, så får du en fräsch hemgjord coleslaw.')),
    148: dict(lead='Drottningen bland de orientaliska bakverken: krispiga degblad fyllda med pistage och dränkta i '
                   'sockerlag och ghee. Trots den intensiva sötman bromsar fettet från pistagen och ghee sockret något, '
                   'med ett medelhögt glykemiskt index (67), men socker- och kaloriinnehållet är mycket högt.',
              tips=('En sötsak för glada högtider med en strikt portion: bara en liten bit efter en fiberrik måltid, och '
                    'undvik att äta den på tom mage, så slipper du en kraftig insulinstegring.',
                    'Drick en kopp osötat arabiskt kaffe med en nypa kanel till; kaffets beska bryter sötman i munnen.')),
    149: dict(lead='Levantens stora favorit: gyllene degtrådar med mild vit ost och varm sockerlag. Det glykemiska indexet '
                   'är högt (72), och den höjer blodsockret snabbt eftersom den suger upp mycket sockerlag.',
              tips=('Vid diabetes: ät högst två små bitar och be konditoriet halvera sockerlagen eller byta ut den mot en '
                    'lag sötad med stevia.',
                    'Proteinet i knafehns ost bromsar stärkelsen något jämfört med sötsaker gjorda på industriell grädde; '
                    'drick ett stort glas vatten efteråt.')),
    150: dict(lead='Gyllene mannagrynskaka dränkt i sockerlag och ghee och toppad med mandel; de fina mannagrynen och '
                   'sockerlagen gör att den smälts snabbt, med ett högt glykemiskt index (70) och en hög kolhydrattäthet.',
              tips=('Ät en halv liten bit som efterrätt efter en komplett lunch med sallad och protein, och undvik att äta '
                    'den på morgonen eller mellan måltiderna.',
                    'Om du bakar den själv, byt ut hälften av sockret i lagen mot stevia och strö rikligt med rå mandel på '
                    'ytan för mer fibrer och omättat fett.')),
    151: dict(lead='Glädjen vid högtider och fester: en mannagrynskaka knådad med ghee och fylld med naturlig dadelmassa '
                   'och anis. Fibrerna från dadlarna och fettet från ghee ger ett medelhögt glykemiskt index (62), mer '
                   'måttligt än för bakverk som dränkts i sockerlag.',
              tips=('Det bästa och renaste valet bland de orientaliska bakverken, eftersom sötman främst kommer från '
                    'naturliga dadlar; en bit till kaffet räcker gott för att njuta.',
                    'Välj maamoul bakad på fullkornsmjöl och fylld med naturliga dadlar utan tillsatt vitt socker i '
                    'dadelmassan.')),
    152: dict(lead='Bakverkens vetenskapliga överraskning: trots sockret består halvan till mer än hälften av sesamtahini, '
                   'och sesamens fett och fibrer bromsar sockerupptaget, så att det glykemiska indexet blir lågt (45).',
              tips=('En liten sked mättar snabbt utan någon kraftig blodsockertopp, men den höga energitätheten kräver att '
                    'du håller dig till en liten portion.',
                    'Ät den med en skiva rostat fullkornsbröd eller gurkbitar till frukost, så blir frukosten mer '
                    'mättande.')),
    153: dict(lead='En mild mjölkpudding med smak av apelsinblomsvatten och mastix, kokad på majsstärkelse och mjölk. Det '
                   'glykemiska indexet är lågt (55) och kalorierna är färre än i friterade sötsaker och sötsaker i '
                   'sockerlag.',
              tips=('En mild sommardessert; gör du den hemma kan du halvera sockret och toppa med kanel och naturella '
                    'nötter för mer fibrer.',
                    'Använd standardmjölk och majsstärkelse med måtta, och låt naturlig vanilj och apelsinblomsvatten ge '
                    'en känsla av sötma utan att du behöver mycket socker.')),
    154: dict(lead='En kärleksfull traditionell rätt där riskorn kokas i mjölk, sötas med socker och toppas med kanel; det '
                   'glykemiska indexet är medelhögt (65) tack vare mjölkproteinet som bromsar riset.',
              tips=('En liten skål kall rispudding räcker som en mättande efterrätt efter lunchen; strö rikligt med kanel '
                    'på ytan för en varm och fyllig smak.',
                    'Om du gör den hemma, koka basmatiris i mjölk och använd stevia eller mycket lite socker, och njut av '
                    'den krämiga smaken utan blodsockertoppar.')),
    155: dict(lead='Mörk choklad med hög kakaohalt består till stor del av kakaosmör och innehåller flavonoider och mycket '
                   'fibrer; det glykemiska indexet är lågt (20) och blodsockret stiger mycket lite.',
              tips=('Ett mellanmål som kan stilla sötsuget; två små rutor till en kopp svart kaffe räcker.',
                    'Läs alltid etiketten och kontrollera att kakaohalten är minst 85 %; mjölkchoklad och vit choklad '
                    'innehåller mycket socker och härdade fetter och saknar de här egenskaperna.')),
    156: dict(lead='Doften av en nybakad fransk smörcroissant på morgonen är svår att motstå och en älskad start på dagen, '
                   'men den vanligaste frågan är: höjer den blodsockret snabbt? Svaret är ja. Kombinationen av vitt, '
                   'siktat mjöl och smörlager gör att kolhydraterna tas upp relativt snabbt, med ett glykemiskt index på '
                   '67, vilket kan ge snabb energi följd av ett snabbt blodsockerfall och tidig hunger.',
              tips=('Gör inte croissanten till en ensam frukost på tom mage; kombinera den alltid med en proteinkälla, som '
                    'ett kokt ägg eller en skiva naturell ost, och byt ut juice och söta drycker mot svart kaffe eller '
                    'varmt te utan socker.',
                    'Värm croissanten i ugnen några minuter, så framhävs smörsmaken och du nöjer dig lättare med en halv '
                    'eller en liten croissant som du äter långsamt och njuter av, i stället för att äta den snabbt i '
                    'farten.',
                    'Om du håller koll på blodsockret eller vill gå ner i vikt rekommenderas croissanten som ett '
                    'genomtänkt undantag en gång i veckan, tillsammans med en proteinrik frukost som håller dig mätt hela '
                    'förmiddagen.')),
    157: dict(lead='En av de klassiska desserter som sötsugna oftast frågar om: påverkar cheesecake blodsockret mindre än '
                   'vanlig sockerkaka? Tack vare fyllningen av färskost med mycket fett och protein tas sockret upp '
                   'relativt långsamt, med ett glykemiskt index på 55, men den höga energitätheten och det koncentrerade '
                   'sockret kräver att du är medveten om storleken på biten.',
              tips=('Ät din lilla bit som en lyxig efterrätt efter en komplett huvudmåltid med grönsaker och protein, och '
                    'undvik att äta den som mellanmål mellan måltiderna, så blir insulinsvängningarna mindre.',
                    'Byt ut färdiga söta såser och sylter mot några färska blåbär eller jordgubbar med en nypa kanel; '
                    'bären ger en frisk och ren sötma.',
                    'Även om sockret tas upp relativt långsamt kan en medelstor bit innehålla mer än 350 kalorier, så det '
                    'kan vara klokt att nöja sig med en tredjedel eller en halv bit för att behålla energibalansen.')),
    158: dict(lead='För dig som älskar latinamerikanska smaker är taco med nötfärs en snabb och omtyckt måltid, och många '
                   'undrar om den passar för ett stabilt blodsocker. Den stora fördelen är den proteinrika nötfärsen, som '
                   'bromsar nedbrytningen av tacoskalet och ger ett lågt glykemiskt index, och tacon mättar väl.',
              tips=('Fyll tacon med rikligt med strimlad sallad, tomatbitar och färsk koriander och pressa över lite lime; '
                    'de extra fibrerna bromsar upptaget av majsstärkelsen tydligt.',
                    'Välj tacoskal av fullkornsmajsmjöl som bakats i ugnen i stället för friterade skal, så minskar '
                    'kalorierna och det oxiderade fettet.',
                    'Var uppmärksam på färdiga tacokryddblandningar, som ofta innehåller majsstärkelse och socker som '
                    'förtjockningsmedel; krydda hellre färsen själv med spiskummin, paprikapulver och vitlök.')),
    159: dict(lead='En burrito är en mäktig mexikansk måltid, och dess värde ligger i kombinationen av grillad kyckling '
                   'och bönor. Bönorna ger komplexa kolhydrater med mycket lösliga fibrer, men den stora vita tortillan '
                   'och tillsatt ris kan snabbt höja måltidens glykemiska belastning.',
              tips=('För att undvika blodsockertoppar och trötthet efter lunchen kan du prova en burrito bowl utan den '
                    'stora tortillan, med fokus på kyckling och bönor och färgglada fajitagrönsaker.',
                    'Be att få byta ut det vita riset mot mer svarta bönor eller grillade grönsaker, och välj färsk salsa '
                    'i stället för flytande ostsåser.',
                    'Vid diabetes eller viktkontroll: kom ihåg att en hel burrito med bröd och ris kan innehålla mer än 70 '
                    'g kolhydrater; genom att ändra innehållet får du det bästa av rätten med ungefär hälften så mycket '
                    'kolhydrater.')),
    160: dict(lead='Värmen från smält ost i en rostad tortilla gör quesadillan till ett av de godaste snabba tröstvalen, '
                   'men hur påverkar den vikt och blodsocker? Ostens fett och protein bromsar nedbrytningen av stärkelsen '
                   'i brödet, men eftersom brödet bakas på vitt, siktat vetemjöl behöver portionen hanteras klokt så att '
                   'kalorierna inte blir för många.',
              tips=('Ät inte quesadillan ensam; börja med en grön sallad och doppa bitarna i naturlig guacamole, som '
                    'innehåller enkelomättat fett, i stället för industriellt framställda gräddsåser.',
                    'Förstärk fyllningen med strimlat kycklingbröst, svamp eller grillad paprika vid sidan av osten; det '
                    'ökar protein- och fiberinnehållet och minskar mängden ost som behövs.',
                    'Quesadillan innehåller mycket mättat fett och salt, så att dela rätten med någon annan är det bästa '
                    'sättet att njuta av smaken.')),
    161: dict(lead='Ett av de smartaste och godaste valen på latinamerikanska restauranger för dig som vill äta '
                   'balanserat. Fajitas bygger i grunden på grillat kycklingbröst med strimlad färgglad paprika och lök, '
                   'vilket gör att själva grundrätten innehåller lite kolhydrater, mycket protein och mycket C-vitamin.',
              tips=('Ät kycklingen och de grillade grönsakerna med gaffel som huvudrätt och nöj dig med en liten tortilla, '
                    'eller byt ut brödet helt och rulla in de varma fajitabitarna i stora, krispiga salladsblad.',
                    'Be att kycklingen och grönsakerna steks i lite olivolja i stället för mycket raffinerad olja, och '
                    'njut av grillsmaken och de aromatiska kryddorna som oregano och spiskummin.',
                    'Fajitas i sig är ett utmärkt val för en jämn blodsockernivå; det som främst höjer blodsockret är inte '
                    'det som ligger i pannan, utan hur många tortillor du äter till.')),
    162: dict(lead='En favorit på kvällar och sammankomster, men friterade majschips täckta med industriellt framställd '
                   'cheddarost gör nachos till en snabbt smält kaloribomb. Den vanliga frågan är hur man äter dem utan att '
                   'drabbas av trötthet och en blodsockertopp, och hemligheten är att göra om "chips med ost" till en '
                   'balanserad måltid.',
              tips=('Gör nachos till en rätt att dela med familj eller vänner i stället för att ställa en egen tallrik '
                    'framför dig, och ät några bitar i taget medan du fokuserar på samtalet och sällskapet.',
                    'Lägg till grillad kyckling, svarta bönor, pico de gallo (tomat, lök och koriander) och jalapeñoskivor '
                    'för mer protein och fibrer och färre friterade chips.',
                    'Färdiga nachosåser innehåller mycket härdat fett, salt och dold stärkelse, så att baka tortillachips '
                    'i ugnen med naturlig ost hemma är ett bättre alternativ.')),
    163: dict(lead='Den traditionella mexikanska avokadoröran, köksgrönt guld: den innehåller nästan inga nettokolhydrater '
                   'men mycket enkelomättat fett och lösliga fibrer, så det glykemiska indexet är inte tillämpligt, och '
                   'den mättar länge.',
              tips=('Använd guacamole som ett smart alternativ till majonnäs och industriellt framställda såser i '
                    'smörgåsar och rätter, och ät den som dipp till krispiga gurk- och morotsstavar i stället för färdiga '
                    'kex och chips.',
                    'Mosa färsk avokado med gaffel tillsammans med limesaft, hackad tomat, färsk koriander och lite '
                    'havssalt; limen hindrar avokadon från att mörkna.',
                    'Den höga fetthalten gör den energität, så två till tre matskedar räcker gott för att göra måltiden '
                    'mättande.')),
    164: dict(lead='Med sin fräscha blandning av färska tomater, lök, koriander och chili är salsa en av de bästa '
                   'naturliga såserna som finns. Den innehåller mycket lite kalorier och kolhydrater och ger en '
                   'oemotståndlig smak åt vilken rätt som helst utan någon blodsockertopp.',
              tips=('Använd salsa som en färgglad grundsås till morgonens ägg, grillat kycklingbröst och fisk, för att '
                    'bryta enformigheten i bantningskosten med en levande smak; tomaterna innehåller lykopen.',
                    'Gör salsan hemma och rå (salsa fresca) för att bevara C-vitaminet och mikronäringsämnena, och '
                    'tillsätt några droppar äppelcidervinäger och limesaft för en god syrlighet.',
                    'När du köper färdig salsa, läs alltid ingrediensförteckningen och kontrollera att den är fri från '
                    'tillsatt socker och modifierad majsstärkelse, som vissa tillverkare använder som förtjockningsmedel.')),
    165: dict(lead='En gryta av köttfärs med röda bönor, tomat och chili: en värmande och mycket mättande vinterrätt. '
                   'Kombinationen av köttets protein och bönornas fibrer ger ett lågt glykemiskt index (38).',
              tips=('Njut av chilin som en komplett och mättande gryta i en djup skål med en färsk bladsallad vid sidan '
                    'om, och undvik att servera den på berg av vitt ris, som ökar stärkelsebelastningen.',
                    'Låt chilin sjuda långsamt på låg värme så att kryddorna blandas med bönorna, och toppa gärna med en '
                    'tesked naturell grekisk yoghurt i stället för gräddfil för mer protein.',
                    'En utmärkt rätt för aktiva personer och för dig som vill ha ett stabilt blodsocker länge tack vare '
                    'fibrerna; drick rikligt med vatten, så hanterar magen baljväxternas fibrer lättare.')),
    166: dict(lead='Det italienska kökets drottning och den mest värmande familjerätten på helgerna. Den vanligaste frågan '
                   'är om lasagne med köttfärs och béchamel höjer blodsockret snabbt. Sanningen är att köttfärsen, '
                   'mozzarellan och tomatsåsen bromsar upptaget av pastaplattorna och ger ett lågt glykemiskt index (52), '
                   'men béchamelns fyllighet och den höga stärkelsemängden gör att storleken på biten är det som verkligen '
                   'avgör.',
              tips=('Börja måltiden med en rejäl grön bladsallad med olivolja och äppelcidervinäger; fibrerna kan bromsa '
                    'upptaget av stärkelsen i pastan. Ät sedan en medelstor bit utan att äta dig övermätt.',
                    'Ett smart kökstrick: byt ut hälften av lasagneplattorna mot tunna skivor av zucchini eller grillad '
                    'aubergine; det minskar kolhydraterna betydligt och ökar fiber- och vatteninnehållet med bibehållen '
                    'fyllig konsistens.',
                    'En medelstor bit lasagne är en komplett, energität och fettrik måltid, så njut av den som huvudrätt '
                    'och undvik vitlöksbröd eller söta desserter direkt efteråt.')),
    167: dict(lead='Den äkta romerska pastan som miljoner älskar för sin sammetslena sås av äggula och parmesan eller '
                   'pecorino. Många blir förvånade över att klassisk spaghetti inte höjer blodsockret så kraftigt som man '
                   'tror: kokad al dente och tillsammans med äggets protein och ostens fett får den ett lågt glykemiskt '
                   'index (50) och smälts gradvis.',
              tips=('Begränsa din portion till högst cirka en kopp kokt spaghetti, och ät den med broccoli eller grillad '
                    'sparris vid sidan om för en bättre balans mellan näringsämnen och fibrer.',
                    'Pastans hemlighet är al dente-regeln: koka inte spaghettin tills den blir mjuk, utan ta upp den medan '
                    'den fortfarande har tuggmotstånd; då behåller stärkelsen en kompakt struktur som '
                    'matsmältningsenzymerna inte bryter ned till socker lika snabbt.',
                    'Eftersom originalreceptet innehåller mycket mättat fett och salt är det bättre att laga den med färsk '
                    'äggula, mindre tillsatt salt och mer smak från svartpeppar och naturlig ost.')),
    168: dict(lead='Den mest kända och spridda husmansrätten i världen: spaghetti med en ragùsås rik på köttfärs och '
                   'långkokta tomater. Den fina balansen mellan köttets protein och tomaternas fibrer ger rätten ett lågt '
                   'glykemiskt index (50), vilket gör den till ett tryggt och mättande val om du håller koll på mängden.',
              tips=('Vänd på den vanliga tallriksmodellen: låt köttfärssåsen och grönsakerna ta upp ungefär två '
                    'tredjedelar av tallriken och pastan en måttlig del, så blir måltiden mer mättande och '
                    'stärkelsebelastningen lägre.',
                    'Tillsätt riven morot, hackad svamp och finhackad selleri i tomatsåsen under tillagningen; grönsakerna '
                    'som kokas med köttet förstärker smaken och ger mer lösliga fibrer utan att smaken ändras märkbart.',
                    'När tomatsåsen kokas med olivolja och kött tas lykopenet upp bättre.')),
    169: dict(lead='Breda fettuccineband i en sås av grädde, smör och parmesan ger en fyllig och lyxig smak. Utmaningen '
                   'med Alfredo är inte en snabb blodsockerstegring, eftersom det rikliga fettet bromsar magsäckstömningen '
                   'och ger ett lågt glykemiskt index (48), utan den höga energitätheten, som kräver att du äter klokt.',
              tips=('Gör fettuccine Alfredo till en rätt för speciella tillfällen och lägg alltid till en ren '
                    'proteinkälla, som grillat kycklingbröst eller räkor, så minskar lusten att äta stora mängder pasta.',
                    'Gör en mindre mäktig version hemma genom att byta ut en del av den tjocka matlagningsgrädden mot '
                    'naturlig kycklingbuljong eller mjölk, med äkta parmesan, lite vitlök och muskotnöt för en äkta och '
                    'frisk smak.',
                    'Om du håller koll på blodfetterna, tänk på att en klassisk Alfredo på restaurang innehåller mycket '
                    'mättat fett, så att dela tallriken är ett klokt val.')),
    170: dict(lead='Det berömda italienska risets mästerverk, med en sammetslen konsistens som smälter i munnen. Men den '
                   'viktiga frågan är: påverkar risotto blodsockret mindre än vanligt ris? I själva verket görs risotto på '
                   'arborioris, ett kortkornigt ris med mycket amylopektin som bryts ned snabbt, vilket ger ett medelhögt '
                   'glykemiskt index (68), så det behöver kombineras klokt för att bromsa nedbrytningen.',
              tips=('Ät inte risotton ensam som huvudrätt, utan som tillbehör i storlek med en knytnäve tillsammans med en '
                    'rejäl bit grillad fisk eller kyckling och en ruccolasallad med rikligt med olivolja.',
                    'Laga risotton med rikligt med färsk skivad svamp och naturlig kycklingbuljong; svampen tillför fibrer '
                    'som kan bromsa upptaget av risets stärkelse.',
                    'Om du älskar risotto och har insulinresistens rekommenderas att du undviker grädde och för mycket '
                    'smör, nöjer dig med lite äkta parmesan och tuggar riskornen mycket långsamt.')),
    171: dict(lead='De små, mjuka gnocchibitarna ser ut som aptitliga kuddar, men grundingredienserna är mosad kokt '
                   'potatis och vetemjöl. Eftersom stärkelsen i mosad potatis bryts ned mycket snabbt har gnocchi ett '
                   'medelhögt glykemiskt index (68), vilket kan ge en snabb blodsockerstegring om de inte kombineras med '
                   'fibrer och fett.',
              tips=('Minska antalet gnocchi på tallriken och låt dem bli en lyxig stärkelsedetalj, och börja gärna '
                    'måltiden med en krispig grönsallad för att dämpa glukostoppen i blodet.',
                    'Undvik söta färdiga såser och välj i stället pesto med extra jungfruolivolja, pinjenötter och färsk '
                    'basilika; det enkelomättade fettet i olivoljan bromsar upptaget av stärkelsen i gnocchin.',
                    'Om du äter lågkolhydratkost eller är känslig för glukos kan du prova blomkålsgnocchi som ett smart '
                    'hemgjort alternativ med samma konsistens och mycket mindre stärkelse.')),
    172: dict(lead='Calzone är hela pizzanjutningen, men inrullad och tätt försluten så att all saftighet, värme och smält '
                   'ost stannar inuti. Den har en tjock deg och en kompakt fyllning, vilket gör den till en måltid med '
                   'mycket kolhydrater och kalorier och ett medelhögt glykemiskt index (58), så den kräver en smart plan '
                   'för hur du delar och äter den.',
              tips=('Den gyllene regeln med calzone är att dela; en halv calzone med en fräsch italiensk sallad räcker '
                    'gott för att du ska bli mätt och nöjd utan att känna dig tung och trött efter maten.',
                    'Be om en fyllning med mycket spenat, svamp, lök och grillad paprika tillsammans med kyckling eller '
                    'magert nötkött, och undvik charkuterier och kanter fyllda med mer industriell ost.',
                    'Den slutna degen stänger in olja och fett, så låt den svalna lite och torka av överflödig olja på '
                    'skorpan med hushållspapper; det minskar onödigt fett och gör den lättare att smälta.')),
    173: dict(lead='En symbol för enkelhet och elegans bland de toskanska förrätterna: krispiga, rostade brödskivor '
                   'toppade med en strålande blandning av mogna tomater, vitlök, aromatisk basilika och extra '
                   'jungfruolivolja. Ett fräscht och glatt val med en måttlig mängd stärkelse och ett lågt glykemiskt '
                   'index (55).',
              tips=('En till två bitar bruschetta räcker gott som en aptitlig inledning före huvudrätten och kan dämpa den '
                    'värsta hungern.',
                    'Rosta brödskivorna ordentligt tills de är gyllene och krispiga, eftersom rostning delvis ändrar hur '
                    'snabbt stärkelsen bryts ned, och gnid in brödet med en färsk vitlöksklyfta innan du lägger på '
                    'tomatblandningen för mer smak.',
                    'Använd alltid färska, hela tomater som du hackar för hand och undvik sötad tomatpuré på burk, och '
                    'välj kallpressad extra jungfruolivolja.')),
    174: dict(lead='Mästerverket från den italienska ön Capri sammanfattar medelhavskostens skönhet i sin enkelhet: skivor '
                   'av färsk mozzarella, mogna röda tomater och doftande gröna basilikablad med en stråle extra '
                   'jungfruolivolja. Rätten påverkar i praktiken inte blodsockret; nettokolhydraterna är försumbara och '
                   'det glykemiska indexet är inte tillämpligt.',
              tips=('En utmärkt rätt att inleda lunch eller middag med; proteinet i mozzarellan och det enkelomättade '
                    'fettet i olivoljan kan tillsammans bromsa nedbrytningen av stärkelsen i måltiden som följer.',
                    'Strö över lite havssalt och nymalen svartpeppar och ringla en liten mängd traditionell, osötad '
                    'balsamvinäger, och undvik tjock färdig balsamicokräm med tillsatt socker eller karamell.',
                    'Ett idealiskt och klassiskt val vid diabetes, insulinresistens, keto och lågkolhydratkost, eftersom '
                    'rätten mättar ordentligt utan någon kolhydratbelastning.')),
    175: dict(lead='Den rustika, traditionella grönsakssoppan som gått i arv i italienska familjer. Soppan är full av '
                   'zucchini, morot, vita bönor, selleri och tomat med en liten mängd små pastabitar. Det glykemiska '
                   'indexet är lågt (39), och den är ett utmärkt exempel på en rätt som ger ett stabilt blodsocker.',
              tips=('En härlig rätt att inleda lunchen eller middagen med; den varma soppan fyller en stor del av magen '
                    'och ger en tidig känsla av mättnad, så att du lättare undviker att äta för mycket av de mäktiga '
                    'rätterna som följer.',
                    'Koka grönsakerna på låg värme så att de behåller lite tuggmotstånd och inte blir helt mosiga, och öka '
                    'mängden bönor och bladgrönsaker samtidigt som du håller pastan till ett minimum.',
                    'Bönorna i minestronen innehåller lösliga fibrer och folat.')),
    176: dict(lead='Sushi är älskat över hela världen som en symbol för lättsam och elegant mat, men den vanligaste frågan '
                   'är: höjer sushiriset blodsockret? Sushiris smaksätts med vinäger och tillsatt socker, vilket ger ett '
                   'lågt glykemiskt index (52), och laxens fett med omega-3 och laxens protein bromsar upptaget och ger '
                   'måltiden en fin balans.',
              tips=('Börja måltiden med en skål misosoppa eller en edamamesallad för fibrer och protein, och nöj dig med '
                    '6–8 bitar som en komplett måltid; undvik friterade rullar (crunchy) och rullar dränkta i söta, '
                    'krämiga såser.',
                    'Doppa sushibiten med laxsidan, inte rissidan, i utspädd sojasås, så suger riset inte upp för mycket '
                    'salt, och njut av lite naturlig wasabi för smakens skull.',
                    '⚠️ Laxen måste vara färsk, avsedd för sushi och fryst i förväg enligt säkerhetsreglerna för fisk; rå '
                    'fisk rekommenderas inte för gravida, barn eller personer med nedsatt immunförsvar, på grund av risken '
                    'för parasiter och bakterier.')),
    177: dict(lead='Den mest beställda och populära rullen i världen: mjuk avokado, krispig gurka och crabsticks i en '
                   'välformad rulle av ris och rostade sesamfrön. En fräsch och lättsam måltid med ett lågt glykemiskt '
                   'index (55), men tänk på att industriellt framställda crabsticks innehåller dold stärkelse.',
              tips=('Håll portionen till 6–8 bitar och komplettera med en grön sallad för mer fibrer, så att stärkelsen '
                    'tas upp gradvis.',
                    'Njut av naturlig inlagd ingefära mellan bitarna för att rensa smaklökarna, och undvik extra stark '
                    'majonnäs ovanpå rullarna.',
                    'Crabsticks (surimi) är bearbetat fiskprotein med tillsatt majsstärkelse; de är alltså inte rent '
                    'protein för dig som äter strikt lågkolhydratkost och bör räknas som stärkelse.')),
    178: dict(lead='Ren mat i sin finaste form: skivor av färsk lax utan ett enda riskorn eller tillsatt socker. Inga '
                   'nettokolhydrater, och det glykemiska indexet är inte tillämpligt, vilket gör den till ett mycket '
                   'blodsockervänligt val och en utmärkt källa till omega-3-fettsyror och protein av hög kvalitet.',
              tips=('Ett oslagbart val för en ren mättnad; protein bidrar till att öka och bibehålla muskelmassan. Ät den '
                    'med krispiga gurkskivor och sjögrässallad (wakame) för ett mineralrikt komplement.',
                    'Ät den kyld på en bädd av is med lite pressad citron eller några droppar sojasås med reducerad '
                    'salthalt, så njuter du av fiskens naturliga sötma och fräscha smak utan tunga såser.',
                    '⚠️ Köp laxen från en pålitlig källa och avsedd att ätas rå (sashimikvalitet); gravida, ammande och '
                    'personer med nedsatt immunförsvar bör helt avstå, för att undvika risken för bakteriella infektioner '
                    'från fisk.')),
    179: dict(lead='Japans mest kända skål för värme och välbehag: en smakrik kycklingbuljong med färska vetenudlar, ett '
                   'kokt ägg och möra kycklingskivor. Den viktigaste frågan är om ramen passar vid bantning och för '
                   'blodsockret. Proteinet och buljongen mättar väl, men vetenudlarna är en rik kolhydratkälla med ett '
                   'lågt glykemiskt index (55), och den koncentrerade buljongen innehåller mycket salt.',
              tips=('Ät först det kokta ägget, kycklingbitarna och grönsakerna för att bromsa upptaget av nudlarnas '
                    'stärkelse, och ät bara hälften av nudlarna i skålen för att spara kolhydrater.',
                    'Be om en mindre salt buljong utan tillsatt fett, och lägg till mer bambuskott, salladslök och '
                    'shiitakesvamp för mer näringsämnen.',
                    'Undvik att dricka upp hela buljongen i botten av skålen; den innehåller mycket stora mängder salt, '
                    'som kan ge vätskeansamling och höjt blodtryck hos personer som är känsliga för salt.')),
    180: dict(lead='Thailändsk gatumat i en glad rätt: stekta risnudlar blandade med ägg, rostade jordnötter och tofu '
                   'eller räkor. Hemligheten bakom smaken är blandningen av surt och sött, men färdig tamarindsås '
                   'innehåller ofta tillsatt socker; det glykemiska indexet ligger på 52, i det låga intervallet, och '
                   'stärkelsen bryts ned relativt snabbt.',
              tips=('Be om mindre socker om det går och pressa en hel lime över rätten; limens syra kan bromsa '
                    'nedbrytningen av stärkelsen. Blanda i krispiga, råa böngroddar för mer fibrer.',
                    'Fokusera på en större andel räkor eller tofu och ägg och en mindre mängd risnudlar, och njut av de '
                    'krossade jordnötterna, vars fett bromsar nedbrytningen av kolhydraterna.',
                    'Risnudlar är naturligt glutenfria, men personer med glutenintolerans eller veteallergi bör '
                    'kontrollera att sojasåsen och fisksåsen i marinaden är helt glutenfria.')),
    181: dict(lead='Möra kycklingbitar i blank teriyakisås förenar animaliskt protein av hög kvalitet med en omtyckt '
                   'asiatisk smak. Men det många missar är att traditionell teriyakisås bygger på socker eller '
                   'karamelliserad honung med soja, vilket höjer måltidens glykemiska index (45) trots att själva '
                   'kycklingen saknar stärkelse.',
              tips=('Ät teriyakikycklingen med en rejäl portion ångkokt broccoli eller asiatiska grönsaker i stället för '
                    'ett berg av vitt ris, för att undvika att såsens socker ger en snabb glukosstegring.',
                    'När du lagar den hemma, pensla kycklingen med lite sås i stället för att doppa den, och byt gärna ut '
                    'hälften av sockret mot ett sötningsmedel tillsammans med färsk ingefära och vitlök för en kraftig '
                    'smak utan fritt socker.',
                    'Vid diabetes eller viktkontroll: kom ihåg att två matskedar färdig teriyakisås kan innehålla mer än '
                    '10 g tillsatt socker, så att vara sparsam med såsen gör hela skillnaden.')),
    182: dict(lead='Kycklingfilé panerad i japanskt pankoströbröd och friterad tills den blir helt gyllene och krispig. '
                   'Katsu ger en oemotståndlig krispighet och rent protein, men paneringen och den uppsugna frityroljan '
                   'höjer rättens glykemiska belastning och kalorier (GI 55) jämfört med vanlig grillad kyckling.',
              tips=('Katsu serveras traditionellt med ett berg av finstrimlad vitkål; hoppa aldrig över den! Ät upp kålen '
                    'först med lite citron; fibrerna kan bromsa upptaget av paneringens stärkelse.',
                    'Du kan göra en gyllene katsu med mindre fett i airfryer med lite olivolja; det ger samma japanska '
                    'krispighet med ungefär hälften så mycket uppsuget fett och kalorier.',
                    'Den tillhörande tonkatsusåsen är söt och påminner mycket om barbecuesås; ha lite vid sidan om att '
                    'doppa i, och undvik att hälla hela såsen över de krispiga kycklingbitarna.')),
    183: dict(lead='Asiens tunna degknyten fyllda med köttfärs eller grönsaker och ångkokta i bambukorgar. Fördelen med '
                   'ångkokning är att degen förblir tunn och helt fri från frityrolja, vilket ger ett lågt glykemiskt '
                   'index (48).',
              tips=('Håll portionen till 4–6 stycken som ett mättande mellanmål, och ät en tallrik kokta gröna '
                    'bladgrönsaker (som pak choi) till för mer fibrer.',
                    'Välj fyllningar med mycket kött och grönsaker som kål och salladslök, och doppa i en blandning av '
                    'kinesisk svart vinäger, hackad ingefära och lite sesamolja i stället för söta såser.',
                    'Ångkokta dumplings är ett betydligt bättre val än friterade, krispiga dumplings (potstickers); du '
                    'slipper det härdade frityrfettet och får en jämnare blodsockernivå.')),
    184: dict(lead='Krispiga asiatiska grönsaksrullar är en av världens mest kända förrätter: spröda degblad som omsluter '
                   'kål, morot och svamp. Trots den grönsaksrika fyllningen gör friteringen i mycket olja och det '
                   'stärkelserika degbladet dem till en snabb kaloritillförsel, med ett lågt glykemiskt index (50).',
              tips=('Gör dem inte till en huvudrätt, utan ät en eller högst två som förrätt, och undvik att doppa dem i '
                    'färdig sweet chilisås med fruktosrik majssirap.',
                    'Det bästa alternativet är färska, icke-friterade vietnamesiska vårrullar (summer rolls) i mjukt '
                    'rispapper med mynta och räkor; de ger en fräsch krispighet med betydligt färre kalorier.',
                    'Friterade vårrullar suger snabbt upp olja eftersom degbladen är så tunna, så låt dem rinna av väl på '
                    'hushållspapper direkt när de tas upp ur oljan; det minskar överflödigt fett och gör dem lättare att '
                    'smälta.')),
    185: dict(lead='Kärnan i det traditionella japanska köket: en mild buljong med fermenterad sojabönspasta, '
                   'tofutärningar och sjögräs (wakame). Soppan påverkar i praktiken inte blodsockret; nettokolhydraterna '
                   'är försumbara och det glykemiska indexet är inte tillämpligt.',
              tips=('En utmärkt soppa att inleda en asiatisk måltid med; den varma soppan fyller en stor del av magen, '
                    'vilket motverkar storätande och ger en mer balanserad måltid.',
                    'Rör ned misopastan i slutet av tillagningen, direkt efter att du stängt av värmen, och undvik att '
                    'koka den kraftigt, eftersom kraftig kokning förstör de levande bakterierna från den naturliga '
                    'jäsningen.',
                    'Misosoppa innehåller mycket salt från den saltade jäsningen, så om du har högt blodtryck '
                    'rekommenderas en liten skål om dagen.')),
    186: dict(lead='Grundstenen för vegetabiliskt protein i Fjärran Östern: ren, pressad sojabönsostmassa i kuber. Tofu är '
                   'nästan fri från nettokolhydrater (cirka 1,6 g per 100 g) och det glykemiska indexet är inte '
                   'tillämpligt, vilket gör den till ett utmärkt val för ett stabilt blodsocker.',
              tips=('Ett utmärkt vegetariskt val för en balanserad måltid utan glukostoppar; woka den med blandade '
                    'grönsaker i lite sesamolja med ingefära och vitlök.',
                    'Hemligheten bakom smaken är att pressa ut vätskan: pressa tofublocket under en tung handduk i 15 '
                    'minuter innan du skär det, så suger det upp kryddorna som en svamp och får en härligt krispig yta vid '
                    'tillagningen.',
                    'Tofu innehåller naturliga isoflavoner, kalcium och järn; den är ett tryggt och mycket mättande '
                    'alternativ i vegetarisk kost och vid insulinresistens.')),
    187: dict(lead='Indonesiens traditionella skatt: hela, fermenterade sojabönor som bildar ett fast block med en omtyckt '
                   'nötig smak. Tempeh skiljer sig från många andra proteinkällor genom att hela bönan behålls under '
                   'fermenteringen, och det glykemiska indexet är lågt (20).',
              tips=('Skär tempeh i tunna skivor och grilla dem i airfryer eller ugn med sojasås och olivolja; det ger en '
                    'rejäl mättnad i flera timmar.',
                    'Att ångkoka tempehskivorna i 5 minuter innan du marinerar dem tar bort en lätt bitter smak och låter '
                    'kryddorna och marinaden tränga djupt in i det fermenterade blocket.',
                    'Under den naturliga fermenteringen bryts fytinsyran och en del av proteinerna ned, vilket kan '
                    'förbättra upptaget av mineraler som magnesium, järn och zink jämfört med ofermenterade sojabönor.')),
    188: dict(lead='Pärlan i det koreanska köket som har erövrat världen: traditionellt fermenterad kål med koreansk '
                   'chili, vitlök och ingefära. Nettokolhydraterna är nära noll och det glykemiska indexet är inte '
                   'tillämpligt; den innehåller fibrer och levande mjölksyrabakterier.',
              tips=('Ät två matskedar kall kimchi till ris- eller kötträtter; den syrliga, starka smaken passar bra till '
                    'måltidens stärkelse.',
                    'Njut av den rå och krispig utan att utsätta den för hög värme, så bevaras de levande '
                    'mjölksyrabakterierna som bildats under veckornas fermentering.',
                    'Kimchi innehåller mycket salt och starka kryddor, så introducera den gradvis om du har känslig mage '
                    'eller halsbränna.')),
    189: dict(lead='Det indiska kökets mest kända ambassadör: möra tandoorikycklingbitar i en krämig tomatsås med '
                   'aromatiska kryddor som ingefära och garam masala. Kycklingen ger rent protein och såsens fett bromsar '
                   'matsmältningen, vilket ger måltiden ett lågt glykemiskt index (45) och en långvarig mättnad.',
              tips=('Njut av kycklingbitarna med en generös mängd sås och ät dem tillsammans med tillagade grönsaker eller '
                    'gurksallad med yoghurt (raita) i stället för stora mängder vitt ris.',
                    'När du lagar den hemma kan du byta ut en del av matlagningsgrädden mot naturell grekisk yoghurt; det '
                    'minskar det mättade fettet och ökar proteinet utan att förstöra den sammetslena konsistensen.',
                    'Färdiga såser på restauranger kan innehålla tillsatt socker för att balansera tomatens syra, så '
                    'måttlighet och äkta kryddor hjälper dig att undvika osynligt tillsatt socker.')),
    190: dict(lead='Indiens främsta gröna vegetariska mästerverk: kryddat mos av färsk spenat med tärningar av den '
                   'traditionella osten paneer. Rätten innehåller fibrer, järn och kalcium och har ett lågt glykemiskt '
                   'index (30), vilket gör den till ett utmärkt val för ett stabilt blodsocker och en behaglig mättnad.',
              tips=('Ett utmärkt val till lunch eller middag; spenaten innehåller magnesium och paneern ger protein som '
                    'bryts ned långsamt.',
                    'Tillaga spenaten varsamt utan att koka den för länge, så behåller den sin klara färg och sina '
                    'vitaminer, och tillsätt lite färsk ingefära och spiskummin för smakens skull.',
                    'Om du räknar kalorier noga är det bättre att bryna osttärningarna i en torr panna med lite naturligt '
                    'ghee än att fritera dem i mycket olja, och att hålla portionen måttlig.')),
    191: dict(lead='Det indiska bordets sultan: omsorgsfulla lager av långkornigt basmatiris, kryddad kyckling, saffran '
                   'och varma kryddor. Basmatiris har naturligt ett lägre glykemiskt index än kortkornigt ris, och '
                   'tillsammans med kycklingens protein och marinadens fett blir det glykemiska indexet medelhögt (58), '
                   'men rätten är energität och kräver medvetenhet om portionen.',
              tips=('Fyll halva tallriken med yoghurtsallad med gurka och mynta (raita) och kycklingbitarna först, och '
                    'lägg sedan till en måttlig portion biryaniris; yoghurten och grönsakerna bromsar effektivt upptaget '
                    'av risets stärkelse.',
                    'Blötlägg basmatiriset i 30 minuter och skölj det väl för att få bort överflödig ytstärkelse, och ånga '
                    'kycklingen och riset i en tätt sluten gryta (dum-metoden) för att minska den tillsatta oljan.',
                    'Tänk på portionen: biryani är en komplett och energität måltid, så undvik läsk och efterrätt direkt '
                    'efteråt, så slipper du känna dig övermätt och trött.')),
    192: dict(lead='Det spröda, platta brödet som bakas mot väggarna i lerugnen tandoor och penslas med smör, vitlök och '
                   'koriander. Naan bakas främst på vitt, siktat och jäst mjöl, vilket ger ett högt glykemiskt index (71) '
                   'och en snabb nedbrytning till socker om det äts ensamt.',
              tips=('Ät inte naanbröd ensamt som mellanmål, utan bryt små bitar att äta proteinrika rätter med, som '
                    'tandoorikyckling eller dal, och undvik att äta ett helt bröd själv.',
                    'När du bakar det hemma kan du blanda fullkornsvetemjöl och vitt mjöl i lika delar för mer fibrer, och '
                    'pensla det med olivolja och hackad vitlök i stället för mycket smör.',
                    'Ett stort naanbröd kan ge 45–50 g snabba kolhydrater, så att dela brödet är ett smart val för '
                    'blodsockret.')),
    193: dict(lead='Kärnan i indiska hem och en symbol för enkel matlagning: en långsamt kokt soppa på gula linser med '
                   'gurkmeja, spiskummin och ingefära. Dal innehåller mycket vegetabiliskt protein och lösliga fibrer och '
                   'har ett lågt glykemiskt index (32), vilket gör den till en utmärkt mat för långvarig mättnad.',
              tips=('Börja måltiden med en varm skål dal; de rikliga fibrerna kan bromsa upptaget av stärkelsen i resten '
                    'av måltiden, och soppan ger snabbt en behaglig känsla av mättnad.',
                    'Pressa över färsk citron precis före servering, eftersom C-vitamin ökar järnupptaget, och strö över '
                    'en nypa spiskummin.',
                    'Dal är ett utmärkt, värmande vegetariskt alternativ till tunga rätter under vinterdagarna och passar '
                    'mycket bra vid diabetes, så länge den inte tillagas med överdrivna mängder fett.')),
    194: dict(lead='De franska bageriernas ikon med sin gyllene, krispiga skorpa och sitt luftiga, vita inkråm. Baguetten '
                   'bakas på högraffinerat vitt vetemjöl, vilket gör att stärkelsen tas upp mycket snabbt, med ett högt '
                   'glykemiskt index (73), och det förklarar varför man snabbt blir hungrig igen om man äter den ensam.',
              tips=('Undvik att äta baguetten ensam eller med sylt; kombinera alltid din skiva med en källa till protein '
                    "och fett, som naturlig ost, ägg eller olivolja med za'atar, för att bromsa blodsockerstegringen.",
                    'Välj baguette på fullkorn eller med långsam naturlig jäsning (surdeg) om det finns; mjölksyran som '
                    'bildas vid den långsamma jäsningen sänker det glykemiska indexet märkbart.',
                    'En liten bit lika lång som handflatan (cirka 50 g) räcker för att njuta av den franska krispigheten; '
                    'om du håller koll på vikten och blodsockret är det bättre att låta den vara ett undantag i en '
                    'balanserad måltid.')),
    195: dict(lead='Det platta, mjuka brödet som är grunden i de mest kända latinamerikanska rätterna, som taco och '
                   'fajitas. Traditionella majstortillor har ett lågt glykemiskt index (52) tack vare att majsen behandlas '
                   'med kalk (nixtamalisering), vilket bevarar fibrerna, medan tortillor av vitt vetemjöl tas upp snabbare '
                   'och innehåller mer kalorier.',
              tips=('Välj alltid tortillor av gul majs eller fullkornsvete och nöj dig med två små, fyllda generöst med '
                    'protein som kyckling och fisk samt bladgrönsaker och avokado.',
                    'Värm tortillan i en torr, het panna utan olja; den torra värmen ger tillbaka mjukheten och den '
                    'naturliga rostade smaken utan osynliga kalorier från fett.',
                    'Läs ingrediensförteckningen på förpackade tortillor; många färdiga produkter innehåller härdade '
                    'vegetabiliska oljor och socker för att hålla dem mjuka länge.')),
    196: dict(lead='Det orientaliska bordets härskare och frukostsmörgåsarnas grund, men eftersom det är så tunt och '
                   'lättätet äter vi ofta mycket av det utan att tänka på det. Den höga stärkelsetätheten ger ett högt '
                   'glykemiskt index (70), vilket kräver medvetenhet om portionsstorlek och fyllning.',
              tips=('Ett bröd motsvarar ungefär två till tre skivor rostbröd; fyll brödet till 70 % med grönsaker och '
                    'magert protein (som ägg, ful medames eller kyckling) för att minska brödets andel.',
                    'Välj pitabröd bakat på fullkornsmjöl eller med kli, och rosta det i ugnen med lite olivolja och '
                    "za'atar i stället för att fritera det.")),
    197: dict(lead='Den trekantiga pärlan bland de levantinska bakverken: en tunn deg som omsluter en generös fyllning av '
                   'färsk spenat kryddad med extra jungfruolivolja, lök och syrlig sumak. Balansen mellan sumakens syra, '
                   'spenatens fibrer och olivoljan ger ett lågt glykemiskt index (52), och de hör till de minst mäktiga '
                   'pajerna.',
              tips=('En till två medelstora fatayer räcker som frukost eller kvällsmat, tillsammans med en kopp varmt te '
                    'utan socker och en tallrik gurk- och tomatskivor.',
                    'Hemligheten bakom en riktigt god levantinsk spenatpaj är att öka mängden spenatfyllning och göra '
                    'degen mycket tunn, och att krama ur spenaten väl så att smaken av sumak och olivolja behålls.',
                    'Spenat innehåller folat, järn och C-vitamin, och fatayer är ett utmärkt vegetariskt val som hela '
                    'familjen tycker om när de bakas i ugnen utan fritering.')),
    198: dict(lead='Den älskade morgonvärmen i varje kvarter: en gyllene bakad deg fylld med mild vit ost och en nypa '
                   'svartkummin. Ostens protein och fett bromsar nedbrytningen av degens stärkelse och ger ett lågt '
                   'glykemiskt index (50), och de mättar länge.',
              tips=('Ät fatayer långsamt och njut av dem som en kompakt huvudmåltid, gärna tillsammans med bladgrönsaker '
                    'som färsk mynta och ruccola för mer fibrer och för att balansera ostens salthalt.',
                    'Lägg osten i ljummet vatten innan du gör fatayer, så försvinner överflödigt salt, och tillsätt '
                    'svartkummin och sesamfrön, som ger fett och en traditionell smak.',
                    'Osten i fatayer innehåller en hel del kalcium men kan vara fettrik, så det räcker att äta en '
                    'medelstor bit för att bli mätt utan att belasta matsmältningen.')),
    199: dict(lead='Pärlan i Aleppos och Levantens bagerier: en mycket tunn och krispig deg toppad med kryddad köttfärs '
                   'med granatäpplesirap, tomat och pinjenötter. Den tunna degen och den höga mängden animaliskt protein '
                   'och fett ger ett medelhögt glykemiskt index (60).',
              tips=('Ät lahmacun med en skål yoghurt eller gurksallad med yoghurt; yoghurtens protein bromsar upptaget av '
                    'kolhydraterna, och måltiden blir mer mättande.',
                    'Grädda lahmacun på plåt eller i mycket varm ugn i bara några minuter, så blir den snabbt krispig utan '
                    'att köttet torkar, och var sparsam med färdig granatäpplesirap sötad med socker.',
                    'Levantinsk lahmacun har en fördel jämfört med västerländsk pizza tack vare den tunna degen, som '
                    'minskar andelen stärkelse till förmån för köttets protein; den blir en utmärkt måltid när du äter 2–3 '
                    'stycken med grönsaker.')),
    200: dict(lead="Levantens morgondoft: ett bakat bröd täckt med malen vild timjan (za'atar), sesamfrön och extra "
                   'jungfruolivolja. Olivoljans enkelomättade fett bromsar nedbrytningen av vetedegen och ger manakish med '
                   "za'atar ett lågt glykemiskt index (55).",
              tips=('Ät en halv manakish eller en liten tillsammans med tomat- och gurkskivor och oliver, och drick '
                    'salvia- eller myntate utan socker för en balanserad morgon.',
                    "Använd en äkta za'atarblandning med mycket sesam och riktig vild timjan utan tillsatt rostat mjöl, "
                    'och välj kallpressad extra jungfruolivolja.',
                    'Den rikliga oljan och degen gör brödet kalorität, så att hålla brödet litet är nyckeln för dig som '
                    'vill hålla vikten.')),
}
