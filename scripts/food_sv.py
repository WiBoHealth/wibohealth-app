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
# foods allowed to use the computed Swedish copy where the other languages carry food-specific copy (none since
# foods 1-50 got their translated copy, 2026-10-24)
COMPUTED_COPY = set()

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
}
