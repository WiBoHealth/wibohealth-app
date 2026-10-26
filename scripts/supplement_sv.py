"""Swedish copy for the static supplement pages (/sv/supplements/<slug>.html), read by generate_supplement_pages.py.

Every text is a translation of the medically approved copy in js/supplements-data.js (the English fields, checked
against the Arabic), in the wording of Swedish pharmacies and of 1177 / Livsmedelsverket / Läkemedelsverket; EFSA
health claims follow the official Swedish wording of the EU register. Nothing is written from scratch. Approved by
Dr. Wassim Habib (2026-10-26): the 50 names below, Swedish number style (1 000, IE, µg) and, where the Arabic and the
English natural sources differ, the English list.

PUBLISH lists the supplements that get a Swedish page (a trial batch first; the others follow once it is approved).
"""

# the Swedish copy as approved for publication: the "uppdaterades senast" date, lastReviewed and the sitemap lastmod
REVIEWED = '2026-10-26'
REVIEWED_TXT = '26 oktober 2026'

NB = ' '   # thousands separator (1 000) and number + unit, so a value never breaks across lines

# approved Swedish names of the first 50 supplements (ids 1-50 of js/supplements-data.js)
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
}

# groupLabel['en'] of js/supplements-data.js -> Swedish (the groups of the first 50)
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


def sv_numbers(text):
    """Swedish number style: a space as thousands separator (1 000, not in years such as 2023) and no line break
    between a number and its unit."""
    import re
    # a four-digit amount: followed by a unit or by the dash of a range (1000–2000 mg, 2500 mg; not EFSA 2023)
    text = re.sub(r'(?<![\d.,\w-])(\d)(\d{3})(?=\s*(?:–\s*\d|mg\b|g\b|IE\b|µg|ml\b))',
                  lambda m: m.group(1) + NB + m.group(2), text)
    text = re.sub(r'(?<=\d) (?=\d{3}\b)', NB, text)                     # 1 000 already written with a plain space
    return re.sub(r'(?<=\d) (?=(?:mg|g|µg|IE|kg|ml|ppm|%)(?!\w))', NB, text)


def _apply(value):
    if isinstance(value, str):
        return sv_numbers(value)
    if isinstance(value, list):
        return [_apply(v) for v in value]
    return {k: _apply(v) for k, v in value.items()}


COPY = {slug: _apply(fields) for slug, fields in COPY.items()}
assert set(COPY) <= set(NAMES), set(COPY) - set(NAMES)

# all 50 of the first batch (trial of 5 approved 2026-10-26, then the other 45)
PUBLISH = set(COPY)
