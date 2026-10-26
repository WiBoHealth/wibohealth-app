"""Swedish copy for the static supplement pages (/sv/supplements/<slug>.html), read by generate_supplement_pages.py.

Every text is a translation of the medically approved copy in js/supplements-data.js (the English fields, checked
against the Arabic), in the wording of Swedish pharmacies and of 1177 / Livsmedelsverket / Läkemedelsverket; EFSA
health claims follow the official Swedish wording of the EU register. Nothing is written from scratch. Approved by
Dr. Wassim Habib (2026-10-26): the 50 names below, Swedish number style (1 000, IE, µg) and, where the Arabic and the
English natural sources differ, the English list.

PUBLISH lists the supplements that get a Swedish page (batches of 50, each approved by Dr. Wassim Habib first).
"""

# the Swedish copy as approved for publication: the "uppdaterades senast" date, lastReviewed and the sitemap lastmod
REVIEWED = '2026-10-26'
REVIEWED_TXT = '26 oktober 2026'

NB = ' '   # thousands separator (1 000) and number + unit, so a value never breaks across lines

# approved Swedish names, in the data order of js/supplements-data.js (first batch 1-50, second batch 51-100)
NAMES = {
    'whey-protein': 'Vassleprotein (whey)',
    'casein-protein': 'Kaseinprotein',
    'creatine-monohydrate': 'Kreatinmonohydrat',
    'bcaa': 'BCAA (grenade aminosyror)',
    'beta-alanine': 'Beta-alanin',
    'multivitamins': 'Multivitamin',
    'omega-3-fish-oil': 'Omega-3 (fiskolja)',
    'vitamin-d3': 'D-vitamin (D3, kolekalciferol)',
    'magnesium': 'Magnesium (glycinat/citrat)',
    'zinc': 'Zink (kelaterat/pikolinat)',
    'green-tea-extract': 'Grönt te-extrakt (EGCG)',
    'cla': 'CLA (konjugerad linolsyra)',
    'l-carnitine': 'L-karnitin',
    'melatonin': 'Melatonin',
    'ashwagandha': 'Ashwagandha (KSM-66)',
    '5-htp': '5-HTP',
    'caffeine': 'Koffein (vattenfritt)',
    'pre-workout': 'Pre-workout',
    'glucosamine-chondroitin': 'Glukosamin och kondroitin',
    'collagen-peptides': 'Kollagenpeptider (hydrolyserat kollagen)',
    'l-citrulline': 'L-citrullin (citrullinmalat 2:1)',
    'taurine': 'Taurin',
    'coenzyme-q10': 'Q10 (koenzym Q10)',
    'l-theanine': 'L-teanin',
    'rhodiola-rosea': 'Rosenrot (Rhodiola rosea)',
    'ginkgo-biloba': 'Ginkgo biloba-extrakt',
    'lions-mane': "Igelkottstaggsvamp (Lion's Mane)",
    'hmb': 'HMB',
    'l-glutamine': 'L-glutamin',
    'l-arginine': 'L-arginin',
    'vitamin-c': 'C-vitamin (askorbinsyra)',
    'vitamin-b-complex': 'B-vitaminkomplex',
    'iron': 'Järn (järnbisglycinat)',
    'calcium': 'Kalcium (citrat/karbonat)',
    'probiotics': 'Mjölksyrabakterier (probiotika, flera stammar)',
    'turmeric-curcumin': f'Gurkmeja – kurkumin 95{NB}% med piperin',
    'ginger': 'Ingefära (rotextrakt)',
    'spirulina': 'Spirulina (ekologisk)',
    'garcinia-cambogia': 'Garcinia cambogia (HCA)',
    'forskolin': 'Forskolin (Coleus forskohlii)',
    'eaa': 'EAA (essentiella aminosyror)',
    'l-leucine': 'L-leucin',
    'lclt': 'L-karnitin-L-tartrat (LCLT)',
    'betaine-tmg': 'Betain (TMG, trimetylglycin)',
    'epicatechin': 'Epikatekin (kakaoextrakt)',
    'phosphatidylserine': 'Fosfatidylserin (PS)',
    'sodium-bicarbonate': 'Natriumbikarbonat',
    'beetroot-nitrates': 'Rödbetsextrakt (nitrat)',
    'alpha-gpc': 'Alfa-GPC',
    'bacopa-monnieri': 'Bacopa monnieri (Brahmi)',
    # second batch (51-100 in the data order), approved 2026-10-26
    'milk-thistle': 'Mariatistel (silymarin)',
    'fenugreek': 'Bockhornsklöver (fröextrakt)',
    'tribulus-terrestris': 'Tribulus terrestris-extrakt',
    'saw-palmetto': 'Sågpalmetto (bärextrakt)',
    'maca-root-extract': 'Maca (rotextrakt 4:1)',
    'vitamin-e': 'E-vitamin (blandade tokoferoler och tokotrienoler)',
    'vitamin-k2': 'K2-vitamin (MK-7)',
    'selenium': 'Selen (L-selenometionin)',
    'chromium-picolinate': 'Krompikolinat',
    'iodine': 'Jod (kelp/kaliumjodid)',
    'nac': 'NAC (N-acetylcystein)',
    'msm': 'MSM (metylsulfonylmetan)',
    'quercetin': 'Kvercetin (fytosom med C-vitamin)',
    'resveratrol': 'Trans-resveratrol',
    'berberine': 'Berberin (berberin-HCl)',
    'pqq': 'PQQ (pyrrolokinolinkinon)',
    'alpha-lipoic-acid': 'R-alfaliponsyra (R-ALA)',
    'boron': 'Bor (glycinat/citrat)',
    'pycnogenol': 'Pycnogenol (tallbarksextrakt)',
    'lutein-zeaxanthin': 'Lutein och zeaxantin',
    'moringa': 'Moringa (ekologiskt bladpulver)',
    'cordyceps': 'Cordyceps (ekologisk)',
    'reishi-mushroom': 'Reishi (lackticka)',
    'holy-basil-tulsi': 'Helig basilika (tulsi)',
    'astaxanthin': 'Astaxantin (naturlig)',
    'd-aspartic-acid': 'D-asparaginsyra (DAA)',
    'apigenin': 'Apigenin (kamomillextrakt)',
    'carnosine': 'L-karnosin',
    'l-ornithine': 'L-ornitin',
    'glycine': 'Glycin',
    'l-tryptophan': 'L-tryptofan',
    'citrulline-malate': 'Citrullinmalat 2:1',
    'choline-bitartrate': 'Kolinbitartrat',
    'phosphatidylcholine': 'Fosfatidylkolin (från solroslecitin)',
    'panax-ginseng': 'Röd koreansk ginseng (Panax ginseng)',
    'citicoline': 'Citikolin (CDP-kolin)',
    'black-seed-oil': 'Svartkumminolja (kallpressad)',
    'aged-garlic-extract': 'Lagrat vitlöksextrakt (luktfritt)',
    'ceylon-cinnamon': 'Ceylonkanel (äkta kanel)',
    'bitter-melon': 'Bittergurka (Momordica charantia)',
    'gymnema-sylvestre': 'Gymnema sylvestre-extrakt',
    'myo-inositol': 'Myo-inositol och D-chiro-inositol (40:1)',
    'white-kidney-bean': 'Vit böna-extrakt (fasolamin)',
    'glucomannan': 'Glukomannan (konjakrot)',
    'valerian-root': 'Vänderot (rotextrakt)',
    'passionflower': 'Passionsblomma (Passiflora incarnata)',
    'lemon-balm': 'Citronmeliss (bladextrakt)',
    'vitamin-a': 'A-vitamin (retinylpalmitat och betakaroten)',
    'biotin': 'Biotin (B7-vitamin)',
    'molybdenum': 'Molybden (glycinat)',
    # third batch (101-174 in the data order), 2026-10-26
    's-adenosyl-methionine': 'SAMe (S-adenosyl-L-metionin)',
    'grape-seed-extract': 'Druvkärnextrakt (95 % OPC)',
    'chlorella': 'Chlorella (sprängd cellvägg)',
    'pantothenic-acid': 'Pantotensyra (B5-vitamin)',
    'riboflavin': 'Riboflavin (B2-vitamin)',
    'thiamine': 'Tiamin (B1-vitamin) och benfotiamin',
    'niacin': 'Niacin (B3-vitamin) – nikotinamid',
    'folate': 'Folat (L-metylfolat, aktivt B9-vitamin)',
    'pyridoxine': 'B6-vitamin (pyridoxin/P5P)',
    'manganese': 'Mangan (bisglycinat)',
    'bilberry-extract': 'Blåbärsextrakt (25 % antocyaner)',
    'hawthorn-berry': 'Hagtorn (Crataegus)',
    'dandelion-root': 'Maskrosrot (Taraxacum officinale)',
    'burdock-root': 'Kardborrerot (Arctium lappa)',
    'black-elderberry': 'Fläderbärsextrakt (Sambucus nigra)',
    'cat-s-claw': 'Kattklo (Uncaria tomentosa)',
    'olive-leaf-extract': 'Olivbladsextrakt (oleuropein)',
    'echinacea': 'Röd solhatt (Echinacea purpurea)',
    'african-mango': 'Afrikansk mango (Irvingia gabonensis)',
    'horny-goat-weed': 'Sockblomma (Epimedium, ikariin)',
    'evening-primrose-oil': 'Nattljusolja (GLA)',
    'black-cohosh': 'Silverax (Cimicifuga racemosa)',
    'phosphatidic-acid': 'Fosfatidsyra (PA, Mediator®)',
    'ursolic-acid': 'Ursolsyra',
    'shilajit': 'Shilajit (renad, mumijo)',
    'dong-quai': 'Dong quai (Angelica sinensis)',
    'vitex': 'Munkpeppar (Vitex agnus-castus)',
    'wild-yam': 'Vild jams (Dioscorea villosa)',
    'ceramides': 'Fytoceramider (för huden)',
    'hyaluronic-acid': 'Hyaluronsyra (natriumhyaluronat)',
    'krill-oil': 'Krillolja (antarktisk, omega-3 i fosfolipidform)',
    'magnesium-threonate': 'Magnesium-L-treonat (Magtein®)',
    'copper': 'Koppar (glukonat/bisglycinat)',
    'plant-sterols-and-stanols': 'Växtsteroler och växtstanoler',
    'red-yeast-rice': 'Röd jästris (monakolin K under 3 mg)',
    'nattokinase': 'Nattokinas (NSK-SD®)',
    'bromelain': 'Bromelain (ananasenzym)',
    'papain': 'Papain (papayaenzym)',
    'full-spectrum-digestive-enzymes': 'Matsmältningsenzymer (bredspektrum)',
    'l-tyrosine': 'L-tyrosin',
    'vitamin-b12': 'B12-vitamin (metylkobalamin)',
    'potassium-citrate': 'Kaliumcitrat',
    'silica': 'Kisel (ortokiselsyra/åkerfräken)',
    'pumpkin-seed-oil': 'Pumpafröolja',
    'sage-extract': 'Salviaextrakt (Salvia officinalis)',
    'anise-seeds': 'Anis (Pimpinella anisum)',
    'chamomile-flowers': 'Kamomillextrakt (Matricaria chamomilla)',
    'cumin-seeds': 'Spiskumminextrakt (Cuminum cyminum)',
    'hibiscus-flower-tea': 'Hibiskusextrakt (Hibiscus sabdariffa)',
    'glutathione': 'Reducerat glutation (Setria®)',
    'artichoke-extract': 'Kronärtskocksbladsextrakt (Cynara scolymus)',
    'cranberry-extract': 'Tranbärsextrakt (36 mg PAC)',
    'nettle-leaf-root': 'Brännässla (Urtica dioica)',
    'beta-glucan': 'Betaglukan (jäst och havre)',
    'cluster-dextrin': 'Cyklisk dextrin (cluster dextrin, HBCD)',
    'electrolytes-mix': 'Elektrolyter (natrium, kalium, magnesium)',
    'tart-cherry-extract': 'Surkörsbärsextrakt (Montmorency)',
    'saffron-extract': 'Saffransextrakt (affron®/Satiereal®)',
    'betaine-hcl': 'Betain-HCl (med pepsin)',
    'slippery-elm': 'Ulmus rubra-bark (slippery elm)',
    'marshmallow-root': 'Läkemalvarot (Althaea officinalis)',
    'dgl-licorice': 'DGL-lakrits (deglycyrrhiziniserad)',
    'peppermint-oil': 'Pepparmyntsolja (enterokapslar)',
    'nicotinamide-riboside': 'Nikotinamidribosid (NR, Niagen®)',
    'banaba-leaf-extract': 'Banababladsextrakt (korosolsyra)',
    'american-ginseng': 'Amerikansk ginseng (Panax quinquefolius)',
    'flaxseed-extract': 'Linfrölignaner (SDG)',
    'mulberry-leaf-extract': 'Vitt mullbärsbladsextrakt (DNJ)',
    'green-coffee-bean-extract': 'Grönt kaffebönsextrakt (klorogensyra)',
    'capsimax': 'Capsimax® (chiliextrakt)',
    'oil-of-oregano': 'Oreganoolja (karvakrol)',
    'bee-propolis': 'Propolis',
    'wheatgrass': 'Vetegräs (ekologiskt pulver)',
    'frankincense': 'Boswellia serrata-extrakt (AKBA)',
}

# groupLabel['en'] of js/supplements-data.js -> Swedish (the groups of the first and second batch)
GROUP_LABELS = {
    'Muscle building & fitness': 'Muskeluppbyggnad och träning',
    'General health & immunity': 'Allmän hälsa och immunförsvar',
    'General & heart health': 'Allmän hälsa och hjärthälsa',
    'General health & bones': 'Allmän hälsa och skelett',
    'General health & nerves': 'Allmän hälsa och nervsystem',
    'Metabolism & weight management': 'Ämnesomsättning och viktkontroll',
    'Metabolism & fitness': 'Ämnesomsättning och träning',
    'Sleep & relaxation': 'Sömn och avslappning',
    'Stress & relaxation': 'Stress och avslappning',
    'Sleep & mood': 'Sömn och sinnesstämning',
    'Energy & focus': 'Energi och fokus',
    'Energy & fitness': 'Energi och träning',
    'Bone & joint health': 'Skelett och leder',
    'Joints & skin': 'Leder och hud',
    'Energy & sports performance': 'Energi och idrottsprestation',
    'Performance & heart health': 'Prestation och hjärthälsa',
    'Heart health & metabolism': 'Hjärthälsa och ämnesomsättning',
    'Energy & stress': 'Energi och stress',
    'Focus & memory': 'Fokus och minne',
    'Digestion & recovery': 'Matsmältning och återhämtning',
    'Energy & nervous system': 'Energi och nervsystem',
    'Blood & vitality': 'Blod och vitalitet',
    'Bones & teeth': 'Skelett och tänder',
    'Digestion & microbiome': 'Matsmältning och tarmflora',
    'Joints & antioxidants': 'Leder och antioxidanter',
    'Digestion & comfort': 'Matsmältning och magkomfort',
    'Superfoods & vitality': 'Supermat och vitalitet',
    'Sports recovery': 'Återhämtning efter träning',
    'Strength & heart health': 'Styrka och hjärthälsa',
    'Performance & circulation': 'Prestation och blodcirkulation',
    'High-intensity performance': 'Högintensiv prestation',
    'Endurance & sports performance': 'Uthållighet och idrottsprestation',
    # second batch, approved 2026-10-26
    'Liver health & antioxidants': 'Leverhälsa och antioxidanter',
    'Metabolism & hormonal balance': 'Ämnesomsättning och hormonbalans',
    'Vitality & libido': 'Vitalitet och lust',
    "Men's health & prostate": 'Mäns hälsa och prostata',
    'Energy & adaptation': 'Energi och anpassning',
    'Antioxidants & cell protection': 'Antioxidanter och cellskydd',
    'Bones & blood vessels': 'Skelett och blodkärl',
    'Thyroid & immunity': 'Sköldkörtel och immunförsvar',
    'Metabolism & blood sugar': 'Ämnesomsättning och blodsocker',
    'Thyroid & energy': 'Sköldkörtel och energi',
    'Antioxidants & respiratory': 'Antioxidanter och luftvägar',
    'Joints & connective tissue': 'Leder och bindväv',
    'Immunity & antioxidants': 'Immunförsvar och antioxidanter',
    'Heart health & healthy ageing': 'Hjärthälsa och hälsosamt åldrande',
    'Cellular energy & focus': 'Cellernas energi och fokus',
    'Antioxidants & nerves': 'Antioxidanter och nerver',
    'Circulation & antioxidants': 'Cirkulation och antioxidanter',
    'Eye health & vision': 'Ögonhälsa och syn',
    'Immunity & relaxation': 'Immunförsvar och avslappning',
    'Antioxidants & skin': 'Antioxidanter och hud',
    'Vitality & sports performance': 'Vitalitet och idrottsprestation',
    'Cell protection & healthy ageing': 'Cellskydd och hälsosamt åldrande',
    'Recovery & relaxation': 'Återhämtning och avslappning',
    'Liver health & choline': 'Leverhälsa och kolin',
    'Immunity & respiratory': 'Immunförsvar och luftvägar',
    'Heart health & circulation': 'Hjärthälsa och cirkulation',
    "Women's health & metabolism": 'Kvinnors hälsa och ämnesomsättning',
    'Vision, immunity & skin': 'Syn, immunförsvar och hud',
    'Hair, skin & energy': 'Hår, hud och energi',
    'Essential minerals': 'Essentiella mineraler',
    # third batch
    'Mood & joints': 'Sinnesstämning och leder',
    'B vitamins & energy': 'B-vitaminer och energi',
    "Women's health & skin": 'Kvinnors hälsa och hud',
    "Women's health & hormonal balance": 'Kvinnors hälsa och hormonbalans',
    'Skin & hydration': 'Hud och fukt',
    'Cholesterol & heart health': 'Kolesterol och hjärthälsa',
    'Digestive enzymes': 'Matsmältningsenzymer',
    'Hair, nails & skin': 'Hår, naglar och hud',
    'Urinary tract health': 'Urinvägarnas hälsa',
}

# page chrome (the T dict of generate_supplement_pages.py)
UI = dict(
    dir='ltr', title='{name}: dosering, nytta och interaktioner med läkemedel | WiBo Health',
    desc='{name}: {desc} Rekommenderad dos: {dose}. Varningar och interaktioner med läkemedel enligt EFSA och NIH.',
    guide='Kosttillskottsguide', role='Funktion och nytta', dose='Rekommenderad dosering och användning',
    rec='Rekommenderad dos', forms='Bästa beredningsformer', timing='Bästa tidpunkt att ta', freq='Hur ofta',
    warnings='Varningar och försiktighet', inter='Interaktioner med läkemedel', sources_food='Naturliga källor i maten',
    refs='Vetenskapliga källor', related='Relaterade kosttillskott', open_guide='Visa i kosttillskottsguiden',
    sources='📚 Publicerade källor och forskning: Europeiska myndigheten för livsmedelssäkerhet (EFSA) • National Institutes '
            'of Health (NIH – ODS) • PubMed/Cochrane-databaser',
    updated='Innehållet uppdaterades senast: {date} · Baserat på publicerade källor och forskning (EFSA / NIH / PubMed)',
    disclaimer='⚖️ Medicinsk ansvarsfriskrivning: Informationen här är endast avsedd som hälsoupplysning och kostvägledning. '
               'Den är ingen medicinsk diagnos och ersätter aldrig ett direkt samtal med din läkare eller farmaceut. Rådgör '
               'alltid med din läkare innan du börjar med ett kosttillskott, särskilt under graviditet eller amning eller om '
               'du tar läkemedel under längre tid.',
    date=REVIEWED_TXT, footer_supp='Kosttillskottsguide')

# Approved additions to a supplement's warnings on its Swedish page (Swedish legal status)
EXTRA_WARNINGS = {
    'melatonin': ['I Sverige klassificeras melatonin som ett läkemedel. Rådgör alltid med läkare eller farmaceut före användning.'],
    'nac': ['I Sverige klassificeras acetylcystein som ett läkemedel. Rådgör med läkare eller farmaceut före användning.'],
}

# slug -> the Swedish version of the record's fields (summary = benefits, as in the data)
COPY = {
    'vitamin-d3': dict(
        summary='D-vitamin bidrar till normalt upptag och normal användning av kalcium och fosfor, till att bibehålla normal '
                'benstomme och normala tänder samt till immunsystemets normala funktion (EFSA).',
        dosage=dict(recommended=f'1{NB}000–2{NB}000{NB}IE (25–50{NB}µg) per dag, eller enligt blodprov',
                    timing='Till en måltid som innehåller fett', frequency='En gång per dag'),
        warnings=[f'Den övre säkra gränsen för vuxna enligt EFSA och NIH är 4{NB}000{NB}IE per dag',
                  'Långvarigt för höga doser kan leda till förhöjd kalciumhalt i blodet och förkalkning av vävnader'],
        interactions='Tiaziddiuretika (vätskedrivande läkemedel) ökar risken för förhöjt kalcium i blodet. Ta D-vitamin med två '
                     'timmars mellanrum från fettblockerande viktminskningsläkemedel (orlistat).',
        naturalSources='Solljus, fet fisk, äggulor och berikade livsmedel.'),
    'omega-3-fish-oil': dict(
        summary='EPA och DHA bidrar till att hjärtat fungerar normalt och till att bibehålla normalt blodtryck och normala '
                'triglyceridnivåer i blodet (EFSA-godkända påståenden vid angivna doser).',
        dosage=dict(recommended=f'1{NB}000–2{NB}000{NB}mg (EPA + DHA) per dag',
                    timing='Till en huvudmåltid som innehåller nyttigt fett', frequency='En gång per dag'),
        warnings=['Kan ge rapningar med fisksmak',
                  'Välj molekylärdestillerade produkter som är fria från kvicksilver och tungmetaller och certifierade av IFOS'],
        interactions=f'Höga doser (mer än 3{NB}g per dag) kan förlänga blödningstiden. Rådgör med läkare om du tar blodförtunnande '
                     'läkemedel (warfarin, acetylsalicylsyra, klopidogrel) eller inför en operation.',
        naturalSources='Vildlax, makrill, sardiner, valnötter och linfrö.'),
    'magnesium': dict(
        summary='Magnesium bidrar till att minska trötthet och utmattning, till elektrolytbalansen, till nervsystemets normala '
                'funktion och till normal muskelfunktion (EFSA-godkända påståenden).',
        dosage=dict(recommended=f'200–250{NB}mg elementärt magnesium per dag',
                    timing='På kvällen eller före sänggåendet', frequency='En gång per dag'),
        warnings=[f'EFSA:s gräns för magnesium från kosttillskott är 250{NB}mg per dag, för att undvika lösande effekt och '
                  'osmotisk diarré',
                  'Personer med svår njursvikt ska inte ta magnesium som tillskott utan medicinsk uppföljning'],
        interactions='Ta magnesium med 2–3 timmars mellanrum från sköldkörtelläkemedel och antibiotika, och var försiktig med '
                     'blodtryckssänkande läkemedel, eftersom magnesium kan förstärka den sänkande effekten.',
        naturalSources='Pumpafrön, mandlar, mörka bladgrönsaker och mörk choklad.'),
    'ashwagandha': dict(
        summary='En traditionell adaptogen ört som enligt studier kan ha en stödjande roll när kroppen anpassar sig till '
                'vardagsstress, och för bättre sömnkvalitet och mentalt lugn.',
        dosage=dict(recommended=f'300–600{NB}mg standardiserat rotextrakt per dag',
                    timing='Till middagen eller före sänggåendet', frequency='En gång per dag'),
        warnings=['Får absolut inte användas under graviditet, eftersom den kan stimulera livmodersammandragningar',
                  'Undvik den vid aktiv autoimmun sjukdom och vid hormonkänslig prostatacancer',
                  'Begränsad i Danmark'],
        interactions='Ashwagandha kan förstärka effekten av lugnande medel och sömnmedel. Den kan stimulera sköldkörtelns '
                     'aktivitet (interaktion med levotyroxin) och påverka blodsockersänkande och blodtryckssänkande läkemedel.',
        naturalSources='Roten av Withania somnifera.'),
    'whey-protein': dict(
        summary='Protein bidrar till att öka och bibehålla muskelmassan (ett EFSA-godkänt påstående för protein). '
                'Vassleprotein tas upp snabbt och är rikt på essentiella aminosyror och leucin.',
        dosage=dict(recommended=f'20–30{NB}g', timing='Efter träning eller mellan måltiderna', frequency='1–2 gånger per dag'),
        warnings=['Undvik det vid svår komjölksallergi',
                  'Vid laktosintolerans är vassleproteinisolat att föredra',
                  'Personer med njursvikt bör hålla koll på sitt totala proteinintag'],
        interactions='Ta det med två timmars mellanrum från läkemedel mot benskörhet (bisfosfonater) och antibiotika (kinoloner '
                     'och tetracykliner), eftersom kalciumet i det minskar upptaget av dem.',
        naturalSources='Mjölk, keso, yoghurt och naturlig vassle.'),
}

# the other 45 of the first batch (written with plain spaces; sv_numbers() below sets the non-breaking ones)
COPY.update({
    'casein-protein': dict(
        summary='Kasein förser musklerna med aminosyror i en långsam, jämn ström i upp till 7 timmar och stödjer därmed '
                'bibehållandet av muskelmassan under sömnen.',
        dosage=dict(recommended='20–40 g', timing='30 minuter före sänggåendet eller mellan långa perioder utan mat',
                    frequency='En gång per dag'),
        warnings=['Innehåller mjölkprotein (kasein) och laktos',
                  'Passar inte personer med mjölkproteinallergi',
                  'Personer med njursjukdom bör hålla koll på sitt totala proteinintag'],
        interactions='Ta det med två timmars mellanrum från antibiotika, bisfosfonater och järntillskott.',
        naturalSources='Standardmjölk, keso och grekisk yoghurt.'),
    'creatine-monohydrate': dict(
        summary='Kreatin ökar den fysiska prestationsförmågan i serier av kortvariga, mycket intensiva träningspass '
                '(EFSA-godkänt påstående vid 3 g per dag).',
        dosage=dict(recommended='3–5 g per dag',
                    timing='Vid samma tid varje dag, med vatten eller kolhydrater för bättre upptag',
                    frequency='Varje dag, kontinuerligt'),
        warnings=['Kan ge en lätt vätskeansamling i muskelcellerna (1–2 kg)',
                  'Drick 3–4 liter vatten per dag',
                  'Personer som har haft njursvikt bör rådgöra med läkare före användning'],
        interactions='Säkert tillsammans med de flesta läkemedel; var försiktig i kombination med läkemedel som kan belasta '
                     'njurarna (till exempel höga doser NSAID).',
        naturalSources='Rött kött, sill och lax (i små mängder).'),
    'bcaa': dict(
        summary='BCAA förser muskelvävnaden med aminosyror under fysisk ansträngning; tillskottet behövs inte om ditt '
                'dagliga proteinintag från vassle och mat är tillräckligt.',
        dosage=dict(recommended='5–10 g (i förhållandet 2:1:1 mellan leucin, isoleucin och valin)',
                    timing='Före eller under träning', frequency='På träningsdagar'),
        warnings=['Får inte användas av personer med lönnsirapssjukdom (MSUD), en ärftlig ämnesomsättningssjukdom'],
        interactions='BCAA kan konkurrera med Parkinsonläkemedlet levodopa om upptaget; ta dem med två timmars mellanrum.',
        naturalSources='Kött, fågel, fisk, ägg och mejeriprodukter.'),
    'beta-alanine': dict(
        summary='Beta-alanin höjer halten av karnosin i musklerna, vilket hjälper till att buffra syran i musklerna vid mycket '
                'intensiva ansträngningar som varar en till fyra minuter.',
        dosage=dict(recommended='2–5 g per dag',
                    timing='Fördelat på små doser (1,5–2 g) för att undvika stickningar i huden',
                    frequency='Varje dag, kontinuerligt'),
        warnings=['Ger tillfälliga, ofarliga stickningar i huden (parestesi) som går över inom 60–90 minuter; att dela upp '
                  'dosen minskar dem',
                  'Gravida och ammande avråds från det eftersom säkerhetsdata är otillräckliga'],
        interactions='Inga allvarliga läkemedelsinteraktioner har registrerats kliniskt.',
        naturalSources='Fågel, rött kött och fisk.'),
    'multivitamins': dict(
        summary='Multivitamin stödjer kroppens normala funktioner och fyller näringsluckor hos personer vars dagliga intag av '
                'viktiga vitaminer och mineraler är för lågt.',
        dosage=dict(recommended='En tablett eller kapsel per dag', timing='Till frukost eller lunch',
                    frequency='En gång per dag'),
        warnings=['Överskrid inte dagsdosen, för att undvika toxisk ansamling av de fettlösliga vitaminerna (A, D, E)',
                  'Gravida bör använda ett särskilt graviditetstillskott utan höga doser A-vitamin'],
        interactions='Var försiktig med produkter som innehåller K-vitamin om du tar blodförtunnande läkemedel (warfarin). '
                     'Ta det med 4 timmars mellanrum från sköldkörtelläkemedel (levotyroxin).',
        naturalSources='Frukt, grönsaker, fullkorn, ägg och baljväxter.'),
    'zinc': dict(
        summary='Zink bidrar till immunsystemets normala funktion, till normal protein- och DNA-syntes och till att '
                'bibehålla normala testosteronnivåer i blodet (EFSA).',
        dosage=dict(recommended='15–25 mg elementärt zink per dag',
                    timing='Till en lätt måltid (undvik att ta det på helt tom mage)', frequency='En gång per dag'),
        warnings=['Den övre säkra gränsen enligt EU:s normer (EFSA) är 25 mg per dag',
                  'Långvarigt höga doser utan koppar kan ge blodbrist på grund av kopparbrist'],
        interactions='Zink minskar upptaget av tetracykliner och fluorokinoloner; ta det med två timmars mellanrum från '
                     'kalcium- och järntillskott, som konkurrerar om samma upptagsvägar.',
        naturalSources='Ostron, nötkött, pumpafrön, linser och kikärter.'),
    'green-tea-extract': dict(
        summary='Grönt te-extrakt innehåller kraftfulla antioxidanter (katekiner) som hjälper till att skydda cellerna mot '
                'oxidativ stress och stödjer den dagliga ämnesomsättningen.',
        dosage=dict(recommended='250–400 mg EGCG per dag', timing='Till en måltid (morgon eller mitt på dagen)',
                    frequency='En gång per dag'),
        warnings=['EFSA varnar: ta det aldrig på tom mage',
                  'Doser över 800 mg EGCG per dag kan ge leverskador',
                  'Inte för gravida, ammande eller barn'],
        interactions='Kan interagera med blodförtunnande och blodtryckssänkande läkemedel; undvik att kombinera det med '
                     'centralstimulerande medel eller läkemedel som påverkar levern.',
        naturalSources='Ceremoniell matcha och bryggt grönt te.'),
    'cla': dict(
        summary='En naturlig fettsyra som enligt vissa studier har en stödjande roll i fettomsättningen och i idrottares '
                'kroppssammansättning, tillsammans med kost och träning.',
        dosage=dict(recommended='3000 mg per dag', timing='Till huvudmåltiderna', frequency='Fördelat på 2–3 doser per dag'),
        warnings=['Kan ge lätta magbesvär i början',
                  'Långvarig användning av för höga doser kräver uppföljning av leverfett och insulinresistens',
                  'Rekommenderas inte under graviditet eller amning'],
        interactions='Generellt säkert; personer som tar diabetesläkemedel bör följa sina blodsockervärden.',
        naturalSources='Nötkött från gräsbetande djur, mejeriprodukter och feta mjölkprodukter.'),
    'l-carnitine': dict(
        summary='L-karnitin har en viktig roll i transporten av långkedjiga fettsyror in i mitokondrierna för '
                'energiproduktion, och stödjer fysisk prestationsförmåga och muskelåterhämtning.',
        dosage=dict(recommended='1000–2000 mg per dag', timing='30–60 minuter före träning eller på morgonen',
                    frequency='1–2 gånger per dag'),
        warnings=['Höga doser kan ge illamående eller en lätt fisklukt i svett och urin',
                  'Undvik att ta det på kvällen för att förebygga sömnsvårigheter',
                  'Rekommenderas inte för personer med epilepsi utan medicinsk uppföljning'],
        interactions='Kan minska effekten av sköldkörtelhormon i vävnaderna; personer med underfunktion i sköldkörteln bör '
                     'rådgöra med läkare. Det interagerar med blodförtunnande läkemedel (antikoagulantia).',
        naturalSources='Rött kött, lamm, fågel och mjölk.'),
    'melatonin': dict(
        summary='Melatonin bidrar till att minska den tid det tar att somna och till att lindra subjektiva känslor av jetlag '
                '(EFSA-godkända påståenden vid 0,5–1 mg).',
        dosage=dict(recommended='0,3–1 mg (börja med den lägsta verksamma dosen)', timing='30–60 minuter före sänggåendet',
                    frequency='Vid behov'),
        # the Dutch legal note of the record is left out (approved 2026-10-26): the Swedish one is in EXTRA_WARNINGS
        warnings=['Kör inte bil och använd inte maskiner efter intag',
                  'Inte för gravida, ammande eller barn utan medicinsk uppföljning'],
        interactions='Melatonin interagerar med lugnande medel, antidepressiva läkemedel, blodtryckssänkande läkemedel och '
                     'blodförtunnande läkemedel (kan förlänga blödningstiden).',
        naturalSources='Syrliga Montmorency-körsbär, valnötter och havre.'),
    '5-htp': dict(
        summary='En naturlig mellanprodukt från fröna av växten Griffonia som omvandlas direkt i hjärnan till signalsubstansen '
                'serotonin, och som stödjer en stabil sinnesstämning och en regelbunden sömnrytm.',
        dosage=dict(recommended='50–100 mg (börja med 50 mg)', timing='30 minuter före sänggåendet med ett lätt mellanmål',
                    frequency='En gång per dag'),
        warnings=['Kan ge illamående eller lätta magbesvär',
                  'Inte för gravida, ammande eller personer som tar Parkinsonläkemedel (karbidopa)'],
        interactions='Viktig klinisk varning: ta det aldrig tillsammans med antidepressiva läkemedel (SSRI, SNRI, MAO-hämmare) '
                     'eller johannesört, för att undvika serotonergt syndrom, som kan vara livshotande.',
        naturalSources='Fröna av växten Griffonia simplicifolia.'),
    'caffeine': dict(
        summary='Koffein bidrar till ökad vakenhet, uppmärksamhet och koncentration och ökar uthålligheten vid muskelarbete '
                '(stöds av positiva vetenskapliga yttranden från EFSA vid angivna doser).',
        dosage=dict(recommended='100–200 mg per dos (högst 400 mg per dag för friska vuxna)',
                    timing='På morgonen eller före träning; undvik det efter klockan 14', frequency='1–2 gånger per dag'),
        warnings=['EFSA:s säkra gräns under graviditet är högst 200 mg per dag från alla källor',
                  'Höga doser ger hjärtklappning, oro och en tillfällig höjning av blodtrycket'],
        interactions='Koffein interagerar med efedrin, astmaläkemedlet teofyllin och läkemedel mot högt blodtryck och '
                     'oregelbunden hjärtrytm.',
        naturalSources='Kaffebönor, teblad, guarana, yerba mate och kakao.'),
    'pre-workout': dict(
        summary='En komplett blandning som kombinerar centralstimulerande ämnen (koffein) med kärlvidgande ämnen (citrullin) '
                'och buffertar mot trötthet (beta-alanin) för att stödja blodflödet och muskelaktiviteten.',
        dosage=dict(recommended='En skopa (eller börja med en halv skopa för att se hur du tål det)',
                    timing='Upplöst i vatten 20–30 minuter före träning',
                    frequency='Endast på träningsdagar (inte dagligen)'),
        warnings=['Vissa blandningar överskrider EFSA:s gräns för koffein per dos (200 mg)',
                  'Inte för personer med hjärtsjukdom eller högt blodtryck, eller för gravida och ammande',
                  'Använd det inte dagligen, för att undvika tillvänjning'],
        interactions='Kombinera det inte med blodtrycks- eller hjärtläkemedel, eller med andra centralstimulerande medel '
                     'eller extra kaffe.',
        naturalSources='En sammansatt prestationshöjande blandning av flera ingredienser.'),
    'glucosamine-chondroitin': dict(
        summary='Naturliga byggstenar som finns i ledbrosk och ledvätska; de hjälper till att stödja ledernas rörlighet och '
                'bibehållandet av bindväven.',
        dosage=dict(recommended='1500 mg glukosaminsulfat + 1200 mg kondroitin per dag',
                    timing='Till måltider (resultat märks efter 2–4 månader)', frequency='1–2 gånger per dag'),
        warnings=['De flesta källor kommer från skal av skaldjur och räkor, så det får absolut inte användas av personer med '
                  'skaldjursallergi (om inte källan är växtbaserad)',
                  'Kan påverka blodsockervärdena något'],
        interactions='Viktig varning vid behandling med warfarin (Waran): glukosamin och kondroitin kan öka blodförtunningen '
                     'och PK(INR)-värdet farligt mycket; noggrann medicinsk uppföljning krävs.',
        naturalSources='Skal av skaldjur och brosk från nötkreatur och fågel.'),
    'collagen-peptides': dict(
        summary='Lättupptagna, hydrolyserade peptider rika på glycin och prolin som hjälper till att stödja hudens '
                'elasticitet och fuktighet samt bindvävens och broskets hälsa.',
        dosage=dict(recommended='10–15 g per dag',
                    timing='Upplöst i morgonkaffet eller i vatten, gärna tillsammans med en källa till C-vitamin',
                    frequency='En gång per dag'),
        warnings=['Välj källan med omsorg om du har allergier (fiskkollagen vid fiskallergi)',
                  'Kontrollera att produkten är fri från tungmetaller'],
        interactions='Säkert, utan kliniskt registrerade läkemedelsinteraktioner.',
        naturalSources='Traditionell benbuljong, fiskskinn och gelatinrikt kött.'),
    'l-citrulline': dict(
        summary='En aminosyra som njurarna effektivt omvandlar till L-arginin, vilket stödjer bildningen av kväveoxid (NO), '
                'vidgningen av blodkärlen och blodflödet till musklerna.',
        dosage=dict(recommended='6–8 g citrullinmalat (eller 3–5 g ren citrullin)', timing='45–60 minuter före träning',
                    frequency='På träningsdagar'),
        warnings=['Lätta magbesvär vid mycket höga doser; börja med 3 g',
                  'Säkert för njurar och lever inom de rekommenderade doserna'],
        interactions='Varning för blodtrycket: citrullin interagerar kraftigt med potensläkemedel (PDE5-hämmare som Viagra och '
                     'Cialis), nitrater och blodtryckssänkande läkemedel, och kan ge ett kraftigt blodtrycksfall.',
        naturalSources='Vattenmelonens skal och fruktkött samt gurka.'),
    'taurine': dict(
        summary='En svavelhaltig aminosyra med en viktig roll i muskelcellernas vätske- och elektrolytbalans, i bildningen av '
                'gallsalter och i nervsystemets och hjärtats funktioner.',
        dosage=dict(recommended='1000–2000 mg per dag', timing='Före träning eller fördelat på måltiderna',
                    frequency='1–2 gånger per dag'),
        warnings=['Publicerade säkerhetsbedömningar visar att det är säkert upp till 3000 mg per dag',
                  'Undvik att få det från energidrycker fulla av socker och centralstimulerande ämnen'],
        interactions='Säkert med de flesta läkemedel; det kan påverka litiumhalten i blodet, så personer som tar litium '
                     'behöver medicinsk uppföljning.',
        naturalSources='Skaldjur, mörkt fågelkött, fisk och inälvsmat.'),
    'coenzyme-q10': dict(
        summary='En livsviktig fettlöslig antioxidant som finns i mitokondrierna i hjärt- och muskelceller och behövs för '
                'cellernas energiproduktion (ATP); den fyller på de nivåer som kolesterolsänkande statiner minskar.',
        dosage=dict(recommended='100–200 mg per dag (den aktiva formen ubikinol är att föredra efter 40 års ålder)',
                    timing='Till en fettrik måltid för bästa upptag, och inte nära sänggåendet', frequency='En gång per dag'),
        warnings=['Säkert i doser upp till 300 mg',
                  'Ta det i god tid före sänggåendet för att undvika lätta sömnsvårigheter hos vissa'],
        interactions='Q10 liknar K-vitamin till strukturen; det kan minska effekten av det blodförtunnande läkemedlet warfarin '
                     'och öka risken för blodproppar, så PK(INR) måste kontrolleras. Det kan sänka blodtrycket och '
                     'blodsockret ytterligare.',
        naturalSources='Inälvsmat (hjärta, lever), fet makrill och sardiner.'),
    'l-theanine': dict(
        summary='En naturlig aminosyra som finns i gröna teblad; den passerar blod-hjärnbarriären och främjar alfavågor i '
                'hjärnan, vilket ger ett tillstånd av lugn vakenhet och avslappning utan dåsighet.',
        dosage=dict(recommended='100–200 mg',
                    timing='På morgonen (ofta 1:2 med koffein för lugnt fokus) eller på kvällen för att stödja avslappning',
                    frequency='1–2 gånger per dag'),
        warnings=['Den kliniska säkerheten är mycket hög upp till 400 mg per dag',
                  'Gravida och ammande avråds från koncentrerade tillskott eftersom kliniska säkerhetsdata är begränsade'],
        interactions='Kan förstärka effekten av blodtryckssänkande läkemedel och lugnande medel som verkar på centrala '
                     'nervsystemet.',
        naturalSources='Gröna teblad (Camellia sinensis) och matcha av hög kvalitet.'),
    'rhodiola-rosea': dict(
        summary='En väletablerad adaptogen fjällört som stödjer kroppens motståndskraft mot stress, mental anspänning och '
                'fysisk trötthet, och hjälper till att bevara den mentala skärpan under press.',
        dosage=dict(recommended='200–400 mg (standardiserat till 3 % rosaviner och 1 % salidrosid)',
                    timing='På morgonen på fastande mage, en halvtimme före frukost; undvik det på kvällen',
                    frequency='En gång per dag'),
        warnings=['Inte för personer med bipolär sjukdom, eftersom det kan utlösa maniska episoder',
                  'Undvik det på kvällen för att förebygga sömnsvårigheter',
                  'Ska inte användas under graviditet och amning'],
        interactions='Rosenrot interagerar med antidepressiva och stämningsstabiliserande läkemedel (sällsynt serotonergt '
                     'syndrom med SSRI är möjligt); det kan sänka blodsocker och blodtryck, så diabetes- och '
                     'blodtrycksläkemedel behöver följas upp.',
        naturalSources='Roten av Rhodiola rosea, skördad på arktiska fjällhöjder.'),
    'ginkgo-biloba': dict(
        summary='Ginkgo hjälper till att stödja mikrocirkulationen och blodflödet i de små kärlen i hjärnan och i armar och '
                'ben; dess flavonoider fungerar som antioxidanter som skyddar nervcellerna mot oxidativ stress och stödjer '
                'mental skärpa och korttidsminne.',
        dosage=dict(recommended='120–240 mg standardiserat extrakt (EGb 761)', timing='Till måltider (morgon och mitt på dagen)',
                    frequency='Fördelat på två doser per dag'),
        forms='Standardiserade 24/6-extrakt (24 % flavonglykosider och 6 % terpenlaktoner, som EGb 761) med en halt av '
              'ginkgolsyror under 5 ppm för att undvika allergiska reaktioner och magbesvär.',
        warnings=['Inte för personer som har haft epilepsi eller krampanfall',
                  'Ska inte användas under graviditet eller amning eftersom säkerhetsdata är otillräckliga',
                  'Sluta ta det 14 dagar före en operation'],
        interactions='Varning för blödning: ginkgo ökar risken för blödning; kombinera det inte utan medicinsk uppföljning '
                     'med blodförtunnande läkemedel och antikoagulantia (warfarin, acetylsalicylsyra, klopidogrel) eller '
                     'NSAID. Det kan interagera med diabetes- och blodtrycksläkemedel.',
        naturalSources='Blad från ginkgoträdet (används endast som standardiserat extrakt).'),
    'lions-mane': dict(
        summary='Innehåller hericenoner och erinaciner, som enligt laboratoriestudier kan stimulera bildningen av '
                'nervtillväxtfaktor (NGF); små studier på människor tyder på att svampen stödjer fokus, mental skärpa och '
                'kognitiv flexibilitet.',
        dosage=dict(recommended='1000–2000 mg standardiserat extrakt av fruktkroppen',
                    timing='På morgonen till frukost eller en varm dryck', frequency='En gång per dag'),
        forms='Extrakt av 100 % fruktkropp, framställt genom extraktion med varmt vatten och alkohol; undvik mycel odlat på '
              'spannmål, som har hög stärkelsehalt och låg halt av aktiva ämnen.',
        warnings=['Kan ge lätt klåda eller allergiska utslag hos personer som är allergiska mot svamp',
                  'Bör undvikas under graviditet och amning eftersom studierna är få'],
        interactions='Kan sänka blodsockret något; följ dina värden om du tar blodsockersänkande läkemedel eller insulin. '
                     'Det kan fördröja blodets koagulation något, så var försiktig med blodförtunnande läkemedel.',
        naturalSources='Färsk eller torkad igelkottstaggsvamp (tillagas som mat i det asiatiska köket).'),
    'hmb': dict(
        summary='En aktiv metabolit av aminosyran leucin; HMB hjälper till att begränsa nedbrytningen av muskelprotein genom '
                'att hämma ubikitinvägen och stimulera mTOR, och är mest användbart vid kalorirestriktion och för att '
                'begränsa åldersrelaterad muskelförlust.',
        dosage=dict(recommended='3 g per dag', timing='Som en dos 60 minuter före träning, eller 1 g till varje huvudmåltid',
                    frequency='En gång per dag eller fördelat på 3 måltider'),
        forms='Kalcium-HMB (HMB-Ca), den vanligaste och billigaste formen, och HMB i fri syraform (HMB-FA), som når blodet '
              'snabbare.',
        warnings=['Säkert för långvarig användning upp till 3 g per dag',
                  'Tillför lite för den som redan äter mycket vassleprotein och leucin',
                  'Personer med njursvikt bör rådgöra med läkare, eftersom HMB-Ca innehåller kalcium'],
        interactions='Inga allvarliga kliniska läkemedelsinteraktioner har rapporterats.',
        naturalSources='Små mängder i alfalfa, grapefrukt och malfisk; kroppen bildar en liten mängd från leucin i maten.'),
    'l-glutamine': dict(
        summary='Den vanligaste aminosyran i blod och muskler; den är det viktigaste bränslet för cellerna i tunntarmens '
                'slemhinna och för immunförsvarets celler, och hjälper till att stödja de täta förbindelserna mellan '
                'tarmcellerna och tarmbarriärens funktion.',
        dosage=dict(recommended='5–10 g per dag (upp till 15–20 g fördelat på flera doser i program för tarmslemhinnan)',
                    timing='Efter träning eller före sänggåendet, upplöst i kallt vatten på fastande mage',
                    frequency='1–2 gånger per dag'),
        forms='Växtfermenterat L-glutaminpulver i fri form för högsta renhet.',
        warnings=['Lös upp det i kallt eller ljummet vatten, eftersom värme minskar stabiliteten',
                  'Inte för personer med hepatisk encefalopati eller långt gången levercirros',
                  'Använd med försiktighet om du har en neurologisk sjukdom'],
        interactions='Glutamin kan minska effekten av läkemedel mot epilepsi och kramper, eftersom det i hjärnan omvandlas '
                     'till det retande ämnet glutamat; rådgör med läkare innan du kombinerar dem.',
        naturalSources='Kött, ägg, fisk, mejeriprodukter, bönor och linser.'),
    'l-arginine': dict(
        summary='En semiessentiell aminosyra som är det direkta substratet för enzymet NOS vid bildningen av kväveoxid, som '
                'får den glatta muskulaturen i artärväggarna att slappna av och därmed hjälper till att vidga blodkärlen '
                'och stödja ett syrerikt blodflöde.',
        dosage=dict(recommended='3–6 g per dag',
                    timing='30–60 minuter före träning på fastande mage, eller fördelat på måltiderna',
                    frequency='En gång per dag eller fördelat på flera doser'),
        forms='Arginin-alfa-ketoglutarat (AAKG) vid träning; citrullintillskott höjer argininhalten i blodet mer effektivt '
              'eftersom de går förbi leverns förstapassagemetabolism.',
        warnings=['Herpes simplex-viruset behöver arginin för att föröka sig; tillskottet kan utlösa munsår eller genitala '
                  'utbrott hos bärare',
                  'Stora doser kan ge tarmkramper och diarré'],
        interactions='Varning för lågt blodtryck: arginin interagerar kraftigt med blodtryckssänkande läkemedel, nitrater mot '
                     'hjärtsjukdom och PDE5-hämmare (sildenafil, tadalafil) och kan ge ett farligt blodtrycksfall.',
        naturalSources='Rött kött och fågel, fisk, nötter och pumpafrön samt baljväxter.'),
    'vitamin-c': dict(
        summary='C-vitamin bidrar till att skydda cellerna mot oxidativ stress, till att upprätthålla immunsystemets normala '
                'funktion under och efter intensiv fysisk träning och till normal kollagenbildning för broskets och hudens '
                'normala funktion (EFSA-godkända påståenden).',
        dosage=dict(recommended='500–1000 mg per dag',
                    timing='Till måltider; upptaget sjunker under 50 % när en enskild dos överstiger 1000 mg',
                    frequency='Fördelat på 1–2 doser'),
        forms='Kalcium- eller magnesiumaskorbat (buffrat C-vitamin) om du har sur mage, eller liposomalt C-vitamin för högre '
              'upptag utan att irritera magen.',
        warnings=['Doser över 2000 mg per dag kan ge osmotisk diarré',
                  'Höga doser kan öka risken för njursten av kalciumoxalat hos personer som är benägna att få det'],
        interactions='C-vitamin ökar markant upptaget av icke-hemjärn (viktigt för personer med järnöverskott). Höga doser kan '
                     'störa vissa cytostatika och kombinationen statin–niacin; rådgör med din läkare.',
        naturalSources='Paprika, guava, kiwi, citrusfrukter, jordgubbar och broccoli.'),
    'vitamin-b-complex': dict(
        summary='De åtta B-vitaminerna fungerar som koenzymer som omvandlar kolhydrater, fett och protein till energi; de '
                'bidrar till normal energiomsättning, till nervsystemets normala funktion, till normal bildning av röda '
                'blodkroppar och till att minska trötthet och utmattning (EFSA).',
        dosage=dict(recommended='1 kapsel per dag (högst 12 mg B6)',
                    timing='Till frukost; undvik det helst på kvällen eftersom det kan öka vakenheten',
                    frequency='En gång per dag'),
        forms='Bioaktiva former: metylkobalamin (B12), metylfolat (5-MTHF) i stället för syntetisk folsyra och '
              'pyridoxal-5-fosfat (P5P) för B6-vitamin.',
        warnings=['Klargul urin är normalt och ofarligt och beror på utsöndrat B2-vitamin',
                  'EFSA:s övre gräns från 2023: dagligt intag av B6-vitamin bör inte överstiga 12 mg, för att undvika '
                  'skador på de perifera känselnerverna'],
        interactions='B6-vitamin kan minska effekten av levodopa vid Parkinsons sjukdom när det tas utan karbidopa. Metformin, '
                     'p-piller, vissa vätskedrivande läkemedel och syrahämmande läkemedel sänker nivåerna av B12 och folat.',
        naturalSources='Fullkorn, ägg, kött och lever, baljväxter, bladgrönsaker och mejeriprodukter.'),
    'iron': dict(
        summary='Järn bidrar till normal bildning av röda blodkroppar och hemoglobin, till normal syretransport i kroppen, '
                'till normal kognitiv funktion och till att minska trötthet och utmattning (EFSA-godkända påståenden).',
        dosage=dict(recommended='14–25 mg elementärt järn per dag (endast när brist är bekräftad)',
                    timing='På fastande mage med ett halvt glas apelsinjuice, eller till ett lätt mellanmål om det ger '
                           'illamående',
                    frequency='En gång per dag'),
        forms='Järnbisglycinat: skonsamt mot mage och tarm, med mindre förstoppning och illamående än traditionellt '
              'järnsulfat.',
        warnings=['Ta det inte utan att först ha tagit ett blodprov för ferritin; järn lagras i lever, hjärta och '
                  'bukspottkörtel och kroppen saknar ett effektivt sätt att göra sig av med det',
                  'Inte för personer med hemokromatos',
                  'Förvara det utom räckhåll för barn för att förhindra akut förgiftning'],
        interactions='Ta det med två timmars mellanrum från kaffe, te, kalcium- och magnesiumtillskott och '
                     'syraneutraliserande medel, och med fyra timmars mellanrum från levotyroxin (sköldkörtelhormon) och '
                     'antibiotika (kinoloner och tetracykliner).',
        naturalSources='Rött kött och lever, linser och bönor, spenat, pumpafrön och berikade flingor.'),
    'calcium': dict(
        summary='Kalcium behövs för att bibehålla normal benstomme och normala tänder och bidrar till normal '
                'blodkoagulering, normal signalöverföring mellan nervcellerna och normal muskelfunktion '
                '(EFSA-godkända påståenden).',
        dosage=dict(recommended='500–800 mg elementärt kalcium per dag',
                    timing='Till måltider (karbonat endast till en måltid); kroppen tar inte upp mer än 500 mg per dos',
                    frequency='Fördelat på två doser'),
        forms='Kalciumcitrat är det bästa valet: det tas upp med eller utan mat och är inte beroende av magsyra; karbonat är '
              'billigare men måste tas till en hel måltid och kan ge gaser och förstoppning.',
        warnings=['EFSA:s övre gräns för vuxna är 2500 mg per dag från alla källor',
                  'Långvarigt överskott utan balans med D3-vitamin, K2-vitamin och magnesium kan öka risken för '
                  'kärlförkalkning och njursten'],
        interactions='Kalcium konkurrerar med järn, zink och magnesium om upptaget; ta det med två timmars mellanrum från dem. '
                     'Det minskar upptaget av levotyroxin, antibiotika (fluorokinoloner och tetracykliner) och '
                     'bisfosfonater; ta det med 2–4 timmars mellanrum.',
        naturalSources='Mjölk, ost och yoghurt, sardiner med ben, tahini, mandlar och mörka bladgrönsaker.'),
    'probiotics': dict(
        summary='Levande nyttiga bakteriestammar (till exempel Lactobacillus och Bifidobacterium) som koloniserar '
                'tarmslemhinnan, konkurrerar med skadliga mikrober och bildar kortkedjiga fettsyror, och som stödjer '
                'tarmslemhinnans barriär och en regelbunden matsmältning.',
        dosage=dict(recommended='10–50 miljarder CFU per dag',
                    timing='20 minuter före frukost eller vid sänggåendet med ett glas kallt vatten',
                    frequency='En gång per dag'),
        forms='Syraresistenta kapslar (fördröjd frisättning) som anger varje stam med fullständigt namn (till exempel LGG '
              'eller BB-12) och är framtagna för att hålla bakterierna levande fram till bäst före-datum.',
        warnings=['Kan ge tillfälliga gaser och uppblåsthet de första dagarna',
                  'Inte för personer med svår immunbrist, intensivvårdspatienter eller personer med central venkateter, '
                  'på grund av en sällsynt risk för blodförgiftning'],
        interactions='Antibiotika dödar de probiotiska bakterierna; ta tillskottet minst 2–3 timmar efter en antibiotikados. '
                     'Rådgör med läkare om du tar immunhämmande läkemedel.',
        naturalSources='Yoghurt och kefir, kärnmjölk, naturligt fermenterade inläggningar, surkål och kimchi.'),
    'turmeric-curcumin': dict(
        summary='Den aktiva polyfenolen i gurkmejaroten; den har antioxidativa egenskaper genom att hämma cellulära '
                'signalvägar kopplade till oxidativ stress (som NF-kB och enzymet COX-2), och hjälper till att stödja '
                'ledernas komfort och rörlighet.',
        dosage=dict(recommended='500–1000 mg standardiserat kurkuminextrakt (95 % kurkuminoider)',
                    timing='Till måltider som innehåller nyttigt fett, till exempel olivolja',
                    frequency='Fördelat på 1–2 doser per dag'),
        forms='Vanligt kurkumin tas upp dåligt; välj ett standardiserat extrakt (95 % kurkuminoider) med piperin '
              '(svartpepparextrakt, som ökade upptaget upp till 20 gånger i en studie på människor) eller en fytosomform '
              'bunden till fosfolipider.',
        warnings=['Inte för personer med gallgångshinder eller aktiva gallstenar, eftersom kurkumin får gallblåsan att dra '
                  'ihop sig',
                  'Den franska livsmedelssäkerhetsmyndigheten (ANSES) har registrerat fall av leverskador med extrakt som '
                  'har högt upptag; avbryt och kontakta läkare om du märker gulfärgning, mörk urin eller buksmärta',
                  'Undvik tillskottsdoser under graviditet och amning'],
        interactions='Kurkumin förstärker effekten av blodförtunnande läkemedel och antikoagulantia och kan sänka blodsockret '
                     'ytterligare tillsammans med diabetesläkemedel. Piperin hämmar leverenzymer (som CYP3A4) och ändrar '
                     'därmed blodnivåerna av många läkemedel.',
        naturalSources='Färsk eller malen gurkmejarot (gurkmeja i köket innehåller bara 2–5 % kurkumin).'),
    'ginger': dict(
        summary='Rik på de aktiva ämnena gingeroler och shogaoler, som hjälper till att påskynda magsäckens tömning, lugna '
                'kramper i matsmältningen och verka på serotoninreceptorerna 5-HT3, och som stödjer magkomforten och '
                'lindrar känslan av illamående och åksjuka.',
        dosage=dict(recommended='500–1500 mg standardiserat extrakt per dag',
                    timing='Till måltider, eller en halvtimme före resa', frequency='Fördelat på 1–3 doser'),
        forms='Kapslar med standardiserat torrextrakt (5 % gingeroler) för en jämn halt, eller te på färsk ingefärsrot.',
        warnings=['Doser över 4–5 g per dag kan ge halsbränna och sura uppstötningar',
                  'Gravida: högst 1000 mg per dag, och endast efter samråd med läkare'],
        interactions='Ingefära har en lätt hämmande effekt på blodplättarna; var försiktig med höga doser blodförtunnande '
                     'läkemedel (warfarin, acetylsalicylsyra). Den kan förstärka blodtrycks- och diabetesläkemedel.',
        naturalSources='Färsk, torkad och malen ingefärsrot.'),
    'spirulina': dict(
        summary='En mikroalg rik på vegetabiliskt protein (cirka 60–65 %), vitaminer och mineraler, med det blå pigmentet '
                'fykocyanin som har antioxidativa egenskaper, och som hjälper till att stödja vardagens vitalitet och energi.',
        dosage=dict(recommended='3–5 g per dag (pulver eller tabletter)', timing='Till frukost eller i smoothies och juicer',
                    frequency='En gång per dag'),
        forms='Certifierat ekologisk spirulina odlad under kontrollerade förhållanden, med analyscertifikat som visar att den '
              'är fri från mikrocystiner och tungmetaller som bly och arsenik.',
        warnings=['Inte för personer med autoimmuna sjukdomar (MS, lupus, reumatoid artrit), eftersom den kan stimulera '
                  'immunförsvaret',
                  'Inte för personer med fenylketonuri (PKU), eftersom den innehåller fenylalanin',
                  'Kan ge lätt illamående i början'],
        interactions='Spirulina kan motverka immunhämmande läkemedel (som kortison och ciklosporin) eftersom den stimulerar '
                     'immunförsvaret. Den kan förstärka blodförtunnande läkemedel något.',
        naturalSources='Spirulina i sig (pulver eller tabletter); den finns inte i vardagsmat.'),
    'garcinia-cambogia': dict(
        summary='Fruktskalet innehåller hydroxicitronsyra (HCA), som i laboratoriestudier hämmar citratlyas, ett enzym som '
                'deltar när ett överskott av kolhydrater omvandlas till fett; den kan stödja mättnadskänslan något, men '
                'effekten på vikten i studier på människor är måttlig.',
        dosage=dict(recommended='500–1000 mg standardiserat extrakt (50–60 % HCA)',
                    timing='30–60 minuter före måltider med ett stort glas vatten', frequency='2–3 gånger per dag'),
        forms='HCA-extrakt bundna till kalcium eller kalium för stabilitet, kontrollerade så att de är fria från '
              'odeklarerade centralstimulerande ämnen.',
        warnings=['Ingen mirakellösning: effekten på viktnedgång är måttlig och varierar mellan studier på människor',
                  'Sällsynta fall av leverskador har rapporterats; inte för personer med lever- eller njursvikt, och avbryt '
                  'genast om du märker gulfärgning eller mörk urin',
                  'Ska inte användas under graviditet eller amning'],
        interactions='Kan sänka blodsockret; följ dina värden om du tar diabetesläkemedel och insulin. Den kan interagera med '
                     'kolesterolsänkande läkemedel (statiner) och serotonerga antidepressiva läkemedel.',
        naturalSources='Skalet av garciniafrukten (används traditionellt i det sydasiatiska köket).'),
    'forskolin': dict(
        summary='Ett växtämne som direkt aktiverar enzymet adenylatcyklas i cellerna och höjer budbärarmolekylen cAMP, som '
                'deltar i fettomsättningen och i avslappningen av glatt muskulatur; forskningen på människor om effekten på '
                'vikten är begränsad.',
        dosage=dict(recommended='250 mg standardiserat extrakt (10–20 % forskolin)', timing='Till frukost och middag',
                    frequency='Två gånger per dag'),
        forms='Standardiserat torrextrakt av Coleus forskohlii-rot (10–20 % forskolin) med dokumenterad renhet.',
        warnings=['Kan öka magsyran och ge lätt diarré; inte för personer med aktivt magsår',
                  'Ska inte användas under graviditet eller amning',
                  'Forskningen på människor är begränsad; resultat tar 8–12 veckor'],
        interactions='Varning för blodtryck och blödning: forskolin vidgar blodkärlen, sänker blodtrycket och hämmar '
                     'blodplättarna; kombinera det inte med blodtryckssänkande eller blodförtunnande läkemedel, för att '
                     'undvika lågt blodtryck och blödningar.',
        naturalSources='Roten av Coleus forskohlii (kransblommiga växter); finns inte i vardagsmat.'),
    'eaa': dict(
        summary='De nio aminosyror som kroppen inte kan bilda själv och måste få från maten; de ger de kompletta '
                'byggstenarna för muskelproteinsyntesen och är bättre än enbart BCAA eftersom de tillför alla aminosyror '
                'som behövs för att fullborda den.',
        dosage=dict(recommended='10–15 g upplöst i vatten', timing='Under eller efter träning, eller mellan måltiderna',
                    frequency='1–2 gånger per dag'),
        forms='Snabbupptaget EAA-pulver i fri form, sockerfritt och berikat med leucin.',
        warnings=['Behövs inte om du äter mycket fullvärdigt protein som kyckling, ägg och vassle',
                  'Personer med långt gången njur- eller leversvikt bör anpassa dosen tillsammans med sin läkare'],
        interactions='Säkert med de flesta läkemedel; ta dem med två timmars mellanrum från levodopa vid Parkinsons sjukdom, '
                     'eftersom aminosyror konkurrerar med det om upptaget.',
        naturalSources='Ägg, kött och fågel, fisk, mejeriprodukter och soja.'),
    'l-leucine': dict(
        summary='Den mest anabola aminosyran; den fungerar som strömbrytaren för signalvägen mTORC1 i muskelfibrerna och '
                'stimulerar proteinsyntesen, och är särskilt användbar för äldre för att motverka den åldersrelaterade '
                'minskningen av det anabola svaret.',
        dosage=dict(recommended='2,5–4 g per dos', timing='Till en proteinfattig måltid eller direkt efter träning',
                    frequency='1–2 gånger per dag'),
        forms='Instantiserat L-leucin framställt genom växtfermentering, för att undvika den beska smaken och den dåliga '
              'lösligheten.',
        warnings=['Undvik stora separata doser under lång tid utan de andra aminosyrorna, för att förhindra obalans i blodets '
                  'nivåer av isoleucin och valin',
                  'Tas helst tillsammans med en fullvärdig proteinkälla eller med EAA'],
        interactions='Generellt säkert; det kan sänka blodsockret något genom att stimulera insulinfrisättningen, så var '
                     'försiktig om du använder insulin eller diabetesläkemedel.',
        naturalSources='Vassle, kött och fågel, ägg, fisk, soja och linser.'),
    'lclt': dict(
        summary='En snabbupptagen form av karnitin bunden till vinsyra; kliniska studier pekar på en roll i att minska '
                'markörer för muskelskador och oxidativ stress efter hård träning, vilket stödjer en effektiv återhämtning.',
        dosage=dict(recommended='1000–2000 mg per dag',
                    timing='På morgonen och efter träning till en måltid som innehåller kolhydrater',
                    frequency='Fördelat på två doser'),
        forms='Rena kapslar eller pulver av L-formen av karnitin (som Carnipure®), fria från föroreningar av D-karnitin.',
        warnings=['Tas helst inte sent på kvällen, för att undvika sömnsvårigheter',
                  'Undvik det om du har svår njursvikt',
                  'Långvarig användning kan höja blodets nivåer av TMAO'],
        interactions='Kan minska sköldkörtelhormonets aktivitet i vävnaderna; var försiktig om du har underfunktion i '
                     'sköldkörteln. Det kan förstärka warfarin och andra antikoagulantia.',
        naturalSources='Rött kött, fågel, fisk och mejeriprodukter.'),
    'betaine-tmg': dict(
        summary='Ett naturligt ämne som finns i rödbetor och spannmål; betain bidrar till normal homocysteinomsättning '
                '(EFSA-godkänt påstående vid 1,5 g per dag) och fungerar som en osmolyt som skyddar muskelcellerna mot '
                'uttorkning och stödjer kraftutvecklingen.',
        dosage=dict(recommended='1,5–2,5 g per dag',
                    timing='30 minuter före träning eller fördelat på måltiderna; börja med 1,25 g',
                    frequency='En gång per dag eller fördelat på flera doser'),
        forms='Rent vattenfritt betain; förväxla det inte med betain-HCl, som är avsett att öka magsyran.',
        warnings=['EFSA varnar: mer än 4 g per dag kan märkbart höja kolesterolet i blodet',
                  'Kan ge lätta magbesvär i början'],
        interactions='Generellt säkert; var försiktig om du använder kolesterolsänkande läkemedel, eftersom höga doser kan '
                     'höja totalkolesterol och LDL-kolesterol något.',
        naturalSources='Rödbetor, spenat, quinoa, vetekli och fullkornsvete.'),
    'epicatechin': dict(
        summary='En växtflavanol som finns i kakao och grönt te; tidiga studier tyder på att den stödjer bildningen av '
                'kväveoxid och blodflödet, och förskjuter balansen mellan myostatin och follistatin, två proteiner som är '
                'kopplade till muskeltillväxt.',
        dosage=dict(recommended='150–250 mg (cirka 1,5–2 mg per kg kroppsvikt)',
                    timing='45 minuter före träning eller till frukost',
                    frequency='En gång per dag, i perioder om 8–12 veckor följda av 4 veckors uppehåll'),
        forms='Standardiserade extrakt av kakao eller te med 90 % epikatekin, inte vanlig choklad, som innehåller mycket '
              'socker och fett.',
        warnings=['Forskningen på människor är fortfarande begränsad och medelstor',
                  'Kan ge lätta sömnsvårigheter hos koffeinkänsliga personer om extraktet kommer från kakao eller te'],
        interactions='Generellt säkert; det kan förstärka blodtryckssänkande och blodförtunnande läkemedel något.',
        naturalSources='Rå kakao och mörk choklad (85 % eller mer), grönt te, äpplen och blå druvor.'),
    'phosphatidylserine': dict(
        summary='En naturlig fosfolipid som är en viktig byggsten i nervcellernas membran; den hjälper till att stödja '
                'signalöverföringen i nerverna och frisättningen av signalsubstanser, och studier tyder på att den '
                'begränsar kraftiga ökningar av stresshormonet kortisol vid fysisk och mental påfrestning.',
        dosage=dict(recommended='300–400 mg per dag',
                    timing='Fördelat på måltiderna, eller på kvällen för att stödja avslappning',
                    frequency='En gång per dag eller fördelat på flera doser'),
        forms='Fosfatidylserin från solros- eller sojalecitin, i stället för de äldre källorna från nötkreatur.',
        warnings=['Ett mycket säkert tillskott för långvarig användning',
                  'Höga doser sent på dagen kan ge lätt dåsighet eller störd sömn',
                  'Undvik produkter från soja om du har sojaallergi'],
        interactions='Kan interagera med antikolinerga läkemedel och läkemedel mot Alzheimers sjukdom '
                     '(kolinesterashämmare). Det kan göra blodet något mer lättflytande, så var försiktig med '
                     'antikoagulantia.',
        naturalSources='Sojabönor, vit fisk, kyckling, vita bönor och äggula.'),
    'sodium-bicarbonate': dict(
        summary='En syrabuffert som höjer halten av bikarbonat i vätskan runt muskelcellerna, påskyndar bortforslingen av de '
                'vätejoner som bildas vid hård anaerob ansträngning (sprint, simning, rodd) och därmed fördröjer '
                'muskeltröttheten.',
        dosage=dict(recommended='0,2–0,3 g per kg kroppsvikt (cirka 15–20 g vid 75 kg)',
                    timing='60–90 minuter före intensiv träning, upplöst i en liter vatten och drucket i små klunkar till '
                           'en kolhydratrik måltid',
                    frequency='Endast före intensiva pass, inte för daglig användning'),
        forms='Enterokapslar som frisätter bikarbonatet i tarmen och minskar magbesvären.',
        warnings=['Tas det snabbt på en gång ger det vattnig diarré, kramper och illamående; prova en låg dos under träning '
                  'före tävling',
                  'Inte för personer med högt blodtryck, njursvikt eller hjärtsvikt, på grund av den höga natriumhalten'],
        interactions='Den basiska urinen som det ger ändrar utsöndringen av vissa läkemedel (som acetylsalicylsyra och '
                     'amfetamin) och ökar utsöndringen av litium, vilket sänker halten i blodet; det kan lösa upp '
                     'enterotabletter för tidigt; använd det inte tillsammans med blodtryckssänkande eller vätskedrivande '
                     'läkemedel på grund av den höga natriumhalten.',
        naturalSources='Finns inte i maten i idrottsdoser; bikarbonat används i små mängder i matlagningen.'),
    'beetroot-nitrates': dict(
        summary='En växtkälla rik på nitrat; bakterier på tungan omvandlar det till nitrit, som kroppen omvandlar till '
                'kväveoxid i musklerna, vilket förbättrar syreutnyttjandet, sänker energikostnaden vid ansträngning och '
                'stödjer blodflödet.',
        dosage=dict(recommended='400–500 mg nitrat (cirka 70 ml koncentrerad rödbetsjuice)',
                    timing='2–3 timmar före aktivitet eller tävling',
                    frequency='En dos före tävling, eller dagligen i 3–6 dagar som laddningsfas'),
        forms='En standardiserad koncentrerad rödbetsshot; undvik antiseptiskt munvatten, som dödar bakterierna på tungan som '
              'omvandlar nitrat och tar bort effekten.',
        warnings=['Rosa eller röd urin och avföring (beturi) är normalt och ofarligt',
                  'Var försiktig om du har haft njursten, eftersom rödbetor innehåller oxalater'],
        interactions='Interagerar med blodtryckssänkande läkemedel, kärlvidgande läkemedel, nitrater mot hjärtsjukdom och '
                     'PDE5-hämmare (sildenafil) och kan sänka blodtrycket ytterligare.',
        naturalSources='Rödbetor, ruccola, spenat, selleri och sallat.'),
    'alpha-gpc': dict(
        summary='En kolinbärare som passerar blod-hjärnbarriären effektivare än vanliga kolinformer; den höjer acetylkolin, '
                'den viktigaste signalsubstansen för inlärning, minne och reaktionssnabbhet, och stödjer aktiveringen av '
                'musklernas motoriska enheter vid träning.',
        dosage=dict(recommended='300–600 mg per dag',
                    timing='På morgonen eller 45 minuter före mental eller fysisk ansträngning, med en lätt fettkälla',
                    frequency='1–2 gånger per dag'),
        forms='Standardiserade kapslar med 50 % eller 99 % renhet; håll förpackningen stängd, eftersom ämnet drar åt sig '
              'fukt kraftigt och snabbt klumpar sig.',
        warnings=['Höga doser kan ge lätt huvudvärk eller, i sällsynta fall, halsbränna',
                  'Observationsstudier tyder på att långvarig användning av höga doser kan höja blodets nivåer av TMAO; '
                  'används helst i perioder eller vid behov'],
        interactions='Kan motverka antikolinerga läkemedel och förstärka effekten av läkemedel mot Alzheimers sjukdom '
                     '(kolinesterashämmare).',
        naturalSources='Äggula, lever, kött, fisk och sojabönor (som källor till kolin).'),
    'bacopa-monnieri': dict(
        summary='En traditionell ayurvedisk ört vars aktiva ämnen (bacosider) stödjer signalöverföringen i nerverna och '
                'skyddar cellerna i hippocampus mot oxidativ stress; metaanalyser tyder på att den stödjer hastigheten i '
                'informationsbearbetningen och förmågan att minnas efter 6–12 veckors regelbunden användning.',
        dosage=dict(recommended='300–450 mg standardiserat extrakt (50–55 % bacosider)',
                    timing='Till en måltid som innehåller fett (frukost eller lunch)', frequency='En gång per dag'),
        forms='Kliniskt studerade extrakt standardiserade för bacosider (50–55 %), som Synapsa® eller Bacognize®.',
        warnings=['Kan ge illamående och tarmkramper på fastande mage; ta det alltid tillsammans med mat',
                  'Kan ge tröghet eller överdriven avslappning de första veckorna',
                  'Undvik under graviditet och amning eftersom säkerhetsdata är begränsade'],
        interactions='Kan förstärka effekten av kolinerga läkemedel och läkemedel mot Alzheimers sjukdom; det kan sänka '
                     'blodtrycket och pulsen något, så var försiktig med blodtryckssänkande läkemedel och betablockerare. '
                     'Det kan interagera med sköldkörtelläkemedel.',
        naturalSources='Örten bacopa (brahmi); används som standardiserat extrakt och finns inte i vardagsmat.'),
})

# second batch (51-100 in the data order), part 1
COPY.update({
    'milk-thistle': dict(
        summary='Innehåller ett flavonoidkomplex som kallas silymarin (främst silibinin); det hjälper till att skydda '
                'levercellernas membran mot oxidativ stress och stödjer glutationnivåerna, och laboratoriestudier tyder på '
                'att det stimulerar proteinsyntesen i levercellerna.',
        dosage=dict(recommended='150–300 mg standardiserat extrakt (80 % silymarin)', timing='Till huvudmåltiderna',
                    frequency='2–3 gånger per dag'),
        forms='Silibininfytosom, som tas upp flera gånger bättre än vanligt silymarin.',
        warnings=['Kan ha en lätt laxerande effekt de första dagarna',
                  'Bör undvikas under graviditet och amning eftersom säkerhetsdata är otillräckliga',
                  'Undvik det om du är allergisk mot korgblommiga växter (som ambrosia och kamomill)'],
        interactions='Mariatistel kan hämma leverenzymer (CYP2C9 och CYP3A4) och därmed höja blodnivåerna av vissa läkemedel, '
                     'till exempel warfarin och vissa statiner. Den kan förstärka blodsockersänkande läkemedel.',
        naturalSources='Frön av mariatistel (används som standardiserat extrakt).'),
    'fenugreek': dict(
        summary='Frön rika på löslig fiber (galaktomannan) och ämnet 4-hydroxiisoleucin; de hjälper till att bromsa '
                'magsäckens tömning och upptaget av kolhydrater, och metaanalyser tyder på att de stödjer glukosnivåerna. '
                'Används traditionellt för att stödja mjölkproduktionen och vitaliteten.',
        dosage=dict(recommended='500–600 mg standardiserat extrakt, eller 1–2 g fröpulver', timing='Till lunch och middag',
                    frequency='1–2 gånger per dag'),
        forms='Standardiserade, luktfria extrakt, eller kliniskt studerade extrakt som Testofen® för mäns vitalitet.',
        warnings=['Koncentrerade tillskott av bockhornsklöver får inte användas under graviditet, eftersom de kan utlösa '
                  'livmodersammandragningar',
                  'En lukt av lönnsirap i svett och urin är normal och ofarlig',
                  'Kan ge allergiska reaktioner hos personer som är allergiska mot jordnötter eller kikärter'],
        interactions='Bockhornsklöver förstärker insulin och diabetestabletter; kontrollera blodsockret för att undvika '
                     'hypoglykemi. Den kan interagera med blodförtunnande läkemedel (warfarin).',
        naturalSources='Frön och blad av bockhornsklöver (används i matlagning och traditionella drycker).'),
    'tribulus-terrestris': dict(
        summary='En traditionell växt vars frukt innehåller saponiner, främst protodioscin; forskning tyder på en stödjande '
                'roll för lust och vitalitet, utan bekräftade kliniska belägg för att den höjer testosteronet hos friska män '
                'med normala nivåer.',
        dosage=dict(recommended='500–1000 mg (45–90 % totala saponiner)', timing='Mitt i en måltid',
                    frequency='Fördelat på 1–2 doser per dag'),
        forms='Extrakt standardiserade för protodioscin (minst 20–40 %); undvik ostandardiserade pulver av rå ört.',
        warnings=['Kan ge magbesvär eller sura uppstötningar; ta det tillsammans med mat',
                  'Undvik det vid förstorad prostata eller hormonkänslig prostatacancer',
                  'Ska inte användas under graviditet eller amning'],
        interactions='Kan sänka blodtrycket och blodsockret; var försiktig med blodtryckssänkande och blodsockersänkande '
                     'läkemedel.',
        naturalSources='Frukten av Tribulus terrestris (används som extrakt); finns inte i vardagsmat.'),
    'saw-palmetto': dict(
        summary='Rik på fria fettsyror och fytosteroler som hämmar 5-alfa-reduktas, enzymet som omvandlar testosteron till '
                'DHT; den används för att stödja ett normalt urinflöde hos äldre män, men en Cochraneöversikt från 2012 fann '
                'ingen tydlig skillnad mot placebo för urinvägsbesvär.',
        dosage=dict(recommended='160–320 mg standardiserat liposterolt extrakt (85–95 % fettsyror)',
                    timing='Till en måltid som innehåller fett', frequency='En gång per dag eller fördelat på flera doser'),
        forms='Mjukkapslar med standardiserat liposterolt extrakt (85–95 % fettsyror) framställt med superkritisk '
              'koldioxidextraktion, i stället för kapslar med torkat bärpulver.',
        warnings=['Ersätter inte regelbundna läkarkontroller av prostata för att utesluta allvarliga tillstånd',
                  'Kan ge lätta magbesvär eller, i sällsynta fall, yrsel; ta det tillsammans med mat',
                  'Endast för vuxna män'],
        interactions='Sågpalmetto kan störa hormonella läkemedel och prostataläkemedel (som finasterid och dutasterid). Den '
                     'kan förlänga blödningstiden något, så var försiktig med blodförtunnande läkemedel.',
        naturalSources='Bär av sågpalmetto (används som liposterolt extrakt); finns inte i vardagsmat.'),
    'maca-root-extract': dict(
        summary='En rotknöl från Anderna som innehåller makamider; små studier tyder på att den stödjer energi, '
                'sinnesstämning, lust och motståndskraft mot trötthet, utan direkt effekt på könshormonnivåerna i blodet.',
        dosage=dict(recommended='1500–3000 mg per dag', timing='På morgonen till frukost (undvik det på kvällen)',
                    frequency='En gång per dag'),
        forms='Gelatiniserad maca, som värmts försiktigt för att ta bort stärkelsen så att den blir lättare att smälta; '
              'finns som svart och röd maca.',
        warnings=['Kan ge sömnsvårigheter om den tas på kvällen',
                  'Bör av försiktighetsskäl undvikas vid östrogenkänsliga tumörer (som bröst- och livmodercancer)'],
        interactions='Säkert med de flesta läkemedel; var försiktig med sköldkörtelläkemedel, eftersom den råa roten '
                     'innehåller strumogena ämnen.',
        naturalSources='Kokt eller pulvriserad macarot (ett traditionellt livsmedel i Peru).'),
    'vitamin-e': dict(
        summary='Den viktigaste fettlösliga antioxidanten i cellmembranen; E-vitamin bidrar till att skydda cellerna mot '
                'oxidativ stress (EFSA-godkänt påstående) genom att stoppa kedjereaktioner som oxiderar omättade fetter i '
                'membranen.',
        dosage=dict(recommended='100–200 IE (cirka 67–134 mg d-alfa-tokoferol)', timing='Till en huvudmåltid som innehåller fett',
                    frequency='En gång per dag'),
        forms='Den naturliga formen (d-alfa-tokoferol) med blandade tokoferoler och tokotrienoler; undvik den mindre '
              'effektiva syntetiska formen (dl-alfa-tokoferol).',
        warnings=['EFSA:s övre gräns för vuxna är 300 mg per dag (cirka 450 IE)',
                  'I en metaanalys var höga doser (400 IE eller mer) kopplade till högre dödlighet, och de motverkar '
                  'K-vitaminets roll i blodets koagulation',
                  'Sluta ta det två veckor före en operation'],
        interactions='Varning för blödning: E-vitamin interagerar med blodförtunnande läkemedel och antikoagulantia '
                     '(warfarin, acetylsalicylsyra) och kan ge blödningar vid höga doser.',
        naturalSources='Vetegroddsolja, solrosfrön, mandlar, hasselnötter, avokado och spenat.'),
    'vitamin-k2': dict(
        summary='K-vitamin bidrar till normal blodkoagulering och till att bibehålla normal benstomme (EFSA-godkända '
                'påståenden); det aktiverar osteokalcin, som binder kalcium i benvävnaden, och matrix-GLA-protein, som '
                'begränsar kalkavlagringar i artärväggarna.',
        dosage=dict(recommended='90–180 µg per dag', timing='Till en måltid som innehåller fett, gärna tillsammans med D3-vitamin',
                    frequency='En gång per dag'),
        forms='Naturligt menakinon-7 (MK-7) från natto eller fermentering (som MenaQ7®), med en halveringstid i blodet på '
              'upp till 72 timmar jämfört med några timmar för MK-4.',
        warnings=['Får absolut inte användas av personer som tar K-vitaminantagonister (warfarin, acenokumarol)',
                  'Det påverkar inte de nyare antikoagulantia (som apixaban och rivaroxaban), men berätta alltid för din läkare'],
        interactions='Varning vid antikoagulantia: K2-vitamin försvagar K-vitaminantagonister (warfarin, acenokumarol) och '
                     'ökar risken för blodproppar; kombinera dem inte.',
        naturalSources='Natto (fermenterade sojabönor), lagrade ostar, äggula och lever.'),
    'selenium': dict(
        summary='Ett spårämne som ingår i ett 25-tal selenoproteiner, bland annat det antioxidativa enzymet '
                'glutationperoxidas och de enzymer som omvandlar sköldkörtelhormonet T4 till T3; selen bidrar till '
                'immunsystemets normala funktion, till normal sköldkörtelfunktion och till att skydda cellerna mot oxidativ '
                'stress (EFSA).',
        dosage=dict(recommended='55–100 µg per dag', timing='Till frukost eller lunch', frequency='En gång per dag'),
        forms='L-selenometionin eller selenjäst, med ett upptag på över 90 % jämfört med oorganiskt selenit och selenat.',
        warnings=['EFSA:s uppdaterade övre gräns (2023): 255 µg per dag från alla källor för vuxna',
                  'Selenförgiftning ger vitlöksandedräkt, håravfall och sköra naglar',
                  'Undvik höga doser under lång tid utan provtagning'],
        interactions='Selen kan störa vissa cytostatika och kombinationen statin–niacin; rådgör med din läkare. Det finns '
                     'ingen bevisad konflikt med C-vitamin i måttliga doser.',
        naturalSources='Paranötter (en nöt kan innehålla 50–90 µg), fisk och skaldjur, ägg och kött.'),
    'chromium-picolinate': dict(
        summary='Krom bidrar till att bibehålla normala blodsockernivåer och till normal omsättning av makronäringsämnen '
                '(EFSA-godkända påståenden); det ingår i kromodulin, som förstärker insulinets bindning till sina '
                'receptorer på cellerna.',
        dosage=dict(recommended='200–400 µg per dag', timing='Till en måltid som innehåller kolhydrater',
                    frequency='En gång per dag'),
        forms='Krompikolinat, där trevärt krom är bundet till pikolinsyra för bättre upptag än kromklorid.',
        warnings=['EFSA har inte fastställt någon formell övre gräns för trevärt krom; överskrid inte den rekommenderade '
                  'dosen utan uppföljning',
                  'Stora doser är inte för personer med njur- eller leversvikt'],
        interactions='Krom ökar insulinkänsligheten och effekten av blodsockersänkande läkemedel; följ dina värden om du tar '
                     'insulin eller sulfonylureider, för att undvika hypoglykemi.',
        naturalSources='Broccoli, fullkorn, kött, ägg, baljväxter och kaffe.'),
    'iodine': dict(
        summary='Den nödvändiga byggstenen i sköldkörtelhormonerna (T4 och T3); jod bidrar till normal produktion av '
                'sköldkörtelhormoner och normal sköldkörtelfunktion, till normal energiomsättning och till nervsystemets '
                'normala funktion (EFSA).',
        dosage=dict(recommended='150–225 µg per dag (vuxnas behov är 150 µg, 200 µg under graviditet och amning enligt EFSA)',
                    timing='Till frukost', frequency='En gång per dag'),
        forms='Exakt doserat kaliumjodid, eller ekologiskt kelpextrakt som är standardiserat och testat för jämn dos och '
              'frihet från arsenik.',
        warnings=['EFSA:s övre gräns för vuxna är 600 µg per dag',
                  'Överskott är farligt vid autoimmun sköldkörtelinflammation (Hashimotos sjukdom) och knölstruma, eftersom '
                  'det kan hämma körteln eller utlösa överfunktion',
                  'Ostandardiserade kelpprodukter kan innehålla mycket varierande mängder jod'],
        interactions='Jod interagerar med tyreostatika, litium, kaliumsparande diuretika och ACE-hämmare; rådgör med din läkare.',
        naturalSources='Havsfisk och skaldjur, alger, mejeriprodukter, ägg och joderat salt.'),
    'nac': dict(
        summary='Ett derivat av den svavelhaltiga aminosyran L-cystein och den begränsande faktorn för bildningen av '
                'cellernas antioxidant glutation i lever och lungor; dess fria svavelgrupper hjälper till att lösa upp segt '
                'slem och stödjer andningsvägarnas komfort.',
        dosage=dict(recommended='600–1200 mg per dag',
                    timing='På fastande mage med ett helt glas vatten, eller till ett lätt mellanmål för att undvika halsbränna',
                    frequency='Fördelat på två doser'),
        forms='Rena kapslar med NAC i fri form; en lätt svavellukt är normal och visar att de aktiva tiolgrupperna finns kvar.',
        warnings=['Kan ge illamående och lätt halsbränna; ta det med två glas vatten',
                  'Inte för personer med cysteinallergi eller sällsynta cystinnjurstenar'],
        # the record's general line (a medicine in some European countries) is left out (approved 2026-10-26):
        # the Swedish one is in EXTRA_WARNINGS
        interactions='Varning vid kärlkrampsläkemedel: NAC interagerar med nitroglycerin och andra nitrater och kan ge ett '
                     'kraftigt blodtrycksfall och svår huvudvärk. Ta det med två timmars mellanrum från antibiotika som tas '
                     'via munnen och från medicinskt kol.',
        naturalSources='NAC i sig finns inte i maten; cystein kommer från fågel, ägg, baljväxter, vitlök och lök.'),
    'msm': dict(
        summary='En organisk svavelförening som ger det svavel som behövs för disulfidbindningar i kollagen- och '
                'keratinfibrer och stödjer bindväven i brosk och leder; studier tyder på att MSM dämpar markörer för '
                'oxidativ stress efter träning.',
        dosage=dict(recommended='1500–3000 mg per dag; börja med 1000 mg och öka gradvis',
                    timing='Till frukost och lunch med ett helt glas vatten', frequency='Fördelat på två doser'),
        forms='MSM-pulver eller kapslar destillerat i flera steg (som OptiMSM®) för garanterad renhet och frihet från '
              'tungmetaller.',
        warnings=['Säkert upp till 4 g per dag',
                  'Kan ge gaser eller lös avföring i början',
                  'Bör undvikas på kvällen, eftersom det kan ge livliga drömmar hos vissa'],
        interactions='Inga större läkemedelsinteraktioner har rapporterats; var försiktig med blodförtunnande läkemedel vid '
                     'doser över 4 g.',
        naturalSources='Små mängder i mjölk, kaffe, tomater och bladgrönsaker.'),
    'quercetin': dict(
        summary='En växtflavonoid som finns i lök och äpplen; den verkar som antioxidant, och laboratoriestudier tyder på '
                'att den stabiliserar mastcellerna (dämpar frisättningen av histamin) och hjälper till att föra zink genom '
                'cellmembranen.',
        dosage=dict(recommended='250–500 mg fytosom (eller 500–1000 mg kvercetindihydrat)',
                    timing='Till en måltid som innehåller nyttigt fett', frequency='En gång per dag eller fördelat på flera doser'),
        forms='Kvercetinfytosom bundet till fosfolipider (som Quercefit®), som tas upp upp till 20 gånger bättre än rått pulver.',
        warnings=['Säkert upp till 1000 mg per dag i 12 veckor',
                  'Kontinuerligt höga doser rekommenderas inte vid njursvikt',
                  'Bör undvikas under graviditet och amning'],
        interactions='Kvercetin hämmar CYP3A4 och P-gp och kan därför höja blodnivåerna av kalciumkanalblockerare, '
                     'ciklosporin och antikoagulantia. Det kan interagera med fluorokinolonantibiotika.',
        naturalSources='Rödlök, äpplen med skal, kapris, bär, te och broccoli.'),
    'resveratrol': dict(
        summary='En polyfenol ur fytoalexinfamiljen; forskning tyder på att den aktiverar sirtuiner (särskilt SIRT1), som är '
                'kopplade till mitokondriernas effektivitet, och hjälper till att stödja blodkärlsväggens elasticitet och '
                'blodflödet.',
        dosage=dict(recommended='Upp till 150 mg trans-resveratrol per dag (EU:s godkända maxdos)',
                    timing='Till frukost eller en lätt måltid som innehåller fett', frequency='En gång per dag'),
        forms='98 % rent trans-resveratrol från japansk pilört (Polygonum cuspidatum); trans-formen är den biologiskt aktiva.',
        warnings=['EU godkänner trans-resveratrol som nytt livsmedel upp till 150 mg per dag för vuxna',
                  'Stora doser (över 1000 mg) ger illamående och diarré',
                  'Inte för personer med östrogenkänsliga tumörer, eller under graviditet och amning'],
        interactions='Resveratrol hämmar blodplättarna; var försiktig med blodförtunnande läkemedel (warfarin, '
                     'acetylsalicylsyra). Det kan sänka blodsockret, så var försiktig med diabetesläkemedel.',
        naturalSources='Skalet på röda druvor, blåbär, jordnötter och kakao.'),
    'berberine': dict(
        summary='En växtalkaloid från berberisrot som aktiverar AMPK, cellernas viktigaste energisensor; den hjälper till att '
                'stödja musklernas insulinkänslighet, minska leverns glukosproduktion och stödja normala nivåer av '
                'kolesterol och triglycerider.',
        dosage=dict(recommended='500 mg per dos (högst 1000–1500 mg per dag); börja med 500 mg per dag',
                    timing='15–30 minuter före måltiderna', frequency='2–3 gånger per dag'),
        forms='Berberin-HCl (97 %), eller nyare fytosomberedningar som höjer det naturligt låga upptaget.',
        warnings=['Får absolut inte användas under graviditet eller amning: det passerar moderkakan och går över i '
                  'bröstmjölken och kan orsaka kärnikterus hos ofödda och ammade barn',
                  'Kan ge tillfälliga tarmkramper och diarré',
                  'Använd det inte i stället för förskrivna diabetesläkemedel'],
        interactions='Allvarlig interaktion: berberin hämmar leverenzymerna CYP3A4 och CYP2D6 och interagerar med '
                     'blodsockersänkande läkemedel (risk för svår hypoglykemi tillsammans med insulin), statiner, '
                     'blodtryckssänkande läkemedel och immunhämmande läkemedel (ciklosporin, takrolimus). Det är nödvändigt '
                     'att rådgöra med läkare.',
        naturalSources='Rötterna av berberis och Hydrastis canadensis (goldenseal); finns inte i vardagsmat.'),
    'pqq': dict(
        summary='En redoxkofaktor som enligt studier kan stimulera bildningen av nya mitokondrier i cellerna via '
                'CREB-signalvägen och PGC-1alfa, och som hjälper till att skydda hjärnans och hjärtats celler mot oxidativ '
                'stress och stödja den mentala energin.',
        dosage=dict(recommended='10–20 mg per dag (EU:s godkända maxdos är 20 mg)', timing='Till frukost',
                    frequency='En gång per dag'),
        forms='Fermenterat PQQ-dinatriumsalt som är godkänt som nytt livsmedel i EU (som BioPQQ®), ofta kombinerat med Q10.',
        warnings=['Håll dig till EU:s godkända gräns på högst 20 mg per dag',
                  'Säkerheten är inte fastställd under graviditet, amning eller före 18 års ålder'],
        interactions='Inga större läkemedelsinteraktioner har rapporterats vid de godkända doserna.',
        naturalSources='Spårmängder i natto, persilja, grön paprika, kiwi och grönt te.'),
    'alpha-lipoic-acid': dict(
        summary='En svavelförening som löser sig i både vatten och fett och därför skyddar cellerna både inifrån och utifrån; '
                'den återvinner andra antioxidanter (C- och E-vitamin och glutation) och hjälper till att stödja '
                'mikrocirkulationen till de perifera nerverna och glukosomsättningen.',
        dosage=dict(recommended='300–600 mg per dag',
                    timing='På fastande mage 30 minuter före maten med mycket vatten (mat minskar upptaget)',
                    frequency='1–2 gånger per dag'),
        forms='Stabiliserad natrium-R-alfaliponsyra (Na-R-ALA), den form som finns i kroppen och som tas upp bättre än den '
              'syntetiska blandningen (RS-ALA).',
        warnings=['I sällsynta fall kan den utlösa insulinautoimmunt syndrom (Hirata sjukdom) hos genetiskt mottagliga '
                  'personer, med svåra episoder av hypoglykemi',
                  'Kan ge halsbränna',
                  'Undvik den vid svår brist på B1-vitamin (till exempel vid hög alkoholkonsumtion) om inte tiamin ersätts'],
        interactions='Alfaliponsyra ökar insulinkänsligheten och sänker blodsockret; diabetesläkemedel bör justeras under '
                     'medicinsk uppföljning. Ta den med fyra timmars mellanrum från levotyroxin.',
        naturalSources='Små mängder i spenat, broccoli, tomater, rött kött och lever.'),
    'boron': dict(
        summary='Ett spårämne som deltar i omsättningen av viktiga mineraler; studier tyder på att bor minskar förlusterna av '
                'kalcium och magnesium via urinen, förlänger livslängden hos aktivt D-vitamin och stödjer bildningen av '
                'benmatrix och ledernas rörlighet.',
        dosage=dict(recommended='3–6 mg elementärt bor per dag (överskrid inte 6 mg utan medicinsk rådgivning)',
                    timing='Till en måltid', frequency='En gång per dag'),
        forms='Borglycinat, borcitrat eller boroglukonat; undvik oorganiska föreningar som borsyra och natriumborat.',
        warnings=['EFSA:s övre gräns för vuxna är 10 mg per dag från alla källor',
                  'Långvarigt överskott kan ge reproduktionstoxiska effekter och belasta njurarna',
                  'Inte för personer med hormonkänslig cancer eller under graviditet'],
        interactions='Bor kan höja nivåerna av fritt östrogen och testosteron något; var försiktig vid '
                     'hormonersättningsbehandling.',
        naturalSources='Katrinplommon, russin, avokado, nötter, baljväxter och äpplen.'),
    'pycnogenol': dict(
        summary='Ett standardiserat extrakt av bark från fransk kusttall, rikt på procyanidiner (OPC); det hjälper till att '
                'stödja bildningen av kväveoxid i artärernas inre vägg, vilket stödjer elastiska blodkärl och '
                'mikrocirkulationen, och hjälper till att stabilisera kollagen- och elastinfibrer.',
        dosage=dict(recommended='100–200 mg per dag (65–75 % procyanidiner)',
                    timing='Till frukost och lunch med ett glas vatten', frequency='Fördelat på två doser'),
        forms='Det registrerade extraktet Pycnogenol®, standardiserat till 65–75 % procyanidiner, eller ett likvärdigt '
              'extrakt av kusttallbark.',
        warnings=['Kan ge magbesvär eller kortvarig yrsel på fastande mage',
                  'Undvik det under graviditetens första tredjedel och rådgör med läkare därefter',
                  'Rådgör med läkare om du har en autoimmun sjukdom'],
        interactions='Pycnogenol vidgar blodkärlen och hämmar blodplättarna; var försiktig med blodförtunnande läkemedel, '
                     'antikoagulantia och blodtryckssänkande läkemedel. Det kan sänka blodsockret något.',
        naturalSources='Bark från kusttall (används som extrakt); procyanidiner finns också i druvkärnor, äpplen och kakao.'),
    'lutein-zeaxanthin': dict(
        summary='Gula karotenoidpigment som koncentreras i gula fläcken (makula) och ögats lins; de fungerar som ett naturligt '
                'filter mot högenergetiskt blått ljus och hjälper till att skydda fotoreceptorerna mot oxidativ stress.',
        dosage=dict(recommended='10–20 mg lutein + 2–4 mg zeaxantin per dag',
                    timing='Till en måltid som innehåller nyttigt fett, till exempel olivolja eller avokado',
                    frequency='En gång per dag'),
        forms='Fritt lutein från ringblommor med zeaxantin i förhållandet 5:1, som i studien AREDS2.',
        warnings=['Säkert för långvarig användning',
                  'Kontinuerligt för höga doser kan ge en lätt gul ton i handflator och fotsulor, vilket är ofarligt och går '
                  'över när dosen minskas'],
        interactions='Inga större läkemedelsinteraktioner har rapporterats; ta det med två timmars mellanrum från orlistat '
                     '(som blockerar fettupptaget) för att säkra upptaget.',
        naturalSources='Grönkål, spenat, äggula, majs, orange paprika och ärter.'),
    'moringa': dict(
        summary='Blad med hög näringstäthet av vitaminer, mineraler och polyfenoler (som rutin och klorogensyra); de hjälper '
                'till att skydda cellerna mot oxidativ stress och stödjer en normal omsättning av kolhydrater och fett och '
                'vardagens vitalitet.',
        dosage=dict(recommended='1000–2000 mg (pulver eller kapslar)', timing='Till frukost eller lunch',
                    frequency='1–2 gånger per dag'),
        forms='Kapslar eller pulver av ekologiska moringablad som torkats i skugga, för att bevara klorofyllet och de '
              'ljuskänsliga vitaminerna.',
        warnings=['Använd endast produkter av bladen och undvik helt tillskott av moringarot och moringabark, eftersom de '
                  'innehåller giftiga alkaloider (som spirochin)',
                  'Ska inte användas under graviditet, eftersom den kan utlösa livmodersammandragningar'],
        interactions='Moringa kan förstärka blodsockersänkande, blodtryckssänkande och sköldkörtelläkemedel; följ dina värden '
                     'och justera doserna under medicinsk uppföljning.',
        naturalSources='Färska moringablad (tillagas som grönsak i Asien och Afrika) och moringaskidor.'),
    'cordyceps': dict(
        summary='En traditionell svamp rik på cordycepin; studier tyder på att den stödjer cellernas energiproduktion (ATP) '
                'och syreutnyttjandet vid träning, vilket stödjer motståndskraften mot fysisk trötthet och uthålligheten.',
        dosage=dict(recommended='1000–2000 mg standardiserat extrakt', timing='På morgonen eller 45 minuter före träning',
                    frequency='1–2 gånger per dag'),
        forms='Extrakt av fruktkroppen av Cordyceps militaris med minst 0,3 % cordycepin, eller den laboratoriefermenterade '
              'stammen CS-4; undvik förorenad vildplockad svamp.',
        warnings=['Undvik den vid blödningsrubbningar och sluta två veckor före en operation',
                  'Använd den inte vid aktiv autoimmun sjukdom utan medicinsk rådgivning',
                  'Ska inte användas under graviditet eller amning'],
        interactions='Cordyceps är lätt blodförtunnande och immunstimulerande; var försiktig med antikoagulantia (warfarin) '
                     'och immunhämmande läkemedel, och följ dina värden vid diabetesläkemedel.',
        naturalSources='Odlad cordycepssvamp (används som extrakt); finns inte i vardagsmat.'),
    'reishi-mushroom': dict(
        summary='En traditionell svamp i asiatisk medicin, rik på betaglukaner och triterpener (ganodersyror); den hjälper '
                'till att stödja immunförsvarets normala svar och fungerar som adaptogen som hjälper till att lugna '
                'nervsystemet och stödja sömnkvaliteten.',
        dosage=dict(recommended='1000–1500 mg standardiserat dubbelextrakt', timing='En timme före sänggåendet eller till middagen',
                    frequency='En gång per dag'),
        forms='Dubbelextrakt (varmt vatten och alkohol) av fruktkroppen av röd reishi, som fångar både polysackariderna och '
              'triterpenerna.',
        warnings=['Kan ge dåsighet; undvik att köra bil efter intag',
                  'Sällsynta fall av leverbelastning har rapporterats med opålitliga råa pulver; håll dig till testade '
                  'extrakt och kontrollera leverfunktionen vid långvarig användning',
                  'Undvik under graviditet och amning och före en operation'],
        interactions='Reishi interagerar med blodförtunnande läkemedel och antikoagulantia (förlänger blödningstiden), '
                     'blodtryckssänkande läkemedel, immunhämmande läkemedel och diabetesläkemedel.',
        naturalSources='Reishisvamp (används som extrakt eller te); finns inte i vardagsmat.'),
    'holy-basil-tulsi': dict(
        summary='En traditionell ayurvedisk adaptogen rik på eugenol, ursolsyra och rosmarinsyra; den hjälper till att '
                'stödja kroppens förmåga att anpassa sig till mental och metabol stress och stödjer mental avslappning och en '
                'klar sinnesstämning utan att göra dig dåsig.',
        dosage=dict(recommended='300–600 mg standardiserat extrakt (2,5 % ursolsyra), eller 2–3 koppar tulsite',
                    timing='Mellan eller till måltiderna', frequency='1–2 gånger per dag'),
        forms='Kapslar med extrakt standardiserat för ursolsyra (2,5 %), eller torkade ekologiska tulsiblad till te.',
        warnings=['Djurstudier har visat en fertilitetshämmande effekt; ska inte användas under graviditet, amning eller när '
                  'du försöker bli gravid',
                  'Kan sänka blodsockret'],
        interactions='Helig basilika kan sänka blodsockret; följ dina värden vid diabetesläkemedel. Den kan bromsa '
                     'blodplättarnas klumpning, så var försiktig med blodförtunnande läkemedel och antikoagulantia.',
        naturalSources='Färska eller torkade blad av helig basilika (används som te i Indien).'),
    'astaxanthin': dict(
        summary='En naturlig röd karotenoid som bildas av mikroalgen Haematococcus; dess molekylstruktur gör att den kan '
                'sträcka sig genom hela cellmembranet och fånga fria radikaler utan att själv bli prooxidant, och den '
                'hjälper till att stödja hudens fuktighet och elasticitet, skyddet mot oxidativ stress och musklernas '
                'återhämtning.',
        dosage=dict(recommended='4–8 mg per dag (EU:s godkända maxdos är 8 mg)',
                    timing='Till en måltid som innehåller nyttigt fett', frequency='En gång per dag'),
        forms='Naturligt astaxantin från algen Haematococcus pluvialis (som AstaReal®) i oljekapslar; undvik syntetiskt '
              'astaxantin som är framställt för fiskfoder.',
        warnings=['Håll dig till EU:s godkända gräns på högst 8 mg per dag',
                  'Höga doser kan ge avföringen en rödaktig färg, vilket är ofarligt',
                  'Rekommenderas inte under graviditet och amning eftersom data är begränsade'],
        interactions='Generellt säkert; det kan förstärka blodtryckssänkande och blodförtunnande läkemedel något, och rådgör '
                     'med läkare om du tar 5-alfa-reduktashämmare.',
        naturalSources='Vildlax, öring, räkor, hummer och krabba.'),
})

# second batch, part 2
COPY.update({
    'd-aspartic-acid': dict(
        summary='En isomer av asparaginsyra som koncentreras i hypofysen och testiklarna; studier tyder på att den stimulerar '
                'frisättningen av luteiniserande hormon (LH) och kan stödja testosteronsyntesen hos män med låga nivåer, '
                'medan effekten är tillfällig eller uteblir hos idrottare med normala nivåer.',
        dosage=dict(recommended='3 g per dag', timing='På morgonen på fastande mage med ett glas vatten',
                    frequency='I perioder: 12–14 dagar med, sedan ett helt uppehåll på 2–3 veckor'),
        forms='Rent pulver av D-asparaginsyra, eller blandningar som kombinerar den med zink och B6-, B12- och D3-vitamin.',
        warnings=['Det är viktigt att följa perioderna med och utan; kontinuerlig användning i mer än en månad kan i stället '
                  'sänka hormonnivåerna',
                  'Inte för personer under 18 år, kvinnor eller gravida'],
        interactions='Säkert med de flesta läkemedel; kombinera det inte med testosteronersättning (TRT) eller '
                     'östrogenhämmare.',
        naturalSources='Mycket små mängder i kött, ägg och mejeriprodukter.'),
    'apigenin': dict(
        summary='En växtflavonoid som finns rikligt i kamomill och persilja; den binder till GABA-A-receptorer i '
                'nervsystemet, vilket hjälper till att lugna överdriven nervaktivitet och stödjer avslappning och vilsam sömn.',
        dosage=dict(recommended='50–100 mg per dag', timing='30–60 minuter före sänggåendet', frequency='En gång per dag'),
        forms='Standardiserade apigeninkapslar (98 % renhet) utvunna ur kamomillblommor, eller lipidextrakt för bättre upptag.',
        warnings=['Ger dåsighet; kör inte bil och använd inte maskiner efter intag',
                  'Undvik koncentrerade doser under graviditet och amning',
                  'Undvik det om du är allergisk mot kamomill eller korgblommiga växter'],
        interactions='Apigenin förstärker lugnande medel, sömnmedel och ångestdämpande läkemedel. Det kan hämma CYP2C9 '
                     'något, så var försiktig med warfarin och läkemedel mot epilepsi.',
        naturalSources='Kamomill, persilja, selleri, timjan och apelsiner.'),
    'carnosine': dict(
        summary='En naturlig dipeptid av beta-alanin och L-histidin som koncentreras i hjärnan och musklerna; studier tyder '
                'på att den begränsar sockrets reaktion med proteiner (glykering) och bildningen av avancerade '
                'glykeringsslutprodukter (AGE), och den fungerar som pH-buffert i vävnaderna och som antioxidant.',
        dosage=dict(recommended='500–1000 mg per dag', timing='En halvtimme före huvudmåltiderna',
                    frequency='Fördelat på två doser'),
        forms='Rent L-karnosinpulver eller kapslar, eller zinkkarnosin för att stödja magslemhinnan.',
        warnings=['En del av karnosinet som tas via munnen bryts ned i blodet av enzymet karnosinas',
                  'Måttliga doser är säkra och ger inte de stickningar i huden som är kända från beta-alanin'],
        interactions='Inga större läkemedelsinteraktioner har rapporterats vid de vanliga doserna.',
        naturalSources='Rött kött, fågel och fisk (finns inte i vegetabiliska livsmedel).'),
    'l-ornithine': dict(
        summary='En aminosyra som inte bygger protein och som står i centrum för ureacykeln i levern; den hjälper till att '
                'omvandla ammoniak från proteinomsättning och muskelarbete till urea som lämnar kroppen med urinen, och en '
                'klinisk studie tyder på att den lindrar trötthet och stödjer sömnkvaliteten.',
        dosage=dict(recommended='2–3 g per dag (upp till 4 g)',
                    timing='En timme före sänggåendet på fastande mage, eller efter hård träning', frequency='En gång per dag'),
        forms='Rent L-ornitinhydroklorid, ibland kombinerat med L-arginin.',
        warnings=['Stora engångsdoser (mer än 7 g) kan ge magkramper och diarré',
                  'Inte för personer med den sällsynta ärftliga bristen på ornitinaminotransferas',
                  'Undvik under graviditet och amning'],
        interactions='Säkert med de flesta läkemedel; ta det med två timmars mellanrum från läkemedel mot epilepsi.',
        naturalSources='Kroppen bildar det av arginin; små mängder finns i kött, fisk, ägg och mejeriprodukter.'),
    'glycine': dict(
        summary='Naturens enklaste aminosyra; den fungerar som hämmande signalsubstans och hjälper till att sänka kroppens '
                'kärntemperatur genom att vidga de perifera blodkärlen, en fysiologisk signal för djup sömn, och den utgör '
                'ungefär en tredjedel av kollagenet i leder och senor.',
        dosage=dict(recommended='3–5 g upplöst i ett glas vatten', timing='En timme före sänggåendet',
                    frequency='En gång per dag'),
        forms='Rent glycinpulver i fri form med livsmedelskvalitet; det löser sig lätt och smakar naturligt sött.',
        warnings=['Mycket säkert i de vanliga doserna',
                  'Kan ge kraftig avslappning; ta det inte under dagen eller innan du kör bil'],
        interactions='Glycin kan förstärka lugnande medel och ångestdämpande läkemedel och kan minska effekten av klozapin.',
        naturalSources='Gelatin och benbuljong, fågelskinn, kött, fisk och baljväxter.'),
    'l-tryptophan': dict(
        summary='En essentiell aminosyra och det direkta förstadiet till serotonin och sömnhormonet melatonin; den hjälper '
                'till att stödja en stabil sinnesstämning och minska täta uppvaknanden under natten.',
        dosage=dict(recommended='500–1000 mg per dag',
                    timing='30–60 minuter före sänggåendet på fastande mage med en klunk juice', frequency='En gång per dag'),
        forms='Kapslar med L-tryptofan i fri form av farmaceutisk renhet (Ph. Eur.), framställt genom fermentering och '
              'testat fritt från föroreningar.',
        warnings=['Ska inte användas under graviditet, amning eller vid svår lever- eller njursjukdom',
                  'Rådgör med din läkare före användning om du tar något psykiatriskt eller neurologiskt läkemedel',
                  'Kan ge dåsighet; kör inte bil efter intag'],
        interactions='Viktig varning (serotonergt syndrom): kombinera det aldrig med antidepressiva läkemedel (SSRI, SNRI, '
                     'MAO-hämmare), johannesört, tramadol eller triptaner, för att undvika en livshotande ansamling av serotonin.',
        naturalSources='Kalkon och kyckling, ägg, ost, havre, pumpafrön och sojabönor.'),
    'citrulline-malate': dict(
        summary='En kombination av L-citrullin och äppelsyra i förhållandet 2:1; citrullin höjer arginin och kväveoxid för '
                'att stödja blodflödet, medan äppelsyran går in i citronsyracykeln och stödjer energiproduktionen, vilket '
                'hjälper dig att klara extra repetitioner vid hård träning.',
        dosage=dict(recommended='6–8 g upplöst i vatten', timing='30–45 minuter före träning',
                    frequency='En gång före träningen'),
        forms='Kontrollera att förhållandet mellan citrullin och malat är dokumenterat till 2:1 och undvik produkter med 1:1.',
        warnings=['Syran kan ge halsbränna hos personer med magkatarr eller aktivt magsår; drick det med mycket vatten'],
        interactions='Citrullinmalat interagerar med nitrater mot hjärtsjukdom, PDE5-hämmare (sildenafil, tadalafil) och '
                     'blodtryckssänkande läkemedel och kan ge ett blodtrycksfall.',
        naturalSources='Vattenmelon (särskilt det vita skalet), gurka och squash.'),
    'choline-bitartrate': dict(
        summary='Kolin bidrar till normal fettomsättning, till att bibehålla normal leverfunktion och till normal '
                'homocysteinomsättning (EFSA-godkända påståenden); det är byggstenen i signalsubstansen acetylkolin och i '
                'lecitin, som transporterar fett ut ur levern.',
        dosage=dict(recommended='500–1000 mg per dag', timing='Till frukost eller lunch', frequency='1–2 gånger per dag'),
        forms='Ett prisvärt val för att stödja levern; fosfolipidformer (som alfa-GPC och citikolin) passerar '
              'blod-hjärnbarriären effektivare.',
        warnings=['EFSA har inte fastställt någon övre gräns för kolin; den amerikanska övre gränsen (NIH) är 3500 mg per dag '
                  'från alla källor',
                  'För höga doser ger fisklukt från kroppen, diarré och lågt blodtryck'],
        interactions='Säkert med de flesta läkemedel; det kan störa antikolinerga läkemedel något.',
        naturalSources='Ägg (särskilt gulan), lever, kött, fisk, sojabönor och broccoli.'),
    'phosphatidylcholine': dict(
        summary='Den viktigaste fosfolipiden i cell- och mitokondriemembranen; den ger kolin i en mycket biotillgänglig form '
                'och hjälper till att emulgera fett i maten, stödja gallflödet och bevara membranen i lever- och nervceller.',
        dosage=dict(recommended='1200–2400 mg per dag (mjukkapslar)', timing='Till huvudmåltiderna',
                    frequency='Fördelat på 1–2 doser'),
        forms='Fosfatidylkolin från solroslecitin, fritt från GMO och soja.',
        warnings=['Höga doser kan ge lös avföring eller magbesvär; ta det mitt i en måltid'],
        interactions='Generellt säkert; var försiktig med blodförtunnande läkemedel och kolinesterashämmare.',
        naturalSources='Äggula, lever, sojabönor, solrosfrön och kött.'),
    'panax-ginseng': dict(
        summary='En traditionell adaptogen i österländsk medicin, rik på ginsenosider; den hjälper till att stödja '
                'motståndskraften mot stress och fysisk trötthet, den kognitiva förmågan och vakenheten samt '
                'mikrocirkulationen.',
        dosage=dict(recommended='200–400 mg standardiserat extrakt (4–7 % ginsenosider)',
                    timing='På morgonen till frukost (undvik den efter lunch för att förebygga sömnsvårigheter)',
                    frequency='En gång per dag, högst 3 månader i följd'),
        forms='Standardiserat extrakt av röd koreansk ginseng (4–7 % ginsenosider), eller fermenterad röd ginseng, där '
              'ginsenosiderna omvandlas till det mer lättupptagna Compound K.',
        warnings=['Inte för personer med okontrollerat högt blodtryck eller kraftig hjärtklappning',
                  'Ska inte användas under graviditet eller amning',
                  'Använd den inte i mer än 3 månader utan uppehåll'],
        interactions='Ginseng kan minska effekten av warfarin; den sänker blodsockret, så var försiktig med diabetesläkemedel '
                     'och insulin; den interagerar med centralstimulerande medel, blodtryckssänkande läkemedel och '
                     'MAO-hämmare.',
        naturalSources='Roten av asiatisk ginseng (Panax ginseng), som används som extrakt eller te.'),
    'citicoline': dict(
        summary='Ett ämne som efter upptaget delas i kolin (för bildningen av acetylkolin) och cytidin (som blir uridin i '
                'hjärnan och bygger fosfolipiderna i nervcellernas membran), och som stödjer fokus och en effektiv '
                'informationsbearbetning.',
        dosage=dict(recommended='250–500 mg per dag (EU:s godkända maxdos för kosttillskott är 500 mg)',
                    timing='På morgonen till frukost eller lunch', frequency='1–2 gånger per dag'),
        forms='Rent fermenterat citikolin (som Cognizin®), godkänt som nytt livsmedel i EU.',
        warnings=['Håll dig till EU:s godkända gräns på 500 mg per dag',
                  'Ger i sällsynta fall en övergående huvudvärk eller lätta sömnsvårigheter om det tas sent',
                  'Inte avsett för barn, gravida eller ammande'],
        interactions='Citikolin kan förstärka levodopa vid Parkinsons sjukdom, vilket kan kräva en dosjustering under '
                     'medicinsk uppföljning.',
        naturalSources='Citikolin finns inte i maten; kolin kommer från ägg, lever och fisk.'),
    'black-seed-oil': dict(
        summary='Rik på tymokinon och essentiella fettsyror (omega-6 och omega-9); den hjälper till att dämpa cellernas '
                'inflammatoriska svar, skydda cellerna mot oxidativ stress och stödja andningsvägarnas komfort och '
                'immunförsvaret.',
        dosage=dict(recommended='1000–2000 mg olja (eller 5 ml flytande olja)', timing='Till frukost',
                    frequency='En gång per dag'),
        forms='Mjukkapslar med kallpressad jungfruolja av svartkummin med standardiserat tymokinon (minst 2–3 %).',
        warnings=['För höga doser kan belasta lever och njurar; håll dig till de angivna doserna',
                  'Koncentrerade kapslar ska inte användas under graviditet, eftersom de kan stimulera livmodern'],
        interactions='Svartkummin sänker glukos och blodtryck och hämmar koagulationen något; följ dina värden vid diabetes- '
                     'och blodtrycksläkemedel och undvik höga doser tillsammans med blodförtunnande läkemedel.',
        naturalSources='Svartkummin (Nigella sativa) och dess olja, som används i bröd och matlagning.'),
    'aged-garlic-extract': dict(
        summary='Framställs genom att skivad vitlök lagras i en vattenlösning i flera månader, vilket omvandlar instabilt '
                'allicin till stabila svavelföreningar, främst S-allylcystein (SAC); det hjälper till att stödja elastiska '
                'artärer, blodkärlsväggens funktion och ett normalt blodtryck, och skyddar LDL-kolesterolet mot oxidation.',
        dosage=dict(recommended='600–1200 mg per dag', timing='Till måltiderna', frequency='Fördelat på 1–2 doser'),
        forms='Lagrat vitlöksextrakt standardiserat för SAC (som Kyolic®); luktfritt och ger inte rapningar eller halsbränna.',
        warnings=['Sluta ta det 10–14 dagar före en planerad operation',
                  'Skonsammare mot magen än rå vitlök och tillskott med vitlöksolja'],
        interactions='Varning för blödning: lagrat vitlöksextrakt hämmar blodplättarnas klumpning; var försiktig med '
                     'blodförtunnande läkemedel och antikoagulantia (warfarin, acetylsalicylsyra). Det kan sänka nivåerna av '
                     'vissa hivläkemedel (som sakvinavir).',
        naturalSources='Färsk vitlök och lagrad svart vitlök.'),
    'ceylon-cinnamon': dict(
        summary='Rik på vattenlösliga procyanidiner och kanelaldehyd; studier tyder på att den bromsar magsäckens tömning och '
                'hämmar de enzymer som bryter ned stärkelse, vilket stödjer ett stabilt blodsocker efter måltiderna.',
        dosage=dict(recommended='1–2 g ceylonkanelpulver (eller 500 mg vattenextrakt)', timing='Till stärkelserika måltider',
                    frequency='1–2 gånger per dag'),
        forms='Endast ceylonkanel (Cinnamomum verum); undvik kinesisk kassiakanel, som har hög halt av leverskadligt kumarin.',
        warnings=['EFSA:s tolerabla dagliga intag av kumarin är 0,1 mg per kg kroppsvikt, vilket gör ceylonkanel till det '
                  'säkra valet för daglig användning',
                  'Höga doser ska inte användas under graviditet'],
        interactions='Kanel förstärker blodsockersänkande läkemedel och insulin; följ dina värden för att undvika hypoglykemi. '
                     'Kassiakanel belastar levern ytterligare tillsammans med läkemedel som belastar levern.',
        naturalSources='Bark av ceylonkanel (stänger eller pulver).'),
    'bitter-melon': dict(
        summary='En traditionell asiatisk frukt som innehåller charantin, vicin och den insulinliknande polypeptid-P; '
                'laboratoriestudier tyder på att den stimulerar musklernas glukosupptag, men beläggen från studier på '
                'människor är fortfarande begränsade enligt en Cochraneöversikt.',
        dosage=dict(recommended='500–1000 mg standardiserat extrakt', timing='30 minuter före huvudmåltiderna',
                    frequency='Två gånger per dag'),
        forms='Kapslar med standardiserat extrakt (2,5–5 % charantin), som undviker fruktens mycket beska smak.',
        warnings=['Ska inte användas under graviditet eller amning, eftersom den kan utlösa livmodersammandragningar och '
                  'blödning',
                  'Inte för personer med G6PD-brist (favism), eftersom fröna innehåller vicin, som kan orsaka hemolys'],
        interactions='Allvarlig interaktion: bittergurka sänker glukosen; använd den inte tillsammans med insulin eller '
                     'sulfonylureider utan medicinsk uppföljning, för att undvika svår hypoglykemi.',
        naturalSources='Bittergurka (karela), som tillagas i det asiatiska köket.'),
    'gymnema-sylvestre': dict(
        summary="Kallas på hindi gurmar, 'sockerförstöraren'; dess gymnemasyror binder till receptorerna för söt smak på "
                'tungan, vilket dämpar sötman i flera timmar och minskar sötsuget, och konkurrerar med glukos om '
                'upptagsställena i tarmen.',
        dosage=dict(recommended='400–600 mg standardiserat extrakt (25–75 % gymnemasyror)',
                    timing='15 minuter före måltiderna med vatten', frequency='Fördelat på två doser'),
        forms='Standardiserat bladextrakt (minst 25 % gymnemasyror), som även finns som droppar på tungan före maten.',
        warnings=['Kan ge lätt illamående på helt tom mage',
                  'Ska inte användas under graviditet eller amning eftersom säkerhetsdata är otillräckliga',
                  'Sluta ta det två veckor före en operation'],
        interactions='Gymnema förstärker blodsockersänkande läkemedel och insulin; följ dina värden och justera doserna under '
                     'din läkares uppföljning.',
        naturalSources='Gymnemablad (används som extrakt eller te); finns inte i vardagsmat.'),
    'myo-inositol': dict(
        summary='Ett vitaminliknande ämne som fungerar som andra budbärare för signalerna från insulin och '
                'follikelstimulerande hormon (FSH) inne i cellerna; det hjälper till att stödja insulinkänsligheten, och '
                'metaanalyser hos kvinnor med polycystiskt ovariesyndrom tyder på att det stödjer en regelbunden ägglossning '
                'och hormonbalansen.',
        dosage=dict(recommended='2–4 g per dag (pulver upplöst i vatten)',
                    timing='Morgon och kväll, till eller mellan måltiderna', frequency='Fördelat på två doser'),
        forms='Blandningen som motsvarar det naturliga förhållandet i plasma (40:1 mellan myo-inositol och '
              'D-chiro-inositol), ofta med folsyra (400 µg).',
        warnings=['Stora startdoser (över 6 g) kan ge magbesvär eller lätt diarré',
                  'Använd det under graviditet endast under medicinsk uppföljning'],
        interactions='Säkert med de flesta läkemedel; det kan förstärka metformin och andra blodsockersänkande läkemedel.',
        naturalSources='Citrusfrukter (särskilt apelsiner och grapefrukt), baljväxter, fullkorn och nötter.'),
    'white-kidney-bean': dict(
        summary='Ett extrakt som innehåller det hämmande proteinet fasolamin, som tillfälligt blockerar det '
                'stärkelsenedbrytande enzymet alfa-amylas, delvis minskar omvandlingen av komplex stärkelse till enkla '
                'sockerarter och låter en del av den passera till tjocktarmen som fiber.',
        dosage=dict(recommended='1000–1500 mg', timing='10–15 minuter före stärkelserika måltider med ett glas vatten',
                    frequency='1–2 gånger per dag till stärkelserika måltider'),
        forms='Extrakt standardiserat för amylashämmande aktivitet och kliniskt studerat (som Phase 2®); undvik '
              'ostandardiserade råa pulver.',
        warnings=['Det verkar bara på komplex stärkelse, inte på enkla sockerarter',
                  'Kan ge gaser, uppblåsthet och lös avföring',
                  'Det ersätter inte en balanserad kost'],
        interactions='Kan sänka blodsockret efter stärkelserika måltider; följ dina värden vid diabetesläkemedel och insulin.',
        naturalSources='Väl kokta vita bönor (Phaseolus vulgaris).'),
    'glucomannan': dict(
        summary='En mycket löslig fiber från konjakroten som suger upp vatten och sväller till en gel som fyller magen och '
                'bromsar tömningen; glukomannan i samband med en energibegränsad kost bidrar till viktminskning '
                '(EFSA-godkänt påstående vid 3 g per dag).',
        dosage=dict(recommended='1 g tre gånger per dag (totalt 3 g, enligt EFSA)',
                    timing='15–30 minuter före huvudmåltiderna med två stora glas vatten (500 ml)',
                    frequency='3 gånger per dag'),
        forms='Kapslar eller portionspåsar med 100 % ren glukomannan, som sväljs eller löses i vatten direkt innan det hinner '
              'bli gel.',
        warnings=['Varning för kvävning (EFSA): svälj det aldrig utan rikligt med vatten, eftersom det kan svälla i matstrupen '
                  'och blockera halsen, särskilt hos personer med sväljsvårigheter',
                  'Ta det inte precis före sänggåendet',
                  'Kan ge uppblåsthet och gaser i början'],
        interactions='Gelen försvårar upptaget av läkemedel som tas via munnen; ta läkemedel minst två timmar före eller fyra '
                     'timmar efter (särskilt diabetes- och blodtrycksläkemedel och p-piller).',
        naturalSources='Konjakrot (används i shiratakinudlar och asiatiska geléer).'),
    'valerian-root': dict(
        summary='En av de äldsta örterna för sömn i Europa, rik på valerensyror; den hjälper till att begränsa nedbrytningen '
                'av den lugnande signalsubstansen GABA, vilket stödjer ett snabbare insomnande och bättre sömn utan '
                'morgontrötthet.',
        dosage=dict(recommended='300–600 mg standardiserat extrakt (0,8 % valerensyra)',
                    timing='30–120 minuter före sänggåendet', frequency='En gång per dag'),
        forms='Kapslar med torrextrakt standardiserat för valerensyra, för en jämn dos utan den råa rotens starka lukt.',
        warnings=['Kör inte bil och använd inte maskiner efter intag',
                  'Kan ge lätt huvudvärk eller livliga drömmar hos ett fåtal',
                  'Inte för barn under 12 år, eller under graviditet och amning'],
        interactions='Vänderot förstärker sömnmedel, lugnande medel, ångestdämpande läkemedel (bensodiazepiner) och alkohol, '
                     'och kan interagera med läkemedel som bryts ned av leverns CYP-enzymer.',
        naturalSources='Vänderot (används som extrakt eller te).'),
    'passionflower': dict(
        summary='En växt rik på flavonoider (som krysin och vitexin); den hjälper till att modulera aktiviteten i hjärnans '
                'GABA-receptorer och stödjer lindring av känslor av spänning och rastlöshet utan att påverka den mentala '
                'vakenheten.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt (eller en infusion)',
                    timing='Två gånger per dag eller en timme före sänggåendet', frequency='1–2 gånger per dag'),
        forms='Kapslar standardiserade för flavonoider (vitexin och isovitexin) eller koncentrerade flytande extrakt, ofta '
              'kombinerade med vänderot och citronmeliss.',
        warnings=['Kan ge lätt dåsighet hos vissa',
                  'Ska inte användas under graviditet, eftersom den innehåller alkaloider som kan utlösa livmodersammandragningar'],
        interactions='Passionsblomma förstärker lugnande medel, ångestdämpande läkemedel och smärtstillande läkemedel; undvik '
                     'den tillsammans med alkohol och antidepressiva MAO-hämmare.',
        naturalSources='Blad och blommor av passionsblomma (används som te eller extrakt).'),
    'lemon-balm': dict(
        summary='En citrondoftande ört ur de kransblommiga växternas familj, rik på rosmarinsyra; studier tyder på att den '
                'hämmar GABA-transaminas, vilket höjer det lugnande GABA i hjärnan, och lindrar stressrelaterade kramper i '
                'matsmältningen.',
        dosage=dict(recommended='300–600 mg per dag',
                    timing='Till måltiderna, eller en timme före sänggåendet för att stödja avslappning',
                    frequency='Fördelat på 1–2 doser'),
        forms='Bladextrakt standardiserat för rosmarinsyra (minst 2–5 %, som Cyracos®), eller te på bladen.',
        warnings=['Var försiktig om du har kraftig underfunktion i sköldkörteln',
                  'Undvik helst koncentrerade tillskott under graviditet och amning',
                  'Kan ge lätt dåsighet'],
        interactions='Citronmeliss kan störa sköldkörtelläkemedel, eftersom studier tyder på att den kan hämma bindningen av '
                     'sköldkörtelstimulerande hormon (TSH) till dess receptorer. Den förstärker sömnmedel och lugnande medel.',
        naturalSources='Färska eller torkade blad av citronmeliss (används som te eller i matlagning).'),
    'vitamin-a': dict(
        summary='A-vitamin bidrar till att bibehålla normal syn, till immunsystemets normala funktion, till att bibehålla '
                'normala slemhinnor och normal hud och har en roll i processen för celldifferentiering (EFSA-godkända '
                'påståenden); det ingår i rodopsin, synpigmentet för seende i svagt ljus.',
        dosage=dict(recommended='800–1500 µg RAE per dag (cirka 2700–5000 IE)', timing='Till en måltid som innehåller fett',
                    frequency='En gång per dag'),
        forms='En kombination av retinol (retinylpalmitat) med naturliga blandade karotenoider, eftersom kroppen omvandlar '
              'betakaroten till A-vitamin bara när det behövs.',
        warnings=['EFSA:s övre gräns för retinol är 3000 µg per dag; gravida får inte överskrida säkra doser på grund av risken '
                  'för fosterskador',
                  'Tillskott med höga doser isolerat betakaroten ökar risken för lungcancer hos rökare (studierna ATBC och CARET)',
                  'Överskott ger håravfall, torr hud och leverbelastning'],
        interactions='Farlig interaktion: kombinera det aldrig med läkemedel mot akne och psoriasis som härstammar från '
                     'A-vitamin (isotretinoin, acitretin), för att undvika A-vitaminförgiftning.',
        naturalSources='Lever, äggula, smör, morötter, sötpotatis, spenat och aprikoser.'),
    'biotin': dict(
        summary='Ett vattenlösligt vitamin som är koenzym för fem karboxylasenzymer; biotin bidrar till normal omsättning av '
                'makronäringsämnen och normal energiomsättning och till att bibehålla normalt hår, normal hud och normala '
                'slemhinnor (EFSA-godkända påståenden).',
        dosage=dict(recommended='100–1000 µg per dag (behovet från maten är 40 µg; 2500–5000 µg används vid sköra naglar och '
                                'skört hår)',
                    timing='Till frukost', frequency='En gång per dag'),
        forms='Naturligt D-biotin, den enda formen med full biologisk aktivitet.',
        warnings=['Varning för laboratorieprover (FDA): höga doser (över 1000 µg) stör immunanalyser och ger falska resultat '
                  'i sköldkörtelprover och prover för hjärttroponin',
                  'Gör uppehåll med biotin 48–72 timmar före alla blodprover och berätta det för din läkare och laboratoriet',
                  'Det hjälper främst hår och naglar när det finns en brist'],
        interactions='Långvarig behandling med läkemedel mot epilepsi (karbamazepin, fenytoin) sänker biotinnivåerna, och '
                     'långvarig antibiotikabehandling minskar tarmbakteriernas produktion av biotin.',
        naturalSources='Kokt äggula, lever, nötter och frön, sötpotatis och lax.'),
    'molybdenum': dict(
        summary='Ett spårämne som bidrar till normal omsättning av svavelhaltiga aminosyror (EFSA-godkänt påstående); det är '
                'kofaktor till sulfitoxidas, som omvandlar sulfit till sulfat, och till xantinoxidas, som bryter ned puriner.',
        dosage=dict(recommended='50–100 µg per dag (vuxnas behov är 65 µg enligt EFSA; finns i de flesta multivitaminer)',
                    timing='Till en måltid', frequency='En gång per dag'),
        forms='Molybdenglycinatkelat eller natriummolybdat.',
        warnings=['EFSA:s övre gräns för vuxna är 600 µg per dag',
                  'Långvarigt överskott kan höja urinsyran och ge giktliknande ledsmärta',
                  'Brist är ovanlig vid en varierad kost'],
        interactions='Säkert i de vanliga doserna; mycket höga doser ökar utsöndringen av koppar i urinen och kan sänka '
                     'kopparnivåerna.',
        naturalSources='Baljväxter (linser, bönor, ärter), fullkorn, nötter och lever.'),
})

# third batch (101-174 in the data order), part A
COPY.update({
    's-adenosyl-methionine': dict(
        summary='Ett ämne som levern bildar av aminosyran metionin och kroppens viktigaste metylgivare; det deltar i '
                'bildningen av signalsubstanser (serotonin och dopamin), glutation och broskets byggstenar, och kliniska '
                'studier tyder på att det stödjer sinnesstämningen och ledernas komfort och rörlighet.',
        dosage=dict(recommended='400–800 mg per dag',
                    timing='På morgonen på fastande mage, en halvtimme före frukost, med ett stort glas vatten',
                    frequency='En gång per dag'),
        forms='Enterodragerade SAMe-tabletter i förseglade blister, eftersom molekylen är mycket känslig för fukt och magsyra.',
        warnings=['Inte för personer med bipolär sjukdom, eftersom det kan utlösa maniska episoder',
                  'Kan ge lätta magbesvär, eller sömnsvårigheter om det tas på kvällen',
                  'Undvik under graviditet och amning, eftersom säkerhetsdata är otillräckliga'],
        interactions='Viktig varning (serotonergt syndrom): kombinera det aldrig med antidepressiva läkemedel (SSRI, SNRI, '
                     'MAO-hämmare), 5-HTP, johannesört, tramadol eller triptaner.',
        naturalSources='Kroppen bildar det av metionin (kött, fisk, ägg); maten innehåller inga betydande mängder.'),
    'grape-seed-extract': dict(
        summary='Ett extrakt rikt på proantocyanidiner (OPC), växtantioxidanter som hjälper till att skydda kollagenfibrerna '
                'i huden och blodkärlsväggarna; studier tyder på att det stödjer venerna och cirkulationen, lindrar tunga, '
                'svullna ben efter långt stillasittande och stödjer en strålande, jämn hudton.',
        dosage=dict(recommended='100–300 mg per dag', timing='Efter frukost eller lunch', frequency='En gång per dag'),
        forms='Druvkärnextrakt standardiserat till 95 % proantocyanidiner (OPC), i kapslar eller tabletter.',
        warnings=['Sluta två veckor före en operation på grund av den lätt blodförtunnande effekten',
                  'Undvik under graviditet och amning, eftersom säkerhetsdata är otillräckliga'],
        interactions='Använd det med försiktighet tillsammans med blodförtunnande och blodplättshämmande läkemedel (warfarin, '
                     'acetylsalicylsyra, klopidogrel), eftersom risken för blödning kan öka.',
        naturalSources='Kärnor och skal av röda druvor, mörka bär och mörk choklad.'),
    'chlorella': dict(
        summary='Mikroskopiska gröna alger rika på klorofyll, protein, järn och K-vitamin; en klinisk studie tyder på att '
                'chlorella stödjer aktiviteten hos immunförsvarets NK-celler och en annan att den stödjer normala nivåer av '
                'blodfetter och antioxidanter, och den stödjer matsmältningen och en regelbunden mage.',
        dosage=dict(recommended='2–3 g per dag',
                    timing='20 minuter före en måltid med ett stort glas vatten, eller i gröna smoothies',
                    frequency='Fördelat på två doser'),
        forms='Tabletter eller pulver av chlorella med sprängd cellvägg för ett bra upptag, helst testade fria från '
              'tungmetaller.',
        warnings=['Kan ge lätta gaser eller grön avföring de första dagarna, vilket är övergående',
                  'Innehåller jod; rådgör med din läkare om du har en sköldkörtelsjukdom',
                  'Undvik om du är allergisk mot alger eller jod'],
        interactions='Chlorella är rik på K-vitamin och kan därför försvaga warfarin (Waran) och andra '
                     'K-vitaminantagonister; håll den dagliga mängden jämn och berätta det för din läkare. Den kan störa '
                     'immunhämmande läkemedel.',
        naturalSources='Ett tillskott i sig; klorofyll finns i mörka bladgrönsaker som spenat och persilja.'),
    'pantothenic-acid': dict(
        summary='Pantotensyra bidrar till normal energiomsättning, till att minska trötthet och utmattning, till normal '
                'mental prestation och till normal syntes och omsättning av steroidhormoner, D-vitamin och vissa '
                'signalsubstanser (EFSA-godkända påståenden); den ingår i koenzym A (CoA), som förbränner kolhydrater och fett.',
        dosage=dict(recommended='50–100 mg per dag (referensintaget på EU-märkningen är 6 mg och EFSA:s adekvata intag för '
                                'vuxna är 5 mg; doser upp till 500 mg används under professionell uppföljning)',
                    timing='På morgonen till frukost', frequency='En gång per dag'),
        forms='Kalcium-D-pantotenat, eller pantetin, den aktiva formen.',
        warnings=['Ett mycket säkert vattenlösligt vitamin som inte ansamlas i kroppen; överskottet lämnar kroppen med urinen',
                  'Mycket stora doser (över 2000 mg) kan ge lös avföring'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats vid de vanliga doserna.',
        naturalSources='Lever, äggula, svamp, avokado, baljväxter och fullkorn.'),
    'riboflavin': dict(
        summary='Riboflavin bidrar till normal energiomsättning, till att bibehålla normal syn, normal hud och normala '
                'slemhinnor, till att skydda cellerna mot oxidativ stress och till att minska trötthet och utmattning '
                '(EFSA-godkända påståenden); det är riboflavin som färgar urinen klargul efter intaget, vilket är normalt och '
                'ofarligt.',
        dosage=dict(recommended='10–25 mg per dag (referensintaget är 1,4 mg; de höga doserna på 200–400 mg som används i '
                                'studier är endast för användning under medicinsk uppföljning)',
                    timing='På morgonen till frukost', frequency='En gång per dag'),
        forms='Rent riboflavin, eller den aktiva formen riboflavin-5\'-fosfat (R5P).',
        warnings=['Ett mycket säkert vattenlösligt vitamin; EFSA har inte fastställt någon övre gräns eftersom inga '
                  'biverkningar har setts',
                  'Klargul urin är normalt och inget att oroa sig för'],
        interactions='Tricykliska antidepressiva läkemedel, vissa antipsykotiska läkemedel (klorpromazin) och p-piller kan '
                     'sänka nivåerna i kroppen.',
        naturalSources='Mjölk och mejeriprodukter, ägg, lever, kött, mandlar och svamp.'),
    'thiamine': dict(
        summary='Tiamin bidrar till normal energiomsättning, till nervsystemets normala funktion, till normal psykologisk '
                'funktion och till hjärtats normala funktion (EFSA-godkända påståenden); det omvandlar glukos till energi '
                'som försörjer hjärnans celler och de perifera nerverna, och behovet ökar med en kost rik på socker och '
                'stärkelse.',
        dosage=dict(recommended='50–100 mg per dag (referensintaget är 1,1 mg)', timing='Till frukost eller lunch',
                    frequency='En gång per dag'),
        forms='Tiaminhydroklorid eller tiaminmononitrat, eller fettlösligt benfotiamin, som har högre biotillgänglighet.',
        warnings=['Ett mycket säkert vattenlösligt vitamin; EFSA har inte fastställt någon övre gräns',
                  'Hög alkoholkonsumtion tömmer kraftigt förråden av tiamin'],
        interactions='Vätskedrivande läkemedel (särskilt furosemid) ökar förlusterna via urinen, och stora mängder kaffe och '
                     'te kan minska upptaget.',
        naturalSources='Fullkorn, fläskkött, baljväxter, solrosfrön och nötter.'),
    'niacin': dict(
        summary='Niacin bidrar till normal energiomsättning, till nervsystemets normala funktion, till normal psykologisk '
                'funktion, till att bibehålla normal hud och normala slemhinnor och till att minska trötthet och utmattning '
                '(EFSA-godkända påståenden); det är råvaran till NAD+, som cellerna behöver för att producera energi.',
        dosage=dict(recommended='Nikotinamid: 16–50 mg per dag (referensintaget är 16 mg). Nikotinsyra: högst 10 mg per dag',
                    timing='Till en hel måltid mitt på dagen', frequency='En gång per dag'),
        forms='Nikotinamid är den föredragna formen eftersom den inte ger rodnad; nikotinsyra ger rodnad och värme i ansikte '
              'och hals (niacinflush) i ungefär en halvtimme.',
        warnings=['EFSA:s övre gränser: 10 mg per dag för nikotinsyra och 900 mg för nikotinamid',
                  'Stora läkemedelsdoser (över 500 mg) kräver kontroll av leverenzymerna och är endast för användning under '
                  'medicinsk uppföljning',
                  'Använd det med försiktighet om du har gikt eller magsår'],
        interactions='Niacin kan förstärka blodtryckssänkande läkemedel och statiner (högre risk för muskelsmärta vid höga '
                     'doser) och kan påverka blodsockerkontrollen hos personer med diabetes.',
        naturalSources='Kyckling, tonfisk, lax, jordnötter, svamp och fullkorn.'),
    'folate': dict(
        summary='Folat bidrar till normal blodbildning, till normal homocysteinomsättning, till normal celldelning, till '
                'tillväxt av moderns vävnader under graviditet och till att minska trötthet och utmattning (EFSA-godkända '
                'påståenden); metylfolat är den aktiva form som kroppen använder direkt, utan omvandling.',
        dosage=dict(recommended='400–800 µg per dag (EFSA:s övre gräns är 1000 µg per dag)',
                    timing='På morgonen, med eller utan mat', frequency='En gång per dag'),
        forms='Kalcium-L-metylfolat (L-5-MTHF), ett bra alternativ för personer med varianter av MTHFR-genen som bromsar '
              'omvandlingen av vanlig folsyra.',
        warnings=['Höga doser kan dölja tecknen på brist på B12-vitamin, så det tas helst tillsammans med B12',
                  'Kvinnor som planerar en graviditet rekommenderas att ta 400 µg per dag från 4 veckor före befruktningen '
                  'till vecka 8 av graviditeten'],
        interactions='Folat kan minska effekten av metotrexat och vissa läkemedel mot epilepsi (fenytoin), och dessa '
                     'läkemedel och metformin sänker folatnivåerna. Fråga din läkare innan du kombinerar dem.',
        naturalSources='Mörka bladgrönsaker, baljväxter, sparris, broccoli, lever och citrusfrukter.'),
    'pyridoxine': dict(
        summary='B6-vitamin bidrar till nervsystemets normala funktion, till normal psykologisk funktion, till normal '
                'bildning av röda blodkroppar, till immunsystemets normala funktion, till regleringen av hormonaktiviteten '
                'och till att minska trötthet och utmattning (EFSA-godkända påståenden); det omvandlar aminosyran '
                'tryptofan till serotonin.',
        dosage=dict(recommended='Mindre än 12 mg per dag från alla källor sammanlagt (P5P i 5–10 mg; referensintaget är 1,4 mg)',
                    timing='På morgonen till frukost', frequency='En gång per dag'),
        forms='Pyridoxal-5\'-fosfat (P5P), den aktiva formen, eller pyridoxinhydroklorid.',
        warnings=['EFSA:s övre gräns (2023) för vuxna är 12 mg per dag från alla källor sammanlagt; överskrid den inte',
                  'Långvarig användning över gränsen är kopplad till perifer sensorisk neuropati (domningar och stickningar i '
                  'händer och fötter); sluta genast om sådana symtom uppstår',
                  'Kontrollera märkningen: B6 finns också i multivitaminer, magnesiumtillskott och B-komplex'],
        interactions='B6-vitamin minskar effekten av levodopa (när det används utan karbidopa) och kan sänka nivåerna av '
                     'fenytoin och fenobarbital. Isoniazid och penicillamin tömmer förråden av B6.',
        naturalSources='Kyckling, fisk, potatis, bananer, kikärter och nötter.'),
    'manganese': dict(
        summary='Ett spårämne som bidrar till normal energiomsättning, till att bibehålla normal benstomme, till normal '
                'bildning av bindväv och till att skydda cellerna mot oxidativ stress (EFSA-godkända påståenden); det ingår '
                'i MnSOD, ett antioxidativt enzym inne i mitokondrierna.',
        dosage=dict(recommended='2–4 mg per dag (referensintaget är 2 mg och EFSA:s adekvata intag är 3 mg)',
                    timing='Till lunch', frequency='En gång per dag'),
        forms='Manganbisglycinatkelat eller manganglukonat, ofta i ledpreparat med glukosamin och kollagen.',
        warnings=['EFSA har inte fastställt någon säker övre gräns för mangan eftersom data är otillräckliga, så håll dig '
                  'till måttliga doser',
                  'Undvik det vid kronisk leversjukdom, eftersom levern gör sig av med mangan',
                  'Brist är ovanlig hos personer som äter fullkorn, te och nötter'],
        interactions='Mangan konkurrerar med järn, kalcium och magnesium om upptaget, så ta det med två timmars mellanrum '
                     'från dem; det minskar upptaget av tetracykliner och kinolonantibiotika.',
        naturalSources='Fullkorn, te, nötter (hasselnötter, valnötter), baljväxter, ananas och spenat.'),
    'bilberry-extract': dict(
        summary='Ett extrakt av europeiska vilda blåbär (Vaccinium myrtillus) rikt på antocyaner; kliniska studier tyder på '
                'att det lindrar ansträngda och trötta ögon hos personer som arbetar många timmar vid skärm och stödjer '
                'ciliarmuskeln som ställer in skärpan.',
        dosage=dict(recommended='80–160 mg per dag', timing='Efter en måltid med ett glas vatten', frequency='En gång per dag'),
        forms='Blåbärsextrakt standardiserat till 25 % antocyaner, i kapslar.',
        warnings=['Tolereras väl i de vanliga doserna',
                  'Undvik det koncentrerade extraktet under graviditet och amning, eftersom säkerhetsdata är otillräckliga'],
        interactions='I höga doser kan det förstärka blodförtunnande och blodplättshämmande läkemedel (warfarin, '
                     'acetylsalicylsyra) och sänka blodsockret ytterligare tillsammans med diabetesläkemedel.',
        naturalSources='Färska eller frysta blåbär, amerikanska blåbär och svarta vinbär.'),
    'hawthorn-berry': dict(
        summary='En traditionell europeisk växt rik på flavonoider och procyanidiner; den används traditionellt för att '
                'stödja hjärtats normala funktion och cirkulationen, och en klinisk studie tyder på att den stödjer ett '
                'normalt blodtryck hos personer med lätt förhöjda värden.',
        dosage=dict(recommended='300–600 mg standardiserat extrakt per dag', timing='Till en måltid på morgonen eller kvällen',
                    frequency='Fördelat på två doser'),
        forms='Extrakt av hagtornsblad, blommor och bär standardiserat för flavonoider eller procyanidiner (som WS 1442).',
        warnings=['Ersätter inte förskrivna hjärtläkemedel; personer med hjärtsjukdom bör rådgöra med sin behandlande läkare '
                  'före användning',
                  'Undvik under graviditet och amning',
                  'Kan ge lätt yrsel eller magbesvär'],
        interactions='Viktig varning: hagtorn kan förstärka digoxin, betablockerare, ACE-hämmare, kalciumkanalblockerare och '
                     'nitrater, så kombinera den bara med dem under din behandlande läkares uppföljning.',
        naturalSources='Färska eller torkade hagtornsbär (används som te eller sylt).'),
    'dandelion-root': dict(
        summary='En traditionell växt rik på bitterämnen och inulin; roten används traditionellt för att stödja en normal '
                'matsmältning och gallflödet, som hjälper till att smälta fett, och bladen används traditionellt för att '
                'stödja ett normalt urinflöde.',
        dosage=dict(recommended='500–1000 mg rotpulver (eller 250–500 mg koncentrerat extrakt)',
                    timing='15 minuter före måltiderna med en kopp varmt vatten', frequency='1–2 gånger per dag'),
        forms='Torkat maskrosrotspulver eller koncentrerat extrakt i kapslar, eller te på rostad rot.',
        warnings=['Ska inte användas vid gallgångshinder, gallblåseinflammation eller gallsten utan medicinsk uppföljning',
                  'Undvik om du är allergisk mot korgblommiga växter (kamomill, krysantemum)',
                  'Kan ge lätt halsbränna'],
        interactions='Maskros kan förstärka vätskedrivande läkemedel och höja litiumhalten i blodet, och den kan minska '
                     'upptaget av kinolonantibiotika. Använd den med försiktighet tillsammans med diabetesläkemedel.',
        naturalSources='Färska maskrosblad i sallader och te på rostad maskrosrot.'),
    'burdock-root': dict(
        summary='En traditionell rot rik på den prebiotiska fibern inulin, som ger näring åt nyttiga tarmbakterier, och på '
                'antioxidativa polyfenoler; den används traditionellt för att stödja matsmältningen, en regelbunden mage och '
                'en klar hud.',
        dosage=dict(recommended='400–800 mg per dag', timing='Till lunch med rikligt med vatten', frequency='En gång per dag'),
        forms='Torkat kardborrerotspulver eller extrakt i kapslar, eller te på roten.',
        warnings=['Undvik om du är allergisk mot korgblommiga växter (kamomill, krysantemum)',
                  'Undvik under graviditet och amning',
                  'Köp den endast från pålitliga källor, eftersom roten kan förväxlas med den giftiga roten av belladonna'],
        interactions='Kardborrerot kan sänka blodsockret ytterligare tillsammans med diabetesläkemedel och kan förstärka '
                     'vätskedrivande och blodförtunnande läkemedel.',
        naturalSources='Färsk kardborrerot (gobo) i japansk matlagning, cikoria, kronärtskocka och lök.'),
    'black-elderberry': dict(
        summary='Ett extrakt av kokta svarta fläderbär rikt på antocyaner och flavonoider; en metaanalys av kliniska studier '
                'tyder på att det förkortar och lindrar symtom från de övre luftvägarna när det tas tidigt, och det stödjer '
                'immunsystemets normala funktion under förkylningssäsongen.',
        dosage=dict(recommended='300–500 mg standardiserat extrakt per dag som förebyggande stöd, och upp till 1000 mg '
                                'fördelat på flera doser i 3–5 dagar vid de första tecknen på förkylning',
                    timing='Direkt efter en måltid', frequency='1–3 gånger per dag'),
        forms='Standardiserat fläderbärsextrakt (som Rubini eller Sambucol) i kapslar, sirap eller sugtabletter.',
        warnings=['Använd endast tillverkade produkter; råa eller omogna bär, blad och stjälkar innehåller giftiga '
                  'cyanogena ämnen',
                  'Undvik under graviditet och amning, eftersom säkerhetsdata är otillräckliga',
                  'Rådgör med din läkare om du har en autoimmun sjukdom'],
        interactions='Fläder kan störa immunhämmande läkemedel (som läkemedel efter transplantation) och kan förstärka '
                     'vätskedrivande läkemedel och diabetesläkemedel.',
        naturalSources='Sylt och saft gjorda på kokta fläderbär.'),
    'cat-s-claw': dict(
        summary='Barken av en växt från Amazonas som används traditionellt för att stödja ledernas komfort och ett normalt '
                'immunsvar; en studie på friska frivilliga tyder på att vattenextraktet stödjer reparationen av DNA och '
                'skyddar cellerna mot oxidativ stress.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt per dag', timing='Till en rejäl måltid',
                    frequency='En gång per dag'),
        forms='Vattenextrakt av kattklobark standardiserat för oxindolalkaloider, i kapslar.',
        warnings=['Ska inte användas under graviditet eller amning, eller av kvinnor som försöker bli gravida',
                  'Inte för personer med autoimmuna sjukdomar (som lupus eller MS) eller organtransplanterade',
                  'Sluta två veckor före en operation'],
        interactions='Kattklo interagerar med immunhämmande och blodförtunnande läkemedel (warfarin) och kan förstärka '
                     'blodtryckssänkande läkemedel; den kan hämma CYP3A4 och därmed höja blodnivåerna av vissa läkemedel.',
        naturalSources='Finns inte i maten; barken används som traditionellt te i Sydamerika.'),
    'olive-leaf-extract': dict(
        summary='Ett extrakt rikt på oleuropein och hydroxityrosol, antioxidanter som är typiska för medelhavskosten; '
                'kliniska studier tyder på att det stödjer normalt blodtryck och normala blodfetter och förbättrar '
                'insulinkänsligheten hos vuxna med övervikt.',
        dosage=dict(recommended='500–1000 mg per dag', timing='Till frukost eller lunch', frequency='Fördelat på två doser'),
        forms='Olivbladsextrakt standardiserat till 15–20 % oleuropein, i kapslar eller som flytande extrakt.',
        warnings=['Tolereras väl; kan ge lätta magbesvär eller huvudvärk de första dagarna',
                  'Undvik under graviditet och amning, eftersom säkerhetsdata är otillräckliga'],
        interactions='Olivbladsextrakt kan förstärka blodtrycks- och diabetesläkemedel, så följ dina värden när du kombinerar '
                     'dem; använd det med försiktighet tillsammans med blodförtunnande läkemedel.',
        naturalSources='Extra jungfruolivolja, oliver och te på olivblad.'),
    'echinacea': dict(
        summary='En traditionell ört som används under korta perioder för att stödja kroppens naturliga försvar under '
                'förkylningssäsongen; metaanalyser tyder på en möjlig nytta för att förebygga och förkorta förkylningar, '
                'med resultat som varierar mellan produkter.',
        dosage=dict(recommended='300–500 mg standardiserat extrakt 3 gånger per dag vid de första tecknen på förkylning, '
                                'i 5–7 dagar, sedan uppehåll',
                    timing='Till måltiderna', frequency='3 gånger per dag'),
        forms='Standardiserad saft eller extrakt av de ovanjordiska delarna av Echinacea purpurea, i kapslar eller droppar.',
        warnings=['Använd den inte kontinuerligt i mer än 10 dagar',
                  'Inte för personer som är allergiska mot korgblommiga växter, eller som har autoimmuna eller progressiva '
                  'systemiska sjukdomar (som tuberkulos eller hiv)',
                  'Rekommenderas inte för barn under 12 år'],
        interactions='Röd solhatt kan störa immunhämmande läkemedel och påverka CYP450-enzymerna, vilket ändrar nivåerna av '
                     'vissa läkemedel (som midazolam och koffein).',
        naturalSources='Finns inte i maten; används som örtte eller extrakt.'),
    'african-mango': dict(
        summary='Ett extrakt av fröna från Irvingia gabonensis, rikt på löslig fiber; en klinisk studie tyder på att det '
                'stödjer aptitkontroll, vikt, midjemått och blodfetter tillsammans med en balanserad kost, medan en '
                'systematisk översikt beskriver evidensens kvalitet som fortfarande begränsad.',
        dosage=dict(recommended='150 mg två gånger per dag (eller 300 mg en gång)',
                    timing='30–60 minuter före en måltid med ett glas vatten', frequency='1–2 gånger per dag'),
        forms='Standardiserat extrakt av afrikanska mangofrön (IGOB131) i kapslar.',
        warnings=['Kan ge lätt muntorrhet, huvudvärk eller gaser de första dagarna; drick tillräckligt med vatten',
                  'Undvik under graviditet och amning',
                  'Det ersätter inte en balanserad kost och fysisk aktivitet'],
        interactions='Det kan sänka blodsockret ytterligare tillsammans med diabetesläkemedel; ta andra läkemedel en timme '
                     'före eller två timmar efter, eftersom fibern kan minska deras upptag.',
        naturalSources='Fröna av irvingiafrukten (används i västafrikansk matlagning för att reda soppor).'),
    'horny-goat-weed': dict(
        summary='En traditionell asiatisk ört rik på ikariin; laboratorie- och djurstudier tyder på att ikariin stödjer '
                'bildningen av kväveoxid och avslappningen av blodkärlen, vilket kan stödja ett normalt blodflöde och '
                'vitaliteten, även om tillräckliga studier på människor fortfarande saknas.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt per dag', timing='En timme efter en måltid',
                    frequency='En gång per dag'),
        forms='Epimediumbladextrakt standardiserat till 10–20 % ikariin, i kapslar.',
        warnings=['Kan sänka blodtrycket och ge yrsel; undvik det vid lågt blodtryck eller hjärtsjukdom',
                  'Ska inte användas under graviditet eller amning',
                  'Höga doser och långvarig användning kan ge hjärtklappning och irritabilitet'],
        interactions='Viktig varning: kombinera det aldrig med nitrater mot hjärtsjukdom eller PDE5-hämmare (sildenafil, '
                     'tadalafil) på grund av risken för ett kraftigt blodtrycksfall; använd det med försiktighet tillsammans '
                     'med blodtryckssänkande och blodförtunnande läkemedel.',
        naturalSources='Finns inte i maten; bladen används traditionellt som te i Kina.'),
    'evening-primrose-oil': dict(
        summary='En fröolja rik på gammalinolensyra (GLA), en omega-6-fettsyra; en metaanalys tyder på att den lindrar '
                'cykliska bröstbesvär kopplade till menstruationscykeln, och en klinisk studie tyder på att den stödjer '
                'hudens fuktighet, mjukhet och elasticitet hos friska vuxna.',
        dosage=dict(recommended='1000–2000 mg per dag', timing='Till huvudmåltider som innehåller fett',
                    frequency='Fördelat på två doser'),
        forms='Kapslar med kallpressad nattljusolja standardiserad till 9–10 % GLA.',
        warnings=['Sluta två veckor före en operation',
                  'Använd den med försiktighet om du har haft krampanfall',
                  'Undvik under graviditet om det inte sker under medicinsk uppföljning'],
        interactions='Nattljusolja kan öka risken för blödning tillsammans med blodförtunnande och blodplättshämmande '
                     'läkemedel (warfarin, acetylsalicylsyra, klopidogrel), och bör undvikas med fentiaziner eftersom den '
                     'kan sänka kramptröskeln.',
        naturalSources='Gurkörtsfröolja, svartvinbärsfröolja och hampfröolja.'),
    'black-cohosh': dict(
        summary='Roten av en nordamerikansk växt som används för att stödja välbefinnandet under klimakteriet; en metaanalys '
                'tyder på att den minskar värmevallningar och nattliga svettningar med cirka 26 %, det spanska sällskapet '
                'för klimakteriet bekräftar effekten och säkerheten hos standardiserade extrakt, och den hjälper till att '
                'lugna humörsvängningar och dålig sömn i den här livsfasen.',
        dosage=dict(recommended='40–80 mg standardiserat extrakt per dag', timing='Till frukost eller middag',
                    frequency='1–2 gånger per dag'),
        forms='Standardiserat isopropanol- eller etanolextrakt av silveraxrot (som Remifemin®).',
        warnings=['Levervarning (EMA): undvik den vid leversjukdom; sluta genast och kontakta läkare om huden eller ögonen '
                  'gulnar, urinen blir mörk eller du får smärta i övre delen av buken',
                  'Inte för kvinnor som har haft östrogenkänsliga tumörer (som bröstcancer) utan medicinsk uppföljning',
                  'Använd den inte i mer än 6 månader utan att rådgöra med läkare; ska inte användas under graviditet eller '
                  'amning'],
        interactions='Använd den med försiktighet tillsammans med läkemedel som belastar levern (som höga doser paracetamol '
                     'och statiner), och kombinera den inte med hormonersättningsbehandling eller tamoxifen utan medicinsk '
                     'uppföljning.',
        naturalSources='Finns inte i maten; roten används som örtextrakt.'),
    'phosphatidic-acid': dict(
        summary='En naturlig fosfolipid som fungerar som signalmolekyl och aktiverar mTOR, signalvägen som driver '
                'muskelproteinsyntesen; kliniska studier tyder på att intag tillsammans med styrketräning stödjer större '
                'ökningar av fettfri massa och styrka än enbart träning.',
        dosage=dict(recommended='750 mg per dag',
                    timing='30–60 minuter före träning på träningsdagar, och till en måltid på vilodagar',
                    frequency='En gång per dag'),
        forms='Fosfatidsyra utvunnen ur sojalecitin (Mediator®), i kapslar.',
        warnings=['Framställd av soja; undvik den om du är allergisk mot soja',
                  'Den tolererades väl i studier som varade upp till 8 veckor; långsiktiga säkerhetsdata saknas',
                  'Den hjälper bara tillsammans med ett regelbundet styrketräningsprogram'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats vid de vanliga doserna.',
        naturalSources='Små mängder i kål, spenat och sojalecitin.'),
    'ursolic-acid': dict(
        summary='Ett växtämne som finns i äppelskal, rosmarin och basilika; djurstudier tyder på att det bevarar '
                'muskelmassan och stödjer brunt fett och insulinkänsligheten, och en liten studie på människor tyder på att '
                'det stödjer muskelstyrkan tillsammans med styrketräning, även om evidensen från människor fortfarande är '
                'begränsad.',
        dosage=dict(recommended='150–300 mg per dag', timing='Till huvudmåltider som innehåller fett, för bättre upptag',
                    frequency='1–2 gånger per dag'),
        forms='Extrakt av äppelskal eller rosmarin standardiserat för ursolsyra, i kapslar.',
        warnings=['Evidensen från människor är begränsad; de flesta resultat kommer från djurstudier',
                  'Undvik under graviditet och amning, eftersom säkerhetsdata är otillräckliga'],
        interactions='Ursolsyra kan sänka blodsockret något, så använd den med försiktighet tillsammans med diabetesläkemedel.',
        naturalSources='Äppelskal, rosmarin, basilika, timjan och tranbär.'),
    'shilajit': dict(
        summary='Ett naturligt harts från Himalayas klippor rikt på fulvosyra och mineraler; en dubbelblind studie tyder på '
                'att det stödjer normala nivåer av totalt och fritt testosteron hos friska män efter 90 dagar, och en annan '
                'att det hjälper till att bibehålla muskelstyrkan mot träningströtthet.',
        dosage=dict(recommended='250–500 mg per dag', timing='På morgonen till frukost, eller upplöst i varmt vatten',
                    frequency='1–2 gånger per dag'),
        forms='Renad, standardiserad shilajit (som PrimaVie®) testad fri från tungmetaller och mykotoxiner, i kapslar.',
        warnings=['Använd aldrig rå, orenad shilajit, eftersom den kan vara förorenad med tungmetaller',
                  'Undvik den vid hemokromatos (järnöverskott) eller gikt',
                  'Ska inte användas under graviditet, amning eller före 18 års ålder'],
        interactions='Shilajit kan förstärka blodtrycks- och diabetesläkemedel; kombinera det inte med '
                     'testosteronersättning (TRT).',
        naturalSources='Finns inte i maten; den samlas in från sprickor i bergsklippor.'),
})

# third batch, part B
COPY.update({
    'dong-quai': dict(
        summary="En rot som i traditionell kinesisk medicin kallas 'kvinnornas ginseng'; den används traditionellt för att "
                'stödja cirkulationen i bäckenområdet, välbefinnandet under menstruationen och varma händer och fötter, även '
                'om modern klinisk evidens fortfarande är begränsad.',
        dosage=dict(recommended='500–1000 mg rotpulver (eller 200–400 mg standardiserat extrakt)',
                    timing='Till lunch med ett stort glas vatten', frequency='En gång per dag'),
        forms='Torkat rotpulver av dong quai, eller extrakt standardiserat för ferulsyra eller ligustilid.',
        warnings=['Ska inte användas under graviditet, eftersom den kan utlösa livmodersammandragningar; undvik under amning',
                  'Undvik den vid östrogenkänsliga tillstånd eller riklig menstruationsblödning',
                  'Den kan göra huden mer känslig för solljus; använd solskydd'],
        interactions='Viktig varning: den innehåller kumariner som kan förstärka warfarin, blodförtunnande och '
                     'blodplättshämmande läkemedel och öka risken för blödning; sluta två veckor före en operation.',
        naturalSources='Ingår inte i västerländsk mat; roten används i soppor och te i det kinesiska köket.'),
    'vitex': dict(
        summary='Frukten av en buske från Medelhavsområdet som verkar på dopaminreceptorer i hypofysen och hjälper till att '
                'reglera frisättningen av prolaktin; en metaanalys av randomiserade studier tyder på att den lindrar '
                'premenstruella besvär som ömma bröst, humörsvängningar och irritabilitet.',
        dosage=dict(recommended='20–40 mg standardiserat torrextrakt per dag (eller 200–400 mg fruktpulver)',
                    timing='På morgonen på nästan tom mage', frequency='En gång per dag, under minst 3 menstruationscykler'),
        forms='Standardiserat torrextrakt av munkpepparfrukt (som Ze 440 eller BNO 1095), eller fruktpulver.',
        warnings=['Ska inte användas under graviditet eller amning',
                  'Undvik den vid östrogenkänsliga tillstånd eller sjukdomar i hypofysen',
                  'Kan ge lätt illamående, huvudvärk eller hudutslag'],
        interactions='Munkpeppar kan störa hormonella preventivmedel och hormonbehandling, och läkemedel som verkar på dopamin '
                     '(dopaminagonister som bromokriptin, och antipsykotiska läkemedel).',
        naturalSources='Ingår inte i vanlig mat; frukten användes förr som ersättning för peppar.'),
    'wild-yam': dict(
        summary='En traditionell rot rik på diosgenin; den används traditionellt för att lindra kramper i tarmen och '
                'bäckenets muskler. Diosgenin omvandlas inte till progesteron eller andra hormoner i kroppen, trots vad '
                'marknadsföringen påstår, och en klinisk studie fann ingen märkbar effekt på klimakteriebesvär eller '
                'hormonnivåer.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt per dag', timing='Till kvällsmåltiden',
                    frequency='En gång per dag'),
        forms='Extrakt av vild jamsrot standardiserat till 10–16 % diosgenin, i kapslar.',
        warnings=['Den ersätter inte hormonbehandling, och krämer eller kapslar med vild jams innehåller inget riktigt '
                  'progesteron',
                  'Höga doser kan ge magbesvär eller illamående',
                  'Undvik under graviditet och amning och vid östrogenkänsliga tillstånd'],
        interactions='Teoretiskt kan den störa p-piller, hormonbehandling och östradiol; fråga din läkare innan du kombinerar dem.',
        naturalSources='Vild jams äts inte som mat; ätliga jamsarter (Dioscorea) äts kokta i Afrika och Asien.'),
    'ceramides': dict(
        summary='Växtlipider som liknar de ceramider som bygger upp hudbarriären och minskar med åldern; dubbelblinda studier '
                'tyder på att intag via munnen stödjer hudens fuktighet, elasticitet och mjukhet och minskar vattenförlusten '
                'genom huden.',
        dosage=dict(recommended='100–350 mg extrakt per dag', timing='Till en måltid som innehåller fett',
                    frequency='En gång per dag'),
        forms='Ceramider utvunna ur glutenfritt vete (Lipowheat®) eller ur ris eller konjak, i kapslar.',
        warnings=['Säkra och väl tolererade',
                  'För personer med celiaki eller veteallergi är ceramider från ris eller konjak det bättre valet'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats.',
        naturalSources='Vete, ris, sötpotatis, konjak och sojabönor.'),
    'hyaluronic-acid': dict(
        summary='En molekyl som binder stora mängder vatten och finns naturligt i huden och ledvätskan; en dubbelblind '
                'studie och en ny analys tyder på att intag via munnen stödjer hudens fuktighet och elasticitet och mildrar '
                'synliga fina linjer, och den används också för att stödja smidiga och bekväma leder.',
        dosage=dict(recommended='100–200 mg per dag', timing='På morgonen eller till lunch, med ett stort glas vatten',
                    frequency='En gång per dag'),
        forms='Natriumhyaluronat med låg till medelhög molekylvikt framställt genom fermentering, i kapslar.',
        warnings=['Säkert och väl tolererat hos vuxna',
                  'Rekommenderas inte under graviditet, amning eller för barn, eftersom data är otillräckliga',
                  'Drick tillräckligt med vatten under dagen'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats.',
        naturalSources='Benbuljong, fågelskinn och brosk (i små mängder).'),
    'krill-oil': dict(
        summary='En marin källa till EPA och DHA bundna till fosfolipider, naturligt rik på astaxantin; EPA och DHA bidrar '
                'till att hjärtat fungerar normalt vid 250 mg per dag (EFSA-godkänt påstående), och kliniska studier tyder '
                'på att krillolja stödjer normala triglyceridnivåer och ledernas komfort.',
        dosage=dict(recommended='1000–1500 mg krillolja per dag (som ger minst 250 mg EPA och DHA tillsammans)',
                    timing='Till en måltid som innehåller fett', frequency='En gång per dag'),
        forms='Krilloljekapslar från certifierat antarktiskt fiske (som MSC), som ger EPA och DHA i fosfolipidform med '
              'astaxantin.',
        warnings=['Inte för personer som är allergiska mot kräftdjur eller skaldjur',
                  'Sluta två veckor före en operation',
                  'Undvik under graviditet och amning om det inte sker under medicinsk uppföljning'],
        interactions='Krillolja kan förstärka blodförtunnande och blodplättshämmande läkemedel (warfarin, acetylsalicylsyra, '
                     'klopidogrel) och sänka blodtrycket ytterligare tillsammans med blodtryckssänkande läkemedel.',
        naturalSources='Fet fisk (lax, makrill, sardiner, sill) och skaldjur.'),
    'magnesium-threonate': dict(
        summary='En form av magnesium som är framtagen för att höja magnesiumhalten i hjärnan; magnesium bidrar till '
                'nervsystemets normala funktion, till normal psykologisk funktion och till att minska trötthet och '
                'utmattning (EFSA-godkända påståenden), en djurstudie tyder på att det stödjer inlärning och minne, och en '
                'ny klinisk studie tyder på att det förbättrar sömnkvaliteten och funktionen under dagen.',
        dosage=dict(recommended='1000–2000 mg Magtein® per dag (som ger cirka 72–144 mg elementärt magnesium)',
                    timing='En dos till lunch och en en timme före sänggåendet', frequency='Fördelat på två doser'),
        forms='Varumärkt magnesium-L-treonat (Magtein®), i kapslar eller pulver.',
        warnings=['EFSA:s övre gräns för magnesium från kosttillskott är 250 mg per dag; räkna med magnesiumet i alla dina '
                  'tillskott',
                  'Använd det med försiktighet om du har njursvikt, eftersom njurarna gör sig av med magnesium',
                  'Det är skonsammare mot tarmen än andra magnesiumformer, men kan ge dåsighet eller lätt huvudvärk'],
        interactions='Det minskar upptaget av tetracykliner, kinolonantibiotika och läkemedel mot benskörhet '
                     '(bisfosfonater), så ta det med minst två timmars mellanrum från dem.',
        naturalSources='Magnesium: mörka bladgrönsaker, nötter och frön, baljväxter, fullkorn och mörk choklad.'),
    'copper': dict(
        summary='Ett spårämne som bidrar till normal transport av järn i kroppen, till normal pigmentering av hår och hud, '
                'till att bibehålla normal bindväv, till immunsystemets och nervsystemets normala funktion och till att '
                'skydda cellerna mot oxidativ stress (EFSA-godkända påståenden); koppar är en nödvändig partner vid '
                'långvarigt intag av zinktillskott.',
        dosage=dict(recommended='1–2 mg per dag (referensintaget är 1 mg och EFSA:s adekvata intag är 1,3–1,6 mg för vuxna)',
                    timing='Till lunch', frequency='En gång per dag'),
        forms='Kopparglukonat eller kopparbisglycinatkelat.',
        warnings=['EFSA:s övre gräns för vuxna är 5 mg per dag från alla källor',
                  'Inte för personer med Wilsons sjukdom (ärftlig kopparansamling)',
                  'Ta inte höga doser ensamt utan behov eller provsvar'],
        interactions='Höga doser zink minskar upptaget av koppar, så ta dem med två timmars mellanrum; koppar minskar upptaget '
                     'av tetracykliner, kinolonantibiotika och penicillamin.',
        naturalSources='Lever, ostron, cashewnötter och andra nötter, sesamfrön, mörk choklad och baljväxter.'),
    'plant-sterols-and-stanols': dict(
        summary='Växtsteroler och växtstanoler har visats sänka kolesterolhalten i blodet. Högt kolesterol är en riskfaktor '
                'för utveckling av kranskärlssjukdom. Ett dagligt intag av 1,5–2,4 g sänker kolesterolet med 7–10 % inom '
                '2–3 veckor (EFSA-godkänt påstående), eftersom de konkurrerar med kolesterolet om upptaget i tarmen.',
        dosage=dict(recommended='1,5–3 g per dag (överskrid inte 3 g per dag från alla källor)',
                    timing='Till huvudmåltiden som innehåller fett', frequency='1–2 gånger per dag'),
        forms='Växtsterol- eller växtstanolestrar i kapslar, eller tillsatta i berikade livsmedel.',
        warnings=['Endast avsett för personer som vill sänka sitt kolesterol; passar inte gravida, ammande eller barn under '
                  '5 år',
                  'Personer som tar kolesterolsänkande läkemedel bör rådgöra med sin läkare före användning',
                  'De kan minska upptaget av betakaroten något; ät rikligt med färgstarka frukter och grönsaker'],
        interactions='De förstärker effekten av kolesterolläkemedel (statiner, ezetimib), så rådgör med din läkare när du '
                     'kombinerar dem.',
        naturalSources='Vegetabiliska oljor, nötter och frön, baljväxter och fullkorn (i mängder långt under den verksamma '
                       'dosen).'),
    'red-yeast-rice': dict(
        summary='Ris som fermenterats med svampen Monascus purpureus, som bildar monakolin K, en hämmare av HMG-CoA-reduktas, '
                'enzymet som bildar kolesterol i levern; en placebokontrollerad studie och en översikt i JACC tyder på att '
                'det stödjer normala nivåer av totalkolesterol och LDL-kolesterol.',
        dosage=dict(recommended='Mindre än 3 mg monakolin K per dag (EU:s lagstadgade gräns enligt förordning (EU) 2022/860)',
                    timing='På kvällen till middagen', frequency='En gång per dag'),
        forms='Extrakt av röd jästris standardiserat för monakolin K (mindre än 3 mg per daglig portion) och testat fritt '
              'från citrinin.',
        warnings=['Obligatoriska varningar (EU 2022/860): inte för gravida eller ammande, personer under 18 år eller personer '
                  'över 70 år',
                  'Använd det inte tillsammans med någon annan produkt som innehåller röd jästris, eller med '
                  'kolesterolsänkande läkemedel',
                  'Kontakta läkare om något hälsoproblem uppstår, särskilt oförklarlig muskelsmärta eller muskelsvaghet'],
        interactions='Viktig varning: kombinera det aldrig med statiner eller fibrater. CYP3A4-hämmare (grapefruktjuice, '
                     'klaritromycin, itrakonazol, vissa hivläkemedel) ökar risken för muskelskador.',
        naturalSources='Ingår inte i västerländsk mat; fermenterat rött ris används traditionellt som livsmedelsfärg i det '
                       'asiatiska köket.'),
    'nattokinase': dict(
        summary='Ett enzym från japanska fermenterade sojabönor (natto) som kan bryta ned proteinet fibrin; en randomiserad '
                'studie tyder på att det stödjer normalt blodtryck och normala nivåer av von Willebrand-faktor, och en annan '
                'studie på människor att det stödjer normala nivåer av fibrinogen och koagulationsfaktorer, vilket hjälper '
                'blodet att flöda fritt.',
        dosage=dict(recommended='2000 FU per dag (cirka 100 mg)',
                    timing='På fastande mage: en halvtimme före frukost eller en timme före sänggåendet',
                    frequency='En gång per dag'),
        forms='Nattokinas standardiserat i fibrinolytiska enheter (FU), renat och fritt från K2-vitamin (som NSK-SD®), i kapslar.',
        warnings=['Inte för personer med blödningsrubbningar eller aktivt magsår; sluta två veckor före en operation eller ett '
                  'tandingrepp',
                  'Undvik det om du är allergisk mot soja',
                  'Ska inte användas under graviditet eller amning'],
        interactions='Viktig varning: kombinera det inte med blodförtunnande eller blodplättshämmande läkemedel (warfarin, '
                     'heparin, acetylsalicylsyra, klopidogrel, nyare antikoagulantia) utan medicinsk uppföljning, på grund av '
                     'risken för blödning. Det kan också förstärka blodtryckssänkande läkemedel.',
        naturalSources='Natto (japanska fermenterade sojabönor).'),
    'bromelain': dict(
        summary='En blandning av proteinnedbrytande enzymer från ananasstjälkar; till maten hjälper den till att smälta '
                'protein, och mellan måltiderna används den för att stödja ledernas komfort och minska svullnad, och en '
                'klinisk studie tyder på att den lindrar lätta knäbesvär och förbättrar välbefinnandet hos friska vuxna.',
        dosage=dict(recommended='500 mg per dag',
                    timing='För matsmältningen: till en proteinrik måltid. För ledernas komfort: mellan måltiderna på tom mage',
                    frequency='1–2 gånger per dag'),
        forms='Bromelain standardiserat för enzymaktivitet (minst 2400 GDU/g), i kapslar eller tabletter.',
        warnings=['Undvik det om du är allergisk mot ananas, latex, papain eller gräspollen',
                  'Sluta två veckor före en operation och undvik det vid aktivt magsår',
                  'Undvik under graviditet och amning'],
        interactions='Bromelain ökar upptaget av vissa antibiotika (amoxicillin, tetracyklin) och kan förstärka '
                     'blodförtunnande och blodplättshämmande läkemedel.',
        naturalSources='Färsk ananas (särskilt kärnan och stjälken).'),
    'papain': dict(
        summary='Ett proteinnedbrytande enzym från saven i omogen papaya; det hjälper till att bryta ned proteinerna i kött '
                'och baljväxter, och en klinisk studie av ett papayapreparat tyder på att det lindrar matsmältningsbesvär, '
                'uppblåsthet och förstoppning.',
        dosage=dict(recommended='100–300 mg till en måltid', timing='Med första tuggan av en proteinrik huvudmåltid',
                    frequency='Till huvudmåltiderna'),
        forms='Rent papainpulver standardiserat i USP-enheter, eller tuggtabletter av papaya.',
        warnings=['Undvik det om du är allergisk mot papaya, latex, kiwi eller fikon',
                  'Ska inte användas i tillskottsdoser under graviditet',
                  'Undvik det vid aktivt magsår'],
        interactions='Papain kan förstärka warfarin och höja PK(INR); följ dina värden när du kombinerar dem.',
        naturalSources='Färsk papaya (särskilt omogen).'),
    'full-spectrum-digestive-enzymes': dict(
        summary='En blandning av enzymer som hjälper till att smälta måltidens olika delar: amylas för stärkelse, proteas för '
                'protein, lipas för fett och laktas för mjölksocker; en randomiserad studie tyder på att ett '
                'multienzymkomplex lindrar symtomen vid funktionell dyspepsi och uppblåsthet.',
        dosage=dict(recommended='1–2 kapslar till en måltid', timing='Med första tuggan av en huvudmåltid',
                    frequency='Till huvudmåltiderna'),
        forms='Ett enzymkomplex från växter eller mikroorganismer (som DigeZyme®) i kapslar.',
        warnings=['Undvik det vid aktivt magsår eller akut bukspottkörtelinflammation',
                  'Det ersätter inte förskrivna bukspottkörtelenzymer vid bukspottkörtelsvikt',
                  'Kontakta läkare om matsmältningsbesvären varar mer än två veckor'],
        interactions='Akarbos och miglitol kan minska effekten av amylas; använd det med försiktighet tillsammans med '
                     'blodförtunnande läkemedel om det innehåller bromelain eller papain.',
        naturalSources='Ananas, papaya, kiwi, mango och fermenterade livsmedel (kefir, surkål).'),
    'l-tyrosine': dict(
        summary='En aminosyra som kroppen använder för att bilda dopamin, noradrenalin och sköldkörtelhormoner; en klinisk '
                'översikt tyder på att den stödjer mental prestation och arbetsminne i krävande situationer, som sömnbrist '
                'och hård mental stress, när dessa signalsubstanser tar slut.',
        dosage=dict(recommended='500–1000 mg (upp till 1500 mg under perioder med hård mental belastning)',
                    timing='På morgonen på fastande mage, 30 minuter före maten, med ett glas vatten',
                    frequency='En gång per dag vid behov'),
        forms='L-tyrosin i fri form i kapslar eller pulver, eller N-acetyl-L-tyrosin (NALT).',
        warnings=['Inte för personer med överfunktion i sköldkörteln eller Graves sjukdom',
                  'Undvik det vid melanom eller svår fenylketonuri (PKU)',
                  'Undvik under graviditet och amning'],
        interactions='Viktig varning: kombinera det aldrig med antidepressiva MAO-hämmare på grund av risken för en kraftig '
                     'blodtrycksstegring; använd det med försiktighet tillsammans med sköldkörtelläkemedel (levotyroxin) och '
                     'levodopa.',
        naturalSources='Ägg, kyckling, fisk, ost, sojabönor och mandlar.'),
    'vitamin-b12': dict(
        summary='B12-vitamin bidrar till nervsystemets normala funktion, till normal psykologisk funktion, till normal '
                'bildning av röda blodkroppar, till normal energiomsättning och till att minska trötthet och utmattning '
                '(EFSA-godkända påståenden); veganer, äldre och personer som länge tar metformin eller syrahämmande '
                'läkemedel behöver det mest.',
        dosage=dict(recommended='500–1000 µg per dag (referensintaget är 2,5 µg; högre doser kompenserar för ett dåligt upptag)',
                    timing='På morgonen till frukost', frequency='En gång per dag'),
        forms='Metylkobalamin eller adenosylkobalamin, eller det stabila cyanokobalaminet; sublinguala tabletter finns.',
        warnings=['Ett mycket säkert vattenlösligt vitamin; EFSA har inte fastställt någon övre gräns',
                  'Bestående domningar i händer eller fötter kräver ett blodprov för B12 hos din läkare',
                  'Veganer behöver en regelbunden källa till B12'],
        interactions='Metformin, protonpumpshämmare (som omeprazol) och H2-blockerare sänker upptaget av B12 vid långvarig '
                     'användning; ta höga doser C-vitamin med två timmars mellanrum.',
        naturalSources='Lever, skaldjur, fisk, rött kött, ägg och mejeriprodukter.'),
    'potassium-citrate': dict(
        summary='Kalium bidrar till att bibehålla ett normalt blodtryck och till normal muskelfunktion och nervsystemets '
                'normala funktion (EFSA-godkända påståenden); en metaanalys i BMJ kopplar ett högre kaliumintag till ett '
                'hälsosammare blodtryck, särskilt vid en salt kost.',
        dosage=dict(recommended='200–400 mg elementärt kalium (det totala dagliga behovet enligt EFSA är cirka 3500 mg, '
                                'främst från maten)',
                    timing='Till en hel måltid med ett stort glas vatten', frequency='1–2 gånger per dag'),
        forms='Kaliumcitrat i kapslar eller pulver; citratformen är skonsam mot magen.',
        warnings=['Inte för personer med njursvikt eller högt kalium i blodet',
                  'Överskrid inte dosen utan provsvar, eftersom för mycket kalium kan störa hjärtrytmen',
                  'Kan ge lätta magbesvär'],
        interactions='Viktig varning: kombinera det inte med kaliumsparande diuretika (spironolakton, amilorid), '
                     'ACE-hämmare, angiotensinreceptorblockerare eller saltersättning med kalium utan medicinsk uppföljning.',
        naturalSources='Bananer, potatis, avokado, spenat, baljväxter, torkade aprikoser och yoghurt.'),
    'silica': dict(
        summary='Kisel deltar i uppbyggnaden av kollagen och bindväv i hud, hår, naglar och skelett; en klinisk studie tyder '
                'på att kolinstabiliserad ortokiselsyra (ch-OSA) stödjer styrkan och tjockleken hos tunt hår hos kvinnor.',
        dosage=dict(recommended='10 mg elementärt kisel (ch-OSA), eller 300–500 mg standardiserat åkerfräkenextrakt',
                    timing='Till lunch med rikligt med vatten', frequency='En gång per dag'),
        forms='Kolinstabiliserad ortokiselsyra (ch-OSA), den form som tas upp bäst, eller standardiserat åkerfräkenextrakt '
              'fritt från tiaminas.',
        warnings=['Åkerfräkenextrakt måste vara fritt från tiaminas, eftersom tiaminas tömmer förråden av B1-vitamin',
                  'Undvik åkerfräken vid njur- eller hjärtsjukdom, eftersom den är vätskedrivande',
                  'Undvik under graviditet och amning'],
        interactions='Åkerfräken kan förstärka vätskedrivande läkemedel och sänka kaliumet; använd den med försiktighet '
                     'tillsammans med litium och digoxin.',
        naturalSources='Havre, korn och fullkornsris, bananer, gröna bönor och mineralvatten.'),
    'pumpkin-seed-oil': dict(
        summary='En kallpressad olja rik på växtsteroler, linolsyra och E-vitamin; en ettårig klinisk studie tyder på att '
                'den stödjer bekväm vattenkastning hos äldre män, och en annan randomiserad studie rapporterar mer hår hos '
                'män med ärftligt håravfall.',
        dosage=dict(recommended='1000–2000 mg olja per dag', timing='Till en huvudmåltid', frequency='1–2 gånger per dag'),
        forms='Kapslar med kallpressad pumpafröolja, eller hela pumpafrön.',
        warnings=['Mycket säker och väl tolererad',
                  'Svårigheter att kissa eller blod i urinen kräver en läkarkontroll för att utesluta andra orsaker'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats; berätta för din läkare om du tar '
                     'prostataläkemedel.',
        naturalSources='Råa eller rostade pumpafrön.'),
    'sage-extract': dict(
        summary='En ört från Medelhavsområdet som används traditionellt för att minska kraftig svettning (traditionell '
                'användning enligt EMA); en multicenterstudie rapporterar ungefär 50–64 % färre värmevallningar hos kvinnor '
                'i klimakteriet med ett preparat av färsk salvia, och en studie med en närbesläktad salviaart tyder på stöd '
                'för korttidsminnet.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt med låg tujonhalt per dag', timing='Till frukost eller middag',
                    frequency='En gång per dag'),
        forms='Tabletter eller standardiserat extrakt av salviablad med låg tujonhalt.',
        warnings=['Ska inte användas under graviditet eller amning; salvia kan minska mjölkproduktionen',
                  'Inte för personer med epilepsi, eftersom tujon kan sänka kramptröskeln',
                  'Använd endast produkter med låg tujonhalt, och överskrid inte dosen'],
        interactions='Salvia kan interagera med läkemedel mot epilepsi, lugnande medel och diabetesläkemedel; fråga din läkare '
                     'innan du kombinerar dem.',
        naturalSources='Färska eller torkade salviablad (används i te och matlagning).'),
    'anise-seeds': dict(
        summary='Aromatiska frön rika på anetol som används traditionellt för att lindra kramper i matsmältningen, '
                'uppblåsthet och gaser (traditionell användning enligt EMA); en klinisk studie tyder på att enterodragerade '
                'kapslar med anisolja lindrade symtomen vid IBS.',
        dosage=dict(recommended='1–2 g fröpulver (eller 300–600 mg standardiserat extrakt)',
                    timing='Efter en måltid med en kopp varmt vatten', frequency='1–3 gånger per dag'),
        forms='Pulver av anisfrön eller te, eller enterodragerade kapslar med anisolja.',
        warnings=['Undvik det om du är allergisk mot flockblommiga växter (selleri, fänkål, koriander)',
                  'Undvik den koncentrerade oljan under graviditet, amning och hos barn, och vid östrogenkänsliga tillstånd'],
        interactions='Teoretiskt kan anis störa hormonbehandling, p-piller och tamoxifen, eftersom anetol har en svag '
                     'östrogenliknande effekt.',
        naturalSources='Anisfrön (används i te och bakning).'),
    'chamomile-flowers': dict(
        summary='Blommor rika på flavonoiden apigenin, som binder till GABA-receptorer i hjärnan; en långvarig klinisk studie '
                'tyder på att ett standardiserat kamomillextrakt stödde lugnet och lindrade ångestsymtom, och kamomill '
                'används traditionellt för att lindra kramper i mage och tarm.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt per dag',
                    timing='45 minuter före sänggåendet, eller efter måltiderna för magens komfort',
                    frequency='1–2 gånger per dag'),
        forms='Kamomillextrakt standardiserat till 1,2 % apigenin, eller te på blommorna.',
        warnings=['Undvik det om du är allergisk mot korgblommiga växter (ambrosia, krysantemum)',
                  'Kan ge dåsighet; kör inte bil efter intag',
                  'Undvik det koncentrerade extraktet under graviditet'],
        interactions='Kamomill förstärker lugnande medel och sömnmedel och kan förstärka warfarin och andra blodförtunnande '
                     'läkemedel.',
        naturalSources='Kamomillte.'),
    'cumin-seeds': dict(
        summary='Aromatiska frön som används traditionellt för att stödja matsmältningen och lindra uppblåsthet; '
                'metaanalyser av kliniska studier tyder på att tillskott av spiskummin kan stödja normala nivåer av '
                'blodfetter och blodsocker och viktmått som en del av en hälsosam livsstil.',
        dosage=dict(recommended='300–500 mg koncentrerat extrakt (eller 1–2 g pulver)',
                    timing='15 minuter före huvudmåltiderna med ett glas vatten', frequency='1–2 gånger per dag'),
        forms='Koncentrerat extrakt av spiskumminfrön i kapslar, eller fröpulver.',
        warnings=['Säkert i de mängder som används i mat och i vanliga doser',
                  'Undvik det koncentrerade extraktet under graviditet och amning',
                  'Sluta två veckor före en operation'],
        interactions='Spiskummin kan sänka blodsockret ytterligare tillsammans med diabetesläkemedel och kan förstärka '
                     'blodförtunnande läkemedel.',
        naturalSources='Spiskumminfrön (används i matlagning och kryddblandningar).'),
    'hibiscus-flower-tea': dict(
        summary='Blommor rika på antocyaner och polyfenoler; en metaanalys av randomiserade studier tyder på att hibiskus '
                'stödjer normalt systoliskt och diastoliskt blodtryck, en klinisk studie bekräftar detta hos vuxna med lätt '
                'förhöjt blodtryck, och den har en lätt vätskedrivande effekt.',
        dosage=dict(recommended='400–800 mg standardiserat extrakt per dag (eller 2–3 koppar te)',
                    timing='Till frukost eller lunch', frequency='1–2 gånger per dag'),
        forms='Hibiskusextrakt standardiserat för antocyaner i kapslar, eller te på blommorna.',
        warnings=['Undvik det om du har lågt blodtryck',
                  'Undvik under graviditet och amning',
                  'Rådgör med din läkare om du behandlar ditt blodtryck med läkemedel'],
        interactions='Hibiskus kan förstärka blodtryckssänkande och vätskedrivande läkemedel (som hydroklortiazid) och kan '
                     'minska upptaget av klorokin; följ dina värden när du kombinerar dem.',
        naturalSources='Hibiskuste (varmt eller iskallt).'),
    'glutathione': dict(
        summary='En tripeptid som är en av de viktigaste antioxidanterna inne i cellerna och hjälper till att återvinna C- och '
                'E-vitamin; en randomiserad studie tyder på att intag via munnen höjer kroppens glutationförråd, och en '
                'översikt pekar på stöd för en strålande, jämn hudton.',
        dosage=dict(recommended='250 mg per dag', timing='På morgonen på fastande mage', frequency='En gång per dag'),
        forms='Reducerat glutation framställt genom fermentering (som Setria®), eller den liposomala formen.',
        warnings=['Tolereras väl; kan ge lätt uppblåsthet',
                  'Undvik under graviditet och amning, eftersom data är otillräckliga',
                  'Personer med astma: undvik inhalerat glutation, och använd formen som tas via munnen endast efter samråd '
                  'med läkare'],
        interactions='Använd det inte under cytostatikabehandling utan din specialists godkännande, eftersom det kan påverka '
                     'hur vissa läkemedel verkar.',
        naturalSources='Kroppen bildar det av cystein, glycin och glutamat; finns i sparris, avokado och spenat.'),
})

# third batch, part C
COPY.update({
    'artichoke-extract': dict(
        summary='Blad rika på cynarin och luteolin som stimulerar gallflödet; en klinisk studie tyder på att '
                'kronärtskocksextrakt lindrade matsmältningsbesvär och uppblåsthet efter feta måltider, och en metaanalys '
                'tyder på att det stödjer normala nivåer av kolesterol och triglycerider.',
        dosage=dict(recommended='300–600 mg standardiserat extrakt per dag',
                    timing='15 minuter före huvudmåltiderna med ett glas vatten', frequency='1–2 gånger per dag'),
        forms='Kronärtskocksbladsextrakt standardiserat till 2,5–5 % cynarin.',
        warnings=['Ska inte användas vid gallgångshinder; rådgör med läkare om du har gallsten',
                  'Undvik det om du är allergisk mot korgblommiga växter',
                  'Undvik under graviditet och amning'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats; använd det med försiktighet tillsammans med '
                     'kolesterolläkemedel.',
        naturalSources='Färska eller konserverade kronärtskockor (hjärtan och blad).'),
    'cranberry-extract': dict(
        summary='Rikt på proantocyanidiner av typ A (PAC), som hindrar E. coli-bakterier från att fästa vid blåsväggen; den '
                'uppdaterade Cochraneöversikten (2023) kopplar tranbärsprodukter till färre återkommande urinvägsbesvär hos '
                'mottagliga kvinnor och hos barn.',
        dosage=dict(recommended='En mängd som ger minst 36 mg PAC per dag',
                    timing='På kvällen före sänggåendet med ett stort glas vatten', frequency='En gång per dag'),
        forms='Standardiserat tranbärsextrakt som ger minst 36 mg PAC per dag.',
        warnings=['Det ersätter inte ett läkarbesök om du har kraftig sveda, feber, ryggsmärta eller blod i urinen',
                  'Använd det med försiktighet om du har haft njursten av oxalat'],
        interactions='Tranbär kan förstärka warfarin och höja PK(INR); följ dina värden när du kombinerar dem.',
        naturalSources='Färska eller osötade torkade tranbär och osötad tranbärsjuice.'),
    'nettle-leaf-root': dict(
        summary='En växt med två användningsområden: en klinisk studie på 620 män tyder på att extrakt av nässelrot stödde '
                'urinflödet och bekväm vattenkastning hos äldre män, medan en laboratoriestudie tyder på att bladextraktet '
                'verkar på histaminreceptorer, vilket kan stödja välbefinnandet under pollensäsongen.',
        dosage=dict(recommended='Rot: 300–600 mg extrakt. Blad: 300–500 mg extrakt', timing='Till måltiderna',
                    frequency='1–2 gånger per dag'),
        forms='Extrakt av nässelrot för bekväm vattenkastning, och frystorkat bladextrakt för våren.',
        warnings=['Lätt vätskedrivande; drick tillräckligt med vatten',
                  'Långvariga svårigheter att kissa kräver en läkarkontroll för att utesluta andra orsaker',
                  'Undvik under graviditet och amning'],
        interactions='Brännässla kan förstärka vätskedrivande, blodtryckssänkande och diabetesläkemedel och höja '
                     'litiumnivåerna; nässelblad är rika på K-vitamin, så var försiktig med warfarin.',
        naturalSources='Kokta färska nässelblad (nässelsoppa) och nässelte.'),
    'beta-glucan': dict(
        summary='Fiber från jästens cellvägg eller från havre. Betaglukan från havre har visats sänka kolesterolhalten i '
                'blodet vid 3 g per dag (EFSA-godkänt påstående), och högt kolesterol är en riskfaktor för kranskärlssjukdom; '
                'en klinisk studie tyder på att betaglukan från jäst minskade svårighetsgraden av symtom från de övre '
                'luftvägarna.',
        dosage=dict(recommended='Immunförsvar: 250 mg betaglukan från jäst. Kolesterol: 3 g betaglukan från havre fördelat '
                                'på måltiderna',
                    timing='På morgonen med ett glas vatten, eller till måltiderna för havre', frequency='Dagligen'),
        forms='Betaglukan från jäst (β-1,3/1,6) för immunförsvaret, och betaglukan från havre eller havrekli för kolesterolet.',
        warnings=['Tolereras väl; betaglukan från havre kan ge lätta gaser i början',
                  'Rådgör med läkare om du har en autoimmun sjukdom eller Crohns sjukdom',
                  'Personer med celiaki bör välja betaglukan från jäst eller certifierat glutenfri havre'],
        interactions='Betaglukan kan störa immunhämmande läkemedel; ta havrefiber med två timmars mellanrum från andra '
                     'läkemedel, eftersom den kan minska deras upptag.',
        naturalSources='Havre och havrekli, korn, svamp och bakjäst.'),
    'cluster-dextrin': dict(
        summary='En starkt förgrenad kolhydrat med hög molekylvikt och låg osmolalitet som lämnar magen snabbt med mindre '
                'tyngdkänsla; en djurstudie tyder på att den stödjer uthålligheten, och en ny studie på människor tyder på '
                'att den stödjer muskelprestationen vid styrketräning.',
        dosage=dict(recommended='25–50 g upplöst i 500–750 ml vatten', timing='I små klunkar under eller direkt efter träning',
                    frequency='På dagar med lång eller hård träning'),
        forms='Rent lösligt pulver av cyklisk dextrin (HBCD).',
        warnings=['En källa till kalorier och socker; avsedd för personer som utför långvarigt eller hårt fysiskt arbete',
                  'Använd den med försiktighet om du har diabetes eller insulinresistens, och följ ditt blodsocker'],
        interactions='Doserna av diabetesläkemedel och insulin kan behöva justeras.',
        naturalSources='Framställs av majsstärkelse genom enzymatisk omvandling; finns inte i maten i den här formen.'),
    'electrolytes-mix': dict(
        summary='En blandning av natrium, kalium, magnesium och klorid; magnesium bidrar till elektrolytbalansen och kalium '
                'till normal muskelfunktion (EFSA-godkända påståenden), och American College of Sports Medicine rekommenderar '
                'att vätska och salter ersätts efter kraftig svettning.',
        dosage=dict(recommended='En portionspåse eller skopa upplöst i 500–750 ml vatten',
                    timing='Under långa fastor, eller under och efter träning med kraftig svettning',
                    frequency='1–2 gånger per dag vid behov'),
        forms='Sockerfria portionspåsar, brustabletter eller pulver med elektrolyter.',
        warnings=['Om du har njursvikt eller högt blodtryck, rådgör med din läkare innan du tar extra natrium och kalium',
                  'Överskrid inte den mängd som rekommenderas på förpackningen'],
        interactions='Viktig varning: använd dem med försiktighet tillsammans med ACE-hämmare, angiotensinreceptorblockerare, '
                     'kaliumsparande diuretika och litium.',
        naturalSources='Saltad grönsaksbuljong, kokosvatten, bananer, bladgrönsaker och nötter.'),
    'tart-cherry-extract': dict(
        summary='Ett surkörsbär rikt på antocyaner som naturligt innehåller melatonin; en dubbelblind studie tyder på att '
                'juicen höjde melatoninnivåerna och förbättrade sömntiden och sömnkvaliteten, och en metaanalys tyder på att '
                'den stödjer musklernas återhämtning efter hård träning.',
        dosage=dict(recommended='500–1200 mg extrakt per dag (eller 30 ml juicekoncentrat)',
                    timing='På kvällen till middagen eller en timme före sänggåendet', frequency='1–2 gånger per dag'),
        forms='Standardiserat extrakt av Montmorency-körsbär i kapslar, eller osötat juicekoncentrat.',
        warnings=['Tolereras väl; juicekoncentratet innehåller naturligt socker, så räkna med det i ditt dagliga kaloriintag',
                  'Kan ge lätta magbesvär vid höga doser'],
        interactions='I höga doser kan det förstärka blodförtunnande läkemedel.',
        naturalSources='Färska, frysta eller osötade torkade surkörsbär.'),
    'saffron-extract': dict(
        summary='Ett extrakt rikt på krocin och safranal; en metaanalys av randomiserade studier tyder på att det stödjer en '
                'positiv sinnesstämning hos vuxna med lätt till måttlig nedstämdhet, och en klinisk studie tyder på att det '
                'minskade småätandet och ökade mättnadskänslan.',
        dosage=dict(recommended='28–30 mg standardiserat extrakt per dag', timing='På morgonen till frukost eller till lunch',
                    frequency='En gång per dag (eller fördelat på två doser)'),
        forms='Standardiserat saffransextrakt (som affron® eller Satiereal®) i kapslar.',
        warnings=['Överskrid inte dosen: mycket stora mängder saffran (flera gram) är giftiga',
                  'Ska inte användas i tillskottsdoser under graviditet, eftersom det kan utlösa livmodersammandragningar; '
                  'undvik under amning',
                  'Undvik det om du har bipolär sjukdom'],
        interactions='Viktig varning: kombinera det inte med antidepressiva läkemedel (SSRI, SNRI) utan medicinsk uppföljning; '
                     'det kan förstärka blodtryckssänkande och blodförtunnande läkemedel.',
        naturalSources='Saffranstrådar (används i små mängder i matlagning).'),
    'betaine-hcl': dict(
        summary='En källa till saltsyra som tillfälligt höjer surheten i magen; en studie på friska frivilliga tyder på att '
                'det snabbt gjorde magen sur igen efter läkemedelsorsakad låg magsyra, vilket stödjer proteinsmältningen och '
                'pepsinets aktivitet hos personer med låg magsyra.',
        dosage=dict(recommended='350–650 mg (en kapsel) till en proteinrik måltid',
                    timing='Mitt i måltiden med klunkar av vatten; öppna eller tugga inte kapseln',
                    frequency='Endast till proteinrika måltider'),
        forms='Kapslar med betain-HCl, ofta med enzymet pepsin.',
        warnings=['Ska inte användas vid aktivt mag- eller tolvfingertarmssår eller magkatarr',
                  'Sluta genast om du känner sveda eller värme i magen',
                  'Återkommande halsbränna kräver en läkarkontroll innan du använder det'],
        interactions='Viktig varning: kombinera det aldrig med NSAID-smärtstillande (ibuprofen, acetylsalicylsyra) eller '
                     'kortison, på grund av risken för magirritation; det är meningslöst tillsammans med syrahämmande '
                     'läkemedel (som omeprazol).',
        naturalSources='Betain finns i rödbetor, spenat och fullkornsvete; hydrokloridformen finns endast som tillskott.'),
    'slippery-elm': dict(
        summary='En bark rik på växtslem, som bildar en gel med vatten som täcker slemhinnan i matstrupe, mage och tarm; den '
                'används traditionellt för att lindra halsbränna och irritation, och en liten pilotstudie tyder på att en '
                'blandning som innehåller den stödde tarmens komfort och regelbundenhet, även om evidensen fortfarande är '
                'begränsad.',
        dosage=dict(recommended='400–800 mg (eller 1 tesked pulver i ett halvt glas ljummet vatten)',
                    timing='30 minuter efter måltiderna eller en timme före sänggåendet', frequency='1–3 gånger per dag'),
        forms='Pulver, kapslar eller sugtabletter av barken.',
        warnings=['Återkommande halsbränna kräver en läkarkontroll',
                  'Undvik under graviditet',
                  'Drick tillräckligt med vatten till den'],
        interactions='Barken täcker tarmväggen och kan fördröja upptaget av andra läkemedel; ta den med minst två timmars '
                     'mellanrum från alla läkemedel.',
        naturalSources='Ingår inte i vanlig mat; innerbarken används som pulver eller te.'),
    'marshmallow-root': dict(
        summary='Rötter rika på slemfiber som bildar ett skyddande lager över slemhinnorna; den används traditionellt för att '
                'lindra irritation i mun och hals och torrhosta, och för att lindra lätta magbesvär (traditionell '
                'användning enligt EMA).',
        dosage=dict(recommended='400–1000 mg extrakt eller pulver per dag', timing='Mellan måltiderna med rikligt med vatten',
                    frequency='1–3 gånger per dag'),
        forms='Pulver eller extrakt av läkemalvarot, en kall rotinfusion, eller sirap.',
        warnings=['Hosta som varar mer än en vecka eller med feber kräver en läkarkontroll',
                  'Undvik under graviditet och amning, eftersom data är otillräckliga',
                  'Sockrad sirap kan höja blodsockret'],
        interactions='Den täcker magväggen och kan fördröja upptaget av andra läkemedel; ta den med två timmars mellanrum '
                     'från alla läkemedel.',
        naturalSources='Ingår inte i vanlig mat; rötterna används som infusion eller sirap.'),
    'dgl-licorice': dict(
        summary='Lakrits där det blodtryckshöjande glycyrrhizinet har tagits bort, så att flavonoiderna som stödjer magens '
                'skyddande slemlager finns kvar; en dubbelblind studie tyder på att ett extrakt av lakritsflavonoider '
                'lindrade symtomen vid funktionell dyspepsi.',
        dosage=dict(recommended='380–760 mg', timing='Tugga tabletten väl 20 minuter före huvudmåltiderna',
                    frequency='Upp till 3 gånger per dag'),
        forms='Tuggtabletter med DGL (10:1), eller extrakt av lakritsflavonoider (som GutGard®).',
        warnings=['Kontrollera att produkten är deglycyrrhiziniserad (DGL); vanlig lakrits höjer blodtrycket och sänker '
                  'kaliumet',
                  'Återkommande halsbränna eller sväljsvårigheter kräver en läkarkontroll',
                  'Undvik under graviditet'],
        interactions='DGL-formen interagerar vanligtvis inte med blodtryckssänkande läkemedel; vanlig lakrits interagerar med '
                     'vätskedrivande läkemedel, digoxin och kortison.',
        naturalSources='Lakritsrot (den traditionella drycken innehåller glycyrrhizin).'),
    'peppermint-oil': dict(
        summary='En olja rik på mentol som får tarmens glatta muskulatur att slappna av; två metaanalyser av kliniska studier '
                'tyder på att enterokapslar med pepparmyntsolja lindrade buksmärta och IBS-symtom. Enterodrageringen hindrar '
                'kapseln från att öppnas i magen och minskar därmed halsbrännan.',
        dosage=dict(recommended='0,2 ml (cirka 180–200 mg) per kapsel',
                    timing='30–60 minuter före en måltid med kallt vatten; dela eller tugga inte',
                    frequency='Upp till 3 gånger per dag'),
        forms='Enterokapslar med pepparmyntsolja (cirka 0,2 ml per kapsel).',
        warnings=['Undvik den vid kraftigt sura uppstötningar eller hiatusbråck',
                  'Inte för barn under 8 år',
                  'Undvik den vid gallsten eller gallgångshinder'],
        interactions='Syraneutraliserande och syrahämmande läkemedel kan lösa upp enterodrageringen för tidigt, så ta dem med '
                     'två timmars mellanrum; den kan höja nivåerna av ciklosporin.',
        naturalSources='Färska myntablad och pepparmyntste (långt mindre koncentrerat än oljan).'),
    'nicotinamide-riboside': dict(
        summary='En form av B3-vitamin som är godkänd i EU som nytt livsmedel (nikotinamidribosidklorid) och som cellerna '
                'omvandlar till NAD+, som mitokondrierna behöver för att producera energi; en dubbelblind studie tyder på att '
                'det på ett säkert sätt höjde NAD+-nivåerna hos medelålders och äldre vuxna.',
        dosage=dict(recommended='Upp till 300 mg per dag (EU:s godkända maxdos för vuxna)',
                    timing='På morgonen till frukost eller lunch', frequency='En gång per dag'),
        forms='Nikotinamidribosidklorid (som Niagen®) i kapslar.',
        warnings=['Endast godkänt för vuxna; ska inte användas under graviditet eller amning',
                  'Det ger inte den hudrodnad som är känd från nikotinsyra',
                  'Räkna med niacinet i alla dina tillskott'],
        interactions='Inga viktiga läkemedelsinteraktioner har rapporterats vid de godkända doserna.',
        naturalSources='Mycket små mängder i mjölk och jäst.'),
    'banaba-leaf-extract': dict(
        summary='Blad från trädet Lagerstroemia speciosa, rika på korosolsyra; en klinisk översikt tyder på att '
                'banabaextrakt och korosolsyra stödjer cellernas glukosupptag och normala blodsockernivåer efter måltiderna.',
        dosage=dict(recommended='32–48 mg av ett extrakt med 1 % korosolsyra (eller 10 mg av ett extrakt med 18 %)',
                    timing='15 minuter före huvudmåltiden', frequency='1–2 gånger per dag'),
        forms='Banabaextrakt standardiserat till 1 % eller 18 % korosolsyra.',
        warnings=['Det kan sänka blodsockret; kontrollera ditt blodsocker regelbundet om du följer det',
                  'Undvik det vid njursjukdom',
                  'Undvik under graviditet och amning'],
        interactions='Viktig varning: banaba kan förstärka diabetesläkemedel och insulin och ge lågt blodsocker; fråga din '
                     'läkare om att justera doserna.',
        naturalSources='Ingår inte i vanlig mat; bladen används traditionellt som te i Sydostasien.'),
    'american-ginseng': dict(
        summary='En typ av ginseng som anses lugnare än asiatisk ginseng; en randomiserad studie tyder på att den stödjer '
                'arbetsminnet och den mentala prestationen, en annan studie tyder på att den dämpade blodsockerstegringen '
                'efter måltiderna, och den används traditionellt för att stödja anpassningen till stress.',
        dosage=dict(recommended='200–1000 mg standardiserat extrakt per dag', timing='På morgonen till frukost',
                    frequency='En gång per dag'),
        forms='Extrakt av amerikansk ginsengrot standardiserat för ginsenosider.',
        warnings=['Undvik under graviditet och amning',
                  'Använd den med försiktighet vid östrogenkänsliga tillstånd',
                  'Kan ge lätta sömnsvårigheter om den tas på kvällen'],
        interactions='Viktig varning: den kan försvaga warfarin och förstärka diabetesläkemedel, så att blodsockret sjunker '
                     'ytterligare; använd den med försiktighet tillsammans med MAO-hämmare.',
        naturalSources='Ingår inte i vanlig mat; roten används som te eller extrakt.'),
    'flaxseed-extract': dict(
        summary='Växtämnen (lignaner) som koncentreras i linfrön och verkar som milda växtöstrogener; en metaanalys tyder på '
                'att tillskott av linfrö stödjer ett normalt blodtryck, och en översikt pekar på en roll för lignaner i '
                'maten i att stödja hjärtats och blodkärlens hälsa.',
        dosage=dict(recommended='100–300 mg SDG-extrakt per dag', timing='Till maten', frequency='En gång per dag'),
        forms='Linfrölignanextrakt standardiserat för SDG, eller krossade linfrön.',
        warnings=['Använd det med försiktighet vid östrogenkänsliga tillstånd (som vissa brösttumörer) utan medicinsk '
                  'uppföljning',
                  'Undvik tillskottsdoser under graviditet och amning'],
        interactions='Det kan störa hormonella läkemedel och tamoxifen; ta det med två timmars mellanrum från andra läkemedel '
                     'om det innehåller linfiber.',
        naturalSources='Krossade linfrön, sesamfrön och fullkorn.'),
    'mulberry-leaf-extract': dict(
        summary='Blad från vitt mullbärsträd (Morus alba), rika på 1-DNJ, som tillfälligt bromsar de sockernedbrytande '
                'enzymerna i tarmen; en klinisk studie tyder på att mullbärsbladsextrakt dämpade stegringen av glukos och '
                'insulin efter en kolhydratrik måltid.',
        dosage=dict(recommended='250–500 mg standardiserat extrakt', timing='5–10 minuter före en kolhydratrik måltid',
                    frequency='Till stärkelserika måltider'),
        forms='Extrakt av vita mullbärsblad standardiserat för 1-DNJ (som Reducose®).',
        warnings=['Kan ge lätta gaser eller uppblåsthet de första dagarna',
                  'Undvik under graviditet och amning'],
        interactions='Det kan förstärka diabetesläkemedel (särskilt akarbos, som verkar på liknande sätt) och sänka '
                     'blodsockret ytterligare; fråga din läkare.',
        naturalSources='Te på vita mullbärsblad.'),
    'green-coffee-bean-extract': dict(
        summary='Orostade kaffebönor rika på klorogensyra, som delvis förstörs vid rostningen; en metaanalys av randomiserade '
                'studier tyder på att det stödjer viktmått, särskilt hos personer med övervikt, och en annan metaanalys '
                'tyder på stöd för vissa markörer för hjärta och ämnesomsättning.',
        dosage=dict(recommended='400–800 mg per dag', timing='Till frukost eller lunch', frequency='Fördelat på två doser'),
        forms='Grönt kaffeextrakt standardiserat till 45–50 % klorogensyra.',
        warnings=['Det innehåller lite koffein; undvik det på kvällen om du är känslig för koffein',
                  'Undvik under graviditet och amning',
                  'Det ersätter inte en balanserad kost och fysisk aktivitet'],
        interactions='Räkna med koffeinet tillsammans med kaffe och energidrycker; använd det med försiktighet tillsammans med '
                     'centralstimulerande medel, blodtryckssänkande och blodförtunnande läkemedel.',
        naturalSources='Gröna, orostade kaffebönor.'),
    'capsimax': dict(
        summary='Ett chilipepparextrakt rikt på capsaicinoider i dragerade pärlor som skyddar magen från att svida; en '
                'randomiserad studie tyder på att pärlorna höjde frisättningen av katekolaminer och blodmarkörer för '
                'fettfrisättning, vilket kan stödja värmebildningen och kaloriförbränningen.',
        dosage=dict(recommended='100 mg per dag (som ger cirka 2 mg capsaicinoider)',
                    timing='Till frukost eller 30 minuter före träning', frequency='En gång per dag'),
        forms='Dragerade Capsimax®-pärlor (OmniBead®) i kapslar.',
        warnings=['Undvik det vid aktivt magsår eller kraftigt sura uppstötningar',
                  'Dela eller tugga inte kapseln',
                  'Undvik under graviditet och amning'],
        interactions='Det kan förstärka blodförtunnande och blodplättshämmande läkemedel; använd det med försiktighet '
                     'tillsammans med blodtryckssänkande läkemedel och ACE-hämmare.',
        naturalSources='Chilipeppar och stark röd paprika.'),
    'oil-of-oregano': dict(
        summary='En eterisk olja rik på karvakrol och tymol; en omfattande översikt beskriver dess antioxidativa och '
                'antimikrobiella egenskaper i laboratoriestudier, och den används traditionellt under korta perioder för att '
                'stödja halsens och magens komfort under förkylningssäsongen, även om evidensen från människor fortfarande är '
                'begränsad.',
        dosage=dict(recommended='100–200 mg olja i en utspädd kapsel', timing='Till en huvudmåltid',
                    frequency='1–2 gånger per dag i högst 10–14 dagar'),
        forms='Kapslar med oreganoolja utspädd i olivolja, standardiserad till 70–80 % karvakrol; drick aldrig den '
              'koncentrerade oljan outspädd.',
        warnings=['Ska inte användas under graviditet, amning eller av barn',
                  'Använd den inte kontinuerligt i mer än 10–14 dagar',
                  'Undvik den om du är allergisk mot kransblommiga växter (mynta, basilika, timjan)'],
        interactions='Oreganoolja kan förstärka blodförtunnande läkemedel och diabetesläkemedel och kan minska upptaget av '
                     'järn, så ta den med två timmars mellanrum från järntillskott.',
        naturalSources='Oregano och vild timjan (i de mängder som används i matlagning).'),
    'bee-propolis': dict(
        summary='Ett harts som bina samlar från trädknoppar, rikt på flavonoider och polyfenoler; en randomiserad studie '
                'tyder på att ett standardiserat propolisextrakt hjälpte lätta symtom från de övre luftvägarna att gå över '
                'snabbare, och en metaanalys tyder på att det stödjer normala inflammationsmarkörer.',
        dosage=dict(recommended='300–500 mg standardiserat extrakt per dag', timing='Till maten',
                    frequency='1–2 gånger per dag'),
        forms='Propolisextrakt standardiserat för polyfenoler, i kapslar, halsspray eller sugtabletter.',
        warnings=['Inte för personer som är allergiska mot biprodukter (honung, pollen, bigift) eller som har allergisk astma',
                  'Sluta två veckor före en operation',
                  'Undvik under graviditet och amning'],
        interactions='Propolis kan förstärka blodförtunnande och blodplättshämmande läkemedel.',
        naturalSources='Produkter från bikupan; små mängder i rå honung.'),
    'wheatgrass': dict(
        summary='Vetets unga skott innan kornet bildas, rika på klorofyll, A-, C- och E-vitamin och järn; vetegräs används '
                'som en koncentrerad källa till gröna växter som stödjer vitaliteten och en regelbunden matsmältning, och en '
                'översikt beskriver dess antioxidativa egenskaper men påpekar ett glapp mellan laboratorieforskning och '
                'klinisk forskning.',
        dosage=dict(recommended='3–5 g pulver per dag', timing='På morgonen, uppblandat i vatten eller juice',
                    frequency='En gång per dag'),
        forms='Torkat ekologiskt vetegräspulver, kapslar eller färsk juice.',
        warnings=['Skotten är naturligt glutenfria, men personer med celiaki bör endast välja certifierat glutenfria '
                  'produkter för att undvika kontaminering',
                  'Kan ge lätt illamående i början; börja med en liten mängd',
                  'Undvik det om du är allergisk mot gräs'],
        interactions='Vetegräs är rikt på K-vitamin och kan därför försvaga warfarin; håll den dagliga mängden jämn och '
                     'berätta det för din läkare.',
        naturalSources='Mörka bladgrönsaker som spenat, ruccola och grönkål.'),
    'frankincense': dict(
        summary='Hartset från trädet Boswellia serrata, rikt på boswelliasyror, främst AKBA, som hämmar det '
                'inflammationsrelaterade enzymet 5-LOX; en metaanalys av kontrollerade studier tyder på att boswellia stödde '
                'ledernas komfort och rörlighet och lindrade stelhet.',
        dosage=dict(recommended='100–250 mg standardiserat extrakt per dag', timing='Till en måltid som innehåller fett',
                    frequency='1–2 gånger per dag'),
        forms='Boswelliaextrakt standardiserat till 20–30 % AKBA (som AprèsFlex® eller 5-Loxin®).',
        warnings=['Tolereras väl; kan ge lätta magbesvär eller diarré',
                  'Undvik under graviditet och amning',
                  'Svår ledsmärta, eller smärta med svullnad och värme, kräver en läkarkontroll'],
        interactions='Boswellia kan förstärka blodförtunnande och blodplättshämmande läkemedel; använd det med försiktighet '
                     'tillsammans med immunhämmande läkemedel.',
        naturalSources='Rökelse (boswelliaharts), som traditionellt tuggas eller dras som te.'),
})


def sv_numbers(text):
    """Swedish number style: a space as thousands separator (1 000, not in years such as 2023) and no line break
    between a number and its unit."""
    import re
    # a four-digit amount: followed by a unit or by the dash of a range (1000–2000 mg, 2500 mg; not EFSA 2023)
    text = re.sub(r'(?<![\d.,\w-])(\d)(\d{3})(?=\s*(?:–\s*\d|mg\b|g\b|IE\b|µg|ml\b|FU\b|GDU\b))',
                  lambda m: m.group(1) + NB + m.group(2), text)
    text = re.sub(r'(?<=\d) (?=\d{3}\b)', NB, text)                     # 1 000 already written with a plain space
    return re.sub(r'(?<=\d) (?=(?:mg|g|µg|IE|kg|ml|ppm|FU|GDU|%)(?!\w))', NB, text)


def _apply(value):
    if isinstance(value, str):
        return sv_numbers(value)
    if isinstance(value, list):
        return [_apply(v) for v in value]
    return {k: _apply(v) for k, v in value.items()}


COPY = {slug: _apply(fields) for slug, fields in COPY.items()}
assert set(COPY) <= set(NAMES), set(COPY) - set(NAMES)

# first batch (1-50) and second batch (51-100), approved 2026-10-26
PUBLISH = set(COPY)
