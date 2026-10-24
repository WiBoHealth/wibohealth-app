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

# foods with a Swedish page: 1-600 (1-50 samples approved 2026-10-24); set below NAMES

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
    201: ('Manakish med akkawiost', 'manakish med ost'),
    202: ('Sambousek med köttfärs', 'sambousek med köttfärs'),
    203: ('Clubsandwich med kalkon och ost', 'clubsandwich'),
    204: ('Tonfisksmörgås med majonnäs och sallad', 'tonfisksmörgås'),
    205: ('Panini med grillad halloumi och tomat', 'halloumipanini'),
    206: ('Avokadotoast med kokt ägg', 'avokadotoast med ägg'),
    207: ('Grönsakssoppa', 'grönsakssoppa'),
    208: ('Kycklingsoppa med vermicelli', 'kycklingsoppa med vermicelli'),
    209: ('Pumpasoppa, krämig', 'krämig pumpasoppa'),
    210: ('Broccolisoppa, krämig', 'krämig broccolisoppa'),
    211: ('Svampsoppa, krämig', 'krämig svampsoppa'),
    212: ('Tomatsoppa på rostade tomater', 'tomatsoppa'),
    213: ('Freekehsoppa med kött', 'freekehsoppa'),
    214: ('Moussaka med aubergine och köttfärs', 'moussaka'),
    215: ('Okragryta med kött och ris', 'okragryta'),
    216: ('Gryta med gröna bönor och kött', 'grönbönsgryta'),
    217: ('Mfarakah, potatis med ägg', 'mfarakah'),
    218: ('Ris med vermicelli och ghee', 'ris med vermicelli'),
    219: ('Pastagratäng med köttfärs och béchamel', 'pastagratäng'),
    220: ('Dawood basha, köttbullar i tomatsås', 'dawood basha'),
    221: ('Caesarsallad med grillad kyckling', 'caesarsallad med kyckling'),
    222: ('Grekisk sallad med fetaost och oliver', 'grekisk sallad'),
    223: ('Quinoasallad med avokado och grönsaker', 'quinoasallad'),
    224: ('Ruccolasallad med granatäpple och valnötter', 'ruccolasallad'),
    225: ('Potatissallad med persilja', 'potatissallad'),
    226: ('Rödbetssallad med citron', 'rödbetssallad'),
    227: ('Tonfisksallad med majs och majonnäs', 'tonfisksallad med majs'),
    228: ('Drakfrukt (pitaya)', 'drakfrukt'),
    229: ('Passionsfrukt', 'passionsfrukt'),
    230: ('Litchi', 'litchi'),
    231: ('Kaktusfikon', 'kaktusfikon'),
    232: ('Aprikoser, torkade', 'torkade aprikoser'),
    233: ('Fikon, torkade', 'torkade fikon'),
    234: ('Katrinplommon', 'katrinplommon'),
    235: ('Gojibär, torkade', 'torkade gojibär'),
    236: ('Gurkmeja, färsk, riven', 'färsk gurkmeja'),
    237: ('Ingefära, färsk', 'färsk ingefära'),
    238: ('Kanel, ceylon', 'ceylonkanel'),
    239: ('Kardemumma, gröna kapslar', 'grön kardemumma'),
    240: ('Saffran', 'saffran'),
    241: ('Vild timjan, torkad (oregano)', 'torkad vild timjan'),
    242: ('Spirulina, pulver', 'spirulinapulver'),
    243: ('Vassleprotein, isolat', 'vassleproteinisolat'),
    244: ('Mandelmjöl, glutenfritt', 'mandelmjöl'),
    245: ('Kokosmjöl', 'kokosmjöl'),
    246: ('Tamarinddryck', 'tamarinddryck'),
    247: ('Johannesbrödsdryck', 'johannesbrödsdryck'),
    248: ('Sahlab med kanel och nötter', 'sahlab'),
    249: ('Arabiskt kaffe med kardemumma', 'arabiskt kaffe'),
    250: ('Karakte med mjölk och kryddor', 'karakte'),
    251: ('Rambutan', 'rambutan'),
    252: ('Kumquat', 'kumquat'),
    253: ('Durian', 'durian'),
    254: ('Stjärnfrukt (carambola)', 'stjärnfrukt'),
    255: ('Jackfrukt', 'jackfrukt'),
    256: ('Mangostan', 'mangostan'),
    257: ('Persimon (kaki)', 'persimon'),
    258: ('Japansk mispel (loquat)', 'japansk mispel'),
    259: ('Kiwano (hornmelon)', 'kiwano'),
    260: ('Acaibär', 'acaibär'),
    261: ('Kålrabbi', 'kålrabbi'),
    262: ('Purjolök', 'purjolök'),
    263: ('Rödkål', 'rödkål'),
    264: ('Rädisor', 'rädisor'),
    265: ('Malva (khubeza), kokt i olivolja', 'malva'),
    266: ('Blomkål, friterad med spiskummin', 'friterad blomkål'),
    267: ('Kryddnejlika, hel', 'kryddnejlika'),
    268: ('Muskotnöt, riven', 'riven muskotnöt'),
    269: ('Rosmarin, torkad', 'torkad rosmarin'),
    270: ('Basilika, torkad', 'torkad basilika'),
    271: ('Svartkummin (nigellafrön)', 'svartkummin'),
    272: ('Sumak', 'sumak'),
    273: ('Tilapia, grillad', 'grillad tilapia'),
    274: ('Zackenabborre (grouper)', 'zackenabborre'),
    275: ('Bläckfisk (octopus), grillad', 'grillad bläckfisk'),
    276: ('Calamares, friterade', 'friterade calamares'),
    277: ('Kaviar, svart', 'svart kaviar'),
    278: ('Sardeller, saltade', 'saltade sardeller'),
    279: ('Lever i Alexandriastil, kryddstark', 'kryddstark lever'),
    280: ('Fatteh med makdous, kött och yoghurt', 'makdous-fatteh'),
    281: ('Shakriyyeh, lammkött i yoghurtsås', 'shakriyyeh'),
    282: ('Jareesh, saudisk vetegröt', 'jareesh'),
    283: ('Areeka med dadlar, honung och ghee', 'areeka'),
    284: ('Näringsjäst, berikad', 'näringsjäst'),
    285: ('Äppelcidervinäger, ofiltrerad', 'äppelcidervinäger'),
    286: ('Proteinbar med choklad och kola', 'proteinbar'),
    287: ('Ketobröd, glutenfritt', 'glutenfritt ketobröd'),
    288: ('Glutenfri pasta (ris och majs)', 'glutenfri pasta'),
    289: ('Granatäpplesirap, utan tillsatt socker', 'granatäpplesirap'),
    290: ('Sojasås, naturligt bryggd', 'naturligt bryggd sojasås'),
    291: ('Srirachasås', 'srirachasås'),
    292: ('Gurka, inlagd', 'inlagd gurka'),
    293: ('Kalamataoliver', 'kalamataoliver'),
    294: ('Öl, vanlig (pilsner)', 'vanlig öl'),
    295: ('Rödvin, torrt', 'torrt rödvin'),
    296: ('Lakritsrotsdryck', 'lakritsrotsdryck'),
    297: ('Hibiskuste, kallt', 'kallt hibiskuste'),
    298: ('Kamomillte', 'kamomillte'),
    299: ('Turkiskt kaffe med kardemumma', 'turkiskt kaffe'),
    300: ('Marockanskt grönt te med mynta', 'marockanskt myntate'),
    301: ('Grönkål', 'grönkål'),
    302: ('Brysselkål', 'brysselkål'),
    303: ('Kärnmjölk', 'kärnmjölk'),
    304: ('Kvarg, fettfri', 'fettfri kvarg'),
    305: ('Kvarg, fullfet', 'fullfet kvarg'),
    306: ('Rågbröd, holländskt grovt', 'holländskt rågbröd'),
    307: ('Holländsk sill (Hollandse nieuwe) med lök', 'holländsk sill'),
    308: ('Ärtsoppa, holländsk (snert)', 'holländsk ärtsoppa'),
    309: ('Stamppot med grönkål och potatis', 'grönkålsstamppot'),
    310: ('Hutspot, mos av morot, lök och potatis', 'hutspot'),
    311: ('Ål, rökt', 'rökt ål'),
    312: ('Kibbeling, friterad torsk', 'kibbeling'),
    313: ('Stroopwafel (sirapsvåffla)', 'stroopwafel'),
    314: ('Poffertjes, små pannkakor', 'poffertjes'),
    315: ('Speculaaskex', 'speculaaskex'),
    316: ('Kruidnoten, holländska pepparnötter', 'kruidnoten'),
    317: ('Bitterballen, köttkroketter', 'bitterballen'),
    318: ('Krokett med nötkött', 'krokett'),
    319: ('Frikandel, korv av köttfärs', 'frikandel'),
    320: ('Ossenworst, rå nötkorv', 'ossenworst'),
    321: ('Filet americain, rå nötfärsröra', 'filet americain'),
    322: ('Edamerost', 'edamerost'),
    323: ('Gouda, lagrad', 'lagrad gouda'),
    324: ('Leidenost med spiskummin', 'leidenost'),
    325: ('Getost, mjuk holländsk', 'mjuk getost'),
    326: ('Vla, holländsk vaniljkräm', 'vla'),
    327: ('Chokladmjölk, holländsk', 'chokladmjölk'),
    328: ('Äppelsirap, holländsk (appelstroop)', 'äppelsirap'),
    329: ('Skorpor av fullkornsvete (beschuit)', 'fullkornsskorpor'),
    330: ('Ontbijtkoek, holländsk kryddkaka', 'ontbijtkoek'),
    331: ('Chokladströssel, mörkt (hagelslag)', 'chokladströssel'),
    332: ('Parmigiano Reggiano, lagrad 24 månader', 'parmesan'),
    333: ('Pecorino Romano', 'pecorino'),
    334: ('Fetaost av fårmjölk, grekisk', 'fetaost'),
    335: ('Brieost', 'brie'),
    336: ('Camembert', 'camembert'),
    337: ('Ricotta, färsk', 'ricotta'),
    338: ('Mascarpone', 'mascarpone'),
    339: ('Gruyère', 'gruyère'),
    340: ('Emmentaler', 'emmentaler'),
    341: ('Roquefort', 'roquefort'),
    342: ('Manchego', 'manchego'),
    343: ('Skyr, naturell', 'naturell skyr'),
    344: ('Surdegsbröd', 'surdegsbröd'),
    345: ('Pumpernickel', 'pumpernickel'),
    346: ('Focaccia med olivolja och rosmarin', 'focaccia'),
    347: ('Tigerbröd, holländskt', 'tigerbröd'),
    348: ('Briochebröd', 'briochebröd'),
    349: ('Bagel med sesam', 'sesambagel'),
    350: ('Bovetegryn, kokta', 'kokta bovetegryn'),
    351: ('Bovetemjöl', 'bovetemjöl'),
    352: ('Speltkärnor, kokta', 'kokta speltkärnor'),
    353: ('Speltmjöl, fullkorn', 'fullkornsspeltmjöl'),
    354: ('Kikärtsmjöl (besan)', 'kikärtsmjöl'),
    355: ('Polenta, kokt', 'kokt polenta'),
    356: ('Cornflakes, osötade', 'osötade cornflakes'),
    357: ('Müsli utan tillsatt socker', 'müsli'),
    358: ('Granola med nötter och honung', 'granola'),
    359: ('Selleri, stjälkar', 'stjälkselleri'),
    360: ('Rotselleri, kokt', 'kokt rotselleri'),
    361: ('Fänkål, färsk', 'färsk fänkål'),
    362: ('Vit sparris, kokt', 'kokt vit sparris'),
    363: ('Endiv (witlof)', 'endiv'),
    364: ('Frisésallat', 'frisésallat'),
    365: ('Isbergssallat', 'isbergssallat'),
    366: ('Romansallat', 'romansallat'),
    367: ('Mangold', 'mangold'),
    368: ('Pak choi', 'pak choi'),
    369: ('Salladslök', 'salladslök'),
    370: ('Schalottenlök', 'schalottenlök'),
    371: ('Majrova, kokt', 'kokt majrova'),
    372: ('Rättika (daikon)', 'rättika'),
    373: ('Gröna ärter, kokta', 'kokta gröna ärter'),
    374: ('Haricots verts', 'haricots verts'),
    375: ('Paprika, röd', 'röd paprika'),
    376: ('Paprika, gul', 'gul paprika'),
    377: ('Jalapeño', 'jalapeño'),
    378: ('Chilipeppar, röd, färsk', 'röd chili'),
    379: ('Butternutpumpa', 'butternutpumpa'),
    380: ('Rabarber, färsk', 'färsk rabarber'),
    381: ('Björnbär, färska', 'färska björnbär'),
    382: ('Röda vinbär', 'röda vinbär'),
    383: ('Svarta vinbär', 'svarta vinbär'),
    384: ('Tranbär, färska', 'färska tranbär'),
    385: ('Krusbär', 'krusbär'),
    386: ('Surkörsbär (morell)', 'surkörsbär'),
    387: ('Nektarin', 'nektarin'),
    388: ('Aprikos, färsk', 'färsk aprikos'),
    389: ('Platt persika (donutpersika)', 'platt persika'),
    390: ('Grapefrukt, rosa', 'rosa grapefrukt'),
    391: ('Pomelo', 'pomelo'),
    392: ('Klementin', 'klementin'),
    393: ('Citron, gul (pressad)', 'citron'),
    394: ('Lime', 'lime'),
    395: ('Guava, rosa', 'rosa guava'),
    396: ('Papaya, mogen', 'mogen papaya'),
    397: ('Pekannötter', 'pekannötter'),
    398: ('Macadamianötter', 'macadamianötter'),
    399: ('Paranötter', 'paranötter'),
    400: ('Hampafrön, skalade', 'skalade hampafrön'),
    401: ('Äkta tunga, grillad', 'grillad tunga'),
    402: ('Piggvar, filé', 'piggvarsfilé'),
    403: ('Guldsparid (dorade), grillad', 'grillad dorade'),
    404: ('Havsabborre, grillad', 'grillad havsabborre'),
    405: ('Regnbåge', 'regnbåge'),
    406: ('Hälleflundra, ångkokt', 'ångkokt hälleflundra'),
    407: ('Kummel, filé', 'kummelfilé'),
    408: ('Sej', 'sej'),
    409: ('Krabbkött, kokt', 'kokt krabbkött'),
    410: ('Hummer, grillad', 'grillad hummer'),
    411: ('Ostron, råa', 'råa ostron'),
    412: ('Blåmusslor, ångkokta', 'ångkokta blåmusslor'),
    413: ('Pilgrimsmusslor, stekta', 'stekta pilgrimsmusslor'),
    414: ('Kalkonbröst, rökt, skivat', 'rökt kalkonbröst'),
    415: ('Kalvstek, mager', 'mager kalvstek'),
    416: ('Ankbröst utan skinn', 'ankbröst utan skinn'),
    417: ('Kaninkött, kokt', 'kaninkött'),
    418: ('Bresaola (lufttorkat nötkött)', 'bresaola'),
    419: ('Pastrami av nötkött', 'pastrami'),
    420: ('Rostbiff, skivad', 'rostbiff'),
    421: ('Kycklingkorv, grillad', 'grillad kycklingkorv'),
    422: ('Kalkonfärs, mager (97/3)', 'mager kalkonfärs'),
    423: ('Kycklinglever, stekt med lök', 'stekt kycklinglever'),
    424: ('Kycklingkrås, kokt', 'kokt kycklingkrås'),
    425: ('Belugalinser, svarta', 'svarta belugalinser'),
    426: ('Röda linser, krossade', 'röda linser'),
    427: ('Mungbönor, kokta', 'kokta mungbönor'),
    428: ('Svarta bönor', 'svarta bönor'),
    429: ('Cannellinibönor', 'cannellinibönor'),
    430: ('Borlottibönor', 'borlottibönor'),
    431: ('Bondbönor, skalade och kokta', 'skalade bondbönor'),
    432: ('Gula ärter, krossade, kokta', 'kokta gula ärter'),
    433: ('Majs, konserverad, utan tillsatt socker', 'konserverad majs'),
    434: ('Kronärtskockshjärtan i lake', 'kronärtskockshjärtan'),
    435: ('Champinjoner, konserverade, skivade', 'konserverade champinjoner'),
    436: ('Palmhjärtan, konserverade', 'palmhjärtan'),
    437: ('Bambuskott i vatten', 'bambuskott'),
    438: ('Vattenkastanjer, konserverade', 'vattenkastanjer'),
    439: ('Skalade plommontomater, konserverade', 'skalade tomater'),
    440: ('Passerade tomater (passata)', 'passata'),
    441: ('Surkål, naturligt fermenterad', 'surkål'),
    442: ('Böngroddar, färska', 'böngroddar'),
    443: ('Kapris i lake', 'kapris'),
    444: ('Paella med skaldjur', 'paella'),
    445: ('Spansk tortilla (potatisomelett)', 'spansk tortilla'),
    446: ('Gazpacho', 'gazpacho'),
    447: ('Salmorejo, kall tomatsoppa', 'salmorejo'),
    448: ('Padrónpaprikor i olivolja', 'padrónpaprikor'),
    449: ('Patatas bravas med stark sås', 'patatas bravas'),
    450: ('Bläckfisk al ajillo med vitlök', 'bläckfisk al ajillo'),
    451: ('Grönsakskroketter, spanska', 'grönsakskroketter'),
    452: ('Pastel de nata (portugisisk vaniljtartelett)', 'pastel de nata'),
    453: ('Pan con tomate (bröd med tomat)', 'pan con tomate'),
    454: ('Fransk löksoppa med ost', 'fransk löksoppa'),
    455: ('Ratatouille', 'ratatouille'),
    456: ('Quiche med grönsaker och ost', 'quiche'),
    457: ('Coq au vin (kycklinggryta med svamp)', 'coq au vin'),
    458: ('Bœuf bourguignon (köttgryta med morötter)', 'bœuf bourguignon'),
    459: ('Salade niçoise med tonfisk och ägg', 'salade niçoise'),
    460: ('Gratin dauphinois (potatisgratäng)', 'potatisgratäng'),
    461: ('Ostsufflé', 'ostsufflé'),
    462: ('Bovetegalett med ost och ägg', 'bovetegalett'),
    463: ('Tarte tatin (karamelliserad äppelpaj)', 'tarte tatin'),
    464: ('Wienerschnitzel av kalv', 'wienerschnitzel'),
    465: ('Spätzle (tyska äggnudlar)', 'spätzle'),
    466: ('Tysk potatissallad med vinäger och senap', 'tysk potatissallad'),
    467: ('Tysk linsgryta med grönsaker', 'tysk linsgryta'),
    468: ('Bayersk pretzel, saltad', 'pretzel'),
    469: ('Äppelstrudel, wienerstil', 'äppelstrudel'),
    470: ('Kaiserschmarrn med äppelmos', 'kaiserschmarrn'),
    471: ('Gyros med kyckling i pitabröd', 'kycklinggyros'),
    472: ('Souvlaki, grillspett', 'souvlaki'),
    473: ('Tzatziki', 'tzatziki'),
    474: ('Spanakopita (spenat- och fetapaj)', 'spanakopita'),
    475: ('Tiropita (ostpaj i filodeg)', 'tiropita'),
    476: ('Briam (ugnsrostade grönsaker)', 'briam'),
    477: ('Fasolada (grekisk bönsoppa)', 'fasolada'),
    478: ('Gemista (fyllda grönsaker med ris)', 'gemista'),
    479: ('Lammfötter, kokta (kawareh)', 'lammfötter'),
    480: ('Kalvtunga med vitlök och citron', 'kalvtunga'),
    481: ('Lammhjärna med olivolja och citron', 'lammhjärna'),
    482: ('Sitti zbaqi (linsgryta med mangold)', 'sitti zbaqi'),
    483: ('Haraq osbao (linsgryta med tamarind)', 'haraq osbao'),
    484: ('Kibbeh i form (kibbeh bil saniyeh)', 'kibbeh i form'),
    485: ('Kibbeh labanieh (kibbeh i yoghurtsås)', 'kibbeh labanieh'),
    486: ('Kibbeh från Aleppo, grillad på spett', 'grillad kibbeh'),
    487: ('Kibbeh safarjalieh med kvitten och granatäpple', 'kibbeh safarjalieh'),
    488: ('Yabraq (vinbladsrullar med lammkött)', 'yabraq'),
    489: ('Sheikh al-mahshi (zucchini i yoghurtsås)', 'sheikh al-mahshi'),
    490: ('Manzaleh med aubergine och köttfärs', 'manzaleh'),
    491: ('Halabessa (varm kryddad kikärtsdryck)', 'halabessa'),
    492: ('Bissara med mynta och spiskummin', 'bissara'),
    493: ('Mutabbaq, jemenitisk köttfärspaj', 'mutabbaq'),
    494: ('Tamees, tunnbröd med sesam', 'tamees'),
    495: ('Balila (varma kryddade kikärter)', 'balila'),
    496: ('Moutabal på rostad pumpa', 'pumpamoutabal'),
    497: ('Grillad halloumi med vattenmelon och mynta', 'grillad halloumi med vattenmelon'),
    498: ('Shanklishsallad med tomat och lök', 'shanklishsallad'),
    499: ('Pomeransmarmelad (bitter apelsinmarmelad)', 'pomeransmarmelad'),
    500: ('Johannesbrödsirap, naturlig', 'johannesbrödsirap'),
    501: ('Shish kebab av lamm, grillad', 'lammshishkebab'),
    502: ('Iskender kebab med tomatsås och yoghurt', 'iskender kebab'),
    503: ('Adana kebab, stark', 'adana kebab'),
    504: ('Manti med vitlöksyoghurt', 'manti'),
    505: ('Pide med ost och ägg', 'pide'),
    506: ('Börek med spenat och fetaost', 'spenatbörek'),
    507: ('İmam bayıldı (fylld aubergine i olivolja)', 'imam bayıldı'),
    508: ('Izgara köfte (grillade köttbullar)', 'izgara köfte'),
    509: ('Yaylasoppa med yoghurt, mynta och ris', 'yaylasoppa'),
    510: ('Çiğ köfte, vegansk (bulgurbiffar)', 'vegansk çiğ köfte'),
    511: ('Lokum med pistage', 'lokum'),
    512: ('Turkiskt äppelte med kanel', 'turkiskt äppelte'),
    513: ('Lammtagine med katrinplommon och mandel', 'lammtagine'),
    514: ('Fisktagine med chermoula', 'fisktagine'),
    515: ('Kycklingtagine med saltad citron och oliver', 'kycklingtagine'),
    516: ('Pastilla med kyckling och mandel', 'kycklingpastilla'),
    517: ('Pastilla med skaldjur och glasnudlar', 'skaldjurspastilla'),
    518: ('Harira (marockansk soppa)', 'harira'),
    519: ('Couscous med sju grönsaker och nötkött', 'couscous med sju grönsaker'),
    520: ('Zaalouk (aubergineröra)', 'zaalouk'),
    521: ('Taktouka (paprika- och tomatsallad)', 'taktouka'),
    522: ('Batbout (marockanskt stekpannebröd)', 'batbout'),
    523: ('Baghrir (marockanska mannagrynspannkakor)', 'baghrir'),
    524: ('Harcha (marockanskt mannagrynsbröd)', 'harcha'),
    525: ('Chebakia med honung och sesam', 'chebakia'),
    526: ('Sellou (rostat mjöl med mandel och sesam)', 'sellou'),
    527: ('Saltade citroner, marockanska', 'saltade citroner'),
    528: ('Harissa (tunisisk chilipasta)', 'harissa'),
    529: ('Kolhapurikyckling (stark curry med kokos)', 'kolhapurikyckling'),
    530: ('Rogan josh (lammcurry från Kashmir)', 'rogan josh'),
    531: ('Kycklingkorma med cashewkräm', 'kycklingkorma'),
    532: ('Vindaloo (stark curry från Goa)', 'vindaloo'),
    533: ('Dal makhani (krämiga svarta linser)', 'dal makhani'),
    534: ('Chana masala (kryddig kikärtscurry)', 'chana masala'),
    535: ('Aloo gobi (potatis och blomkål)', 'aloo gobi'),
    536: ('Bhindi masala (stekt okra)', 'bhindi masala'),
    537: ('Äggcurry, indisk', 'äggcurry'),
    538: ('Samosa med grönsaker', 'grönsakssamosa'),
    539: ('Roti av fullkornsvete (chapati utan olja)', 'fullkornsroti'),
    540: ('Paratha, stekt i ghee', 'paratha'),
    541: ('Mangolassi med kardemumma', 'mangolassi'),
    542: ('Masala chai med mjölk', 'masala chai'),
    543: ('Gulab jamun i sockerlag', 'gulab jamun'),
    544: ('Kheer (indisk risgrynspudding)', 'kheer'),
    545: ('Pho med nötkött', 'pho'),
    546: ('Vietnamesiska vårrullar med räkor, färska', 'vietnamesiska vårrullar'),
    547: ('Tom yum goong (stark räksoppa)', 'tom yum goong'),
    548: ('Grön thaicurry med kokosmjölk', 'grön thaicurry'),
    549: ('Röd thaicurry med bambuskott', 'röd thaicurry'),
    550: ('Som tam (grön papayasallad)', 'som tam'),
    551: ('Mango sticky rice med kokosgrädde', 'mango sticky rice'),
    552: ('Kung pao-kyckling med jordnötter och chili', 'kung pao-kyckling'),
    553: ('Pekinganka med hoisinsås', 'pekinganka'),
    554: ('Wokat nötkött med broccoli i ostronsås', 'wokat nötkött med broccoli'),
    555: ('Mapo tofu med nötfärs och szechuanpeppar', 'mapo tofu'),
    556: ('Teägg, kinesiska, med fem kryddor', 'kinesiska teägg'),
    557: ('Glasnudlar av mungbönsstärkelse, kokta', 'kokta glasnudlar'),
    558: ('Sobanudlar av 100 % bovete', 'sobanudlar'),
    559: ('Udonnudlar, kokta', 'kokta udonnudlar'),
    560: ('Bibimbap med ägg, nötkött och grönsaker', 'bibimbap'),
    561: ('Bulgogi (koreanskt marinerat nötkött)', 'bulgogi'),
    562: ('Gyoza med kyckling, stekta', 'kycklinggyoza'),
    563: ('Wakame, torkad och blötlagd', 'wakame'),
    564: ('Norirak, rostade', 'norirak'),
    565: ('Shiitakesvamp, tillagad', 'tillagad shiitake'),
    566: ('Enokisvamp, färsk', 'enokisvamp'),
    567: ('Bipollen, obehandlat', 'bipollen'),
    568: ('Manukahonung (med angiven MGO-halt)', 'manukahonung'),
    569: ('Vetegräspulver, ekologiskt', 'vetegräspulver'),
    570: ('Macapulver (peruansk macarot)', 'macapulver'),
    571: ('Baobabpulver, ekologiskt', 'baobabpulver'),
    572: ('Kakaopulver, rått, osötat', 'rått kakaopulver'),
    573: ('Kakaosmör, kallpressat', 'kakaosmör'),
    574: ('Kakaonibs, råa', 'kakaonibs'),
    575: ('Linfrö, nymalda', 'nymalda linfrön'),
    576: ('Solrosfrösmör, naturellt', 'solrosfrösmör'),
    577: ('Pumpafrösmör, rått', 'pumpafrösmör'),
    578: ('Linfröolja, kallpressad', 'linfröolja'),
    579: ('Svartkumminolja, kallpressad', 'svartkumminolja'),
    580: ('Levertran, norsk', 'levertran'),
    581: ('Hjortron', 'hjortron'),
    582: ('Havtornsbär', 'havtornsbär'),
    583: ('Fläderbär, kokta', 'kokta fläderbär'),
    584: ('Kvitten, pocherat med kanel', 'pocherat kvitten'),
    585: ('Aprikoser, soltorkade, osvavlade', 'soltorkade aprikoser'),
    586: ('Svarta mullbär, färska', 'svarta mullbär'),
    587: ('Vita mullbär, torkade', 'torkade vita mullbär'),
    588: ('Sötkastanjer, rostade', 'rostade kastanjer'),
    589: ('Pinjenötter', 'pinjenötter'),
    590: ('Svarta sesamfrön', 'svarta sesamfrön'),
    591: ('Kombucha, opastöriserad', 'kombucha'),
    592: ('Vattenkefir med fikon och citron', 'vattenkefir'),
    593: ('Rooiboste', 'rooiboste'),
    594: ('Grönt te med jasmin', 'jasminte'),
    595: ('Earl Grey-te med bergamott', 'Earl Grey-te'),
    596: ('Oolongte', 'oolongte'),
    597: ('Rostad maskrosrot (kaffeersättning)', 'rostad maskrosrot'),
    598: ('Gurkmejamjölk med svartpeppar och ingefära', 'gurkmejamjölk'),
    599: ('Vatten med gurka, citron och mynta', 'gurkvatten med mynta'),
    600: ('Apelsinblomsvatten, destillerat', 'apelsinblomsvatten'),
}
PUBLISH = set(NAMES)
# foods allowed to use the computed Swedish copy where the other languages carry food-specific copy (none since
# foods 1-50 got their translated copy, 2026-10-24)
COMPUTED_COPY = set()

# names that take a plural pronoun in the sentences ({det}/{dem}: "de"/"dem" instead of "det")
PLURAL = {18, 19, 20, 21, 22, 23, 24, 25, 28, 40,
          52, 53, 56, 57, 58, 60, 61, 62, 63, 68, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 99, 100,
          117, 142, 161, 162, 171, 183, 184, 197, 198,
          232, 233, 234, 235, 260, 264, 276, 278, 293,
          314, 316, 317, 329, 350, 352, 356, 373, 374, 381, 382, 383, 384, 385, 386, 397, 398, 399, 400,
          411, 412, 413, 425, 426, 427, 428, 429, 430, 431, 432, 434, 435, 436, 437, 438, 439, 442, 448, 449, 451, 465, 479,
          504, 508, 523, 527, 543, 546, 556, 557, 558, 559, 564, 574, 575, 581, 582, 583, 585, 586, 587, 588, 589, 590}

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
    # foods 201-300: translated from the approved Arabic copy (2026-10-24, four checked blocks of 25)
    201: dict(lead='Smält, trådig ost på ett varmt bröd direkt från ugnen: en frukost som både barn och vuxna älskar. '
                   'Akkawiostens fett och protein bromsar upptaget av degens stärkelse, med ett lågt glykemiskt index '
                   '(55), och den mättar i många timmar, men tänk på att osten är salt.',
              tips=("Be om en delad manakish (hälften za'atar, hälften ost), så får du både olivolja och mättande ost med "
                    'hälften så mycket mättat fett, och ät alltid färska grönsaker till.',
                    'Vattna gärna ur akkawiosten ordentligt genom att lägga den i blöt och byta vatten, så minskar '
                    'salthalten, och lägg inte på för mycket ost.',
                    'En hel manakish med ost kan innehålla mycket salt och mättat fett, så om du behöver hålla koll på '
                    'salt eller blodfetter räcker det med ett halvt bröd.')),
    202: dict(lead='Den gyllene, krispiga halvmånen som ofta står på festbordet, fylld med nötfärs, lök och rostade '
                   'pinjenötter. Köttets protein bromsar matsmältningen, men den tunna, friterade degen höjer kalorierna '
                   'och den glykemiska belastningen (GI 58, medelhögt), så ät den med eftertanke.',
              tips=('Ät en eller två som en trevlig del av måltiden, inte som huvudrätt, och börja alltid med soppa eller '
                    'sallad så att magen först fylls med fibrer.',
                    'Det smartaste alternativet: grädda sambousek i ugnen eller i airfryer efter att ha penslat dem med '
                    'några droppar olivolja; du får samma krispighet med en fjärdedel så mycket uppsuget fett.',
                    'Fritering i mycket olja på hög värme gör maten tung att smälta, så ugnsbakning hemma är det bättre '
                    'valet för dig som håller koll på vikten och blodsockret.')),
    203: dict(lead='Den klassiska smörgåsen i flera lager: rostat formbröd med kalkonbröst, naturlig ost, sallad och '
                   'tomat. Kalkonens magra protein och osten bromsar formbrödets glykemiska effekt (GI 55) och ger en god '
                   'mättnad.',
              tips=('Ät clubsandwichen med en grön sallad och hoppa över den vanliga portionen pommes frites, så slipper '
                    'du dubbelt med stärkelse och härdat fett.',
                    'Välj formbröd av fullkorn för mer fibrer, och byt ut den tjocka majonnäsen mot lite senap eller mosad '
                    'färsk avokado.',
                    'Välj naturligt, grillat kalkonbröst och undvik charkuterier med mycket nitrit och salt.')),
    204: dict(lead='Den snabba och populära lunchen för dig som vill ha ett enkelt och mättande protein från havet. '
                   'Tonfisk är helt fri från stärkelse och innehåller fullvärdigt protein och omega-3; tillsammans med '
                   'formbrödet bryts kolhydraterna ned långsammare, med ett lågt glykemiskt index (52).',
              tips=('En mycket mättande smörgås som passar långa arbetsdagar; ät den med selleri- eller morotsstavar för '
                    'extra fräschör.',
                    'Använd avrunnen tonfisk i vatten eller olivolja, och byt ut hälften av majonnäsen mot grekisk yoghurt '
                    'med citron, svartpeppar och finhackad selleri för krispighet och mer protein.',
                    'Välj gärna ljus tonfisk (light tuna) och ät den med måtta, två till tre gånger i veckan, för att '
                    'begränsa intaget av kvicksilver; detta bör särskilt gravida tänka på.')),
    205: dict(lead='Italienskt paninibröd rostat på grillen med varma skivor halloumi, tomatskivor och mynta eller timjan. '
                   'Den grillade halloumins protein och fett gör att smörgåsen smälts långsamt, med ett lågt glykemiskt '
                   'index (42).',
              tips=('Ett utmärkt lunchval som mättar direkt; ät en halv smörgås med en ruccolasallad med olivolja och '
                    'citron för att balansera halloumins naturliga salthalt.',
                    'Grilla halloumiskivorna på en torr grill utan olja, eftersom osten släpper sitt eget fett, och lägg '
                    'till grillade tomatskivor med lite oregano för en doftande medelhavssmak.',
                    'Halloumi innehåller naturligt mycket salt, kalcium och mättat fett; att lägga skivorna i ljummet '
                    'vatten några minuter före grillningen minskar saltet.')),
    206: dict(lead='Den moderna frukostfavoriten som förenar smart näring och njutning: en skiva rostat fullkornsbröd med '
                   'mosad avokado och ett färskt kokt ägg. Kombinationen ger ett lågt glykemiskt index (40), eftersom det '
                   'omättade fettet, proteinet och fibrerna dämpar blodsockerstegringen.',
              tips=('En perfekt start på morgonen som håller dig mätt till lunch; drick en kopp grönt te eller svart kaffe '
                    'till.',
                    'Mosa en halv avokado med gaffel tillsammans med citronsaft, lite salt och krossad chili, och lägg det '
                    'kokta eller pocherade ägget med krämig gula ovanpå brödet.',
                    'En balanserad kombination som mättar väl och passar vid diabetes och insulinresistens samt för dig '
                    'som vill gå ner i vikt.')),
    207: dict(lead='Den traditionella, värmande soppan som lagas när det börjar bli kallt: en färgglad blandning av '
                   'zucchini, morot, gröna bönor och selleri i en mild buljong. Den vanliga frågan är om grönsakssoppa '
                   'höjer blodsockret. Det glykemiska indexet är lågt (30) tack vare den höga halten fibrer och vatten, '
                   'vilket gör soppan till ett utmärkt sätt att inleda måltiden och få en lugn mättnad.',
              tips=('Börja lunchen eller middagen med en stor skål grönsakssoppa; den varma soppan fyller en stor del av '
                    'magen, så att du lättare tar en mindre portion av stärkelserätterna som följer.',
                    'Koka grönsakerna tills de är mjuka men har lite tuggmotstånd kvar och undvik att mixa allt; hela '
                    'grönsaksbitar smälts långsammare och fibrernas struktur bevaras.',
                    'Undvik färdiga buljongtärningar med mycket salt och glutamat, och använd hemlagad kyckling- eller '
                    'köttbuljong kryddad med gurkmeja och svartpeppar för en ren smak.')),
    208: dict(lead='Den klassiska soppan som alltid förknippas med värme: kycklingbuljong med strimlad kyckling och '
                   'gyllene vermicelli. Många undrar om vermicellin i soppan höjer blodsockret; kycklingens protein och '
                   'buljongens fett bromsar nedbrytningen av stärkelsen, så att soppan får ett lågt glykemiskt index (35).',
              tips=('Låt kyckling och grönsaker som morot och persilja dominera i skålen och håll vermicellin till en '
                    'liten mängd, så får buljongen en god konsistens utan för mycket raffinerad stärkelse.',
                    'Rosta vermicellin lätt i en torr kastrull med non-stick-beläggning innan du häller på buljongen; det '
                    'förbättrar smaken och gör att den inte suger upp buljongen lika snabbt och blir mjuk.',
                    'Pressa över rikligt med färsk citron och strö över hackad persilja precis innan du äter; citronens '
                    'syra kan bromsa upptaget av kolhydraterna.')),
    209: dict(lead='Den sammetslena höstsoppan med sin vackra orange färg och varma, söta smak. Den vanligaste frågan är '
                   'om pumpans söta smak höjer blodsockret snabbt. Pumpa innehåller mycket vatten och har ett lågt '
                   'glykemiskt index (51), och eftersom mängden kolhydrater i en portion är måttlig förblir den glykemiska '
                   'belastningen låg.',
              tips=('Ät en medelstor skål som förrätt till lunchen och toppa med en näve rostade pumpafrön för mer zink '
                    'och fett, som bromsar matsmältningen.',
                    'Ugnsrosta pumpatärningarna med olivolja, kanel och muskotnöt innan du mixar dem med buljongen; '
                    'rostningen karamelliserar det naturliga sockret, så du behöver inte tillsätta socker eller aromer.',
                    'Byt ut den tjocka matlagningsgrädden mot lätt kokosmjölk eller naturell yoghurt för mindre mättat '
                    'fett och en sammetslen konsistens.')),
    210: dict(lead='Pärlan bland de gröna sopporna: broccolibuketter blir en len soppa som innehåller sulforafan. Broccoli '
                   'innehåller mycket lite kolhydrater och mycket fibrer, så soppan har ett lågt glykemiskt index (25) och '
                   'mättar väl.',
              tips=('Ett utmärkt val till en varm kvällsmåltid; ät den med ett kokt ägg eller en bit naturell ost, så får '
                    'du en komplett kvällsmåltid som håller hungern borta under natten.',
                    'Ångkoka broccolibuketterna i några minuter innan du mixar dem med en mild kycklingbuljong och en '
                    'krossad vitlöksklyfta, så behåller de sin smaragdgröna färg och sitt värmekänsliga C-vitamin.',
                    'Undvik att mixa i potatis för att göra soppan tjockare; mixa i stället en del av broccolin '
                    'tillsammans med den skalade stjälken för en naturligt tjock konsistens utan raffinerad stärkelse.')),
    211: dict(lead='Den klassiska restaurangrätten med sin förföriska, jordiga doft och fylliga konsistens med färsk svamp '
                   'karamelliserad med vitlök och örter. Svamp innehåller naturligt lite kolhydrater, och soppan har ett '
                   'lågt glykemiskt index (30), vilket gör den till en förrätt som påverkar insulinet lite.',
              tips=('Ät den långsamt som en varm förrätt till en proteinrik lunch och njut av svampens djupa smak, som kan '
                    'minska suget efter friterad och fet mat.',
                    'Fräs svampen med olivolja, hackad lök och oregano tills vätskan har kokat in och den fått en djupt '
                    'brun färg; det lockar fram den naturliga umamismaken, och du behöver inget vitt mjöl för att reda '
                    'soppan.',
                    'Svamp innehåller fibrer och betaglukaner; håll koll på hur mycket grädde du tillsätter, så att dagens '
                    'totala fettmängd blir balanserad.')),
    212: dict(lead='Italiensk enkelhet när den är som bäst: mogna tomater rostade i ugnen med vitlök, olivolja och färsk '
                   'basilika och mixade till en lysande röd soppa. Det glykemiska indexet är lågt (38), och tomaterna '
                   'innehåller lykopen.',
              tips=('En glad och fräsch soppa som bryter enformigheten i bantningskosten; ät den med en skiva rostat '
                    'fullkornsbröd med getost eller grillad halloumi för en balanserad kombination av fibrer och protein.',
                    'Hemligheten bakom smaken är att rosta tomaterna med vitlöksklyftorna och olivoljan med skalet på i '
                    'ugnen; värmen tillsammans med olivoljan gör att lykopenet tas upp bättre.',
                    'Mogna tomater kan behöva balanseras mot syrligheten; undvik skeden socker som restauranger ofta '
                    'använder och mixa i stället ned en liten rostad morot för en naturlig, mild sötma.')),
    213: dict(lead='Drottningen bland de traditionella levantinska sopporna: rostade och krossade gröna vetekorn som får '
                   'sjuda långsamt med köttbuljong och möra köttbitar. Freekeh innehåller mer lösliga fibrer och protein '
                   'än ris och bulgur, vilket ger soppan ett lågt glykemiskt index (42) och en mättnad som varar i timmar.',
              tips=('En komplett rätt i sig; en skål med en grön sallad och lite pressad citron blir en balanserad lunch '
                    'en vinterdag.',
                    'Skölj freekehn väl och låt den ligga i blöt en stund före kokningen, och använd magert kalvkött med '
                    'naturlig buljong och en nypa svartpeppar och spiskummin för en god, naturligt rökig smak.',
                    'Freekeh innehåller fibrer, men eftersom det är grönt vete passar det inte personer med veteallergi '
                    'eller celiaki.')),
    214: dict(lead='En klassiker på det medelhavsinspirerade och arabiska bordet: lager av aubergine som tillagats med '
                   'koncentrerad tomatsås och kryddad köttfärs. Auberginen innehåller mycket fibrer och vatten, och '
                   'samspelet mellan köttets protein och tomatsåsen ger ett lågt glykemiskt index (42) och en mycket '
                   'balanserad effekt på blodsockret.',
              tips=('Ät moussakan med gaffel som en fyllig huvudrätt tillsammans med en grön sallad eller yoghurt, och '
                    'undvik att doppa den med ett helt vitt bröd, som dubblerar de snabba kolhydraterna.',
                    'Den avgörande hemligheten ligger i auberginen: ugnsrosta skivorna med lite olivolja penslad på i '
                    'stället för att fritera dem, eftersom auberginen som en svamp suger upp stora mängder frityrolja.',
                    'Ugnsrostad aubergine mättar väl med måttligt med kalorier, och med mager köttfärs blir moussakan en '
                    'utmärkt rätt när du vill hålla vikten.')),
    215: dict(lead='Den äkta husmansrätten som miljontals människor älskar: okraskidor som kokas i en sås av tomat, vitlök '
                   'och färsk koriander tillsammans med möra köttbitar. Okra är ett utmärkt val med sina geléartade, '
                   'slemmiga fibrer (mucilage), som bromsar upptaget av kolhydraterna och ger måltiden ett lågt glykemiskt '
                   'index (35).',
              tips=('Låt okra, kött och tomatsås ta upp ungefär två tredjedelar av tallriken och nöj dig med 4–5 matskedar '
                    'ris, så njuter du av smaken med ett stabilt blodsocker.',
                    'Fräs okran snabbt med vitlök, koriander och olivolja innan du tillsätter tomatsåsen så att den håller '
                    'formen, och pressa över en färsk citron för smakens skull och eftersom C-vitamin ökar järnupptaget.',
                    'De unika lösliga fibrerna i okra bildar ett geléartat nätverk som bromsar sockerupptaget, vilket gör '
                    'den till ett bra val vid diabetes och för dig som vill vara mätt länge.')),
    216: dict(lead='En värmande husmansgryta: skurna gröna bönor som kokas i tomatsås med citronsaft och vitlök '
                   'tillsammans med lamm- eller kalvkött. Gröna bönor innehåller mycket lite kolhydrater och mycket fibrer '
                   'och vatten, vilket ger ett lågt glykemiskt index (30).',
              tips=('Ät en generös mängd bönor och kött som huvudrätt och var måttlig med riset till, så slipper du '
                    'tröttheten efter lunch.',
                    'Koka bönorna tills de är mjuka men fortfarande håller formen och färgen, och tillsätt rikligt med '
                    'vitlök och färsk koriander i slutet för en aromatisk smak utan mycket olja.',
                    'En rätt som passar dig som äter lågkolhydratkost eller har insulinresistens, eftersom den mättar väl '
                    'utan någon egentlig kolhydratbelastning.')),
    217: dict(lead='Ett älskat frukost- och kvällsmål i Levantens kvarter: potatistärningar, stekta eller kokta, blandade '
                   'med vispat ägg och kryddor som svartpeppar och spiskummin. Den eviga frågan är om potatis med ägg '
                   'höjer blodsockret; äggets protein och fett bromsar upptaget av potatisstärkelsen, vilket ger rätten '
                   'ett lågt glykemiskt index (55).',
              tips=('Ät mfarakah med gaffel tillsammans med fräscha grönsaker som tomat, gurka och mynta, och undvik att '
                    'äta den med vitt bröd, som dubblerar den raffinerade stärkelsen.',
                    'Förkoka potatistärningarna, bryn dem sedan i lite olivolja i stället för att fritera dem, och '
                    'tillsätt därefter äggen; det minskar kalorierna och det oxiderade fettet tydligt.',
                    'Rätten är mycket mättande; om du håller koll på vikten och blodsockret är det bättre att ha mer ägg '
                    'än potatis i pannan för en bättre näringsbalans.')),
    218: dict(lead='Den självklara följeslagaren till arabiska rätter och vardagsgrytor: vitt ris kokat med rostad '
                   'vermicelli och lite ghee. Den viktigaste frågan är hur man kan njuta av det utan att blodsockret '
                   'stiger snabbt. Både vitt ris och vermicelli är raffinerad stärkelse med ett medelhögt glykemiskt index '
                   '(65), och hemligheten ligger helt i portionens storlek och vad man äter till.',
              tips=('Ät aldrig riset med vermicelli ensamt; ät det alltid som en liten del till grytor med mycket '
                    'grönsaker och kött (som okra eller molokhia), och håll portionen till 4–6 matskedar.',
                    'Blötlägg och skölj riset väl för att få bort överflödig ytstärkelse, och använd naturligt ghee med '
                    'måtta för smakens skull; fettet bromsar magsäckstömningen jämfört med enbart kokt ris.',
                    'Resistent stärkelse: när riset kokas, får svalna i kylskåpet och sedan värms upp igen ändras '
                    'strukturen hos en del av stärkelsen, så att den tas upp långsammare.')),
    219: dict(lead='Den mest lockande formen för fester och familjemiddagar: ugnsbakad pasta med kryddad köttfärs, dränkt '
                   'i gyllene béchamelsås. Den mäktiga kombinationen av kött, mjölkfett och smör bromsar nedbrytningen av '
                   'pastan, med ett medelhögt glykemiskt index (58), men den höga kaloritätheten kräver medvetenhet.',
              tips=('Börja måltiden med en rejäl grön sallad med vinäger och olivolja, och nöj dig med en medelstor bit '
                    'gratäng som en komplett huvudrätt utan andra stärkelserika förrätter.',
                    'Gör béchamelsåsen på lättmjölk och mild buljong, byt ut hälften av vetemjölet mot majsstärkelse eller '
                    'havremjöl, och fyll köttfärsen med lök och riven svamp för mer fibrer.',
                    'En energirik och proteinrik måltid som passar unga och aktiva personer, medan den som har '
                    'insulinresistens eller rör sig lite bör hålla strikt koll på bitens storlek för att undvika '
                    'tyngdkänsla efter maten.')),
    220: dict(lead='Den traditionella osmanska klassikern: köttbullar av kryddad köttfärs och lök som kokas i en tjock '
                   'tomatsås med rostade pinjenötter. Köttbullarna ger protein, och rätten har ett lågt glykemiskt index '
                   '(42) och ger en djup känsla av mättnad.',
              tips=('Njut av köttbullarna och den fylliga tomatsåsen med gaffel tillsammans med en fräsch grön sallad, och '
                    'nöj dig med två till tre matskedar vitt ris.',
                    'Grädda köttbullarna i ugnen några minuter så att överflödigt fett försvinner och de håller ihop innan '
                    'du lägger dem i tomatsåsen, och undvik att reda såsen med majsstärkelse eller socker; låt den i '
                    'stället koka ihop långsamt.',
                    'Ren nöt- eller lammfärs innehåller järn och B12-vitamin, och protein bidrar till att bibehålla '
                    'muskelmassan; blodsockret håller sig stabilt om du är måttlig med riset.')),
    221: dict(lead='Världens mest beställda restaurangsallad: krispig romansallad toppad med grillat kycklingbröst, '
                   'parmesan och krutonger med fyllig caesardressing. Den innehåller mycket lite kolhydrater och har ett '
                   'lågt glykemiskt index (20), vilket gör den till en snabb och utmärkt måltid för dig som vill ha en '
                   'proteinrik och mättande rätt.',
              tips=('En perfekt arbetslunch som mättar direkt utan trötthet efter maten; minska mängden vita krutonger '
                    'eller byt ut dem mot rostade nötter för fett av bättre kvalitet.',
                    'Be om dressingen vid sidan om och doppa gaffeln i den i stället för att hälla hela mängden över '
                    'salladen; färdiga caesardressingar kan innehålla härdat fett och dolt salt och socker.',
                    'Kycklingens magra protein tillsammans med salladens fibrer och parmesanen är en bra kombination för '
                    'ett stabilt blodsocker och viktkontroll, och hemligheten ligger helt i dressingens kvalitet och '
                    'mängd.')),
    222: dict(lead='Medelhavets friskhet: tärningar av färsk gurka, mogna tomater, paprika, rödlök, kalamataoliver och en '
                   'bit naturell fetaost kryddad med olivolja och oregano. Nettokolhydraterna är nästan noll och det '
                   'glykemiska indexet är inte tillämpligt.',
              tips=('En utmärkt inledning på vilken huvudmåltid som helst eller en komplett sommarmiddag; fibrerna, '
                    'olivoljan och fetaosten ger en lugn mättnad och förhindrar en snabb blodsockerstegring.',
                    'Använd kallpressad extra jungfruolivolja och äppelcidervinäger eller citron och rikligt med torkad '
                    'oregano, och undvik färdiga dressingar för att bevara de äkta medelhavssmakerna.',
                    'Naturell fetaost innehåller kalcium och B12-vitamin men är salt, så tänk på det om du behöver hålla '
                    'koll på blodtrycket; du kan lägga osten i vatten en stund för att minska saltet.')),
    223: dict(lead='Den moderna salladen för smart näring: kokt quinoa blandad med avokadotärningar, körsbärstomater, '
                   'gurka och koriander med en dressing av citron och olivolja. Quinoa är ett fullkorn med fullvärdigt '
                   'vegetabiliskt protein och fibrer, vilket ger salladen ett lågt glykemiskt index (53).',
              tips=('En komplett måltid som passar vegetarianer och idrottare efter träning, och avokadons omättade fett '
                    'gör att blodsockret håller sig jämnt.',
                    'Koka quinoan i mild grönsaksbuljong och låt den svalna helt innan du blandar den med de färska '
                    'grönsakerna; nedkylningen ökar mängden resistent stärkelse och ger salladen en krispigare konsistens.',
                    'Quinoa är naturligt glutenfri och innehåller magnesium och järn; den är ett fint alternativ till '
                    'pasta- och rissallader.')),
    224: dict(lead='Den eleganta gröna salladen med sin skarpa, karaktäristiska smak: ruccola toppad med rubinröda '
                   'granatäpplekärnor, valnötshalvor och parmesan eller halloumi med lite granatäpplesirap. '
                   'Nettokolhydraterna är mycket låga, det glykemiska indexet är inte tillämpligt, och valnötterna '
                   'innehåller vegetabiliskt omega-3 (ALA).',
              tips=('Ett lyxigt tillbehör som passar perfekt före kött- och fiskrätter; valnötterna ger en mättande '
                    'krispighet som bromsar upptaget av måltiden.',
                    'Använd naturlig granatäpplesirap utan tillsatt socker och i måttlig mängd (bara en tesked), och låt '
                    'de färska granatäpplekärnornas naturliga sötma, extra jungfruolivoljan och citronsaften stå för '
                    'smaken.',
                    'Ruccola innehåller naturligt nitrat.')),
    225: dict(lead='Den enkla och omtyckta salladen från det levantinska köket och medelhavsköket: kokta potatistärningar '
                   'kryddade med extra jungfruolivolja, krossad vitlök, citronsaft och rikligt med hackad persilja. Den '
                   'vanliga frågan är om kokt potatissallad höjer blodsockret lika mycket som pommes frites. Det '
                   'glykemiska indexet är medelhögt (56), och den smälts betydligt lugnare än potatismos eller friterad '
                   'potatis.',
              tips=('Ät en måttlig portion som stärkelsetillbehör till grillad fisk eller kyckling med grönsaker, och låt '
                    'persiljan och olivoljan dominera på tallriken.',
                    'Den viktigaste hemligheten: koka potatistärningarna med skalet på tills de är klara och låt dem sedan '
                    'svalna helt i kylskåpet i några timmar innan du kryddar dem; nedkylningen omvandlar en stor del av '
                    'stärkelsen till resistent stärkelse som tas upp långsamt.',
                    'Olivoljan och citronsaften i dressingen bromsar nedbrytningen av stärkelsen; salladen passar '
                    'idrottare och andra med stort energibehov, så länge portionen hålls måttlig.')),
    226: dict(lead='Färg och näring på bordet: tärningar av djupröd rödbeta kryddade med vitlök, citronsaft, olivolja och '
                   'persilja. Många tvekar på grund av rödbetans söta smak: höjer den blodsockret? Det glykemiska indexet '
                   'är medelhögt (64), men den höga halten vatten och fibrer gör att den glykemiska belastningen i en '
                   'måttlig portion är låg till måttlig och väl godtagbar.',
              tips=('Ät två till tre matskedar som ett färgglatt tillskott ovanpå den gröna salladen i stället för en hel '
                    'tallrik rödbetor, så balanserar du den totala mängden naturligt socker.',
                    'Koka rödbetorna hela med skalet på utan att skära i dem så att färgen stannar kvar, skala och tärna '
                    'dem när de har svalnat, och blanda med olivolja och färsk citronsaft.',
                    'Rödbetor innehåller betalainer och naturligt nitrat; för dig som håller koll på blodsockret är det '
                    'bäst att äta dem kokta tillsammans med fibrer och fett, så undviker du kraftiga toppar.')),
    227: dict(lead='Den snabba favoritsalladen bland studenter och kontorsarbetare: avrunnen tonfisk blandad med söt gul '
                   'majs, sallad, lite majonnäs och citronsaft. Tonfiskens magra protein är fritt från kolhydrater, medan '
                   'majsen tillför en måttlig mängd stärkelse, vilket ger salladen ett lågt glykemiskt index (35) och en '
                   'snabb mättnad.',
              tips=('En komplett och utmärkt lunch utanför hemmet; salladen mättar länge, och om du äter den direkt med '
                    'gaffel behöver du inget bröd.',
                    'Byt ut hälften av majonnäsen mot en sked naturell yoghurt eller olivolja och citron, och ta rikligt '
                    'med sallad och hackad gurka för mer volym och fibrer utan extra kalorier.',
                    'Gul majs innehåller kolhydrater och naturlig stärkelse, så var måttlig med majsen och öka mängden '
                    'tonfisk och bladgrönsaker, så förblir rättens glykemiska belastning låg.')),
    228: dict(lead='Den förtrollande tropiska frukten med sitt speciella yttre och fruktkött prickat med små svarta frön '
                   'som liknar sesam. Många undrar om drakfrukt passar vid diabetes och bantning. Den har en mycket '
                   'måttlig sötma, mycket vatten och lösliga fibrer och ett lågt glykemiskt index (48).',
              tips=('Njut av en halv till en medelstor kyld frukt som ett svalkande mellanmål en varm sommardag, och ät '
                    'den i bitar med sked så får du med de små, krispiga fröna.',
                    'Ät den färsk och kyld som den är, eller tärnad i en fruktsallad med tranbär och kiwi, och undvik att '
                    'pressa den eller mixa den med tillsatt socker, så bevaras fibrernas struktur.',
                    'Drakfrukt innehåller C-vitamin och fibrer och är ett tryggt sätt att njuta av en exotisk smak utan '
                    'oro för kraftiga blodsockertoppar.')),
    229: dict(lead='En tropisk fräschörsbomb med syrlig, doftande smak och krispiga frön omgivna av gyllene fruktkött. Den '
                   'vanliga frågan är om den passar blodsockret. Passionsfrukt är en av de fiberrikaste frukterna i '
                   'förhållande till sin vikt, och det glykemiska indexet är lågt (30).',
              tips=('Skär upp en eller två frukter med kniv och ät fruktköttet och fröna direkt med sked; de krispiga '
                    'fröna ger olösliga fibrer och en omedelbar känsla av fräschör.',
                    'Lägg färskt passionsfruktkött på en skål naturell grekisk yoghurt eller morgonens havregrynsgröt, så '
                    'får du en härlig tropisk smak utan att behöva sötningsmedel eller socker.',
                    'Passionsfrukt innehåller ämnet piceatannol och mycket växtfibrer, ett utmärkt val för dig som tycker '
                    'om syrliga, fräscha smaker.')),
    230: dict(lead='Asiens tropiska pärla med sitt skrovliga rosa skal och sitt genomskinliga, saftiga vita fruktkött med '
                   'en unik blommig smak. Fruktälskare frågar om litchi innehåller mycket socker. Litchi har en tydlig '
                   'naturlig sötma och mycket vatten och ett lågt glykemiskt index (50), så njut av den medvetet och med '
                   'måtta i antalet.',
              tips=('Håll portionen till 5–6 färska frukter som en naturlig och svalkande efterrätt efter maten, och ät '
                    'dem långsamt i stället för att äta stora mängder på en gång.',
                    'Ät färska skalade litchi som de är och undvik helt konserverade litchi i sockerlag; konserveringen '
                    'ökar mängden fritt socker kraftigt.',
                    'Litchi innehåller C-vitamin och koppar; för dig som håller koll på vikten och blodsockret räcker en '
                    'medveten portion med några få frukter för att njuta av den fina smaken.')),
    231: dict(lead='Sommarens folkliga favoritfrukt i Levanten och Maghreb: kylda kaktusfikon fulla av svalkande sötma och '
                   'hårda frön. Den mest sökta frågan är om kaktusfikon passar vid diabetes. Det är en ovanlig frukt med '
                   'ett lågt glykemiskt index (35) och geléartade fibrer som bromsar upptaget av sockret.',
              tips=('Njut av två till tre kylda frukter på morgonen eller som ett svalkande mellanmål i sommarvärmen; de '
                    'släcker törsten och innehåller vatten samt mineraler som magnesium och kalium.',
                    'Skala frukterna försiktigt och ät dem färska och kylda som de är, tugga fruktköttet och undvik att '
                    'pressa dem och sila bort frön och fibrer.',
                    'De lösliga fibrerna och pektinet i kaktusfikon bidrar till en jämnare blodsockerkurva; drick '
                    'tillräckligt med vatten och var måttlig med antalet, så mår magen bra.')),
    232: dict(lead='Gyllene torkade aprikoser är ett av de godaste naturliga mellanmålen med fibrer och mineraler. Många '
                   'blir förvånade över att torkade aprikoser har ett lågt glykemiskt index (30) enligt den kliniska '
                   'granskningen; de lösliga fibrerna (pektin) bromsar nedbrytningen av det naturliga sockret.',
              tips=('Håll portionen till 3–4 aprikoser som mellanmål efter träning eller mellan måltiderna, och kombinera '
                    'dem med några råa mandlar eller valnötter för att bli mättare och bromsa upptaget ytterligare.',
                    'Välj bruna, soltorkade aprikoser utan tillsatt svaveldioxid, och skölj och blötlägg dem en stund i '
                    'ljummet vatten om du vill ha en mjukare konsistens.',
                    'Torkning koncentrerar sockret och kalorierna i en mindre volym, så att räkna portionen i antal och '
                    'inte äta fritt ur påsen är det säkraste sättet att hålla blodsockret jämnt.')),
    233: dict(lead='Den traditionella frukten full av krispiga små frön, som innehåller kalcium, kalium och järn. Torkade '
                   'fikon har ett medelhögt glykemiskt index (61) enligt den kliniska granskningen, eftersom det naturliga '
                   'sockret koncentreras när vattnet avdunstar, så de bör ätas medvetet och med tanke på portionen.',
              tips=('Nöj dig med en eller två fikon som en naturlig efterrätt till en kopp svart kaffe eller grönt te, och '
                    'undvik att äta fritt av dem på tom mage, så slipper du en snabb glukosstegring.',
                    'Skär fikonet i små bitar och lägg dem i en skål naturell grekisk yoghurt med en nypa kanel; '
                    'yoghurtens protein och fett bromsar upptaget av fikonens socker.',
                    'För dig som håller koll på vikten och blodsockret ger ett enda fikon all smak och njutning utan någon '
                    'extra kolhydratbelastning.')),
    234: dict(lead='Mörka katrinplommon med en söt och fyllig smak. De har ett lågt glykemiskt index (29) enligt den '
                   'kliniska granskningen, och hemligheten är det naturliga sockeralkoholen sorbitol, som tas upp '
                   'långsamt, och de rikliga lösliga fibrerna.',
              tips=('Ät två till tre katrinplommon om dagen på morgonen med ett glas ljummet vatten; de mättar väl.',
                    'Du kan lägga katrinplommonen i vatten över natten, dricka blötläggningsvattnet och äta frukterna på '
                    'morgonen, så blir fibrerna mjukare.',
                    'Katrinplommon innehåller polyfenoler och är ett av de smartaste valen bland torkad frukt vid '
                    'diabetes, så länge du håller dig till portionen.')),
    235: dict(lead='Röda bär med rötter i gammal asiatisk folkmedicin, kända för sin höga näringstäthet och sitt innehåll '
                   'av zeaxantin. Gojibär har ett lågt glykemiskt index (29) tack vare sin höga halt av komplexa fibrer '
                   'och protein jämfört med annan torkad frukt.',
              tips=('En matsked (cirka 15–20 g) räcker gott, och tillsammans med en näve nötter blir det ett balanserat '
                    'mellanmål.',
                    'Låt de torkade gojibären dra några minuter i varmt te eller vatten så att de blir mjuka igen, eller '
                    'strö dem över en grönsakssallad för en lätt syrlighet och en glad färg.',
                    'Om du tar blodförtunnande läkemedel bör du rådfråga din läkare innan du äter koncentrerade mängder '
                    'gojibär varje dag.')),
    236: dict(lead='Gyllene, livfulla rötter: färsk riven gurkmeja har en aromatisk smak och innehåller curcumin. Eftersom '
                   'den används i små mängder som krydda är det glykemiska indexet inte tillämpligt.',
              tips=('Tillsätt en tesked riven färsk gurkmeja i soppor, grytor eller marinader till kyckling och grillade '
                    'grönsaker för en naturlig gyllene färg och en djup, jordig smak.',
                    'Hemligheten bakom upptaget: tillaga alltid gurkmeja med en nypa svartpeppar och en fettkälla som '
                    'olivolja; piperinet i pepparn ökar upptaget av curcumin i kroppen.',
                    'Personer med aktiva gallstenar bör vara måttliga med gurkmeja.')),
    237: dict(lead='Vinterns följeslagare: färsk ingefärsrot med sin heta, skarpa smak och sitt innehåll av gingeroler. '
                   'Kolhydraterna i en portion är nästan obefintliga och det glykemiska indexet är inte tillämpligt.',
              tips=('Drick färska ingefärsskivor med citron i varmt vatten efter mastiga måltider.',
                    'Riv en liten bit färsk ingefära i asiatiska rätter och kötträtter för att göra köttet mört, och '
                    'undvik att koka den länge, så bevaras de känsliga flyktiga oljorna.',
                    'Var måttlig med ingefära och undvik mycket stora mängder om du har aktivt magsår eller svår sur '
                    'reflux.')),
    238: dict(lead='Drottningen bland de aromatiska kryddorna och favoriten i bakverk och drycker: äkta ceylonkanel, tunn '
                   'och i många lager, med en mild söt smak. Det glykemiska indexet är inte tillämpligt.',
              tips=('Strö en halv tesked malen kanel över havregrynsgröten, morgonkaffet eller fruktbitar; kanelen ger en '
                    'känsla av sötma så att du inte behöver tillsätta raffinerat socker.',
                    'Välj alltid äkta ceylonkanel och undvik den tjocka kinesiska kassiakanelen; ceylonkanel är nästan fri '
                    'från kumarin och passar för regelbunden daglig användning.',
                    'Kanel är en god krydda i drycker och rätter, men den ersätter inte medicinsk behandling.')),
    239: dict(lead='Exklusiva, aromatiska kardemummakapslar som ger det arabiska kaffet och de orientaliska rätterna deras '
                   'äkta karaktär. Kardemumma innehåller aromatiska oljor som terpineol och ger en frisk smak, och det '
                   'glykemiska indexet är inte tillämpligt eftersom mängden är så liten.',
              tips=('Lägg lätt öppnade kardemummakapslar i teet, kaffet eller när du kokar kött och kyckling; de tar bort '
                    'oönskade lukter.',
                    'Mal kardemummakapslarna färska precis före användning för att bevara de koncentrerade flyktiga '
                    'oljorna, i stället för att köpa färdigmald kardemumma som snabbt förlorar sin doft.',
                    'Kardemumma påverkar inte blodsockret och tillför praktiskt taget inga kalorier i de mängder som '
                    'används.')),
    240: dict(lead='Det röda guldet och världens dyraste krydda: naturliga saffranstrådar med en kunglig doft och klart '
                   'karmosinröd färg. Saffran innehåller krocin och krocetin, det glykemiska indexet är inte tillämpligt, '
                   'och kryddan ger rätterna en särskild smak utan nämnvärda kolhydrater.',
              tips=('Låt några saffranstrådar dra i en kopp rosenvatten eller varmt vatten i en kvart och tillsätt sedan '
                    'blandningen till risrätter eller te för att njuta av färgen och doften.',
                    'Mortla saffranstrådarna försiktigt med ett korn grovt salt innan du blötlägger dem, så frigörs all '
                    'färg och smak, och undvik att koka dem kraftigt.',
                    'En mycket liten mängd saffranstrådar räcker gott för smak och färg.')),
    241: dict(lead='Medelhavsbergens doft i en sked: torkade blad av vild timjan med aromämnena tymol och karvakrol. '
                   'Kolhydraterna i en sked krydda är försumbara och det glykemiska indexet är inte tillämpligt, och '
                   'kryddan är en grundpelare i det italienska och levantinska köket.',
              tips=('Strö rikligt över sallader, äggrätter, tomatsåser och ost; aromatiska örter förhöjer smaken och '
                    'minskar behovet av salt.',
                    'Gnid de torkade timjanbladen mellan handflatorna direkt över den varma rätten i slutet av '
                    'tillagningen, så frigörs de aromatiska oljorna utan att brännas av värmen.',
                    'Vild timjan innehåller polyfenoler.')),
    242: dict(lead='Blågröna alger som innehåller mikronäringsämnen, fullvärdigt protein och järn. Eftersom den används i '
                   'små mängder (en tesked, cirka 3–5 g) är kolhydratpåverkan försumbar och det glykemiska indexet är inte '
                   'tillämpligt.',
              tips=('Tillsätt en tesked spirulinapulver i morgonens gröna smoothie eller i ett glas vatten med lite '
                    'pressad citron.',
                    'Att blanda spirulina med citrusjuice (som citron eller apelsin) döljer den karaktäristiska havs- och '
                    'jordsmaken, och C-vitamin ökar järnupptaget.',
                    'Spirulina innehåller fykocyanin och klorofyll; om du har sköldkörtelsjukdom eller autoimmun sjukdom '
                    'är det bäst att rådfråga din läkare innan du använder den dagligen i större mängder.')),
    243: dict(lead='Favoritvalet bland idrottare och för dig som vill bygga muskler och hålla vikten: rent protein som '
                   'separerats från det mesta av mjölkens fett och socker (laktos). Kolhydraterna i en skopa är nästan '
                   'obefintliga, det glykemiska indexet är inte tillämpligt, och protein bidrar till att öka muskelmassan.',
              tips=('Ta en skopa blandad med vatten efter träningen eller mellan måltiderna; protein bidrar till att '
                    'bibehålla muskelmassan, även när du äter för att gå ner i vikt.',
                    'Blanda det med kallt vatten eller osötad mandeldryck i en shaker, och undvik mycket varmt vatten, så '
                    'att proteinet inte klumpar sig.',
                    'Vassleproteinisolat är ett bra val även för personer med lindrig laktosintolerans; välj produkter '
                    'utan tillsatt socker eller sötningsmedel.')),
    244: dict(lead='Det gyllene alternativet till vitt mjöl för dig som äter keto eller lågkolhydratkost: skalade, '
                   'finmalda mandlar med mycket enkelomättat fett och protein. Det glykemiska indexet är lågt (15), vilket '
                   'gör mandelmjölet till ett alternativ till vanligt bröd som knappt påverkar blodsockret.',
              tips=('Använd det till bakverk och pannkakor; det mättar väl i flera timmar.',
                    'Eftersom mandelmjöl saknar gluten kan du blanda det med ägg eller psylliumskal (loppfröskal), så '
                    'håller degen ihop och jäser bättre vid bakning.',
                    'Mandelmjöl innehåller E-vitamin och magnesium men är, som alla nötter, mycket energitätt, så håll '
                    'bakverken måttligt stora.')),
    245: dict(lead='Ett mjöl med mycket fibrer: torkat och malet kokoskött som oljan har pressats ur. Det har en mild '
                   'tropisk doft och ovanligt mycket lösliga och olösliga fibrer, ett lågt glykemiskt index (45) och lite '
                   'nettokolhydrater.',
              tips=('Ett utmärkt glutenfritt växtbaserat alternativ i bakverk vid diabetes; det mättar snabbt eftersom det '
                    'suger upp mycket vätska.',
                    'Kokosmjöl suger upp vätska som en svamp, så du behöver bara en tredjedel så mycket som vanligt mjöl '
                    'och dubbelt så många ägg eller mycket mer vätska i receptet.',
                    'Ett utmärkt glutenfritt val, men var försiktig om du är allergisk mot kokos, och drick rikligt med '
                    'vatten så hanterar magen de täta fibrerna lättare.')),
    246: dict(lead='Den traditionella drycken med sin karaktäristiska syrlighet och omedelbara fräschör: ett extrakt av '
                   'naturlig tamarind. Den avgörande frågan är om tamarind höjer blodsockret. Naturlig tamarind är i sig '
                   'syrlig och har ett lågt glykemiskt index (40), men risken ligger alltid i de stora mängder raffinerat '
                   'socker som traditionellt tillsätts.',
              tips=('Njut av ett kallt glas hemgjord tamarinddryck utan socker eller sötad med ett sötningsmedel för att '
                    'släcka törsten på sommaren.',
                    'Lägg naturlig tamarind i vatten, låt det koka upp en stund och sila, och justera syrligheten med '
                    'citronsaft eller några droppar stevia i stället för vitt socker.',
                    'Färdig tamarinddryck i butiker och restauranger är en färgad, koncentrerad sockerlösning som höjer '
                    'blodsockret kraftigt, så gör den helst själv av hela tamarindfrukter.')),
    247: dict(lead='Den äkta folkliga drycken med sin omtyckta jordiga, kolaliknande smak: ett avkok på '
                   'johannesbrödsfrukter. Johannesbröd innehåller fibrer och naturligt socker, är fritt från koffein och '
                   'har ett lågt glykemiskt index (40).',
              tips=('Drick ett litet glas med is som ett alternativ till läsk och varm choklad; johannesbrödet ger en '
                    'naturlig känsla av sötma.',
                    'Koka de krossade johannesbrödsfrukterna långsamt i vatten så att den naturliga sötman frigörs utan '
                    'att brännas, undvik raffinerat socker, och drick drycken kall och väl silad.',
                    'Johannesbrödsfrukter innehåller garvämnen och pektin; tänk på att färdiga drycker sötade med socker '
                    'höjer blodsockret.')),
    248: dict(lead='Den arabiska vinterns värme i en kopp: en tjock, varm mjölkdryck doftande av mastix och '
                   'apelsinblomsvatten, toppad med kanel, kokos och nötter. Mjölksockret och stärkelsen ger ett lågt '
                   'glykemiskt index (55) och snabb energi, så mängden tillsatt socker behöver hållas i schack.',
              tips=('Njut av en liten kopp som en värmande stund kalla vinterkvällar, och strö rikligt med kanel och '
                    'naturella nötter som valnötter och pistage för att bromsa upptaget av stärkelsen.',
                    'Gör sahlab på standardmjölk med lite sahlabpulver eller majsstärkelse, byt ut sockret mot ett '
                    'sötningsmedel och smaksätt med apelsinblomsvatten och äkta mastix.',
                    'Nötterna och kanelen på toppen är inte bara dekoration; deras fett och fibrer bromsar upptaget av '
                    'sahlabens kolhydrater och bidrar till ett jämnare blodsocker.')),
    249: dict(lead='En symbol för generositet och gästfrihet på Arabiska halvön: ljust, lätt rostat kaffe som kokas med '
                   'rikligt med kardemumma, saffran och mastix. Nästan inga kalorier, inga kolhydrater, och det glykemiska '
                   'indexet är inte tillämpligt; kaffet påverkar inte blodsockret.',
              tips=('En perfekt dryck efter maten eller när man träffas; drick det alltid utan socker för att njuta av '
                    'kardemummans och kryddornas doft.',
                    'Koka det ljusa kaffet på låg värme i tjugo minuter, och tillsätt nymald grön kardemumma och '
                    'saffranstrådar i kannan vid serveringen, så bevaras smaken och de flyktiga oljorna.',
                    'Arabiskt kaffe höjer i sig inte blodsockret; hemligheten ligger i att inte äta för många av dadlarna '
                    'som serveras till, utan nöja sig med en eller två.')),
    250: dict(lead='Gulfens varma gatute: starkt svart te som kokas länge med evaporerad mjölk, kardemumma, kryddnejlika, '
                   'saffran och ingefära. Mjölken och kryddorna ger teet ett lågt glykemiskt index (50), och effekten '
                   'beror helt på mängden tillsatt socker.',
              tips=('Be om karakte utan socker eller med mycket lite socker, så njuter du av kryddorna och den '
                    'koncentrerade mjölken utan en onödig glukostopp.',
                    'Gör det hemma av löst svart te och osötad evaporerad mjölk, och koka det med kardemumma, färsk '
                    'ingefära och kryddnejlika för en äkta och balanserad karaksmak.',
                    'Färdigt karakte innehåller ofta stora mängder sötad kondenserad mjölk, så om du gör det med vanlig '
                    'osötad evaporerad mjölk blir det ett mycket bättre val för ett stabilt blodsocker.')),
    251: dict(lead='Den asiatiska frukten med sitt häpnadsväckande yttre av mjuka röda hår och sitt genomskinliga vita '
                   'fruktkött som liknar litchi. Rambutan har en måttligt söt smak och mycket saft och ett lågt glykemiskt '
                   'index (50), så ät den med måtta för att hålla koll på det enkla sockret.',
              tips=('Håll portionen till 4–5 färska frukter som ett svalkande sommarmellanmål; fruktköttet innehåller '
                    'mycket vatten och C-vitamin.',
                    'Skala den färska frukten med fingrarna och ät fruktköttet direkt, undvik att bita i den bittra kärnan '
                    'och ät frukten som den är utan sötningsmedel eller mixad i juice.',
                    'Rambutan innehåller koppar och mangan; för dig som håller koll på vikten och blodsockret räcker det '
                    'att hålla dig till det bestämda antalet frukter för att njuta av den tropiska smaken utan att få i '
                    'dig för mycket energi.')),
    252: dict(lead='Små gyllene citrusfrukter som äts hela med skal och fruktkött i en enda tugga! Det speciella är att '
                   'skalet är sött medan fruktköttet är syrligt och skarpt. Kumquat innehåller mycket fibrer och har ett '
                   'lågt glykemiskt index (30).',
              tips=('Ät 4–5 hela frukter med skalet som en svalkande efterrätt eller ett mellanmål; skalet är rikt på '
                    'aromatiska oljor och bromsar nedbrytningen av det naturliga sockret.',
                    'Skölj frukterna väl och ät dem råa utan att skala dem, eller skär dem i tunna skivor och lägg dem i '
                    'en grön sallad för en karaktäristisk, fyllig citrussmak.',
                    'Kumquatskalet innehåller flavonoider och fibrer, och frukten passar utmärkt vid bantning och mättar '
                    'väl.')),
    253: dict(lead='Sydostasiens "fruktkung": den taggiga frukten som är känd för sin genomträngande, omdiskuterade doft '
                   'och sin krämiga konsistens som påminner om vaniljkräm. Durian skiljer sig genom att innehålla fett och '
                   'protein, och den har ett lågt glykemiskt index (49), men den är mycket kalorität.',
              tips=('En liten bit räcker gott; den krämiga konsistensen och fettet ger en tung och omedelbar mättnad, så '
                    'du behöver inte mer.',
                    'Ät den färsk och kyld direkt när den har öppnats, och undvik att äta den med annan fet mat i samma '
                    'måltid eftersom den är mäktig och kalorität.',
                    'Durian innehåller kalium, B-vitaminer och tryptofan; eftersom den är så kalorität bör du som håller '
                    'koll på vikten och blodsockret räkna en bit som en hel, energirik måltid.')),
    254: dict(lead='Den glada tropiska frukten som bildar gula, femuddiga stjärnor när den skärs på tvären; fruktköttet är '
                   'krispigt, saftigt och milt syrligt. Den innehåller mycket lite kolhydrater, det glykemiska indexet är '
                   'inte tillämpligt, och den är en svalkande frukt med få kalorier.',
              tips=('Ät en medelstor frukt skuren i stjärnor i en fruktsallad eller som den är; den ger vätska, C-vitamin '
                    'och fibrer utan oro för blodsockret.',
                    'Skölj frukten och skär den direkt i tunna stjärnor med det tunna skalet kvar, och strö över lite '
                    'färsk mynta för extra fräschör.',
                    '⚠️ Mycket viktig klinisk varning: stjärnfrukt innehåller nervgiftet karamboxin och mycket oxalat; den '
                    'får inte ätas av personer med njursvikt eller i dialys, eftersom sjuka njurar inte kan utsöndra '
                    'ämnet. För friska personer är den säker.')),
    255: dict(lead='Världens största trädfrukt: en jättelik tropisk frukt med mjuka gula klyftor och en doft som påminner '
                   'om både banan och ananas. Mogen jackfrukt har ett högt glykemiskt index (75) eftersom den innehåller '
                   'socker som bryts ned snabbt, så portionen kräver strikt uppmärksamhet.',
              tips=('Nöj dig med två till tre klyftor av den mogna frukten som ett begränsat mellanmål, och ät en '
                    'proteinkälla eller nötter till för att bromsa sockerupptaget.',
                    'Grön (omogen) jackfrukt används som ett fantastiskt växtbaserat alternativ till kött i salta rätter '
                    'som tacos och grytor; den omogna frukten innehåller mycket fibrer och dess stärkelse tas upp '
                    'betydligt långsammare.',
                    'Jackfrukt innehåller kalium och A-vitamin; vid diabetes eller viktkontroll är det bättre att äta kokt '
                    'grön jackfrukt och undvika för mycket mogen frukt eller frukt på burk i sockerlag.')),
    256: dict(lead='"Den tropiska fruktens drottning": ett tjockt lila skal döljer vita klyftor som liknar vitlöksklyftor, '
                   'med en sidenlen smak av persika och jordgubbe. Mangostan har ett lågt glykemiskt index (46) och '
                   'innehåller xantoner.',
              tips=('Njut av två till tre färska frukter efter maten; det svalkande fruktköttet ger en fin, mild sötma '
                    'utan några plötsliga blodsockertoppar.',
                    'Tryck försiktigt på det lila skalet för att öppna det med fingrarna och ät de vita klyftorna direkt, '
                    'och undvik att svälja de stora fröna i de största klyftorna.',
                    'Med sitt måttliga innehåll av fibrer och socker är mangostan en lyxig och trygg efterrätt för den som '
                    'vill njuta av något tropiskt.')),
    257: dict(lead='Höstens strålande orange frukt med honungsglans och mjuk, geléartad konsistens; en säsongsfrukt med '
                   'A-vitamin. Den eviga frågan är om persimon höjer blodsockret snabbt. Den har en tydlig sötma och ett '
                   'lågt glykemiskt index (50), men det höga innehållet av lösliga pektinfibrer gör att sockret tas upp '
                   'jämnt när frukten är lagom mogen.',
              tips=('Ät en medelstor frukt som ett mättande mellanmål mellan måltiderna eller som en naturlig efterrätt '
                    'efter lunchen, gärna med några råa mandlar för att fördröja nedbrytningen av sockret.',
                    'Välj fullmogna frukter som är lite mjuka, så att de sammandragande garvämnena har brutits ned, och ät '
                    'dem färska med det tunna, väl sköljda skalet för fibrernas skull.',
                    'Persimon innehåller karotenoider och lutein; för dig som håller koll på vikten och blodsockret ger en '
                    'enda frukt full mättnad och sötma utan att du behöver mer.')),
    258: dict(lead='Vårens gyllene förebud som fyller marknaderna i Levanten och Medelhavsområdet: små gula frukter med en '
                   'smak mellan aprikos och plommon och en glad syrlighet. Japansk mispel har ett lågt glykemiskt index '
                   '(55) och innehåller mycket vatten och fibrer.',
              tips=('Håll portionen till 4–5 frukter som en svalkande sommarportion frukt; de släcker törsten och '
                    'innehåller kalium och C-vitamin utan att vara tunga för magen.',
                    'Skala försiktigt bort det yttre skalet, ta bort de stora, släta kärnorna och njut av det färska '
                    'fruktköttet direkt, och undvik att pressa frukterna eller koka sylt med socker av dem.',
                    'Frukterna och bladen innehåller triterpener, och frukten passar bra för en naturlig mättnad.')),
    259: dict(lead='Den exotiska frukten med taggigt orange skal och smaragdgrönt, geléartat fruktkött med en smak som '
                   'blandar gurka, banan och citron. Nettokolhydraterna är mycket låga och det glykemiska indexet är lågt '
                   '(25), och frukten är en av de mest vätskerika och svalkande.',
              tips=('Skär frukten på mitten och ät det geléartade fruktköttet och de mjuka fröna direkt med sked; den ger '
                    'vätska och mineraler som magnesium och zink med nästan inga kalorier.',
                    'Njut av fruktköttet som det är med några droppar citronsaft eller rosenvatten, eller lägg det över en '
                    'frukt- och grönsakssallad för ett exotiskt utseende och en frisk, syrlig smak.',
                    'Ett ovanligt val för dig som äter keto eller lågkolhydratkost och vill ha en exotisk smak som knappt '
                    'påverkar blodsocker eller insulin.')),
    260: dict(lead='Mörklila bär från Amazonas regnskogar som har blivit mycket populära. Naturlig acai är nästan fri från '
                   'enkla sockerarter och innehåller ovanligt mycket fett (omega-9 och omega-6) och antocyaniner, och det '
                   'glykemiska indexet är inte tillämpligt.',
              tips=('En acaiskål är ett utmärkt frukostval, förutsatt att den görs av ren, osötad acaipuré och toppas med '
                    'en näve nötter, chiafrön och lite färska bär.',
                    "Köp fryst acaipuré där det tydligt står 'utan tillsatt socker' (unsweetened), och mixa den med osötad "
                    'mandeldryck och grekisk yoghurt.',
                    'Var försiktig med färdiga acaiskålar på kaféer; de mixas ofta med sockersirap, koncentrerad '
                    'äppeljuice och karamelliserade nötter och blir då en kaloririk sockerbomb.')),
    261: dict(lead='Den växande stjärnan bland de korsblommiga grönsakerna: en rund, krispig stam som förenar kålens sötma '
                   'med rädisans och äpplets krispighet. Nettokolhydraterna är mycket låga (cirka 2,6 g per 100 g), det '
                   'glykemiska indexet är inte tillämpligt, och kålrabbi mättar väl.',
              tips=('Skala och skär den i krispiga stavar och ät dem med hummus eller guacamole; ett naturligt och '
                    'krispigt alternativ till chips och friterade snacks.',
                    'Ät den rå och krispig för att få med C-vitamin och fibrer, eller ugnsrosta tärningar med olivolja och '
                    'rosmarin som ett alternativ till rostad potatis.',
                    'Kålrabbi innehåller isotiocyanater och passar utmärkt vid diabetes och viktkontroll utan '
                    'begränsningar i portionen.')),
    262: dict(lead='Den traditionella stjälkgrönsaken som är omtyckt i soppor och medelhavsmat; den ger en mild löksmak '
                   'med lätt sötma. Purjolök innehåller fibern inulin och har ett lågt glykemiskt index (15).',
              tips=('Tillsätt hackad purjolök i alla slags soppor, grytor och äggröror; den gör rätterna mer mättande.',
                    'Fräs den vita och ljusgröna delen varsamt i olivolja tills den mjuknar och får en söt, len '
                    'konsistens, och skölj den noga inifrån så att all jord mellan lagren försvinner.',
                    'Inulinfibrerna i purjolök bromsar sockerupptaget, och purjolök är ett bra val för mättnad och ett '
                    'stabilt blodsocker.')),
    263: dict(lead='Djupröd glädje på salladsbordet: krispiga kålblad som innehåller antocyaniner och C-vitamin. '
                   'Nettokolhydraterna är mycket låga och det glykemiska indexet är inte tillämpligt.',
              tips=('Gör riven rödkål till en daglig ingrediens i dina gröna sallader; den täta krispigheten kräver mycket '
                    'tuggande, vilket gör måltiden mer mättande.',
                    'Massera den strimlade kålen med lite havssalt, äppelcidervinäger och olivolja tio minuter före '
                    'servering; det mjukar upp fibrerna och gör kålen lättare att äta.',
                    'Rödkål innehåller K-vitamin och naturliga svavelföreningar, och den är ett utmärkt val vid diabetes '
                    'utan begränsningar i mängden.')),
    264: dict(lead='Krispiga rubinröda rädisor med en frisk, hettande smak; den ständiga följeslagaren till mezerätter och '
                   'grillat i Mellanöstern. Nettokolhydraterna är nära noll och det glykemiska indexet är inte '
                   'tillämpligt, och rädisor är en av de rotfrukter som inte påverkar blodsockret.',
              tips=('Ät färska röda rädisor med skalet till kött- och fiskrätter; den milda hettan ger rätterna en frisk '
                    'kontrast.',
                    'Skölj dem väl och ät dem färska, kalla och krispiga, eller skär dem i tunna skivor med citronsaft och '
                    'mynta, och undvik att tillaga dem, så behåller de sin krispighet och sina senapsoljor.',
                    'Rädisor är ett utmärkt sätt att ha något att tugga på och stå emot småätande mellan måltiderna, med '
                    'nästan inga kalorier.')),
    265: dict(lead='Kronan bland vildväxande örter på landsbygden i Levanten och Palestina: gröna malvablad plockade i '
                   'naturen och tillagade med extra jungfruolivolja, lök, vitlök och citronsaft. Bladen innehåller mycket '
                   'slemmiga växtfibrer och järn, nettokolhydraterna är mycket låga och det glykemiska indexet är inte '
                   'tillämpligt.',
              tips=('En värmande traditionell rätt; ät den med gaffel som en lätt kvällsrätt eller som tillbehör med '
                    'rikligt med pressad citron, och undvik för mycket vitt bröd till.',
                    'Låt de sköljda malvabladen sjuda på låg värme i olivolja tills de mjuknar men behåller sin mörkgröna '
                    'färg, och ta rikligt med vitlök och karamelliserad lök för en äkta smak.',
                    'Malvans slemmiga fibrer bromsar upptaget av kolhydrater, och rätten är ett fint exempel på naturlig '
                    'mat som mättar väl.')),
    266: dict(lead='Den folkliga mezerätten som älskas i varje hem och restaurang i Levanten och Egypten: blomkålsbuketter '
                   'friterade tills de blir gyllenbruna och kryddade med spiskummin, citron och tahini. Blomkål är en '
                   'utmärkt grönsak, men friteringen höjer kalorierna, och det glykemiska indexet är lågt (35).',
              tips=('Njut av några kryddade buketter som en del av mezen tillsammans med tahinisås med citron, och se till '
                    'att det inte blir en friterad vardagsrätt, så slipper du för mycket frityrolja.',
                    'Det bästa alternativet: rosta blomkålsbuketterna i ugnen eller i airfryer med lite olivolja och en '
                    'nypa spiskummin och vitlök; du får samma goda krispighet med en fjärdedel av kalorierna.',
                    'Strö gärna malen spiskummin över blomkålen; den ger rätten dess karaktäristiska smak.')),
    267: dict(lead='Aromatiska kryddnejlikor med runt huvud: en av de äldsta och mest kända kryddorna, med en het och varm '
                   'smak och mycket eugenol. Eftersom de används några stycken i taget som smaksättning är det glykemiska '
                   'indexet inte tillämpligt.',
              tips=('Lägg två till tre kryddnejlikor i tekannan, kaffet eller när du kokar kött; de ger en varm, kryddig '
                    'smak.',
                    'Koka kryddnejlikorna försiktigt med teet eller örterna för att frigöra de aromatiska oljorna.',
                    'Kryddnejlika är en bra krydda för måttlig daglig användning.')),
    268: dict(lead='Den exklusiva kungliga kryddan med söt, varm doft, som béchamelsås och vinterrätter inte blir '
                   'kompletta utan: kärnan i frukten av ett vintergrönt träd, rik på aromatiska oljor. Det glykemiska '
                   'indexet är inte alls tillämpligt eftersom den används i små nypor.',
              tips=('En mycket liten nypa (mindre än en kvarts tesked) räcker för att ge smak åt potatismos, béchamelsås, '
                    'pumpa och varma mjölkdrycker.',
                    'Riv den hårda kärnan färsk med ett fint rivjärn direkt över den varma rätten före servering; de '
                    'aromatiska oljorna avdunstar snabbt om den mals och förvaras länge.',
                    '⚠️ Viktig klinisk varning: muskotnöt är en utmärkt krydda i små mängder (en lätt nypa), men den får '
                    'inte användas i stora mängder (gram), eftersom den innehåller myristicin som i höga doser kan ge '
                    'förgiftning och nervpåverkan.')),
    269: dict(lead='Naturens tidlösa aromatiska barr i det italienska och medelhavsinspirerade köket: torkade rosmarinblad '
                   'som innehåller rosmarinsyra och karnosinsyra. En krydda vars glykemiska index inte är tillämpligt, som '
                   'ger grillat en fin, träig doft.',
              tips=('Strö över grillat kött, kyckling, fisk och ugnsgrönsaker; rosmarin kan minska bildningen av de ämnen '
                    'som uppstår vid höga temperaturer under grillningen.',
                    'Smula de torkade bladen mellan fingrarna över olivolja och vitlök och använd som marinad en halvtimme '
                    'före grillningen, så tränger smaken djupt in i köttet.',
                    'Rosmarin påverkar inte blodsockret och tillför inga nämnvärda kalorier.')),
    270: dict(lead='Doften av pizza och toskanska pastasåser: torkade aromatiska basilikablad med flavonoider och '
                   'linalool. Det glykemiska indexet är inte tillämpligt eftersom så lite används vid kryddningen.',
              tips=('Strö rikligt över tomatsåser, minestrone och ostsallader; aromatiska örter förstärker smaken och '
                    'minskar behovet av salt.',
                    'Tillsätt den torkade basilikan halvvägs eller mot slutet av tillagningen så att den blandas med '
                    'tomatsåsen utan att de fina aromatiska oljorna bränns.',
                    'Basilika innehåller aromatiska ämnen och passar i alla slags rätter.')),
    271: dict(lead='Svartkummin med sin långa tradition genom århundradena: frön av Nigella sativa med flyktig olja och '
                   'ämnet tymokinon. Eftersom den används i en nypa eller en tesked är det glykemiska indexet inte '
                   'tillämpligt, och den är ett gott tillskott i en balanserad kost.',
              tips=('Strö en halv tesked svartkummin över frukosträtter som vit ost, labneh och ägg, eller knåda in den i '
                    'bakverk för en omtyckt krispighet.',
                    'Mal fröna eller tugga dem väl när du äter; det hårda skalet kan hindra upptaget av tymokinonet inuti '
                    'om fröet sväljs helt utan att tuggas.',
                    'Svartkummin i måttliga mängder som krydda är en del av ett varierat kostmönster.')),
    272: dict(lead='Det syrliga, karmosinröda pulvret som utmärker det levantinska köket och traditionella rätter som '
                   'musakhan och fattoush: malda vilda sumakbär. Kolhydraterna i en sked krydda är mycket få och det '
                   'glykemiska indexet är inte tillämpligt, och sumak innehåller garvämnen.',
              tips=('Strö rikligt över lökskivor till grillat, fatayer och sallader; den naturliga syrligheten balanserar '
                    'fettet och ger en citrussmak så att du kan minska på salt och vinäger.',
                    'Välj naturlig sumak med mörkt vinröd till brunaktig färg utan tillsatta färgämnen och citronsyra, och '
                    'njut av den rena, syrliga smaken.',
                    'Sumak passar i ett kostmönster för ett stabilt blodsocker och är ett utmärkt sätt att ge maten smak '
                    'utan att höja blodtryck eller blodsocker.')),
    273: dict(lead='Den mest spridda och populära sötvattensfisken: kritvitt, milt kött med fullvärdigt protein som är '
                   'lätt att smälta. Tilapia är helt fri från kolhydrater och det glykemiska indexet är inte tillämpligt; '
                   'protein bidrar till att öka muskelmassan.',
              tips=('En typisk och idealisk lunch vid bantning och för blodsockret; ät den grillad eller ugnsbakad med en '
                    'stor grön sallad och ett halvt bröd eller några skedar ris.',
                    'Krydda med vitlök, spiskummin, citron och koriander och baka i ugnen eller på plåt, och undvik att '
                    'fritera den i härdade oljor, så förblir den mager och kalorisnål.',
                    'Tilapia är ett utmärkt, magert protein; köp den färsk från välskötta och pålitliga odlingar.')),
    274: dict(lead='Pärlan bland fiskarna i Persiska viken och på festborden: fast, vitt kött med en fin havssmak som är '
                   'omtyckt i machboos och sayadieh. Zackenabborre innehåller inga kolhydrater, det glykemiska indexet är '
                   'inte tillämpligt, och fisken ger protein av hög kvalitet och omega-3.',
              tips=('Njut av en ugnsgrillad filé med örter och citron och grillade grönsaker; den mättar länge utan någon '
                    'stärkelse.',
                    'Grilla fiskbitarna i en form med tomat-, paprika-, lök- och citronskivor och olivolja, och undvik för '
                    'mycket ris kokat i fett till, så njuter du av den äkta smaken.',
                    'Zackenabborre innehåller jod, selen och B-vitaminer, och selen bidrar till normal '
                    'sköldkörtelfunktion; ett lyxigt val för dig som håller koll på blodsocker och vikt.')),
    275: dict(lead='En ikon på de grekiska och medelhavsinspirerade restaurangerna: bläckfiskarmar grillade över kol tills '
                   'de blir krispiga utanpå och möra inuti. Bläckfisk är ett rent havsprotein nästan utan kolhydrater, det '
                   'glykemiska indexet är inte tillämpligt, och den innehåller järn och B12-vitamin.',
              tips=('En utmärkt förrätt eller huvudrätt för den som älskar skaldjur; ät den med rikligt med pressad '
                    'citron, extra jungfruolivolja och ruccolasallad för en proteinrik och mättande måltid.',
                    'Hemligheten bakom mör bläckfisk är att låta den sjuda långsamt på låg värme med vinäger och örter i '
                    'en timme tills den är mör, och sedan grilla den några minuter över het kolglöd för att få rökig smak.',
                    'Bläckfisk innehåller zink och taurin och är ett utmärkt livsmedel för idrottare och för dig som '
                    'strikt vill gå ner i vikt.')),
    276: dict(lead='Helgens favorit bland skaldjursrätterna: bläckfiskringar med ett tunt mjölhölje, friterade tills de '
                   'blir gyllene och krispiga. Bläckfisken i sig är rent havsprotein, men mjölet och friteringen höjer det '
                   'glykemiska indexet till cirka 45 och tillför mer energi.',
              tips=('Njut av några ringar som en trevlig skaldjursförrätt, pressa över en hel citron och ät dem med en '
                    'grön sallad, och undvik att doppa dem i tjock majonnäs eller färdig tartarsås.',
                    'Det smarta alternativet: be om grillad bläckfisk (grilled calamari) med vitlök, citron och persilja; '
                    'du får en härlig havssmak utan kolhydrater och med hälften av kalorierna.',
                    'Bläckfisk innehåller koppar och fullvärdigt protein; för dig som håller koll på vikten och '
                    'blodsockret är grillad bläckfisk det bättre valet, medan den friterade kräver en måttlig portion.')),
    277: dict(lead='Kungarnas mat och en av havens mest sällsynta delikatesser: blank, svart rom från stör med en '
                   'koncentrerad och karaktäristisk havssmak. Kaviar innehåller nästan inga nettokolhydrater, det '
                   'glykemiska indexet är inte tillämpligt, och den innehåller kolin, omega-3-fettsyror och fosfolipider.',
              tips=('En tesked räcker gott för att njuta av den exklusiva smaken; ät den på krispiga gurkskivor eller på '
                    'ett kokt ägg i stället för på vitt, raffinerat bröd.',
                    'Ät den kyld direkt med skedar av pärlemor eller ben och undvik metallskedar, som kan påverka den äkta '
                    'havssmaken, och utsätt den aldrig för värme.',
                    '⚠️ Viktig klinisk varning: kaviar innehåller mycket salt och bör ätas med måtta vid högt blodtryck, '
                    'och gravida rekommenderas att undvika rå eller opastöriserad kaviar på grund av risken för listeria.')),
    278: dict(lead='Små, silverglänsande fiskar med koncentrerad smak; grunden i caesardressing och napolitansk pizza. '
                   'Sardeller är rent havsprotein utan stärkelse, det glykemiska indexet är inte tillämpligt, och de '
                   'innehåller omega-3-fettsyror, kalcium och järn.',
              tips=('Tillsätt en eller två mosade filéer i salladsdressingar och såser för en djup umamismak utan att '
                    'behöva industriella smakförstärkare.',
                    'Lägg sardellfiléerna i kallt vatten eller olivolja några minuter före användning för att få bort '
                    'överflödigt salt, och njut av dem finhackade.',
                    '⚠️ Klinisk varning om salt: konserverade sardeller är mycket salta, så personer med högt blodtryck '
                    'eller njursjukdom bör äta dem med stor försiktighet och i mycket små mängder.')),
    279: dict(lead='Den egyptiska gatans stolthet och det mest kända leverreceptet i arabvärlden: tunna skivor kalvlever '
                   'som steks snabbt med vitlöksklyftor, chili, spiskummin, koriander och citronsaft. Levern innehåller '
                   'nästan inga kolhydrater, det glykemiska indexet är inte tillämpligt, och den innehåller mycket järn '
                   'och B-vitaminer.',
              tips=('Ät levern med gaffel tillsammans med tahinisallad och en grönsakssallad, och nöj dig med ett litet '
                    'bröd i stället för flera vita, raffinerade bröd.',
                    'Fräs levern på mycket hög värme i bara några minuter så att den förblir mör och saftig, och avsluta '
                    'med att pressa över en hel citron, eftersom C-vitamin ökar järnupptaget.',
                    '⚠️ Viktig närings- och klinisk upplysning: järn bidrar till normal bildning av röda blodkroppar och '
                    'hemoglobin, men gravida rekommenderas att inte äta för mycket lever eftersom den innehåller mycket '
                    'stora mängder naturligt A-vitamin.')),
    280: dict(lead='Drottningen bland de levantinska fattehrätterna och en klassisk rätt från Damaskus: små auberginer '
                   'fyllda med köttfärs och pinjenötter, serverade på rostat bröd med en sås av yoghurt, tahini och '
                   'vitlök. Den mäktiga kombinationen med mycket protein och fett bromsar upptaget av brödet, med ett lågt '
                   'glykemiskt index (55).',
              tips=('Ät en måttlig portion med sked som en härlig huvudrätt, börja gärna med en grön sallad för att fylla '
                    'magen, och låt köttet och yoghurten stå för mättnaden.',
                    'Rosta brödbitarna i ugnen utan att fritera dem, ugnsrosta auberginerna i stället för att dränka dem i '
                    'olja, och använd mager yoghurt blandad med lite naturlig tahini för färre kalorier.',
                    'Makdous-fatteh är en rik och komplett måltid med protein från kött och yoghurt och fibrer från '
                    'auberginen, och med en måttlig mängd rostat bröd påverkar den blodsockret måttligt.')),
    281: dict(lead='En ikon på det levantinska bordet vid högtider och fester: möra bitar av lammkött som får sjuda '
                   'långsamt i en yoghurtsås som redts med stärkelse och smaksatts med lök och aromatiska kryddor. Köttets '
                   'och yoghurtens protein ger rätten en djup mättnad och ett lågt glykemiskt index (50).',
              tips=('Fyll tallriken med köttbitar och varm yoghurtsås och nöj dig med 4–5 matskedar ris med vermicelli '
                    'till; den kokta yoghurten innehåller mycket protein.',
                    'Koka yoghurten med en mycket liten mängd majsstärkelse för att binda den, och använd köttets '
                    'naturliga kokspad med lök för en fyllig smak utan extra olja eller fett.',
                    'Shakriyyeh är en värmande rätt med kalcium och fullvärdigt protein, och att hålla en klok portion ris '
                    'till är hemligheten bakom att njuta av den utan trötthet efter maten.')),
    282: dict(lead='Kungen på bordet i Najd och den främsta traditionella rätten vid fester: krossat vete som får sjuda '
                   'långsamt i timmar med yoghurt och kött, toppat med musammana (en fräsning av lök, torkad lime och '
                   'ghee). Fullkornsvetet ger mycket fibrer som bromsar nedbrytningen och ger ett lågt glykemiskt index '
                   '(50).',
              tips=('Ät en måttlig portion med sked som huvudrätt till lunch, ta gärna en färsk grön sallad till, och nöj '
                    'dig med en lätt klick musammana på toppen för att undvika för mycket mättat fett.',
                    'Koka jareesh med naturell mager yoghurt eller filmjölk och bitar av magert kalvkött i stället för '
                    'fårfett, så får du en krämig, proteinrik konsistens med hälften så mycket fett.',
                    'Det krossade vetet smälts långsamt och mättar länge; vid diabetes och insulinresistens är en portion '
                    'på en kopp nyckeln till att njuta av rätten.')),
    283: dict(lead='Ett gästfrihetens mästerverk från södra Arabiska halvön: en rostad fullkornskaka som knådas med fin '
                   'dadelmassa och dränks i naturligt ghee, honung och grädde. En glädjefylld och mycket koncentrerad '
                   'kaloribomb med ett medelhögt glykemiskt index (68) och mycket hög glykemisk belastning och kalorihalt.',
              tips=('Areeka är en rätt att dela kalla morgnar och ingen vardagsmat för en person; nöj dig med tre till '
                    'fyra små tuggor som du äter långsamt, gärna med osötat, beskt arabiskt kaffe som bryter den '
                    'koncentrerade sötman.',
                    'Gör degen av fullkornsmjöl med kli, låt dadlarnas naturliga sötma räcka, och undvik att hälla extra '
                    'honung eller härdad grädde över fatet.',
                    'En rätt med mycket snabbt socker och fett; vid diabetes eller strikt viktnedgång bör den ätas med '
                    'stor försiktighet och sparsamt för att undvika kraftiga glukostoppar.')),
    284: dict(lead='Gyllene flingor som är omtyckta bland vegetarianer: inaktiva jästflingor (Saccharomyces cerevisiae) '
                   'med en smak som påminner om lagrad ost och nötter. Kolhydraterna i en portion är få, det glykemiska '
                   'indexet är inte tillämpligt, och flingorna innehåller mycket B-vitaminer och protein.',
              tips=('Strö en till två matskedar över soppor, sallader, rostade grönsaker eller popcorn; de ger en krämig '
                    'ostsmak.',
                    'Använd dem som avslutande krydda och undvik långvarig upphettning på mycket hög värme, så bevaras de '
                    'värmekänsliga B-vitaminerna som B12 och B6.',
                    'Ett bra sätt att berika måltider med zink, selen och betaglukaner; näringsjäst påverkar inte '
                    'blodsockret nämnvärt och är naturligt fri från mjölkprodukter.')),
    285: dict(lead='Den mest kända fermenterade produkten i dagens kostdebatt: ofiltrerad äppelcidervinäger med "moder" '
                   '(en hinna av bakterier och enzymer från jäsningen). Inga kolhydrater, och det glykemiska indexet är '
                   'inte tillämpligt.',
              tips=('Om du vill dricka den, späd alltid en matsked i ett glas ljummet vatten och drick med sugrör.',
                    'Använd den i dagliga salladsdressingar med extra jungfruolivolja och vitlök; det ger en frisk '
                    'syrlighet så att du kan minska på salt och färdiga såser.',
                    'Drick aldrig äppelcidervinäger outspädd, för att skydda tandemaljen och matstrupens slemhinna, och '
                    'den som har aktivt magsår bör undvika den på tom mage.')),
    286: dict(lead='Det praktiska mellanmålet för kontorsarbetare och idrottare en hektisk dag: en proteinbar täckt med '
                   'choklad och sockerfri kola. Det glykemiska indexet är lågt (35) tack vare den höga andelen protein och '
                   'fibrer, vilket gör den till ett smart alternativ till vanlig choklad.',
              tips=('Ät den som ett mellanmål i nödfall på resor eller efter träning när hungern kommer plötsligt; protein '
                    'bidrar till att bibehålla muskelmassan, men låt den inte ersätta vanliga, kompletta måltider.',
                    'Läs etiketten noga: välj bars med vassle- eller mjölkprotein, sötade med sötningsmedel som stevia '
                    'eller erytritol och utan härdad palmolja.',
                    'Vissa proteinbars innehåller sockeralkoholer (polyoler som maltitol), som kan ge uppblåsthet och '
                    'gaser hos känsliga personer, så en bar om dagen är det bästa valet.')),
    287: dict(lead='En dröm för den som äter keto eller inte tål vete: bröd bakat på mandelmjöl, linfrön, psylliumskal och '
                   'ägg. Nettokolhydraterna är nära noll och det glykemiska indexet är inte tillämpligt, så brödet '
                   'påverkar inte blodsockret nämnvärt.',
              tips=('Använd en rostad skiva till en smörgås med ägg eller avokado och ost; den ger brödets konsistens och '
                    'känsla utan ett enda korn raffinerad stärkelse.',
                    'Rosta skivan väl i brödrosten före servering för en stadigare konsistens och god nötsmak, och drick '
                    'ett glas vatten till så att psylliumfibrerna kan svälla.',
                    'Ketobröd innehåller fett och lösliga fibrer men är kaloritätt, så en till två skivor räcker gott för '
                    'mättnaden utan att vikten står still.')),
    288: dict(lead='Det vanliga alternativet till traditionell pasta, gjort på en blandning av ris- och majsmjöl för '
                   'personer med celiaki eller veteallergi. Den viktigaste frågan är om glutenfri pasta påverkar '
                   'blodsockret mindre. Svaret är överraskande: nej, ris- och majsstärkelse bryts ned snabbare än '
                   'stärkelsen i durumvete, och det glykemiska indexet är medelhögt (62).',
              tips=('Ät den inte ensam; kombinera den alltid med rikligt med protein (som köttfärs eller kycklingbröst), '
                    'bladgrönsaker och tomatsås för att bromsa upptaget av risstärkelsen.',
                    'Håll noga koll på koktiden och koka den al dente; glutenfri pasta blir snabbt mjuk och får då ett '
                    'högre glykemiskt index om den kokas för länge.',
                    'Vid diabetes utan glutenintolerans är vanlig fullkornspasta eller pasta av lins- och kikärtsmjöl ett '
                    'betydligt bättre val för blodsockret än pasta av ris och majs.')),
    289: dict(lead='Den tjocka, rubinröda vätskan som ger de levantinska rätterna deras djupa syrlighet: naturlig '
                   'granatäpplejuice som kokas ned långsamt. Även utan tillsatt vitt socker koncentreras fruktens '
                   'naturliga socker, och det glykemiska indexet är lågt (55), så sirapen bör användas medvetet.',
              tips=('Använd en tesked (cirka 5–10 ml) för att smaksätta sallader som hummus och fattoush eller lever- och '
                    'kötträtter; du får en oemotståndlig smak med minsta möjliga mängd socker.',
                    "Läs ingrediensförteckningen och köp alltid ren sirap märkt '100 % granatäpplejuice', och undvik "
                    'billiga produkter som blandar citronsyra med raffinerat socker och karamellfärg.',
                    'Granatäpplesirap innehåller polyfenoler, och i små mängder i matlagningen påverkar den inte '
                    'blodsockret nämnvärt.')),
    290: dict(lead='Kärnan i den östasiatiska smaken (umami) i en flaska: sojabönor, vete, vatten och salt som fått jäsa '
                   'naturligt i många månader. Eftersom den används i teskedsmängder i matlagningen är kolhydraterna '
                   'mycket få och det glykemiska indexet är inte tillämpligt, och den ger en djup smak som gör att du kan '
                   'minska på salt och fett.',
              tips=('Använd några droppar för att smaksätta wokade grönsaker, fisk och asiatiska soppor och bryt '
                    'enformigheten i bantningskosten utan att tillsätta socker eller fett.',
                    'Välj alltid naturligt bryggd sojasås (naturally brewed) och undvik sojasås som framställts genom '
                    'snabb kemisk hydrolys, och välj gärna varianten med reducerad salthalt.',
                    'Sojasås tillför inga nämnvärda kalorier eller stärkelse men innehåller mycket salt, så personer med '
                    'högt blodtryck bör använda den med måtta och inte tillsätta salt i samma rätt.')),
    291: dict(lead='Världens mest kända thailändska chilisås: mosad röd chili med vitlök, vinäger och socker. Den ger '
                   'rätterna en härlig hetta, det glykemiska indexet är lågt (35), men det tillsatta sockret kräver att '
                   'portionen mäts i teskedar.',
              tips=('Lägg en tesked över äggrätter, grillad kyckling eller nudlar för en frisk, het skärpa som kan ersätta '
                    'majonnäs och feta såser.',
                    'Tänk på mängden: färdig sriracha innehåller cirka 1 g socker per tesked, så använd den droppvis som '
                    'smaksättning och inte som dipp.',
                    'Om du har känslig mage eller halsbränna är det bäst att använda mycket lite, så slipper du besvär.')),
    292: dict(lead='Den omtyckta följeslagaren till smörgåsar och shawarma: små krispiga gurkor fermenterade i en lag av '
                   'vatten, salt, vitlök och dill. Nettokolhydraterna är nästan noll, det glykemiska indexet är inte '
                   'tillämpligt, och den naturliga jäsningen gör att de innehåller mjölksyrabakterier.',
              tips=('Ät en till två krispiga gurkor till mättande luncher; syrligheten och krispigheten friskar upp '
                    'smaklökarna och kan minska suget efter något sött efter maten.',
                    'Välj helst hemgjord inlagd gurka fermenterad med naturligt havssalt utan tillsatt socker eller '
                    'kemiska konserveringsmedel, och skölj den i kallt vatten om du vill minska saltet på ytan.',
                    'Inlagd gurka tillför nästan inga kalorier och påverkar inte blodsockret, men den höga salthalten '
                    'kräver strikt måtta vid högt blodtryck och vätskeansamling.')),
    293: dict(lead='Greklands glänsande pärla med mörklila färg, mandelform och fyllig, fruktig smak; oliverna innehåller '
                   'oljesyra och hydroxityrosol. Kolhydraterna är nästan obefintliga, det glykemiska indexet är inte '
                   'tillämpligt, och oliverna är en grundpelare i medelhavskosten.',
              tips=('Lägg 4–5 oliver i den dagliga gröna salladen eller på frukosttallriken; det enkelomättade fettet '
                    'bromsar nedbrytningen av kolhydraterna och gör måltiden mer mättande.',
                    'Välj oliver i extra jungfruolivolja och vinäger och undvik oliver behandlade med natronlut, och lägg '
                    'dem gärna i ljummet vatten före servering för att minska saltet.',
                    'Kalamataoliver innehåller mycket omättat fett; att ersätta mättat fett med omättat fett i kosten '
                    'bidrar till att bibehålla normala kolesterolhalter i blodet, och med måtta påverkar oliverna inte '
                    'blodsockret.')),
    294: dict(lead='Världens mest konsumerade alkoholhaltiga dryck, gjord av jäst korn och humle. Den viktigaste '
                   'fysiologiska frågan är hur öl påverkar blodsockret. Det glykemiska indexet är inte tillämpligt på '
                   'grund av alkoholen, men maltosen och alkoholens tomma kalorier gör att öl lätt leder till mer fett i '
                   'levern och runt magen.',
              tips=('Ur folkhälsosynpunkt rekommenderas att avstå eller välja alkoholfria alternativ; alkohol hämmar '
                    'fettförbränningen och belastar levern.',
                    'Om du dricker öl, drick det aldrig på tom mage och drick dubbelt så mycket vatten för att minska '
                    'uttorkningen.',
                    '⚠️ Viktig klinisk varning: alkohol hämmar leverns nybildning av glukos (glukoneogenes), vilket '
                    'utsätter personer med diabetes som tar insulin eller sulfonylureider för risk för plötsligt och '
                    'kraftigt blodsockerfall flera timmar efter att de druckit.')),
    295: dict(lead='Drycken som jäses av röd druvsaft och som i forskningen är känd för att innehålla resveratrol och '
                   'polyfenoler från druvskalen. Restsockret är lågt och det glykemiska indexet är inte tillämpligt, men '
                   'energin kommer helt från alkoholen.',
              tips=('Ur klinisk synvinkel rekommenderas aldrig att börja dricka alkohol som behandling eller för hälsans '
                    'skull; alkoholens skador på levern och dess giftighet väger tyngre än någon förmodad fördel med '
                    'resveratrol, som också finns i druvor och bär.',
                    'Polyfenolerna i vin finns också i färska röda druvor med skal, och du kan dricka hibiskuste eller äta '
                    'tranbär helt utan alkohol.',
                    '⚠️ Läkemedels- och klinisk varning: alkohol belastar leverns enzymer och samverkar farligt med '
                    'läkemedel mot högt blodtryck, diabetes och smärta; gravida, ammande och personer med fettlever ska '
                    'inte dricka alkohol.')),
    296: dict(lead='Den svarta folkliga drycken med lång tradition i Egypten och Levanten: ett extrakt av naturlig '
                   'lakritsrot med tjockt skum och unik sötma. Det glykemiska indexet är lågt (35), och sötman kommer inte '
                   'från socker utan från det naturliga, mycket söta ämnet glycyrrhizin.',
              tips=('Endast för friska personer: ett litet kallt glas, och undvik att dricka det upprepade gånger under '
                    'dagen.',
                    'Låt pulver av lakritsrot dra med en nypa natriumbikarbonat i rent vatten och sila genom ren gasväv, '
                    'och tillsätt inget vitt socker; den naturliga sötman är cirka 50 gånger starkare än socker.',
                    '⚠️ Mycket viktig klinisk varning: glycyrrhizin hämmar ett enzym i njurarna och ger kraftig ansamling '
                    'av natrium och vatten och förlust av kalium; drycken får inte drickas av personer med högt blodtryck, '
                    'hjärtsjukdom eller njursvikt eller av gravida, eftersom blodtrycket kan stiga farligt.')),
    297: dict(lead='Ett naturligt, svalkande rubinrött te: torkade röda hibiskusblad som dragit, med en härligt syrlig '
                   'smak som påminner om bär. Inga kolhydrater och inget socker i sin naturliga form, och det glykemiska '
                   'indexet är inte tillämpligt.',
              tips=('Drick ett stort glas med is på sommaren som ett smart alternativ till sötade juicer och läsk; det '
                    'släcker törsten och svalkar direkt utan kalorier.',
                    'Låt hibiskusbladen dra i kallt vatten i flera timmar (kallbryggning), så bevaras C-vitaminet, och '
                    'drick det osötat eller med några droppar stevia.',
                    'Osötat hibiskuste påverkar inte blodsockret och passar vid diabetes.')),
    298: dict(lead='Fina gyllene kamomillblommor som många hem tar till på kvällen: ett örtte med ämnet apigenin. Inga '
                   'kalorier, inga kolhydrater, och det glykemiska indexet är inte tillämpligt.',
              tips=('Drick en varm kopp en halvtimme före sänggåendet eller efter en mäktig middag.',
                    'Låt kamomillblommorna dra i nykokt vatten i 7–10 minuter med ett tättslutande lock över koppen, så '
                    'att de fina aromatiska oljorna och flavonoiderna inte avdunstar.',
                    'God sömn är en viktig grund för ett stabilt blodsocker på morgonen.')),
    299: dict(lead='Den äkta orientaliska kaffestunden med en liten kopp och ett djupt, sammetslent skum: mycket finmalet '
                   'kaffe som får koka långsamt med lite mald kardemumma. Inga kolhydrater och nästan inga kalorier när '
                   'det dricks utan socker, det glykemiska indexet är inte tillämpligt, och kaffet innehåller '
                   'klorogensyra.',
              tips=('Drick din lilla kopp på morgonen eller eftermiddagen, och alltid utan socker för att njuta av den '
                    'fina beskheten.',
                    'Koka kaffet med kallt vatten och kardemumma på mycket låg värme (i en cezve av koppar) tills skummet '
                    'bildas och stiger försiktigt utan att koka över, så bevaras kaffets fylliga oljor.',
                    'Att undvika skedar av raffinerat socker i koppen är det som gör turkiskt kaffe till en dryck som inte '
                    'påverkar blodsockret.')),
    300: dict(lead='Marockos klassiska atay och en symbol för generositet och gästfrihet: grönt krutte (gunpowder) som '
                   'kokas och blandas med buketter av färsk, aromatisk mynta. Teet innehåller inga kalorier i sin '
                   'naturliga form, det glykemiska indexet är inte tillämpligt, och det innehåller katekiner, bland annat '
                   'EGCG.',
              tips=('Njut av en varm kopp efter en mäktig lunch.',
                    'Be alltid om teet utan socker på kafé; traditionellt läggs stora mängder sockerbitar i kannan, medan '
                    'du hemma med naturlig mynta får all smak utan socker.',
                    'Osötat grönt te med mynta är en dryck som passar varje dag och påverkar inte blodsockret.')),
    # foods 301-400: translated from the approved Arabic copy (2026-10-24, four checked blocks of 25)
    301: dict(lead='Vinterns stolthet i Nederländerna och en av de mest omtalade bladgrönsakerna: krusiga, mörkgröna '
                   'grönkålsblad med K-, A- och C-vitamin och kalcium. Nettokolhydraterna är mycket låga och det '
                   'glykemiska indexet är inte tillämpligt.',
              tips=('En grundingrediens i holländsk stamppot eller finskuren i sallader; den mättar väl och påverkar inte '
                    'blodsockret negativt.',
                    'Massera den hackade grönkålen med olivolja, citron och lite salt i två minuter så att bladen mjuknar '
                    'i salladen, eller ångkoka den några minuter.',
                    'Grönkål innehåller glukosinolater och passar utmärkt utan begränsning vid diabetes och viktkontroll.')),
    302: dict(lead='Eleganta små kålhuvuden som hör hemma på det europeiska vinterbordet: krispiga gröna bollar som '
                   'förenar kålens milda sötma med en rostad nötsmak när de ugnsrostas. Nettokolhydraterna är låga, det '
                   'glykemiska indexet är inte tillämpligt, och brysselkål är en god källa till fibrer och folat.',
              tips=('Ett utmärkt tillbehör till grillad fisk och kött; fibrerna fyller magen snabbt och ger en jämnare '
                    'blodsockerkurva efter måltiden.',
                    'Halvera kålhuvudena och rosta dem i ugnen med olivolja, krossad vitlök och lite svartpeppar tills '
                    'kanterna blir bruna och krispiga; rostningen karamelliserar sockret och tar bort beskan.',
                    'Brysselkål innehåller naturliga svavelföreningar och lösliga fibrer.')),
    303: dict(lead='Den traditionella vardagsdrycken i Nederländerna och norra Europa: naturligt syrad mjölk med en frisk, '
                   'syrlig smak och lätt tjock konsistens. Fetthalten är mycket låg och det glykemiska indexet är lågt '
                   '(30), och kärnmjölken innehåller mjölksyrabakterier och kalcium.',
              tips=('Drick ett kallt glas till lunch eller som ett mättande mellanmål på eftermiddagen.',
                    'Drick den kall och omskakad som den är utan smaksättning eller tillsatt socker, eller använd den som '
                    'ett mildare alternativ till grädde i soppor och dressingar.',
                    'Mjölksyrabakterierna förbrukar en stor del av laktosen under tillverkningen, och kärnmjölken passar '
                    'bra vid diabetes och insulinresistens.')),
    304: dict(lead='Ett välkänt val bland idrottare och bantare i Tyskland och Nederländerna: en len färskost som påminner '
                   'om tjock grekisk yoghurt, med mycket protein (kasein) och nästan inget fett. Kolhydraterna är mycket '
                   'få och det glykemiska indexet är inte tillämpligt.',
              tips=('En perfekt skål till frukost eller före sänggåendet; kaseinet tas upp långsamt, protein bidrar till '
                    'att bibehålla muskelmassan, och kvargen mättar länge, även under natten.',
                    'Blanda den med några blåbär, lite kanel och en halv tesked chiafrön, så får du en lyxig proteinrik '
                    'efterrätt med krämig konsistens utan fett och fritt socker.',
                    'Fettfri kvarg ger cirka 11–12 g protein och bara 52 kcal per 100 g, ett av de bästa valen för mättnad '
                    'och viktkontroll.')),
    305: dict(lead='Den fylliga varianten av traditionell färskost (volle kwark), med sammetslen konsistens och naturlig '
                   'gräddighet. Kolhydraterna är mycket få och det glykemiska indexet är inte tillämpligt.',
              tips=('Ät en halv kopp som ett mättande mål vid lågkolhydratkost och keto; den mättar väl i många timmar.',
                    'Använd den som ett lyxigt alternativ till majonnäs och industriell färskost i såser och som dipp till '
                    'färska grönsaker med vitlök och örter som dill och mynta.',
                    'Fullfet kvarg innehåller kalcium, fosfor och A- och D-vitamin; en måttlig portion gör att du inte får '
                    'i dig för mycket kalorier totalt.')),
    306: dict(lead='Det mörka traditionella brödet och det kompaktaste i Nederländerna och norra Europa (Fries '
                   'roggebrood): krossade hela rågkorn som bakas långsamt i många timmar utan vitt mjöl. Det innehåller '
                   'mycket fibrer och har ett lågt glykemiskt index (45) och smälts mycket långsamt.',
              tips=('En tunn skiva räcker gott; lägg en skiva lagrad holländsk ost eller ett kokt ägg med gurkskivor '
                    'ovanpå för en stabil start på dagen.',
                    'Det behöver inte rostas eftersom det är så fuktigt och kompakt; ät det färskt och njut av den '
                    'kompakta konsistensen som kräver ordentligt tuggande, och drick ett glas vatten eller varmt te till.',
                    'Grovt rågbröd är ett välkänt exempel på bröd som passar vid diabetes; de rikliga fibrerna dämpar '
                    'glukossvaret i många timmar.')),
    307: dict(lead='En symbol för den holländska gatan och sommarens favorit (Hollandse Nieuwe): rå, lätt saltad sill som '
                   'hålls i stjärten och äts i ett svep med hackad vit lök och inlagd gurka. Inga nettokolhydrater, det '
                   'glykemiska indexet är inte tillämpligt, och sill är en av de fetaste fiskarna med omega-3; EPA och DHA '
                   'bidrar till hjärtats normala funktion vid ett dagligt intag av 250 mg.',
              tips=('Ett snabbt och mättande mål; ät sillen som den är med hackad lök och undvik den i ett litet vitt bröd '
                    '(broodje haring), så slipper du raffinerad stärkelse.',
                    'Välj färsk sill under säsongen (juni och juli) och väl kyld; den hackade löken balanserar fiskens '
                    'fetma och ger fräschör.',
                    '⚠️ Säkerhetsvarning: sillen är rå och bara lätt saltad; den ska inte ätas rå av gravida, barn eller '
                    'personer med nedsatt immunförsvar på grund av risken för listeria och parasiter, och tänk på '
                    'salthalten om du har högt blodtryck.')),
    308: dict(lead='Den traditionella holländska vintersoppan som smälter frosten: en mycket tjock soppa på torkade gröna '
                   'ärter, selleri och purjolök med köttbitar och rökt korv. Ärterna ger komplexa kolhydrater med mycket '
                   'fibrer och vegetabiliskt protein, vilket ger soppan ett lågt glykemiskt index (40).',
              tips=('En komplett vinterlunch i sig; en skål mättar i flera timmar utan blodsockerfall, och om du äter den '
                    'med sked behöver du inget bröd till.',
                    'Låt ärterna sjuda långsamt tills de faller sönder och ger soppan dess traditionella tjocka konsistens '
                    '(där skeden ska stå upprätt), och använd magert kalvkött och mindre korv för mindre mättat fett och '
                    'salt.',
                    'Ärtsoppan innehåller mycket lösliga fibrer och zink; drick rikligt med vatten, så hanterar magen '
                    'baljväxternas fibrer lättare.')),
    309: dict(lead='Nederländernas folkliga nationalrätt: potatismos med krusig grönkål, traditionellt serverad med en '
                   'rökt korv. Grönkålen tillför fibrer som bromsar upptaget av potatisstärkelsen, vilket ger rätten ett '
                   'medelhögt glykemiskt index (58).',
              tips=('Vänd på den klassiska balansen: låt den gröna grönkålen dominera (ungefär två tredjedelar av '
                    'tallriken) med en måttlig mängd potatismos, och ät bara en halv korv för mindre mättat fett.',
                    'Ångkoka grönkålen och mosa den försiktigt med kokt potatis och lite olivolja eller kärnmjölk i '
                    'stället för stora mängder smält smör.',
                    'Grönkål innehåller K- och C-vitamin och vegetabiliskt kalcium; att vara måttlig med potatismoset är '
                    'hemligheten vid diabetes och viktkontroll.')),
    310: dict(lead='Den värmande holländska klassikern med lång historia: en balanserad blandning av söta vintermorötter, '
                   'karamelliserad lök och potatis som mosas tillsammans och serveras med långkokt nötkött (klapstuk). '
                   'Morötternas naturliga sötma och potatisstärkelsen ger ett medelhögt glykemiskt index (60), så '
                   'portionen behöver planeras.',
              tips=('Servera hutspot med en rejäl bit kokt nötkött eller grillat kycklingbröst; köttets protein bromsar '
                    'upptaget av stärkelsen och sockret från morötter och potatis.',
                    'Mosa inte grönsakerna till en puré; låt morots- och potatisbitarna vara grova (stamppot rustiek), '
                    'eftersom en grövre konsistens smälts långsammare och mättar mer.',
                    'Morötter innehåller mycket betakaroten; om du håller koll på blodsockret räcker en portion i storlek '
                    'med en knytnäve.')),
    311: dict(lead='Den mest exklusiva och kända havsdelikatessen i holländska kustbyar som Volendam: ål rökt över ekved '
                   'tills köttet blir smörigt och mjukt med en förtrollande rökig smak. Inga kolhydrater, det glykemiska '
                   'indexet är inte tillämpligt, och ål innehåller protein, A- och D-vitamin och omega-3-fett.',
              tips=('En liten bit ålfilé räcker gott som en proteinrik och fet måltid; ät den med krispiga gurkskivor '
                    'eller på en skiva ketobröd eller fullkornsbröd.',
                    'Dra av det tunna skinnet och ät ålen kyld med lite pressad citron för att balansera den mycket '
                    'fylliga smaken, och undvik att steka den eller servera den med feta såser.',
                    'Ål är naturligt mycket fet; en liten portion (cirka 50–70 g) ger de fettlösliga vitaminerna utan att '
                    'kännas tung.')),
    312: dict(lead='Det populäraste mellanmålet på de holländska fiskmarknaderna: möra bitar av vit torsk (kabeljauw) i '
                   'smet, friterade tills de blir gyllene och krispiga, med fiskkryddor och vit sås (ravigottesås). '
                   'Torsken är rent havsprotein, men smeten höjer det glykemiska indexet till cirka 35.',
              tips=('Njut av en liten portion med gaffel som en trevlig fisklunch, och doppa gaffeln lätt i vitlöks- eller '
                    'tartarsås i stället för att dränka bitarna i färdig sås.',
                    'Det bästa alternativet: be om grillad torsk (gebakken vis) utan smet, eller kibbeling gjord i '
                    'airfryer, så slipper du mycket frityrfett.',
                    'Torsk innehåller fullvärdigt protein och jod och är i sig mager; för dig som håller koll på vikten '
                    'och blodsockret håller måtta med de friterade bitarna och en grön sallad till måltiden i balans.')),
    313: dict(lead='Det mest kända bakverket i Nederländernas historia och landets ambassadör i världen: två tunna, '
                   'krispiga våffelkakor med en varm fyllning av farinsockerkola, kanel och smör. Stroopwafel har ett högt '
                   'glykemiskt index (72) och är en koncentrerad sötsak som kräver stor medvetenhet om storleken.',
              tips=('Njut av en liten som ett genomtänkt undantag en gång i veckan; det klassiska holländska sättet är att '
                    'lägga den på en kopp varmt, svart kaffe i en minut så att kolafyllningen smälter av ångan, och sedan '
                    'äta den mycket långsamt.',
                    'Undvik stora stroopwafels (mega stroopwafel) täckta med choklad och nötter, och nöj dig med den lilla '
                    'traditionella storleken (mini) efter en komplett, fiberrik måltid.',
                    'En enda kaka innehåller mycket enkla sockerarter som tas upp snabbt, så den passar inte för dagligt '
                    'bruk vid diabetes eller viktnedgång.')),
    314: dict(lead='De små, luftiga pannkakorna som säljs i holländska vinterstånd: de gräddas av bovete- och vetemjöl med '
                   'jäst i särskilda kopparformar och serveras dränkta i smör och florsocker. Det glykemiska indexet är '
                   'medelhögt (68), och de ger snabb kolhydratenergi.',
              tips=('En efterrätt att dela med familjen på utflykter; nöj dig med 4–5 små pannkakor och undvik att äta '
                    'hela tallriken själv, så slipper du kraftiga blodsockertoppar och trötthet.',
                    'Be om dem med lite naturligt smör och så lite florsocker som möjligt, och toppa gärna med några '
                    'färska tranbär för fibrernas skull.',
                    'Bovetet i degen tillför vissa mineraler, men florsockret och det rikliga smöret gör dem till en '
                    'kaloririk rätt som kräver strikt måtta.')),
    315: dict(lead='Det traditionella högtidskexet med vackra mönster från trädformar och spröd krispighet, kryddat med '
                   'kanel, muskotnöt, kryddnejlika, ingefära och farinsocker. Det glykemiska indexet är medelhögt (65), '
                   'och kryddorna är hemligheten bakom doften och vintersmaken.',
              tips=('Ett krispigt kex till en kopp svart te eller kaffe utan socker räcker gott för att stilla '
                    'förmiddagens sötsug.',
                    'Välj kex bakade på fullkornsmjöl och naturligt smör i stället för härdade vegetabiliska oljor, och '
                    'undvik varianten fylld med söt mandelmassa (gevulde speculaas) utom vid sällsynta tillfällen.',
                    'Socker och vitt mjöl gör kexet till en sötsak som ska räknas in i dagens totala kalorier.')),
    316: dict(lead='Små, krispiga runda kakor som barn och vuxna i Nederländerna älskar under vintersäsongen: kulor '
                   'kryddade med kanel, ingefära och farinsocker. Det glykemiska indexet är medelhögt (67), och de små '
                   'kakorna gör det lätt att äta stora mängder utan att märka det.',
              tips=('Bestäm portionen i förväg genom att lägga en liten näve (cirka 10–15 st) på ett litet fat och ställ '
                    'undan den stora påsen, så njuter du av smaken och krispigheten medvetet.',
                    'Undvik kruidnoten doppade i vit choklad eller saltkola; den traditionella naturella varianten '
                    'innehåller betydligt mindre socker och kalorier.',
                    'Koncentrerade sockriga och stärkelserika kakor som smälts snabbt; för dig som håller koll på vikten '
                    'och blodsockret är portionen avgörande, så att dolda kalorier inte samlas på hög medan man sitter och '
                    'pratar.')),
    317: dict(lead='Den självklara stjärnan bland smårätterna på holländska kaféer och sammankomster: krispiga kulor av '
                   'ströbröd med en het och god fyllning av tjock, kryddad nötköttsgryta. Köttets protein och fett bromsar '
                   'upptaget av det stärkelserika ströbrödshöljet, med ett lågt glykemiskt index (55).',
              tips=('Ät två till tre varma bitterballen som smårätt och doppa dem i stark gul senap (mosterd); senapen är '
                    'fri från socker och ger en skarp smak.',
                    'Var försiktig med första tuggan eftersom fyllningen är mycket varm, och gör dem gärna i airfryer för '
                    'samma krispighet med hälften så mycket uppsuget fett.',
                    'Friterade smårätter med mycket fett och salt; gör dem till ett trevligt undantag vid sociala '
                    'tillfällen och balansera dem med dagens övriga måltider.')),
    318: dict(lead='Storasyster till bitterballen och den mest sålda snabbmaten i holländska automater och kaféer: en '
                   'krispig cylinder fylld med redd sås och mört, kryddat nötkött. Det glykemiska indexet är lågt (55), '
                   'och kroketten ger en fyllig smakupplevelse.',
              tips=('Ät en krokett med gaffel tillsammans med en grön sallad och lite naturlig senap, och undvik den i ett '
                    'mjukt vitt bröd med smör (broodje kroket), så slipper du dubbelt med raffinerad stärkelse.',
                    'Välj kroketter av rent nötkött (rundvlees), grädda dem i airfryer för att minska det uppsugna '
                    'frityrfettet, och ät långsamt.',
                    'En friterad, kalori- och salttät rätt; en krokett räcker gott för att bli mätt och smaka på den '
                    'holländska klassikern.')),
    319: dict(lead='Det mest ätna folkliga mellanmålet i Nederländerna: kryddad köttfärs formad till korvar utan skinn, '
                   'friterade eller grillade tills de blir stadiga och mörka. Kolhydraterna är mycket få (cirka 6 g per '
                   '100 g från bindande stärkelse) och det glykemiska indexet är lågt (25) jämfört med annan snabbmat.',
              tips=('Välj grillad frikandel och ät den naturell eller med lite senap, och undvik frikandel speciaal med '
                    'tjock majonnäs, söt currysås och lök.',
                    'Grilla frikandellerna eller gör dem i airfryer utan extra olja; köttet släpper sitt eget fett och får '
                    'en lätt krispighet.',
                    'Frikandel är bearbetat kött med salt, mättat fett och kryddor och passar därför inte som vardagsmat '
                    'för barn eller personer med hjärtsjukdom, men den är ett snabbt alternativ med lite stärkelse när det '
                    'behövs.')),
    320: dict(lead='Amsterdams traditionella korv med anor: rå, malen nötfärs kryddad med muskotnöt, kryddnejlika och '
                   'vitpeppar och lätt kallrökt. Inga nettokolhydrater, det glykemiska indexet är inte tillämpligt, och '
                   'korven innehåller protein, järn och B-vitaminer.',
              tips=('Ät några tunna skivor som en del av en kall smårättstallrik med inlagd gurka och stark holländsk '
                    'senap; korven ger en omedelbar proteinrik mättnad.',
                    'Köp den mycket färsk från en pålitlig slaktare (keurslager), förvara den i kylskåp och ät den inom '
                    'högst två dagar, och låt den inte stå i rumstemperatur.',
                    '⚠️ Viktig klinisk varning: ossenworst är helt rått nötkött; den får inte ätas av gravida, små barn '
                    'eller personer med nedsatt immunförsvar på grund av risken för E. coli och toxoplasma.')),
    321: dict(lead='Det mest efterfrågade pålägget på holländska frukost- och lunchbord: mycket finmald rå nötfärs blandad '
                   'med majonnäs, senap och paprikapulver. Kolhydraterna är nästan obefintliga (cirka 2 g) och det '
                   'glykemiska indexet är inte tillämpligt, och pålägget innehåller protein.',
              tips=('Bred en matsked på en skiva fullkornsbröd eller ketobröd och toppa med hackad lök och kokt ägg för en '
                    'mättande lunch.',
                    'Förvara förpackningen i kylskåp vid 4 °C och ät den direkt efter öppning, och välj varianter utan '
                    'tillsatt socker eller kemiska smakförstärkare.',
                    '⚠️ Strikt klinisk varning: filet americain är 100 % rått nötkött; det får inte ätas av gravida, '
                    'ammande eller personer som får immunhämmande behandling, för att undvika risken för allvarliga '
                    'bakterie- och parasitinfektioner.')),
    322: dict(lead='Den berömda runda osten med blankt rött vaxhölje från staden Edam, med mild smak och mjuk, halvfast '
                   'konsistens. Nettokolhydraterna är nära noll och det glykemiska indexet är inte tillämpligt; en '
                   'medelfet ost med kalcium och fullvärdigt protein.',
              tips=('En eller två skivor till frukost eller som mellanmål med några vindruvor eller valnötter; osten ger '
                    'en lugn mättnad och innehåller ingen stärkelse.',
                    'Ta bort det röda, oätliga vaxhöljet och ät osten i rumstemperatur, så kommer den milda, smöriga '
                    'smaken fram.',
                    'Edamerost är mindre fet än gouda och innehåller fosfor och zink, ett bra val vid viktkontroll och '
                    'diabetes eftersom den mättar utan kolhydrater.')),
    323: dict(lead='Kronan bland de holländska ostarna (oude kaas): äkta gouda som lagrats tålmodigt i mer än 10–12 '
                   'månader tills krispiga kristaller bildats och osten fått en djup, skarp kolasmak. Inga kolhydrater, '
                   'nästan ingen laktos, och det glykemiska indexet är inte tillämpligt.',
              tips=('Små tärningar som en lyxig proteinrik efterrätt eller smårätt med lite senap; den intensiva smaken '
                    'gör att man snabbt känner sig mätt och nöjd.',
                    'Skär den i små tärningar med en kniv för hårdost och servera med oliver och valnötter i stället för '
                    'med salta vita kex.',
                    'Den långa lagringen bryter ned laktosen nästan helt, så lagrad gouda passar ofta även personer med '
                    'laktosintolerans, och osten innehåller K2-vitamin.')),
    324: dict(lead='Den traditionella osten från staden Leiden: en halvfast ost med hela, aromatiska spiskumminfrön som '
                   'ger en varm, jordig smak. Kolhydraterna är mycket få och det glykemiska indexet är inte tillämpligt.',
              tips=('En smakrik skiva på morgonens smörgås eller som mellanmål; spiskumminfröna ger en aromatisk smak som '
                    'minskar behovet av salt.',
                    'Tugga ostbitarna väl så att de aromatiska oljorna i kumminfröna frigörs, och njut av osten med en '
                    'kopp grönt te eller svart kaffe.',
                    'Leidenost görs traditionellt av delvis skummad mjölk och är därför mindre fet och kaloririk än vanlig '
                    'gouda, vilket passar dig som håller koll på blodfetterna och vikten.')),
    325: dict(lead='En mjuk vit ost gjord av färsk holländsk getmjölk, med krämig mjölksmak, mild syrlighet och en '
                   'konsistens som smälter i munnen. Nettokolhydraterna är mycket låga och det glykemiska indexet är inte '
                   'tillämpligt.',
              tips=('Smula en matsked över en sallad med ruccola, rödbetor och valnötter; fettet och proteinet bromsar '
                    'upptaget av salladens stärkelse och gör måltiden både lyxig och mättande.',
                    'Grädda en liten getostrundel i ugnen några minuter tills mitten smälter, toppa med lite vild timjan '
                    'och undvik att hälla tjock honung över, så hålls sockret nere.',
                    'Fettet i getmjölk innehåller en högre andel medellånga fettsyror (MCT) och mindre fettkulor; vissa '
                    'som är känsliga för ost av komjölk tycker att getost är ett bra alternativ.')),
    326: dict(lead='Den vanligaste vardagsefterrätten i holländska kylskåp: en tjock, len mjölkkräm med vaniljsmak som '
                   'hälls upp kall efter middagen. Den innehåller mjölk, stärkelse och socker och har ett medelhögt '
                   'glykemiskt index (62), så portionen bör mätas med sked.',
              tips=('Ät en halv liten kopp som ett undantag efter en komplett huvudmåltid, och toppa med några färska bär '
                    'och en nypa kanel för mer fibrer och en lugnare matsmältning.',
                    "Välj varianter märkta 'halvfet och utan tillsatt socker' (vla 0 % suiker toevoeging), eller gör den "
                    'hemma med mjölk, lite stärkelse, ett sötningsmedel och ren vaniljextrakt.',
                    'Traditionell vla innehåller mycket flytande socker som tas upp snabbt, så vid diabetes eller strikt '
                    'bantning bör den ätas medvetet och de osötade alternativen väljas.')),
    327: dict(lead='Den berömda nationaldrycken i gul förpackning: mjölk med tjock choklad och kakao som dricks kall på '
                   'sommaren eller varm med grädde på vintern. Det glykemiska indexet är lågt (50) tack vare mjölkens '
                   'protein och fett, men drycken innehåller mycket tillsatt socker som tas upp snabbt.',
              tips=('För aktiva personer och idrottare: ett litet glas efter hård fysisk träning fyller snabbt på '
                    'glykogenet och ger protein för återhämtningen, men den passar inte som daglig dryck för den som rör '
                    'sig lite.',
                    "Välj varianten märkt '0 % suiker' eller halvfet; den ger samma fylliga chokladsmak med hälften så "
                    'mycket socker och kalorier.',
                    'Kakao innehåller flavonoider, men det tillsatta sockret i den traditionella drycken gör den '
                    'energirik, så den kräver strikt måtta vid diabetes och insulinresistens.')),
    328: dict(lead='Det traditionella mörka pålägget i Nederländerna: en tjock sirap som kokas av äppeljuice och '
                   'sockerbetor i många timmar och som innehåller järn. Det glykemiska indexet är medelhögt (58), och '
                   'sirapen är ett fint alternativ till sylt och chokladpålägg.',
              tips=('Bred ett tunt lager (en tesked) på en skiva mörkt bröd med en skiva holländsk gouda; den kända '
                    'holländska kombinationen förenar järn, kalcium och protein.',
                    "Välj traditionella varianter som 'Rinsche appelstroop' med mild och ren syrlighet utan tillsatt "
                    'majssirap, och nöj dig med ett tunt lager som täcker brödet.',
                    'Äppelsirapen innehåller järn, men tänk på att räkna in det naturliga sockret om du håller koll på '
                    'blodsockret.')),
    329: dict(lead='Spröda, runda skorpor som inte saknas på något holländskt frukostbord (beschuit): de gräddas två '
                   'gånger tills de blir mycket krispiga och luftiga. Skorpor av fullkornsvete innehåller kli, men den '
                   'spröda konsistensen ger ett medelhögt glykemiskt index (68).',
              tips=('Ät en eller två skorpor med vit ost eller naturligt jordnötssmör utan socker; proteinet och fettet '
                    'bromsar upptaget av skorpans stärkelse.',
                    'Välj alltid skorpor av 100 % fullkornsvetemjöl (volkoren) och undvik vanliga vita skorpor, som snabbt '
                    'bryts ned till socker i munnen.',
                    'En skorpa ger cirka 40 kcal; ett praktiskt och krispigt alternativ på morgonen, förutsatt att du äter '
                    'protein till så att du inte blir hungrig igen snabbt.')),
    330: dict(lead='Den traditionella bruna morgonkakan med smak av kanel, kryddnejlika och ingefära; den bakas '
                   'traditionellt på rågmjöl och innehåller nästan inget fett. Det glykemiska indexet är medelhögt (65); '
                   'trots den låga fetthalten och rågens fibrer sötas kakan med glukossirap eller honung.',
              tips=('En tunn skiva med lite naturligt smör till morgonkaffet; smörets fett kan bromsa upptaget av kakans '
                    'socker.',
                    "Välj varianter märkta 'minder suiker' eller volkoren ontbijtkoek, med mer rågfibrer och utan "
                    'överdrivet tillsatt socker.',
                    'Rågfibrerna mättar väl, men tänk på att den traditionella kakan innehåller mycket enkla sockerarter, '
                    'så storleken på skivan är viktig vid diabetes.')),
    331: dict(lead='Världens mest kända och kanske märkligaste holländska frukostritual: små avlånga chokladkorn strödda '
                   'över en smörad brödskiva. Den mörka varianten (puur) innehåller mer än 32 % äkta kakao och kakaosmör, '
                   'vilket ger ett lågt glykemiskt index (45).',
              tips=('En matsked strödd över fullkornsrostat bröd med naturligt smör räcker gott för att stilla morgonens '
                    'chokladsug medvetet och utan att överdriva.',
                    'Välj alltid mörkt chokladströssel (puur hagelslag) med mindre socker och mer kakao, och undvik '
                    'mjölkchoklad eller färgat sockerströssel (vruchtenhagel).',
                    'Kakaosmöret i mörk choklad bromsar sockerupptaget; med en måttlig mängd blir det en kontrollerad '
                    'holländsk njutning.')),
    332: dict(lead='Den italienska "ostarnas kung" (Parmigiano Reggiano SUB): en hårdost som lagras tålmodigt i två år '
                   'tills naturlig glutaminsyra och krispiga kristaller bildats. Inga nettokolhydrater, det glykemiska '
                   'indexet är inte tillämpligt, och osten innehåller mycket protein och ger en kraftfull smak utan att '
                   'påverka blodsockret.',
              tips=('Riv en matsked över pastarätter, soppor och bladsallader; fettet och proteinet bromsar upptaget av '
                    'måltidens stärkelse och ger en omedelbar känsla av mättnad.',
                    'Ät den i rumstemperatur i tunna flagor med lite traditionell balsamvinäger, och spara den hårda '
                    'parmesanskorpan att koka med i soppor för en djup umamismak.',
                    'Den långa lagringen i 24 månader bryter ned mjölksockret nästan helt, så osten är nästan laktosfri '
                    'och innehåller mycket kalcium.')),
    333: dict(lead='Roms gamla, historiska ost: den görs bara av helmjölk från får, saltas och lagras tills den får en '
                   'fast konsistens och en skarp, het och salt smak. Kolhydraterna är nästan obefintliga, det glykemiska '
                   'indexet är inte tillämpligt, och osten är grunden i klassiska romerska pastarätter som carbonara och '
                   'cacio e pepe.',
              tips=('En liten nypa riven ost räcker för att ge rätten en skarp smak; använd den som ett smart sätt att '
                    'minska vanligt salt.',
                    'Blanda den riven med nymalen svartpeppar och strö över rostade grönsaker eller äggrätter för mer smak '
                    'och mättnad.',
                    'Fårmjölk innehåller konjugerad linolsyra (CLA); eftersom osten är naturligt mycket salt bör personer '
                    'med högt blodtryck vara måttliga.')),
    334: dict(lead='Grekiska öarnas äkta skatt (feta SUB): en vit, mjuk och smulig ost gjord av fårmjölk med lite getmjölk '
                   'och lagrad i saltlake. Nettokolhydraterna är mycket låga, det glykemiska indexet är inte tillämpligt, '
                   'och fetaost är en grundpelare i medelhavskosten.',
              tips=('Smula en medelstor bit över den dagliga gröna salladen med olivolja och oliver; proteinet och fettet '
                    'bromsar nedbrytningen av måltiden.',
                    'Grädda en bit feta i ugnen med körsbärstomater, olivolja och lite oregano i några minuter tills den '
                    'mjuknar, så får du en varm dipp.',
                    'Om du håller koll på blodtrycket kan du lägga fetaosten i ljummet vatten en stund för att minska '
                    'saltet.')),
    335: dict(lead='Den franska mjuka "ostarnas drottning": en ätbar vit skorpa av penicilliummögel som omsluter ett '
                   'elfenbensfärgat inre som smälter som grädde med en fin, smörig och jordig smak. Inga kolhydrater, det '
                   'glykemiska indexet är inte tillämpligt, och osten innehåller fett, K2-vitamin och B12-vitamin.',
              tips=('En tunn skiva till frukost eller som mellanmål med några valnötter eller jordgubbar; den mättar väl '
                    'och ger en stor smakupplevelse utan blodsockertoppar.',
                    'Ta ut osten ur kylskåpet en halvtimme före servering, eftersom den krämiga konsistensen och smaken '
                    'bara kommer fram i rumstemperatur, och ät gärna den vita skorpan, som är ätlig.',
                    '⚠️ Säkerhetsvarning för gravida: brie av opastöriserad mjölk (au lait cru) ska inte ätas av gravida '
                    'på grund av risken för listeria. Livsmedelsverket avråder gravida från vit- och blåmögelost även av '
                    'pastöriserad mjölk, om osten inte har värmts ordentligt.')),
    336: dict(lead='Normandies stolthet i sin berömda träask: en mjuk ost med koncentrerad smak, jordig svampdoft och '
                   'sammetslen, fyllig konsistens. Nettokolhydraterna är nära noll och det glykemiska indexet är inte '
                   'tillämpligt, och osten innehåller protein och fett.',
              tips=('En liten bit räcker gott; ät den med gurkskivor eller på fullkornsrostat bröd för en proteinrik start '
                    'på dagen som håller hungern borta.',
                    'Grädda camemberten i asken i ugnen i 10 minuter efter att ha stuckit ned en vitlöksklyfta och en '
                    'rosmarinkvist, och doppa morots- och sellerstavar i den som en lyxig vintermiddag utan stärkelse.',
                    '⚠️ Varning för gravida: samma som för brie; osten ska vara gjord av pastöriserad mjölk, och '
                    'Livsmedelsverket avråder gravida från vitmögelost som inte har värmts ordentligt. Ugnsbakad camembert '
                    'som blivit genomvarm är säkrare.')),
    337: dict(lead='Den milda, mjuka vita italienska osten som traditionellt görs av vasslen från tillverkningen av andra '
                   'ostar, med krämig konsistens och mild, söt mjölksmak. Nettokolhydraterna är mycket låga (cirka 5 g), '
                   'det glykemiska indexet är inte tillämpligt, och ricotta innehåller vassleprotein som tas upp snabbt.',
              tips=('Två matskedar på morgonen med en nypa kanel och några tranbär; en utmärkt frukost för idrottare och '
                    'för mättnad, och protein bidrar till att öka muskelmassan.',
                    'Använd ricotta som ett mildare alternativ till grädde och majonnäs i pastafyllningar, såser och '
                    'salladsdressingar, eller bred den på mörkt rostat bröd med tomatskivor och basilika.',
                    'Ricotta innehåller mycket vassleprotein och en naturlig mängd mjölksocker (laktos), så personer med '
                    'uttalad laktosintolerans bör tänka på mängden.')),
    338: dict(lead='Huvudingrediensen i Italiens mest kända efterrätt (tiramisu): en mycket len och fet färskost gjord av '
                   'grädde som koagulerats med citronsyra. Mascarpone består nästan helt av fett och grädde med försumbara '
                   'kolhydrater, det glykemiska indexet är inte tillämpligt, och den ger en oslagbar sammetslen '
                   'konsistens.',
              tips=('En matsked som en lyxig efterrätt för dig som äter keto, blandad med rå kakao och lite vanilj; den '
                    'mättar snabbt och kan ersätta söta efterrätter.',
                    'Vispa den kall med lite espresso och stevia, så får du en snabb tiramisumousse helt utan raffinerat '
                    'socker och mjöl.',
                    'Mascarpone är mycket kalori- och fettät (cirka 430 kcal per 100 g), så en strikt portion på en '
                    'matsked gör att du kan njuta av den utan att få i dig för mycket energi.')),
    339: dict(lead='De schweiziska Alpernas pärla och grundosten i fondue och fransk löksoppa: en lagrad hårdost med en '
                   'komplex, nötig och smörig smak som växlar mellan lätt sötma och djup sälta. Inga nettokolhydrater, det '
                   'glykemiska indexet är inte tillämpligt, och osten innehåller kalcium och zink.',
              tips=('En liten skiva som smälter över rostade grönsaker eller soppor; fettet och proteinet ger en jämn '
                    'mättnad.',
                    'Riv den fint och njut av hur jämnt den smälter utan att fettet skiljer sig, vilket gör den till ett '
                    'fint val i ugnsgratänger med grönsaker och ägg.',
                    'Den långsamma lagringen gör osten nästan laktosfri, och den innehåller fullvärdigt protein; ett bra '
                    'val vid diabetes och lågkolhydratkost.')),
    340: dict(lead='Den klassiska osten med stora runda hål och mild, nötig smak, gjord av mjölk från schweiziska alpkor '
                   'och lagrad tills hålen bildas av den naturliga jäsningsgasen. Inga kolhydrater, det glykemiska indexet '
                   'är inte tillämpligt, och emmentaler är en av de mildaste hårdostarna med minst salt.',
              tips=('En tunn skiva på en fullkornssmörgås med sallad och tomat ger krispighet, smak och mättnad hela '
                    'förmiddagen.',
                    'Ät den i tärningar med oliver som mellanmål, eller använd den i varma smörgåsar eftersom den smälter '
                    'snabbt och får en omtyckt seg konsistens.',
                    'Emmentaler innehåller mindre salt än de flesta andra lagrade hårdostar, vilket gör den till ett bra '
                    'val för dig som håller koll på blodtrycket och vill ha kalcium.')),
    341: dict(lead='"De blå ostarnas kung" och Frankrikes skarpaste och mest anrika ost: den görs av opastöriserad '
                   'fårmjölk och lagras i de naturliga grottorna i Combalou med blåmöglet Penicillium roqueforti. '
                   'Kolhydraterna är nästan obefintliga, det glykemiska indexet är inte tillämpligt, och osten har en '
                   'skarp, salt och samtidigt sammetslen smak.',
              tips=('En mycket liten bit, stor som en fingertopp, räcker för att fylla munnen med smak; smula den över en '
                    'sallad med valnötter och päron eller sallad.',
                    'Blanda en liten bit med olivolja och citronsaft till en äkta fransk salladsdressing, så behöver du '
                    'inget salt eller industriella såser.',
                    '⚠️ Varning för gravida: roquefort är en lagrad blåmögelost av opastöriserad mjölk och ska inte ätas '
                    'av gravida på grund av risken för listeria.')),
    342: dict(lead='Stoltheten från La Mancha i Spanien och tapasbordets följeslagare: en hårdost gjord enbart av mjölk '
                   'från manchegafår, med de traditionella flätmönstren i skorpan. Inga kolhydrater, det glykemiska '
                   'indexet är inte tillämpligt, och osten har en örtig, smörig smak som blir skarpare ju längre den '
                   'lagras.',
              tips=('Tunna trekantiga skivor med råa mandlar och oliver som ett elegant mellanmål som ger en lugn mättnad.',
                    'Skala bort vaxskorpan och ät osten i rumstemperatur, och undvik att äta den med tjock söt sylt.',
                    'Manchego innehåller A-, D- och E-vitamin, och den lagrade varianten är nästan laktosfri.')),
    343: dict(lead='Vikingarnas traditionella mat som har erövrat världen: en isländsk mejeriprodukt som görs som en silad '
                   'mjuk ost men äts som tjock yoghurt. Den innehåller mycket protein (cirka 11 g per 100 g), nästan inget '
                   'fett och mycket lite kolhydrater (cirka 4 g), och det glykemiska indexet är inte tillämpligt.',
              tips=('En perfekt frukostskål; en liten kopp med lite kanel och några blåbär mättar i många timmar utan att '
                    'höja blodsockret nämnvärt.',
                    'Välj alltid naturell skyr och blanda själv med färsk frukt, och undvik smaksatta varianter med '
                    'tillsatt socker och glukossirap.',
                    'Protein bidrar till att öka muskelmassan, och skyr är ett av de mest populära livsmedlen bland '
                    'personer med diabetes och idrottare.')),
    344: dict(lead='Det äkta hantverksbrödet med krispig skorpa och segt inkråm fullt av luftbubblor: det jäser naturligt '
                   'i 24–48 timmar med vildjäst och mjölksyrabakterier utan bagerijäst. Den långa jäsningen bryter ned en '
                   'del av stärkelsen, vilket ger ett lågt glykemiskt index (53) och en betydligt lugnare matsmältning än '
                   'vanligt vitt bröd.',
              tips=('En rostad skiva med kokt ägg och avokado eller olivolja är en perfekt kombination som bromsar '
                    'upptaget av kolhydraterna och mättar ända till lunch.',
                    'Rosta surdegsbrödet i brödrosten, eftersom rostning delvis ändrar hur snabbt stärkelsen bryts ned, '
                    'och njut av den goda syrliga smaken.',
                    'Mjölksyrabakterierna i surdegen bryter ned en del av glutenet och fytinsyran, vilket kan förbättra '
                    'upptaget av mineraler som zink och magnesium; brödet innehåller ändå gluten och passar inte personer '
                    'med glutenintolerans.')),
    345: dict(lead='De traditionella tyska bageriernas stolthet: ett mörkt, kompakt och tungt bröd av krossade hela '
                   'rågkorn som ångbakas mycket långsamt i upp till 16–24 timmar. Det glykemiska indexet är lågt (46), och '
                   'brödet hör till dem som tas upp långsammast och innehåller mest fibrer.',
              tips=('En tunn skiva räcker gott för att bli mätt; lägg en skiva lagrad ost eller ett kokt ägg med gurka '
                    'ovanpå för ett mycket stabilt blodsocker.',
                    'Ät det färskt som det är utan att rosta det, eftersom det är naturligt mycket fuktigt, och drick ett '
                    'glas vatten eller varmt te till så att rågfibrerna kan svälla i magen.',
                    'Pumpernickel innehåller mycket fibrer som dämpar glukossvaret; ett typiskt val vid diabetes och '
                    'viktkontroll.')),
    346: dict(lead='Det omtyckta, svampiga italienska brödet med sin doftande arom: en mjuk vetedeg full av bubblor som '
                   'dränks i extra jungfruolivolja, rosmarin och grovt salt. Eftersom det bakas på vitt mjöl har det ett '
                   'högt glykemiskt index (71), även om olivoljan bromsar nedbrytningen något.',
              tips=('Ät en liten bit stor som en handflata som förrätt med en grön sallad, och undvik att äta stora bitar '
                    'ensamma, så slipper du en snabb glukosstegring.',
                    'Värm focaccian några minuter i ugnen så att kanterna blir krispiga igen, och doppa den i lite extra '
                    'jungfruolivolja och vinäger för att fördröja nedbrytningen av stärkelsen.',
                    'Ett gott men energi- och kaloririkt bröd; om du håller koll på vikten och blodsockret är strikt måtta '
                    'med bitens storlek och fokus på grönsakerna och proteinet till det rätta valet.')),
    347: dict(lead='Det populäraste vardagsbrödet i holländska bagerier: ett bröd med en krispig, sprucken skorpa som '
                   'liknar tigerskinn, som uppstår när ytan penslas med en smet av rismjöl och sesamolja före gräddningen. '
                   'Inkråmet är av lätt vitt mjöl och det glykemiska indexet är medelhögt (68).',
              tips=('En skiva räcker; bred alltid på ett mättande protein som lagrad gouda, naturligt jordnötssmör eller '
                    'kokt ägg, så slipper du den snabba hungern efter vitt bröd.',
                    'Välj varianten av fullkornsvete (volkoren tijgerbrood); den ger samma krispiga tigerskorpa men med '
                    'ett kliinkråm med fibrer som tas upp långsammare.',
                    'Det luftiga vita inkråmet bryts snabbt ned till socker, så att äta det med fett och protein bromsar '
                    'glukostoppen och förlänger mättnaden.')),
    348: dict(lead='Det gyllene, sammetslena brödet som tronar över de franska bakverken: en lyxig korsning mellan bröd '
                   'och kaka med färska ägg och naturligt karamelliserat smör. Smörfettet gör att det smälts relativt '
                   'långsamt, men det vita mjölet och det tillsatta sockret ger ett högt glykemiskt index (70) och mycket '
                   'kalorier.',
              tips=('En liten skiva som ett undantag under helgen; ät ett kokt ägg och drick en kopp svart kaffe utan '
                    'socker till, så undviker du för mycket enkla sockerarter.',
                    'Rosta briocheskivan lätt för att njuta av smörsmaken utan att behöva bre på mer sylt eller choklad.',
                    'Brioche är en energität måltid som förenar raffinerad stärkelse, fett och socker, så vid diabetes '
                    'eller strikt bantning bör den ses som en sällsynt sötsak och inte som vardagsbröd.')),
    349: dict(lead='New Yorks berömda runda brödring med sin täta, sega konsistens och blanka skorpa strödd med sesam; den '
                   'kokas i vatten före gräddningen och får därför sin unika täthet. Den kompakta degen av vitt mjöl ger '
                   'ett högt glykemiskt index (72) och en stor kolhydratbelastning.',
              tips=('En halv bagel räcker gott till en måltid; fyll den generöst med ricotta eller rökt lax och gurka, '
                    'eftersom proteinet och fettet bromsar upptaget av den täta degen.',
                    'Välj bagel av fullkornsvete och gröp ur en del av det mjuka inkråmet före fyllningen; det kökstricket '
                    'minskar smörgåsens kolhydrater med ungefär en tredjedel.',
                    'En hel bagel kan motsvara 4–5 skivor vanligt rostbröd i mängd stärkelse, så att dela den eller äta '
                    'hälften är det smartaste valet vid diabetes och viktkontroll.')),
    350: dict(lead='Det anrika ryska och europeiska kornet (kasja): trekantiga, naturligt glutenfria gryn med en '
                   'karaktäristisk nötig och jordig smak. Kokta bovetegryn har ett lågt glykemiskt index (49) och '
                   'innehåller fullvärdigt vegetabiliskt protein, zink och magnesium.',
              tips=('Ett utmärkt alternativ till vitt ris och pasta vid lunchen; bovetegryn mättar länge och ger en jämn '
                    'blodsockerkurva.',
                    'Blötlägg grynen en stund och koka dem sedan i förhållandet 1 del bovete till 2 delar vatten med lite '
                    'salt och olivolja i 15 minuter tills vattnet har sugits upp och grynen är mjuka men håller ihop.',
                    'Bovete innehåller rutin och är ett utmärkt val vid diabetes och celiaki.')),
    351: dict(lead='Det karaktäristiska grå mjölet som franska galetter och japanska sobanudlar görs av: malet helt bovete '
                   'med fibrer och protein. Vid bakning är det glykemiska indexet lågt (50), och bovetemjöl är ett av de '
                   'bästa alternativen till vitt mjöl för personer som inte tål vete.',
              tips=('Använd det till crêpes, pannkakor och bakverk; det mättar längre och smälts jämnare än glutenfritt '
                    'rismjöl eller majsstärkelse.',
                    'Eftersom det saknar gluten kan du blanda det med lite malda linfrön eller ägg för att binda degen och '
                    'ge den en fin smidighet vid gräddning på plåt.',
                    'Bovetemjöl bryts ned långsammare än de flesta glutenfria mjölsorter i handeln, vilket ger en jämnare '
                    'blodsockerkurva.')),
    352: dict(lead='Ett gammalt, ursprungligt vete som inte har förädlats som modernt vete: hela bruna korn med god nötig '
                   'smak och en krispig konsistens som är skön att tugga. Kokta speltkärnor har ett lågt glykemiskt index '
                   '(45) och innehåller fibrer, protein och mineraler.',
              tips=('Ett utmärkt alternativ till ris i risotto (farrotto) eller som ett mättande tillskott i sallader och '
                    'soppor, utan trötthet efter maten.',
                    'Blötlägg kärnorna i flera timmar före tillagningen och koka dem sedan i mild buljong i 30–40 minuter '
                    'tills de är klara men har kvar en skön krispighet, och servera med olivolja och örter.',
                    'Glutenet i spelt löser sig lättare i vatten, och vissa upplever spelt som lättare att smälta än '
                    'modernt vete; spelt innehåller ändå gluten och passar inte personer med celiaki.')),
    353: dict(lead='Fullkornsmjöl av det gamla speltkornet med skal och kli; ett fint alternativ till vitt vetemjöl i '
                   'europeiska hantverksbagerier. Vid bakning är det glykemiska indexet lågt (55), och mjölet ger brödet '
                   'en vacker brun färg, en varm doft och en fyllig smak.',
              tips=('Använd det till hembakat bröd och pajer; det smälts lugnare och mättar längre än vitt mjöl.',
                    'Speltdeg behöver försiktig knådning och lite kortare jäsningstid än vanligt vete eftersom '
                    'glutennätverket är känsligare, så knåda inte för mycket om du vill ha en mjuk konsistens.',
                    'Mjölet innehåller magnesium, järn och fosfor och tas upp betydligt långsammare än raffinerat vitt '
                    'mjöl, ett fint val för dig som vill baka balanserat bröd hemma.')),
    354: dict(lead='Ett mångsidigt mjöl från Indien och Medelhavet (besan, gram flour): finmalda torkade kikärter, '
                   'naturligt glutenfria och med mycket vegetabiliskt protein och fibrer. Det glykemiska indexet är lågt '
                   '(35), och kikärtsmjöl är ett av de bästa alternativen till vanligt mjöl vid diabetes och '
                   'insulinresistens.',
              tips=('Använd det till snabba plattbröd (socca, cheela) eller i stället för ströbröd och ägg för att reda '
                    'soppor och göra pannkakor; det mättar länge och ger en jämn blodsockerkurva.',
                    'Blanda det med vatten, olivolja, spiskummin och lite salt och låt smeten vila en halvtimme, stek den '
                    'sedan i en het panna till tunna, gyllene, krispiga och proteinrika pannkakor.',
                    'Kikärtsmjöl innehåller folat, järn och fibrer och är ett av de mjölsorter som påverkar blodsockret '
                    'minst; det passar bra för idrottare och vegetarianer.')),
    355: dict(lead='Den berömda värmande italienska landsbygdsrätten: en gyllene, krämig gröt av majsgryn som får sjuda '
                   'långsamt med buljong eller mjölk och parmesan. Eftersom den bygger på majsstärkelse har kokt polenta '
                   'ett medelhögt glykemiskt index (68), så den behöver balanseras med protein.',
              tips=('Håll portionen till en halv kopp kokt polenta och servera den varm under långkokt kött, grillad svamp '
                    'och tomatsås för att bromsa upptaget av majsstärkelsen.',
                    'Koka den med buljong och lite olivolja i stället för mycket smör; du kan också låta den svalna, skära '
                    'den i skivor och grilla den för en krispig yta och måttligt med kalorier.',
                    'Polenta är naturligt glutenfri och innehåller karotenoider och A-vitamin; vid diabetes är en måttlig '
                    'portion med protein nyckeln till att njuta av den.')),
    356: dict(lead='Världens mest spridda frukostflingor: rostade majsflingor utan tillsatt socker. Trots att de saknar '
                   'socker gör värmebehandlingen och valsningen att stärkelsen bryts ned och tas upp mycket snabbt, med '
                   'ett högt glykemiskt index (79) enligt den kliniska granskningen.',
              tips=('Undvik att äta en stor skål med bara mjölk på morgonen; blanda en liten näve med grekisk yoghurt, '
                    'chiafrön och nötter för att bromsa den kraftiga glukostoppen.',
                    'Välj alltid naturella varianter helt utan fruktosrik majssirap eller tillsatt socker, och ät dem '
                    'långsamt med protein till för att sakta ned matsmältningen.',
                    'Även osötade cornflakes höjer blodsockret lika snabbt som vitt bröd på grund av den snabba '
                    'stärkelsestrukturen, så fullkornshavre eller skyr är betydligt bättre val vid diabetes och '
                    'viktkontroll.')),
    357: dict(lead='Den äkta frukosten från Alperna som den schweiziske läkaren Bircher-Benner skapade: en blandning av '
                   'hela havreflingor, råg, naturella nötter och linfrön utan raffinerat socker eller industriell honung. '
                   'Det glykemiska indexet är lågt (45), och müsli är ett av de frukostval som påverkar blodsockret minst.',
              tips=('Låt en halv kopp dra i mjölk eller naturell yoghurt över natten med lite kanel och några bär, så får '
                    'du en krämig och mättande frukost som räcker hela förmiddagen.',
                    "Läs etiketten; välj alltid förpackningar där det tydligt står 'utan tillsatt socker', och undvik "
                    'müslimixar med sockrad torkad frukt eller chokladflingor.',
                    'Havrens betaglukaner bromsar upptaget av kolhydraterna; müsli är ett utmärkt alternativ till '
                    'industriella frukostflingor.')),
    358: dict(lead='Krispiga havrekluster rostade i ugnen med mandel, valnötter, kokos och pumpafrön och lite naturlig '
                   'honung. Trots de goda ingredienserna gör rostningen med fett och honung granolan energität, och den '
                   'har ett lågt glykemiskt index (52) men en koncentrerad kolhydratmängd som kräver medvetenhet om '
                   'portionen.',
              tips=('Se granola som ett krispigt tillskott och inte som en hel skål mat; strö bara två matskedar (cirka 30 '
                    'g) över en kopp naturell grekisk yoghurt för mer protein och långsammare sockerupptag.',
                    'Gör den hemma så har du full kontroll: blanda hela havregryn med kokosolja och naturella nötter, nöj '
                    'dig med en sked honung och lite kanel och vanilj, och rosta tills den blir gyllene och krispig.',
                    'Färdig granola i butiken innehåller ofta raffinerade oljor och koncentrerad majssirap, så att läsa '
                    'ingrediensförteckningen och hålla sig till portionen skyddar mot dolda glukostoppar.')),
    359: dict(lead='Krispiga, gröna stjälkar fulla av vatten: stjälkselleri innehåller fibrer, mineraler och apigenin. '
                   'Nettokolhydraterna är nära noll och det glykemiska indexet är inte tillämpligt.',
              tips=('Ett perfekt krispigt mellanmål när du vill ha något att tugga på; ät två till tre stjälkar doppade i '
                    'naturligt jordnötssmör utan socker eller hummus för mer mättnad utan nämnvärda kolhydrater.',
                    'Skölj stjälkarna och ät dem färska och krispiga, eller hacka dem fint i tonfisk- och kycklingsallader '
                    'för en frisk krispighet.',
                    'Selleri innehåller naturligt nitrat och ftalider och passar fritt och utan begränsning vid diabetes '
                    'och viktkontroll.')),
    360: dict(lead='Den traditionella höstroten i det europeiska och holländska köket (knolselderij): sellerins runda rot '
                   'med grovt skal och elfenbensfärgat inre med varm, mild sellerismak. Den innehåller betydligt mindre '
                   'kolhydrater än potatis och har ett lågt glykemiskt index (35).',
              tips=('Ett smart alternativ med lite stärkelse till potatismos: koka och mosa rotsellerin med lite olivolja '
                    'och vitlök och servera till grillad fisk eller kött med hälften av kalorierna och stärkelsen.',
                    'Skala bort det tjocka yttre skalet ordentligt, tärna roten och rosta den i ugnen med rosmarin och '
                    'olivolja tills den får färg, eller lägg den i vintriga grönsakssoppor för en krämig konsistens.',
                    'Rotselleri innehåller fibrer, K- och C-vitamin och fosfor och är ett utmärkt val vid diabetes och '
                    'insulinresistens som ett värmande alternativ till stärkelserika rotfrukter.')),
    361: dict(lead='Den vita, aromatiska löken med frisk anissmak och krispig konsistens som ett äpple (venkel); en gåva '
                   'från Medelhavet. Nettokolhydraterna är låga och det glykemiska indexet är inte tillämpligt, och fänkål '
                   'innehåller den aromatiska oljan anetol.',
              tips=('Skär den i tunna skivor som en självklar del av sallader till skaldjur och fisk med lite citron och '
                    'olivolja.',
                    'Ät den rå och krispig för den svala anissmaken, eller ugnsrosta klyftor med olivolja tills de mjuknar '
                    'och karamelliseras och smaken blir mycket mild och söt.',
                    'Fänkål mättar väl utan att påverka blodsockret.')),
    362: dict(lead='"Det vita guldet" och vårens främsta grönsak i Nederländerna och Tyskland (witte asperges): '
                   'sparrisskott som växer i mörker under jorden och därför behåller sin elfenbensfärg, sin sidenmjuka '
                   'konsistens och sin fina, smöriga smak. Kolhydraterna är nästan obefintliga och det glykemiska indexet '
                   'är inte tillämpligt.',
              tips=('Den traditionella vårmiddagen: kokt sparris med hackat kokt ägg, kalkonskivor, lite persilja och lite '
                    'naturligt smör, en lyxig proteinrik måltid helt utan stärkelse.',
                    'Skala stjälkarna noga från strax under toppen ned till basen och skär bort den träiga änden, och låt '
                    'dem sjuda på låg värme i vatten med lite salt och en citronskiva i 10–15 minuter tills de är mjuka.',
                    'Sparris innehåller asparagin, folat och mycket vatten och påverkar inte blodsockret nämnvärt.')),
    363: dict(lead='Den mest kända elfenbensfärgade, kägelformade grönsaken i Belgien och Nederländerna (witlof): tätt '
                   'sittande, krispiga blad med en fin, lätt bitterhet och frisk, vattnig smak. Nettokolhydraterna är '
                   'mycket låga, det glykemiska indexet är inte tillämpligt, och endiv innehåller fibern inulin.',
              tips=("Använd de böjda vita bladen som krispiga 'båtar' till tonfisksallad eller ost och ägg i stället för "
                    'kex och rostat bröd, så får du en frisk smårätt nästan utan kolhydrater.',
                    'Ta bort den lilla kägelformade kärnan i basen för att minska bitterheten, och ät endiven i en sallad '
                    'med äpple och valnötter, eller ugnsgrilla den med lite gouda.',
                    'Endiv är ett utmärkt val vid diabetes.')),
    364: dict(lead='De vågiga gröna bladen med taggiga kanter och frisk, jordig smak (andijvie), grunden i holländsk '
                   'stamppot både sommar och vinter. Kolhydraterna påverkar inte blodsockret, det glykemiska indexet är '
                   'inte tillämpligt, och frisésallat innehåller A- och K-vitamin.',
              tips=('Hacka den färsk och blanda med varma rätter eller ät den som en krispig bladsallad med vinäger och '
                    'olivolja; de rikliga fibrerna bromsar upptaget av måltiden och gör den mättande.',
                    'Blanda den hackade, råa frisésalladen med lite varmt grönsaksmos (rauwe andijviestamppot), så '
                    'behåller den sin krispighet, färg och sina vitaminer utan att tillagas för länge.',
                    'Frisésallat innehåller folat och lutein och påverkar inte blodsockret.')),
    365: dict(lead='Världens mest sålda runda, krispiga salladshuvud: tätt sittande ljusa blad fulla av kallt vatten och '
                   'frisk krispighet. Kolhydraterna är nästan obefintliga (mindre än 2 g netto) och det glykemiska indexet '
                   'är inte tillämpligt.',
              tips=('Använd de breda, stadiga bladen som ett alternativ till tortilla eller hamburgerbröd (lettuce wraps) '
                    'till grillad kyckling, fajitas och burgare, så sparar du hundratals kalorier och raffinerad '
                    'stärkelse.',
                    'Skär den i tjocka strimlor till hamburger- och tacosallader, och förvara den sköljd och torkad i '
                    'kylskåpet så att den förblir krispig och kall.',
                    'Isbergssallat har mycket få kalorier och kan ätas utan begränsning vid diabetes och lågkolhydratkost.')),
    366: dict(lead='Den avlånga, mörkgröna salladen; ryggraden i caesarsallad och medelhavssallader. Den har högre '
                   'näringstäthet än isbergssallat med A- och C-vitamin och folat, nettokolhydraterna är försumbara och '
                   'det glykemiska indexet är inte tillämpligt.',
              tips=('Börja varje huvudmåltid med en sallad av romansallat och olivolja; bladfibrerna och vattnet fyller '
                    'magen tidigt och bromsar upptaget av sockret i måltiden som följer.',
                    'Skär bladen på längden och krydda med olivolja, citron och vitlök; du kan också grilla halva '
                    'salladshuvuden i två minuter för en härlig rökig smak.',
                    'Romansallat innehåller klorofyll och mineraler, och att äta rikligt varje dag påverkar inte '
                    'blodsockret.')),
    367: dict(lead='Den kungliga bladgrönsaken med färgglada stjälkar och breda gröna blad, omtyckt i medelhavs- och '
                   'levantinsk mat som fyllning i pajer och i grytor. Nettokolhydraterna är mycket låga, det glykemiska '
                   'indexet är inte tillämpligt, och mangold innehåller kalium och magnesium.',
              tips=('Koka mangoldbladen med kokta kikärter, citronsaft och olivolja till en varm och mättande levantinsk '
                    'rätt.',
                    'Koka de hårda stjälkarna några minuter först och tillsätt de tunna gröna bladen mot slutet så att de '
                    'mjuknar varsamt med vitlöksklyftor och olivolja.',
                    'Mangold innehåller oxalat, så personer som är benägna att få njursten bör förvälla den lätt.')),
    368: dict(lead='Den lilla kinesiska kålen med krispiga vita stjälkar och mörkgröna, sidenlena blad (paksoi), som '
                   'förenar sellerins krispighet med spenatens mjukhet. Nettokolhydraterna är högst cirka 1,5 g per 100 g, '
                   'det glykemiska indexet är inte tillämpligt, och pak choi innehåller kalcium och C-vitamin.',
              tips=('Lägg skuren pak choi i nudelrätter och asiatiska soppor eller woka den med kycklingbröst och räkor, '
                    'så får måltiden mer volym utan extra kalorier.',
                    'Woka den i bara tre minuter med några droppar sesamolja, vitlök och ingefära, så behåller stjälkarna '
                    'sin naturliga saftiga krispighet.',
                    'Pak choi innehåller kalcium och svavelföreningar och är en av de bästa grönsakerna för mättnad och '
                    'ett stabilt blodsocker.')),
    369: dict(lead='De friska gröna stjälkarna med söt och lätt skarp löksmak; en följeslagare till vardagsmaten, grillat '
                   'och asiatiska rätter. Nettokolhydraterna i en portion är få, det glykemiska indexet är inte '
                   'tillämpligt, och salladslök innehåller organiska svavelföreningar och kvercetin.',
              tips=('Ät den rå till lunch eller hacka den fint över soppor, stekt ägg och fisk; den ger mycket smak.',
                    'Använd både den vita och den gröna delen; den vita delen har en aromatisk löksmak, medan den gröna '
                    'innehåller klorofyll och värmekänsligt K-vitamin.',
                    'Salladslök är en smakrik krydda utan någon kolhydratbelastning.')),
    370: dict(lead='Kockarnas fina lök med små klyftor och kopparrosa skal; smaken är mildare och sötare än vanlig lök och '
                   'saknar den brännande skärpan. Den används i små mängder i marinader och såser, och det glykemiska '
                   'indexet är inte tillämpligt.',
              tips=('Finhacka den i salladsdressingar (vinägrett) eller koka den med sås till kött och fisk, så får maten '
                    'ett fint djup i smaken och du behöver mindre salt.',
                    'Karamellisera schalottenlöksskivorna varsamt på låg värme i olivolja tills de mjuknar och blir '
                    'gyllene, och undvik att bränna dem, så behåller de sin naturliga sötma.',
                    'Schalottenlök innehåller flavonoider och berikar smaken utan att påverka blodsockret negativt.')),
    371: dict(lead='Den kritvita roten med en tunn lila topp (meiraap); en klassisk holländsk grönsak med mjuk konsistens '
                   'och en söt, mild smak som påminner om lätt kål. Nettokolhydraterna är mycket låga (cirka 4 g) och det '
                   'glykemiska indexet är inte tillämpligt.',
              tips=('Ett utmärkt sätt att byta ut en del av potatisen i grytor och soppor; majrovan suger upp buljongens '
                    'och kryddornas smak och mättar med hälften av kalorierna och stärkelsen.',
                    'Koka eller ångkoka den och mosa med lite olivolja och muskotnöt, eller tärna och rosta den i ugnen '
                    'med örter och kött.',
                    'Majrova innehåller C-vitamin och fibrer och är en av de rotfrukter som passar bäst vid diabetes och '
                    'insulinresistens.')),
    372: dict(lead='Den jättelika vita rättikan som är mest känd i det japanska och koreanska köket: en kritvit rot full '
                   'av krispigt vatten. Nettokolhydraterna är nästan obefintliga och det glykemiska indexet är inte '
                   'tillämpligt.',
              tips=('Riv en liten mängd fint och ät den till fisk, skaldjur och grillat kött.',
                    'Ät den rå och krispig i sallader, eller tärna och koka den i misosoppa och asiatiska soppor där den '
                    'blir mjuk och genomskinlig och tar upp all smak.',
                    'Rättika fyller magen med fibrer utan att tillföra socker eller nämnvärda kalorier.')),
    373: dict(lead='Gröna pärlor som alla älskar för sin naturliga sötma; ärter innehåller både vegetabilisk stärkelse, '
                   'fibrer och protein. Eftersom de innehåller komplexa kolhydrater har ärter ett lågt glykemiskt index '
                   '(48), och de mättar väl.',
              tips=('Ät en halv kopp som en del av en ris- eller gryträtt med mycket kött och grönsaker, och undvik en '
                    'stor tallrik ärter för sig själv, så att stärkelsen räknas rätt.',
                    'Ångkoka dem bara några minuter tills de är mjuka men behåller sin klargröna färg och sitt hela skal, '
                    'och undvik att koka dem för länge, eftersom stärkelsen då blir mjuk och tas upp snabbare.',
                    'Ärter innehåller vegetabiliskt protein, zink och lösliga fibrer; en bestämd portion gör att du kan '
                    'njuta av dem med ett stabilt blodsocker.')),
    374: dict(lead='De tunna, fina gröna bönorna (haricots verts), en symbol för elegans i det franska och holländska '
                   'köket med sin fina krispighet och smaragdgröna färg. Nettokolhydraterna är mycket låga (cirka 4 g) och '
                   'det glykemiska indexet är inte tillämpligt.',
              tips=('Ett perfekt tillbehör till kött, kyckling och grillad fisk; bönorna ger tallriken mättande volym och '
                    'fibrer som bromsar nedbrytningen av måltiden, utan nämnvärd stärkelse.',
                    'Förväll dem i tre till fyra minuter i kokande vatten och lägg dem direkt i isvatten så behåller de '
                    'krispigheten och färgen, och fräs dem sedan snabbt med en vitlöksklyfta, olivolja och lite grovt '
                    'salt.',
                    'Haricots verts innehåller kisel, folat och fibrer och kan ätas fritt vid diabetes och viktnedgång '
                    'utan oro för blodsockret.')),
    375: dict(lead='Den söta paprikan som fått mogna helt på plantan; saftig, krispig och med en vacker karmosinröd färg. '
                   'Nettokolhydraterna är mycket låga, det glykemiska indexet är inte tillämpligt, och röd paprika är en '
                   'av de livsmedel som innehåller mest C-vitamin, samt kapsantin.',
              tips=('En hel paprika skuren i stavar till frukost eller lunch ger mer än dubbla dagsbehovet av C-vitamin '
                    'och en glad krispighet och sötma i stället för snacks.',
                    'Ät den rå och krispig för att bevara det värmekänsliga C-vitaminet, eller ugnsrosta den med olivolja '
                    'och dra av det tunna skalet för att göra muhammara.',
                    'Mogen röd paprika innehåller betydligt mer C-vitamin än apelsin och påverkar inte blodsockret.')),
    376: dict(lead='En glad sol bland grönsakerna på salladsbordet: gyllengul paprika med en mild, fruktig smak och saftig '
                   'krispighet. Nettokolhydraterna är mycket låga, det glykemiska indexet är inte tillämpligt, och gul '
                   'paprika innehåller karotenoider och lutein.',
              tips=('Skär den i färgglada strimlor i den gröna salladen eller ät den som dipp till hummus och guacamole; '
                    'ett svalkande mellanmål som bryter enformigheten i bantningskosten utan snabb stärkelse.',
                    'Skär den färsk precis före servering så att den behåller krispigheten och saften, och ät den gärna '
                    'med en fettkälla som olivolja så tas A-vitaminet och karotenet upp bättre.',
                    'En vattenrik grönsak som mättar fräscht och inte påverkar blodsockret.')),
    377: dict(lead='Den kända mexikanska heta gröna chilin med en örtig, skarp smak och en omtyckt medelstark hetta. Den '
                   'äts i små mängder på några gram, kolhydraterna är försumbara, det glykemiska indexet är inte '
                   'tillämpligt, och den innehåller capsaicin.',
              tips=('Lägg färska jalapeñoskivor i tacos, sallader och äggrätter; hettan väcker sinnena och gör maten '
                    'smakrik.',
                    'Ta bort fröna och de vita hinnorna om du vill minska hettan och njuta av den örtiga smaken, och '
                    'undvik inlagd jalapeño på burk med socker och konserveringsmedel.',
                    'Om du har känslig mage eller sur reflux är det bäst att vara mycket måttlig, så slipper du '
                    'irritation.')),
    378: dict(lead='Små röda chilifrukter fulla av hetta och smak; grunden i det asiatiska och latinamerikanska köket och '
                   'i världens starka kryddor. Kolhydraterna i en portion på några gram är försumbara, det glykemiska '
                   'indexet är inte tillämpligt, och chili innehåller mycket capsaicin.',
              tips=('Hacka en halv chili fint i tomatsåser, soppor och grytor; den kraftiga hettan bryter enformigheten '
                    'och gör att du äter långsammare och med mer njutning.',
                    'Fräs den tidigt med olivolja och vitlök så att de heta oljorna frigörs och sprids jämnt i rätten, och '
                    'tvätta händerna noga med tvål och vatten efter att du skurit den så att du inte får den i ögonen.',
                    'Chili tillför inga nämnvärda kalorier eller stärkelse, men den som har känslig tarm eller aktivt '
                    'magsår bör vara mycket måttlig.')),
    379: dict(lead='Den gyllene, päronformade vinterpumpan med orange fruktkött fullt av söt, smörig och nötig smak; en av '
                   'de godaste grönsakerna med fibrer och mineraler. Kolhydraterna är måttliga och det glykemiska indexet '
                   'är lågt (51), med en låg glykemisk belastning tack vare de rikliga fibrerna och vattnet.',
              tips=('Ät en ugnsrostad bit i storlek med en knytnäve som ett smart stärkelsealternativ till ris och potatis '
                    'till grillat kött, och njut av den söta smaken utan att tillsätta socker eller honung.',
                    'Skala bort det hårda skalet, tärna pumpan och rosta den i ugnen med olivolja, kanel och lite '
                    'svartpeppar tills fruktköttet karamelliseras och blir mjukt och sammetslent, eller mixa den till en '
                    'värmande vintersoppa.',
                    'Butternutpumpa innehåller mycket betakaroten och lösliga fibrer, och en bestämd portion ger mättnad '
                    'och njutning utan oro för blodsockret.')),
    380: dict(lead='De rosa och färgglada stjälkarna med mycket syrlig och frisk smak (rabarber); i köket behandlas '
                   'rabarber som frukt, men det är en ren stjälkgrönsak. Nettokolhydraterna är mycket låga (mindre än 2 '
                   'g), det glykemiska indexet är inte tillämpligt, och rabarber innehåller fibrer, äppelsyra och oxalat.',
              tips=('Koka de skurna stjälkarna med lite vatten, stevia och en nypa kanel, så får du en syrlig och god '
                    'kompott att lägga på grekisk yoghurt utan tillsatt socker.',
                    '⚠️ Viktig köksvarning: ät bara de rosa stjälkarna och kasta bladen helt; bladen innehåller giftiga, '
                    'mycket höga halter av oxalsyra och får aldrig ätas.',
                    'Personer som har haft njursten bör vara måttliga med rabarber eftersom den innehåller oxalat.')),
    381: dict(lead='Skogens blanka svarta pärlor, saftiga och milt söta med en lätt syrlighet. Björnbär innehåller '
                   'pektinfibrer och antocyaniner och har ett lågt glykemiskt index (25) med en mycket låg glykemisk '
                   'belastning.',
              tips=('En hel kopp björnbär som mellanmål eller med morgonens yoghurt mättar väl och stillar sötsuget helt '
                    'utan att höja blodsockret nämnvärt.',
                    'Ät dem färska och sköljda som de är, så får du med de små krispiga fröna, och undvik helt att koka '
                    'sylt med socker av dem eller sila dem till juice.',
                    'Björnbär innehåller mycket fibrer och är ett av de bästa bärvalen vid diabetes, lågkolhydratkost och '
                    'keto.')),
    382: dict(lead='Blanka, genomskinliga rubinklasar som pryder trädgårdar och butiker i Europa och Nederländerna '
                   '(aalbessen): små, syrliga och saftiga bär med C-vitamin. Röda vinbär har ett lågt glykemiskt index '
                   '(25) tack vare mycket fibrer och pektin och lite naturligt socker.',
              tips=('En liten kopp färska bär som en svalkande efterrätt eller ett mellanmål; syrligheten väcker sinnena '
                    'och släcker törsten, och med lite naturell yoghurt dämpas syrligheten och du blir lugnt mätt.',
                    'Repa försiktigt av bären från de gröna klasarna och ät dem färska och väl sköljda, och undvik att '
                    'koka sylt med raffinerat socker av dem.',
                    'Röda vinbär innehåller lösliga fibrer och polyfenoler och är ett av de tryggaste bärvalen vid '
                    'diabetes och viktkontroll.')),
    383: dict(lead='Den mörklila pärlan med högst näringsvärde bland bären (cassis), med en kraftfull smak som förenar '
                   'aromatisk skärpa och syrlighet, och med antocyaniner och mycket C-vitamin. Svarta vinbär har ett lågt '
                   'glykemiskt index (25).',
              tips=('Lägg en näve i morgonens grekiska yoghurt eller havregrynsgröt; de mörka bären ger måltiden en glad '
                    'färg och bromsar upptaget av kolhydraterna.',
                    'Njut av de färska bären som de är med sitt tunna mörka skal, och undvik industriella vinbärsdrycker '
                    'och färdig cassissirap med koncentrerat socker.',
                    'Svarta vinbär innehåller betydligt mer C-vitamin än apelsin och påverkar blodsockret lite.')),
    384: dict(lead='Hårda, karmosinröda tranbär kända för sin skarpa syrlighet och sträva smak (veenbessen), som '
                   'innehåller proantocyanidiner. Färska tranbär har ett lågt glykemiskt index (35) och skiljer sig helt '
                   'från torkade tranbär fulla av socker.',
              tips=('Blanda dem med naturligt söt frukt som äpple eller i gröna smoothies för att balansera den kraftiga '
                    'syrligheten.',
                    'Koka färska tranbär med lite vatten, stevia och lite pressad apelsin till en hemgjord tranbärssås '
                    'utan tillsatt socker till kalkon och kött.',
                    'Var försiktig med industriellt torkade tranbär (craisins) och färdig tranbärsjuice; de sötas kraftigt '
                    'för att dölja syrligheten, medan färska eller frysta bär är det bästa valet.')),
    385: dict(lead='De traditionella sommarbären med genomskinligt randigt skal i gulgrönt eller rosa (kruisbessen); de '
                   'spricker i munnen med syrlig, lätt söt saft som påminner om omogna druvor och kiwi. Krusbär har ett '
                   'lågt glykemiskt index (25) och innehåller mycket fibrer och vatten.',
              tips=('En liten kopp kylda bär som mellanmål i sommarvärmen; det tunna skalet och de små fröna ger en frisk '
                    'krispighet och en lugn mättnad som släcker törsten.',
                    'Skölj bären och ät dem hela och färska, eller koka dem lätt till en syrlig sås till fet fisk som lax '
                    'och makrill som balanserar fettet på ett naturligt sätt.',
                    'Krusbär innehåller pektin och passar i alla kalorisnåla kostupplägg.')),
    386: dict(lead='En skatt från fruktträdgårdarna i Levanten och Europa (morellen): djupröda körsbär med god syrlig '
                   'saft, som innehåller melatonin och antocyaniner. Surkörsbär har ett lågt glykemiskt index (22) och är '
                   'en av de frukter som påverkar glukosen minst.',
              tips=('En liten kyld skål på kvällen; den påverkar blodsockret lite.',
                    'Ta bort kärnorna och ät frukterna färska, eller använd dem i den kända aleppiska körsbärskebaben, där '
                    'den syrliga saften förenas med grillat lammkött och ger en kunglig smak som bromsar nedbrytningen av '
                    'måltiden.',
                    'Surkörsbär passar bra vid diabetes och för idrottare.')),
    387: dict(lead='Sommarfrukten med slätt, blankt skal och aromatisk smak som förenar persikans sötma med plommonets '
                   'friskhet. Färsk nektarin har ett lågt glykemiskt index (43), och de lösliga fibrerna och den rikliga '
                   'saften ger vätska och en jämn matsmältning.',
              tips=('En medelstor kyld nektarin som äts med skalet som mellanmål mellan huvudmåltiderna ger mättnad och '
                    'naturlig sötma utan plötsliga blodsockertoppar.',
                    'Skölj frukten väl och ät den hel med det tunna skalet, där en stor del av de olösliga fibrerna finns, '
                    'och undvik att pressa eller skala den.',
                    'Nektarin innehåller kalium, betakaroten och C-vitamin; för dig som håller koll på vikten och '
                    'blodsockret är en frukt en typisk portion frukt.')),
    388: dict(lead='Den korta, älskade sommarens guld: sammetslena aprikoser som doftar vår och är fulla av naturlig saft '
                   'med lutein och zeaxantin. Färska aprikoser har ett lågt glykemiskt index (34) och innehåller betydligt '
                   'mindre koncentrerat socker än torkade aprikoser.',
              tips=('Ät två till tre färska aprikoser som en portion sommarfrukt; de innehåller kalium.',
                    'Ta bort kärnan och ät frukterna färska som de är, eller skär dem över en spenatsallad eller grekisk '
                    'yoghurt med lite kanel för en frisk och mättande smak.',
                    'Aprikoser innehåller A-vitamin, och fibrerna bidrar till en jämnare blodsockerkurva.')),
    389: dict(lead='Den speciella sommarfrukten med sin platta, diskusliknande form och lilla kärna (platte perzik, '
                   'paraguayo), med krämigt vitt fruktkött, stark doft och en mild sötma med låg syra. Det glykemiska '
                   'indexet är lågt (40) tack vare mycket fibrer och vatten.',
              tips=('En medelstor frukt är en glad sommarefterrätt som är lätt att äta och omtyckt av hela familjen.',
                    'Skölj frukten och ät den med det tunna sammetslena skalet, som bromsar upptaget av det naturliga '
                    'sockret, och ät den färsk och kyld utan att tillaga den.',
                    'Platt persika innehåller C-vitamin och polyfenoler, och det måttliga innehållet av nettokolhydrater '
                    'gör den till ett trevligt val vid diabetes och viktkontroll.')),
    390: dict(lead='Den stora citrusfrukten med glödande rosa fruktkött och en smak som skickligt förenar en omtyckt beska '
                   'med syrlighet och fräschör; den innehåller C-vitamin, pektinfibrer och lykopen. Det glykemiska indexet '
                   'är lågt (25) och effekten på blodsockret är mycket mild.',
              tips=('En halv stor grapefrukt på morgonen som äts med sked ger vätska och mättar väl.',
                    'Dela frukten på mitten och ät klyftorna med sked tillsammans med de tunna hinnorna för fibrernas '
                    'skull, och undvik att pressa den så att fibrerna inte silas bort.',
                    '⚠️ Avgörande klinisk och läkemedelsvarning: grapefrukt innehåller furanokumariner som hämmar '
                    'leverenzymet CYP3A4, vilket kan leda till farligt höga halter av vissa läkemedel i blodet (till '
                    'exempel kolesterolsänkande statiner, blodtrycksläkemedel och immunhämmande läkemedel). Den som tar '
                    'sådana läkemedel bör rådfråga sin läkare och undvika grapefrukt.')),
    391: dict(lead='Världens största citrusfrukt och grapefruktens förfader: ett tjockt, svampigt skal skyddar jättelika '
                   'klyftor fulla av krispig saft och en mild, söt smak nästan utan beska. Pomelo har ett lågt glykemiskt '
                   'index (30) och få kalorier.',
              tips=('Två till tre skalade klyftor som mellanmål på eftermiddagen fyller magen med fibrer och vatten och '
                    'ger en stor del av dagsbehovet av C-vitamin utan oro för blodsockret.',
                    'Skala bort det tjocka svampiga skalet och de hårda vita hinnorna runt klyftorna, och ät de saftiga '
                    'fruktköttskornen färska och kalla.',
                    'Pomelo innehåller kalium och fibrer; samma läkemedelsvarning som för grapefrukt gäller, men i mildare '
                    'grad, så den som tar statiner bör vara försiktig.')),
    392: dict(lead='Vinterns mest omtyckta frukt: små blanka mandariner som är lätta att skala och oftast saknar kärnor, '
                   'med en glad, aromatisk sötma och mycket saft. Klementiner har ett lågt glykemiskt index (42).',
              tips=('Två små klementiner är en perfekt portion frukt efter lunchen eller i jobb- och skolväskan; de '
                    'släcker törsten och ger en lugn mättnad som minskar suget efter industriella sötsaker.',
                    'Skala dem för hand och ät klyftorna med de tunna vita trådarna runt dem; trådarna innehåller pektin '
                    'och flavonoider som bromsar sockerupptaget.',
                    'Klementiner innehåller C-vitamin och hesperidin, och att äta hela frukter i stället för att pressa '
                    'dem är nyckeln till ett stabilt blodsocker.')),
    393: dict(lead='Kökets naturliga sol och smakens kärna: mogen gul citron med syrlig saft som innehåller citronsyra och '
                   'C-vitamin. Eftersom den används som saft och smaksättning i små mängder är nettokolhydraterna '
                   'försumbara och det glykemiska indexet är inte tillämpligt.',
              tips=('Pressa en rejäl halv citron över linsrätter, sallader, fisk och kött; C-vitamin ökar järnupptaget, '
                    'och syrligheten ger en smak som kan ersätta salt.',
                    'Tillsätt några droppar färsk citron i ett glas ljummet vatten på morgonen eller efter mastiga '
                    'måltider, utan några kalorier.',
                    'Citron påverkar inte blodsockret och är ett enkelt sätt att ge maten smak.')),
    394: dict(lead='Små gröna limefrukter med doftande arom och skarp, livlig syrlighet; grunden i det latinamerikanska '
                   'och thailändska köket och i svalkande drycker. Nettokolhydraterna i en portion är mycket låga, det '
                   'glykemiska indexet är inte tillämpligt, och skalet innehåller doftande oljor och limonen.',
              tips=('Pressa den över tacos, fajitas och guacamole; den aromatiska syrligheten förhöjer smaken och ger '
                    'fräschör som minskar suget efter feta såser.',
                    'Pressa frukten färsk precis före måltiden så att de aromatiska oljorna bevaras, och riv lite av det '
                    'gröna skalet för en härlig tropisk doft.',
                    'Lime innehåller C-vitamin och är en naturlig smaksättning som inte påverkar blodsockret.')),
    395: dict(lead='Drottningen bland de tropiska frukterna med en aromatisk doft som fyller rummet och vackert rosa '
                   'fruktkött; en av världens fiberrikaste frukter med mest C-vitamin. Färsk guava har ett lågt glykemiskt '
                   'index (15).',
              tips=('En hel frukt med skal som ett utmärkt mellanmål; de täta fibrerna fyller magen i många timmar och ger '
                    'en rejäl mättnad och aromatisk sötma utan att höja blodsockret nämnvärt.',
                    'Skölj frukten och ät den hel med skal och fruktkött, eftersom skalet innehåller mest C-vitamin, och '
                    'ät de små fröna utan att mala dem för fibrernas skull.',
                    'Guava innehåller ungefär fyra gånger så mycket C-vitamin som apelsin och unika lösliga fibrer, och '
                    'den är ett av de bästa fruktvalen vid diabetes.')),
    396: dict(lead='Den gyllene tropiska frukten med sidenlent orange fruktkött och svarta frön som liknar pepparkorn, '
                   'känd för enzymet papain. Papaya har en tydlig tropisk sötma och ett medelhögt glykemiskt index (60), '
                   'så portionen bör vara måttlig och frukten ätas medvetet.',
              tips=('En medelstor bit, ungefär en kopp tärningar, som naturlig efterrätt efter en proteinrik måltid.',
                    'Pressa lite lime över de kalla papayatärningarna; syrligheten bryter sötman, lyfter fram den tropiska '
                    'smaken och bromsar upptaget av sockret.',
                    'Papaya innehåller lykopen och A- och C-vitamin; vid diabetes gör en bestämd portion (en kopp) att du '
                    'kan njuta av den utan att belasta blodsockret.')),
    397: dict(lead='Den eleganta amerikanska nöten med slätt skal, vågig mandelform och en naturligt smörig och söt smak; '
                   'den liknar valnöten men är fetare och mindre besk. Nettokolhydraterna är nästan obefintliga, det '
                   'glykemiska indexet är inte tillämpligt, och pekannötter innehåller mycket omättat fett.',
              tips=('En liten näve (cirka 25–30 g, ungefär 15–18 halvor) som dagligt mellanmål mättar länge och ger en '
                    'jämn blodsockerkurva.',
                    'Ät dem råa eller lätt torrostade i ugnen, och undvik pekannötter täckta med kola eller raffinerat '
                    'socker.',
                    'Pekannötter innehåller zink, E-vitamin och oljesyra och passar bra vid keto och lågkolhydratkost.')),
    398: dict(lead='Nötternas pärla och den med renast fett av alla: krämvita kulor med fyllig, lyxig smörsmak som smälter '
                   'i munnen. Nettokolhydraterna är nära noll, det glykemiska indexet är inte tillämpligt, och '
                   'macadamianötter innehåller mycket enkelomättat fett (palmitoleinsyra, omega-7).',
              tips=('6–8 nötter räcker gott; den mycket höga fetthalten ger en snabb och djup mättnad som håller suget '
                    'efter stärkelse och mellanmål borta i många timmar.',
                    'Ät dem råa eller lätt rostade utan salt för att njuta av den naturliga, smöriga sötman, och undvik '
                    'nötter friterade i industrioljor eller kraftigt saltade.',
                    'Macadamianötter innehåller mest enkelomättat fett och minst kolhydrater av alla nötter och passar '
                    'utmärkt vid keto och insulinresistens.')),
    399: dict(lead='Paranötter är en av de rikaste livsmedelskällorna till selen, och selen bidrar till normal '
                   'sköldkörtelfunktion. Kolhydraterna är nästan obefintliga och de höjer inte blodsockret, och det '
                   'glykemiska indexet är inte tillämpligt.',
              tips=('En till högst två nötter om dagen; de mättar direkt och kan täcka dagsbehovet av selen.',
                    'Ät dem råa och krispiga som de är på morgonen med ett glas vatten, och undvik kraftig rostning för '
                    'att bevara de fina fettsyrorna och mineralerna.',
                    '⚠️ Avgörande klinisk varning om mängden: paranötter innehåller mycket höga halter av selen; ät inte '
                    'för många, håll dig till en eller två om dagen och ät aldrig mer än 3–4 om dagen, för att undvika '
                    'selenförgiftning (selenos).')),
    400: dict(lead='Ett komplett vegetabiliskt protein (hemp hearts): små mjuka frön med god nötig smak som påminner om '
                   'pinjenötter och solrosfrön. Nettokolhydraterna är nästan obefintliga, det glykemiska indexet är inte '
                   'tillämpligt, och hampafrön är en av de få växtkällorna till fullvärdigt protein med alla nio '
                   'essentiella aminosyror.',
              tips=('Strö två matskedar över gröna sallader, soppor, ägg eller en kopp yoghurt för mer protein och '
                    'omega-3- och omega-6-fettsyror och en jämn mättnad.',
                    'Ät dem råa och skalade utan att tillaga dem för att skydda det värmekänsliga omättade fettet, och '
                    'förvara påsen i kylskåp efter öppning så att oljorna inte härsknar.',
                    'Hampafrön är helt fria från berusande ämnen; de innehåller magnesium och järn, och protein bidrar '
                    'till att bibehålla muskelmassan.')),
    # foods 401-500: translated from the approved Arabic copy and FAQ (2026-10-24, four checked blocks of 25)
    401: dict(lead='Äkta tunga är en av de finaste och godaste vita havsfiskarna, med mjukt kött som är mycket lätt att '
                   'smälta. Den är helt fri från stärkelse och det glykemiska indexet är inte tillämpligt, vilket gör den '
                   'till en utmärkt måltid vid diabetes och viktnedgång utan oro för blodsockret.',
              tips=('Servera tungfilén med lätt sauterade grönsaker som zucchini och broccoli; en mild middag som mättar '
                    'länge utan att kännas tung före sänggåendet.',
                    'Ugnsbaka den gärna med lite olivolja, citronsaft och vitlök, och undvik att steka den i mjöl och '
                    'mycket smör, så förblir den mager.',
                    'Ett bra val för personer med känslig mage eller IBS och för den som har långsam magsäckstömning, '
                    'eftersom muskelfibrerna är så fina.'),
              faq=[dict(q='Passar tunga vid diabetes och viktnedgång?',
                        a='Ja, mycket bra. Den är rent protein nästan utan fett och stärkelse, påverkar inte blodsockret '
                          'och ger bara cirka 86 kcal per 100 g.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i en vanlig portion tunga?',
                        a='En portion på 150 g tillagad tunga innehåller cirka 130 kcal och 26 g protein och nästan ingen '
                          'stärkelse.'),
                   dict(q='Vad är skillnaden mellan att ugnsbaka och att steka tunga?',
                        a='Ugnsbakning bevarar den magra fisken, medan stekning i smör och mjöl ungefär tredubblar '
                          'kalorierna och tillför oönskat fett.')]),
    402: dict(lead='Piggvar kallas de lyxiga skaldjursbordens kung och har en fyllig, gelatinös konsistens och djup smak. '
                   'Eftersom den är helt fri från stärkelse och det glykemiska indexet inte är tillämpligt ger den en '
                   'proteinrik måltid som inte höjer insulinet; protein bidrar till att bibehålla muskelmassan.',
              tips=('Ät portionen med en lätt sås av aromatiska örter och citronsaft och en grön sallad med extra '
                    'jungfruolivolja.',
                    'Den blir bäst i ugnen på medelvärme med tomat- och fänkålsskivor; det tjocka köttet behåller sin '
                    'saftighet utan extra olja.',
                    'Piggvar innehåller zink, magnesium och omega-3.'),
              faq=[dict(q='Höjer piggvar blodsockret?',
                        a='Nej, piggvar innehåller inga kolhydrater och ger ingen blodsockerstegring eller plötslig '
                          'insulinfrisättning.'),
                   dict(q='Passar piggvar vid keto och lågkolhydratkost?',
                        a='Den är ett utmärkt val vid keto och lågkolhydratkost, eftersom den är ett rent havsprotein med '
                          'en del fett.'),
                   dict(q='Vad är näringsvärdet i en portion på 150 g piggvar?',
                        a='Portionen ger cirka 140 kcal och ungefär 30 g protein av hög kvalitet samt omega-3-fettsyror.')]),
    403: dict(lead='Dorade är den självklara stjärnan vid Medelhavets och arabvärldens kuster, omtyckt för sin naturligt '
                   'söta smak och stadiga kött. Den är fri från kolhydrater och det glykemiska indexet är inte '
                   'tillämpligt, vilket gör den till ett utmärkt vardagsval för dig som vill hålla koll på blodsockret och '
                   'äta god mat.',
              tips=('Ät den kolgrillad eller ugnsbakad med en grön sallad och några skedar basmatiris för att hålla nere '
                    'måltidens totala glykemiska belastning.',
                    'Öppna fiskens buk och gnid in den med spiskummin, citron, vitlök och dill innan du ugnsbakar den; det '
                    'lyfter fram smaken utan industriellt fett.',
                    'En mycket god källa till B12-vitamin och selen; selen bidrar till normal sköldkörtelfunktion.'),
              faq=[dict(q='Passar dorade vid diabetes och insulinresistens?',
                        a='Ja. Det goda proteinet och fettet bromsar magsäckstömningen och bidrar till jämnare '
                          'blodsockervärden.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i en medelstor dorade?',
                        a='En portion på 150 g doradefilé ger cirka 170 kcal och nästan 30 g protein och inga kolhydrater.'),
                   dict(q='Kan dorade hjälpa vid viktnedgång?',
                        a='Ja, den långvariga mättnaden från fisken gör det lättare att stå emot stärkelse och småätande '
                          'mellan måltiderna.')]),
    404: dict(lead='Havsabborre är en ikon bland de lyxiga fiskrätterna: kritvitt kött och en mild smak som även de som '
                   'inte gillar stark fisksmak tycker om. Det glykemiska indexet är inte tillämpligt eftersom fisken '
                   'saknar stärkelse.',
              tips=('En komplett tallrik med havsabborrefilé, sparris eller gröna bönor och en sked olivolja ger en '
                    'balanserad måltid som är lätt för magen.',
                    'Tillaga den i bakplåtspapper (en papillote) med citronskivor och örter, så stängs fukten och smaken '
                    'inne utan extra fettkalorier.',
                    'Havsabborre innehåller kalium och omega-3; EPA och DHA bidrar till hjärtats normala funktion vid ett '
                    'dagligt intag av 250 mg.'),
              faq=[dict(q='Hur kan havsabborre hjälpa personer med diabetes att hålla koll på värdena?',
                        a='Eftersom den saknar stärkelse ger den rent protein som mättar utan att stimulera en överdriven '
                          'insulinfrisättning.'),
                   dict(q='Vad är näringsvärdet i en portion havsabborre (150 g)?',
                        a='Portionen ger cirka 145 kcal, 28 g protein och fett av god kvalitet.'),
                   dict(q='Kan man äta havsabborre till middag när man bantar?',
                        a='Den är ett av de bästa valen för en lätt middag; den är lättsmält och ger sällan uppblåsthet.')]),
    405: dict(lead='Regnbåge förenar den vita fiskens milda smak med den feta fiskens omega-3. Den är fri från socker och '
                   'det glykemiska indexet är inte tillämpligt, och den ger en glädjande måltid.',
              tips=('Njut av den grillad med en sallad av ruccola och champinjoner; fettet i fisken förbättrar upptaget av '
                    'de fettlösliga vitaminerna i måltiden.',
                    'Grilla regnbågen hel på låg värme med citronskivor och vild timjan; det naturliga fettet räcker för '
                    'att den ska bli klar och mör utan olja.',
                    'Regnbåge innehåller det naturliga färgämnet astaxantin.'),
              faq=[dict(q='Skiljer sig regnbåge från lax i kalorier och fett?',
                        a='Regnbåge innehåller något mindre kalorier och fett totalt än lax, men ger också '
                          'omega-3-fettsyror.'),
                   dict(q='Är regnbåge bra för hjärtat?',
                        a='Regnbåge innehåller EPA och DHA, och EPA och DHA bidrar till hjärtats normala funktion vid ett '
                          'dagligt intag av 250 mg.'),
                   dict(q='Hur många gram protein finns i en vanlig portion regnbåge?',
                        a='En portion på 150 g innehåller nästan 30 g protein och cirka 210 kcal och inga kolhydrater.')]),
    406: dict(lead='Den stora hälleflundran har kompakta skivor kött som påminner om biffar, elfenbensvit färg och en '
                   'mild, omtyckt smak. Det glykemiska indexet är inte tillämpligt och fisken är helt fri från socker; den '
                   'är en utmärkt källa till mättande protein, och protein bidrar till att öka muskelmassan.',
              tips=('En grillad skiva med coleslaw i lätt yoghurtdressing ger en perfekt och god måltid vid keto eller '
                    'bantning.',
                    'Eftersom köttet är tätt och magert, tillaga det inte för länge så att det blir torrt; några minuter '
                    'på grillen eller i en het panna med lite olivolja räcker.',
                    'Hälleflundra innehåller mycket magnesium; magnesium bidrar till normal muskelfunktion.'),
              faq=[dict(q='Passar hälleflundra vid lågkolhydratkost?',
                        a='Den är ett utmärkt val för den som vill ha mycket protein och lång mättnad utan '
                          'nettokolhydrater.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g hälleflundra?',
                        a='Cirka 165 kcal och 34 g protein; hälleflundra är en av de fiskar som innehåller mest protein.'),
                   dict(q='Är hälleflundra ett säkert val under graviditeten?',
                        a='Enligt källtexten med måtta (en gång i veckan) eftersom det är en stor fisk, och gärna växelvis '
                          'med mindre fiskar som sardiner och regnbåge. Livsmedelsverket avråder dock gravida och ammande '
                          'från att äta hälleflundra, på grund av kvicksilverhalten.')]),
    407: dict(lead='Kummel är en god vän i det prisvärda hemmaköket: mycket milt kött som blir klart snabbt och vars smak '
                   'både barn och vuxna tycker om. Det glykemiska indexet är inte tillämpligt eftersom fisken saknar '
                   'kolhydrater.',
              tips=('Servera filén kokt med tomatsås och färska örter, eller mosad till fiskbullar i ugnen med persilja '
                    'och vitlök.',
                    'Undvik helt panerade, friterade kummelpinnar och ugnsbaka eller ångkoka fisken med lite paprikapulver '
                    'och citronsaft.',
                    'En av de mest lättsmälta fiskarna av alla och ett bra val efter operationer och för personer med '
                    'halsbränna och reflux.'),
              faq=[dict(q='Passar kummel vid strikt kaloriräkning?',
                        a='Ja, den är ett förstahandsval; en portion på 150 g ger bara cirka 117 kcal och 25 g protein med '
                          'nästan inget fett.'),
                   dict(q='Höjer kummel blodsockret?',
                        a='Nej, den är helt fri från kolhydrater och påverkar inte blodsockret när den tillagas utan '
                          'stärkelserika tillsatser.'),
                   dict(q='Hur kan jag servera kummel på ett gott sätt utan att steka den?',
                        a='En form i ugnen med paprikaskivor, lök, citronsaft och en nypa spiskummin ger fin smak och '
                          'behåller den magra fisken.')]),
    408: dict(lead='Sejen är den osynliga hjälten bland de nordiska fiskrätterna: vitt, mört kött och en hållbar källa '
                   'till B-vitaminer och protein av hög kvalitet. Den innehåller ingen stärkelse och det glykemiska '
                   'indexet är inte tillämpligt.',
              tips=('Ät den i en god fisk- och grönsakssoppa eller ugnsbakad med rostad broccoli och blomkål för mer '
                    'fibrer.',
                    'Att ångkoka eller ugnsbaka den med ingefära och citron bevarar fräschören och näringsvärdet utan '
                    'tillsatt fett.',
                    'Sej hör till de havsfiskar som innehåller minst kvicksilver och passar därför för regelbunden '
                    'konsumtion i familjen och för gravida.'),
              faq=[dict(q='Är sej samma fisk som används i snabbmatens fiskburgare?',
                        a='Ofta ja, men skillnaden är stor: den naturella fisken är utmärkt, medan panering och fritering '
                          'i industrioljor tar bort fördelarna.'),
                   dict(q='Vad är näringsvärdet i en portion sej (150 g)?',
                        a='Cirka 125 kcal och 27 g protein med en försumbar mängd fett och inget socker.'),
                   dict(q='Kan sej hjälpa till att hålla insulinnivåerna jämna?',
                        a='Sejen ger aminosyror som mättar, utan att höja blodsockret.')]),
    409: dict(lead='Naturligt krabbkött är en proteinrik havsdelikatess med en naturligt söt smak som kommer från '
                   'aminosyror och inte från tillsatt socker. Det glykemiska indexet är inte tillämpligt eftersom det '
                   'saknas nämnvärda kolhydrater, och krabbkött innehåller zink och selen; zink och selen bidrar till '
                   'immunsystemets normala funktion.',
              tips=('Njut av färskt naturligt krabbkött med lite citronsaft på en avokado- och salladssallad; se upp för '
                    'industriella crabsticks (surimi) fulla av stärkelse.',
                    'Snabb ångkokning med lagerblad och en citronskiva är det bästa sättet att få fram det söta köttet '
                    'utan feta såser eller majonnäs.',
                    'Var försiktig vid gikt och höga urinsyravärden; kräftdjur innehåller måttligt med puriner, så var '
                    'måttlig och drick rikligt med vatten.'),
              faq=[dict(q='Vad är skillnaden mellan naturligt krabbkött och crabsticks (surimi)?',
                        a='Naturligt krabbkött är rent protein utan stärkelse, medan industriella surimistavar innehåller '
                          'tillsatt stärkelse och socker som höjer blodsockret.'),
                   dict(q='Hur många kalorier finns i en vanlig portion krabbkött (100 g)?',
                        a='Cirka 85 kcal och 18 g protein med nästan inget fett, vilket gör det till ett bra val vid '
                          'viktnedgång.'),
                   dict(q='Höjer krabbkött det skadliga kolesterolet?',
                        a='Kolesterolet i maten höjer inte blodkolesterolet hos de flesta, så länge krabban tillagas och '
                          'äts utan stora mängder smält smör.')]),
    410: dict(lead='Hummer är en symbol för lyxig havsmat: elfenbensvitt kött med fullvärdigt protein och mycket lite fett '
                   'och kalorier. Det glykemiska indexet är inte tillämpligt eftersom hummern saknar kolhydrater, och den '
                   'mättar länge.',
              tips=('Servera hummerkött med en lätt sås av olivolja, krossad vitlök och citron i stället för att doppa det '
                    'i den klassiska skålen med smält smör.',
                    'Att ångkoka hummern eller grilla den i ugnen i några minuter behåller den fina saften och hindrar '
                    'köttet från att bli segt; krydda enkelt med svartpeppar och timjan.',
                    'Hummer innehåller koppar, selen och fosfor.'),
              faq=[dict(q='Passar hummer vid diabetes och bantning?',
                        a='Ja, den ger rent protein utan stärkelse eller nämnvärt fett och håller blodsockret stabilt '
                          'efter måltiden.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 100 g hummerkött?',
                        a='En portion på 100 g innehåller cirka 90 kcal och 19 g protein med mindre än 1 g fett.'),
                   dict(q='Kan man äta hummer om man har högt blodtryck?',
                        a='Skaldjur innehåller naturligt en del natrium, så det är bäst att inte salta extra vid '
                          'tillagningen.')]),
    411: dict(lead='Ostron hör till de livsmedel som innehåller mest zink och har en havssmak full av mineraler. Det '
                   'glykemiska indexet är inte tillämpligt eftersom kolhydraterna är mycket få; zink bidrar till normal '
                   'metabolism av kolhydrater och till immunsystemets normala funktion.',
              tips=('Ät dem gärna färska med några droppar citronsaft, eller ångkokta med lite dill och olivolja.',
                    'Om du tillagar dem räcker det att ångkoka i två minuter tills skalen öppnar sig, och undvik friterade '
                    'ostron i smet, som tillför stärkelse och fett.',
                    'Gravida och personer med nedsatt immunförsvar ska inte äta råa ostron, på grund av risken för '
                    'infektion med vibriobakterier.'),
              faq=[dict(q='Varför nämns ostron i samband med insulinresistens?',
                        a='Därför att de innehåller mycket zink, och zink bidrar till normal metabolism av kolhydrater.'),
                   dict(q='Hur många kalorier finns i 100 g ostron?',
                        a='Bara cirka 70 kcal med 7 g protein och mycket B12-vitamin, järn och koppar.'),
                   dict(q='Kan personer med njursjukdom äta ostron fritt?',
                        a='Rådfråga din läkare, eftersom ostron innehåller mycket fosfor, protein och mineraler som kan '
                          'behöva följas upp.')]),
    412: dict(lead='Blåmusslor är en av de populäraste och mest näringsrika skaldjursrätterna: orange kött med fyllig, '
                   'omtyckt smak och en näringsrik måltid till en rimlig kostnad. Det glykemiska indexet är inte '
                   'tillämpligt, och blåmusslor innehåller mycket järn; järn bidrar till normal bildning av röda '
                   'blodkroppar och hemoglobin.',
              tips=('En känd rätt är blåmusslor kokta i tomat-, vitlöks- och örtbuljong; drick buljongen med sked och njut '
                    'av mättnaden utan vitt bröd.',
                    'Koka dem några minuter under lock med lök, hackad vitlök, koriander och citronsaft, och kasta genast '
                    'alla musslor som inte öppnar sig under kokningen.',
                    'Blåmusslor innehåller mycket B12-vitamin och järn och en del glykogen; kolhydraterna räknas till '
                    'cirka 4 g per 100 g, en mycket liten mängd.'),
              faq=[dict(q='Är blåmusslor bra vid järnbrist?',
                        a='Blåmusslor innehåller hemjärn, som tas upp väl, i mängder som kan jämföras med rött kött men '
                          'med betydligt mindre kalorier och fett; järn bidrar till normal bildning av röda blodkroppar '
                          'och hemoglobin.'),
                   dict(q='Vad är näringsvärdet i 150 g kokta blåmusslor?',
                        a='Cirka 130 kcal, 18 g protein och mer än 300 % av dagsbehovet av B12-vitamin.'),
                   dict(q='Höjer blåmusslor blodsockret vid diabetes?',
                        a='De påverkar inte blodsockret nämnvärt, eftersom de innehåller lite naturlig stärkelse och '
                          'mycket protein.')]),
    413: dict(lead='Pilgrimsmusslor har ett vitt, sammetslent kött och en mild sötma som smälter i munnen och är kockarnas '
                   'stolthet världen över. Det glykemiska indexet är inte tillämpligt, och de är ett rent havsprotein; '
                   'protein bidrar till att bibehålla muskelmassan.',
              tips=('Servera stekta pilgrimsmusslor på ett mos av blomkål och vitlök, så får du en restaurangupplevelse '
                    'med nästan ingen glykemisk belastning.',
                    'Torka musslorna väl med hushållspapper innan de läggs i en mycket het panna med lite olivolja i en '
                    'och en halv minut per sida, så karamelliseras ytan utan att insidan förlorar sin mjukhet.',
                    'Pilgrimsmusslor innehåller magnesium, kalium och B12-vitamin; B12-vitamin bidrar till normal '
                    'homocysteinmetabolism.'),
              faq=[dict(q='Betyder den söta smaken att pilgrimsmusslor innehåller tillsatt socker?',
                        a='Nej, sötman är naturlig och kommer från aminosyror som glycin; den höjer inte blodsockret och '
                          'passar vid lågkolhydratkost.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 100 g pilgrimsmusslor?',
                        a='Cirka 110 kcal och ungefär 20 g protein med mindre än 1 g fett och cirka 5 g naturliga '
                          'kolhydrater.'),
                   dict(q='Passar pilgrimsmusslor till en snabb middag vid diabetes?',
                        a='Ja, de är klara på 3 minuter, är lätta för magen och ger varken plötsliga blodsockerfall eller '
                          'toppar under natten.')]),
    414: dict(lead='Rökt kalkonbröst är ett praktiskt och mycket vanligt val till smörgåsar och snabba måltider under '
                   'arbets- och skoldagar. Det är fritt från stärkelse, det glykemiska indexet är inte tillämpligt, och '
                   'det ger snabbt protein.',
              tips=('Rulla kalkonskivor runt gurk- eller paprikastavar och en bit keso som ett mellanmål som mättar länge '
                    'utan bröd.',
                    'Välj alltid skivor av hel bröstmuskel (whole muscle) och undvik malda och omformade charkuterier '
                    'fulla av stärkelse och soja.',
                    'Viktig klinisk varning vid högt blodtryck och njursjukdom: rökt kött innehåller nitrit och relativt '
                    'mycket salt, så var måttlig och välj varianter med reducerad salthalt.'),
              faq=[dict(q='Är rökt kalkon tillåtet vid keto och bantning?',
                        a='Ja, men läs förpackningen för att se att det inte tillsatts karamelliserat socker eller '
                          'majssirap vid rökningen.'),
                   dict(q='Vad är näringsvärdet i 50 g rökt kalkonbröst?',
                        a='Portionen innehåller cirka 55 kcal, 11 g protein, mindre än 1 g fett och mindre än 1 g '
                          'kolhydrater.'),
                   dict(q='Kan rökt kött ge vätskeansamling?',
                        a='Ja, om det är mycket salt, så drick gärna två glas vatten till och ät kaliumrika livsmedel som '
                          'gurka och avokado.')]),
    415: dict(lead='Kalvkött har fina muskelfibrer och en mild mjölkig smak och är ett av de lättaste röda köttslagen för '
                   'magen. Det glykemiska indexet är inte tillämpligt, och köttet ger animaliskt protein av högt '
                   'biologiskt värde utan tungt fett.',
              tips=('Ät en grillad kalvbiff med en stor tallrik rostade grönsaker och en grön sallad; C-vitamin ökar '
                    'järnupptaget.',
                    'Tillaga det snabbt på medelvärme och låt det inte bli torrt, eftersom det innehåller så lite eget '
                    'fett; svartpeppar och rosmarin räcker för att lyfta fram smaken.',
                    'Kalvkött innehåller hemjärn, zink och B12-vitamin; protein bidrar till att öka muskelmassan.'),
              faq=[dict(q='Är kalvkött bättre vid insulinresistens än kött från vuxna djur?',
                        a='Inget av dem höjer blodsockret, men kalvkött innehåller mindre mättat fett och är lättare att '
                          'smälta.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 120 g mager kalvstek?',
                        a='Portionen ger cirka 205 kcal och nästan 34 g protein av hög kvalitet med cirka 7 g fett.'),
                   dict(q='Är kalvkött tillåtet vid högt kolesterol?',
                        a='Ja, med måtta (två gånger i veckan) om du väljer magra styckningsdetaljer som filé och tillagar '
                          'köttet genom att koka eller grilla det.')]),
    416: dict(lead='Ankkött har en fyllig och lyxig traditionell smak och sticker ut bland fåglarna med ett fett som '
                   'liknar olivoljans (oljesyra). Det glykemiska indexet är inte tillämpligt, och ankbröst mättar mycket '
                   'väl.',
              tips=('Ät skinnfritt ankbröst med kokt rödkål eller sauterade grönsaker för färre kalorier och en härlig '
                    'smak.',
                    'Ta bort skinnet eller ugnsbaka ankan på ett högt galler så att fettet droppar av; du kan spara det '
                    'naturliga fettet och använda mycket små mängder i matlagningen.',
                    'Ankkött innehåller järn, B-vitaminer och selen; den som behöver hålla koll på blodfetterna bör ta '
                    'bort skinnet helt.'),
              faq=[dict(q='Är ankfett lika ofördelaktigt som annat fågelfett?',
                        a='Ankfett innehåller en god andel enkelomättat fett, men det är kaloririkt och mängden behöver '
                          'begränsas.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 120 g ankbröst utan skinn?',
                        a='Cirka 165 kcal och 34 g protein av hög kvalitet med bara cirka 3 g fett.'),
                   dict(q='Passar ankkött vid typ 2-diabetes?',
                        a='Ja, det höjer inte blodsockret, och fettet bidrar till mättnaden när det äts utan söta '
                          'tillsatser som honung.')]),
    417: dict(lead='Kaninkött är ett av de renaste vita köttslagen; det har mest protein och minst fett och kolesterol av '
                   'allt animaliskt kött. Det glykemiska indexet är inte tillämpligt, och kaninkött passar utmärkt vid '
                   'strikt bantning.',
              tips=('Ät det kokt eller ugnsbakat i en grönsaksgryta eller i traditionell molokhia kokad på lätt '
                    'kaninbuljong.',
                    'Låt det sjuda på låg värme med mastix, kardemumma, lök och citron för en aromatisk smak så att det '
                    'inte blir torrt, och undvik att bryna det i härdade oljor.',
                    'Kaninkött innehåller lite natrium och fett och passar äldre personer eftersom det är lättsmält.'),
              faq=[dict(q='Varför rekommenderas kaninkött ofta vid hjärt- och blodtrycksproblem?',
                        a='Därför att det innehåller mindre kolesterol, fett och natrium än kyckling och rött kött och ger '
                          'rent protein.'),
                   dict(q='Hur många kalorier finns i 120 g kokt kaninkött?',
                        a='Portionen innehåller bara cirka 210 kcal med 40 g protein och cirka 4 g fett och inga '
                          'kolhydrater.'),
                   dict(q='Kan kaninkött hjälpa vid viktnedgång?',
                        a='Det mättar väl med mycket protein utan att höja insulinet, och passar därför bra när du vill gå '
                          'ner i vikt.')]),
    418: dict(lead='Italiensk bresaola är rent nötkött som lufttorkats och saltats enligt gamla traditioner och räknas '
                   'till världens finaste charkuterier. Det glykemiska indexet är inte tillämpligt, proteinhalten är över '
                   '30 % och fettet nästan obefintligt, och den är ett förstahandsval bland idrottare för snabb mättnad.',
              tips=('Lägg några skivor bresaola på en tallrik vild ruccola med lite olivolja, naturlig citronsaft och '
                    'några flagor parmesan.',
                    'Den äts rå och färdig som den är utan tillagning eller uppvärmning; skär den i mycket tunna skivor '
                    'för att njuta av den fylliga smaken.',
                    'Varning: charkuterier innehåller mycket salt; den som har svårt högt blodtryck eller vätskeansamling '
                    'bör inte äta för mycket.'),
              faq=[dict(q='Är bresaola bättre än mortadella och andra pålägg?',
                        a='Ja, betydligt; den är hel, naturlig muskel som inte malts och saknar stärkelse, soja och '
                          'vegetabiliska oljor.'),
                   dict(q='Vad är näringsvärdet i 40 g bresaola?',
                        a='Cirka 60 kcal, 13 g protein och mindre än 1 g fett, utan kolhydrater och socker.'),
                   dict(q='Passar bresaola som mellanmål före eller efter träning?',
                        a='Ja, den ger protein och aminosyror; protein bidrar till att bibehålla muskelmassan.')]),
    419: dict(lead='Traditionell pastrami är en stolthet bland orientaliska och balkanska smårätter: fint nötkött täckt '
                   'med den kända kryddskorpan av bockhornsklöver, vitlök och paprika. Det glykemiska indexet är inte '
                   'tillämpligt, och den ger en het, fyllig smak utan att höja blodsockret.',
              tips=('Lägg två skivor pastrami i en omelett med två ägg i en panna med lite smör; en mättande ketofrukost '
                    'som håller hungern borta hela dagen.',
                    'Fräs den bara några sekunder på låg värme så att kryddorna med bockhornsklöver och vitlök inte bränns '
                    'och blir beska.',
                    'Den höga salthalten kräver måtta vid högt blodtryck.'),
              faq=[dict(q='Är pastrami säker vid diabetes och insulinresistens?',
                        a='Ja, när det gäller blodsockret; den saknar kolhydrater och höjer inte glukosen, men tänk på '
                          'blodtrycket på grund av saltet.'),
                   dict(q='Hur många kalorier finns i 30 g pastrami (två till tre skivor)?',
                        a='Cirka 45 kcal, 7 g animaliskt protein och cirka 1,7 g fett.'),
                   dict(q='Bör man ta bort kryddskorpan (bockhornsklöver och vitlök) före servering?',
                        a='Det behövs inte, utom för den som inte tycker om lukten av bockhornsklöver eller har en mycket '
                          'känslig mage.')]),
    420: dict(lead='Skivad rostbiff (kall ugnsstekt nötkött) är det enklaste sättet att få mättande protein under en tung '
                   'arbetsdag. Det glykemiska indexet är inte tillämpligt, och den hjälper dig att stå emot plötsliga '
                   'hungerattacker och sötsug vid bantning.',
              tips=('Rulla en skiva rostbiff runt en bit naturlig cheddar med ett salladsblad och en inlagd gurka för en '
                    'snabb och mättande måltid.',
                    'Ugnssteka en bit rostbiff (till exempel innanlår) hemma och skär den kall; ett rent alternativ utan '
                    'konserveringsmedel och industriell stärkelse.',
                    'Rostbiff innehåller hemjärn, zink och B6-vitamin; B6-vitamin bidrar till normal protein- och '
                    'glykogenmetabolism.'),
              faq=[dict(q='Är färdigskivad rostbiff från butiken ett bra val?',
                        a='Läs etiketten; bra varianter innehåller minst 95 % nötkött utan stärkelse, tillsatt socker '
                          'eller natriumglutamat.'),
                   dict(q='Vad är näringsvärdet i 50 g skivad rostbiff?',
                        a='Cirka 65 kcal, 11 g protein och cirka 2 g fett, utan kolhydrater.'),
                   dict(q='Passar rostbiff som kvällsmål vid diabetes?',
                        a='Ja, två skivor rostbiff före sänggåendet påverkar inte blodsockret nämnvärt.')]),
    421: dict(lead='Kycklingkorv är ett enkelt och praktiskt alternativ som barn och ungdomar gillar, och ger en snabb '
                   'lösning till frukost och middag. Det glykemiska indexet är inte tillämpligt, och korven är en bra '
                   'proteinkälla så länge den görs av en hög andel riktigt kycklingkött.',
              tips=('Servera korven grillad med stekt ägg och färska grönsaker, och undvik att lägga den i industriellt '
                    'vitt bröd, som ger en snabb blodsockerstegring.',
                    'Grilla eller koka den i stället för att steka den i olja, och välj korv med en enkel '
                    'ingrediensförteckning utan stärkelse, soja och glukossirap.',
                    'Kontrollera alltid salt- och nitrithalten på förpackningen; billiga industrivarianter kan innehålla '
                    'mycket dolt salt.'),
              faq=[dict(q='Hur vet jag om en kycklingkorv passar vid bantning och för blodsockret?',
                        a='Om kolhydraterna på förpackningen är under 1–2 g per 100 g och andelen kycklingkött är över 85 '
                          '%.'),
                   dict(q='Hur många kalorier finns i en kycklingkorv (portion på 75 g)?',
                        a='Portionen innehåller nästan 130 kcal, 13 g protein och cirka 8 g fett, beroende på hur fet '
                          'kycklingen är.'),
                   dict(q='Är kycklingkorv bättre än industriell nötkorv?',
                        a='Den har ofta färre kalorier och mindre mättat fett, men det avgörande är att den är fri från '
                          'stärkelsefyllning och kemiska konserveringsmedel.')]),
    422: dict(lead='Mald kalkon är ett smart alternativ till vanlig köttfärs; den ger samma variation och konsistens i '
                   'rätterna med betydligt mindre fett. Det glykemiska indexet är inte tillämpligt, och den är en utmärkt '
                   'proteinkälla vid viktnedgång; protein bidrar till att öka muskelmassan.',
              tips=('Använd den till lätta grillade köttbullar eller en bolognesesås på zucchinistrimlor i stället för '
                    'pasta.',
                    'Eftersom den är så mager, blanda i riven lök, hackad persilja och lite olivolja så att den förblir '
                    'mör och saftig vid tillagningen.',
                    'Kalkon innehåller aminosyran tryptofan.'),
              faq=[dict(q='Kan mald kalkon hjälpa vid viktnedgång?',
                        a='Ja, att byta ut nötfärs mot mager kalkonfärs sparar hundratals kalorier och minskar intaget av '
                          'mättat fett.'),
                   dict(q='Vad är näringsvärdet i 120 g tillagad kalkonfärs?',
                        a='Cirka 145 kcal, 31 g protein och cirka 2 g fett, utan kolhydrater.'),
                   dict(q='Smakar mald kalkon som mald kyckling?',
                        a='Smaken är kraftigare och djupare och köttet kompaktare än kyckling och påminner om ljust rött '
                          'kött, vilket gör den till ett gott och övertygande alternativ i recept.')]),
    423: dict(lead='Stekt kycklinglever är en traditionell och fyllig rätt som förenar god smak med ett mycket högt '
                   'näringsvärde. Det glykemiska indexet är inte tillämpligt, och kycklinglever innehåller mycket järn och '
                   'B12-vitamin; järn bidrar till normal bildning av röda blodkroppar och hemoglobin.',
              tips=('Ät den med en grön sallad med mycket tomat och paprika; C-vitamin ökar järnupptaget.',
                    'Fräs den snabbt på hög värme med vitlök, olivolja, osötad granatäpplesirap och en nypa spiskummin; '
                    'för lång tillagning gör den seg och torr.',
                    'Viktig klinisk varning för gravida: kycklinglever innehåller mycket stora mängder animaliskt '
                    'A-vitamin (retinol), och man bör undvika att äta mycket av den, särskilt under graviditetens första '
                    'trimester.'),
              faq=[dict(q='Höjer kycklinglever blodsockret?',
                        a='Nej, kolhydraterna är mycket få (cirka 1 g per 100 g), och levern innehåller järn och zink.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 100 g kycklinglever?',
                        a='Cirka 165 kcal och 24 g protein, mycket järn och mer än dagsbehovet av B12-vitamin.'),
                   dict(q='Passar kycklinglever vid högt kolesterol?',
                        a='Den innehåller mycket kolesterol, så det rekommenderas att äta den en gång i veckan, och '
                          'personer med ärftligt högt kolesterol bör vara extra försiktiga.')]),
    424: dict(lead='Kokt kycklingkrås är en näringsrik muskelmat med fast konsistens och en omtyckt smak i folkliga '
                   'rätter. Det glykemiska indexet är inte tillämpligt eftersom kråset saknar stärkelse, och det ger en '
                   'proteinrik måltid som håller hungern borta i många timmar.',
              tips=('Tillaga kråset i en grönsaksform i ugnen med lök, vitlök och naturlig tomatsås, och ät det med gaffel '
                    'som en kalorisnål huvudrätt.',
                    'Eftersom muskelvävnaden är så tät behöver kråset först sjuda på låg värme med aromatiska kryddor '
                    '(kardemumma, lagerblad och kanel) tills det är mört innan det fräses.',
                    'Kråset innehåller naturligt kollagen.'),
              faq=[dict(q='Passar kycklingkrås vid bantning och muskeluppbyggnad?',
                        a='Det är ett av de bästa prisvärda valen; rent muskelkött med mycket protein och nästan inget '
                          'fett eller kolhydrater, och protein bidrar till att öka muskelmassan.'),
                   dict(q='Vad är näringsvärdet i 100 g kokt kycklingkrås?',
                        a='Cirka 145 kcal, 30 g protein och mindre än 3 g fett, utan kolhydrater.'),
                   dict(q='Är kycklingkrås svårsmält för känsliga magar?',
                        a='Ja, om det inte är ordentligt tillagat, så koka det tills det är helt mört för att det täta '
                          'kollagenrika köttet ska bli lättare att smälta.')]),
    425: dict(lead='Svarta belugalinser kallas baljväxternas kaviar för sin eleganta runda form, blanka svarta färg och '
                   'lyxiga konsistens som inte faller sönder vid kokning. Det glykemiska indexet är lågt (en kliniskt '
                   'granskad uppskattning, 28) och den glykemiska belastningen är låg, vilket gör dem till ett utmärkt val '
                   'vid diabetes.',
              tips=('Lägg kokta linser i en medelhavssallad med vit ost, olivolja och citronsaft; de lösliga fibrerna '
                    'bromsar blodsockerstegringen.',
                    'De behöver inte blötläggas; koka dem i vatten med en vitlöksklyfta och lite spiskummin i 20 minuter '
                    'tills de är klara men hela.',
                    'Den svarta färgen kommer från en ovanligt hög halt av antocyaniner, samma färgämne som i blåbär.'),
              faq=[dict(q='Höjer svarta belugalinser blodsockret efter måltiden?',
                        a='Nej, det glykemiska indexet är lågt (cirka 28), och de rikliga fibrerna ger ett långsamt och '
                          'jämnt flöde av glukos till blodet.'),
                   dict(q='Vad är näringsvärdet i 150 g kokta belugalinser?',
                        a='Cirka 170 kcal, 14 g vegetabiliskt protein, 13 g kostfiber och 16 g komplexa nettokolhydrater '
                          'som tas upp långsamt.'),
                   dict(q='Varför föredrar kockar belugalinser framför bruna linser i sallader?',
                        a='Därför att de behåller sin fina, hela form och inte blir mjuka eller soppiga, vilket ger en '
                          'skön tuggighet.')]),
    426: dict(lead='Krossade röda linser (som blir gula vid kokning) är grunden i den värmande vintersoppan i varje '
                   'arabiskt hem och en snabb och omtyckt växtkälla till protein och fibrer. Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 26) och den glykemiska belastningen låg.',
              tips=('Ät linssoppan med en halv färskpressad citron och en nypa spiskummin; C-vitamin ökar järnupptaget.',
                    'Koka linserna med morot, lök och vitlöksklyftor utan att tillsätta vermicelli eller friterade bitar '
                    'av vitt bröd, så förblir det glykemiska indexet lågt.',
                    'Eftersom de är skalade och krossade är röda linser lättare att smälta än hela linser och ett bra val '
                    'för den som får lätt uppblåsthet av hela baljväxter.'),
              faq=[dict(q='Höjer linssoppa blodsockret snabbt?',
                        a='Nej, linser innehåller mycket lösliga fibrer som bromsar sockerupptaget och ger en lång känsla '
                          'av värme och mättnad.'),
                   dict(q='Vad är näringsvärdet i 150 g kokta röda linser?',
                        a='Portionen ger cirka 170 kcal, 13 g vegetabiliskt protein och cirka 8 g kostfiber.'),
                   dict(q='Passar röda linser när man bantar?',
                        a='Ja, mycket bra; de mättar i många timmar och kan minska suget efter stärkelse på kvällen.')]),
    427: dict(lead='Mungbönor hör till de äldsta baljväxterna i asiatisk folkmat. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 25).',
              tips=('Ät dem kokta i soppa eller i gröna sallader, eller groddade (mungbönsgroddar).',
                    'Blötlägg mungbönorna i ljummet vatten i 6–8 timmar före tillagningen och koka dem sedan med lite '
                    'ingefära och gurkmeja, så blir de lättare att smälta och mängden fytinsyra minskar.',
                    'Mungbönor innehåller flavonoiderna vitexin och isovitexin.'),
              faq=[dict(q='Kan mungbönor hjälpa vid insulinresistens?',
                        a='Det glykemiska indexet är lågt, och de rikliga fibrerna ger en jämn blodsockerkurva.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g kokta mungbönor?',
                        a='Cirka 160 kcal, 11 g vegetabiliskt protein och 11 g fibrer, nästan utan fett.'),
                   dict(q='Ger mungbönor gaser som andra baljväxter?',
                        a='Mungbönor hör till de baljväxter som är lättast att smälta och ger minst gaser, och de blir '
                          'ännu lättare att smälta när de blötläggs eller groddas.')]),
    428: dict(lead='Svarta bönor är den lysande stjärnan i det latinamerikanska köket; den mörka färgen kommer från en hög '
                   'halt av antocyaniner. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 30), och de '
                   'ger en jämn blodsockerkurva utan plötsliga toppar.',
              tips=('Blanda dem med söt majs, färgglad paprika, avokado och limesaft till en tacosallad med protein och '
                    'omättat fett.',
                    'Skölj konserverade bönor ordentligt under rinnande vatten för att få bort överflödigt salt, eller '
                    'koka torkade bönor efter blötläggning över natten med en vitlöksklyfta och lite spiskummin.',
                    'De lösliga fibrerna fermenteras i tjocktarmen och bildar smörsyra.'),
              faq=[dict(q='Är svarta bönor ett bra val vid diabetes?',
                        a='Ja, de är ett av de bästa valen; det låga glykemiska indexet och de rikliga fibrerna dämpar '
                          'blodsockerstegringen efter måltiden.'),
                   dict(q='Vad är näringsvärdet i 150 g svarta bönor?',
                        a='Nästan 200 kcal, 13 g protein och cirka 13 g fibrer.'),
                   dict(q='Kan svarta bönor hjälpa mot högt blodtryck?',
                        a='De innehåller naturligt kalium, magnesium och kalcium; kalium bidrar till att bibehålla ett '
                          'normalt blodtryck.')]),
    429: dict(lead='Italienska vita cannellinibönor är kända för sin smöriga, krämiga konsistens och milda nötaktiga smak. '
                   'Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 31) och den glykemiska belastningen '
                   'låg, vilket gör dem till hemligheten bakom mättnad och elegans i medelhavsrätter.',
              tips=('Mosa dem lätt med extra jungfruolivolja, vitlök, rosmarin och citronsaft till en mycket god dipp som '
                    'ersätter majonnäs och färdiga såser.',
                    'Lägg dem i grönsaksgrytor eller italiensk minestrone den sista kvarten av tillagningen, så tar de upp '
                    'smakerna utan att det sidenlena skalet går sönder.',
                    'Cannellinibönor innehåller ämnet fasolamin.'),
              faq=[dict(q='Passar cannellinibönor vid viktnedgång?',
                        a='Ja, den resistenta stärkelsen och fibrerna gör dem mättande.'),
                   dict(q='Hur mycket protein och hur många kalorier finns i 150 g kokta cannellinibönor?',
                        a='Portionen innehåller cirka 190 kcal, 13 g vegetabiliskt protein och 10 g kostfiber.'),
                   dict(q='Är cannellinibönor ett bra alternativ till pasta och potatis?',
                        a='Ja, de ger samma mättande konsistens men med betydligt lägre glykemiskt index och dubbelt så '
                          'mycket protein och fibrer.')]),
    430: dict(lead='Borlottibönor (de romerska prickiga bönorna) har ett vackert rosa mönster och en fyllig smak som '
                   'påminner om kokta kastanjer. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 28), '
                   'och de ger måltiderna djup och vintrig konsistens i stället för enkel stärkelse.',
              tips=('En härlig traditionell rätt är att koka dem med naturlig tomat, vitlök och olivolja och äta dem med '
                    'sked tillsammans med en färsk ruccolasallad.',
                    'Om du använder torkade bönor, blötlägg dem i 10 timmar och byt vatten två gånger, så försvinner de '
                    'komplexa sockerarter som ger uppblåsthet.',
                    'En utmärkt källa till folat och molybden; molybden bidrar till normal metabolism av svavelhaltiga '
                    'aminosyror.'),
              faq=[dict(q='Höjer borlottibönor HbA1c?',
                        a='Nej, de tas upp mycket långsamt och påverkar blodsockret lite.'),
                   dict(q='Vad är näringsvärdet i 150 g borlottibönor?',
                        a='Cirka 195 kcal, 14 g protein och 11 g fibrer, nästan helt utan fett.'),
                   dict(q='Varför försvinner det vackra prickiga mönstret vid kokning?',
                        a='Värmen omvandlar antocyaninerna till en jämn krämbrun färg; det är helt naturligt och påverkar '
                          'inte näringsvärdet.')]),
    431: dict(lead='Bissara är en traditionell varm rätt på bordet i Egypten och Maghreb, gjord av skalade bondbönor eller '
                   'krossade ärter med gröna örter som dill och koriander och olivolja. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 32), och den är en äkta folkrätt som förenar näringsvärde och låg '
                   'kostnad.',
              tips=('Ät den varm med sked och ringla en sked extra jungfruolivolja, en nypa spiskummin och paprikapulver '
                    'över, och ät salladslök och krispig gurka till i stället för vitt bröd.',
                    'Undvik att toppa rätten med lök som friterats i mjöl och härdade oljor; nöj dig med lätt '
                    'karamelliserad lök i lite olivolja eller hoppa över den.',
                    'Blandningen av bondbönor och gröna örter ger magnesium och klorofyll.'),
              faq=[dict(q='Passar bissara vid diabetes om den äts utan bröd?',
                        a='Ja, mycket bra; den är ett vegetabiliskt protein med mycket fibrer och lågt glykemiskt index, '
                          'och problemet brukar bara vara mängden bröd till.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i en vanlig tallrik bissara (150 g)?',
                        a='Tallriken innehåller nästan 175 kcal, 13 g vegetabiliskt protein och cirka 9 g fibrer.'),
                   dict(q='Får personer med favism (G6PD-brist) äta bissara?',
                        a='Avgörande klinisk varning: om bissaran är gjord på bondbönor får personer med favism '
                          '(G6PD-brist) inte äta den alls; de kan bara äta bissara gjord på ärter.')]),
    432: dict(lead='Krossade gula ärter är de klassiska baljväxternas gula guld; de löses snabbt upp och ger soppor en '
                   'sammetslen, fyllig konsistens utan grädde eller raffinerad stärkelse. Det glykemiska indexet är lågt '
                   '(en kliniskt granskad uppskattning, 25).',
              tips=('Gör en varm soppa av dem med lök, selleri och citronsaft och servera den som en mättande måltid som '
                    'håller hungern borta kalla vinterdagar.',
                    'Låt dem sjuda på låg värme och skumma bort det vita skummet som bildas de första minuterna, så '
                    'minskar gasbildningen och konsistensen blir len och lättsmält.',
                    'Gula ärter innehåller isoflavoner och olösliga fibrer.'),
              faq=[dict(q='Höjer gul ärtsoppa blodsockret vid diabetes?',
                        a='Den höjer inte blodsockret snabbt; gula ärter har ett av de lägsta glykemiska indexen bland '
                          'baljväxterna.'),
                   dict(q='Hur många kalorier finns i 150 g kokta gula ärter?',
                        a='Cirka 175 kcal, 12 g protein och 12 g fibrer.'),
                   dict(q='Behöver krossade gula ärter blötläggas?',
                        a='Det behövs inte på samma sätt som för hela baljväxter, men två timmars blötläggning förkortar '
                          'koktiden och gör dem lättare att smälta.')]),
    433: dict(lead='Konserverad söt majs ger färg och en omtyckt krispighet åt moderna sallader och grytor med sin '
                   'naturliga, behagliga sötma. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 46), '
                   'och majsen bör räknas som komplex stärkelse och inte som en bladgrönsak som kan ätas fritt.',
              tips=('Ät den som en avvägd del av salladen (två till tre matskedar) med sallad och protein, så dämpas '
                    'effekten av det naturliga sockret på blodsockret.',
                    'Skölj den konserverade majsen ordentligt för att få bort lagen, som kan innehålla tillsatt socker och '
                    "mycket salt, och läs förpackningen för att välja 'utan tillsatt socker'.",
                    'Majs innehåller karotenoiderna lutein och zeaxantin.'),
              faq=[dict(q='Är konserverad söt majs tillåten vid diabetes och bantning?',
                        a='Ja, men räkna med den; den innehåller stärkelse och naturligt socker och ska räknas in i '
                          'måltidens kolhydratportion, inte som en grönsak som kan ätas fritt.'),
                   dict(q='Vad är näringsvärdet i 80 g konserverad söt majs?',
                        a='Cirka 70 kcal, 2,2 g protein, 2 g fibrer och cirka 15 g stärkelse.'),
                   dict(q='Skiljer sig konserverad majs från färska grillade majskolvar?',
                        a='Färsk grillad majs har mer intakta fibrer och inget tillsatt salt, men konserverad majs är ett '
                          'praktiskt val om den sköljs väl.')]),
    434: dict(lead='Konserverade kronärtskockshjärtan har en unik sammansättning av fibrer. Det glykemiska indexet är inte '
                   'tillämpligt eftersom nettokolhydraterna är låga, och de ger ett gott och näringsrikt tillskott till '
                   'många rätter.',
              tips=('Skär kronärtskockshjärtan över en grekisk sallad med olivolja, citronsaft och vit ost, eller fräs dem '
                    'med vitlök och örter.',
                    'Välj hjärtan i vatten och salt i stället för i billiga vegetabiliska oljor, och skölj dem snabbt för '
                    'att minska saltet.',
                    'Kronärtskocka är en av de rikaste naturliga källorna till fibern inulin.'),
              faq=[dict(q='Höjer kronärtskockshjärtan blodsockret?',
                        a='Nej, de innehåller nästan ingen stärkelse som tas upp.'),
                   dict(q='Hur många kalorier finns i 100 g konserverade kronärtskockshjärtan?',
                        a='Bara cirka 35 kcal med 2,4 g protein och 5 g kostfiber.'),
                   dict(q='Vilka ämnen finns i kronärtskocka?',
                        a='Kronärtskocka innehåller cynarin och luteolin.')]),
    435: dict(lead='Konserverade champinjoner är ett snabbt och lätt förvarat sätt att ge vardagsrätterna god umamismak '
                   'och näring. Det glykemiska indexet är inte tillämpligt eftersom de saknar stärkelse som tas upp, och '
                   'de mättar utan extra kalorier.',
              tips=('Lägg dem i morgonens omelett, hemgjorda tomatsåser och grönsakssoppor för mer konsistens och mättnad.',
                    'Låt champinjonerna rinna av och skölj dem, och fräs dem sedan på hög värme i en het panna med lite '
                    'vitlök och vilda örter så att överflödig fukt avdunstar och de får god smak.',
                    'Champinjoner innehåller ergotionein och betaglukaner.'),
              faq=[dict(q='Passar konserverade champinjoner vid diabetes och bantning?',
                        a='Ja, mycket bra; de är nästan sockerfria, innehåller mycket få kalorier och höjer inte '
                          'insulinet.'),
                   dict(q='Vad är näringsvärdet i 100 g konserverade champinjoner?',
                        a='Bara cirka 20 kcal, 2 g protein och 2 g fibrer, nästan helt utan fett och nettokolhydrater.'),
                   dict(q='Förlorar champinjoner sina fördelar vid konservering jämfört med färska?',
                        a='De behåller de flesta mineraler och betaglukaner, men färska innehåller något mer B-vitaminer '
                          'och har krispigare konsistens.')]),
    436: dict(lead='Palmhjärtan är en exklusiv och speciell råvara från palmens kärna, känd för sin mjuka, sparrisliknande '
                   'konsistens och milda smak. Det glykemiska indexet är inte tillämpligt eftersom nettokolhydraterna är '
                   'försumbara, och de är ett mycket populärt alternativ i bantnings- och ketorecept.',
              tips=('Skär dem i runda skivor över en sallad med avokado och tomat, eller skär dem på längden och använd '
                    'dem som alternativ till fettuccine med pesto.',
                    'Skölj dem i kallt vatten för att få bort den sura lagen, och ät dem kalla och krispiga eller värm dem '
                    'snabbt med ånga utan att tillaga dem för länge.',
                    'Palmhjärtan innehåller kalium, koppar och zink, lite naturligt natrium och mycket fibrer.'),
              faq=[dict(q='Passar palmhjärtan vid keto?',
                        a='De är ett av världens mest kända ketolivsmedel; nettokolhydraterna är nära noll och de ger en '
                          'härlig konsistens i måltiderna.'),
                   dict(q='Hur många kalorier finns i 100 g palmhjärtan?',
                        a='Bara cirka 30 kcal, 2,5 g protein och cirka 2,5 g fibrer.'),
                   dict(q='Hur kan de användas som alternativ till pasta?',
                        a='De säljs också som färdiga pastaremsor, eller kan skäras för hand och vändas med naturlig '
                          'tomatsås i två minuter, så liknar de pasta.')]),
    437: dict(lead='Bambuskott är en klassisk ingrediens i det asiatiska köket, kända för sin karaktäristiska krispighet '
                   'och sin förmåga att ta upp kryddornas och buljongens smak. Det glykemiska indexet är inte tillämpligt, '
                   'och de ger rätten volym och fibrer utan nämnvärda kalorier.',
              tips=('Lägg dem i wokrätter (stir-fry) med kycklingskivor, grönsaker och sesamolja, eller i asiatisk '
                    'kycklingsoppa för mer variation.',
                    'Använd alltid konserverade eller förkokta skott, och skölj dem i kokande vatten några minuter för att '
                    'få bort eventuell naturlig beska.',
                    'Bambuskott innehåller kalium och lösliga fibrer.'),
              faq=[dict(q='Påverkar bambuskott blodsockret?',
                        a='Nej, de innehåller nästan inget socker och ger fibrer som bromsar upptaget av resten av '
                          'måltiden.'),
                   dict(q='Vad är näringsvärdet i 100 g avrunna bambuskott?',
                        a='Bara cirka 27 kcal, 2,6 g protein och 2,2 g fibrer, nästan utan fett och socker.'),
                   dict(q='Kan färska bambuskott ätas råa?',
                        a='Varning: färska bambuskott får aldrig ätas råa, eftersom de innehåller naturliga cyanogena '
                          'ämnen som försvinner helt vid kokning och konservering.')]),
    438: dict(lead='Vattenkastanj är en krispig vattengrönsak som är mycket omtyckt i kinesisk mat och behåller sin '
                   'härliga vattniga krispighet även efter lång tillagning. Det glykemiska indexet är lågt (en kliniskt '
                   'granskad uppskattning, 50) och den glykemiska belastningen låg, vilket gör den till ett glatt inslag '
                   'som bryter enformigheten i bantningskosten.',
              tips=('Skär dem i skivor och lägg dem i ugnsrostade grönsaker eller nudelrätter; krispigheten ger en '
                    'mättande känsla som ersätter industriella snacks.',
                    'De läggs vanligen i de sista minuterna av tillagningen så att de behåller sin saft och krispighet, '
                    'och skölj de konserverade för att få bort eventuell metallsmak.',
                    'Trots namnet är de inte nötter utan vattenlevande stamknölar, och de innehåller B6-vitamin och '
                    'mangan.'),
              faq=[dict(q='Höjer vattenkastanjer blodsockret snabbt?',
                        a='Det glykemiska indexet är lågt (cirka 50) och stärkelsen är blandad med vatten och fibrer, så '
                          'de ger ingen kraftig stegring om portionen begränsas.'),
                   dict(q='Hur många kalorier finns i 80 g vattenkastanjer?',
                        a='Cirka 40 kcal, mindre än 1 g protein, 1,3 g fibrer och cirka 10 g kolhydrater som smälts '
                          'långsamt.'),
                   dict(q='Passar vattenkastanjer för personer med nötallergi?',
                        a='Ja, de är inte nötter utan en vattenväxt som växer i sankmark och innehåller inte de allergener '
                          'som finns i trädnötter och jordnötter.')]),
    439: dict(lead='Italienska skalade plommontomater på burk är hemligheten bakom de stora italienska restaurangernas '
                   'goda hemlagade såser med smak av söta, solmogna tomater. Det glykemiska indexet är inte tillämpligt '
                   'eftersom kolhydraterna är få, och de är det bästa valet för en sås utan tillsatt socker och '
                   'konserveringsmedel.',
              tips=('Krossa dem för hand med vitlöksklyftor, extra jungfruolivolja och färska basilikablad i en varm '
                    'panna, så får du en marinarasås utan socker.',
                    'Välj burkar som bara innehåller hela tomater och tomatjuice utan extra salt eller tillsatt socker; '
                    'att tillaga dem varsamt med olivolja gör att lykopenet tas upp bättre.',
                    'Tillagning och konservering gör att lykopenet tas upp betydligt bättre än från råa tomater.'),
              faq=[dict(q='Höjer konserverade skalade tomater blodsockret vid diabetes?',
                        a='Nej, sockret är naturligt och kombinerat med fibrer och tomatens milda syra.'),
                   dict(q='Vad är näringsvärdet i 100 g skalade tomater på burk?',
                        a='Bara cirka 20 kcal, 1 g protein, 1,5 g fibrer och cirka 4,5 g naturliga kolhydrater.'),
                   dict(q='Kan skalade tomater på burk ge halsbränna?',
                        a='De kan ge halsbränna hos personer med aktiv sur reflux; du kan mildra dem genom att koka dem '
                          'med riven morot i stället för att tillsätta socker.')]),
    440: dict(lead='Passata är silade tomater utan skal och kärnor med en helt sidenlen konsistens och grunden i ren '
                   'hemmamatlagning. Det glykemiska indexet är inte tillämpligt, och passata är ett rent alternativ till '
                   'koncentrerad industriell tomatpuré och söt ketchup.',
              tips=('Använd den som bas för grönsaks- och kötträtter och ugnsformar, eller som snabb sås till pizza med '
                    'havrebotten eller fullkornsbröd.',
                    "Läs ingrediensförteckningen; den ska bara innehålla 'silade tomater' och högst 0,5 % salt, utan "
                    'socker eller förtjockningsmedel.',
                    'Passata innehåller kalium, C-vitamin och fettlösligt lykopen.'),
              faq=[dict(q='Vad är skillnaden mellan passata och vanlig tomatsås?',
                        a='Passata är rena, pressade och silade råa tomater utan förkokning, tillsatt socker eller '
                          'stärkelse, till skillnad från färdiga såser.'),
                   dict(q='Hur många kalorier finns i 100 g passata?',
                        a='Nästan 25 kcal, 1,2 g protein och cirka 4 g naturliga kolhydrater utan fett.'),
                   dict(q='Passar passata vid insulinresistens?',
                        a='Ja, mycket bra, så länge den saknar tillsatt socker; den ger rätterna god smak utan att påverka '
                          'blodsockret.')]),
    441: dict(lead='Surkål (mjölksyrafermenterad vitkål på tyskt vis) förenar kålens krispighet med mjölksyrajäsningen. '
                   'Det glykemiska indexet är inte tillämpligt eftersom den saknar stärkelse, och den innehåller levande '
                   'mjölksyrabakterier.',
              tips=('Ät två matskedar till lunch eller middag som ett syrligt tillbehör.',
                    'Ät den rå utan att tillaga eller värma den, eftersom värmen dödar de levande laktobaciller som '
                    'bildats under den naturliga jäsningen.',
                    'Varning vid högt blodtryck: surkål innehåller salt från saltningen, och den som tar MAO-hämmare bör '
                    'vara uppmärksam på att den innehåller naturligt tyramin.'),
              faq=[dict(q='Vad innehåller surkål?',
                        a='Den innehåller mjölksyrabakterier och enzymer från den naturliga jäsningen.'),
                   dict(q='Vad är näringsvärdet i 100 g surkål?',
                        a='Bara cirka 20 kcal, 1 g protein och 3 g fibrer, samt C-vitamin och K2-vitamin.'),
                   dict(q='Påverkar surkål blodsockret?',
                        a='Surkål innehåller mycket lite kolhydrater och påverkar inte blodsockret nämnvärt.')]),
    442: dict(lead='Böngroddar (mungbönsgroddar) hör till de friskaste livsmedlen i världen: krispiga groddar fulla av '
                   'vatten och näring. Det glykemiska indexet är inte tillämpligt eftersom de saknar kolhydrater som tas '
                   'upp, och de passar bra vid viktnedgång.',
              tips=('Lägg en hel näve på en varm soppa eller en rå grönsakssallad; de ger en frisk krispighet och mättande '
                    'volym.',
                    'Woka dem i bara trettio sekunder eller ät dem färska och noga sköljda, så förblir de krispiga och '
                    'behåller sitt värmekänsliga C-vitamin.',
                    'Groddningen bryter ned fytinsyran, vilket kan förbättra upptaget av järn, zink och kalcium jämfört '
                    'med torkade bönor.'),
              faq=[dict(q='Passar böngroddar vid bantning och keto?',
                        a='De är ett av de bästa valen; 95 % av vikten är vatten och fibrer, och de innehåller bara cirka '
                          '4 g nettokolhydrater per 100 g.'),
                   dict(q='Hur många kalorier finns i 100 g böngroddar?',
                        a='Bara cirka 30 kcal, 3 g vegetabiliskt protein och cirka 2 g fibrer.'),
                   dict(q='Är det säkert för gravida att äta groddar?',
                        a='Gravida och äldre bör upphetta eller woka groddarna som en försiktighetsåtgärd mot bakterier '
                          'som kan växa i den fuktiga groddmiljön.')]),
    443: dict(lead='Inlagd kapris är Medelhavets syrliga och salta pärla som ger fisk och sallader en fantastisk '
                   'smakexplosion. Det glykemiska indexet är inte tillämpligt eftersom kolhydraterna är mycket få, och '
                   'kapris innehåller flavonoider.',
              tips=('Lägg en tesked kapris över grillad fiskfilé eller en sallad med tonfisk och kokt ägg för mer smak '
                    'utan fett eller socker.',
                    'Skölj kaprisen några sekunder i kallt vatten före användning för att få bort överflödigt salt från '
                    'lagen, och njut av den örtiga, skarpa smaken.',
                    'Kapris är en av de livsmedel som innehåller mest kvercetin.'),
              faq=[dict(q='Höjer inlagd kapris blodsockret?',
                        a='Nej, den påverkar inte blodsockret eftersom mängden är liten och den saknar stärkelse.'),
                   dict(q='Vad är näringsvärdet i 10 g kapris (en liten matsked)?',
                        a='Bara cirka 2 kcal och nästan inget protein eller fett.'),
                   dict(q='Påverkar kapris personer med högt blodtryck?',
                        a='Ja, inlagd kapris innehåller mycket salt, så skölj den väl och använd den sparsamt som '
                          'smaksättning.')]),
    444: dict(lead='Spansk paella är folkrätternas drottning i Valencia och förenar saffranskryddat ris med ett lyxigt '
                   'urval av skaldjur eller fågel och grönsaker. Det glykemiska indexet är medelhögt (en kliniskt granskad '
                   'uppskattning, 58) och den glykemiska belastningen tenderar att vara hög på grund av riset, så '
                   'hemligheten är att hålla portionen i schack och fokusera på proteinet.',
              tips=('Börja måltiden med en grön sallad med olivolja, ät först skaldjuren, proteinbitarna och grönsakerna i '
                    'rätten och nöj dig med en halv kopp ris.',
                    'Gör paellan med rikligt med grönsaker och skaldjur och mindre ris, och undvik härdat fett; saffranet '
                    'och den naturliga buljongen räcker för att ge den en kunglig smak.',
                    'Saffran innehåller krocin och krocetin.'),
              faq=[dict(q='Passar spansk paella vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är medelhögt (cirka 58), skaldjurens protein bromsar '
                          'upptaget av riset, och det viktiga är att hålla portionen till 150–200 g.'),
                   dict(q='Hur många kalorier finns i en vanlig portion paella (250 g)?',
                        a='En hel portion innehåller nästan 540 kcal, 30 g protein och cirka 70 g kolhydrater, beroende på '
                          'mängden ris och protein.'),
                   dict(q="Vad är det krispiga 'socarrat'-lagret i botten av paellan?",
                        a='Det är det rostade lagret ris i botten av pannan; det är mycket gott, men se upp så att det '
                          'inte bränns, eftersom det kan bilda oönskad akrylamid.')]),
    445: dict(lead='Spansk tortilla (den traditionella omeletten med potatis och ägg) är en ikon bland tapas som inte '
                   'saknas på något bord i Spanien, med sammetslen konsistens och värmande, mättande smak. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 48), eftersom fettet och proteinet i äggen och '
                   'olivoljan bromsar potatisstärkelsen.',
              tips=('Ät en skiva stor som en handflata med en sallad av ruccola och körsbärstomater till en komplett '
                    'medelhavsfrukost eller lunch.',
                    'För en mindre fet variant: ånga eller tillaga potatisskivorna i airfryer i stället för att dränka dem '
                    'i olja, blanda dem sedan med ägg och extra jungfruolivolja och grädda på låg värme.',
                    'Tortillan förenar kolin från äggulan och kalium från potatisen, och den mättar länge utan kraftiga '
                    'blodsockersvängningar.'),
              faq=[dict(q='Höjer spansk tortilla blodsockret som vanlig friterad potatis?',
                        a='Nej, äggens protein och fettet bromsar nedbrytningen av potatisstärkelsen tydligt, så det '
                          'glykemiska indexet är lågt (cirka 48).'),
                   dict(q='Vad är näringsvärdet i 150 g spansk tortilla?',
                        a='Cirka 285 kcal, 12 g fullvärdigt protein, 16,5 g fett och cirka 20 g stärkelse.'),
                   dict(q='Kan man lägga till grönsaker i tortillan för att öka näringsvärdet?',
                        a='Ja, gärna; spenat, svamp, lök och paprika ger mer fibrer och sänker den glykemiska belastningen '
                          'ytterligare.')]),
    446: dict(lead='Andalusisk gazpacho är världens mest kända kalla soppa med tomat och grönsaker och en av de svalkande '
                   'rätter som det spanska köket skapat mot sommarvärmen. Det glykemiska indexet är inte tillämpligt '
                   'eftersom sockerhalten är låg, och soppan ger vätska och vitaminer.',
              tips=('Drick den kall i ett glas eller en liten skål i början av måltiden; fibrerna och vätskan fyller en '
                    'stor del av magen och hjälper dig att hålla aptiten i schack till huvudrätten.',
                    'Den görs genom att mixa mogna tomater, gurka, grön paprika, vitlök och extra jungfruolivolja med '
                    'sherryvinäger; undvik att mixa i vitt bröd, så förblir den så lätt som möjligt.',
                    'Gazpacho innehåller vatten, kalium, lykopen och C-vitamin.'),
              faq=[dict(q='Passar gazpacho vid bantning och viktnedgång?',
                        a='Den är ett av de bästa sommarvalen vid viktnedgång; ett helt glas mättar väl med bara cirka 90 '
                          'kcal.'),
                   dict(q='Hur många kalorier finns i 200 ml gazpacho utan bröd?',
                        a='Portionen innehåller cirka 90 kcal, främst från skeden extra jungfruolivolja och grönsakerna, '
                          'med mycket lite kolhydrater.'),
                   dict(q='Höjer gazpacho blodsockret vid diabetes?',
                        a='Nej, den påverkar inte blodsockret nämnvärt.')]),
    447: dict(lead='Salmorejo från Córdoba är gazpachons tjockare och sammetslenare kusin, med en lyxig krämig konsistens '
                   'som serveras kall. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 35) tack vare '
                   'den rikliga extra jungfruolivoljan som bromsar upptaget av den lilla mängd kolhydrater som tillsätts.',
              tips=('Den toppas traditionellt med hackat kokt ägg och skivor lufttorkat kött (jamón eller bresaola); med '
                    'dessa proteiner blir den en komplett och näringsrik lunch.',
                    'För en variant som passar vid diabetes kan du minska det traditionella vita brödet till en fjärdedel '
                    'eller byta ut det mot fullkornsbröd, och låta tomaterna och olivoljan stå för den sammetslena '
                    'konsistensen.',
                    'Den rikliga extra jungfruolivoljan ger oljesyra och polyfenoler.'),
              faq=[dict(q='Vad är skillnaden mellan salmorejo och gazpacho?',
                        a='Gazpacho är lätt och flytande och innehåller gurka, paprika och vinäger, medan salmorejo är '
                          'tjockare och bara bygger på tomat, olivolja och lite bröd.'),
                   dict(q='Vad är näringsvärdet i 150 g salmorejo?',
                        a='Nästan 140 kcal, 3 g protein (mer med ägg), 7 g omättat fett och cirka 14 g stärkelse.'),
                   dict(q='Passar salmorejo för dig som äter medelhavskost?',
                        a='Ja, den är ett typiskt exempel på medelhavskost som förenar tomater, enkelomättat fett och '
                          'protein.')]),
    448: dict(lead='Padrónpaprikor stekta i olivolja med grovt havssalt är den mest kända spanska tapasrätten: små gröna '
                   'paprikor med förtrollande aromatisk smak och goda överraskningar (en av tio kan vara stark!). Det '
                   'glykemiska indexet är inte tillämpligt, och de är ett mellanmål utan stärkelse och fullt av glädje och '
                   'smak.',
              tips=('Ät dem varma direkt från pannan som en mättande vegetarisk förrätt till grillat kött och fisk för mer '
                    'fibrer.',
                    'Fräs paprikorna i en mycket het panna med extra jungfruolivolja tills de blåser upp och får lätt '
                    'brända fläckar, ta sedan genast upp dem och strö över grovt havssalt.',
                    'Padrónpaprikor innehåller C-vitamin och lite capsaicin.'),
              faq=[dict(q='Är padrónpaprikor tillåtna vid keto och lågkolhydratkost?',
                        a='Ja, de är en lätt grönsak nästan utan nettokolhydrater.'),
                   dict(q='Hur många kalorier finns i 100 g tillagade padrónpaprikor?',
                        a='Cirka 55 kcal (främst från den uppsugna olivoljan), 1,5 g protein och 2 g kostfiber.'),
                   dict(q='Är padrónpaprikor mycket starka?',
                        a="De flesta är helt milda och aromatiska; det kända spanska ordspråket säger 'unos pican y otros "
                          "no' (vissa är starka, andra inte), vilket gör dem roliga att äta.")]),
    449: dict(lead='Patatas bravas är krispiga friterade potatistärningar med stark sås och vitlökssås (aioli), den mest '
                   'beställda rätten i Madrids gränder och i hela Spanien. Det glykemiska indexet är högt (en kliniskt '
                   'granskad uppskattning, 70) på grund av friteringen och den snabba stärkelsen, så de kräver stor '
                   'försiktighet och måtta vid diabetes och insulinresistens.',
              tips=('Om du vill smaka, nöj dig med några små bitar (3–4 tärningar) och ät dem efter en proteinrik måltid '
                    'och en grön sallad för att dämpa den kraftiga glukostoppen.',
                    'Skär potatisen, förkoka den och rosta den sedan i airfryer eller ugn med lite olja och rökt '
                    'paprikapulver och en naturlig tomat- och vitlökssås, utan fritering.',
                    'Klinisk varning vid diabetes och hjärtsjukdom: kombinationen av snabbt upptagen stärkelse och '
                    'vegetabilisk olja som hettats upp kraftigt är ett dåligt val.'),
              faq=[dict(q='Varför är det glykemiska indexet för patatas bravas högt?',
                        a='Därför att potatisen skärs i små tärningar och friteras, vilket bryter ned stärkelsen så att '
                          'den snabbt blir glukos i blodet (cirka 70).'),
                   dict(q='Vad är näringsvärdet i 150 g traditionella patatas bravas?',
                        a='Portionen innehåller nästan 280 kcal, 5 g protein och cirka 12 g frityrfett, med 35 g snabb '
                          'stärkelse.'),
                   dict(q='Hur kan jag göra patatas bravas till ett bättre val hemma?',
                        a='Låt den kokta potatisen svalna i kylskåpet först så att resistent stärkelse bildas, rosta den '
                          'sedan i airfryer och använd en hemgjord tomatsås med olivolja och stark vitlök.')]),
    450: dict(lead='Bläckfisk al ajillo (med vitlök, olivolja och chili) är kronan bland de snabba skaldjursrätterna i '
                   'södra Spanien: möra bläckfiskbitar kryddade med gyllene vitlök och extra jungfruolivolja. Det '
                   'glykemiska indexet är inte tillämpligt eftersom rätten saknar stärkelse, och den är en ren proteinrik '
                   'havsrätt som mättar väl utan något socker.',
              tips=('Njut av den varm med gaffel tillsammans med en grön sallad, och undvik att doppa vitt bröd i oljan, '
                    'så slipper du extra kalorier.',
                    'Fräs den skurna bläckfisken i varm olivolja med vitlöksskivor, lite chili och hackad persilja i bara '
                    'två till tre minuter; för lång tillagning gör den gummiaktig och seg.',
                    'Bläckfisk innehåller koppar, B12-vitamin och zink, och vitlöken ger allicin.'),
              faq=[dict(q='Är bläckfisk al ajillo bättre än klassisk friterad calamares?',
                        a='Ja, betydligt; den tillagas med vitlök och ren olivolja utan mjöl- och ströbrödshölje och utan '
                          'fritering i härdade oljor.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g bläckfisk al ajillo?',
                        a='Portionen innehåller cirka 220 kcal, 27 g protein, cirka 10,5 g fett från olivoljan och bara '
                          'cirka 4 g kolhydrater.'),
                   dict(q='Höjer bläckfisk blodkolesterolet?',
                        a='Kolesterolet i bläckfisk påverkar blodkolesterolet lite hos de flesta, så länge den tillagas i '
                          'olivolja och inte friteras i billiga industrioljor.')]),
    451: dict(lead='Spanska grönsakskroketter (croquetas de verduras) hör till de mest kända tapasrätterna: krispiga '
                   'utanpå och sidenlena inuti tack vare fyllningen av béchamelsås och karamelliserade grönsaker. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 53), eftersom fettet i olivoljan '
                   'bromsar upptaget av mjölet i béchamelsåsen, men de förblir en festlig rätt där portionen behöver '
                   'hållas i schack.',
              tips=('Ät bara två stycken som en smakbit tillsammans med en grön sallad med rikligt med vinäger och '
                    'citronsaft, så sänks måltidens glykemiska belastning.',
                    'Du kan grädda dem i airfryer efter att ha sprayat dem med olivolja i stället för att fritera dem, så '
                    'får du samma krispighet med en tredjedel av kalorierna och fettet.',
                    'Den traditionella béchamelfyllningen innehåller mjöl, mjölk och smör; därför bör personer med '
                    'laktosintolerans och insulinresistens äta dem med god måtta.'),
              faq=[dict(q='Passar spanska grönsakskroketter vid diabetes?',
                        a='Det glykemiska indexet är lågt (cirka 53), men de innehåller mycket kalorier och mjöl, så nöj '
                          'dig med högst en till två kroketter i måltiden.'),
                   dict(q='Hur många kalorier finns i 100 g grönsakskroketter?',
                        a='Portionen (två medelstora kroketter) innehåller cirka 235 kcal, 7,5 g protein, 12 g fett och '
                          'cirka 24 g kolhydrater.'),
                   dict(q='Hur gör jag kroketterna till ett bättre val hemma?',
                        a='Använd havre- eller mandelmjöl i béchamelsåsen, fyll dem med spenat och svamp och tillaga dem i '
                          'airfryer.')]),
    452: dict(lead='Pastel de nata (den kända portugisiska vaniljtarteletten) är ett mästerverk bland Lissabons bakverk, '
                   'med krispigt smördegsskal och varm, karamelliserad vaniljkräm. Det glykemiska indexet är medelhögt (en '
                   'kliniskt granskad uppskattning, 62), och den är en lyxig sötsak för festliga tillfällen, där '
                   'stärkelsen behöver vägas upp under resten av dagen.',
              tips=('Njut av en liten tartelett som efterrätt direkt efter en lunch rik på fibrer och protein, så undviker '
                    'du en kraftig blodsockertopp.',
                    'Strö lite äkta kanel över ytan; kanelen lyfter fram den traditionella smaken.',
                    'Tarteletten innehåller äggula, socker och smördeg rik på smör, vilket ger mycket kalorier och mättat '
                    'fett för den som har högt kolesterol.'),
              faq=[dict(q='Kan den som har diabetes smaka pastel de nata?',
                        a='Ja, en halv eller en liten tartelett (60 g) vid festliga tillfällen efter en komplett måltid, '
                          'och räkna med cirka 21 g snabb stärkelse.'),
                   dict(q='Vad är näringsvärdet i en pastel de nata (60 g)?',
                        a='Den ger cirka 180 kcal, 3 g protein, 9 g fett och cirka 22 g kolhydrater och socker.'),
                   dict(q='Varför är det glykemiska indexet medelhögt (62) och inte högt?',
                        a='Därför att fettet och proteinet i äggulan och grädden bromsar magsäckstömningen jämfört med '
                          'rena sockerrika sötsaker.')]),
    453: dict(lead='Pan con tomate (katalanskt tomatbröd) är grunden i den spanska frukosten: en krispig skiva lantbröd '
                   'som gnids med färsk tomat och en vitlöksklyfta och ringlas med jungfruolivolja. Det glykemiska indexet '
                   'är lågt (en kliniskt granskad uppskattning, 54), och rätten visar medelhavskostens enkelhet.',
              tips=('Ät en skiva med två skivor keso eller ett kokt ägg för mer protein och en mättnad som håller till '
                    'lunch.',
                    'Använd surdegsbröd eller fullkornsbröd för lägre glykemiskt index och mer fibrer.',
                    'Kombinationen av ren olivolja och färsk tomat gör att lykopenet tas upp bättre.'),
              faq=[dict(q='Passar spanskt tomatbröd när man bantar?',
                        a='Ja, mycket bra; en skiva är en typisk medelhavsfrukost med olivolja och tomat på cirka 140 '
                          'kcal.'),
                   dict(q='Vad är näringsvärdet i en vanlig skiva pan con tomate (80 g)?',
                        a='Den innehåller cirka 140 kcal, 3,5 g protein, 5,5 g fett och cirka 19 g stärkelse.'),
                   dict(q='Höjer den här frukosten blodsockret?',
                        a='Det glykemiska indexet är lågt (cirka 54), och jungfruolivoljan och tomatens fibrer bromsar '
                          'tydligt nedbrytningen av brödets stärkelse.')]),
    454: dict(lead="Klassisk fransk löksoppa (soupe à l'oignon) smeker sinnena med långsamt karamelliserad lök, djup smak "
                   'av köttbuljong och ett lager smält ost. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 35), och soppan är ett varmt och ombonat vinterval.',
              tips=('Njut av den varma soppan med sked och en enda liten skiva baguette, och undvik att doppa stora '
                    'mängder vitt bröd i skålen.',
                    'Karamellisera löken långsamt på låg värme utan att tillsätta socker; lökens naturliga sötma kommer '
                    'fram vid långsam tillagning i olivolja och aromatisk köttbuljong.',
                    'Karamelliserad lök innehåller kvercetin och inulin; den som har högt blodtryck bör vara uppmärksam på '
                    'buljongens salthalt.'),
              faq=[dict(q='Höjer fransk löksoppa blodsockret?',
                        a='Nej, det glykemiska indexet är lågt (cirka 35), och de naturliga fibrerna och proteinet i '
                          'buljongen dämpar blodsockerstegringen.'),
                   dict(q='Hur många kalorier finns i en skål fransk löksoppa (300 g)?',
                        a='Skålen ger cirka 440 kcal (beroende på mängden gruyère och bröd), med 19,5 g protein och cirka '
                          '39 g nettokolhydrater.'),
                   dict(q='Passar soppan vid keto?',
                        a='Den passar vid keto om du hoppar över baguetteskivan ovanpå och nöjer dig med buljongen, löken '
                          'och den smälta gruyèren.')]),
    455: dict(lead='Ratatouille är en ikon från den franska landsbygden och Provence: en harmoni av aubergine, zucchini, '
                   'paprika och tomat som tillagas i olivolja med aromatiska örter. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 25), och rätten är rik på vätska och fibrer.',
              tips=('En komplett rätt där portionen kan vara generös; ät den som ett mättande tillbehör till grillat '
                    'kycklingbröst eller en fiskfilé för mer protein.',
                    'Lägg de runda grönsaksskivorna omväxlande i en form och grädda dem med olivolja, rosmarin, timjan och '
                    'hackad vitlök, så bevaras vitaminerna.',
                    'Ratatouille innehåller kalium, C-vitamin och ämnena naringenin och antocyaniner; kalium bidrar till '
                    'att bibehålla ett normalt blodtryck.'),
              faq=[dict(q='Passar ratatouille vid diabetes och strikt bantning?',
                        a='Den är en av de allra bästa rätterna; kolhydraterna är få och den ger ingen kraftig '
                          'blodsockerstegring.'),
                   dict(q='Vad är näringsvärdet i 200 g ratatouille?',
                        a='Portionen innehåller cirka 145 kcal, 3,5 g protein, 7 g fett och 17 g kolhydrater (varav cirka '
                          '7 g fibrer).'),
                   dict(q='Kan ratatouille ätas kall?',
                        a='Ja, i Provence äts den varm som huvudrätt eller kall dagen efter med några droppar citron, och '
                          'den smakar lika gott.')]),
    456: dict(lead='Quiche med grönsaker och ost är en elegant fransk paj som förenar en ugnsbakad äggstanning med grädde '
                   'och ett rikt urval av spenat, svamp och ost. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 45), eftersom fettet i äggen och osten bromsar upptaget av degens stärkelse.',
              tips=('Ät en medelstor triangelformad bit med en sallad av ruccola och tomat, så bryts ostens fyllighet och '
                    'du får mer lösliga fibrer.',
                    'För en lättare variant: grädda quichen utan botten (crustless quiche) i en pajform, så får du en '
                    'proteinrik ketorätt.',
                    'Quiche innehåller kalcium, fullvärdigt protein och B12-vitamin; den som har åderförkalkning bör äta '
                    'den med måtta eftersom grädden och osten innehåller mycket mättat fett.'),
              faq=[dict(q='Passar grönsaksquiche med ost vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 45), proteinet och fettet dämpar plötsliga '
                          'blodsockertoppar, och det viktiga är bitens storlek.'),
                   dict(q='Hur många kalorier finns i en bit grönsaksquiche (150 g)?',
                        a='En vanlig bit ger cirka 410 kcal, 16,5 g protein, 25,5 g fett och cirka 28,5 g kolhydrater.'),
                   dict(q='Hur minskar jag kalorierna i en hemgjord quiche?',
                        a='Byt ut den tjocka grädden mot grekisk yoghurt med låg fetthalt och använd fullkornsmjöl, eller '
                          'hoppa över pajbotten helt.')]),
    457: dict(lead='Coq au vin är en av de äldsta klassikerna i det franska lantköket: kyckling som sjuder på låg värme '
                   'med svamp, pärllök och aromatiska örter. Det glykemiska indexet är inte tillämpligt eftersom rätten '
                   'saknar nettokolhydrater, och den är en proteinrik festmåltid; protein bidrar till att bibehålla '
                   'muskelmassa.',
              tips=('Ät de goda kycklingbitarna med svampen och löken och en sked av den aromatiska buljongen, och nöj dig '
                    'med en liten kokt potatis för att hålla stärkelsen i schack.',
                    'Rätten kan göras med koncentrerad kött- eller kycklingbuljong, två matskedar äppelcidervinäger och '
                    'naturlig druvjuice utan tillsatt socker, vilket ger samma djupa smak.',
                    'I det traditionella europeiska köket används rött vin; en koncentrerad buljong med örter ger ett '
                    'likvärdigt smakdjup och samma protein.'),
              faq=[dict(q='Höjer coq au vin blodsockret?',
                        a='Nej; rätten består av animaliskt protein med svamp och lök, och det glykemiska indexet är inte '
                          'tillämpligt eftersom den saknar stärkelse som tas upp.'),
                   dict(q='Vad är näringsvärdet i 250 g coq au vin?',
                        a='Portionen innehåller cirka 310 kcal, 38 g protein och 14 g fett, med bara 4 g kolhydrater från '
                          'grönsakerna.'),
                   dict(q='Passar rätten vid keto och lågkolhydratkost?',
                        a='Den är en utmärkt ketorätt: saftig kyckling med mycket smak, protein och naturligt fett utan '
                          'mjöl.')]),
    458: dict(lead='Bœuf bourguignon är den främsta kötträtten i Frankrike: tärningar av nötkött som sjuder i flera timmar '
                   'med morötter, svamp och karamelliserad lök tills de smälter i munnen. Det glykemiska indexet är inte '
                   'tillämpligt, och rätten är en lyxig vintermåltid med järn; järn bidrar till normal bildning av röda '
                   'blodkroppar och hemoglobin.',
              tips=('Ät din portion med gaffel tillsammans med grönsakerna som kokats i buljongen, och byt ut det vita '
                    'potatismoset mot ett krämigt blomkålsmos för en måltid som är lätt för blodsockret.',
                    'Hemligheten bakom mörheten är att låta rätten sjuda på mycket låg värme i två och en halv timme; en '
                    'örtrik köttbuljong med balsamvinäger ger den en äkta smak.',
                    'Bœuf bourguignon innehåller järn, zink, B12-vitamin och kollagen från köttets bindväv.'),
              faq=[dict(q='Påverkar bœuf bourguignon blodsockret?',
                        a='Den påverkar blodsockret lite eftersom den främst består av protein; effekten av de kokta '
                          'morötterna är liten eftersom de ingår i en komplett måltid med protein och fett.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 250 g bœuf bourguignon?',
                        a='Portionen ger cirka 590 kcal, 62,5 g protein och cirka 30 g fett, med cirka 16 g kolhydrater '
                          'från grönsakerna.'),
                   dict(q='Passar rätten den som har höga urinsyranivåer (gikt)?',
                        a='Den som har gikt bör äta den med stor måtta och undvika den koncentrerade buljongen, eftersom '
                          'långkokt nötkött innehåller mycket puriner.')]),
    459: dict(lead='Salade niçoise är ett mästerverk från Franska rivieran som förenar tonfisk, kokt ägg, haricots verts, '
                   'oliver och tomat med en dressing av olivolja och senap. Det glykemiska indexet är lågt (en kliniskt '
                   'granskad uppskattning, 20), och salladen är ett typiskt exempel på en komplett och mättande måltid.',
              tips=('En lunch i sig själv; proteinet i tonfisken och äggen och grönsakernas fibrer ger en jämn '
                    'blodsockerkurva under eftermiddagen.',
                    'Förväll haricots verts så att de förblir krispiga och gröna, och använd tonfisk i olivolja eller '
                    'vatten med en sked dijonsenap och äppelcidervinäger.',
                    'Salladen innehåller omega-3-fettsyror, kolin, D-vitamin och kalium.'),
              faq=[dict(q='Passar salade niçoise vid diabetes?',
                        a='Den är en av de bästa måltiderna; det glykemiska indexet och den glykemiska belastningen är '
                          'låga, och den mättar väl utan snabb stärkelse.'),
                   dict(q='Vad är näringsvärdet i en stor tallrik salade niçoise (300 g)?',
                        a='Tallriken ger cirka 280 kcal, 24 g protein, 16 g fett och cirka 8 g kolhydrater (varav 4 g '
                          'fibrer).'),
                   dict(q='Ändrar några små potatisar det glykemiska indexet?',
                        a='Två små kokta och avsvalnade potatisar ökar stärkelsen med bara cirka 10 g, och vinägern, oljan '
                          'och tonfisken håller det samlade glykemiska indexet lågt.')]),
    460: dict(lead='Gratin dauphinois (fransk potatisgratäng med grädde och ost) är en av de godaste festrätterna på '
                   'vintern, med potatisskivor i vitlök och grädde som gräddas i ugnen. Det glykemiska indexet är '
                   'medelhögt (en kliniskt granskad uppskattning, 65), och portionen behöver styras noga vid diabetes.',
              tips=('Nöj dig med två till tre matskedar som tillbehör till en bit kött eller kyckling och en stor grön '
                    'sallad, så dämpas stärkelseupptaget.',
                    'Du kan blanda blomkåls- eller zucchiniskivor med potatisskivorna till hälften, så halveras stärkelsen '
                    'och kalorierna medan den lyxiga krämiga konsistensen behålls.',
                    'Kombinationen av snabb potatisstärkelse och mycket mättat fett från grädden belastar '
                    'blodsockerregleringen när portionen blir för stor.'),
              faq=[dict(q='Varför är det glykemiska indexet för gratin dauphinois medelhögt (65)?',
                        a='Därför att det tunga fettet (grädde och ost) delvis bromsar upptaget av potatisstärkelsen, men '
                          'den samlade glykemiska belastningen förblir hög.'),
                   dict(q='Hur många kalorier finns i en vanlig portion gratäng (150 g)?',
                        a='Portionen innehåller cirka 265 kcal, 6 g protein, 15 g fett och 27 g kolhydrater.'),
                   dict(q='Hur kan jag njuta av gratängen utan att höja blodsockret?',
                        a='Ät salladens fibrer och proteinet först, och ät gratängen sist i måltiden i en portion på högst '
                          '100 g.')]),
    461: dict(lead='Klassisk fransk ostsufflé är luftens magi i matlagningen: en skör konsistens, lätt som ett moln, med '
                   'djup smak av gruyère och parmesan. Det glykemiska indexet är inte tillämpligt eftersom stärkelsen är '
                   'låg (cirka 6 g per 100 g), och rätten ger en förfinad restaurangupplevelse.',
              tips=('Ät den direkt när den kommer ut ur ugnen innan den sjunker ihop, och gör den till en lätt huvudrätt '
                    'med en sallad av portlak och ruccola med citrondressing.',
                    'Sufflén reser sig tack vare att äggvitorna vispas till fast skum; använd mycket lite mjöl till '
                    'grundsåsen och låt äggen och osten bära rätten.',
                    'En proteinrik ketorätt; protein bidrar till att bibehålla muskelmassa. Den som har hjärtsjukdom bör '
                    'vara uppmärksam på natriumet och fettet.'),
              faq=[dict(q='Höjer ostsufflé blodsockret?',
                        a='Den påverkar blodsockret mycket lite, eftersom kolhydraterna är få och proteinet är högt.'),
                   dict(q='Vad är näringsvärdet i 120 g ostsufflé?',
                        a='Portionen ger cirka 260 kcal, 14 g protein, 19 g fett och bara cirka 8 g kolhydrater.'),
                   dict(q='Passar ostsufflé vid keto?',
                        a='Den är en klassisk och utmärkt ketorätt som förenar ägg och franska ostar utan tillsatt '
                          'stärkelse.')]),
    462: dict(lead='Bovetegalett (galette de sarrasin) är Bretagnes stolthet: en tunn, mörk crêpe med krispiga kanter som '
                   'traditionellt görs av bovetemjöl. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, '
                   '45), och den är ett bättre alternativ till vanliga crêpes av vitt mjöl.',
              tips=('Fyll den med stekt ägg, ost och spenat eller stekt svamp (den kompletta bretonska varianten), så får '
                    'du en mättande och komplett frukost eller middag.',
                    'Bovetemjölet blandas bara med vatten och en nypa salt och får vila, och smeten gräddas sedan i en '
                    'mycket het platt stekpanna som smorts med lite smör.',
                    'Bovete är inte vete utan ett frö som innehåller rutin och D-chiro-inositol.'),
              faq=[dict(q='Är bovetegalett säker vid celiaki (glutenintolerans)?',
                        a='Ja, bovete är naturligt glutenfritt, under förutsättning att det inte blandats med vetemjöl vid '
                          'tillverkningen.'),
                   dict(q='Vad är näringsvärdet i en galett med ägg och ost (150 g)?',
                        a='Den ger cirka 370 kcal, 19 g protein, 16,5 g fett och cirka 36 g komplexa kolhydrater med '
                          'mycket fibrer.'),
                   dict(q='Hur påverkar galetten blodsockret jämfört med en vanlig crêpe?',
                        a='Bovetets fibrer och det låga glykemiska indexet (cirka 45) dämpar en kraftig '
                          'blodsockerstegring, och galetten mättar mer än en vanlig crêpe.')]),
    463: dict(lead='Tarte tatin är Frankrikes kända upp-och-nedvända äppelpaj: tjocka äppelskivor som karamelliserats i '
                   'smör och gräddats under ett lock av mör deg. Det glykemiska indexet är medelhögt (en kliniskt granskad '
                   'uppskattning, 58), och äpplets naturliga pektin dämpar sockrets effekt något.',
              tips=('Nöj dig med en tunn skiva och ät den ljummen efter en proteinrik lunch, och undvik att lägga söt '
                    'vaniljglass ovanpå.',
                    'Karamellisera äpplena med kanel och mycket lite socker eller naturliga sötningsmedel; äpplena avger '
                    'sitt eget socker, som karamelliseras naturligt med smöret.',
                    'Tillagade äpplen innehåller pektin som delvis bromsar upptaget av kolhydraterna, men karamellagret '
                    'kräver försiktighet vid diabetes och viktkontroll.'),
              faq=[dict(q='Höjer tarte tatin blodsockret snabbt?',
                        a='Det glykemiska indexet är medelhögt (cirka 58), och upptaget är långsammare än för sockerkaka '
                          'tack vare smörets fett och äpplets fibrer, men den förblir en söt bakelse där portionen behöver '
                          'räknas in.'),
                   dict(q='Hur många kalorier finns i en skiva tarte tatin (100 g)?',
                        a='Portionen innehåller cirka 290 kcal, 3 g protein, 10,5 g fett och cirka 46 g kolhydrater och '
                          'socker.'),
                   dict(q='Vad är skillnaden mellan tarte tatin och amerikansk äppelpaj?',
                        a='I tarte tatin karamelliseras äpplena direkt i botten av pannan, degen läggs ovanpå och pajen '
                          'vänds efter gräddningen; den innehåller också mindre deg än den klassiska pajen.')]),
    464: dict(lead='Wienerschnitzel är en tunn skiva magert kalvkött som bankats noggrant och täckts med ett gyllene, '
                   'krispigt lager av ströbröd och ägg. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, '
                   '35), eftersom ströbrödslagret är en begränsad mängd stärkelse tillsammans med köttets rena protein.',
              tips=('Pressa en färsk citronklyfta över den och ät den med en fräsch grön sallad i stället för de vanliga '
                    'pommes frites, så håller du kalorierna i schack.',
                    'Tillaga den i airfryer eller i ugnen med lite olja i stället för att fritera den i mycket olja; '
                    'kalvköttet blir fantastiskt mört.',
                    'Rik på animaliskt protein, zink och järn; kommersiell fritering ökar mängden oxiderat omega-6-fett, '
                    'så hemlagad i ugn är ett betydligt bättre val.'),
              faq=[dict(q='Passar wienerschnitzel vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 35), det mesta av vikten är protein, och '
                          'ströbrödslagret påverkar blodsockret lite.'),
                   dict(q='Vad är näringsvärdet i en portion wienerschnitzel av kalv (150 g)?',
                        a='Portionen innehåller cirka 420 kcal, 39 g protein, 21 g fett och 18 g kolhydrater från '
                          'panering.'),
                   dict(q='Vad är skillnaden mellan äkta wienerschnitzel och kycklingschnitzel?',
                        a='Den äkta är skyddad i österrikisk lag och görs bara av kalvkött, medan den som är vanlig i '
                          'världen görs av kyckling- eller kalkonbröst.')]),
    465: dict(lead='Spätzle är de traditionella lantliga äggnudlarna från södra Tyskland och Österrike: färska, '
                   'oregelbundna bitar med en omtyckt seg konsistens och varm smak. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 52), eftersom den rikliga äggulan bromsar stärkelsen.',
              tips=('Använd dem som tillbehör i en avvägd portion (en halv kopp) till kött och stekta grönsaker, så håller '
                    'du måltidens samlade kolhydrater i schack.',
                    'Koka dem snabbt i kokande vatten och fräs dem sedan i en panna med lite olivolja, en nypa muskot och '
                    'hackad persilja, och undvik att dränka dem i fet ost.',
                    'Den höga andelen ägg i spätzledegen sänker det glykemiska indexet jämfört med vanlig vit pasta, men '
                    'de är fortfarande stärkelse där portionen behöver styras vid diabetes.'),
              faq=[dict(q='Är spätzle bättre än vanlig pasta vid diabetes?',
                        a='Ja, något bättre; det glykemiska indexet (cirka 52) är lägre tack vare den höga äggandelen, men '
                          'måtta i mängden är avgörande.'),
                   dict(q='Hur många kalorier finns i 150 g kokta spätzle?',
                        a='Portionen innehåller cirka 250 kcal, 10 g protein, 2 g fett och cirka 46 g kolhydrater.'),
                   dict(q='Kan spätzle göras med fullkornsmjöl?',
                        a='Ja, att blanda i fullkornsvetemjöl eller dinkelmjöl ger mer fibrer och en utmärkt lantlig, '
                          'nötig smak.')]),
    466: dict(lead='Den ljumma tyska potatissalladen (Kartoffelsalat) skiljer sig från klassiska sallader genom sin lätta '
                   'dressing av vinäger, buljong och senap i stället för fet majonnäs. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 52), tack vare vinägerns ättiksyra och att stärkelsen svalnar.',
              tips=('Ät en portion stor som en knytnäve med en bit protein och en grön sallad; vinägerns syra hjälper till '
                    'att bromsa nedbrytningen av hela måltiden.',
                    'Koka potatisen med skalet, skär den och låt den svalna något innan du blandar den med vinäger och '
                    'senap; när potatisen svalnar bildas resistent stärkelse.',
                    'Ättiksyran i vinägerdressingen bidrar till att potatisen ger ett lägre glykemiskt index.'),
              faq=[dict(q='Varför är det glykemiska indexet för tysk potatissallad lågt (52) jämfört med potatismos?',
                        a='Tack vare ättiksyran i dressingen, att potatisbitarna är hela och att resistent stärkelse '
                          'bildas när de svalnar.'),
                   dict(q='Vad är näringsvärdet i 150 g potatissallad med vinäger?',
                        a='Den ger cirka 175 kcal, 3 g protein, 5 g fett och 28,5 g kolhydrater som tas upp i måttlig '
                          'takt.'),
                   dict(q='Innehåller salladen mättat fett eller majonnäs?',
                        a='Den traditionella sydtyska varianten bygger helt på buljong, vinäger, senap och lite olja och '
                          'innehåller ingen majonnäs.')]),
    467: dict(lead='Tysk linsgryta (Linseneintopf) är en varm, lantlig vinterrätt som förenar bruna linser med morot, '
                   'selleri och purjolök och en karaktäristisk skvätt vinäger. Det glykemiska indexet är lågt (en kliniskt '
                   'granskad uppskattning, 35), och grytan ger mycket mättnad och fibrer.',
              tips=('En stor och komplett rätt som inte behöver något bröd till; linsernas fibrer och vegetabiliska '
                    'protein mättar i flera timmar.',
                    'Tillsätt en tesked äppelcidervinäger den sista minuten av tillagningen; vinägern är den traditionella '
                    'tyska hemligheten som lyfter fram linsernas sötma.',
                    'Grytan innehåller järn, magnesium och folat, och linsernas fibrer fermenteras i tarmen och bildar '
                    'smörsyra.'),
              faq=[dict(q='Passar tysk linsgryta vid diabetes?',
                        a='Mycket bra; det glykemiska indexet är lågt och den glykemiska belastningen måttlig, och '
                          'glukosen frisätts mycket långsamt i blodet.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i en stor tallrik linsgryta (300 g)?',
                        a='Tallriken ger cirka 405 kcal, 25,5 g vegetabiliskt protein, 19,5 g fibrer och cirka 43,5 g '
                          'komplexa nettokolhydrater.'),
                   dict(q='Ger grytan gaser i magen?',
                        a='Långsam tillagning av linserna med aromatiska grönsaker som selleri, spiskummin och vinäger '
                          'bryter ned de komplexa sockerarterna och minskar uppblåstheten till ett minimum.')]),
    468: dict(lead='Bayersk pretzel är det kända bakverket med blank brun yta, grovt salt och den ikoniska knutformen från '
                   'Tyskland. Det glykemiska indexet är högt (en kliniskt granskad uppskattning, 78) på grund av det vita '
                   'mjölet och den snabba nedbrytningen, vilket kräver stor försiktighet och måtta vid diabetes.',
              tips=('Om du vill äta en, dela den stora pretzeln och ät bara en fjärdedel efter att ha skrapat bort det '
                    'mesta av saltet, och ät den med keso eller kokt ägg för att bromsa stärkelseupptaget.',
                    'Degen doppas före gräddningen i en särskild alkalisk lösning som ger den brun färg; för en bättre '
                    'variant hemma kan du använda fullkornsmjöl och mindre salt på ytan.',
                    'Dubbel klinisk varning: snabb stärkelse som höjer blodsockret mycket snabbt (cirka 78) och mycket '
                    'natrium på ytan som kan höja blodtrycket.'),
              faq=[dict(q='Varför är det glykemiska indexet för pretzel högt?',
                        a='Därför att den görs av fint raffinerat vitt mjöl som gräddas i hög värme, vilket gör att den '
                          'snabbt omvandlas till glukos i blodet.'),
                   dict(q='Vad är näringsvärdet i en medelstor bayersk pretzel (90 g)?',
                        a='Den innehåller cirka 305 kcal, 8 g protein, 2,5 g fett och cirka 60 g snabba kolhydrater.'),
                   dict(q='Hur kan den som har diabetes äta pretzel säkrare?',
                        a='Nöj dig med en fjärdedel vid festliga tillfällen, bred på en ost med mycket protein och låt bli '
                          'att äta de grova saltkornen.')]),
    469: dict(lead='Österrikisk äppelstrudel (Apfelstrudel) är den kejserliga bakverksrullen fylld med äpplen kryddade med '
                   'kanel, russin, kokos och nötter i en mycket tunn deg. Det glykemiska indexet är lågt (en kliniskt '
                   'granskad uppskattning, 55), och fibrerna i äpplena och nötterna ger den en bättre näringsbalans.',
              tips=('Njut av en liten bit som festlig efterrätt efter en proteinrik lunch, och strö äkta kanel över i '
                    'stället för florsocker.',
                    'Hemligheten bakom en bättre strudel är att fylla rullen med rikligt med äpplen och valnötter och att '
                    'använda mycket tunna lager filodeg med lite smör.',
                    'Kanelen i fyllningen ger smak, och fettet i valnötterna bromsar upptaget av det naturliga sockret i '
                    'äpplena och russinen.'),
              faq=[dict(q='Passar äppelstrudel för den som vill hålla blodsockret i schack?',
                        a='Det glykemiska indexet ligger på gränsen 55 (lågt); den är betydligt bättre än fet tårta, men '
                          'mängden russin och tillsatt socker behöver beaktas.'),
                   dict(q='Vad är näringsvärdet i 100 g äppelstrudel?',
                        a='Portionen innehåller cirka 245 kcal, 3 g protein, 7 g fett och cirka 42 g kolhydrater som tas '
                          'upp i måttlig takt.'),
                   dict(q='Är vaniljsåsen som serveras till ett dåligt val?',
                        a='Kommersiell vaniljsås innehåller mycket tillsatt socker och höjer kalorierna och det glykemiska '
                          'indexet kraftigt; det är bättre att hoppa över den och äta strudeln som den är.')]),
    470: dict(lead='Kaiserschmarrn (den österrikiska kejsarpannkakan i bitar) är Alpernas älskade efterrätt: en tjock och '
                   'luftig pannkaka som slits i bitar i pannan, karamelliseras med smör och russin och serveras med '
                   'plommonkompott. Det glykemiska indexet är medelhögt (en kliniskt granskad uppskattning, 64), och den '
                   'är en mäktig söt rätt som är gjord för att delas.',
              tips=('En stor och lockande rätt; dela den alltid med två eller tre personer efter en promenad eller '
                    'skidtur, och ät den inte som en ensam måltid.',
                    'Äggvitorna vispas som maräng så att den blir luftig som ett moln; med havremjöl och mindre tillsatt '
                    'socker i pannan blir den ett skonsammare val för blodsockret hemma.',
                    'Rik på protein tack vare de många äggen i smeten, men vitt vetemjöl och karamelliserat socker höjer '
                    'rättens samlade glykemiska belastning.'),
              faq=[dict(q='Höjer kaiserschmarrn blodsockret snabbt?',
                        a='Ja, i måttlig grad (cirka 64) eftersom stärkelsen och karamellen bryts ned snabbt, så den som '
                          'har diabetes bör vara försiktig med den.'),
                   dict(q='Hur många kalorier finns i en vanlig portion kaiserschmarrn (150 g)?',
                        a='Portionen ger cirka 390 kcal, 11 g protein, 13 g fett och cirka 57 g kolhydrater och socker.'),
                   dict(q='Hur dämpar plommonkompotten effekten?',
                        a='Naturlig osötad plommonkompott (Zwetschkenröster) innehåller fibrer och sorbitol (en naturlig '
                          'sockeralkohol), och båda bromsar upptaget.')]),
    471: dict(lead='Grekisk kycklinggyros i pitabröd är en känd och modern gatumat: skivor av kyckling kryddad med örter '
                   'och citron, rullade i pitabröd med tomat, lök och tzatziki. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 54), eftersom kycklingens protein och yoghurtens fett bromsar brödets '
                   'stärkelse.',
              tips=('Beställ gyros utan pommes frites i rullen, och be om mer tzatziki och tomat- och gurksallad.',
                    'Grilla kycklingskivor kryddade med timjan, vitlök och citron hemma och rulla in dem i '
                    'fullkornspitabröd med gurka och naturell grekisk yoghurt.',
                    'En balanserad och näringsrik måltid med protein och fett; det viktiga är att hålla koll på '
                    'pitabrödets storlek och saltet i marinaden.'),
              faq=[dict(q='Passar kycklinggyros när man bantar och vid diabetes?',
                        a='Ja, ett utmärkt val om pommes fritesen tas bort; det glykemiska indexet är lågt (cirka 54) och '
                          'den mättar länge.'),
                   dict(q='Vad är näringsvärdet i en komplett kycklinggyros (250 g)?',
                        a='Rullen ger cirka 420 kcal, 32 g protein, 15 g fett och cirka 38 g kolhydrater från pitabrödet '
                          'och grönsakerna.'),
                   dict(q='Är tzatziki ett bra val i rullen?',
                        a='Ja, mycket; den bygger på grekisk yoghurt, gurka, olivolja och vitlök och innehåller inte '
                          'socker som majonnäs och ketchup.')]),
    472: dict(lead='Grekisk souvlaki är spett av magert kött eller kyckling som grillas över kol och kryddas med olivolja, '
                   'citron och vild oregano. Det glykemiska indexet är inte tillämpligt eftersom rätten saknar '
                   'kolhydrater, och den är ett levande exempel på medelhavsmat för den aktiva.',
              tips=('Ät två spett souvlaki med gaffel tillsammans med en grekisk sallad med fetaost och olivolja, så får '
                    'du en utmärkt måltid vid keto eller bantning.',
                    'En marinad av citron, olivolja, vitlök och örter räcker för att möra köttet; grilla det på medelhög '
                    'värme så att det förblir mört och saftigt utan att brännas.',
                    'Rent protein av hög biologisk kvalitet; protein bidrar till att bibehålla muskelmassa.'),
              faq=[dict(q='Höjer souvlaki blodsockret?',
                        a='Nej; det är grillat kött utan kolhydrater, och det glykemiska indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g souvlaki?',
                        a='Portionen ger cirka 320 kcal (beroende på kötttyp), med 40 g protein och cirka 16,5 g fett.'),
                   dict(q='Är souvlaki det bästa valet på grekiska restauranger?',
                        a='Ja, det är ett utmärkt val vid diabetes och bantning, eftersom det är äkta grillat kött som '
                          'inte är processat och saknar dolda stärkelserika såser.')]),
    473: dict(lead='Grekisk tzatziki är en klassisk, fräsch dipp gjord på silad grekisk yoghurt, riven och urpressad '
                   'gurka, vitlök, olivolja och färsk dill. Det glykemiska indexet är inte tillämpligt eftersom den saknar '
                   'nettostärkelse.',
              tips=('Använd den som ett bra alternativ till kommersiella såser som majonnäs; doppa gurk- och morotsstavar '
                    'i den eller lägg den på grillat kött.',
                    'Pressa den rivna gurkan ordentligt i en duk för att få bort överflödigt vatten innan du blandar den '
                    'med den tjocka yoghurten, så förblir konsistensen krämig och fast.',
                    'Grekisk yoghurt ger levande mjölksyrabakterier, protein och kalcium, och vitlöken ger allicin.'),
              faq=[dict(q='Är tzatziki tillåten vid keto och lågkolhydratkost?',
                        a='Ja, den passar mycket bra; kolhydraterna är nästan obefintliga och den innehåller protein och '
                          'fett.'),
                   dict(q='Vad är näringsvärdet i 50 g tzatziki (två matskedar)?',
                        a='Portionen innehåller cirka 50 kcal, 2,4 g protein, 3,4 g fett och mindre än 2 g kolhydrater.'),
                   dict(q='Passar tzatziki den som har laktosintolerans?',
                        a='Silad grekisk yoghurt innehåller mycket mindre laktos än vanlig mjölk, och de flesta med '
                          'lindrig intolerans tål den.')]),
    474: dict(lead='Spanakopita är den kända grekiska pajen med spenat och fetaost, med protein och förtrollande örtsmak '
                   'under tunna, krispiga lager av filodeg. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 48), eftersom spenatens fibrer och fetaostens fett bromsar stärkelseupptaget.',
              tips=('Ät en medelstor fyrkantig bit stor som en handflata som lunch eller lätt middag med en färsk sallad '
                    'av tomat och gurka.',
                    'Pressa ur spenaten ordentligt efter att den fått mjukna med lök och dill, och pensla filodegsarken '
                    'med olivolja i stället för industriellt smör.',
                    'Spenat innehåller folat, lutein, järn och magnesium; den som har njursten bör vara försiktig eftersom '
                    'spenat innehåller oxalat.'),
              faq=[dict(q='Höjer spanakopita blodsockret snabbt?',
                        a='Nej, det glykemiska indexet är lågt (cirka 48), och det mesta av fyllningen är spenat, ägg och '
                          'ost och inte deg, så upptaget är lugnt.'),
                   dict(q='Hur många kalorier finns i en vanlig bit spanakopita (120 g)?',
                        a='Biten innehåller cirka 310 kcal, 10 g protein, 17 g fett och cirka 30 g kolhydrater.'),
                   dict(q='Är fetaosten i pajen lätt att smälta?',
                        a='Äkta grekisk fetaost görs av får- och getmjölk, och många upplever den som lättare att smälta '
                          'än industriella ostar av komjölk.')]),
    475: dict(lead='Tiropita är den gyllene grekiska ostpajen som doftar av fetaost, ricotta och ägg som gräddats i spröda '
                   'filodegsark. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 50), och pajen ger '
                   'proteinrik mättnad med en varm medelhavssmak.',
              tips=('En triangelformad bit räcker helt till frukost; ät den med en kopp örtte och en sallad av gurka och '
                    'sallat för att få de fibrer som pajen saknar.',
                    'Blanda den skarpa fetaosten med ricotta eller keso med låg salthalt för att minska natriumet, med en '
                    'nypa svartpeppar och torkad mynta som ger en härlig fräschhet.',
                    'En paj med mycket kalcium, protein och fett; portionen behöver styras vid högt blodtryck och högt '
                    'kolesterol på grund av fetaostens salthalt och fetthalt.'),
              faq=[dict(q='Vad är skillnaden mellan tiropita och spanakopita i effekten på blodsockret?',
                        a='Tiropita saknar spenat och har därför mindre fibrer och fler kalorier från fett, men det '
                          'glykemiska indexet förblir lågt (cirka 50) tack vare ostens protein och fett.'),
                   dict(q='Vad är näringsvärdet i en medelstor bit tiropita (100 g)?',
                        a='Den ger cirka 295 kcal, 11 g protein, 16 g fett och cirka 26 g stärkelse från filodegen.'),
                   dict(q='Kan den gräddas i airfryer?',
                        a='Ja, mycket bra; 12 minuter räcker för att degen ska bli flagig och helt krispig utan extra '
                          'fett.')]),
    476: dict(lead='Briam är den grekiska sommarformen med ugnsrostade grönsaker: skivor av potatis, zucchini, aubergine '
                   'och tomat kryddade med jungfruolivolja, vitlök och persilja. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 30), och rätten är en grönsakssymfoni rik på fibrer och mineraler.',
              tips=('Ät en generös portion med en bit fetaost eller en grillad fiskfilé; en typisk medelhavsmåltid.',
                    'Grädda formen täckt med bakplåtspapper de första 40 minuterna och ta sedan bort papperet så att '
                    'grönsakerna får färg, kanterna karamelliseras och den naturliga tomatsåsen tjocknar.',
                    'Briam innehåller kalium, C-vitamin och olika fibrer; kalium bidrar till att bibehålla ett normalt '
                    'blodtryck.'),
              faq=[dict(q='Passar briam vid diabetes?',
                        a='Ja, mycket bra; det glykemiska indexet är lågt (cirka 30), och andelen potatis vägs upp av '
                          'vattenrika grönsaker och olivolja, vilket dämpar blodsockerstegringen.'),
                   dict(q='Hur många kalorier finns i en stor portion briam (250 g)?',
                        a='Portionen innehåller cirka 240 kcal (mest från olivoljan), med 5,5 g protein och 10,5 g fibrer.'),
                   dict(q='Vad skiljer briam från en vanlig ugnsform med grönsaker?',
                        a='Den långsamma rostningen i riklig jungfruolivolja med vitlök och persilja, som ger grönsakerna '
                          'en söt och smörig konsistens utan att vatten tillsätts.')]),
    477: dict(lead='Fasolada är Greklands nationalsoppa: den traditionella soppan på vita bönor som tillagas med riklig '
                   'olivolja, tomat, selleri och morot. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, '
                   '35), och soppan är en del av den traditionella kosten på de grekiska öarna, som Ikaria.',
              tips=('Ät en varm skål med sked tillsammans med svarta oliver och ruccola som en mättande vegetarisk lunch '
                    'som inte behöver något bröd till.',
                    'Blötlägg bönorna över natten och koka dem tills de är smöriga, och tillsätt jungfruolivoljan de sista '
                    '10 minuterna så att den förenas med buljongen till en lyxig, emulgerad konsistens.',
                    'Soppan innehåller lösliga fibrer, kalium, järn och magnesium.'),
              faq=[dict(q='Höjer fasolada blodsockret?',
                        a='Nej, vita bönor har ett lågt glykemiskt index (cirka 35), och fibrerna bromsar '
                          'stärkelseupptaget och mättar länge.'),
                   dict(q='Vad är näringsvärdet i en tallrik grekisk fasolada (300 g)?',
                        a='Tallriken ger cirka 420 kcal, 23 g vegetabiliskt protein, 20 g fibrer och cirka 46 g komplexa '
                          'nettokolhydrater.'),
                   dict(q='Varför kallar grekerna den nationalrätten?',
                        a='Därför att den historiskt var vanligt folks mat och förenade högt näringsvärde med låg kostnad.')]),
    478: dict(lead='Gemista hör till de godaste grekiska sommarrätterna: tomater, paprikor och zucchini fyllda med ris '
                   'kryddat med örter som dill och mynta, tomatkött och olivolja. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 50), och rätten ger en varm och aptitlig grönsaksmåltid.',
              tips=('Ät två fyllda grönsaker med en bit vit fetaost eller ett grillat kycklingbröst, så balanseras '
                    'proteinet med risets stärkelse.',
                    'Blanda riset med rikligt med hackade grönsaker och örter, och grädda formen med potatisskivor runt '
                    'omkring tills tomatskalen får en rökig smak.',
                    'Långsam tillagning av tomaterna med olivolja gör att lykopenet tas upp bättre.'),
              faq=[dict(q='Passar gemista vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 50) eftersom grönsaksskalet, örterna och '
                          'olivoljan bromsar upptaget av riset i fyllningen.'),
                   dict(q='Hur många kalorier finns i en portion med två gemista (300 g)?',
                        a='Portionen innehåller cirka 465 kcal, 10,5 g protein, 13,5 g fett och 78 g kolhydrater (varav 11 '
                          'g fibrer).'),
                   dict(q='Finns det varianter av gemista med köttfärs?',
                        a='Ja, köttfärs i fyllningen ger mer protein och sänker måltidens glykemiska belastning '
                          'ytterligare.')]),
    479: dict(lead='Kawareh (kokta lammfötter) är en traditionell rätt med en särskild plats på de orientaliska borden, '
                   'känd för sin geléartade buljong med naturligt upplöst kollagen. Det glykemiska indexet är inte '
                   'tillämpligt eftersom rätten saknar stärkelse.',
              tips=('Drick den varma buljongen med en skvätt citron och en krossad vitlöksklyfta och ät köttet med sked; '
                    'undvik att äta den med fatteh av vitt bröd och mycket ghee.',
                    'Den sjuder i många timmar på låg värme med mastix, kardemumma, lagerblad och lök tills gelatinet '
                    'lösts upp i buljongen och den blir klar och aromatisk.',
                    'Rätten innehåller mycket glycin, prolin och kollagen; den som har höga blodfetter eller högt '
                    'blodtryck bör äta den med måtta.'),
              faq=[dict(q='Höjer kawareh blodsockret?',
                        a='Nej, den höjer inte blodsockret eftersom den saknar stärkelse; det är fatteh och bröd till som '
                          'ger den kraftiga blodsockerstegringen.'),
                   dict(q='Vad är näringsvärdet i en tallrik kawareh med buljong (200 g)?',
                        a='Den ger cirka 420 kcal, 52 g protein (till stor del kollagen) och 24 g fett, med mindre än 1 g '
                          'kolhydrater.'),
                   dict(q='Vad innehåller kawareh?',
                        a='Den innehåller kollagen samt naturligt glukosamin och kondroitin från brosket.')]),
    480: dict(lead='Kokt kalvtunga hör till de godaste och mörast styckningsdelarna i det orientaliska och europeiska '
                   'köket, med sammetslena muskelfibrer som smälter i munnen och en fyllig, mild smak. Det glykemiska '
                   'indexet är inte tillämpligt eftersom den saknar kolhydrater, och den innehåller järn och B-vitaminer.',
              tips=('Skär den i skivor och ät den med en sås av vitlök, citron och olivolja, lite persilja och en fräsch '
                    'grön sallad.',
                    'Koka tungan med aromatiska kryddor tills den är helt genomkokt, och dra sedan av det vita yttre '
                    'skinnet medan den är varm, så återstår det möra, magra köttet.',
                    'Kalvtunga innehåller mycket zink, järn, B12-vitamin och kolin; B12-vitamin bidrar till nervsystemets '
                    'normala funktion, och järn bidrar till normal bildning av röda blodkroppar och hemoglobin.'),
              faq=[dict(q='Passar kalvtunga vid diabetes och bantning?',
                        a='Ja, mycket bra; den är muskelprotein utan stärkelse och mättar länge.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g kokt kalvtunga?',
                        a='Portionen innehåller cirka 340 kcal, 36 g protein och 21 g fett, utan socker.'),
                   dict(q='Är tungkött mycket fett?',
                        a='Det innehåller en måttlig mängd fett fördelat mellan fibrerna, vilket gör det mört, och mycket '
                          'mindre fett än lammfärs.')]),
    481: dict(lead='Lammhjärna är en traditionell, näringstät rätt med krämig, smörig konsistens och mycket mild smak, och '
                   'den hör till de livsmedel som innehåller mest fosfolipider. Det glykemiska indexet är inte tillämpligt '
                   'eftersom den saknar stärkelse.',
              tips=('Ät en avvägd portion (en halv hjärna), kokt eller lätt stekt i lite olja, med citronsaft, spiskummin '
                    'och vitlök och grovt bröd eller grönsaker.',
                    'Blötlägg den i kallt vatten med vinäger för att få bort blodkärlen, och låt den sjuda varsamt i några '
                    'minuter med citronsaft och lagerblad så att den behåller sin krämiga fasthet.',
                    'Viktig klinisk varning: hjärna har den högsta kolesterolhalten av alla animaliska livsmedel (mer än 2 '
                    '000 mg/100 g) och ska därför undvikas vid familjär hyperkolesterolemi och åderförkalkning.'),
              faq=[dict(q='Höjer lammhjärna blodsockret?',
                        a='Nej, den höjer inte blodsockret eftersom den saknar kolhydrater; risken ligger i fetthalten och '
                          'den mycket höga kolesterolhalten.'),
                   dict(q='Vad är näringsvärdet i 100 g lammhjärna?',
                        a='Portionen innehåller cirka 145 kcal, 11 g protein och 11 g fett (främst fosfolipider), med '
                          'nästan inga kolhydrater.'),
                   dict(q='Vad innehåller lammhjärna?',
                        a='Den innehåller omega-3-fettsyran DHA och fosfatidylserin, som är byggstenar i hjärncellernas '
                          'membran.')]),
    482: dict(lead='Sitti zbaqi är en av de äldsta traditionella vinterrätterna i det levantinska köket, känd för sin '
                   'harmoniska blandning av bruna linser och färska mangoldblad med citronsaft, vitlök, koriander och '
                   'degbitar. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 40), och rätten är en '
                   'varm och mättande måltid med järn.',
              tips=('Ät en varm skål med sked och en extra skvätt citron; mangoldens och linsernas fibrer mättar länge '
                    'utan att du behöver något bröd.',
                    'Minska mängden degbitar och öka mängden mangold och linser, och fräs vitlöken och koriandern i '
                    'jungfruolivolja de sista minuterna, så bevaras den äkta levantinska smaken.',
                    'Linserna och mangolden ger järn, magnesium och kalium, och den naturliga citronsaften innehåller '
                    'C-vitamin; C-vitamin ökar järnupptaget.'),
              faq=[dict(q='Passar sitti zbaqi vid diabetes och insulinresistens?',
                        a='Ja, mycket bra; det glykemiska indexet är lågt (cirka 40), och de rikliga fibrerna i mangolden '
                          'och linserna dämpar kraftiga blodsockertoppar.'),
                   dict(q='Vad är näringsvärdet i en vanlig tallrik sitti zbaqi (300 g)?',
                        a='Tallriken ger cirka 465 kcal, 22 g vegetabiliskt protein, 17 g fibrer och cirka 55 g komplexa '
                          'nettokolhydrater.'),
                   dict(q='Varför heter rätten sitti zbaqi?',
                        a='Det är ett gammalt och lustigt levantinskt namn som syftar på hur snabbt och enkelt rätten '
                          'lagas och läggs upp; den bygger främst på linser, mangold och citron.')]),
    483: dict(lead='Haraq osbao från Damaskus är det äkta levantinska kökets stolthet: en mosaik av bruna linser och '
                   'degremsor som tillagas i en syrlig sås av tamarind och granatäppelsirap och garneras med krispigt '
                   'bröd, karamelliserad lök och granatäpplekärnor. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 45) tack vare de rikliga linserna och tamarindens syra.',
              tips=('Ät den som huvudrätt med sked; fokus på de färska granatäpplekärnorna och koriandern, och undvik att '
                    'ta mycket av de friterade brödbitarna ovanpå.',
                    'Byt ut det friterade vita brödet mot ugnsrostat grovt bröd, och använd naturlig blötlagd tamarind '
                    'utan tillsatt socker.',
                    'Syran i tamarinden och den naturliga granatäppelsirapen bidrar till rättens låga glykemiska index.'),
              faq=[dict(q='Passar haraq osbao vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 45) tack vare linserna och den naturliga '
                          'syran, och det viktiga är att begränsa den stekta löken och brödet ovanpå.'),
                   dict(q='Vad är näringsvärdet i en tallrik haraq osbao (250 g)?',
                        a='Den ger cirka 550 kcal, 21 g protein, 14 g fett (mest från olivolja) och 90 g kolhydrater rika '
                          'på fibrer (varav 18 g fibrer).'),
                   dict(q='Varför har rätten fått sitt lustiga namn?',
                        a='Enligt folkberättelsen kunde kocken inte vänta på att få smaka den syrliga och förtrollande '
                          'rätten, stack ned fingret medan den kokade och brände sig – namnet betyder ungefär "den som '
                          'bränner fingret".')]),
    484: dict(lead='Kibbeh i form (levantinsk ugnskibbeh) är ett bättre val för den som älskar kibbeh: två lager av magert '
                   'kött och bulgur som omsluter en fyllning av kryddad köttfärs och pinjenötter och gräddas i ugnen. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 50), och rätten är ett bättre '
                   'alternativ till kibbeh friterad i olja.',
              tips=('Ät en medelstor bit stor som en handflata med en gurksallad med yoghurt eller en grön sallad, så blir '
                    'måltiden balanserad.',
                    'Grädda den i ugnen med lite olivolja eller naturlig ghee i stället för att dränka den i fett, och öka '
                    'andelen magert kött i förhållande till bulguren.',
                    'Bulgur är ett fullkornsvete med mycket fibrer och lågt glykemiskt index, och tillsammans med köttets '
                    'protein mättar den väl och ger en jämn blodsockerkurva.'),
              faq=[dict(q='Är kibbeh i form bättre vid diabetes än friterad kibbeh?',
                        a='Ja, betydligt bättre; ugnsbakning sparar hundratals kalorier och undviker det oxiderade fett '
                          'som bildas vid fritering.'),
                   dict(q='Vad är näringsvärdet i en bit kibbeh i form (150 g)?',
                        a='Biten innehåller cirka 405 kcal, 24 g protein, 21 g fett och cirka 31,5 g kolhydrater som tas '
                          'upp långsamt.'),
                   dict(q='Passar kibbeh i form vid viktnedgång?',
                        a='Ja, ett bra val; en bit mättar i många timmar och ger protein och järn; protein bidrar till att '
                          'bibehålla muskelmassa.')]),
    485: dict(lead='Kibbeh labanieh är en av kungarna på det aleppiska och levantinska bordet: fyllda kibbehbollar som '
                   'tillagas i en sidenlen yoghurtsås kryddad med vitlök och torkad mynta. Det glykemiska indexet är lågt '
                   '(en kliniskt granskad uppskattning, 45), och rätten förenar god smak med mild yoghurt.',
              tips=('Ät två till tre kibbehbollar med en generös slev varm yoghurtsås, och ät dem med sked utan att behöva '
                    'ris till.',
                    'Koka kibbehbollarna i kokande vatten i tre minuter innan du lägger dem i den kokta yoghurten, så '
                    'håller de ihop och yoghurtens smak förblir ren.',
                    'Den kokta yoghurten ger kalcium och mjölksyra.'),
              faq=[dict(q='Höjer kibbeh labanieh blodsockret snabbt?',
                        a='Nej, det glykemiska indexet är lågt (cirka 45), och proteinet i yoghurten och köttet dämpar '
                          'kraftiga blodsockertoppar.'),
                   dict(q='Hur många kalorier finns i en portion kibbeh labanieh (två bollar med yoghurt, 300 g)?',
                        a='Portionen ger cirka 320 kcal, 22 g protein, 14 g fett och cirka 26 g kolhydrater som tas upp i '
                          'måttlig takt.'),
                   dict(q='Förlorar kokt yoghurt sina mjölksyrabakterier?',
                        a='Värmen dödar de levande bakterierna, men yoghurten behåller allt sitt protein och kalcium.')]),
    486: dict(lead='Aleppisk kibbeh grillad på spett (över kol) är ett mästerverk i det aleppiska köket: en blandning av '
                   'magert nöt- och lammkött med fin bulgur, valnötter och aleppiska kryddor som formas på spett och '
                   'grillas över kol. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 42), och den har '
                   'en oemotståndlig rökig grillsmak.',
              tips=('Ät spettet med en piyazsallad (persilja, lök och sumak), en skvätt citron och grillade grönsaker som '
                    'lök och tomat.',
                    'I spettkibbeh är förhållandet mellan kött och bulgur 3 till 1 till köttets fördel, vilket gör att den '
                    'håller ihop på spettet och innehåller mycket protein.',
                    'Grillning över kol låter överflödigt fett droppa av, medan järnet och zinken behålls, och valnötterna '
                    'ger den vegetabiliska omega-3-fettsyran ALA.'),
              faq=[dict(q='Passar aleppisk spettkibbeh vid insulinresistens?',
                        a='Ja, ett utmärkt val; det glykemiska indexet är lågt (cirka 42) och andelen bulgur är liten '
                          'jämfört med proteinet och fettet.'),
                   dict(q='Vad är näringsvärdet i ett vanligt grillat kibbehspett (150 g)?',
                        a='Spettet innehåller cirka 440 kcal, 27 g protein, 27 g fett och 24 g kolhydrater som tas upp '
                          'långsamt.'),
                   dict(q='Innehåller spettkibbeh härdat fett?',
                        a='Nej, fettet är naturligt och kommer från lammets svansfett och valnötterna, och inga '
                          'industriella vegetabiliska oljor används.')]),
    487: dict(lead='Kibbeh safarjalieh är en pärla i det anrika aleppiska köket som förenar kibbehbollar och köttbitar med '
                   'kvittentärningar som tillagas i en buljong av granatäpple, granatäppelsirap, vitlök och mynta. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 45), och rätten har en unik smak som '
                   'förenar sött och syrligt.',
              tips=('Njut av rätten varm med sked; kvittentärningarna innehåller mycket fibrer och ersätter ris eller vitt '
                    'bröd.',
                    'Kvittenen kokas tills den mjuknar utan att falla sönder; naturlig granatäpplejuice och traditionell '
                    'granatäppelsirap utan industriellt socker är hemligheten bakom rättens kvalitet.',
                    'Kvitten är en höstfrukt som innehåller mycket pektin och garvämnen (tanniner).'),
              faq=[dict(q='Höjer kvittenens sötma blodsockret i kibbeh safarjalieh?',
                        a='Nej, kvitten är en frukt med lite socker och mycket strama fibrer, och rättens glykemiska index '
                          'är lågt (cirka 45) tack vare köttet, myntan och vitlöken.'),
                   dict(q='Hur många kalorier finns i en tallrik kibbeh safarjalieh (300 g)?',
                        a='Tallriken ger cirka 330 kcal, 21 g protein, 15 g fett och cirka 28 g kolhydrater.'),
                   dict(q='Vad innehåller kvitten?',
                        a='Kvitten innehåller pektin och garvämnen (tanniner), och den räknas som en av de mildaste '
                          'frukterna för magen.')]),
    488: dict(lead='Levantinsk yabraq (vinblad fyllda med kött och ris och tillagade med vitlök och citron) är sultanen '
                   'bland festrätterna i Damaskus: mjuka vinbladsrullar som smälter i munnen i en god, syrlig buljong. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 35), eftersom vinbladens fibrer och '
                   'köttets fett bromsar upptaget av riset.',
              tips=('Ät 6 till 8 rullar med de kokta vitlöksklyftorna och en bit av lammrevbenen som tillagats med dem, så '
                    'får du en proteinrik mättnad som håller länge.',
                    'Den levantinska hemligheten är rikligt med vitlöksklyftor, citronsaft och torkad mynta mellan lagren, '
                    'mindre ris och mer magert kött i fyllningen.',
                    'Vinblad innehåller polyfenoler och kalium.'),
              faq=[dict(q='Passar yabraq med kött vid diabetes jämfört med yalanji?',
                        a='Yabraq med kött är betydligt bättre; andelen ris är mindre, och proteinet, fettet och '
                          'citronsyran sänker det glykemiska indexet till cirka 35.'),
                   dict(q='Vad är näringsvärdet i en vanlig portion yabraq (200 g, 7–8 rullar)?',
                        a='Portionen innehåller cirka 390 kcal, 24 g protein, 20 g fett och cirka 28 g kolhydrater som '
                          'smälts långsamt.'),
                   dict(q='Vad innehåller yabraqbuljongen med citron och vitlök?',
                        a='Det är en köttbuljong med aminosyror, naturligt C-vitamin från citronen och allicin från den '
                          'kokta vitlöken.')]),
    489: dict(lead='Sheikh al-mahshi (zucchini i yoghurt, ablama) är en förnäm festrätt där små zucchini fylls med '
                   'köttfärs stekt med enbart pinjenötter, utan ett enda riskorn, och läggs i kokt yoghurt. Det glykemiska '
                   'indexet är inte tillämpligt eftersom den samlade stärkelsen är låg (cirka 6 g per 100 g), och rätten '
                   'passar vid keto och insulinresistens.',
              tips=('Ät 3 till 4 zucchini med yoghurten med sked som en komplett huvudrätt; den ger proteinrik mättnad '
                    'utan att du behöver någon extra risrätt.',
                    'Rosta de fyllda zucchinina i airfryer eller ugn med lite olja i stället för att fritera dem i mycket '
                    'olja, så förblir rätten lätt.',
                    'Zucchini är en lätt och vattenrik grönsak, yoghurten ger kalcium och mjölksyra, och köttet ger '
                    'protein.'),
              faq=[dict(q='Varför är sheikh al-mahshi den fyllda grönsaksrätt som passar bäst vid diabetes?',
                        a='Därför att den saknar ris och stärkelse; fyllningen är bara kött och pinjenötter, så den '
                          'påverkar blodsockret mycket lite.'),
                   dict(q='Vad är näringsvärdet i 300 g sheikh al-mahshi med yoghurt?',
                        a='Portionen ger cirka 555 kcal, 39 g protein, 33 g fett och cirka 18 g nettokolhydrater som '
                          'enbart kommer från zucchinin och yoghurten.'),
                   dict(q='Passar sheikh al-mahshi vid keto?',
                        a='Den är en klassisk levantinsk ketorätt som mättar väl med mycket få kolhydrater.')]),
    490: dict(lead='Levantinsk manzaleh (aubergine med köttfärs) är en känd hemlagad ugnsrätt som förenar lager av grillad '
                   'aubergine och kryddad köttfärs med naturlig tomatsås och pinjenötter. Det glykemiska indexet är lågt '
                   '(en kliniskt granskad uppskattning, 32), och rätten är en varm och mättande måltid.',
              tips=('Ät den med gaffel som huvudrätt till lunch med en grön sallad, och undvik att doppa vitt bröd i den, '
                    'så hålls blodsockret i schack.',
                    'Grilla auberginskivorna i ugnen eller i airfryer efter att ha penslat dem med lite olivolja i stället '
                    'för att fritera dem, så suger de inte upp för mycket olja.',
                    'Auberginens skal innehåller antocyaninen nasunin.'),
              faq=[dict(q='Passar manzaleh med aubergine när man bantar och vid diabetes?',
                        a='Ja, mycket bra om auberginen grillas; det glykemiska indexet är lågt (cirka 32) och auberginens '
                          'fibrer mättar väl med måttligt antal kalorier.'),
                   dict(q='Hur många kalorier finns i en vanlig portion manzaleh (250 g)?',
                        a='Portionen innehåller cirka 440 kcal, 26 g protein, 26 g fett och cirka 27,5 g kolhydrater '
                          '(varav 9,5 g fibrer).'),
                   dict(q='Vad är skillnaden mellan levantinsk manzaleh och egyptisk moussaka?',
                        a='Manzaleh bygger på lager av aubergine fylld med köttfärs och pinjenötter i en ordnad form, '
                          'medan moussakan skärs i tärningar och innehåller paprika och ibland kikärter.')]),
    491: dict(lead='Halabessa (egyptiska varma kikärter) är den mest kända heta vinterdrycken längs Nilens strandpromenad: '
                   'kokta kikärter i en frisk röd buljong av tomat, vitlök, spiskummin, chili och citron. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 25), och den förenar en god dryck med värdet av en '
                   'mättande måltid.',
              tips=('Drick den varma buljongen och ät kikärterna med sked ur koppen; en varm kvällsmåltid som håller '
                    'vinterhungern borta nästan utan fett och utan socker.',
                    'Blötlägg kikärterna i 12 timmar och byt vatten för att minska gasbildningen, och koka dem sedan med '
                    'tomatjuice, spiskummin och citronsaft utan industriella buljongtärningar.',
                    'Kikärterna innehåller lösliga fibrer, och spiskummin och chili ger rätten dess karaktär.'),
              faq=[dict(q='Höjer halabessa blodsockret vid diabetes?',
                        a='Nej; kikärter har ett av de lägsta glykemiska indexen (cirka 25), och buljongen innehåller lite '
                          'fett och inget socker, vilket gör den till ett lätt val när blodsockret ska hållas i schack.'),
                   dict(q='Vad är näringsvärdet i en vanlig kopp halabessa (kikärter och buljong, 250 g)?',
                        a='Koppen ger cirka 240 kcal, 13 g vegetabiliskt protein, 11 g fibrer och lite fett (cirka 4,5 g).'),
                   dict(q='Är chilin i halabessa skonsam för magen?',
                        a='Chilin är valfri och bör användas med måtta; den som har magkatarr eller IBS bör nöja sig med '
                          'spiskummin, citron och tomat.')]),
    492: dict(lead='Marockansk bissara med mynta och spiskummin är en varm folksoppa från Maghreb som görs av krossade '
                   'torkade bondbönor med jungfruolivolja, vitlök, torkad mynta och spiskummin. Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 35), och soppan är den traditionella vintermaten för arbetare '
                   'och bönder i Atlasbergen.',
              tips=('Ät den varm med sked och ringla en tunn stråle jungfruolivolja och en nypa spiskummin och '
                    'paprikapulver över, som en komplett frukost eller lunch utan bröd.',
                    'Koka de krossade bondbönorna med vitlöksklyftor tills de lösts upp helt, mixa dem fint och tillsätt '
                    'den torkade myntan, olivoljan och spiskumminen de sista minuterna.',
                    'Myntan och spiskumminen kan minska uppblåsthet från bondbönorna. Sträng klinisk varning: personer med '
                    'favism (G6PD-brist) får inte äta den alls.'),
              faq=[dict(q='Vad är skillnaden mellan marockansk och egyptisk bissara?',
                        a='Egyptisk bissara är grön, äts kall, tillagas med dill, jutemalva (molokhia) och koriander och '
                          'äts med bröd, medan den marockanska är en varm gul soppa som äts med sked med olivolja, mynta '
                          'och spiskummin.'),
                   dict(q='Passar marockansk bissara vid diabetes?',
                        a='Ja, mycket bra; det glykemiska indexet är lågt (cirka 35), och det rikliga proteinet och '
                          'fibrerna ger ett långsamt upptag utan blodsockerstegring.'),
                   dict(q='Vad är näringsvärdet i en tallrik marockansk bissara (150 g)?',
                        a='Den innehåller cirka 220 kcal, 14 g vegetabiliskt protein, 11 g fibrer och 4 g fett från '
                          'olivoljan.')]),
    493: dict(lead='Jemenitisk mutabbaq (med ägg, kött och purjolök) är en av de mest kända folkliga frukost- och '
                   'kvällsrätterna i Jemen och på Arabiska halvön: en tunn deg fylld med köttfärs, ägg och purjolök som '
                   'gräddas på en het plåt (saj). Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 55), '
                   'eftersom fyllningen av ägg och kött bromsar degens stärkelse.',
              tips=('Pressa en färsk citronklyfta över och ät bara två till tre bitar som huvudrätt med en grön sallad, så '
                    'hålls kalorierna nere.',
                    'Grädda mutabbaq på en torr plåt med mycket lite olja i stället för att steka den i mycket ghee, och '
                    'dubbla mängden grön purjolök och ägg i fyllningen.',
                    'Purjolök innehåller allicin och svavelföreningar; mutabbaq från gatukök kan innehålla raffinerade '
                    'oljor och mycket kalorier från fett, vilket kräver måtta.'),
              faq=[dict(q='Kan den som har diabetes äta jemenitisk mutabbaq?',
                        a='Ja, med måtta; det glykemiska indexet ligger på gränsen 55 (lågt), proteinet i äggen och köttet '
                          'dämpar en kraftig blodsockertopp, och det viktiga är att inte äta för många bitar.'),
                   dict(q='Hur många kalorier finns i en vanlig portion salt mutabbaq (150 g, två stora bitar)?',
                        a='Den ger cirka 430 kcal, 21 g protein, 19,5 g fett och cirka 42 g kolhydrater.'),
                   dict(q='Vilken sorts mutabbaq är det bästa valet?',
                        a='Mutabbaq med purjolök och ägg som gräddas på torr plåt utan fett kött och utan härdat '
                          'vegetabiliskt fett.')]),
    494: dict(lead='Tamees från Hijaz är det stora tandoorbrödet av afghanskt och jemenitiskt ursprung, med krispiga '
                   'kanter och luftig inkråm, omtyckt till rätter av bondbönor och qallaba i den folkliga frukosten. Det '
                   'glykemiska indexet är medelhögt (en kliniskt granskad uppskattning, 68) på grund av storleken, det '
                   'vita mjölet och den snabba nedbrytningen.',
              tips=('Nöj dig med en fjärdedel av brödet och doppa den i bondbönor kryddade med olivolja och spiskummin och '
                    'ett kokt ägg; proteinet och fibrerna dämpar brödets blodsockertopp.',
                    "Välj alltid 'tamees burr' (av fullkornsvetemjöl med kli) i stället för vanligt vitt tamees eller "
                    'kexliknande tamees fullt av ghee och socker.',
                    'Ett helt vitt tamees motsvarar 3 till 4 vanliga bröd i kalorier och stärkelse; därför är det '
                    'avgörande att dela det med familjen vid diabetes och bantning.'),
              faq=[dict(q='Varför höjer vitt tamees blodsockret snabbt?',
                        a='Därför att det glykemiska indexet är medelhögt (cirka 68), det görs av raffinerat mjöl med '
                          'mycket stärkelse, och den snabba gräddningen i tandoorns höga värme gör att det smälts och tas '
                          'upp mycket snabbt.'),
                   dict(q='Vad är näringsvärdet i en fjärdedel av ett vanligt tamees (100 g)?',
                        a='En fjärdedel ger cirka 275 kcal, 8,5 g protein, 3 g fett och cirka 54 g snabba kolhydrater.'),
                   dict(q='Är grovt tamees (burr) ett säkert val vid diabetes?',
                        a='Det är ett betydligt bättre val eftersom kliet och fibrerna sänker det glykemiska indexet, men '
                          'det är fortfarande stärkelse där portionen behöver begränsas till en fjärdedel av brödet.')]),
    495: dict(lead='Balila från Levanten och Hijaz är en av de godaste folkrätterna i de gamla kvarteren: mjuka kokta '
                   'kikärter kryddade med spiskummin, olivolja, citron, vinäger och inlagda grönsaker. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 28), och den är ett mättande mellanmål.',
              tips=('Ät en varm skål balila med sked som snabb frukost eller mättande eftermiddagsmål; citronens och '
                    'vinägerns syra med spiskumminen ger en härlig mättnadskänsla.',
                    'Koka kikärterna tills de är helt mjuka, och strö över nymalen spiskummin, jungfruolivolja och en sked '
                    'vinäger med skivor av inlagd rova eller krispig gurka.',
                    'Balila innehåller zink, magnesium och fibrer.'),
              faq=[dict(q='Höjer balila blodsockret vid diabetes?',
                        a='Nej, det glykemiska indexet är lågt (cirka 28), och fibrerna dämpar blodsockertoppar.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i en vanlig skål balila (150 g)?',
                        a='Portionen innehåller cirka 230 kcal, 12 g vegetabiliskt protein, 10,5 g fibrer och 5 g fett '
                          'från olivoljan.'),
                   dict(q='Ger balila uppblåsthet?',
                        a='Att blötlägga kikärterna i 16 timmar, koka dem väl och tillsätta spiskummin och citron minskar '
                          'uppblåstheten tydligt.')]),
    496: dict(lead='Moutabal på rostad pumpa är en nyskapande levantinsk höstdipp som förenar den rostade pumpans sötma '
                   'med den fylliga sesamtahinin, vitlök och citron. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 35), eftersom tahinins fett och protein uppväger pumpans höga glykemiska index när den '
                   'äts ensam.',
              tips=('Njut av den som dipp med selleri- och gurkstavar eller rostat fullkornsbröd till grillat och '
                    'ugnsrätter.',
                    'Rosta pumpatärningarna i ugnen tills kanterna karamelliseras och den naturliga sötman kommer fram, '
                    'och mosa dem sedan med naturell tahini, citronsaft, vitlök, en nypa havssalt och olivolja.',
                    'Pumpa hör till de livsmedel som innehåller mest betakaroten, som kroppen omvandlar till A-vitamin.'),
              faq=[dict(q='Kokt pumpa har ett högt glykemiskt index – varför är det glykemiska indexet för pumpamoutabal '
                          'lågt (35)?',
                        a='Därför att pumpan blandas med en god andel tahini och olivolja, som tillför fett och protein '
                          'och bromsar sockerupptaget i matsmältningen.'),
                   dict(q='Vad är näringsvärdet i 60 g pumpamoutabal (två matskedar)?',
                        a='Portionen ger cirka 65 kcal, 1,7 g protein, 3,6 g omättat fett och 7 g kolhydrater.'),
                   dict(q='Passar pumpamoutabal vid insulinresistens?',
                        a='Ja, mycket bra; den är en god och näringsrik frukost eller förrätt som påverkar blodsockret '
                          'lite.')]),
    497: dict(lead='Grillad halloumi med vattenmelon är medelhavets mest uppfriskande och glada sommarduo: den varma, '
                   'salta halloumin möter den kalla, krispiga och söta vattenmelonen och myntabladen. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 45), eftersom ostens fett och protein bromsar '
                   'upptaget av vattenmelonens snabba socker.',
              tips=('Ät två skivor grillad halloumi med en kopp kall vattenmelon i tärningar och lite färsk mynta som en '
                    'lätt och fräsch sommarmiddag.',
                    'Grilla halloumiskivorna i en torr, non-stick grillpanna i en minut per sida så att de får en vacker '
                    'gyllene färg utan olja eller smör.',
                    'Den smarta kombinationen av protein och fett (halloumi) med en frukt med snabbt socker (vattenmelon) '
                    'är en praktisk tillämpning av att sänka måltidens glykemiska belastning.'),
              faq=[dict(q='Kan den som har diabetes äta vattenmelon på det här sättet?',
                        a='Ja; vattenmelon ensam höjer blodsockret snabbt, men tillsammans med halloumi dämpas stegringen '
                          'och måltiden blir balanserad.'),
                   dict(q='Hur många kalorier finns i en vanlig tallrik halloumi och vattenmelon (200 g)?',
                        a='Tallriken ger cirka 370 kcal, 24 g protein, 22 g fett och cirka 18 g naturliga kolhydrater.'),
                   dict(q='Passar halloumi vid högt blodtryck?',
                        a='Halloumi innehåller relativt mycket natrium; därför rekommenderas att ostskivorna blötläggs i '
                          'ljummet vatten i 20 minuter före grillningen för att få bort överflödigt salt.')]),
    498: dict(lead='Levantinsk shanklishsallad är en av de äldsta och godaste rätterna med lagrad ost i Orienten: torkade '
                   'shanklishbollar täckta med vild timjan som smulas och blandas med tomat, lök och jungfruolivolja. Det '
                   'glykemiska indexet är inte tillämpligt eftersom rätten saknar stärkelse, och den är en äkta och mycket '
                   'god förrätt.',
              tips=('Ät den med gaffel som proteinrik frukost eller middag med gurka, sallat och färsk mynta, och undvik '
                    'att doppa vitt bröd i den.',
                    'Smula shanklishbollen med en gaffel och blanda den med finhackad tomat, salladslök och en halv kopp '
                    'förstklassig jungfruolivolja för att mildra den lagrade smaken.',
                    'Shanklish är en naturligt fermenterad ost med mjölksyrabakterier från jäsningen; den som har högt '
                    'blodtryck bör vara uppmärksam på salthalten från torkningen.'),
              faq=[dict(q='Höjer shanklishsallad blodsockret?',
                        a='Nej; den består av protein, vattenrika grönsaker och ren olivolja, och det glykemiska indexet '
                          'är inte tillämpligt eftersom den saknar kolhydrater som tas upp.'),
                   dict(q='Vad är näringsvärdet i 150 g shanklishsallad med olivolja?',
                        a='Portionen innehåller cirka 250 kcal, 16,5 g protein, 17 g fett och 7 g kolhydrater enbart från '
                          'grönsakerna (varav 2 g fibrer).'),
                   dict(q='Varför har shanklish så stark doft och smak?',
                        a='På grund av mjölksyrajäsningen och lagringen av den torkade labneh med örter och värme i flera '
                          'veckor, som bildar kortkedjiga fettsyror.')]),
    499: dict(lead='Pomeransmarmelad (marmelad på bitter apelsin) är en pärla bland de levantinska och medelhavsländernas '
                   'marmelader, med aromatiska skal och en smak i balans mellan behaglig beska och orientalisk sötma. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 52) tack vare det rikliga pektinet i '
                   'skalen.',
              tips=('Ät bara en liten struken matsked (15 g) på en bit vit ost eller keso med fullkornsbröd, så hålls '
                    'sockermängden i schack.',
                    'För en hemgjord variant: koka de rullade skalen flera gånger för att få bort överflödig beska, och '
                    'använd hälften av den vanliga sockermängden eller naturligt sötningsmedel av stevia.',
                    'Viktig klinisk varning: pomeransskal (bitter apelsin) innehåller det stimulerande ämnet synefrin; den '
                    'som har hjärtklappning eller högt blodtryck bör vara försiktig och undvika marmeladen tillsammans med '
                    'känsliga blodtrycksläkemedel.'),
              faq=[dict(q='Passar pomeransmarmelad vid diabetes?',
                        a='Det glykemiska indexet är relativt lågt (cirka 52) tack vare pektinet, men den är fortfarande '
                          'en sockerrik marmelad, så bara en tesked (10–15 g) tillsammans med en proteinrik måltid.'),
                   dict(q='Vad är näringsvärdet i en matsked pomeransmarmelad (15 g)?',
                        a='Den innehåller cirka 35 kcal, nästan inget fett eller protein och cirka 9 g kolhydrater och '
                          'snabbt socker.'),
                   dict(q='Vad innehåller pomeransskal?',
                        a='De innehåller flavonoider, limonen, flyktiga oljor och pektin.')]),
    500: dict(lead='Naturlig johannesbrödsirap är ett traditionellt bergsarv i Libanon och Levanten: ett extrakt av '
                   'johannesbrödsfrukter som kokas långsamt, med en mörk smak som påminner om karamell och mörk choklad. '
                   'Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 40), och sirapen är ett naturligt '
                   'sötningsalternativ som innehåller mineraler.',
              tips=('Blanda en tesked johannesbrödsirap med en sked ren sesamtahini som ett naturligt alternativ till '
                    'halva eller nougatkräm.',
                    'Välj alltid traditionell sirap som pressats med vatten och kokats långsamt, utan tillsatt rörsocker '
                    'eller industriell glukossirap.',
                    'Johannesbrödsirap innehåller kalcium, järn, zink och polyfenoler.'),
              faq=[dict(q='Varför anses johannesbrödsirap vara ett bättre val vid diabetes än dadelsirap och honung?',
                        a='Därför att det glykemiska indexet är lågt (cirka 40) och de naturliga fibrerna, pektin och '
                          'galaktomannan, bromsar sockerupptaget i blodet.'),
                   dict(q='Vad är näringsvärdet i en matsked naturlig johannesbrödsirap (15 g)?',
                        a='Den ger cirka 40 kcal, 0,3 g protein, inget fett och cirka 10 g kolhydrater, samt kalcium.'),
                   dict(q='Innehåller johannesbrödsirap järn?',
                        a='Ja, den innehåller järn och B-vitaminer.')]),
    # foods 501-600: translated from the approved Arabic copy and FAQ (2026-10-24, four checked blocks of 25)
    501: dict(lead='Turkisk shish kebab av lamm (kuzu şiş) är en pärla i den anatoliska grillkonsten: möra tärningar av '
                   'lammkött marinerade i paprikasås, olivolja och lök och grillade över kol. Det glykemiska indexet är '
                   'inte tillämpligt eftersom rätten saknar kolhydrater, och den är en proteinrik måltid som mättar väl '
                   'utan att påverka blodsockret.',
              tips=('Ät spetten med gaffel tillsammans med lök kryddad med sumak och en sallad av grillade grönsaker, och '
                    'undvik att rulla in dem i vitt bröd.',
                    'En marinad av lökjuice, olivolja och yoghurt med pul biber räcker för att möra köttet; grilla det på '
                    'låg värme så att det förblir saftigt utan att ytan bränns.',
                    'Lammkött innehåller hemjärn, B12-vitamin och zink; zink och B12-vitamin bidrar till immunsystemets '
                    'normala funktion. Den som har hjärtsjukdom bör vara måttlig med svansfettet.'),
              faq=[dict(q='Höjer turkisk shish kebab blodsockret?',
                        a='Nej; det är grillat kött utan stärkelse, och det ger ingen blodsockerstegring.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g lammshishkebab?',
                        a='Portionen ger cirka 295 kcal, 28 g protein och 18 g naturligt fett, med nästan inga '
                          'kolhydrater.'),
                   dict(q='Passar shish kebab vid keto och viktnedgång?',
                        a='Ja, den är en typisk ketorätt som mättar i många timmar.')]),
    502: dict(lead='Iskender kebab (İskender kebap) är staden Bursas stolthet: tunna skivor av kebabkött över bitar av '
                   'pidebröd som dränkts i fyllig tomatsås och smält smör och serveras med yoghurt. Det glykemiska indexet '
                   'är lågt (en kliniskt granskad uppskattning, 45), eftersom fettet i köttet och yoghurten bromsar '
                   'upptaget av brödets stärkelse.',
              tips=('Börja med köttskivorna och yoghurten, och nöj dig med några små bitar av det såsindränkta brödet i '
                    'botten av tallriken för att hålla kolhydraterna i schack.',
                    'Be om lite smör i stället för en generös skvätt brynt smör, så halveras det mättade fettet medan den '
                    'kungliga smaken behålls.',
                    'Yoghurten till ger mjölksyra och protein som bromsar magsäckstömningen, men rätten innehåller mycket '
                    'kalorier och mättat fett och kräver stor måtta.'),
              faq=[dict(q='Passar iskender kebab vid diabetes?',
                        a='Ja, med försiktighet; det glykemiska indexet är lågt (cirka 45), men rätten innehåller både '
                          'mycket stärkelse och fett, så ät inte allt bröd under köttet.'),
                   dict(q='Vad är näringsvärdet i en vanlig tallrik iskender kebab (300 g)?',
                        a='Tallriken innehåller cirka 520 kcal, 34 g protein, 28 g fett och cirka 32 g stärkelse.'),
                   dict(q='Vad bidrar tomatsåsen och yoghurten med i rätten?',
                        a='Tomatsåsen ger lykopen och yoghurten ger kalcium.')]),
    503: dict(lead='Adana kebab är kungen bland de starka grillrätterna i södra Turkiet: handhackad köttfärs på breda '
                   'spett, kryddad med stark röd paprika och svansfett och grillad över glödande kol. Det glykemiska '
                   'indexet är inte tillämpligt eftersom rätten saknar kolhydrater, och den är en het festrätt som väcker '
                   'sinnena.',
              tips=('Ät spettet med gaffel tillsammans med grillad grön chili och tomat och en sallad av persilja och '
                    'sumak, och undvik rullar av vitt lavashbröd.',
                    'Att bara gnida in köttet med söt och stark paprika och salt, utan mjöl eller ströbröd, bevarar den '
                    'turkiska äktheten och gör att rätten saknar stärkelse.',
                    'Chilin innehåller capsaicin; den som har IBS eller sur reflux bör vara försiktig med de starka '
                    'kryddorna.'),
              faq=[dict(q='Höjer adana kebab blodsockret?',
                        a='Nej, den påverkar inte blodsockret; den består bara av protein, fett och röd paprika, och det '
                          'glykemiska indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier finns i ett vanligt spett adana kebab (150 g)?',
                        a='Spettet ger cirka 320 kcal, 26 g protein och 24 g naturligt fett från svansfettet, med nästan '
                          'inga kolhydrater.'),
                   dict(q='Vad är skillnaden mellan adana kebab och urfa kebab?',
                        a='Adana kebab är mycket stark med het röd paprika, medan urfa kebab har mild smak utan chili och '
                          'passar en känslig mage.')]),
    504: dict(lead='Turkisk manti (Kayseri mantısı) är mycket små degknyten fyllda med köttfärs som kokas i vatten och '
                   'toppas med vitlöksyoghurt och brynt smör med sumak och mynta. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 53) tack vare den rikliga yoghurten och köttfyllningen som bromsar '
                   'degens stärkelse.',
              tips=('Var generös med vitlöksyoghurten över tallriken; proteinet och yoghurtens syra dämpar '
                    'blodsockertoppen från knytenas stärkelse.',
                    'Koka mantin al dente så att de håller formen, vilket sänker det glykemiska indexet, och använd '
                    'naturell yoghurt med låg fetthalt och tomatsås i stället för att dränka dem i smör.',
                    'Vitlöksyoghurten ger mjölksyrabakterier och allicin; det viktiga är att hålla koll på mängden deg vid '
                    'diabetes och insulinresistens.'),
              faq=[dict(q='Passar turkisk manti vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 53) tack vare yoghurten och köttet, och '
                          'det viktiga är en måttlig portion (en kopp, 200–250 g).'),
                   dict(q='Vad är näringsvärdet i en tallrik turkisk manti (250 g)?',
                        a='Tallriken innehåller cirka 380 kcal, 18 g protein, 14 g fett och cirka 42 g stärkelse.'),
                   dict(q='Varför gör turkiska familjer mantin så små?',
                        a='Ett folkligt talesätt i Kayseri säger att en skicklig kock får plats med 40 manti i en matsked, '
                          'som ett tecken på noggrannhet och fin deg!')]),
    505: dict(lead='Turkisk pide med ost och ägg (peynirli yumurtalı pide) är den traditionella anatoliska båten av deg '
                   'som gräddas på sten och fylls med turkisk kaşarost och flytande äggula. Det glykemiska indexet är '
                   'medelhögt (en kliniskt granskad uppskattning, 60), och den är en anrik turkisk frukost som mättar väl.',
              tips=('Dela båten med någon och ät bara hälften tillsammans med en riklig turkisk grönsakstallrik med tomat, '
                    'gurka, oliver och ruccola.',
                    'Gör degen med fullkornsvetemjöl eller urspannmål för mer fibrer, och lägg ägget den sista minuten av '
                    'gräddningen så att det blir ett näringsrikt stekt ägg utan att brännas.',
                    'Ägg och ost ger kolin och fullvärdigt protein, men mycket gul ost och vitt mjöl ger fler kalorier och '
                    'mer mättat fett för den som har kärlsjukdom.'),
              faq=[dict(q='Varför är det glykemiska indexet för turkisk pide medelhögt (60)?',
                        a='Därför att degen görs av fint vitt mjöl; proteinet och fettet i osten och ägget bromsar '
                          'upptaget, men den glykemiska belastningen förblir märkbar.'),
                   dict(q='Hur många kalorier finns i en halv pide med ost och ägg (200 g)?',
                        a='Portionen innehåller cirka 420 kcal, 19 g fullvärdigt protein, 18 g fett och cirka 45 g '
                          'kolhydrater.'),
                   dict(q='Kan pide bli ett bättre val vid viktnedgång?',
                        a='Ja, med lorost med låg fetthalt, en mycket tunn degbotten och fyllning av spenat och ägg.')]),
    506: dict(lead='Turkisk spenatbörek (ıspanaklı börek) hör till de mest kända bakverken av spröd yufkadeg, med en '
                   'fyllig fyllning av färska spenatblad, lorost eller fetaost och rostad lök som gräddas gyllene och '
                   'krispig. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 52) tack vare den rikliga '
                   'spenaten och proteinet i fyllningen.',
              tips=('Ät en rektangulär bit stor som en handflata med en kopp osötat turkiskt te och en grön sallad; ett '
                    'lätt mellanmål till frukost eller arbetspausen.',
                    'Pensla yufkaarken med olivolja och lite lättmjölk i stället för smält smör och ghee, så halveras det '
                    'mättade fettet.',
                    'Spenat innehåller lutein, magnesium, kalium och järn; kalium bidrar till att bibehålla ett normalt '
                    'blodtryck.'),
              faq=[dict(q='Är spenatbörek bättre vid diabetes än börek med ost och potatis?',
                        a='Ja, betydligt bättre; spenatfyllningen innehåller mycket fibrer och nästan ingen stärkelse, '
                          'vilket sänker det glykemiska indexet till cirka 52.'),
                   dict(q='Vad är näringsvärdet i en vanlig bit spenatbörek (120 g)?',
                        a='Den ger cirka 240 kcal, 8 g protein, 12 g fett och cirka 24 g kolhydrater som smälts i måttlig '
                          'takt.'),
                   dict(q='Hur undviker jag halsbränna efter börek?',
                        a='Undvik friterade bakverk och välj ugnsbakad börek, och pressa ur spenaten ordentligt när du '
                          'fyller den.')]),
    507: dict(lead='İmam bayıldı är en pärla i det osmanska vegetariska köket med olivolja (zeytinyağlılar): mjuka '
                   'auberginer fyllda med karamelliserad lök, tomat, vitlök och persilja som tillagas långsamt i '
                   'jungfruolivolja. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 25).',
              tips=('Den serveras traditionellt kall eller rumstempererad; ät den med gaffel som en lätt vegetarisk middag '
                    'utan bröd och njut av den söta olivoljesaften.',
                    'Rosta auberginen i ugnen efter att ha snittat den på längden i stället för att fritera den i mycket '
                    'olja; auberginen suger upp olja som en svamp, och ugnen håller rätten lätt.',
                    'Auberginens skal innehåller nasunin, olivoljan oljesyra och vitlöken allicin.'),
              faq=[dict(q="Varför heter rätten 'imam bayıldı' (imamen svimmade)?",
                        a='Enligt den osmanska anekdoten svimmade imamen av hur god rätten var, eller när han såg hur '
                          'mycket fin jungfruolivolja som gick åt!'),
                   dict(q='Passar imam bayıldı vid diabetes och keto?',
                        a='Ja, mycket bra; det glykemiska indexet är lågt (cirka 25) och fettet är omättat.'),
                   dict(q='Vad är näringsvärdet i en vanlig portion imam bayıldı (200 g)?',
                        a='Portionen innehåller cirka 160 kcal, 3 g protein, 11 g fett från olivoljan och 12 g kolhydrater '
                          '(varav 6 g fibrer).')]),
    508: dict(lead='Turkiska izgara köfte är grillade köttbullar som är omtyckta i varje hörn av Turkiet för sin fasthet, '
                   'saftighet och kryddning med lök och spiskummin. Det glykemiska indexet är inte tillämpligt eftersom de '
                   'saknar kolhydrater, och de är en proteinrik familjemåltid; protein bidrar till att bibehålla '
                   'muskelmassa.',
              tips=('Ät 3 till 4 grillade köttbullar med turkisk piyaz (sallad av vita bönor med lök och sumak) till en '
                    'mättande och komplett måltid.',
                    'Knåda köttfärsen väl med riven och urpressad lök, spiskummin och peppar, och nöj dig med en sked '
                    'grova brödsmulor så att de håller ihop utan mer stärkelse.',
                    'De ger fullvärdigt protein, zink och animaliskt järn.'),
              faq=[dict(q='Höjer turkiska grillade köttbullar blodsockret?',
                        a='Nej, de påverkar inte blodsockret; de är kött nästan utan kolhydrater, och det glykemiska '
                          'indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 150 g izgara köfte?',
                        a='Portionen ger cirka 290 kcal, 25 g protein och 20 g naturligt fett, med mindre än 2 g '
                          'kolhydrater.'),
                   dict(q='Är grillade köttbullar bättre än stekta?',
                        a='Grillning över eld låter överflödigt fett droppa av och undviker att köttet suger upp härdade '
                          'vegetabiliska oljor.')]),
    509: dict(lead='Turkisk yaylasoppa (yayla çorbası, ängssoppan) är en varm soppa på yoghurt och ris med doft av torkad '
                   'mynta och olivolja och en traditionell rätt i Anatolien. Det glykemiska indexet är lågt (en kliniskt '
                   'granskad uppskattning, 40), och soppan är mild för magen.',
              tips=('Drick en varm skål i början av måltiden eller som lätt middag; yoghurten och myntan ger en lugn '
                    'mättnad före sänggåendet.',
                    'Använd en avvägd mängd basmatiris eller bulgur (två matskedar per kastrull), och red soppan med '
                    'naturell yoghurt och äggula och avsluta med mynta fräst i olivolja.',
                    'Soppan är lättsmält och innehåller protein, kalcium och zink.'),
              faq=[dict(q='Höjer yaylasoppa blodsockret vid diabetes?',
                        a='Nej, det glykemiska indexet är lågt (cirka 40), och mjölksyran och proteinet i yoghurten '
                          'bromsar upptaget av den lilla mängden ris.'),
                   dict(q='Vad är näringsvärdet i en vanlig tallrik yaylasoppa (300 g)?',
                        a='Tallriken ger cirka 180 kcal, 8 g protein, 6 g fett och cirka 22 g kolhydrater.'),
                   dict(q='Vad innehåller yaylasoppa?',
                        a='Den förenar yoghurt med mjölksyrabakterier och mynta.')]),
    510: dict(lead='Vegansk çiğ köfte (etsiz çiğ köfte) är det populäraste gatusnacket i Turkiet: en slät massa av '
                   'handknådad fin bulgur med paprikapasta, tomat, valnötter, granatäppelsirap och kryddor. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 45), och den äts inrullad i färska salladsblad.',
              tips=('Lägg köftestavarna i ett stort romansalladsblad och pressa över rikligt med citronsaft; salladen ger '
                    'vätska och fibrer som mättar direkt.',
                    'Ingredienserna knådas kraftigt länge tills bulguren mjuknar av knådningens värme och syran i tomaten '
                    'och citronen, utan tillagning och utan rått kött.',
                    'Den moderna veganska varianten saknar risken med bakterier och parasiter från det råa köttet i den '
                    'gamla varianten, och den innehåller vegetabiliskt järn och fibrer.'),
              faq=[dict(q='Passar vegansk çiğ köfte vid diabetes och bantning?',
                        a='Ja, ett bra och snabbt val; det glykemiska indexet är lågt (cirka 45), och fibrerna i bulguren '
                          'och salladen dämpar blodsockerstegringen.'),
                   dict(q='Vad är näringsvärdet i 100 g vegansk çiğ köfte (4 stavar)?',
                        a='Den innehåller cirka 180 kcal, 5,5 g vegetabiliskt protein, 4 g omättat fett (från valnötterna) '
                          'och 32 g kolhydrater som smälts långsamt.'),
                   dict(q='Innehåller den som säljs i butiker rått kött?',
                        a='I Turkiet är det enligt moderna livsmedelsregler förbjudet att sälja çiğ köfte med rått kött '
                          'kommersiellt, och alla butiker säljer den veganska varianten med bulgur och nötter.')]),
    511: dict(lead='Turkisk lokum är sultanernas historiska konfekt med mjuk, seg geléartad konsistens och smak av '
                   'rosenvatten och mastix, täckt med stärkelse och pistagenötter. Det glykemiska indexet är högt (en '
                   'kliniskt granskad uppskattning, 75), eftersom den består av rent socker och raffinerad stärkelse, '
                   'vilket kräver största försiktighet vid diabetes.',
              tips=('Nöj dig med en mycket liten bit (15–20 g) till en kopp osötat turkiskt kaffe, och bara vid festliga '
                    'tillfällen.',
                    'Välj alltid lokum fylld med hela nötter som pistage eller valnötter; nötternas fett bromsar '
                    'sockerupptaget något.',
                    'Sträng klinisk varning: en snabbt upptagen sötsak som höjer blodsockret mycket snabbt; den som har '
                    'diabetes eller insulinresistens bör undvika den till vardags.'),
              faq=[dict(q='Varför är det glykemiska indexet för turkisk lokum högt?',
                        a='Därför att den görs av vitt socker, glukossirap och raffinerad majsstärkelse, som snabbt blir '
                          'blodsocker så fort den smälter i munnen.'),
                   dict(q='Hur många kalorier finns i två bitar turkisk lokum (30 g)?',
                        a='Portionen innehåller cirka 112 kcal, nästan inget protein eller fett (cirka 1 g från pistagen) '
                          'och består främst av cirka 25 g socker.'),
                   dict(q='Är lokum med pistage ett bättre val?',
                        a='Ja, något bättre, eftersom pistagen ger protein och fibrer som minskar den glykemiska '
                          'belastningen jämfört med naturell lokum av bara socker och stärkelse.')]),
    512: dict(lead='Turkiskt äppelte (elma çayı) är den aromatiska välkomstdrycken i Istanbuls basarer: torkade '
                   'äppelskivor med kanelstänger och kryddnejlika som dras i kokande vatten. Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 30), och teet är ett varmt alternativ utan koffein och utan '
                   'industriellt socker.',
              tips=('Drick det varmt i klassiska turkiska teglas efter måltiden eller på kvällen.',
                    'Koka naturliga äppelskivor och kanelstänger i en tekanna utan att tillsätta socker, och se upp med '
                    'snabbpulver för äppelte som är fullt av socker och konstgjorda aromer.',
                    'Kanel och naturliga äpplen innehåller polyfenoler.'),
              faq=[dict(q='Höjer naturligt turkiskt äppelte blodsockret?',
                        a='Nej; om det görs av riktiga äppelskivor utan tillsatt socker är kolhydraterna nästan '
                          'obefintliga och det glykemiska indexet lågt.'),
                   dict(q='Vad är skillnaden mellan naturligt äppelte och snabbpulver?',
                        a='Kommersiellt pulver består av vitt socker, citronsyra och konstgjorda aromer som höjer '
                          'blodsockret kraftigt, medan det naturliga avkoket saknar tillsatt socker.'),
                   dict(q='Vad är näringsvärdet i en kopp naturligt äppelte (250 ml)?',
                        a='Koppen innehåller cirka 25 kcal från den urlakade äppelsaften, inget fett eller protein och '
                          'cirka 5 g naturligt fruktsocker.')]),
    513: dict(lead='Lammtagine med honungsglaserade katrinplommon och aprikoser är den lyxiga marockanska festrätten: '
                   'lammkött som tillagas långsamt i lerkruka med saffran och ingefära och garneras med katrinplommon och '
                   'krispig mandel. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 45) tack vare det '
                   'rikliga köttproteinet och de torkade fruktens fibrer.',
              tips=('Fokusera på de möra köttbitarna med gaffel tillsammans med ett katrinplommon och rostad mandel, och '
                    'undvik att doppa mycket vitt bröd i såsen.',
                    'Tillaga köttet i en tagine av lera på låg värme, och karamellisera katrinplommonen med '
                    'apelsinblomsvatten, kanel och mycket lite honung i stället för stora mängder socker.',
                    'Katrinplommon innehåller pektin och sorbitol; den som har diabetes bör begränsa dem på grund av den '
                    'koncentrerade sötman.'),
              faq=[dict(q='Passar lammtagine med katrinplommon vid diabetes?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 45) eftersom måltiden främst består av '
                          'protein och fett, och det viktiga är att nöja sig med ett eller två katrinplommon och undvika '
                          'vitt bröd.'),
                   dict(q='Vad är näringsvärdet i en vanlig portion lammtagine med katrinplommon (300 g)?',
                        a='Portionen innehåller cirka 440 kcal, 32 g protein, 22 g fett och cirka 26 g kolhydrater från de '
                          'torkade frukterna.'),
                   dict(q='Vad är hemligheten med att laga mat i en tagine av lera?',
                        a='Det koniska locket kondenserar ångan och för den hela tiden tillbaka till köttet, så att det '
                          'tillagas i sin egen saft, blir mycket mört och behöver mycket lite fett.')]),
    514: dict(lead='Fisktagine med marockansk chermoula är en atlantisk havsrätt som doftar av koriander, vitlök, '
                   'spiskummin, paprika, olivolja och saltad citron, med skivor av paprika, tomat och morot. Det '
                   'glykemiska indexet är inte tillämpligt eftersom rätten saknar stärkelse.',
              tips=('Ät fiskbitarna med de kokta grönsakerna i buljongen direkt med gaffel; en mättande och komplett '
                    'medelhavslunch som inte behöver något bröd till.',
                    'Den äkta chermoulamarinaden lyfter fram fiskens fräschhet; tillaga den i en tagine av lera med skivor '
                    'av tomat och paprika utan att tillsätta vatten, så får du njuta av den rena saften.',
                    'Rätten innehåller omega-3-fettsyror från fisken, jod, selen och C-vitamin.'),
              faq=[dict(q='Höjer marockansk fisktagine blodsockret?',
                        a='Nej; den består av protein från havet, vattenrika grönsaker och olivolja, och det glykemiska '
                          'indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier finns i 300 g fisktagine?',
                        a='Portionen innehåller cirka 265 kcal, 30 g protein, 12 g fett och mindre än 8 g kolhydrater från '
                          'grönsakerna.'),
                   dict(q='Vad är chermoula?',
                        a='En klassisk marockansk blandning av koriander, persilja, vitlök, olivolja, citronsaft, '
                          'spiskummin och paprika.')]),
    515: dict(lead='Kycklingtagine med saltad citron och gröna oliver är den mest älskade och kända hemrätten i Marocko: '
                   'kyckling som tillagas tills den smälter med lök, saffran och ingefära och den lagrade citronens syra. '
                   'Det glykemiska indexet är inte tillämpligt, och rätten ger god och lätt proteinrik mat.',
              tips=('Njut av kycklingbitarna med den tjocka löksåsen (daghmira) och oliverna med gaffel, eller med en '
                    'avvägd mängd grovt bröd och en marockansk sallad.',
                    'Tillaga kycklingen på låg värme tills löken karamelliseras (daghmira) utan mjöl eller stärkelse; den '
                    'saltade citronens syra gör att du inte behöver tillsätta bordssalt.',
                    'Marinaden innehåller ingefära, gurkmeja och saffran; saltet i citronen och oliverna kräver måtta vid '
                    'högt blodtryck.'),
              faq=[dict(q='Passar kycklingtagine med citron och oliver vid bantning och keto?',
                        a='Ja, den är en utmärkt keto- och bantningsrätt med protein och olivfett utan nämnvärda '
                          'kolhydrater eller socker.'),
                   dict(q='Vad är näringsvärdet i 300 g kycklingtagine med oliver?',
                        a='Portionen ger cirka 320 kcal, 34 g protein, 18 g fett och mindre än 5 g kolhydrater från den '
                          'karamelliserade löken.'),
                   dict(q='Är daghmirasåsen ett bra val?',
                        a='Ja, den består av lök som karamelliserats i olivolja med naturliga kryddor och saffran, inte av '
                          'härdat fett.')]),
    516: dict(lead='Kycklingpastilla från Fès är höjdpunkten i det anrika marockanska köket och förenar salt och sött: '
                   'tunna, krispiga lager av warqadeg runt en fyllning av kyckling och ägg som karamelliserats med mandel, '
                   'kanel och lite socker. Det glykemiska indexet är medelhögt (en kliniskt granskad uppskattning, 58), '
                   'och rätten är ett mästerverk för förnäma fester.',
              tips=('En medelstor triangel räcker för att njuta av smaken; ät den efter en grön sallad för att minska '
                    'upptaget av sockret på ytan och degens stärkelse.',
                    'För en lättare hemgjord variant: hoppa över florsockret, nöj dig med äkta kanel och använd rostad '
                    'mandel som inte friterats i olja.',
                    'Den ger protein och magnesium från mandeln, men florsockret och smöret i degen höjer den glykemiska '
                    'belastningen, vilket kräver stor måtta vid diabetes.'),
              faq=[dict(q='Varför är det glykemiska indexet för kycklingpastilla medelhögt (58)?',
                        a='Därför att mandelns fett och proteinet i kycklingen och äggen bromsar upptaget av fyllningens '
                          'socker och degens stärkelse, men rätten innehåller fortfarande mycket kalorier.'),
                   dict(q='Hur många kalorier finns i en vanlig portion kycklingpastilla (150 g)?',
                        a='Portionen innehåller cirka 400 kcal, 20 g protein, 22 g fett och cirka 32 g stärkelse och '
                          'socker.'),
                   dict(q='Kan den som har diabetes smaka pastilla?',
                        a='Ja, en liten bit (100 g) utan florsocker på ytan, som en del av en kaloriberäknad måltid vid '
                          'festliga tillfällen.')]),
    517: dict(lead='Stark skaldjurspastilla (pastilla aux fruits de mer) är pastillans friska och heta havsversion: en '
                   'lyxig fyllning av bläckfisk, räkor, vit fisk, glasnudlar, sojasås och harissa i filodeg. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 52), med syrlig och kryddig smak.',
              tips=('Ät en medelstor bit med en skvätt färsk citron; proteinet från skaldjuren utgör den största delen av '
                    'fyllningen och mättar länge.',
                    'Minska andelen glasnudlar och dubbla mängden skaldjur och grönsaker som svamp och paprika, och grädda '
                    'den i ugnen med lite olivolja i stället för smör.',
                    'Skaldjuren ger zink, jod och B12-vitamin, och harissan ger chili; håll koll på natriumet från '
                    'sojasåsen och skaldjurssåserna.'),
              faq=[dict(q='Är skaldjurspastilla bättre vid diabetes än kycklingpastilla?',
                        a='Ja, bättre; den saknar karamelliserat florsocker och innehåller mycket protein från havet och '
                          'starka kryddor, vilket ger ett lägre glykemiskt index (cirka 52).'),
                   dict(q='Vad är näringsvärdet i en portion skaldjurspastilla (150 g)?',
                        a='Den ger cirka 290 kcal, 24 g protein, 12 g fett och cirka 22 g stärkelse från degen och '
                          'nudlarna.'),
                   dict(q='Höjer skaldjurspastilla kolesterolet?',
                        a='Kolesterolet i räkor och bläckfisk påverkar blodkolesterolet lite hos de flesta; det viktiga är '
                          'att inte ta för mycket fett på degen.')]),
    518: dict(lead='Marockansk harira är drottningen bland soppor i Maghreb: en fyllig och sammetslen soppa med kikärter, '
                   'linser, kött, färska tomatbitar, selleri och koriander, redd med lite mjöl. Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 38), och soppan är en komplett måltid.',
              tips=('Ät en skål varm harira med ett kokt ägg och en dadel; baljväxterna och fibrerna fyller magen och '
                    'dämpar suget efter sötsaker efter måltiden.',
                    'Red soppan med lite fullkornsmjöl eller havremjöl, eller mosa en del av kikärterna och linserna för '
                    'att göra den tjockare utan extra vitt mjöl.',
                    'Kikärter och linser innehåller fibrer, och det låga glykemiska indexet dämpar plötsliga '
                    'blodsockerstegringar vid diabetes.'),
              faq=[dict(q='Höjer marockansk harira blodsockret snabbt?',
                        a='Nej, det glykemiska indexet är lågt (cirka 38), och baljväxternas fibrer och protein gör att '
                          'glukosen tas upp långsamt.'),
                   dict(q='Vad är näringsvärdet i en vanlig tallrik marockansk harira (300 g)?',
                        a='Tallriken ger cirka 260 kcal, 14 g fullvärdigt protein, 6 g fett och cirka 36 g komplexa '
                          'kolhydrater rika på fibrer.'),
                   dict(q='Hur gör jag hariran lättare för magen?',
                        a='Blötlägg kikärterna, ta bort skalen och koka dem väl med selleri och ingefära, så minskar '
                          'gasbildningen.')]),
    519: dict(lead='Marockansk couscous med sju grönsaker är en traditionell familjerätt i Maghreb: ångkokta mannagryn som '
                   'dränks i aromatisk grönsaksbuljong med pumpa, morot, rova, zucchini, kål, kikärter och kött. Det '
                   'glykemiska indexet är medelhögt (en kliniskt granskad uppskattning, 58), och rätten visar '
                   'medelhavsodlingens rikedom.',
              tips=('Fyll halva tallriken med de olika grönsakerna, köttet och kikärterna, och nöj dig med en halv kopp '
                    'couscous med het buljong över, så sänks den samlade glykemiska belastningen.',
                    'Välj couscous av fullkornsdurumvete (blé complet) eller kornscouscous (belboula) för mer fibrer och '
                    'ett tydligt lägre glykemiskt index.',
                    'De sju grönsakerna ger en rik variation av växtämnen och lösliga fibrer, och det viktiga vid diabetes '
                    'är att styra mängden couscous.'),
              faq=[dict(q='Passar couscous med sju grönsaker vid diabetes?',
                        a='Ja, mycket bra om andelen grönsaker och kött är större än couscousen; det glykemiska indexet är '
                          'medelhögt (cirka 58), och grönsakernas fibrer bromsar blodsockerstegringen.'),
                   dict(q='Hur många kalorier finns i en komplett portion couscous med grönsaker och kött (350 g)?',
                        a='Portionen innehåller cirka 450 kcal, 24 g protein, 12 g fett och cirka 58 g kolhydrater rika på '
                          'fibrer och mineraler.'),
                   dict(q='Vad är fördelen med kornscouscous (belboula)?',
                        a='Kornscouscous innehåller betaglukaner och har ett betydligt lägre glykemiskt index än couscous '
                          'av vete.')]),
    520: dict(lead='Marockansk zaalouk är den främsta varma förrätten i det marockanska köket: grillad eller kokt '
                   'aubergine som mosas med färsk tomat, vitlök, koriander, spiskummin, paprika och jungfruolivolja. Det '
                   'glykemiska indexet är inte tillämpligt eftersom rätten saknar nettostärkelse.',
              tips=('Ät den med gaffel som varm eller kall dipp till grillat och fisk, eller doppa gurk- och morotsstavar, '
                    'och undvik vitt bröd.',
                    'Att grilla auberginen på låg värme ger den en förtrollande rökig smak; tillaga den med tomat och '
                    'olivolja utan socker, så förblir den lätt.',
                    'Rätten förenar auberginens fibrer med lykopen från tomaten och olivolja.'),
              faq=[dict(q='Passar zaalouk vid keto och bantning?',
                        a='Ja, mycket bra; nettokolhydraterna är få och den ger omättat fett och viktiga vitaminer.'),
                   dict(q='Vad är näringsvärdet i 100 g marockansk zaalouk?',
                        a='Den ger cirka 85 kcal (mest från jungfruolivoljan), 2 g protein, 5 g fett och 8,5 g kolhydrater '
                          '(varav cirka 4 g fibrer).'),
                   dict(q='Kan zaalouk hjälpa vid viktnedgång?',
                        a='Ja, den mättar länge tack vare de många fibrerna och har en kraftig kryddig smak som minskar '
                          'suget efter fet mat.')]),
    521: dict(lead='Marockansk taktouka är en varm och färgglad sallad: grillad och skalad paprika som sjuder på låg värme '
                   'med tjock tomatsås, olivolja, vitlök, spiskummin och paprikapulver. Det glykemiska indexet är inte '
                   'tillämpligt eftersom den saknar stärkelse, och den innehåller mycket C-vitamin.',
              tips=('Servera den varm eller kall till grillad fisk eller fågeltaginer; den söta och rökiga smaken berikar '
                    'bordet helt utan socker.',
                    'Grilla den gröna och röda paprikan över eld och skala den utan att skölja den i vatten, så bevaras '
                    'den djupa grillsmaken, och låt den sedan sjuda med tomat och jungfruolivolja.',
                    'Grillad paprika hör till de livsmedel som innehåller mest C-vitamin; C-vitamin bidrar till '
                    'immunsystemets normala funktion.'),
              faq=[dict(q='Höjer taktouka blodsockret?',
                        a='Nej, den påverkar inte blodsockret; den består av vattenrika grönsaker och jungfruolivolja, och '
                          'det glykemiska indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier finns i 100 g taktouka?',
                        a='Portionen innehåller cirka 80 kcal, 1,5 g protein, 4,5 g fett och 7 g naturliga kolhydrater.'),
                   dict(q='Vad är skillnaden mellan taktouka och zaalouk?',
                        a='Taktouka bygger helt på grillad paprika och tomat, medan zaalouk främst bygger på mosad '
                          'aubergine.')]),
    522: dict(lead='Marockansk batbout (litet matloubröd som gräddas i stekpanna) är ett runt, luftigt bröd som är ihåligt '
                   'inuti som en ficka och mycket omtyckt till smörgåsar vid frukost. Det glykemiska indexet är medelhögt '
                   '(en kliniskt granskad uppskattning, 65), och portionen behöver hållas måttlig vid diabetes.',
              tips=('Ät ett litet bröd (stort som en handflata) fyllt med tonfisk eller kokt ägg med sallat och tomat; '
                    'proteinet och fibrerna bromsar upptaget av brödets stärkelse.',
                    'Gör batbout med 50 % fullkornsdurumvete eller kornmjöl blandat med vetemjöl för mer fibrer och '
                    'långsammare nedbrytning.',
                    'Gräddning i en het torr panna gör brödet lätt och fritt från fett, men det vita mjölet höjer '
                    'blodsockret snabbt om det inte kombineras med protein.'),
              faq=[dict(q='Varför är det glykemiska indexet för batbout medelhögt (65)?',
                        a='Därför att det görs av fint jäst mjöl som gräddas snabbt på plåten, så att stärkelsekedjorna '
                          'bryts ned lätt och snabbt i tarmen.'),
                   dict(q='Vad är näringsvärdet i ett litet vanligt batbout (70 g)?',
                        a='Brödet ger cirka 180 kcal, 6 g protein, 1 g fett och cirka 36 g snabbt upptagna kolhydrater.'),
                   dict(q='Är batbout av fullkornsvete bättre vid diabetes?',
                        a='Ja, betydligt bättre; batbout med kli innehåller mycket fibrer som bromsar sockerupptaget och '
                          'mättar flera timmar längre.')]),
    523: dict(lead='Marockanska baghrir (pannkakorna med tusen hål) är de kända pannkakorna från Maghreb med täta, '
                   'förtrollande hål som suger upp honung och smält smör; de görs av fina mannagryn och jäst och gräddas '
                   'bara på ena sidan. Det glykemiska indexet är medelhögt (en kliniskt granskad uppskattning, 65), och de '
                   'pryder de traditionella frukostborden.',
              tips=('Ät en medelstor pannkaka med lite olivolja eller naturlig honung, tillsammans med ett kokt ägg och en '
                    'kopp te utan socker.',
                    'Grädda baghrir i en kall non-stick panna som torkas av med vatten mellan varje pannkaka, så får du de '
                    'täta hålen utan fett i tillagningen.',
                    'Själva smeten är fettfri, men risken vid diabetes kommer från förmågan att suga upp stora mängder '
                    'smör och honung, så mängden fett och sötning behöver styras.'),
              faq=[dict(q='Kan den som har diabetes äta baghrir?',
                        a='Ja, en liten pannkaka stor som en handflata (80 g), om den smörjs med en tesked naturlig honung '
                          'eller olivolja i stället för att dränkas i sirap.'),
                   dict(q='Hur många kalorier finns i en vanlig baghrir utan tillbehör (80 g)?',
                        a='En naturell pannkaka innehåller cirka 170 kcal, 4,5 g protein, mindre än 2 g fett och 34 g '
                          'stärkelse.'),
                   dict(q='Vad är hemligheten bakom de täta hålen i baghrir?',
                        a='Den dubbla jäsningen med jäst och bakpulver och gräddningen på medelvärme på bara ena sidan gör '
                          'att luftbubblorna spricker uppåt och bildar de kända hålen.')]),
    524: dict(lead='Marockansk harcha är det gyllene stekpannebrödet av mannagryn, smör och olivolja, krispigt utanpå och '
                   'mjukt inuti, och en följeslagare till eftermiddagsfikat på marockanska kaféer. Det glykemiska indexet '
                   'är medelhögt (en kliniskt granskad uppskattning, 68), och brödet ger varm och koncentrerad energi.',
              tips=('Nöj dig med en liten triangel (stor som en handflata) och bred på vit färskost eller olivolja i '
                    'stället för söt marmelad, så vägs mannagrynens stärkelse upp.',
                    'Gör harcha med jungfruolivolja och fullkornsmannagryn i stället för industriellt smör och raffinerade '
                    'mannagryn, så minskar det mättade fettet och fibrerna fördubblas.',
                    'Mannagryn innehåller mycket snabb stärkelse och många kalorier; därför kräver harcha strikt '
                    'portionskontroll vid insulinresistens och fettlever.'),
              faq=[dict(q='Varför höjer harcha blodsockret snabbt?',
                        a='Därför att den bygger på fina mannagryn som bryts ned snabbt, och det glykemiska indexet är '
                          'medelhögt (cirka 68), vilket kräver måtta i mängden.'),
                   dict(q='Vad är näringsvärdet i en vanlig bit harcha (80 g)?',
                        a='Den ger cirka 235 kcal, 5 g protein, 7 g fett och cirka 38 g stärkelse.'),
                   dict(q='Är harcha av korngryn (belboula) ett bättre val?',
                        a='Ja, betydligt bättre; att byta vetemannagryn mot korngryn ger mer betaglukaner och ett tydligt '
                          'lägre glykemiskt index vid diabetes.')]),
    525: dict(lead='Marockansk chebakia (mkharqa) är en anrik festlig sötsak: ett invecklat flätat bakverk som friteras i '
                   'olja och doppas i naturlig honung kryddad med apelsinblomsvatten, saffran och kanel och garneras med '
                   'rostade sesamfrön. Det glykemiska indexet är högt (en kliniskt granskad uppskattning, 72), och den är '
                   'en energi- och sockerbomb som kräver stor försiktighet.',
              tips=('En liten bit räcker helt för att smaka den traditionella smaken vid festliga tillfällen efter en '
                    'komplett proteinrik måltid, och den bör inte ätas dagligen.',
                    'För en bättre hemgjord variant: grädda chebakian i ugnen i stället för att fritera den, och pensla '
                    'med lite honung och sesam i stället för att doppa den djupt.',
                    'Sträng klinisk varning: kombinationen av fritering i olja, koncentrerad honung och vitt mjöl höjer '
                    'blodsockret och blodfetterna (triglyceriderna) mycket snabbt.'),
              faq=[dict(q='Kan den som har diabetes äta chebakia vid festliga tillfällen?',
                        a='Det rekommenderas att avstå; om du vill smaka, nöj dig med en halv mycket liten bit efter '
                          'måltiden och räkna med cirka 9 g snabbt socker.'),
                   dict(q='Hur många kalorier finns i en medelstor chebakia (30 g)?',
                        a='En bit innehåller cirka 125 kcal, 2 g protein, 5 g fett och cirka 19 g kolhydrater och socker.'),
                   dict(q='Vad bidrar sesamen och anisen med i chebakia?',
                        a='Sesamfröna, anisen och den malda mandeln i degen ger kalcium och aromatiska oljor, men sockret '
                          'och friteringen väger tyngre.')]),
    526: dict(lead='Marockansk sellou (sfouf, tqawt) är en traditionell, energität blandning som förr gjordes efter '
                   'förlossning och till högtider: rostat mjöl, rostad mandel, malda sesamfrön, anis och kanel med '
                   'olivolja eller honung. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 50) tack '
                   'vare de rikliga nötterna och fettet.',
              tips=('Ät bara två matskedar (30 g) som förmiddagsmål; fettet i mandeln och sesamen ger ett långvarigt '
                    'mellanmål.',
                    'Gör sellou på rostat kornmjöl eller havremjöl i stället för vitt mjöl, och använd jungfruolivolja och '
                    'lite äkta honung; undvik florsocker och smält smör.',
                    'Sellou innehåller vegetabiliskt kalcium, magnesium, E-vitamin och enkelomättat fett.'),
              faq=[dict(q='Varför är det glykemiska indexet för sellou relativt lågt (50) jämfört med andra traditionella '
                          'sötsaker?',
                        a='Därför att hälften av vikten består av sesamfrön och hel mandel, vars fett och fibrer tydligt '
                          'bromsar nedbrytningen av det rostade mjölet.'),
                   dict(q='Vad är näringsvärdet i 30 g sellou (två matskedar)?',
                        a='Portionen ger cirka 145 kcal, 3,5 g protein, 8 g fett och 14 g kolhydrater rika på fibrer och '
                          'mineraler.'),
                   dict(q='Passar sellou för den som vill gå upp i vikt?',
                        a='Ja, den är ett bra val för viktuppgång tack vare det naturligt höga energiinnehållet och fettet '
                          'från nötterna.')]),
    527: dict(lead='Saltade citroner (lagrade citroner på marockanskt vis) är själen i det marockanska köket: hela '
                   'citroner som lagras i sin egen saft och havssalt i månader tills skalet blir sammetslent och smörigt '
                   'med koncentrerad doft. Det glykemiska indexet är inte tillämpligt eftersom de saknar stärkelse, och de '
                   'ger mycket smak med få kalorier.',
              tips=('Använd en fjärdedel finhackat citronskal i taginer, grytor, fisk och grillat; den kraftiga smaken gör '
                    'att du inte behöver industriella buljongtärningar.',
                    'Skölj citronbiten i vatten innan du hackar den och tillsätt inget extra salt i rätten; saltet från '
                    'lagringen räcker för att salta hela rätten.',
                    'Lagrade citrusskal innehåller mycket limonen och flyktiga oljor; saltet kräver full försiktighet vid '
                    'högt blodtryck.'),
              faq=[dict(q='Höjer saltade citroner blodsockret?',
                        a='Nej, de påverkar inte blodsockret; de saknar stärkelse och socker, och det glykemiska indexet '
                          'är inte tillämpligt.'),
                   dict(q='Vad är näringsvärdet i en matsked hackad saltad citron (10 g)?',
                        a='Den innehåller mindre än 4 kcal, inget fett eller protein och mindre än 1 g naturliga '
                          'kolhydrater från skalet.'),
                   dict(q='Varför föredrar marockanska kockar skalet framför fruktköttet?',
                        a='Därför att lagringen bryter ned skalets beska och gör det smörigt och rikt på koncentrerade '
                          'aromatiska oljor, medan fruktköttet bara är surt och skarpt.')]),
    528: dict(lead='Harissa från Maghreb (stark chilipasta med kummin, vitlök och olivolja) är ett tunisiskt och '
                   'marockanskt arv som är upptaget på Unescos lista: en eldröd krydda som väcker sinnena och ger rätterna '
                   'en varm, oemotståndlig smak. Det glykemiska indexet är inte tillämpligt eftersom en portion nästan '
                   'saknar kolhydrater.',
              tips=('Tillsätt en tesked i tomatsåser, eller blanda den med olivolja som dipp till grillat och fisk.',
                    'Den görs genom att torkad röd chili gnids med vitlök, kumminfrön, torkad koriander och ren '
                    'jungfruolivolja; undvik kommersiella sorter med tillsatt stärkelse eller socker.',
                    'Harissa innehåller koncentrerat capsaicin; den får inte ätas vid aktivt magsår.'),
              faq=[dict(q='Höjer stark harissa blodsockret?',
                        a='Nej, kolhydraterna i en sked harissa är mycket få (cirka 1 g).'),
                   dict(q='Hur många kalorier finns i en matsked naturlig harissa (15 g)?',
                        a='Den innehåller bara cirka 13 kcal, främst från dropparna jungfruolivolja och chilipulvret, utan '
                          'härdat fett.'),
                   dict(q='Ger harissa hemorrojder?',
                        a='Chili orsakar inte hemorrojder i sig, men kan ge smärtsam irritation vid tarmtömning hos den '
                          'som redan har analfissur eller inflammerade hemorrojder.')]),
    529: dict(lead='Kolhapurikyckling är en av de mest kända och djärvaste starka rätterna i västra Indien: möra '
                   'kycklingbitar som tillagas i en mörkröd sås med smak av rostad kokos, garam masala och kashmirisk '
                   'chili. Det glykemiska indexet är inte tillämpligt eftersom rätten saknar nettokolhydrater, och den är '
                   'en eldig proteinrätt.',
              tips=('Ät kycklingbitarna med den fylliga såsen med sked tillsammans med gurksallad med yoghurt (raita) för '
                    'att dämpa hettan, och undvik att ta mycket vitt ris.',
                    'Att rosta korianderfrön och spiskummin med färsk riven kokos ger såsen en naturligt tjock konsistens '
                    'utan mjöl eller stärkelse.',
                    'De starka indiska kryddorna ger rätten dess karaktär, men rätten är mycket stark och kräver '
                    'försiktighet vid känslig mage och sur reflux.'),
              faq=[dict(q='Passar kolhapurikyckling vid keto?',
                        a='Ja, den är en utmärkt ketorätt: kyckling och protein med fett från kokosen och kryddor helt '
                          'utan socker.'),
                   dict(q='Vad är näringsvärdet i 250 g kolhapurikyckling?',
                        a='Portionen innehåller cirka 310 kcal, 33 g protein, 18 g fett och mindre än 5 g kolhydrater från '
                          'kryddorna.'),
                   dict(q='Höjer kashmirisk chili blodsockret?',
                        a='Nej, den påverkar inte blodsockret; den ger en djupröd färg och varm smak med måttlig hetta.')]),
    530: dict(lead='Rogan josh är en lyxig pärla i det kashmiriska köket: bitar av lamm- eller kalvkött som tillagas '
                   'långsamt i en aromatisk röd buljong av kashmirisk chili, yoghurt, ingefära, fänkål och kardemumma. Det '
                   'glykemiska indexet är inte tillämpligt eftersom rätten saknar stärkelse, och den är en varm '
                   'vinterrätt.',
              tips=('Ät de möra köttbitarna med gaffel tillsammans med den aromatiska såsen, och nöj dig med en halv roti '
                    'av fullkornsvete.',
                    'Hemligheten bakom äkta rogan josh är att köttet tillagas långsamt i yoghurt och senapsolja eller '
                    'naturlig ghee med kashmiriska kryddor, utan lök eller vitlök i det kashmiriska originalreceptet.',
                    'Lammkött innehåller hemjärn, zink och B12-vitamin, och såsen kryddas med fänkål och ingefära.'),
              faq=[dict(q='Höjer rogan josh blodsockret?',
                        a='Nej; rätten består av kött, kryddor och yoghurt utan snabb stärkelse, och det glykemiska '
                          'indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 250 g rogan josh?',
                        a='Portionen ger cirka 340 kcal, 31 g protein, 22 g naturligt fett och mindre än 4 g kolhydrater '
                          'från kryddorna.'),
                   dict(q='Vad ger rogan josh dess karaktäristiska djupröda färg?',
                        a='Naturlig kashmirisk chili och rötterna från den traditionella växten ratanjot, en naturlig färg '
                          'helt utan konstgjorda färgämnen.')]),
    531: dict(lead='Kycklingkorma är den aristokratiska rätten i det moguliska köket i Indien: möra kycklingbitar i en '
                   'elfenbensvit, sammetslen sås med yoghurt, mandel- och cashewpasta och milda kryddor som kardemumma och '
                   'muskot. Det glykemiska indexet är inte tillämpligt eftersom rätten nästan saknar nettostärkelse (cirka '
                   '2,5 g per 100 g), och den är en förnäm och mild rätt.',
              tips=('Ät kycklingbitarna med nötsåsen med sked; fettet och proteinet mättar länge utan att du behöver '
                    'naanbröd av vitt mjöl.',
                    'Kormans konsistens bygger på cashew- och mandelpasta och yoghurt utan mjöl eller stärkelse, och den '
                    'innehåller enkelomättat fett.',
                    'Cashew och mandel ger magnesium och fett, men rätten innehåller mycket kalorier och portionen behöver '
                    'hållas i schack vid viktnedgång.'),
              faq=[dict(q='Är kycklingkorma stark som andra indiska curryrätter?',
                        a='Nej, korma är en mycket mild och krämig rätt utan chili, omtyckt av barn och av den som inte '
                          'tål starka kryddor.'),
                   dict(q='Vad är näringsvärdet i 250 g kycklingkorma?',
                        a='Portionen innehåller cirka 360 kcal, 32 g protein, 24 g fett från nötterna och bara cirka 6 g '
                          'kolhydrater.'),
                   dict(q='Passar kycklingkorma vid diabetes?',
                        a='Ja, mycket bra; den påverkar blodsockret lite, och nötternas fett och proteinet dämpar '
                          'blodsockerstegringen.')]),
    532: dict(lead='Vindaloo är en legend från den indiska delstaten Goa med portugisiskt ursprung: köttbitar som tillagas '
                   'i en eldig, syrlig sås kryddad med vinäger, vitlök, stark röd chili och spiskummin. Det glykemiska '
                   'indexet är inte tillämpligt eftersom rätten saknar stärkelse, och den är den djärvaste och starkaste '
                   'av alla curryrätter.',
              tips=('Ät den försiktigt med gaffel tillsammans med en kall gurksallad med yoghurt för att dämpa de '
                    'brännande kryddorna, och undvik att ta mycket stärkelse till.',
                    'Att marinera köttet i vinäger, vitlök och chili i flera timmar bryter ned köttfibrerna så att det '
                    'snabbt smälter i munnen.',
                    'Vindaloo innehåller ättiksyra och capsaicin; rätten är mycket stark och ska helt undvikas vid magsår '
                    'och ulcerös kolit.'),
              faq=[dict(q='Höjer vindaloo blodsockret?',
                        a='Nej, den påverkar inte blodsockret; den består av kött, vinäger och kryddor utan socker, och '
                          'det glykemiska indexet är inte tillämpligt.'),
                   dict(q='Hur många kalorier finns i 250 g vindaloo?',
                        a='Portionen ger cirka 310 kcal, 30 g protein, 19 g fett och mindre än 5 g kolhydrater från '
                          'vitlöken och kryddorna.'),
                   dict(q='Vad är hemligheten bakom den syrliga smaken i vindaloo?',
                        a="Naturlig vinäger; ordet kommer från den portugisiska rätten vinha d'alhos, som betyder kött "
                          'marinerat i vinäger och vitlök.')]),
    533: dict(lead='Dal makhani är en pärla bland rätterna från Punjab i Indien: hela svarta linser (urad dal) och '
                   'kidneybönor som tillagas långsamt i många timmar på låg värme med tomat, smör, ingefära och lite '
                   'grädde. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 38), och rätten är en '
                   'mättande och mycket len vegetarisk måltid.',
              tips=('Ät en varm skål med sked som huvudrätt eller doppa en roti av fullkornsvete i den; proteinet och de '
                    'lösliga fibrerna mättar i flera timmar.',
                    'Långsam tillagning av de svarta linserna ger en naturligt smörig konsistens; du kan minska smöret och '
                    'grädden till en sked och låta linserna själva stå för krämigheten.',
                    'Svarta linser och kidneybönor innehåller mycket lösliga fibrer, järn och magnesium.'),
              faq=[dict(q='Passar dal makhani vid diabetes och insulinresistens?',
                        a='Ja, mycket bra; det glykemiska indexet är lågt (cirka 38), och de komplexa fibrerna gör att '
                          'glukosen frisätts långsamt i blodet.'),
                   dict(q='Vad är näringsvärdet i 200 g dal makhani?',
                        a='Portionen innehåller cirka 220 kcal, 10 g vegetabiliskt protein, 8 g fibrer och cirka 26 g '
                          'kolhydrater som smälts långsamt.'),
                   dict(q='Vad är skillnaden mellan dal makhani och vanlig gul indisk dal?',
                        a='Gul dal är lätt, snabblagad och tunn, medan dal makhani görs av hela svarta linser och bönor '
                          'och har en tung, sammetslen konsistens och djup kryddig smak.')]),
    534: dict(lead='Chana masala är den kända, kryddiga kikärtsrätten från norra Indien: kokta kikärter som drar åt sig en '
                   'sås av tomat, lök, ingefära, garam masala och torkat mangopulver (amchur). Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 32), och rätten är en vegetarisk måltid rik på järn.',
              tips=('Ät den med sked tillsammans med en grönsakssallad, lite färsk koriander och en skvätt citron; '
                    'C-vitamin ökar järnupptaget.',
                    'Blötlägg kikärterna över natten, och använd amchurpulver (omogen mango) eller citronsaft för den äkta '
                    'indiska syran utan tillsatt socker.',
                    'Kikärter innehåller mycket fibrer, och det låga glykemiska indexet gör rätten till ett bra val när '
                    'blodsockret ska hållas i schack.'),
              faq=[dict(q='Kan chana masala hjälpa vid viktnedgång?',
                        a='Ja; kikärter innehåller mycket vegetabiliskt protein och fibrer och mättar i många timmar efter '
                          'måltiden.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i 200 g chana masala?',
                        a='Portionen ger cirka 210 kcal, 11 g vegetabiliskt protein, 9 g fibrer och cirka 30 g komplexa '
                          'kolhydrater.'),
                   dict(q='Ger indiska kikärter gaser i tarmen?',
                        a='Att koka kikärterna med färsk ingefära, spiskumminfrön och svartkummin som i det indiska '
                          'receptet minskar gasbildningen och gör dem lättare att smälta.')]),
    535: dict(lead='Aloo gobi är den klassiska indiska hemrätten med potatis och blomkål: krispiga blomkålsbuketter och '
                   'stekta potatistärningar med gurkmeja, ingefära, spiskummin och koriander. Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 48), eftersom blomkålens fibrer uppväger potatisens höga '
                   'glykemiska index.',
              tips=('Se till att portionen innehåller mer blomkål än potatis, och ät den med gaffel tillsammans med en bit '
                    'grillat protein eller en grön sallad.',
                    'Tillaga blomkålen och potatisen i en torr panna med ånga och kryddor utan mycket vatten, så behåller '
                    'blomkålen sin krispighet utan att falla sönder eller suga upp stekfett.',
                    'Blomkål innehåller sulforafan, och gurkmejan ger kurkumin.'),
              faq=[dict(q='Passar aloo gobi vid diabetes trots potatisen?',
                        a='Ja, med måtta; det glykemiska indexet är lågt (cirka 48) eftersom den stora mängden blomkål, '
                          'kryddorna och senapsoljan bromsar upptaget av potatisstärkelsen.'),
                   dict(q='Vad är näringsvärdet i 200 g tillagad aloo gobi?',
                        a='Portionen innehåller cirka 160 kcal, 4 g protein, 5 g fett och 24 g kolhydrater (varav 5 g '
                          'fibrer).'),
                   dict(q='Hur gör jag aloo gobi ketovänlig?',
                        a='Byt ut potatistärningarna mot zucchini eller tofu, eller nöj dig med enbart blomkål (gobi '
                          'masala).')]),
    536: dict(lead='Bhindi masala är den indiska rätten med krispig stekt okra: skivade okraskidor som steks på hög värme '
                   'med lök, tomat, spiskummin, mangopulver och varma kryddor helt utan slemmighet. Det glykemiska indexet '
                   'är lågt (en kliniskt granskad uppskattning, 25), och rätten är ett bra val vid diabetes.',
              tips=('Ät den med gaffel som huvudsakligt grönsakstillbehör; den krispiga konsistensen och den syrliga '
                    'smaken ger stor njutning.',
                    'Hemligheten är att torka okran helt efter sköljningen innan den skärs, och att steka den på hög värme '
                    'med citronsaft så att slemämnena inte frigörs.',
                    'Okra innehåller slemämnen (mucilage), en typ av lösliga fibrer.'),
              faq=[dict(q='Varför är okra ett bra val vid diabetes?',
                        a='Därför att det glykemiska indexet är lågt (cirka 25), och de lösliga fibrerna dämpar plötsliga '
                          'blodsockertoppar.'),
                   dict(q='Hur många kalorier finns i 150 g bhindi masala?',
                        a='Portionen innehåller cirka 130 kcal, 4 g protein, 5 g fett och cirka 16,5 g kolhydrater (varav '
                          '6 g fibrer).'),
                   dict(q='Förlorar indisk okra sina näringsämnen utan sås?',
                        a='Torrstekning bevarar C-vitaminet och zinken betydligt bättre än lång kokning i vatten.')]),
    537: dict(lead='Indisk äggcurry (anda curry) är en billig, proteinrik och snabb måltid: kokta ägg som lätt bryns i '
                   'olja och läggs i en currysås av tomat, lök, ingefära, kokosmjölk och kryddor. Det glykemiska indexet '
                   'är inte tillämpligt eftersom rätten saknar nettokolhydrater, och den passar bra vid keto och bantning.',
              tips=('Ät två ägg med den goda såsen med gaffel tillsammans med en grön sallad; en komplett proteinrik '
                    'måltid som mättar hela kvällen.',
                    'Gör små skåror med kniven i de kokta äggen innan du bryner dem med gurkmeja, så att currysåsens smak '
                    'tränger in ända till gulan.',
                    'Äggulan innehåller kolin, lutein och B12-vitamin, och såsen kryddas med gurkmeja och ingefära.'),
              faq=[dict(q='Höjer äggcurry blodsockret?',
                        a='Nej, den påverkar inte blodsockret; den består av protein, fett och kryddor utan stärkelse, och '
                          'det glykemiska indexet är inte tillämpligt.'),
                   dict(q='Vad är näringsvärdet i en portion äggcurry (två ägg med sås, 250 g)?',
                        a='Portionen ger cirka 270 kcal, 15 g fullvärdigt protein, 20 g fett och mindre än 5 g kolhydrater '
                          'från tomatsåsen.'),
                   dict(q='Passar äggcurry för den som tränar?',
                        a='Ja, den är ett bra och billigt val med animaliskt protein av hög kvalitet utan härdat fett; '
                          'protein bidrar till att öka muskelmassan.')]),
    538: dict(lead='Indisk grönsakssamosa är den mest kända krispiga gatuförrätten i Indien med sin karaktäristiska '
                   'pyramidform: en krispig deg fylld med kryddad potatis, ärter, koriander och rostade spiskumminfrön. '
                   'Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 54), och den är en god förrätt där '
                   'portionen behöver styras.',
              tips=('Nöj dig med en medelstor samosa med mynta- och korianderchutney, och undvik att doppa den i söt '
                    'kommersiell tamarindsås.',
                    'Grädda samosan i airfryer eller ugn efter att ha penslat den med lite olja i stället för att fritera '
                    'den i mycket olja; du får samma krispighet med hälften av kalorierna.',
                    'Ärterna, spiskumminen och koriandern i fyllningen ger fibrer, men den friterade degen och '
                    'potatisstärkelsen kräver försiktighet vid diabetes och viktkontroll.'),
              faq=[dict(q='Är grönsakssamosa tillåten vid diabetes?',
                        a='Ja, bara en (100 g), helst ugnsbakad; det glykemiska indexet ligger på gränsen 54 (lågt), och '
                          'det viktiga är att inte äta för mycket friterad stärkelse.'),
                   dict(q='Hur många kalorier finns i en vanlig indisk grönsakssamosa (100 g)?',
                        a='En friterad samosa innehåller cirka 260 kcal, 5 g protein, 14 g fett och 28 g kolhydrater.'),
                   dict(q='Vilken chutney passar bäst till samosa?',
                        a='Chutney på mynta och koriander med citron och grön chili, eftersom den saknar socker.')]),
    539: dict(lead='Indisk roti (chapati) är det dagliga osyrade brödet av fullkornsvete som gräddas på en het torr plåt '
                   'utan en droppe olja. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 52), och '
                   'brödet är ett indiskt vardagsval som passar vid diabetes och bantning.',
              tips=('Ät ett eller två bröd stora som en handflata till dal, stekta grönsaker och protein, utan att pensla '
                    'dem med mycket ghee.',
                    'Fullkornsvetemjöl (atta) knådas bara med ljummet vatten, kavlas tunt och gräddas på en het tawa tills '
                    'det blåser upp av ångan inuti, helt utan olja.',
                    'Roti innehåller vetekli, olösliga fibrer och B-vitaminer, vilket gör den till ett betydligt bättre '
                    'val än kommersiellt naanbröd av vitt mjöl.'),
              faq=[dict(q='Varför anses roti vara det bästa brödet vid diabetes?',
                        a='Därför att den görs av fullkornsvetemjöl med kli utan socker och olja, och det glykemiska '
                          'indexet är lågt (cirka 52).'),
                   dict(q='Vad är näringsvärdet i en indisk roti (40 g)?',
                        a='Brödet ger bara cirka 110 kcal, 3,5 g protein, mindre än 1 g fett och 22 g komplexa kolhydrater '
                          'rika på fibrer.'),
                   dict(q='Vad är skillnaden mellan roti, chapati och paratha?',
                        a='Roti och chapati är torrt fullkornsbröd utan olja, medan paratha kavlas ut i lager med ghee '
                          'eller olja och innehåller mer kalorier och fett.')]),
    540: dict(lead='Indisk paratha är det flagiga och krispiga frukostbrödet: vetedeg som kavlas ut och viks i lager med '
                   'ghee eller olja och steks på plåten tills den får gyllene färg och spröd konsistens. Det glykemiska '
                   'indexet är medelhögt (en kliniskt granskad uppskattning, 62), och brödet ger mättande vinterenergi som '
                   'kräver måtta.',
              tips=('Nöj dig med ett medelstort bröd och ät det med grekisk yoghurt eller kokt ägg och färska grönsaker, '
                    'och undvik paratha fylld med dubbelstekt potatis.',
                    'Gör paratha med fullkornsvetemjöl och pensla lagren med lite naturlig ghee eller olivolja i stället '
                    'för härdat vegetabiliskt fett.',
                    'Lagren med fett ger god smak och bromsar upptaget något, men fördubblar kalorierna och det mättade '
                    'fettet; därför rekommenderas ett enda bröd vid hjärtsjukdom och diabetes.'),
              faq=[dict(q='Passar paratha vid diabetes?',
                        a='Det glykemiska indexet är medelhögt (cirka 62), men kalorierna och fettet är höga, så det är '
                          'bättre att äta torr roti till vardags och spara paratha till festliga tillfällen.'),
                   dict(q='Hur många kalorier finns i en vanlig indisk paratha (80 g)?',
                        a='Brödet innehåller cirka 275 kcal, 5 g protein, 12 g fett och cirka 35 g stärkelse.'),
                   dict(q='Vad är fylld paratha (aloo paratha)?',
                        a='En paratha fylld med kryddad potatis; den är mycket mäktig och rik på stärkelse, och ett bröd '
                          'kan innehålla mer än 380 kcal.')]),
    541: dict(lead='Mangolassi är världens mest kända indiska sommardryck: en sammetslen och svalkande blandning av mogen '
                   'tropisk mango, yoghurt och filmjölk med en nypa kardemumma och saffran. Det glykemiska indexet är lågt '
                   '(en kliniskt granskad uppskattning, 48) tack vare det rikliga proteinet och fettet i yoghurten.',
              tips=('Drick ett litet kallt glas som svalkande efterrätt efter en stark måltid; mjölkproteinet kasein '
                    'släcker hettan från de brännande kryddorna i munnen direkt.',
                    'Mixa färsk naturlig mango med grekisk yoghurt med låg fetthalt, isbitar och en nypa kardemumma utan '
                    'att tillsätta vitt socker eller sirap.',
                    'Yoghurten ger mjölksyrabakterier, kalcium och protein, och mangon ger A- och C-vitamin, men '
                    'kommersiell lassi innehåller tillsatt socker som snabbt höjer kalorierna.'),
              faq=[dict(q='Passar mangolassi vid diabetes?',
                        a='Ja, i den naturliga osötade varianten och i en liten portion (150–200 ml); det glykemiska '
                          'indexet är lågt (cirka 48) tack vare yoghurtens protein.'),
                   dict(q='Vad är näringsvärdet i ett glas hemgjord mangolassi (250 ml)?',
                        a='Glaset ger cirka 170 kcal, 7 g protein, 4 g fett och cirka 26 g kolhydrater och naturligt '
                          'fruktsocker.'),
                   dict(q='Varför släcker mjölkprodukter hettan från chili i indisk mat?',
                        a='Därför att kaseinet i mjölk och yoghurt löser upp och bryter ned de feta capsaicinmolekylerna '
                          'som fastnar på tungans värmereceptorer, till skillnad från vatten som sprider dem.')]),
    542: dict(lead='Indisk masala chai med mjölk och kryddor är den mest kända varma gatudrycken i Indien: starkt svart te '
                   'som kokas med mjölk och en förtrollande blandning av färsk ingefära, kardemumma, kanel, kryddnejlika '
                   'och svartpeppar. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 45) tack vare '
                   'mjölkfettet.',
              tips=('Drick det varmt som en härlig morgondryck som värmer kroppen, och drick det utan vitt socker så att '
                    'du njuter av kryddornas naturliga sötma.',
                    'Koka de nymalda kryddorna med svart te och mjölk på låg värme tills smakerna förenas, och använd '
                    'naturliga sötningsmedel som stevia eller drick det osötat.',
                    'Ingefära, kanel och kryddnejlika ger drycken dess karaktär.'),
              faq=[dict(q='Höjer indisk masala chai blodsockret?',
                        a='Om det görs utan tillsatt socker är det glykemiska indexet lågt (cirka 45) och det höjer inte '
                          'blodsockret.'),
                   dict(q='Vad är näringsvärdet i en kopp osötad masala chai med mjölk (250 ml)?',
                        a='Koppen innehåller cirka 90 kcal från mjölkens protein och fett, med 5 g protein och 8 g '
                          'kolhydrater från naturlig laktos.'),
                   dict(q='Vad är skillnaden mellan karak och indisk masala chai?',
                        a='Indisk masala chai fokuserar på de sex kryddorna (ingefära, kanel, kardemumma, kryddnejlika, '
                          'svartpeppar och fänkål) med färsk mjölk, medan karak från Gulfstaterna oftast görs på '
                          'kondenserad mjölk, kardemumma och saffran.')]),
    543: dict(lead='Gulab jamun är den obestridda kungen bland indiska och pakistanska sötsaker: mjuka gyllene bollar av '
                   'torkade mjölkfasta ämnen (khoya) som friteras varsamt och dränks i en aromatisk sockerlag kryddad med '
                   'kardemumma, rosenvatten och saffran. Det glykemiska indexet är högt (en kliniskt granskad '
                   'uppskattning, 78), eftersom de är en socker- och sirapsbomb som kräver stor försiktighet.',
              tips=('Nöj dig med en mycket liten boll vid stora festliga tillfällen, pressa ur överflödig sockerlag innan '
                    'du äter den, och ät den aldrig på fastande mage.',
                    'Bollarna kan gräddas i airfryer och läggas i en lätt lag sötad med steviaextrakt, rosenvatten och '
                    'saffran för att minska den kraftiga effekten på blodsockret.',
                    'Sträng klinisk varning: en snabbt upptagen sötsak som förenar fritering i ghee med full indränkning i '
                    'sockerlag; den höjer blodsockret och insulinet mycket snabbt.'),
              faq=[dict(q='Är gulab jamun förbjudet vid diabetes?',
                        a='Det rekommenderas att helt avstå; om du vill smaka, nöj dig med en halv liten boll efter en '
                          'komplett måltid och följ blodsockervärdena noga.'),
                   dict(q='Hur många kalorier finns i två gulab jamun (50 g)?',
                        a='Portionen innehåller cirka 190 kcal, 3 g protein, 6 g fett och cirka 32 g snabbt upptaget '
                          'socker.'),
                   dict(q="Varför heter de 'gulab jamun'?",
                        a="'Gulab' betyder rosenvatten på persiska, och 'jamun' syftar på den mörka indiska "
                          'jambolanfrukten, som de liknar i storlek och form.')]),
    544: dict(lead='Indisk kheer är den äldsta traditionella risgrynspuddingen på den indiska subkontinenten: basmatiris '
                   'som tillagas mycket långsamt i standardmjölk tills det löses upp till en krämig och aromatisk '
                   'konsistens kryddad med kardemumma och saffran och garnerad med pistage och mandel. Det glykemiska '
                   'indexet är medelhögt (en kliniskt granskad uppskattning, 60), och den är en varm festlig efterrätt.',
              tips=('Ät en liten kall skål som efterrätt efter en proteinrik lunch; nötterna och kanelen hjälper till att '
                    'bromsa sockerupptaget.',
                    'Koka riset i lättmjölk på mycket låg värme, och använd malda dadlar eller naturliga sötningsmedel i '
                    'stället för raffinerat vitt socker för färre kalorier.',
                    'Mjölken och nötterna ger kalcium, protein och fett, men den långkokta risstärkelsen och sockret '
                    'kräver måtta vid diabetes.'),
              faq=[dict(q='Vad är skillnaden mellan indisk kheer och arabisk risgrynspudding?',
                        a='Kheer kokas i timmar tills mjölken karamelliseras och får en ljust beige färg, utan tillsatt '
                          'raffinerad stärkelse, och kryddas med kardemumma, saffran, kewravatten, cashew och pistage.'),
                   dict(q='Vad är näringsvärdet i en vanlig skål indisk kheer (150 g)?',
                        a='Skålen ger cirka 230 kcal, 6 g protein, 6 g fett och cirka 39 g kolhydrater och socker.'),
                   dict(q='Kan kheer göras utan ris för den som har diabetes?',
                        a='Ja, det finns ett känt indiskt recept med valnötter, riven morot eller havre, som är betydligt '
                          'skonsammare för blodsockret.')]),
    545: dict(lead='Vietnamesisk pho (phở bò) är Vietnams mest kända nationalsoppa: en klar nötköttsbuljong som sjuder på '
                   'låg värme i 12 timmar med stjärnanis, kanel och ingefära och hälls över risnudlar, tunna köttskivor '
                   'och färska örter. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 50), eftersom '
                   'buljongen och proteinet dominerar över stärkelsen.',
              tips=('Börja med att dricka den aromatiska buljongen och äta köttskivorna, och fyll skålen med en stor näve '
                    'böngroddar, basilika, mynta och lime med mindre nudlar.',
                    'Hemligheten bakom pho är att svedja ingefäran och löken över eld innan de kokas med nötköttsbenen och '
                    'kryddorna, så att det bildas en djup och klar kollagenrik buljong utan tillsatta oljor.',
                    'Nötköttsbuljongen innehåller upplöst kollagen och glycin, och risnudlarna är lätta och glutenfria för '
                    'den som följer en känslig kost.'),
              faq=[dict(q='Passar vietnamesisk pho vid diabetes och bantning?',
                        a='Ja, mycket bra om mängden risnudlar begränsas; buljongen innehåller protein och kollagen utan '
                          'tungt fett, och det glykemiska indexet är lågt (cirka 50).'),
                   dict(q='Vad är näringsvärdet i en stor skål pho med nötkött (500 g)?',
                        a='Skålen ger cirka 400 kcal, 28 g protein, 8 g fett och cirka 48 g kolhydrater från risnudlarna '
                          'och grönsakerna.'),
                   dict(q='Varför läggs köttet rått i den heta pho-skålen (phở tái)?',
                        a='De mycket tunna köttskivorna läggs råa i skålen och den kokande buljongen hälls genast över, så '
                          'att de tillagas på sekunder och förblir möra och saftiga. Livsmedelsverket avråder gravida från '
                          'kött som inte är genomstekt; be då om genomkokt kött.')]),
    546: dict(lead='Färska vietnamesiska vårrullar (gỏi cuốn, summer rolls) är rullar fulla av fräschhet: kokta räkor och '
                   'färska örter som mynta och koriander, sallat och gurka rullade i tunt, genomskinligt rispapper. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 35), och de är ett omtyckt val för den '
                   'som vill äta enkel och ren mat.',
              tips=('Ät två till tre rullar och doppa dem i naturlig jordnötssås eller en sås av lime och chili; en lätt '
                    'och fräsch måltid.',
                    'Blöt rispapperet några sekunder i ljummet vatten tills det mjuknar och rulla det tätt runt räkorna '
                    'och örterna; undvik att fritera dem, så förblir de färska sommarrullar.',
                    'De saknar härdat fett och gluten och ger protein från havet med mycket vätska från de färska örterna '
                    'och grönsakerna.'),
              faq=[dict(q='Vad är skillnaden mellan färska sommarrullar och friterade vårrullar?',
                        a='Sommarrullarna äts färska i genomskinligt rispapper helt utan fritering, medan friterade '
                          'vårrullar friteras i mycket olja och blir mäktiga.'),
                   dict(q='Hur många kalorier finns i två sommarrullar med räkor (150 g)?',
                        a='Portionen innehåller cirka 165 kcal, 11 g protein, cirka 2 g fett och 24 g kolhydrater.'),
                   dict(q='Höjer rispapperet blodsockret?',
                        a='Rispapperet är mycket tunt och väger bara några gram, och fyllningen av räkor och grönsaker gör '
                          'att effekten på blodsockret blir långsam och måttlig (cirka 35).')]),
    547: dict(lead='Tom yum goong är världens mest kända syrliga och starka thailändska soppa: en fräsch räksoppa som '
                   'kokas med citrongräs, kaffirlimeblad, galangal, chili och halmsvamp. Det glykemiska indexet är inte '
                   'tillämpligt eftersom soppan saknar stärkelse.',
              tips=('Drick den syrliga, heta buljongen och ät räkorna och svampen med sked, och tugga inte de stora '
                    'bitarna galangal och citrongräs, som bara är till för smaken.',
                    'Koka räkskalen med de aromatiska thailändska örterna till en koncentrerad buljong, och lägg i räkorna '
                    'de sista tre minuterna så att de förblir möra och saftiga.',
                    'De tre thailändska örterna (galangal, citrongräs och limeblad) ger soppan dess karaktär, men den '
                    'syrliga hettan kräver måtta vid magkatarr.'),
              faq=[dict(q='Höjer tom yum blodsockret?',
                        a='Nej; den är en klar buljong med räkor, svamp och aromatiska kryddor utan stärkelse, och det '
                          'glykemiska indexet är inte tillämpligt.'),
                   dict(q='Vad är näringsvärdet i en skål tom yum med räkor (300 g)?',
                        a='Skålen ger bara cirka 130 kcal, 18 g protein, 3 g fett och mindre än 5 g naturliga kolhydrater.'),
                   dict(q='Vad är skillnaden mellan klar tom yum (nam sai) och krämig tom yum (nam khon)?',
                        a='Den klara är en ren och lätt örtbuljong, medan den krämiga får kokosmjölk eller evaporerad '
                          'mjölk och chilipasta och innehåller mer kalorier och fett.')]),
    548: dict(lead='Grön thaicurry (gaeng kiew wan) är kungen bland curryrätterna i Bangkok: kycklingbitar och runda '
                   'thailändska auberginer som tillagas i kokosmjölk med stark grön chilipasta, thaibasilika och '
                   'kaffirlimeblad. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 35), och rätten '
                   'förenar chilins hetta med kokosens krämiga sötma.',
              tips=('Ät kyckling- och auberginebitarna med den aromatiska kokossåsen med sked, och nöj dig med två till '
                    'tre matskedar basmati- eller jasminris.',
                    'Fräs den gröna currypastan i en sked kokosgrädde tills de aromatiska oljorna separerar och doften '
                    'kommer fram, och undvik att tillsätta mycket palmsocker.',
                    'Kokosmjölk innehåller medellånga fettsyror (MCT), och basilikan och chilin ger rätten dess karaktär.'),
              faq=[dict(q='Passar grön thaicurry vid diabetes och keto?',
                        a='Ja, den är en mycket bra ketorätt; det glykemiska indexet är lågt (cirka 35) och den innehåller '
                          'protein och fett som dämpar blodsockerstegringen när den äts utan ris.'),
                   dict(q='Hur många kalorier finns i 250 g grön thaicurry med kyckling?',
                        a='Portionen innehåller cirka 320 kcal, 24 g protein, 22 g fett från kokosen och cirka 7 g '
                          'kolhydrater från grönsakerna.'),
                   dict(q='Vad gör grön curry starkare än röd curry?',
                        a="Pastan görs av färsk grön thailändsk fågelögonchili (bird's eye chili), som är mycket stark och "
                          'skarp jämfört med torkad röd chili.')]),
    549: dict(lead='Röd thaicurry (gaeng phed) är en varm thailändsk rätt med djup smak: kyckling- eller räkbitar som '
                   'tillagas i kokosmjölk kryddad med torkad röd thailändsk chilipasta, citrongräs, vitlök, bambuskott och '
                   'basilika. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 35), och rätten ger en '
                   'lyxig asiatisk smakbalans.',
              tips=('Njut av rätten med gaffel och sked tillsammans med bambuskotten och köttet, och ät en grön sallad '
                    'till för att minska behovet av stärkelse vid sidan av.',
                    'Tillsätt bambuskott och paprika för mer fibrer och mättnad, och använd naturlig osötad kokosmjölk.',
                    'Rätten förenar röd chili, kokosmjölk och galangal, men kokosens mättade fett kräver måtta för den som '
                    'håller koll på det totala fettet.'),
              faq=[dict(q='Vad är skillnaden mellan röd och grön thaicurry?',
                        a='Röd curry bygger på torkad röd chili och är varmare, djupare och mindre skarp än grön curry, '
                          'som görs av färsk och skarp grön chili.'),
                   dict(q='Vad är näringsvärdet i 250 g röd thaicurry?',
                        a='Den ger cirka 310 kcal, 23 g protein, 21 g fett (bland annat MCT) och cirka 8 g kolhydrater som '
                          'tas upp lugnt.'),
                   dict(q='Passar röd thaicurry vid insulinresistens?',
                        a='Ja, mycket bra; nettokolhydraterna är få, det glykemiska indexet är lågt (cirka 35) och den '
                          'mättar länge.')]),
    550: dict(lead='Thailändsk grön papayasallad (som tam) är Asiens mest kända och fräschaste sallad: tunna, krispiga '
                   'strimlor av omogen grön papaya som stöts i mortel med chili, vitlök, lime, fisksås, tomat och '
                   'jordnötter. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 30).',
              tips=('Ät den som en fräsch förrätt före huvudrätten; fibrerna fyller en stor del av magen.',
                    'Ingredienserna stöts i en mortel av trä så att smakerna blandas och papayastrimlorna mjuknar; be om '
                    'en halv tesked palmsocker eller inget alls, så hålls blodsockret i schack.',
                    'Grön papaya innehåller mycket av enzymet papain, som bryter ned protein. Gravida bör helt undvika '
                    'omogen papaya.'),
              faq=[dict(q='Passar grön papayasallad när man bantar?',
                        a='Ja, den är en av de bästa salladerna vid bantning; fibrerna ger en härlig krispig mättnad.'),
                   dict(q='Hur många kalorier finns i en vanlig tallrik thailändsk som tam (200 g)?',
                        a='Tallriken innehåller cirka 130 kcal (mest från skeden rostade jordnötter), 4 g protein, 5 g '
                          'fett och 18 g kolhydrater som tas upp långsamt.'),
                   dict(q='Hur skiljer sig grön papaya från mogen orange papaya?',
                        a='Den gröna används som en krispig grönsak med lite socker och mycket enzymer och resistent '
                          'stärkelse, medan den mogna är en söt orange frukt rik på fruktos.')]),
    551: dict(lead='Mango sticky rice är världens mest kända thailändska gatudessert, som förenar mangons naturliga '
                   'tropiska sötma med klibbigt ris i varm kokosmjölk och lite krispig sesam. En fyllig rätt som smeker '
                   'sinnena, men som kräver eftertanke på grund av den rikliga snabbt upptagna stärkelsen.',
              tips=('Ät den inte som ett mellanmål på fastande mage; det är bättre att dela tallriken med familjen och äta '
                    'den efter en måltid rik på fibrer och protein, så kommer sockret långsammare ut i blodet.',
                    'Minska det tillsatta vita sockret i kokossåsen, låt den mogna mangons naturliga sötma räcka, och byt '
                    'ut en del av det vita riset mot svart eller brunt klibbris för mer fibrer.',
                    'Vid diabetes och insulinresistens har rätten en hög glykemisk belastning (45). Se till att portionen '
                    'inte är större än halva den vanliga mängden (75 g), och ta en promenad på 15 minuter efter måltiden.'),
              faq=[dict(q='Höjer thailändsk mango sticky rice blodsockret snabbt?',
                        a='Ja, klibbris innehåller mycket snabbt nedbruten amylopektinstärkelse, och det glykemiska '
                          'indexet är medelhögt nära gränsen till högt (68), så det höjer blodsockret snabbt om det inte '
                          'äts i en begränsad och avvägd mängd.'),
                   dict(q='Passar den vid bantning eller viktnedgång?',
                        a='Den är en rätt med mycket kalorier (cirka 367 kcal per 150 g) och mättat fett från '
                          'kokosmjölken; därför passar den inte till vardags och kan bara ätas i en liten portion vid ett '
                          'festligt tillfälle.'),
                   dict(q='Vad är näringsvärdet i en vanlig portion (150 g)?',
                        a='Portionen ger 367 kcal, 5,3 g protein, 8,2 g fett och 66 g nettokolhydrater.')]),
    552: dict(lead='Kung pao-kyckling är kungen i det starka szechuanköket: en klassisk och livfull rätt som blandar möra '
                   'kycklingbitar med rostade jordnötter och den stickande szechuanpepparn som ger munnen en känsla av '
                   'värme och fräschhet. En måltid med mycket protein som inte behöver mycket stärkelse.',
              tips=('En komplett måltid i sig; ät den med en krispig grön sallad eller en handfull kokt basmatiris i '
                    'stället för stekt ris fullt av olja.',
                    'Tillaga ingredienserna i wok med snabb omrörning och bara en sked sesamolja, och undvik för mycket '
                    'majsstärkelse eller raffinerat socker i marinaden.',
                    'Det glykemiska indexet är lågt (45) och den glykemiska belastningen låg (8 per 200 g); protein bidrar '
                    'till att bibehålla muskelmassa. Den som har högt blodtryck bör vara uppmärksam på natriumet från '
                    'sojasåsen.'),
              faq=[dict(q='Hur många kalorier finns i en tallrik kung pao-kyckling?',
                        a='En portion på 200 g som lagats hemma med lite olja innehåller cirka 480 kcal och mycket protein '
                          '(44 g).'),
                   dict(q='Passar den vid keto och insulinresistens?',
                        a='Ja, mycket bra, om den görs utan tillsatt socker eller honung i såsen; den bygger på fettet i '
                          'jordnötterna och proteinet i kycklingen.'),
                   dict(q='Hur påverkar jordnötterna i rätten blodsockret?',
                        a='Fettet och fibrerna i jordnötterna bromsar tydligt nedbrytningen av måltiden och mättar i flera '
                          'timmar.')]),
    553: dict(lead='Pekinganka är en ikon i det kinesiska kejserliga köket: ett gyllene, glasklart och mycket krispigt '
                   'skinn över mört kött fullt av smak. Den serveras traditionellt med färska gurkskivor, salladslök och '
                   'hoisinsås inrullade i tunna kinesiska pannkakor.',
              tips=('Lägg mycket gurka och salladslök i rullen för att balansera ankans fyllighet, och njut av det '
                    'krispiga köttet utan att ta för mycket av den söta hoisinsåsen.',
                    'Vertikal stekning i ugn eller airfryer gör att det mesta av överflödigt fett droppar ned i '
                    'långpannan, så att den gyllene krispigheten behålls och kalorierna minskar.',
                    'Ankkött saknar kolhydrater och det glykemiska indexet är lågt (25), men kommersiell hoisinsås '
                    'innehåller socker; därför rekommenderas bara en tunn pensling vid diabetes.'),
              faq=[dict(q='Är skinnet på pekinganka ett bra val eller fullt av fett?',
                        a='Ankskinn innehåller en god andel enkelomättat fett (oljesyra, som i olivolja), men det '
                          'innehåller många kalorier och bör ätas med måtta.'),
                   dict(q='Är pekinganka tillåten vid keto?',
                        a='Ankkött och skinn passar vid keto, men byt ut pannkakorna mot salladsblad och använd sojasås '
                          'utan socker i stället för hoisin.'),
                   dict(q='Vad är näringsvärdet i 150 g pekinganka?',
                        a='Portionen ger 435 kcal, 30 g protein, 30 g fett och 9,3 g nettokolhydrater (mest från skeden '
                          'hoisin).')]),
    554: dict(lead='Den mest omtyckta rätten på asiatiska restauranger för den som vill äta lätt: möra skivor av kalvkött '
                   'i harmoni med gröna broccolibuketter och ostronsås med djup umamismak. Det glykemiska indexet är inte '
                   'tillämpligt eftersom kolhydraterna är få.',
              tips=('En utmärkt rätt till lunch eller middag efter träning; broccolin mättar väl, och nötköttet ger järn, '
                    'zink och B12-vitamin.',
                    'Wokfräs broccolin i bara 3 till 4 minuter med ånga så att den förblir krispig; lång tillagning gör '
                    'att den förlorar sulforafan.',
                    'Rättens glykemiska belastning är nära noll, och den ger ingen nämnvärd blodsockerstegring.'),
              faq=[dict(q='Kan nötkött med broccoli hjälpa vid viktnedgång?',
                        a='Ja, den är ett bra val tack vare balansen mellan mycket protein och broccolins fibrer, som '
                          'mättar länge med måttligt antal kalorier (cirka 438 kcal per 250 g).'),
                   dict(q='Hur påverkar rätten blodsockret?',
                        a='Den glykemiska belastningen är nära noll, och rätten ger ingen nämnvärd blodsockerstegring.'),
                   dict(q='Vad är näringsvärdet i 250 g?',
                        a='Den innehåller 438 kcal, 52 g fullvärdigt protein, 18 g fett och bara 10 g nettokolhydrater.')]),
    555: dict(lead='Mapo tofu är ett anrikt mästerverk från provinsen Sichuan: mjuka, silkeslena tofutärningar i en '
                   'glödande röd sås med smak av szechuanpeppar och sesamolja och lite köttfärs. En rätt som förenar de '
                   'asiatiska kryddornas värme med det lätta vegetabiliska sojaproteinet.',
              tips=('Tofun suger upp såsens smaker utmärkt; ät den som en varm rätt kalla dagar med stekta grönsaker som '
                    'dämpar kryddornas hetta.',
                    'Koka tofutärningarna i saltat vatten i en minut innan du lägger dem i såsen så att de inte faller '
                    'sönder när du rör, och använd äkta szechuanpeppar.',
                    'Stärkelsen är mycket låg (mindre än 5 g per 100 g), så det glykemiska indexet är inte tillämpligt och '
                    'den glykemiska belastningen obefintlig; ett bra val vid insulinresistens för den som vill ha en '
                    'mättande måltid med lite stärkelse.'),
              faq=[dict(q='Passar mapo tofu vid diabetes?',
                        a='Ja, mycket bra; tofu höjer inte blodsockret.'),
                   dict(q='Passar den i vegetarisk kost?',
                        a='Den traditionella varianten innehåller köttfärs, men köttet kan lätt bytas mot hackad '
                          'shiitakesvamp till en helt vegetarisk rätt med mycket protein.'),
                   dict(q='Vad är näringsvärdet i 250 g?',
                        a='Den innehåller cirka 360 kcal, 30 g protein, 22,5 g fett och bara 7,5 g nettokolhydrater.')]),
    556: dict(lead='Det mest kända traditionella mellanmålet på Asiens gator och tågstationer: kokta ägg med sprucket skal '
                   'som dras i timmar i en aromatisk buljong av svart te, kanelstänger, stjärnanis och sojasås, så att de '
                   'får förtrollande marmorerade ränder och en djup, jordig smak. Det glykemiska indexet är inte '
                   'tillämpligt eftersom de nästan saknar kolhydrater.',
              tips=('Ett komplett proteinrikt mellanmål för den som tränar eller arbetar; äggen kan förvaras i kylskåp och '
                    'ätas kalla som en snabb måltid som stillar hungern mellan måltiderna.',
                    'Knacka försiktigt på det kokta äggets skal med baksidan av en sked så att det bildas fina sprickor '
                    'där teets ämnen kan tränga in i äggvitan.',
                    'Teägg saknar nästan helt kolhydrater och påverkar inte blodsockret, och de innehåller kolin; kolin '
                    'bidrar till normal leverfunktion.'),
              faq=[dict(q='Ändrar tedragningen äggens näringsvärde?',
                        a='Svart te och stjärnanis tillför flavonoider och polyfenoler utan att tillföra några kalorier.'),
                   dict(q='Passar teägg vid keto och periodisk fasta?',
                        a='Ja, de är ett utmärkt val för att bryta en periodisk fasta och passar bra vid keto och '
                          'lågkolhydratkost; de mättar jämnt och länge.'),
                   dict(q='Vad är näringsvärdet i ett ägg (50 g)?',
                        a='Det innehåller 74 kcal, 6,4 g protein, 5,1 g fett och 0,6 g kolhydrater.')]),
    557: dict(lead='Kristallklara glasnudlar av ren mungbönsstärkelse har en hal, elastisk och mycket behaglig konsistens '
                   'att tugga, och de suger upp soppor och såser utan att förlora formen. De är naturligt glutenfria, och '
                   'det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 39).',
              tips=('Ät dem inte ensamma som en ren nudelrätt; tillsätt rikligt med bladgrönsaker, kycklingskivor eller '
                    'räkor för att sänka hela måltidens glykemiska belastning.',
                    'Blötlägg dem i hett vatten i bara några minuter i stället för att koka dem länge; lång kokning '
                    'påskyndar nedbrytningen av stärkelsen, medan kort blötläggning bevarar den geléartade strukturen.',
                    'Det glykemiska indexet är lågt (39) tack vare mungbönsstärkelsen, som är rik på amylos, vilket gör '
                    'dem till ett bra alternativ till vanliga nudlar och pasta av vitt mjöl vid diabetes.'),
              faq=[dict(q='Är glasnudlar glutenfria?',
                        a='Ja, de görs bara av mungbönsstärkelse och vatten och är naturligt glutenfria; kontrollera '
                          'förpackningen om du har celiaki.'),
                   dict(q='Passar glasnudlar vid viktnedgång?',
                        a='Kalorierna är måttliga efter tillagning (cirka 157 kcal per 150 g kokta) eftersom de suger upp '
                          'mycket vatten och fyller magen, men stärkelsen (38 g) behöver räknas in.'),
                   dict(q='Vad är skillnaden mot risnudlar?',
                        a='Mungbönsnudlar ger ett betydligt långsammare sockerupptag än nudlar av vitt ris, som har ett '
                          'tydligt högre glykemiskt index.')]),
    558: dict(lead='Japanska sobanudlar är mörkbruna nudlar med jordig, nötaktig smak som traditionellt görs av '
                   'fullkornsbovetemjöl utan vete. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 46), '
                   'och de är en förfinad japansk rätt som serveras kall med tsuyusås på sommaren eller varm på vintern.',
              tips=('Kall soba med noriremsor, salladslök och lite wasabi är en utmärkt lunch.',
                    'Koka dem i bara 5 minuter och skölj dem genast i iskallt rinnande vatten; sköljningen tar bort '
                    'ytstärkelsen, ger nudlarna fast konsistens och sänker det glykemiska indexet.',
                    'Det glykemiska indexet är lågt (46) och den glykemiska belastningen måttlig (12,6), och de innehåller '
                    'rutin.'),
              faq=[dict(q='Hur vet jag att sobanudlarna är fria från vete?',
                        a="Läs ingrediensförteckningen noga och leta efter '100 % buckwheat' (juwari soba), eftersom många "
                          'kommersiella sorter blandar bovete med vanligt vetemjöl.'),
                   dict(q='Passar soba vid diabetes och insulinresistens?',
                        a='Ja, de hör till de bästa komplexa stärkelsekällorna vid diabetes; det glykemiska indexet är '
                          'lågt, och de innehåller D-chiro-inositol.'),
                   dict(q='Vad är näringsvärdet i en vanlig portion (150 g kokta)?',
                        a='Portionen ger 148 kcal, 7,6 g vegetabiliskt protein, 0,2 g fett och 27,3 g nettokolhydrater med '
                          '4 g fibrer.')]),
    559: dict(lead='Den som älskar nudlar vet vilken trygghet en skål udonsoppa ger: breda, tjocka och mjuka nudlar med '
                   'stor elasticitet och sidenlen mjukhet som stillar suget efter god pasta i varm buljong. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 55).',
              tips=('Udon görs av vetemjöl, så låt dem inte vara den enda ingrediensen i skålen; fyll den med '
                    'dashibuljong, kokt ägg, spenat och shiitakesvamp för en balanserad måltid.',
                    'Ät udon al dente och koka dem inte för länge, så att glutenbindningarna inte bryts ned och stärkelsen '
                    'blir snabbt upptagen.',
                    'Det glykemiska indexet är lågt men på gränsen (55), och den glykemiska belastningen för 200 g är '
                    'relativt hög (28,4); därför bör den som har diabetes begränsa mängden eller välja soba i stället.'),
              faq=[dict(q='Gör udonnudlar att man går upp i vikt?',
                        a='En mättande portion (200 g kokta) innehåller 260 kcal och 51,6 g nettokolhydrater; med klar '
                          'buljong och grönsaker är den en måttlig måltid, men med friterade tillbehör och tjocka såser '
                          'bidrar den till viktuppgång.'),
                   dict(q='Är udon glutenfria?',
                        a='Nej, klassisk udon görs av vitt vetemjöl med mycket gluten, som ger den karaktäristiska sega '
                          'konsistensen, så den passar inte vid celiaki.'),
                   dict(q='Vad är näringsvärdet i en skål på 200 g?',
                        a='Den ger 260 kcal, 8 g protein, 1 g fett och 51,6 g nettokolhydrater.')]),
    560: dict(lead='Ett färgglatt konstverk i en het lerskål: en av de mest kända rätterna i det koreanska köket, som '
                   'förenar ris med kryddade grönsaker (morot, spenat, zucchini och böngroddar), kalvkött, ett stekt ägg i '
                   'mitten och den goda starka gochujangsåsen. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 52).',
              tips=('Blanda alla ingredienser snabbt innan du äter så att köttsaften förenas med äggets värme och såsen; '
                    'den stora färgvariationen ger många olika vitaminer och mineraler.',
                    'Beställ eller laga den med brunt ris i stället för vitt, och använd fermenterade grönsaker (kimchi).',
                    'Rätten innehåller fibrer och protein och har ett lågt glykemiskt index (52), men en hel portion (300 '
                    'g) innehåller en hel del ris (glykemisk belastning 39); vid diabetes rekommenderas att halvera riset '
                    'och dubbla grönsakerna och ägget.'),
              faq=[dict(q='Är bibimbap en balanserad måltid?',
                        a='Ja, den är en av de mest balanserade asiatiska rätterna, med fullvärdigt protein från kött och '
                          'ägg, fibrer från fem sorters grönsaker och stärkelse.'),
                   dict(q='Hur många kalorier finns i en skål bibimbap?',
                        a='En mättande skål på 300 g innehåller cirka 585 kcal och 28,5 g protein och mättar i många '
                          'timmar.'),
                   dict(q='Vad tillför kimchin och grönsakerna i bibimbap?',
                        a='De fermenterade grönsakerna innehåller mjölksyrabakterier och fibrer.')]),
    561: dict(lead='Bulgogi är världens mest kända koreanska grillrätt: tunna, möra skivor av kalvkött som smälter i '
                   'munnen, marinerade i en förtrollande blandning av mosat asiatiskt päron, sesamolja, soja och vitlök. '
                   'Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 25), och rätten mättar ordentligt.',
              tips=('Rulla in de grillade köttskivorna i stora salladsblad med en skiva färsk vitlök och en tesked kimchi; '
                    'det traditionella koreanska sättet minskar behovet av bröd och ger fräsch krispighet.',
                    'Låt päronmosets naturliga sötma möra köttet och undvik raffinerat vitt socker i marinaden, och grilla '
                    'köttet snabbt på hög värme så att saften stannar kvar.',
                    'Det glykemiska indexet är lågt (25) och den glykemiska belastningen nästan obefintlig (2,4), och '
                    'rätten är ett bra val vid diabetes och för den som tränar tack vare det höga proteininnehållet (36 g '
                    'per portion); protein bidrar till att bibehålla muskelmassa.'),
              faq=[dict(q='Passar bulgogi vid keto och lågkolhydratkost?',
                        a='Ja, mycket bra, om den görs hemma utan tillsatt socker eller majssirap, som vissa restauranger '
                          'använder.'),
                   dict(q='Hur många kalorier finns i en portion grillad bulgogi?',
                        a='En portion på 150 g innehåller cirka 322 kcal och mycket järn, zink och B12-vitamin.'),
                   dict(q='Höjer päronmarinaden blodsockret?',
                        a='Päronet används i liten mängd för sina enzymer som mörar köttet, och det höga proteinet och '
                          'sesamfettet dämpar blodsockerstegringen.')]),
    562: dict(lead='Den omtyckta japanska förrätten förenar två härliga motsatser: en gyllene, mycket krispig botten och '
                   'en mjuk, ångkokt ovansida som omsluter en fyllig fyllning av kycklingfärs med purjolök och frisk '
                   'ingefära. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 48).',
              tips=('Ät högst 4 till 6 stycken som en del av en komplett måltid med en grön sallad eller varm misosoppa, '
                    'så undviker du att äta för mycket deg.',
                    'Använd tekniken att först steka snabbt i en sked olja och sedan ångkoka, undvik fritering, och byt ut '
                    'färdiga såser mot risvinäger med några droppar natriumreducerad soja.',
                    'Det glykemiska indexet är lågt (48) och den glykemiska belastningen för 6 stycken (150 g) är 16,2; de '
                    'räknas som måttlig stärkelse vid diabetes och höjer inte blodsockret kraftigt tack vare '
                    'kycklingproteinet.'),
              faq=[dict(q='Gör gyoza att man går upp i vikt när man bantar?',
                        a='6 stycken som stekts lätt och sedan ångkokats ger 315 kcal; med måtta förstör de inte '
                          'bantningen, och hemligheten är att inte fritera dem.'),
                   dict(q='Hur minskar jag stärkelsen i gyoza vid insulinresistens?',
                        a='Välj mycket tunna degark, och dubbla fyllningen av kyckling, kål och purjolök på degens '
                          'bekostnad.'),
                   dict(q='Vad är näringsvärdet i 6 stycken (150 g)?',
                        a='De innehåller 315 kcal, 13,5 g protein, 12,8 g fett och 33,8 g nettokolhydrater.')]),
    563: dict(lead='Havets gröna gåva: ett havsgrönsak som växer i rent vatten och sväller när den blötläggs till mjuka, '
                   'smaragdgröna remsor med lätt jodsmak och naturligt fräsch sälta, och som är stjärnan i japansk '
                   'misosoppa. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 15).',
              tips=('Lägg en matsked blötlagd wakame i den dagliga salladen eller soppan; fibrerna suger upp vatten och '
                    'fyller magen.',
                    'Blötlägg den i ljummet vatten i bara 5 minuter och låt den rinna av; koka den inte länge, så att '
                    'fukoidan och de värmekänsliga vitaminerna bevaras.',
                    'Det glykemiska indexet och den glykemiska belastningen är nära noll (0,4), och wakame innehåller '
                    'naturligt jod; jod bidrar till normal produktion av sköldkörtelhormoner.'),
              faq=[dict(q='Är wakame bra vid underfunktion i sköldkörteln?',
                        a='Wakame hör till de rikaste naturliga källorna till jod, som behövs för att bilda '
                          'sköldkörtelhormoner, men den som har överfunktion i sköldkörteln eller autoimmun '
                          'sköldkörtelinflammation (Hashimoto) bör vara försiktig, eftersom för mycket jod kan förvärra '
                          'tillståndet.'),
                   dict(q='Vad är fukoxantin i wakame?',
                        a='Fukoxantin är ett naturligt pigment som finns i brunalger som wakame.'),
                   dict(q='Hur många kalorier finns i en portion blötlagd wakame (30 g)?',
                        a='Den innehåller bara 14 kcal, 1 g protein och cirka 2,6 g nettokolhydrater.')]),
    564: dict(lead='De svarta, krispiga arken som omsluter världens mest kända sushibitar: fjäderlätta ark av torkade och '
                   'varsamt rostade rödalger som ger god umamismak och en krispighet som gör dem till ett alternativ till '
                   'kommersiella chips. Det glykemiska indexet är inte tillämpligt eftersom nettostärkelsen är nära noll.',
              tips=('Ät dem som ett krispigt mellanmål mellan måltiderna eller använd dem i stället för bröd för att rulla '
                    'in tonfisk och avokado; de höjer inte blodsockret och innehåller mineraler.',
                    'Välj ark som rostats i olivolja eller sesamolja utan härdade oljor, och förvara förpackningen tätt '
                    'tillsluten med fuktabsorberande påse så att de förblir krispiga.',
                    'Nettostärkelsen är nära noll, så det glykemiska indexet är inte tillämpligt, och de innehåller lite '
                    'B12-vitamin.'),
              faq=[dict(q='Är noriark tillåtna vid keto?',
                        a='Ja, de passar mycket bra; ett ark innehåller nästan inga kolhydrater och ger mineraler.'),
                   dict(q='Är noriark ett bra alternativ till potatischips för barn?',
                        a='Ja, de ger samma goda krispighet men utan härdade oljor och utan raffinerad stärkelse, och de '
                          'innehåller jod och järn.'),
                   dict(q='Hur många kalorier och hur mycket protein finns i ett noriark (3 g)?',
                        a='Det innehåller cirka 10 kcal, cirka 1,2 g protein och ingen nettostärkelse.')]),
    565: dict(lead='Shiitake är kejsarnas svamp i det gamla asiatiska köket: tjocka bruna hattar med köttig konsistens och '
                   'träaktig umamismak som ger soppor och grytor ett fantastiskt djup. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 15).',
              tips=('Ett mycket bra sätt att ersätta kött i rätter vid diabetes och övervikt; svampen ger samma tuggkänsla '
                    'som kött med en fjärdedel av kalorierna och utan kolesterol.',
                    'Snabb stekning med lite olivolja och krossad vitlök, eller tillagning i soppor, frigör lentinan och '
                    'bevarar den köttiga konsistensen.',
                    'Det glykemiska indexet är lågt (15) och den glykemiska belastningen för 80 g bara 1,5; svampen '
                    'innehåller betaglukanfibrer.'),
              faq=[dict(q='Vilka ämnen finns i shiitakesvamp?',
                        a='Den innehåller polysackariden betaglukan och lentinan.'),
                   dict(q='Vad är eritadenin i shiitake?',
                        a='Eritadenin är ett naturligt ämne som förekommer i shiitakesvamp.'),
                   dict(q='Vad är näringsvärdet i 80 g tillagad shiitake?',
                        a='Portionen ger 45 kcal, 1,8 g protein, 1,7 g fibrer och 9,8 g nettokolhydrater som tas upp '
                          'långsamt.')]),
    566: dict(lead='Långa, snövita trådar med små runda huvuden som påminner om knappnålar; enokisvamp har en unik '
                   'krispighet och mycket mild, fruktig smak och är en självklar stjärna i asiatiska varma grytor (hot '
                   'pot). Det glykemiska indexet är inte tillämpligt eftersom stärkelsen är låg.',
              tips=('Lägg en näve enoki i den heta soppskålen en minut innan du äter; krispigheten gör måltiden roligare '
                    'och får dig att tugga långsamt.',
                    'Skär bort den sammanvuxna rotbasen och skölj svampen varsamt; tillaga den inte längre än två minuter, '
                    'så att den inte blir gummiaktig och förlorar sin omtyckta krispighet.',
                    'Det glykemiska indexet är inte tillämpligt och den glykemiska belastningen försumbar; svampen '
                    'innehåller mycket olösliga fibrer.'),
              faq=[dict(q='Kan enokisvamp hjälpa vid viktnedgång?',
                        a='Ja, den passar mycket bra vid bantning; 80 g innehåller bara 30 kcal och fyller magen väl.'),
                   dict(q='Kan enoki ätas rå i sallader?',
                        a='Den bör alltid ångkokas eller läggas i hett vatten i en minut för att döda eventuella bakterier '
                          'på ytan och göra fibrerna lättare att smälta. Livsmedelsverket rekommenderar att enokisvamp '
                          'alltid upphettas ordentligt eftersom den kan innehålla listeria.'),
                   dict(q='Vad är näringsvärdet i 80 g?',
                        a='Portionen ger 30 kcal, 2,2 g protein, 2,2 g fibrer och 4 g nettokolhydrater.')]),
    567: dict(lead='Små gyllene och orange kulor som arbetsbina samlar från blommornas nektar och pollen; bipollen '
                   'innehåller enzymer, vitaminer och alla essentiella aminosyror. Det glykemiska indexet är lågt (en '
                   'kliniskt granskad uppskattning, 30).',
              tips=('Börja med en fjärdedels tesked per dag och öka gradvis till en matsked (10 g); strö den över grekisk '
                    'yoghurt eller havregryn till frukost.',
                    'Blanda den aldrig med kokande eller heta drycker, så att de värmekänsliga B-vitaminerna och enzymerna '
                    'inte förstörs.',
                    'Det glykemiska indexet är lågt (30) och den glykemiska belastningen för en matsked bara 1,0.'),
              faq=[dict(q='Vem bör vara försiktig med bipollen?',
                        a='Den som har svår allergi mot bistick eller säsongsbunden pollenallergi; testa först med ett '
                          'enda korn.'),
                   dict(q='Vad innehåller bipollen?',
                        a='Den innehåller protein med essentiella aminosyror, B-vitaminer och kolhydrater.'),
                   dict(q='Vad är näringsvärdet i en matsked (10 g)?',
                        a='Den innehåller 31 kcal, 2,4 g fullvärdigt protein och 3,4 g naturliga kolhydrater.')]),
    568: dict(lead='Manukahonung kommer från Nya Zeelands orörda skogar: en tjock, mörk honung som bina samlar från '
                   'manukabuskens blommor, känd i hela världen för sitt innehåll av metylglyoxal (MGO). Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 55).',
              tips=('Ät en tesked till en matsked (10–20 g), eller lös upp den i ljummet (inte kokande) vatten.',
                    'Använd en träsked eller plastsked och kontrollera att förpackningen anger en verifierad MGO-halt. '
                    'Barn under ett år ska inte äta honung (Livsmedelsverket).',
                    'Det glykemiska indexet är lågt men på gränsen (55), och den glykemiska belastningen för en matsked '
                    '(20 g) är 8,8; vid diabetes räknas den som socker i en begränsad portion och inte som ett fritt '
                    'alternativ till socker.'),
              faq=[dict(q='Vad betyder MGO på manukahonung?',
                        a='MGO står för metylglyoxal, det ämne vars halt anges på förpackningen, till exempel MGO 400+.'),
                   dict(q='Är manukahonung ett säkert val vid diabetes?',
                        a='Den är fortfarande honung som innehåller glukos och fruktos, så portionen bör inte överstiga en '
                          'matsked (20 g) och den ska räknas in noga i förhållande till insulin- eller läkemedelsdosen.'),
                   dict(q='Vad är näringsvärdet i en matsked (20 g)?',
                        a='Den ger 62 kcal och 16 g nettokolhydrater från naturligt socker.')]),
    569: dict(lead='Vetegräspulver är koncentrerat klorofyll: små gröna skott som skördas innan kornen bildas och '
                   'frystorkas till ett mycket grönt pulver som samlar bladgrönsakernas näring i en tesked. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 15).',
              tips=('Blanda en tesked (5 g) med ett glas kallt vatten och en skvätt citron på morgonen.',
                    'Blanda det inte med heta drycker, och använd en handmixer så att pulvret löses upp utan klumpar, '
                    'gärna med lite grön äppeljuice för att mildra den gräsiga smaken.',
                    'Det glykemiska indexet är lågt (15) och den glykemiska belastningen obefintlig (0,1); vetegräs är '
                    'glutenfritt eftersom det skördas innan de glutenhaltiga vetekornen bildas.'),
              faq=[dict(q='Är vetegräspulver glutenfritt vid celiaki?',
                        a='Ja, gluten finns bara i kornen, medan själva gräset är glutenfritt, men välj en produkt som är '
                          'certifierad glutenfri (Certified Gluten-Free) för att undvika kontaminering.'),
                   dict(q='Vad innehåller vetegräs?',
                        a='Det innehåller klorofyll och tylakoider.'),
                   dict(q='Vad är näringsvärdet i 5 g?',
                        a='Det ger bara 13 kcal, 1,4 g protein och cirka 0,4 g nettokolhydrater med en god mängd A- och '
                          'C-vitamin.')]),
    570: dict(lead='Macapulver kommer från de peruanska Anderna: en rotknöl som växer under mycket hårda förhållanden högt '
                   'upp i bergen och mals till ett jordfärgat pulver med nötig karamellsmak. Det glykemiska indexet är '
                   'lågt (en kliniskt granskad uppskattning, 25).',
              tips=('Tillsätt en tesked (5–10 g) i varm kakao eller morgonens smoothie.',
                    'Välj gelatiniserad maca om din mage är känslig, eftersom den tunga stärkelsen har brutits ned så att '
                    'den blir lättare att smälta.',
                    'Det glykemiska indexet är lågt (25) och den glykemiska belastningen för 10 g bara 1,4.'),
              faq=[dict(q='Påverkar maca hormonerna?',
                        a='Det finns inga belägg för att maca förändrar hormonnivåerna i blodet.'),
                   dict(q='Innehåller maca koffein?',
                        a='Nej, maca innehåller inget koffein.'),
                   dict(q='Vad är näringsvärdet i en matsked (10 g)?',
                        a='Den innehåller 32 kcal, 1,4 g protein och 5,8 g komplexa kolhydrater samt järn och kalium.')]),
    571: dict(lead='Frukten från det afrikanska ”livets träd”: baobabfrukten torkar naturligt på grenarna i solens värme '
                   'och mals till ett gott, syrligt pulver med mycket C-vitamin och lösliga fibrer. Det glykemiska indexet '
                   'är inte tillämpligt eftersom nettokolhydraterna i en portion är få.',
              tips=('En matsked i dricksvattnet eller i naturlig juice ger mycket C-vitamin; C-vitamin ökar järnupptaget '
                    'och bidrar till normal kollagenbildning för hudens normala funktion.',
                    'Ett bra naturligt alternativ till citron i salladsdressingar, eller att röra ned i frukostyoghurten.',
                    'Nästan hälften av vikten är lösliga fibrer, och nettokolhydraterna i en vanlig portion (10 g) är '
                    'högst 2,5 g.'),
              faq=[dict(q='Hur mycket C-vitamin finns i baobab?',
                        a='Den innehåller ungefär sex gånger så mycket C-vitamin som färska apelsiner; C-vitamin bidrar '
                          'till immunsystemets normala funktion och till normal kollagenbildning.'),
                   dict(q='Vad innehåller baobab för fibrer?',
                        a='Baobab innehåller mycket lösliga fibrer, som fermenteras i tarmen och bildar kortkedjiga '
                          'fettsyror.'),
                   dict(q='Vad är näringsvärdet i en sked (10 g)?',
                        a='Den innehåller bara 24 kcal, 4,5 g lösliga fibrer och bara 2,5 g nettokolhydrater.')]),
    572: dict(lead='Riktig choklad som naturen skapade den innan industrin och sockret: kakaobönor som pressats och malts '
                   'kallt utan alkalisering (non-alkalized) och som behåller en mycket hög halt av flavanoler. Det '
                   'glykemiska indexet är inte tillämpligt eftersom nettokolhydraterna i en portion är få.',
              tips=('En matsked i en kopp varm mandeldryck med en nypa kanel blir en kraftfull varm choklad utan ett enda '
                    'gram socker.',
                    'Låt det inte koka; tillsätt kakaopulvret när mjölken har värmts så att de värmekänsliga flavanolerna '
                    'bevaras, och använd ren stevia om du vill söta.',
                    'Nettokolhydraterna i en vanlig portion (10 g) är högst 2,4 g, så det glykemiska indexet är inte '
                    'tillämpligt och den glykemiska belastningen nära noll; kakao innehåller mycket magnesium.'),
              faq=[dict(q='Vad är skillnaden mellan rå kakao (cacao) och vanlig kakao (cocoa)?',
                        a='Vanlig kakao utsätts för hög värme och alkalisering (holländsk metod), som gör att den förlorar '
                          'en stor del av flavanolerna, medan rå kakao bearbetas kallt och behåller det mesta.'),
                   dict(q='Är rå kakao tillåten vid keto?',
                        a='Ja, den är grundingrediensen i ketobakverk tack vare de många fibrerna, det naturliga fettet '
                          'och de mycket få nettokolhydraterna.'),
                   dict(q='Vad är näringsvärdet i en matsked (10 g)?',
                        a='Den ger 38 kcal, 2,4 g protein, 3,4 g fibrer och bara 2,4 g nettokolhydrater samt magnesium.')]),
    573: dict(lead='Det lyxiga, aromatiska vegetabiliska fettet som ger chokladen dess förtrollande sammetslena smältning: '
                   'ett rent fett som utvinns genom kallpressning av kakaobönor, med fyllig chokladdoft; det är fast i '
                   'rumstemperatur och smälter vid kroppstemperatur. Det glykemiska indexet är inte tillämpligt eftersom '
                   'det saknar kolhydrater.',
              tips=('Grunden för hemgjord ketochoklad och fat bombs; ren fettenergi som mättar i flera timmar.',
                    'Smält det i vattenbad (bain-marie) och blanda med rått kakaopulver och munkfruktsötning till mörka '
                    'chokladkakor som är bättre än de färdiga.',
                    'Kakaosmör saknar helt kolhydrater, så det glykemiska indexet är inte tillämpligt; det innehåller '
                    'mycket stearinsyra, en mättad fettsyra.'),
              faq=[dict(q='Höjer kakaosmör blodsockret?',
                        a='Nej, det höjer inte blodsockret eftersom det saknar kolhydrater.'),
                   dict(q='Är kakaosmör ätbart eller bara för hudvård?',
                        a='Rent kakaosmör av livsmedelskvalitet (food grade) är ätbart och är grundingrediensen i vit och '
                          'mörk choklad.'),
                   dict(q='Hur många kalorier finns i en matsked (10 g)?',
                        a='Den innehåller 88 kcal och 10 g rent fett, inga kolhydrater och inget protein.')]),
    574: dict(lead='Naturliga, krispiga chokladflingor utan socker och utan bearbetning: rena kakaobönor som krossats till '
                   'små bitar, med djup chokladbeska och härlig krispighet som ger frukosten en förfinad prägel. Det '
                   'glykemiska indexet är inte tillämpligt eftersom nettokolhydraterna i en portion är få.',
              tips=('Strö en matsked över havregryn, yoghurt eller fruktsallad; du får krispighet och chokladsmak utan att '
                    'blodsockret stiger.',
                    'Använd dem i stället för sötade chokladknappar (chocolate chips) i bakning, eller ät dem med mandel '
                    'som ett krispigt mellanmål.',
                    'Nettokolhydraterna i en portion (15 g) är högst 1,8 g, så det glykemiska indexet är inte tillämpligt '
                    'och den glykemiska belastningen obefintlig; kakaonibs innehåller mycket teobromin.'),
              faq=[dict(q='Kan kakaonibs hjälpa vid viktnedgång?',
                        a='De innehåller mycket fibrer och har en naturlig beska som kan minska suget efter sötsaker.'),
                   dict(q='Innehåller kakaonibs koffein?',
                        a='De innehåller mycket lite koffein; det mesta av de stimulerande ämnena utgörs av teobromin.'),
                   dict(q='Vad är näringsvärdet i 15 g (en rågad matsked)?',
                        a='Portionen innehåller 88 kcal, 2 g protein, 7,5 g fett och 2,7 g fibrer med bara 1,8 g '
                          'nettokolhydrater.')]),
    575: dict(lead='Linfrön är en rik källa till vegetabiliskt omega-3 (ALA): små gyllene eller bruna frön där malningen '
                   'frigör oljan och lignanerna, och som med vatten bildar en geléartad massa. Det glykemiska indexet är '
                   'inte tillämpligt eftersom nettokolhydraterna är nära noll.',
              tips=('Ät en matsked malda linfrön om dagen (10 g) med ett glas ljummet vatten eller med filmjölk; hela frön '
                    'passerar tarmen utan att tas upp, så nymalning är en förutsättning.',
                    'Mal bara en mängd som räcker en vecka och förvara den i en mörk glasburk i kylskåpet; omega-3-fettet '
                    'är mycket känsligt för oxidation, ljus och värme.',
                    'Linfrön innehåller slemämnen (mucilage) och ALA; ALA bidrar till att bibehålla normala '
                    'kolesterolnivåer i blodet. Den gynnsamma effekten uppnås vid ett dagligt intag på 2 g ALA. '
                    'Livsmedelsverket avråder från att äta mer än 2 matskedar krossade eller malda linfrön per dag '
                    '(cyanogena glykosider).'),
              faq=[dict(q='Varför ska linfrön malas innan man äter dem?',
                        a='Linfrönas skal är mycket hårt och kan inte brytas ned av magsaften, så fröna passerar '
                          'oförändrade utan att det värdefulla omega-3-fettet tas upp, om de inte mals.'),
                   dict(q='Hur fungerar linfrön i tarmen?',
                        a='När de äts med vatten sväller fibrerna och ökar tarminnehållets volym och mjukhet.'),
                   dict(q='Vad är näringsvärdet i en matsked (10 g)?',
                        a='Den innehåller 53 kcal, 1,8 g protein och 4,2 g fett, varav cirka 2,3 g vegetabiliskt omega-3 '
                          '(ALA), och 2,7 g fibrer med 0,2 g nettokolhydrater.')]),
    576: dict(lead='Ett naturligt alternativ till jordnötssmör för den som är allergisk mot nötter: en krämig, slät pasta '
                   'med fyllig och rostad smak som görs av 100 % solrosfrön utan tillsatt olja eller raffinerat socker. '
                   'Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 25).',
              tips=('Bred en matsked (16 g) på äppelskivor eller fullkornsrostat bröd, eller tillsätt den i morgonens '
                    'smoothie; den mättar gott och ger E-vitamin.',
                    "Välj sorter vars ingrediensförteckning bara anger 'rostade solrosfrön och en nypa havssalt', och "
                    'undvik härdade vegetabiliska oljor som tillsätts för att oljan inte ska separera.',
                    'Det glykemiska indexet är lågt (25) och den glykemiska belastningen för en matsked bara 0,4.'),
              faq=[dict(q='Är solrosfrösmör ett säkert val för barn i skolan?',
                        a='Ja, det är ett utmärkt nötfritt val (nut-free) eftersom det saknar vanliga allergener som '
                          'jordnötter och trädnötter.'),
                   dict(q='Hur mycket E-vitamin innehåller solrosfrösmör?',
                        a='En matsked innehåller cirka en fjärdedel av det dagliga behovet av E-vitamin; E-vitamin bidrar '
                          'till att skydda cellerna mot oxidativ stress.'),
                   dict(q='Vad är näringsvärdet i en matsked (16 g)?',
                        a='Den ger 99 kcal, 2,7 g protein, 8,9 g omättat fett och 1,8 g nettokolhydrater.')]),
    577: dict(lead='Smaragdgrönt smör med zink och magnesium: en mörk pasta med unik grön färg och djup jordig smak som '
                   'görs av råa pumpafrön. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 20).',
              tips=('En matsked före sänggåendet med en bit keso; pumpafrösmöret innehåller tryptofan och magnesium, och '
                    'magnesium bidrar till normal muskelfunktion.',
                    'Välj kallpressat och rått smör (inte hårt rostat) så att fettet och klorofyllet skyddas mot '
                    'oxidation.',
                    'Det glykemiska indexet är lågt (20) och den glykemiska belastningen obefintlig (0,2); smöret '
                    'innehåller mycket zink.'),
              faq=[dict(q='Vad innehåller pumpafrösmör?',
                        a='Det innehåller koncentrerat zink och växtsteroler.'),
                   dict(q='Innehåller pumpafrösmör tryptofan?',
                        a='Ja, det innehåller aminosyran tryptofan och magnesium.'),
                   dict(q='Vad är näringsvärdet i en matsked (16 g)?',
                        a='Den innehåller 93 kcal, 4,5 g protein, 7,7 g fett och bara 0,9 g nettokolhydrater.')]),
    578: dict(lead='Den gyllene oljan som i Levanten och Egypten kallas ”den heta oljan”: en ren olja som kallpressas av '
                   'linfrön och hör till de oljor som innehåller mest alfa-linolensyra (ALA), vegetabiliskt omega-3. Det '
                   'glykemiska indexet är inte tillämpligt eftersom oljan saknar kolhydrater.',
              tips=('Ringla en matsked över varma bondbönor (ful medames), hummus eller sallad; laga inte mat med den och '
                    'värm den aldrig, eftersom stekvärme förstör omega-3-fettet och omvandlar det till skadliga '
                    'föreningar.',
                    'Förvara den i en mycket mörk flaska i kylskåpsdörren och använd den inom en månad efter öppning; '
                    'smaken är frisk och mycket lätt bitter, och om den blir skarpt bitter har den oxiderat.',
                    'Linfröolja saknar kolhydrater och innehåller mycket ALA; ALA bidrar till att bibehålla normala '
                    'kolesterolnivåer i blodet. Den gynnsamma effekten uppnås vid ett dagligt intag på 2 g ALA.'),
              faq=[dict(q='Får man värma linfröolja eller laga mat med den?',
                        a='Nej, absolut inte; rökpunkten är mycket låg och omega-3-bindningarna bryts ned och oxiderar av '
                          'värme, så den ska bara användas kall.'),
                   dict(q='Kan linfröolja ersätta fiskolja?',
                        a='Den ger vegetabiliskt omega-3 (ALA), som kroppen i begränsad grad omvandlar till EPA och DHA, '
                          'och den är ett bra val för vegetarianer.'),
                   dict(q='Hur många kalorier finns i en matsked (10 g)?',
                        a='Den innehåller 88 kcal och 10 g fett (varav cirka 5,3 g vegetabiliskt omega-3) och inga '
                          'kolhydrater.')]),
    579: dict(lead='Svartkumminolja är en mörk olja med skarp och värmande smak som kallpressas av svartkumminfrön '
                   '(Nigella sativa) och innehåller ämnet tymokinon. Det glykemiska indexet är inte tillämpligt eftersom '
                   'den saknar stärkelse.',
              tips=('Ta en tesked (5 ml) på morgonen blandad med en tesked naturlig honung eller med citronsaft för att '
                    'mildra den skarpa smaken i halsen.',
                    'Se till att den är kallpressad (cold-pressed) och oraffinerad, och förvara den skyddad från köksvärme '
                    'och direkt solljus.',
                    'Den som tar diabetesläkemedel eller blodförtunnande läkemedel ska rådfråga sin läkare innan den '
                    'används, eftersom den kan förstärka läkemedlens effekt.'),
              faq=[dict(q='Vad innehåller svartkumminolja?',
                        a='Den innehåller tymokinon och fett.'),
                   dict(q='Vad är tymokinon?',
                        a='Tymokinon är det mest kända aktiva ämnet i svartkumminfrön.'),
                   dict(q='Vilken mängd är rimlig per dag?',
                        a='En tesked (5 g = 44 kcal) räcker; ta inte för mycket, för att undvika belastning på levern '
                          'eller kraftigt blodtrycksfall.')]),
    580: dict(lead='Ett traditionellt kosttillskott i Skandinavien: en ren olja som utvinns ur levern från vild arktisk '
                   'torsk och som i en sked förenar marint omega-3 (EPA och DHA) med en hög naturlig dos D3-vitamin och '
                   'A-vitamin. Det glykemiska indexet är inte tillämpligt eftersom den saknar kolhydrater.',
              tips=('Ta en tesked (5 ml) till lunch eller frukost; fettet i måltiden förbättrar upptaget av de fettlösliga '
                    'D- och A-vitaminerna.',
                    'Välj molekylärt renade sorter utan kvicksilver och tungmetaller, gärna med naturlig smak som citron '
                    'för att dölja fisksmaken, och förvara alltid flaskan i kylskåp efter öppning.',
                    'EPA och DHA bidrar till hjärtats normala funktion (vid ett dagligt intag på 250 mg), och D-vitamin '
                    'bidrar till immunsystemets normala funktion. Till gravida: överskrid inte den rekommenderade dosen '
                    'och rådfråga din läkare, eftersom höga doser A-vitamin kan skada fostret.'),
              faq=[dict(q='Vad är skillnaden mellan levertran och vanlig fiskolja (fish oil)?',
                        a='Vanlig fiskolja utvinns ur fiskköttet och innehåller bara omega-3, medan levertran utvinns ur '
                          'levern och utöver omega-3 innehåller koncentrerat naturligt D3- och A-vitamin.'),
                   dict(q='Vad bidrar D-vitaminet och DHA i levertran med?',
                        a='D-vitamin bidrar till att bibehålla normal benstomme, och DHA bidrar till att bibehålla normal '
                          'hjärnfunktion (vid ett dagligt intag på 250 mg DHA).'),
                   dict(q='Vad är näringsvärdet i en tesked (5 g)?',
                        a='Den innehåller 45 kcal och 5 g fett, varav cirka 1 g omega-3 (EPA och DHA), och täcker det '
                          'mesta eller hela det dagliga behovet av D3-vitamin beroende på produkt.')]),
    581: dict(lead='Hjortron är Arktis sällsynta guld och de orörda skandinaviska skogarnas frukt: glittrande '
                   'bärnstensfärgade bär som liknar hallon men har en varm gyllene färg och en syrlig smak som blandar '
                   'aprikos och honung; de växer var för sig på kalla myrar och är en dyr delikatess. Det glykemiska '
                   'indexet är inte tillämpligt eftersom nettokolhydraterna är få.',
              tips=('Njut av dem färska eller med yoghurt och nötter, eller som en varm sås utan socker över grillad ost '
                    'som man gör i Lappland.',
                    'Ät dem helst färska eller frysta utan lång kokning, så att ellagsyran och det värmekänsliga '
                    'C-vitaminet bevaras.',
                    'Nettokolhydraterna är högst 2,7 g per 100 g, så det glykemiska indexet är inte tillämpligt och den '
                    'glykemiska belastningen försumbar; bären innehåller ellagsyra och polyfenoler.'),
              faq=[dict(q='Varför kallas hjortron för Arktis guld?',
                        a='Därför att de inte odlas kommersiellt utan plockas för hand med stor möda på kalla arktiska '
                          'myrar, och varje planta ger bara ett enda bär.'),
                   dict(q='Vad innehåller hjortron?',
                        a='De innehåller mycket polyfenoler och naturlig bensoesyra.'),
                   dict(q='Vad är näringsvärdet i 100 g hjortron?',
                        a='De innehåller 51 kcal, 1,3 g protein, hela 6,3 g fibrer och bara 2,7 g nettokolhydrater.')]),
    582: dict(lead='Havtornsbär är små, starkt orange bär som växer på taggiga buskar längs kusterna, med kraftig, frisk '
                   'syra och en unik orange olja i fruktköttet; havtorn hör till de få växter som innehåller omega-7. Det '
                   'glykemiska indexet är inte tillämpligt eftersom nettokolhydraterna nästan saknas.',
              tips=('Syran är mycket kraftig; pressa en näve med morotsjuice eller mixa i en smoothie, eller ta en sked '
                    'osötad koncentrerad juice utspädd med vatten.',
                    'Drick den som färsk, kall juice utan värmepastörisering så att det sällsynta omega-7-fettet och '
                    'C-vitaminet bevaras.',
                    'Nettokolhydraterna nästan saknas, så det glykemiska indexet är inte tillämpligt och den glykemiska '
                    'belastningen försumbar; bären innehåller omega-7 (palmitoleinsyra).'),
              faq=[dict(q='Vad är omega-7 i havtorn?',
                        a='Omega-7 är palmitoleinsyra, en enkelomättad fettsyra som finns i havtornsbärens fruktkött.'),
                   dict(q='Hur mycket C-vitamin innehåller havtorn jämfört med citron och apelsin?',
                        a='Havtorn innehåller många gånger mer C-vitamin än citron och apelsin; C-vitamin bidrar till '
                          'immunsystemets normala funktion.'),
                   dict(q='Vad är näringsvärdet i 50 g?',
                        a='Portionen ger 41 kcal, 2,6 g vegetabiliskt fett och bara cirka 0,8 g nettokolhydrater.')]),
    583: dict(lead='Fläderbär är glänsande svarta bär som växer i hängande klasar och som i europeisk folktradition är '
                   'kända som en vintersaft. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 30).',
              tips=('Ät dem alltid som kokt och silad saft, eller som hemgjord sylt med ett sötningsmedel; en matsked om '
                    'dagen under vintern.',
                    'Viktig klinisk varning: fläderbär får aldrig ätas råa; råa bär, blad och stjälkar innehåller '
                    'cyanogena glykosider som ger illamående, kräkningar och förgiftning, och ordentlig upphettning bryter '
                    'ned ämnena och gör bären säkra.',
                    'Det glykemiska indexet är lågt (30) och den glykemiska belastningen för 50 g bara 1,7; bären '
                    'innehåller mycket antocyaniner.'),
              faq=[dict(q='Vad innehåller fläderbär?',
                        a='De innehåller mycket antocyaniner och fibrer.'),
                   dict(q='Är fläderbär ett säkert val vid diabetes?',
                        a='Kokta bär i sig innehåller lite socker och är ett säkert val, men var försiktig med kommersiell '
                          'fläderbärssaft som är full av glukossirap och tillsatt socker.'),
                   dict(q='Vad är näringsvärdet i 50 g kokta bär utan socker?',
                        a='Portionen ger 36 kcal, 3,5 g fibrer och bara 5,7 g nettokolhydrater.')]),
    584: dict(lead='Kvitten är höstens doftande gyllene frukt med anrikt damascenskt och turkiskt ursprung: en hård frukt '
                   'som vid varsam pochering blir mjuka bärnstens- och rosafärgade bitar med doft av kryddnejlika och '
                   'kanelens värme, till en mild vinterdessert. Det glykemiska indexet är lågt (en kliniskt granskad '
                   'uppskattning, 35).',
              tips=('Ett bra alternativ till mäktiga orientaliska sötsaker; ät det varmt efter lunch eller med en sked '
                    'grädde eller grekisk yoghurt och krossade valnötter.',
                    'Pochera det i vatten kryddat med kanelstänger, stjärnanis och kryddnejlika utan socker; kanelen ger '
                    'en känsla av naturlig sötma, och nöj dig med en liten sked honung om du vill.',
                    'Det glykemiska indexet är lågt (35) och den glykemiska belastningen för 150 g låg (7,0); kvitten '
                    'innehåller pektinfibrer.'),
              faq=[dict(q='Höjer pocherat kvitten HbA1c?',
                        a='Kvitten innehåller mycket pektin och fibrer och höjer inte blodsockret nämnvärt, så länge det '
                          'inte kokas i sockerlag.'),
                   dict(q='Vad innehåller kvitten?',
                        a='Kvitten innehåller pektin och sammandragande garvämnen.'),
                   dict(q='Vad är näringsvärdet i 150 g kvitten pocherat med kanel?',
                        a='Portionen ger 85 kcal, 2,9 g fibrer och 20 g naturliga kolhydrater som smälts långsamt.')]),
    585: dict(lead='Mörka bergsaprikoser som torkats i ren sol: naturligt torkade utan tillsatt svaveldioxid, så att de '
                   'behåller sin mörkt jordbruna färg och äkta karamell- och honungssmak med mycket kalium. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 30).',
              tips=('Ät 3 till 4 aprikoser (40 g) före träning eller med valnötter som ett mellanmål.',
                    'Välj bruna torkade aprikoser och undvik de starkt orange; den orange färgen visar att svavel '
                    '(sulfiter) har använts, som kan ge allergi och astmaanfall hos känsliga personer.',
                    'Det glykemiska indexet är lågt (30) och den glykemiska belastningen för 40 g är 6,7; aprikoserna '
                    'innehåller mycket kalium, och kalium bidrar till att bibehålla ett normalt blodtryck.'),
              faq=[dict(q='Varför har naturligt torkade aprikoser en mörkbrun färg?',
                        a='Därför att fruktsockret karamelliseras naturligt i solens värme utan svavel som bevarar färgen, '
                          'och den bruna färgen är ett tecken på naturlig torkning.'),
                   dict(q='Vad innehåller torkade aprikoser?',
                        a='De innehåller cellulosafibrer och sorbitol samt vegetabiliskt järn och A-vitamin.'),
                   dict(q='Vad är näringsvärdet i 40 g (cirka 4 aprikoser)?',
                        a='Portionen ger 96 kcal, 1,4 g protein, 2,9 g fibrer och 22,3 g naturliga kolhydrater.')]),
    586: dict(lead='Svarta mullbär är Levantens lyxiga sommarfrukt: mörka bär fulla av förtrollande karmosinröd saft som '
                   'blandar sötma med frisk syra. Det glykemiska indexet är lågt (en kliniskt granskad uppskattning, 25).',
              tips=('Ät dem färska under säsongen som ett fräscht mellanmål ensamma eller med yoghurt och nötter; den '
                    'djupröda färgen som fastnar på fingrarna kommer från antocyaninerna.',
                    'Skölj dem mycket varsamt i kallt vatten och ät dem färska direkt; koka dem inte och tillsätt inget '
                    'socker, så bevaras C-vitaminet och flavonoiderna.',
                    'Det glykemiska indexet är lågt (25) och den glykemiska belastningen för 100 g bara 2,0; bären '
                    'innehåller mycket antocyaniner.'),
              faq=[dict(q='Höjer svarta mullbär blodsockret?',
                        a='Nej, det glykemiska indexet är lågt (25) och sockret tas upp långsamt, vilket gör dem till ett '
                          'bra fruktval vid diabetes.'),
                   dict(q='Vad innehåller svarta mullbär?',
                        a='De innehåller antocyaniner, flavonoider och C-vitamin.'),
                   dict(q='Vad är näringsvärdet i 100 g färska mullbär?',
                        a='Portionen ger 43 kcal, 1,4 g protein, 1,7 g fibrer och bara 8,1 g nettokolhydrater.')]),
    587: dict(lead='Naturens krispiga godis och ett alternativ till russin och sötsaker: vita mullbär som torkats '
                   'naturligt till en ljus bärnstensfärg, med smak av karamell och honung och lätt krispighet. Det '
                   'glykemiska indexet är lågt (en kliniskt granskad uppskattning, 35).',
              tips=('En liten näve (30 g) till kaffet eller teet i stället för sötsaker, eller blandade med råa nötter och '
                    'havregryn.',
                    'Välj naturligt torkade bär utan tillsatt sockerlag eller svavel; konsistensen ska vara elastisk och '
                    'måttligt krispig, inte stenhård.',
                    'Det glykemiska indexet är lågt (35) och den glykemiska belastningen för 30 g är 6,6; bären innehåller '
                    'växtämnet DNJ.'),
              faq=[dict(q='Vad är DNJ i vita mullbär?',
                        a='DNJ (1-deoxynojirimycin) är ett naturligt växtämne som finns i mullbär.'),
                   dict(q='Passar torkade vita mullbär vid viktnedgång?',
                        a='De ger naturlig sötma i stället för raffinerat socker, men de är torkad frukt med koncentrerade '
                          'kalorier, så nöj dig med en liten näve om dagen.'),
                   dict(q='Vad är näringsvärdet i 30 g?',
                        a='Portionen innehåller cirka 96 kcal, 3 g vegetabiliskt protein, 3,6 g fibrer och 18,9 g '
                          'nettokolhydrater.')]),
    588: dict(lead='Vinterns doft och de kalla kvällarnas värme: sötkastanjer skiljer sig helt från andra nötter, med en '
                   'stärkelserik, krämig konsistens som påminner om sötpotatis och en karamelliserad smak från kolelden. '
                   'Det glykemiska indexet är medelhögt (en kliniskt granskad uppskattning, 60).',
              tips=('Ät en portion med cirka 8 varma rostade kastanjer (80 g) som eftermiddagsmål eller före träning; de '
                    'mättar länge.',
                    'Skär ett kryss i skalet före rostningen så att de inte spricker, och rosta dem i ugn eller airfryer '
                    'tills skalet blir krispigt och lätt att skala utan att kärnan bränns.',
                    'Det glykemiska indexet är medelhögt (60) och den glykemiska belastningen för 80 g (cirka 8 kastanjer) '
                    'är 17,7; till skillnad från valnötter och mandel innehåller de mycket stärkelse och lite fett, så de '
                    'räknas som stärkelse vid diabetes.'),
              faq=[dict(q='Är kastanjer nötter eller stärkelse?',
                        a='Näringsmässigt räknas kastanjer mer som stärkelse än som feta nötter; de innehåller mycket lite '
                          'fett och mycket komplex stärkelse och C-vitamin.'),
                   dict(q='Gör rostade kastanjer att man går upp i vikt?',
                        a='80 g innehåller cirka 170 kcal och är ett mättande mellanmål, men stora mängder ökar det '
                          'dagliga stärkelseintaget.'),
                   dict(q='Vad är näringsvärdet i 80 g rostade kastanjer?',
                        a='Portionen ger 170 kcal, 2 g protein, mindre än 2 g fett och 29,5 g nettokolhydrater med 6,5 g '
                          'fibrer.')]),
    589: dict(lead='Pinjenötter är aristokraten på det levantinska bordet: små elfenbensvita frön som med möda samlas från '
                   'pinjeträdens kottar, med smörig, fet smak och en konsistens som smälter i munnen. Det glykemiska '
                   'indexet är lågt (en kliniskt granskad uppskattning, 15).',
              tips=('Strö en matsked (15 g) råa eller lätt rostade pinjenötter över fatteh, hummus eller ruccolasallad, '
                    'eller använd dem som huvudingrediens i italiensk pesto.',
                    'Rosta dem på mycket låg värme utan olja i bara två minuter; pinjenötternas egen olja räcker för att '
                    'ge dem färg, och hög värme bränner dem snabbt.',
                    'Det glykemiska indexet är lågt (15) och den glykemiska belastningen nästan obefintlig (0,2); de '
                    'innehåller den unika pinolensyran.'),
              faq=[dict(q='Vad är pinolensyra?',
                        a='Pinolensyra (pinolenic acid) är en fettsyra som är karaktäristisk för pinjenötter.'),
                   dict(q='Vad innehåller pinjenötter för fett och mineraler?',
                        a='De innehåller mycket enkelomättat fett, magnesium och E-vitamin.'),
                   dict(q='Vad är näringsvärdet i en matsked (15 g)?',
                        a='Den ger 101 kcal, 2 g protein, 10,2 g fett och bara 1,4 g nettokolhydrater.')]),
    590: dict(lead='Svarta sesamfrön är små koksvarta, oskalade frön som innehåller mer polyfenoler och mineraler än '
                   'skalade vita sesamfrön och ger rätter och bröd en ren, rostad och nötig smak. Det glykemiska indexet '
                   'är lågt (en kliniskt granskad uppskattning, 25).',
              tips=('Strö en matsked (10 g) över sallader, nudlar, ägg eller havregryn; tugga dem väl eller krossa dem '
                    'lätt så att kalciumet och mineralerna i skalet frigörs.',
                    'Lätt rostning i en torr panna i en minut väcker de aromatiska oljorna och sesaminet och gör fröna '
                    'lättare att smälta.',
                    'Det glykemiska indexet är lågt (25) och den glykemiska belastningen obefintlig (0,3); fröna hör till '
                    'de vegetabiliska livsmedel som innehåller mest kalcium, järn och zink.'),
              faq=[dict(q='Vad är skillnaden mellan svarta och vita sesamfrön?',
                        a='Svarta sesamfrön behåller hela sitt naturliga skal och innehåller därför betydligt mer kalcium, '
                          'fibrer och polyfenoler än skalade vita sesamfrön.'),
                   dict(q='Vad innehåller svarta sesamfrön mer?',
                        a='De innehåller koppar, järn och fettsyror.'),
                   dict(q='Vad är näringsvärdet i en matsked (10 g)?',
                        a='Den ger 57 kcal, 1,8 g protein, 5 g fett och 1,2 g nettokolhydrater med 1,2 g fibrer.')]),
    591: dict(lead='Kombucha är en naturligt bubblande dryck: svart och grönt te som fermenterats av en levande kultur av '
                   'bakterier och jäst (SCOBY), vilket ger ett syrligt, lätt sött och kolsyrat te som ett alternativ till '
                   'läsk.',
              tips=('Börja med ett halvt glas (120 ml) om dagen till lunch tills magen har vant sig, och drick sedan gärna '
                    'ett helt glas (250 ml).',
                    'Drick den kyld, och välj råa opastöriserade sorter (raw unpasteurized) om du vill ha levande '
                    'bakterier; undvik sorter med socker eller konstgjorda aromer som tillsatts efter fermenteringen.',
                    'Bakterierna förbrukar en stor del av sockret under fermenteringen och bildar organiska syror, så det '
                    'glykemiska indexet är inte tillämpligt, men ett glas (250 ml) innehåller fortfarande cirka 11 g '
                    'socker som ska räknas in vid diabetes.'),
              faq=[dict(q='Innehåller kombucha alkohol eller socker?',
                        a='Fermenteringen lämnar kvar socker (cirka 11 g per glas) och spår av alkohol (mindre än 0,5 %), '
                          'och den är ett lättare alternativ till läsk, som innehåller mer än dubbelt så mycket socker.'),
                   dict(q='Vad innehåller kombucha?',
                        a='Den innehåller ättiksyra, glukonsyra och levande bakterier.'),
                   dict(q='Vad är näringsvärdet i ett glas (250 ml)?',
                        a='Glaset ger cirka 45 kcal, inget fett och cirka 11 g kolhydrater från det naturliga socker som '
                          'finns kvar.')]),
    592: dict(lead='Vattenkefir är en fräsch fermenterad dryck helt utan mjölk och laktos: kristallklara geléartade korn '
                   'som lever på en lag av torkade fikon och citron och bildar ett bubblande vatten med frisk smak och '
                   'miljontals levande bakterier.',
              tips=('Ett bra modernt alternativ till sötade juicer och läsk för barn och vuxna; drick den kall sommartid '
                    'efter måltiderna.',
                    'Om du gör den hemma, låt den fermentera i 48 timmar tills kefirkornen har förbrukat det mesta av '
                    'sockret och bildat naturlig kolsyra och en frisk syrlig smak.',
                    'Det glykemiska indexet är inte tillämpligt eftersom det mesta av sockret förbrukas under '
                    'fermenteringen, men ett glas (250 ml) innehåller cirka 9,5 g socker; den passar den som är allergisk '
                    'mot mjölkprotein eller inte tål laktos.'),
              faq=[dict(q='Vad är skillnaden mellan vattenkefir och mjölkkefir?',
                        a='Mjölkkefir bygger på fermenterad mjölk och innehåller kasein och protein, medan vattenkefir '
                          'bygger på vatten och frukt, är helt vegansk och mycket lätt.'),
                   dict(q='Passar den vid diabetes?',
                        a='Ja, med måtta, eftersom bakterierna förbrukar det mesta av sockret och omvandlar det till '
                          'syror; men ett helt glas innehåller fortfarande cirka 9,5 g socker som ska räknas in.'),
                   dict(q='Vad är näringsvärdet i ett glas (250 ml)?',
                        a='Det innehåller bara cirka 38 kcal, inget fett och cirka 9,5 g nettokolhydrater.')]),
    593: dict(lead='Rooiboste är den rubinröda, varma drycken från Cederbergsbergen i Sydafrika: tunna, nålformade blad '
                   'som fermenteras naturligt och ger ett te med lätt honungs- och jordig sötma. Det är naturligt '
                   'koffeinfritt, och det glykemiska indexet är inte tillämpligt eftersom det saknar kolhydrater.',
              tips=('En varm kopp på kvällen före sänggåendet; rooibos saknar koffein och kan drickas hela dagen av både '
                    'vuxna och barn.',
                    'Låt det dra i kokande vatten i 5 till 7 minuter; bladen tål lång dragning utan att bli skarpt beska '
                    'eftersom de innehåller lite sammandragande garvämnen.',
                    'Rooibos saknar helt kalorier och stärkelse, så det glykemiska indexet är inte tillämpligt; teet '
                    'innehåller ämnet aspalatin (aspalathin).'),
              faq=[dict(q='Hämmar rooiboste järnupptaget som vanligt te?',
                        a='Den stora fördelen är att det innehåller mycket lite garvämnen och oxalat, så det påverkar inte '
                          'upptaget av järn eller kalcium nämnvärt.'),
                   dict(q='Innehåller rooibos något koffein?',
                        a='Det är naturligt 100 % koffeinfritt (inte kemiskt koffeinfritt), vilket gör det till en bra '
                          'dryck före sänggåendet.'),
                   dict(q='Vad är näringsvärdet i en kopp (250 ml) utan socker?',
                        a='Den innehåller bara cirka 2 kcal, ingen stärkelse och inget fett, samt polyfenoler.')]),
    594: dict(lead='Jasminte är en av de finaste teceremonierna i kinesisk tradition: unga gröna teblad från våren som '
                   'förvaras och doftsätts nattetid över färska jasminblommor så att de tar upp den rika doften. Det '
                   'glykemiska indexet är inte tillämpligt eftersom teet saknar kolhydrater.',
              tips=('Drick det på morgonen eller mitt på dagen; teet innehåller naturligt koffein och aminosyran L-teanin.',
                    'Använd vatten på 80 °C (inte kokande) och låt teet dra i bara två till tre minuter, så undviker du '
                    'beska och bevarar de aromatiska oljorna.',
                    'Jasminte saknar stärkelse och socker, så det glykemiska indexet är inte tillämpligt; tebladen '
                    'innehåller katekiner (EGCG).'),
              faq=[dict(q='Vad ger jasminteet dess doft?',
                        a='Doften kommer från jasminblommornas aromatiska ämnen, bland annat linalool.'),
                   dict(q='Vad är EGCG i grönt te?',
                        a='EGCG är den vanligaste katekinen i grönt te.'),
                   dict(q='Vad är näringsvärdet i en kopp (250 ml)?',
                        a='Kalorierna är nära noll (mindre än 3 kcal), och teet saknar fett och stärkelse.')]),
    595: dict(lead='Earl Grey är världens mest kända aristokratiska engelska te: fint svart te från Ceylon eller Indien '
                   'blandat med eterisk olja som pressats ur skalet på italiensk bergamott, med en frisk citrusdoft som '
                   'väcker sinnena. Det glykemiska indexet är inte tillämpligt eftersom teet saknar kolhydrater.',
              tips=('En utmärkt morgondryck; drick det varmt med en tunn citronskiva eller några droppar vegetabilisk '
                    'dryck.',
                    'Låt det dra i kokande vatten (100 °C) i 3 till 4 minuter; välj sorter som doftsatts med ren naturlig '
                    'bergamottolja och undvik billiga konstgjorda aromer.',
                    'Teet saknar kalorier och stärkelse, så det glykemiska indexet är inte tillämpligt; bergamott '
                    'innehåller flavonoider, men mängden i en kopp te är mycket liten.'),
              faq=[dict(q='Vad är bergamott i Earl Grey?',
                        a='Bergamott är en aromatisk citrusfrukt som odlas i södra Italien och som innehåller flavanoner.'),
                   dict(q='Vad är Earl Grey för slags te?',
                        a='Det är svart te smaksatt med olja från bergamottens skal.'),
                   dict(q='Vad är näringsvärdet i en kopp (250 ml) utan socker?',
                        a='Cirka 2 kcal, inget fett och ingen stärkelse.')]),
    596: dict(lead='Oolong är en pärla från provinsen Fujian och det kända Tieguanyin-teet: ett te i ett förtrollande '
                   'mellanläge mellan friskt grönt te och djupt svart te, som genomgår en noggrann delvis oxidation som '
                   'ger en komplex blommig och fruktig smak. Det glykemiska indexet är inte tillämpligt eftersom teet '
                   'saknar kolhydrater.',
              tips=('Drick en varm kopp 30 minuter efter en mäktig måltid; i kinesisk tradition är oolong känt som en '
                    'dryck efter fet mat.',
                    'Låt det dra i vatten på 90 °C; det fantastiska med de rullade oolongbladen är att samma blad kan dras '
                    '3 eller 4 gånger och ge ett nytt smaklager varje gång.',
                    'Oolong saknar stärkelse och socker, så det glykemiska indexet är inte tillämpligt; teet innehåller '
                    'särskilda polymeriserade polyfenoler.'),
              faq=[dict(q='Vad är oolongte?',
                        a='Ett delvis oxiderat te mellan grönt och svart te.'),
                   dict(q='Hur mycket koffein innehåller oolong?',
                        a='Det innehåller en måttlig mängd koffein (mindre än kaffe och svart te och något mer än grönt '
                          'te).'),
                   dict(q='Vad är näringsvärdet i en kopp (250 ml)?',
                        a='Inget fett, ingen stärkelse och mindre än 3 kcal.')]),
    597: dict(lead='Rostad maskrosrot är det örtalternativ som smakar mest som fylligt kaffe: rötterna från vild maskros '
                   'rostas och mals till en mörk dryck med djup jordig smak och behaglig beska som påminner om espresso, '
                   'men helt utan koffein. Det glykemiska indexet är inte tillämpligt eftersom stärkelsen är mycket låg.',
              tips=('En varm kopp på morgonen för den som vill minska på koffeinet, eller efter middagen.',
                    'Koka en matsked krossade rötter i ett glas vatten i 5 minuter och sila; du kan tillsätta en skvätt '
                    'mandeldryck eller en nypa kanel för en naturlig latte.',
                    'Stärkelsen är mycket låg, så det glykemiska indexet är inte tillämpligt, och kalorierna är få; '
                    'rötterna innehåller den lösliga fibern inulin.'),
              faq=[dict(q='Vad innehåller maskrosrot?',
                        a='Den innehåller den lösliga fibern inulin och beska ämnen.'),
                   dict(q='Är maskrosdryck urindrivande?',
                        a='Maskros används traditionellt som urindrivande, och bladen innehåller mycket kalium; den som '
                          'tar urindrivande läkemedel eller litium ska rådfråga sin läkare först.'),
                   dict(q='Vad är näringsvärdet i en kopp (250 ml)?',
                        a='Cirka 12 kcal och cirka 2,3 g nettokolhydrater, mest inulin.')]),
    598: dict(lead='Gurkmejamjölk (golden milk) är den kända varma ayurvediska drycken: varm mjölk i solens färg med ren '
                   'gurkmeja, en nypa svartpeppar, ingefära och kanel som värmer kroppen. Det glykemiska indexet är lågt '
                   '(en kliniskt granskad uppskattning, 30).',
              tips=('Ett varmt glas en halvtimme före sänggåendet.',
                    'Den gyllene regeln: drick aldrig gurkmeja utan en nypa svartpeppar och några droppar fett (som '
                    'kokosolja); piperinet i pepparn ökar upptaget av kurkumin kraftigt (upp till 2 000 %).',
                    'Det glykemiska indexet är lågt (30) och den glykemiska belastningen för 250 ml är 3,8; drycken '
                    'innehåller kurkumin.'),
              faq=[dict(q='Varför ska man tillsätta svartpeppar och fett i gurkmejamjölk?',
                        a='Kurkumin tas naturligt upp dåligt och är fettlösligt; svartpeppar ökar upptaget ungefär '
                          'tjugofalt, och fettet hjälper det att nå blodet.'),
                   dict(q='Hur mycket kurkumin innehåller ett glas gurkmejamjölk?',
                        a='Mängden kurkumin i ett glas är betydligt mindre än de koncentrerade doser som har studerats.'),
                   dict(q='Vad är näringsvärdet i ett glas (250 ml)?',
                        a='Det innehåller cirka 163 kcal, 8 g protein, 8 g fett och 12,8 g nettokolhydrater.')]),
    599: dict(lead='Ett uppfriskande sommarvatten: rent vatten med krispiga gurkskivor, citronskivor och färska myntablad, '
                   'där varje klunk ger fräschhet och svalka. Det glykemiska indexet är inte tillämpligt eftersom drycken '
                   'nästan saknar kolhydrater.',
              tips=('Fyll en glasflaska och drick ur den under dagen och vid träning; det uppmuntrar dig att dricka mer '
                    'vatten om du inte tycker om smaken av vanligt vatten.',
                    'Krossa myntabladen varsamt med en sked så att mentololjorna frigörs, och låt ingredienserna dra i '
                    'iskallt vatten i två timmar i kylskåpet före drickandet; pressa inte citronen hårt, så blir det inte '
                    'beskt.',
                    'Kalorierna och stärkelsen är nästan obefintliga, så det glykemiska indexet är inte tillämpligt; '
                    'gurkan och citronen ger små mängder kalium och C-vitamin.'),
              faq=[dict(q='Hjälper vatten med gurka och mynta vid viktnedgång?',
                        a='Indirekt; det är ett bra alternativ till sötade juicer och läsk och gör att du dricker mer '
                          'vatten.'),
                   dict(q='Hur länge håller vattnet i kylskåpet?',
                        a='Det är bäst att dricka det inom 24 timmar, och du kan fylla på nytt vatten över samma gurk- och '
                          'myntaskivor två till tre gånger samma dag.'),
                   dict(q='Vad är näringsvärdet i ett glas (250 ml)?',
                        a='Det innehåller bara cirka 7 kcal och cirka 1,3 g nettokolhydrater.')]),
    600: dict(lead='Apelsinblomsvatten är Orientens doft i levantinska och nordafrikanska rätter: en ren, klar vätska som '
                   'ångdestilleras ur blommorna från pomeransträdet (bitter apelsin), med en förtrollande blommig '
                   'citrusdoft som ger drycker och sötsaker en unik smak. Det glykemiska indexet är inte tillämpligt '
                   'eftersom det saknar kolhydrater.',
              tips=('Tillsätt en matsked (15 ml) i en kopp varmt vatten och drick efter mäktiga måltider som ”vitt kaffe”, '
                    'eller använd det som naturlig arom i sötsaker.',
                    'Välj 100 % rent destillerat apelsinblomsvatten utan kemiska aromer eller alkohol; några droppar '
                    'räcker för en kraftig smak.',
                    'Det saknar helt kalorier, stärkelse och socker, så det glykemiska indexet är inte tillämpligt.'),
              faq=[dict(q='Vad är libanesiskt ”vitt kaffe”?',
                        a='En folklig varm dryck som görs genom att blanda en matsked destillerat apelsinblomsvatten i en '
                          'kopp kokande vatten, ibland med en nypa kardemumma eller kanel, och som dricks efter maten.'),
                   dict(q='Vad innehåller apelsinblomsvatten?',
                        a='Det innehåller flyktiga aromatiska oljor från pomeransblommorna.'),
                   dict(q='Vad är näringsvärdet i en matsked (15 ml)?',
                        a='Inga kalorier, inget fett och inga kolhydrater; bara ren arom.')]),
}
