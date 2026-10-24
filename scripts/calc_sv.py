"""Swedish copy for the four calculator pages (merged into CALCS by calculator_content.py; built as /sv/<slug>.html).
Decimal comma in text (the widget formats numbers with sv-SE); Swedish care pathways (vårdcentral, 1177); neutral wording
(no religious references); food links open the English food guide and say so once per page."""

T_SV = dict(
    dir='ltr', hub='Hälsokalkylatorer', reviewed='Framtagen och granskad av WiBo Healths medicinska team · 18 oktober 2026',
    faq='Vanliga frågor', related='Fler kalkylatorer och verktyg', refs='Vetenskapliga källor', footer_articles='Artiklar',
    foods_title='Livsmedelsguide (på engelska)', foods_blurb='Glykemiskt index och kalorier för mer än 700 livsmedel.',
    boodi_title='boodi-appen: granska maten innan du äter den 💚',
    boodi_text='Siffror räcker inte ensamma: det du äter styr ditt insulin- och blodsockersvar. Skanna streckkoder i butiken och se produktens glykemiska index, ingredienser och hälsosammare alternativ.',
    boodi_cta='Upptäck boodi-appen')

FOOD_NOTE = ' (Livsmedelssidorna finns än så länge på engelska.)'

SV = {
    'bmi': {
        'title': 'BMI-kalkylator: räkna ut ditt BMI och din hälsosamma vikt | WiBo Health',
        'desc': 'Räkna ut ditt BMI gratis enligt WHO:s tabell, se den hälsosamma vikten för din längd, lägre gränser för vissa ursprung och praktiska råd.',
        'h1': 'BMI-kalkylator: kroppsmasseindex och hälsosam vikt för din längd',
        'crumb': 'BMI-kalkylator',
        'cat': 'Hälsokalkylator · Kroppsmått',
        'short': 'Kroppsmasseindex (BMI)',
        'blurb': 'Klassa din vikt och se det hälsosamma intervallet för din längd.',
        'about': [{'name': 'Kroppsmasseindex'}, {'name': 'Fetma', 'condition': True}, {'name': 'Undervikt', 'condition': True}],
        'lead': 'Kroppsmasseindex (BMI) är det vanligaste verktyget för att bedöma om vikten passar längden. Fyll i vikt och längd så får du ditt BMI, WHO:s klassning och det hälsosamma viktintervallet för din längd. Läs sedan guiden nedan om vad siffran betyder – och vad den inte säger.',
        'ui': {
            'card_title': 'Räkna ut ditt BMI', 'lbl_weight': 'Vikt (kg)', 'lbl_height': 'Längd (cm)',
            'ph_weight': 't.ex. 78', 'ph_height': 't.ex. 175', 'btn': 'Räkna ut mitt BMI',
            'res_heading': 'Ditt kroppsmasseindex (BMI)', 'ideal_label': 'Hälsosam vikt för din längd (BMI 18,5–24,9)',
            'prime_label': 'BMI Prime: ditt BMI i förhållande till den övre hälsosamma gränsen (25)',
            'st_under': 'Undervikt', 'st_normal': 'Normalvikt', 'st_over': 'Övervikt',
            'st_ob1': 'Fetma grad I', 'st_ob2': 'Fetma grad II', 'st_ob3': 'Fetma grad III',
            'tip_under': 'Din vikt ligger under det hälsosamma intervallet. Prata med din vårdcentral om möjliga orsaker (till exempel sköldkörtelrubbningar eller dåligt näringsupptag) och satsa på energi- och proteinrik mat i stället för tomma kalorier.',
            'tip_normal': 'Din vikt ligger i det hälsosamma intervallet. Behåll den med regelbunden rörelse och balanserad kost, och kontrollera även midja-längd-kvoten: bukfettet kan öka även vid normalvikt.',
            'tip_over': 'Din vikt ligger över det hälsosamma intervallet. Redan en viktnedgång på 5–10 % förbättrar blodtryck, blodsocker och blodfetter märkbart. Räkna ut ditt kaloribehov och börja med ett måttligt underskott.',
            'tip_obese': 'Resultatet ligger i intervallet för fetma, som är kopplat till ökad risk för typ 2-diabetes och hjärt-kärlsjukdom. En hälsokontroll (HbA1c, blodfetter, blodtryck) och en strukturerad plan för viktnedgång tillsammans med vården rekommenderas.',
        },
        'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Vad är kroppsmasseindex (BMI)?</span></h2>
            <p>Kroppsmasseindex är ett enkelt tal som sätter vikten i relation till längden. Det används för att bedöma om vikten ligger i ett hälsosamt intervall, under eller över det. Idén kommer från den belgiske matematikern Adolphe Quetelet på 1800-talet, och Världshälsoorganisationen (WHO) har gjort det till internationell standard för att klassa undervikt, övervikt och fetma hos vuxna.</p>
            <p>BMI är snabbt, gratis och kräver bara en våg och ett måttband. På befolkningsnivå följer det kroppsfettet och risken för kroniska sjukdomar som typ 2-diabetes, högt blodtryck, hjärt-kärlsjukdom och vissa cancerformer. Men det är <strong>ett screeningverktyg, inte en diagnos</strong>: det mäter inte fettet direkt och kan inte visa var fettet sitter.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hur räknas BMI ut?</span></h2>
            <p>Kalkylatorn delar vikten i kilo med längden i meter i kvadrat:</p>
            <p class="formula-box">BMI = vikt (kg) ÷ [längd (m) × längd (m)]</p>
            <p><strong>Räkneexempel:</strong> en person som väger 78 kg och är 175 cm lång. Längden i kvadrat = 1,75 × 1,75 = 3,0625, och 78 ÷ 3,0625 = <strong>25,5</strong>, alltså strax inom övervikt. Det hälsosamma viktintervallet för längden får man genom att multiplicera längden i kvadrat med gränserna för normalvikt: 18,5 × 3,0625 = 56,7 kg och 24,9 × 3,0625 = 76,3 kg.</p>
            <p>Kalkylatorn visar också <strong>BMI Prime</strong>: ditt BMI delat med 25, den övre gränsen för normalvikt. Värdet 1,00 betyder att du ligger precis på gränsen; 1,10 att du ligger ungefär 10 % över den.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>BMI-tabell för vuxna</span></h2>
            <p>Klassningen nedan följer WHO:s rapport och är densamma för kvinnor och män från 18 år:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Klass</th><th>BMI (kg/m²)</th><th>Risk för följdsjukdomar</th></tr></thead>
                <tbody>
                    <tr><td><span class="dot b"></span>Undervikt</td><td>under 18,5</td><td>Låg för fetmarelaterade sjukdomar, men högre risk för undernäring, benskörhet och sämre immunförsvar</td></tr>
                    <tr><td><span class="dot g"></span>Normalvikt</td><td>18,5–24,9</td><td>Genomsnittlig (referensnivå)</td></tr>
                    <tr><td><span class="dot y"></span>Övervikt</td><td>25,0–29,9</td><td>Ökad</td></tr>
                    <tr><td><span class="dot o"></span>Fetma grad I</td><td>30,0–34,9</td><td>Måttlig</td></tr>
                    <tr><td><span class="dot r"></span>Fetma grad II</td><td>35,0–39,9</td><td>Svår</td></tr>
                    <tr><td><span class="dot r"></span>Fetma grad III</td><td>40 och över</td><td>Mycket svår</td></tr>
                </tbody>
            </table></div>

            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>Lägre gränser för personer med ursprung i Mellanöstern, Asien och Afrika</span></h2>
            <p>Sambandet mellan BMI och kroppsfett är inte detsamma i alla befolkningar. WHO har sett att risken för diabetes och hjärtsjukdom börjar stiga vid lägre värden i asiatiska befolkningar och föreslog gränser vid 23 och 27,5. I sin uppdatering 2022 rekommenderade brittiska NICE de lägre gränserna för personer med familjebakgrund i <strong>Mellanöstern</strong>, Sydasien, Kina, övriga Asien, Afrika söder om Sahara eller Karibien:</p>
            <ul class="check-list">
                <li><strong>23–27,4:</strong> räknas som övervikt.</li>
                <li><strong>27,5 och över:</strong> räknas som fetma.</li>
            </ul>
            <p>Har du ett sådant ursprung och ett BMI mellan 23 och 25, nöj dig inte med ”normalvikt”: mät midjan med <a href="{calc:whtr}">kalkylatorn för midja-längd-kvot</a> och be om fasteglukos eller HbA1c vid nästa hälsokontroll.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>När är BMI mindre träffsäkert?</span></h2>
            <ul class="check-list">
                <li><strong>Idrottare och mycket muskulösa personer:</strong> muskler väger mer än fett, så en idrottare kan hamna i ”övervikt” trots lite kroppsfett.</li>
                <li><strong>Äldre:</strong> muskelmassan minskar och fettet ökar med åldern, så BMI kan se normalt ut trots mycket kroppsfett.</li>
                <li><strong>Barn och tonåringar (under 18 år):</strong> bedöms med ålders- och könsanpassade tillväxtkurvor, inte med den här tabellen.</li>
                <li><strong>Graviditet och amning:</strong> vikten ändras av naturliga skäl; viktuppgången följs av din barnmorska.</li>
                <li><strong>Vätskeansamling, ödem eller amputation:</strong> vikten påverkas av annat än fett.</li>
                <li><strong>Fettfördelning:</strong> BMI skiljer inte på fett runt höfterna och det mer riskfyllda bukfettet, så komplettera alltid med ett midjemått.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Vad gör du med resultatet? Praktiska råd</span></h2>
            <h3>Om du är underviktig</h3>
            <p>Oavsiktlig undervikt ska kontrolleras av vården, särskilt vid snabb viktnedgång, trötthet eller magbesvär. Öka energiintaget med näringstät mat som nötter, baljväxter, yoghurt och feta mejeriprodukter, och styrketräna så att den extra vikten blir muskler och inte fett.</p>
            <h3>Om du har normalvikt</h3>
            <p>Målet är att stanna där: 150–300 minuter måttlig fysisk aktivitet i veckan enligt WHO, styrketräning två dagar i veckan, tillräckligt med sömn och en tallrik byggd på grönsaker, bra protein och fullkorn.</p>
            <h3>Om du har övervikt eller fetma</h3>
            <p>Du behöver inte nå en ”idealvikt” för att hälsan ska förbättras. I den amerikanska studien Diabetes Prevention Program minskade en viktnedgång på ungefär 7 % tillsammans med 150 minuters aktivitet i veckan risken att utveckla typ 2-diabetes med 58 % hos personer med prediabetes. Börja så här:</p>
            <ol class="steps">
                <li>Räkna ut ditt dagliga kaloribehov med <a href="{calc:tdee}">kaloribehovskalkylatorn (TDEE)</a> och börja med ett måttligt underskott på ungefär 20 % i stället för en extrem diet.</li>
                <li>Fyll halva tallriken med grönsaker, en fjärdedel med protein (kyckling, fisk, ägg, baljväxter) och en fjärdedel med fullkorn med lågt GI.</li>
                <li>Byt söta drycker mot vatten; se hur mycket du behöver med <a href="{calc:water}">vätskebehovskalkylatorn</a>.</li>
                <li>Mät midjan varje månad: en minskande midja visar att bukfettet minskar även när vågen står still.</li>
                <li>Tar du läkemedel mot diabetes eller högt blodtryck, prata med din läkare innan du minskar kalorierna märkbart, eftersom doserna kan behöva ändras.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Livsmedel som hjälper viktkontrollen</span></h2>
            <p>De här livsmedlen är rika på fiber eller protein och mättar länge. Öppna dem för att se kalorier, glykemiskt index och näringsvärden.''' + FOOD_NOTE + '''</p>
            <div class="food-links">
                <a href="{food:oatmeal}">Havregrynsgröt</a><a href="{food:lentils}">Linser</a><a href="{food:chickpeas}">Kikärter</a>
                <a href="{food:greek-yogurt}">Grekisk yoghurt</a><a href="{food:grilled-chicken-breast}">Grillad kycklingfilé</a>
                <a href="{food:broccoli}">Broccoli</a><a href="{food:apple}">Äpple</a><a href="{food:quinoa}">Quinoa</a>
                <a href="{food:whole-wheat-bread}">Fullkornsbröd</a>
            </div>
            <p>Bläddra i hela <a href="{site:/foods.html}">livsmedelsguiden</a> för att jämföra mer än 700 livsmedel efter glykemiskt index och kalorier.</p>
''',
        'faq': [
            ('Vad är ett normalt BMI för vuxna?', 'Ett hälsosamt BMI är 18,5–24,9 för kvinnor och män från 18 år. För personer med familjebakgrund i Mellanöstern, Asien eller Afrika räknar NICE övervikt redan från 23.'),
            ('Hur räknar jag ut min idealvikt för min längd?', 'Multiplicera längden i meter i kvadrat med 18,5 och med 24,9. För 170 cm (2,89 i kvadrat) blir det hälsosamma intervallet ungefär 53,5–72 kg. Kalkylatorn ovan visar intervallet automatiskt.'),
            ('Räknas BMI olika för kvinnor och män?', 'Formeln och gränserna är desamma för vuxna kvinnor och män, men vid samma BMI har kvinnor i genomsnitt mer kroppsfett, så ett midjemått kompletterar bilden.'),
            ('Kan jag använda kalkylatorn för barn?', 'Nej. Barn och ungdomar under 18 år bedöms med åldersanpassade tillväxtkurvor eftersom kroppen förändras under uppväxten. Barnhälsovården eller skolhälsovården hjälper till att tolka värdena.'),
            ('Varför hamnar en idrottare i övervikt?', 'BMI utgår från hela kroppsvikten och kan inte skilja muskler från fett. För idrottare säger midjemått eller fettprocent mer än BMI.'),
            ('Vad är skillnaden mellan BMI och midja-längd-kvot?', 'BMI speglar kroppens storlek, medan midja-längd-kvoten speglar fettet runt magen, som har starkare koppling till insulinresistens och hjärtsjukdom. Använd båda för en bättre bedömning.'),
        ],
        'disclaimer': 'Kalkylatorn är ett utbildande screeningverktyg för vuxna (från 18 år). Den ställer ingen diagnos och passar inte under graviditet eller för barn. Tolka resultatet tillsammans med din vårdcentral eller en dietist utifrån din hälsa i stort.',
    },
    'tdee': {
        'title': 'Kaloribehov (TDEE): räkna ut dagligt energibehov och BMR | WiBo Health',
        'desc': 'Räkna ut ditt dagliga kaloribehov (TDEE) och din basalomsättning (BMR) med Mifflin-St Jeor-ekvationen, med säkra kalorier för viktnedgång och fördelning av protein, fett och kolhydrater.',
        'h1': 'Kaloribehovskalkylator (TDEE): dagligt energibehov och basalomsättning (BMR)',
        'crumb': 'Kaloribehov (TDEE)',
        'cat': 'Hälsokalkylator · Energi och näring',
        'short': 'Dagligt kaloribehov (TDEE)',
        'blurb': 'Kalorier för att behålla vikten, gå ner i fett eller bygga muskler.',
        'about': [{'name': 'Basalomsättning'}, {'name': 'Totalt dagligt energibehov'}, {'name': 'Fetma', 'condition': True}],
        'lead': 'Hur många kalorier behöver kroppen varje dag? Verktyget uppskattar din basalomsättning (BMR) med Mifflin-St Jeor-ekvationen, den mest träffsäkra av de vanliga ekvationerna för vuxna, och multiplicerar den med din aktivitetsnivå. Då får du ditt totala dagliga energibehov (TDEE), säkra mål för viktnedgång och muskeluppbyggnad och en fördelning av makronäringsämnen.',
        'ui': {
            'card_title': 'Räkna ut ditt dagliga kaloribehov', 'lbl_sex': 'Kön', 'male': 'Man', 'female': 'Kvinna',
            'lbl_age': 'Ålder (år)', 'lbl_weight': 'Vikt (kg)', 'lbl_height': 'Längd (cm)',
            'ph_age': 't.ex. 34', 'ph_weight': 't.ex. 68', 'ph_height': 't.ex. 165',
            'lbl_activity': 'Fysisk aktivitetsnivå', 'acts': [
                'Stillasittande: kontorsjobb, ingen träning (×1,2)', 'Lätt aktiv: träning 1–3 dagar i veckan (×1,375)',
                'Måttligt aktiv: träning 3–5 dagar i veckan (×1,55)', 'Mycket aktiv: hård träning 6–7 dagar i veckan (×1,725)',
                'Extremt aktiv: idrottare eller tungt fysiskt arbete (×1,9)'],
            'btn': 'Räkna ut mina kalorier', 'res_heading': 'Totalt dagligt energibehov (TDEE)',
            'kcal_day': 'kalorier per dag för att behålla din nuvarande vikt',
            'bmr_label': 'Basalomsättning (BMR)', 'bmr_sub': 'det kroppen gör av med i fullständig vila',
            'deficit_label': 'Viktnedgång (20 % underskott)', 'deficit_sub': 'aldrig under din BMR',
            'surplus_label': 'Muskeluppbyggnad (15 % överskott)', 'surplus_sub': 'tillsammans med styrketräning',
            'macros_header': 'Förslag på fördelning av dina kalorier för viktnedgång',
            'protein': 'Protein (1,8 g/kg)', 'fat': 'Fett (25 % av energin)', 'carbs': 'Kolhydrater (resten)',
            'tip': 'Siffrorna är uppskattningar: följ din vikt i två veckor och justera sedan med 100–200 kalorier. Välj kolhydrater med lågt GI och mycket fiber.',
            'tip_lowcarb': 'Kalorierna för viktnedgång är låga i förhållande till ditt proteinmål, så det blir lite kvar till kolhydrater. Gå inte lägre utan stöd av en dietist, särskilt om du tar läkemedel mot diabetes.',
        },
        'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>BMR och TDEE: vad är skillnaden?</span></h2>
            <p><strong>Basalomsättningen (BMR)</strong> är den energi kroppen behöver i fullständig vila bara för att hålla sig vid liv: hjärtslag, andning, hjärna, lever och njurar, förnyelse av celler och att hålla kroppen varm. För de flesta som inte är särskilt aktiva är den den största delen av dagens energiförbrukning.</p>
            <p><strong>Det totala dagliga energibehovet (TDEE)</strong> är allt du förbrukar under ett dygn. Det har tre delar:</p>
            <ul class="check-list">
                <li><strong>Basalomsättningen:</strong> den största delen.</li>
                <li><strong>Matens termiska effekt:</strong> ungefär 10 % av kalorierna, energin som går åt till att smälta och ta upp maten; högre för protein.</li>
                <li><strong>Aktivitet:</strong> träning plus vardagsrörelse som att gå, stå och städa. Den här delen skiljer sig mest mellan människor.</li>
            </ul>
            <p>Äter du ungefär ditt TDEE ligger vikten stilla; äter du mindre går du ner i vikt; äter du mer går du upp.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Mifflin-St Jeor-ekvationen: så räknar kalkylatorn</span></h2>
            <p>Mifflin-St Jeor-ekvationen publicerades 1990. En senare systematisk översikt för amerikanska dietistförbundet fann att den oftast förutsäger viloförbrukningen inom 10 % av det uppmätta värdet, både hos personer med och utan fetma:</p>
            <p class="formula-box">Män: BMR = (10 × vikt i kg) + (6,25 × längd i cm) − (5 × ålder) + 5</p>
            <p class="formula-box">Kvinnor: BMR = (10 × vikt i kg) + (6,25 × längd i cm) − (5 × ålder) − 161</p>
            <p>Sedan: <strong>TDEE = BMR × aktivitetsfaktor</strong>.</p>
            <p><strong>Räkneexempel:</strong> en 34-årig kvinna som väger 68 kg, är 165 cm lång och tränar 3–5 dagar i veckan. BMR = 680 + 1 031,25 − 170 − 161 = <strong>1 380 kcal</strong>, och TDEE = 1 380 × 1,55 = <strong>2 139 kcal per dag</strong>. För viktnedgång med 20 % underskott behöver hon ungefär <strong>1 712 kcal</strong>; för muskeluppbyggnad med 15 % överskott ungefär <strong>2 460 kcal</strong>.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>Tabell över aktivitetsfaktorer</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Aktivitetsnivå</th><th>Beskrivning</th><th>Faktor</th></tr></thead>
                <tbody>
                    <tr><td>Stillasittande</td><td>Kontorsjobb, lite promenader, ingen regelbunden träning</td><td>1,2</td></tr>
                    <tr><td>Lätt aktiv</td><td>Lätt träning eller raska promenader 1–3 dagar i veckan</td><td>1,375</td></tr>
                    <tr><td>Måttligt aktiv</td><td>Måttlig träning 3–5 dagar i veckan</td><td>1,55</td></tr>
                    <tr><td>Mycket aktiv</td><td>Hård träning 6–7 dagar i veckan</td><td>1,725</td></tr>
                    <tr><td>Extremt aktiv</td><td>Elitidrottare, träning två gånger om dagen eller tungt fysiskt arbete</td><td>1,9</td></tr>
                </tbody>
            </table></div>
            <p>Tips: de flesta överskattar sin aktivitet. Välj den lägre nivån om du är osäker. Faktorn inkluderar redan din träning, så lägg inte till kalorierna som klockan visar ovanpå ditt TDEE.</p>

            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Hur många kalorier för en säker viktnedgång?</span></h2>
            <p>Kalkylatorn föreslår ett måttligt underskott på 20 % under ditt TDEE och går aldrig under din BMR. Det brukar ge en viktnedgång på ungefär 0,5–1 kg i veckan i början, den takt som de flesta medicinska riktlinjer rekommenderar för att skydda muskelmassan.</p>
            <p>Den gamla regeln att ”7 700 kalorier = 1 kg fett” är en förenkling. Modeller från amerikanska National Institutes of Health visar att viktnedgången planar ut, eftersom en lättare kropp förbrukar mindre energi. Räkna om varje gång du har gått ner 4–5 kg.</p>
            <ul class="check-list">
                <li><strong>Följ inte dieter under 800 kalorier per dag</strong> utan direkt medicinsk uppföljning.</li>
                <li><strong>Personer med diabetes</strong> som tar insulin eller sulfonylurea kan få för lågt blodsocker när de äter mindre; planera ändringar med din läkare.</li>
                <li><strong>Under graviditet och amning</strong> ska du inte äta med kaloriunderskott utan råd från vården.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>Fördelning: protein, fett och kolhydrater</span></h2>
            <p>Kalkylatorn fördelar dina kalorier för viktnedgång så här:</p>
            <ul class="check-list">
                <li><strong>Protein 1,8 g per kg kroppsvikt:</strong> en metaanalys i British Journal of Sports Medicine fann att proteinets nytta för muskeltillväxt vid styrketräning planar ut runt 1,6 g/kg, med en möjlig övre nivå nära 2,2 g/kg. <em>Personer med kronisk njursjukdom behöver lägre mängder som läkaren bestämmer.</em></li>
                <li><strong>Fett 25 % av energin:</strong> inom EFSA:s intervall på 20–35 %, gärna från rapsolja, olivolja, nötter och fet fisk.</li>
                <li><strong>Kolhydrater resten:</strong> från fullkorn, baljväxter, grönsaker och frukt, gärna med lågt GI för ett jämnare blodsocker.</li>
            </ul>
            <p>I exemplet ovan (1 712 kcal): ungefär 122 g protein, 48 g fett och 199 g kolhydrater per dag.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Beräkningens begränsningar</span></h2>
            <p>Alla ekvationer för energiförbrukning förutsäger genomsnitt för grupper; din verkliga förbrukning kan vara ungefär 10 % högre eller lägre. Träffsäkerheten minskar hos mycket muskulösa idrottare, mycket gamla, personer med sköldkörtelsjukdom och personer som tar läkemedel som påverkar ämnesomsättningen. Ekvationen är gjord för vuxna; tonåringar behöver extra energi för att växa.</p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Livsmedel som hjälper dig att nå målen</span></h2>
            <p>Protein- och fiberkällor ur vår livsmedelsguide, med kalorier och glykemiskt index.''' + FOOD_NOTE + '''</p>
            <div class="food-links">
                <a href="{food:grilled-chicken-breast}">Grillad kycklingfilé</a><a href="{food:boiled-egg}">Kokt ägg</a>
                <a href="{food:greek-yogurt}">Grekisk yoghurt</a><a href="{food:skyr-naturel}">Skyr</a><a href="{food:lentils}">Linser</a>
                <a href="{food:quinoa}">Quinoa</a><a href="{food:brown-rice}">Fullkornsris</a><a href="{food:sweet-potato}">Sötpotatis</a>
                <a href="{food:walnuts}">Valnötter</a><a href="{food:avocado}">Avokado</a>
            </div>
            <p>Kontrollera om din vikt ligger i ett hälsosamt intervall med <a href="{calc:bmi}">BMI-kalkylatorn</a>, och följ bukfettet med <a href="{calc:whtr}">kalkylatorn för midja-längd-kvot</a>.</p>
''',
        'faq': [
            ('Vad är skillnaden mellan BMR och TDEE?', 'BMR är det kroppen förbrukar i fullständig vila; TDEE är den totala förbrukningen per dygn när matsmältning, vardagsrörelse och träning räknas in. Planer för viktnedgång utgår från TDEE, inte från BMR.'),
            ('Hur många kalorier ska jag äta för att gå ner i vikt?', 'Dra av ungefär 20 % från ditt TDEE utan att gå under din BMR. För en kvinna med ett TDEE på 2 139 kcal blir det ungefär 1 712 kcal per dag.'),
            ('Är Mifflin-St Jeor-ekvationen träffsäker?', 'Enligt en systematisk översikt är den den mest träffsäkra av de vanliga ekvationerna för vuxna, men den är fortfarande en uppskattning som kan skilja ungefär 10 % från det uppmätta värdet. Följ vikten i två veckor och justera.'),
            ('Varför har viktnedgången stannat av trots att jag äter under mitt TDEE?', 'En lättare kropp förbrukar mindre energi, och vätska kan tillfälligt dölja att fettet minskar. Räkna om med din nya vikt, mät midjan och kontrollera att du registrerar maten noggrant.'),
            ('Hur mycket protein behöver jag per dag?', 'Den lägsta rekommendationen för vuxna är ungefär 0,8 g per kg. Vid viktnedgång med styrketräning hjälper 1,6–2,2 g/kg till att skydda musklerna. Personer med njursjukdom ska följa läkarens råd.'),
            ('Ska jag lägga till kalorierna jag förbrukar vid träning?', 'Nej. Aktivitetsfaktorn inkluderar redan din vanliga träning. Lägger du till den igen räknas den två gånger och underskottet försvinner.'),
        ],
        'disclaimer': 'Kalkylatorn ger en utbildande uppskattning för friska vuxna och ersätter inte en plan från en dietist. Har du diabetes, njur- eller hjärtsjukdom, eller är du gravid eller ammar, prata med vården innan du ändrar ditt kaloriintag.',
    },
    'water': {
        'title': 'Vätskebehov: hur mycket vatten ska jag dricka per dag? | WiBo Health',
        'desc': 'Hur mycket vatten ska du dricka per dag? Räkna ut ditt behov utifrån vikt och aktivitet och jämför med EFSA:s värden för kvinnor, män och graviditet.',
        'h1': 'Vätskebehovskalkylator: hur mycket vatten behöver du per dag?',
        'crumb': 'Vätskebehov',
        'cat': 'Hälsokalkylator · Vätska',
        'short': 'Dagligt vätskebehov',
        'blurb': 'Rätt mängd vätska för din vikt och aktivitet.',
        'about': [{'name': 'Vätskebalans'}, {'name': 'Uttorkning', 'condition': True}],
        'lead': 'Vatten utgör mer än hälften av en vuxens kroppsvikt, och alla organ är beroende av det. Verktyget uppskattar ditt dagliga vätskebehov utifrån vikt och fysisk aktivitet och visar samtidigt Europeiska livsmedelssäkerhetsmyndighetens (EFSA) referensvärden, så att du ser i siffror hur många glas du faktiskt behöver.',
        'ui': {
            'card_title': 'Räkna ut ditt vätskebehov', 'lbl_sex': 'Kön', 'male': 'Man', 'female': 'Kvinna',
            'lbl_weight': 'Vikt (kg)', 'ph_weight': 't.ex. 75',
            'lbl_activity': 'Träning eller fysisk ansträngning', 'acts': [
                'Ingen träning / kontorsjobb', '30 minuter måttlig aktivitet (+350 ml)', '60 minuter aktiv träning (+650 ml)',
                '90+ minuter eller varmt väder (+1000 ml)'],
            'lbl_status': 'Graviditet och amning (kvinnor)', 'status_opts': ['Ej aktuellt', 'Gravid (+300 ml)', 'Ammar (+700 ml)'],
            'btn': 'Räkna ut mitt vätskebehov', 'res_heading': 'Ditt uppskattade dagliga vätskebehov',
            'cups': '{a} till {b} glas (250 ml)',
            'efsa_label': 'EFSA:s referens för totalt vatten', 'efsa_sub': 'från dryck och mat tillsammans',
            'drinks_label': 'Varav från dryck, ungefär', 'drinks_sub': 'cirka 80 % av det totala',
            'tip': 'Fördela drickandet över dagen i stället för att vänta på törsten, och använd ljusgul urin som riktmärke. Te och kaffe i måttliga mängder räknas som vätska; byt söta drycker mot vatten.',
            'tip_heavy': 'Vid högre kroppsvikt överskattar regeln ”ml per kg”; utgå från den lägre delen av intervallet eller EFSA:s referens och justera efter törst och urinens färg.',
        },
        'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Varför behöver kroppen vatten?</span></h2>
            <p>Vatten utgör ungefär 50–60 % av en vuxens kroppsvikt och behövs för nästan alla livsviktiga processer: det transporterar näring och syre i blodet, reglerar kroppstemperaturen via svett, för bort avfall via njurarna och smörjer leder och slemhinnor. Kroppen kan inte lagra vatten, så det vi förlorar varje dag via urin, svett och andning måste hela tiden ersättas.</p>
            <p>Redan lätt uttorkning, en förlust på ungefär 1–2 % av kroppsvikten som vatten, kan kopplas till huvudvärk, trötthet, sämre koncentration och sämre prestation vid träning, enligt en översikt i Nutrition Reviews.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hur uppskattar kalkylatorn ditt vätskebehov?</span></h2>
            <p>Kalkylatorn kombinerar två sätt att räkna:</p>
            <ol class="steps">
                <li><strong>Den viktbaserade tumregeln:</strong> 30–35 ml per kilo kroppsvikt, en vanlig tumregel i kostrådgivning, plus extra vätska vid träning beroende på längd och intensitet.</li>
                <li><strong>Det europeiska referensvärdet (EFSA):</strong> visas som jämförelse. Det är ett ”adekvat intag” av totalt vatten från dryck och mat tillsammans.</li>
            </ol>
            <p class="formula-box">Vätskebehov (l) = vikt × (0,030 till 0,035) + vätska vid träning + (0,3 vid graviditet eller 0,7 vid amning)</p>
            <p><strong>Räkneexempel:</strong> en man som väger 75 kg och har 30 minuters måttlig aktivitet. 75 × 30 = 2 250 ml och 75 × 35 = 2 625 ml; med 350 ml för träningen blir intervallet <strong>2,6–3,0 liter per dag</strong>, ungefär 10–12 glas. EFSA:s referens för män är 2,5 liter från alla källor, varav ungefär 2,0 liter från dryck.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>EFSA:s referensvärden för vatten</span></h2>
            <p>År 2010 fastställde EFSA ett ”adekvat intag” av totalt vatten per dag. Vanligtvis kommer 20–30 % från maten och resten från dryck:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Grupp</th><th>Totalt vatten per dag</th><th>Från dryck, ungefär (80 %)</th></tr></thead>
                <tbody>
                    <tr><td>Barn 4–8 år</td><td>1,6 l</td><td>1,3 l</td></tr>
                    <tr><td>Pojkar 9–13 år</td><td>2,1 l</td><td>1,7 l</td></tr>
                    <tr><td>Flickor 9–13 år</td><td>1,9 l</td><td>1,5 l</td></tr>
                    <tr><td>Kvinnor (från 14 år)</td><td>2,0 l</td><td>1,6 l</td></tr>
                    <tr><td>Män (från 14 år)</td><td>2,5 l</td><td>2,0 l</td></tr>
                    <tr><td>Graviditet</td><td>2,3 l</td><td>1,8 l</td></tr>
                    <tr><td>Amning</td><td>2,7 l</td><td>2,2 l</td></tr>
                </tbody>
            </table></div>
            <p>Värdena gäller vid måttlig temperatur och måttlig aktivitet. Under värmeböljor eller vid långa träningspass ökar behovet tydligt.</p>

            <h2 class="section-title"><i class="fas fa-person-running"></i> <span>Vatten och träning</span></h2>
            <p>American College of Sports Medicine (ACSM) rekommenderar att svettförlusten under träning hålls under 2 % av kroppsvikten. Det enklaste sättet att veta ditt behov är att väga dig före och efter träningen: ersätt varje förlorat kilo med ungefär <strong>1,5 liter</strong> vätska, fördelat över de närmaste timmarna. Vid pass längre än en timme med mycket svett hjälper en dryck med natrium.</p>

            <h2 class="section-title"><i class="fas fa-eye"></i> <span>Dricker du tillräckligt? Tecken på uttorkning</span></h2>
            <ul class="check-list">
                <li><strong>Urinens färg:</strong> ljusgul (halmfärgad) betyder bra vätskebalans; mörkgul betyder att du behöver mer vatten.</li>
                <li><strong>Törst och muntorrhet:</strong> relativt sena signaler, och svagare hos äldre, som har nytta av att dricka på fasta tider.</li>
                <li><strong>Huvudvärk, trötthet och yrsel när man reser sig:</strong> kan vara tecken på uttorkning, särskilt i värme.</li>
                <li><strong>Sällan behov att kissa:</strong> färre än 4 gånger per dag kan tyda på för lite vätska.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>När ska man vara försiktig med stora mängder vatten?</span></h2>
            <p>Att dricka mycket stora mängder på kort tid kan sänka natriumhalten i blodet (hyponatremi), ett allvarligt tillstånd som ibland ses vid långa uthållighetslopp. Ännu viktigare: vissa patienter ska enligt läkarens ordination <strong>begränsa vätskeintaget</strong>, till exempel vid hjärtsvikt, långt framskriden njursvikt eller dialys, levercirros eller SIADH. Gäller det dig, följ den mängd läkaren angett, inte kalkylatorn.</p>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Praktiska råd för vätskebalansen</span></h2>
            <ol class="steps">
                <li>Börja dagen med ett glas vatten och ha en flaska synlig på jobbet.</li>
                <li><strong>För personer med diabetes:</strong> högt blodsocker ökar urinmängden och törsten. Vatten är det bästa valet; undvik juice och söta läskedrycker som höjer blodsockret snabbt.</li>
                <li><strong>Kaffe och te:</strong> räknas som vätska. En studie i PLoS One fann att fyra måttliga koppar kaffe per dag gav ungefär samma vätskebalans som vatten.</li>
                <li><strong>För viktkontroll:</strong> en randomiserad studie fann att ungefär 500 ml vatten före måltiderna under en kalorisnål kost gav något större viktnedgång hos medelålders och äldre. Räkna ut dina kalorier med <a href="{calc:tdee}">kaloribehovskalkylatorn</a>.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Vattenrika livsmedel ur vår livsmedelsguide</span></h2>
            <p>En del av vattnet får du från maten. De här livsmedlen innehåller mycket vatten och lite kalorier.''' + FOOD_NOTE + '''</p>
            <div class="food-links">
                <a href="{food:watermelon}">Vattenmelon</a><a href="{food:cucumber}">Gurka</a><a href="{food:strawberry}">Jordgubbar</a>
                <a href="{food:orange}">Apelsin</a><a href="{food:zucchini}">Zucchini</a><a href="{food:tomato}">Tomat</a>
                <a href="{food:spinach}">Spenat</a><a href="{food:kefir}">Kefir</a>
            </div>
            <p>Kontrollera fler hälsomått med <a href="{calc:bmi}">BMI-kalkylatorn</a> och <a href="{calc:whtr}">kalkylatorn för midja-längd-kvot</a>, eller bläddra i <a href="{site:/foods.html}">livsmedelsguiden</a>.</p>
''',
        'faq': [
            ('Hur många liter vatten ska jag dricka per dag?', 'EFSA rekommenderar 2,0 liter per dag för kvinnor och 2,5 liter för män från alla källor, varav ungefär 80 % från dryck. Räknat på vikt behöver vuxna oftast 30–35 ml per kg, mer vid träning och värme.'),
            ('Räknas te och kaffe som vätska?', 'Ja. Kaffe och te i måttliga mängder bidrar till vätskebalansen. Håll nere tillsatt socker och undvik för mycket koffein på kvällen.'),
            ('Hjälper vatten mot övervikt?', 'Lite. Ungefär 500 ml före måltiderna under en kalorisnål kost ökade viktnedgången i en randomiserad studie, och att byta söta drycker mot vatten sänker dagens kalorier.'),
            ('Kan man dricka för mycket vatten?', 'Ja. Mycket stora mängder på kort tid kan sänka natriumhalten i blodet. Personer med hjärt-, njur- eller leversjukdom kan behöva begränsa vätskan enligt läkarens råd.'),
            ('Hur vet jag att jag dricker tillräckligt?', 'Det enklaste tecknet är ljusgul urin och att du kissar normalt under dagen. Mörk urin, huvudvärk och trötthet kan vara tecken på för lite vätska.'),
            ('Behöver personer med diabetes mer vatten?', 'Högt blodsocker ökar vätskeförlusten via urinen, så personer med diabetes bör dricka regelbundet och välja vatten framför söta drycker, om inte läkaren av annat skäl begränsat vätskan.'),
        ],
        'disclaimer': 'Kalkylatorn ger en utbildande uppskattning för friska vuxna. Har du hjärtsvikt, njur- eller leversjukdom, eller har läkaren sagt att du ska begränsa vätskan, följ läkarens anvisningar i stället för kalkylatorn.',
    },
    'whtr': {
        'title': 'Midja-längd-kvot (WHtR): kalkylator för bukfett | WiBo Health',
        'desc': 'Räkna ut din midja-längd-kvot och risken med bukfett enligt NICE 2022. Så mäter du midjan rätt och så minskar du bukfettet.',
        'h1': 'Kalkylator för midja-längd-kvot (WHtR): ligger ditt bukfett i det säkra intervallet?',
        'crumb': 'Midja-längd-kvot',
        'cat': 'Hälsokalkylator · Bukfett',
        'short': 'Midja-längd-kvot (WHtR)',
        'blurb': 'Ett enkelt mått på bukfett och metabol risk.',
        'about': [{'name': 'Midja-längd-kvot'}, {'name': 'Bukfetma', 'condition': True}, {'name': 'Insulinresistens', 'condition': True}],
        'lead': 'Regeln är enkel: <strong>håll midjemåttet under halva din längd</strong>. Midja-längd-kvoten mäter fettet runt magen, den mest skadliga typen av fett för ämnesomsättningen, och i många studier var den bättre än BMI på att visa risken för diabetes och hjärtsjukdom. Fyll i midjemått och längd för att se var du ligger.',
        'ui': {
            'card_title': 'Räkna ut din midja-längd-kvot', 'lbl_waist': 'Midjemått (cm)', 'lbl_height': 'Längd (cm)',
            'ph_waist': 't.ex. 94', 'ph_height': 't.ex. 175', 'btn': 'Bedöm mitt bukfett',
            'res_heading': 'Din midja-längd-kvot', 'target_label': 'Hälsosam gräns för midjan (halva din längd)',
            'diff_label': 'Så mycket behöver midjan minska', 'ok_diff': 'Inom gränsen ✓',
            'st_low': 'Under 0,4: kontrollera din vikt', 'st_healthy': 'Hälsosamt intervall', 'st_increased': 'Ökad hälsorisk', 'st_high': 'Hög hälsorisk',
            'tip_low': 'En kvot under 0,4 kan betyda låg kroppsvikt eller lite muskelmassa. Kontrollera ditt BMI och din kost, särskilt om du går ner i vikt utan att vilja det.',
            'tip_healthy': 'Ditt bukfett ligger i det hälsosamma intervallet. Behåll det med regelbunden rörelse och lite tillsatt socker, och mät igen om några månader.',
            'tip_increased': 'Du har extra fett runt magen, vilket är kopplat till insulinresistens, högt blodtryck och höga blodfetter. Några centimeter mindre midja förbättrar värdena; be om en blodsockerkontroll vid nästa hälsokontroll.',
            'tip_high': 'En kvot på 0,6 eller mer innebär hög risk för typ 2-diabetes och hjärtsjukdom. En medicinsk bedömning (HbA1c, blodfetter, blodtryck, fettlever) och en strukturerad plan för viktnedgång rekommenderas.',
        },
        'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Vad är midja-längd-kvot?</span></h2>
            <p>Midja-längd-kvoten (WHtR) är midjemåttet delat med längden, i samma enhet. Styrkan är att den mäter <strong>var fettet sitter</strong>, inte bara den totala vikten. Bukfettet inne i buken, runt levern och tarmarna, är metabolt aktivt, frisätter inflammatoriska ämnen och är starkt kopplat till insulinresistens, typ 2-diabetes, fettlever, högt blodtryck och hjärtsjukdom.</p>
            <p>Två personer med samma BMI kan därför ha helt olika risk: den ena lagrar fett på höfterna, den andra runt magen. En metaanalys i Obesity Reviews kom fram till att midja-längd-kvoten är ett bättre screeningverktyg än midjemått eller BMI för vuxnas kardiometabola riskfaktorer.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hur räknas kvoten ut?</span></h2>
            <p class="formula-box">Midja-längd-kvot = midjemått (cm) ÷ längd (cm)</p>
            <p><strong>Räkneexempel:</strong> en person som är 175 cm lång med 94 cm i midjemått: 94 ÷ 175 = <strong>0,54</strong>, i intervallet för ökad risk. Den hälsosamma gränsen för midjan är halva längden, 175 ÷ 2 = <strong>87,5 cm</strong>, så midjan behöver minska med ungefär 6,5 cm.</p>
            <p>En stor fördel är att den hälsosamma gränsen är ungefär densamma för kvinnor och män, olika ursprung och olika längder, vilket en systematisk översikt i Nutrition Research Reviews visade när den föreslog 0,5 som global gräns.</p>

            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Så mäter du midjan rätt</span></h2>
            <ol class="steps">
                <li>Stå rak med fötterna nära varandra och dra upp kläderna så att måttbandet ligger direkt mot huden.</li>
                <li>Leta upp nedersta revbenet och höftbenskammen på sidan och lägg måttbandet <strong>mitt emellan</strong>, som WHO och NICE rekommenderar.</li>
                <li>Håll måttbandet vågrätt runt kroppen, mot huden utan att trycka in den.</li>
                <li>Andas in som vanligt, andas ut och läs av måttet i slutet av utandningen utan att dra in magen.</li>
                <li>Mät två gånger och ta medelvärdet. För att följa förändringen, mät vid samma tid på dagen (på morgonen före frukost).</li>
            </ol>
            <p>Hittar du inte benen är det vanligt att mäta i höjd med naveln; använd bara samma metod varje gång.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>Tabell för midja-längd-kvot hos vuxna</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Kvot</th><th>Klassning (NICE 2022)</th><th>Vad det betyder i praktiken</th></tr></thead>
                <tbody>
                    <tr><td>under 0,4</td><td><span class="dot b"></span>Ej klassad</td><td>Kan tyda på låg kroppsvikt; bedöm tillsammans med BMI</td></tr>
                    <tr><td>0,40–0,49</td><td><span class="dot g"></span>Ingen ökad risk</td><td>Hälsosam fettfördelning; fortsätt så</td></tr>
                    <tr><td>0,50–0,59</td><td><span class="dot y"></span>Ökad hälsorisk</td><td>För mycket bukfett; börja ändra levnadsvanor</td></tr>
                    <tr><td>0,60 och över</td><td><span class="dot r"></span>Ytterligare ökad (hög) risk</td><td>Medicinsk bedömning och strukturerad uppföljning rekommenderas</td></tr>
                </tbody>
            </table></div>
            <p>Som jämförelse använder WHO enbart midjemåttet: ökad risk över 94 cm för män och 80 cm för kvinnor, och kraftigt ökad risk över 102 cm för män och 88 cm för kvinnor. De gränserna tar inte hänsyn till längden, så en lång och en kort man bedöms efter samma siffra – och där är midja-längd-kvoten bättre.</p>

            <h2 class="section-title"><i class="fas fa-code-compare"></i> <span>WHtR, WHR eller BMI?</span></h2>
            <ul class="check-list">
                <li><strong>Kroppsmasseindex (BMI):</strong> speglar kroppens storlek men inte var fettet sitter. Räkna ut det med <a href="{calc:bmi}">BMI-kalkylatorn</a>.</li>
                <li><strong>Midja-höft-kvot (WHR):</strong> ett annat mått där midjan delas med höftmåttet. Det kräver två mätningar och har olika gränser för kvinnor och män.</li>
                <li><strong>Midja-längd-kvot (WHtR):</strong> ett midjemått och ungefär en gräns för alla (0,5). Därför rekommenderade NICE 2022 den tillsammans med BMI för vuxna med BMI under 35.</li>
            </ul>
            <p>Ett internationellt konsensusutlåtande i Nature Reviews Endocrinology (2020) föreslog att midjemåttet ska behandlas som en ”vitalparameter” som mäts vid varje vårdbesök, precis som blodtrycket.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>När är kvoten mindre tillförlitlig?</span></h2>
            <ul class="check-list">
                <li><strong>Graviditet:</strong> använd den inte under graviditet.</li>
                <li><strong>Barn och tonåringar:</strong> NICE-gränserna gäller vuxna; barn bedöms av barnhälsovården eller skolhälsovården.</li>
                <li><strong>Utspänd buk av medicinska skäl:</strong> till exempel ascites, bråck eller kraftig uppsvälldhet.</li>
                <li><strong>BMI på 35 eller mer:</strong> risken är redan hög, och det extra måttet ändrar klassningen lite.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Så minskar du bukfettet: råd byggda på forskning</span></h2>
            <p>Det goda beskedet är att bukfettet ofta svarar snabbare än fettet under huden. Situps stärker musklerna men <strong>bränner inte fett från en viss plats</strong>; det som hjälper är förändringar för hela kroppen:</p>
            <ol class="steps">
                <li><strong>Ett måttligt kaloriunderskott:</strong> räkna ut det med <a href="{calc:tdee}">kaloribehovskalkylatorn</a>. En viktnedgång på 5–10 % minskar bukfettet tydligt.</li>
                <li><strong>Regelbunden konditionsträning:</strong> 150–300 minuter i veckan av rask promenad, simning eller cykling, plus styrketräning två dagar i veckan.</li>
                <li><strong>Mindre tillsatt socker, söta drycker och raffinerad stärkelse:</strong> välj i stället livsmedel med lågt GI och mycket fiber.</li>
                <li><strong>Protein och fiber vid varje måltid:</strong> de mättar och skyddar musklerna under viktnedgången.</li>
                <li><strong>Sömn och stress:</strong> för lite sömn och långvarigt högt kortisol är kopplat till mer bukfett; sikta på minst 7 timmars sömn.</li>
                <li><strong>Kontrollera blodsockret:</strong> om kvoten är 0,5 eller mer, be din vårdcentral om HbA1c, blodfetter och levervärden.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Livsmedel som stöder minskat bukfett</span></h2>
            <p>Livsmedel rika på löslig fiber, omega-3 eller protein, med glykemiskt index och näringsvärden.''' + FOOD_NOTE + '''</p>
            <div class="food-links">
                <a href="{food:oatmeal}">Havregrynsgröt</a><a href="{food:chia-seeds}">Chiafrön</a><a href="{food:lentils}">Linser</a>
                <a href="{food:grilled-salmon}">Grillad lax</a><a href="{food:walnuts}">Valnötter</a><a href="{food:apple}">Äpple</a>
                <a href="{food:pear}">Päron</a><a href="{food:bulgur}">Bulgur</a><a href="{food:broccoli}">Broccoli</a>
            </div>
            <p>Håll vätskebalansen med <a href="{calc:water}">vätskebehovskalkylatorn</a>, och bläddra i <a href="{site:/foods.html}">livsmedelsguiden</a> efter alternativ med lågt GI.</p>
''',
        'faq': [
            ('Vad är en hälsosam midja-längd-kvot?', '0,4–0,49 för vuxna, alltså att midjan är mindre än halva längden. 0,5–0,59 innebär ökad hälsorisk, och 0,6 eller mer ytterligare ökad risk enligt NICE 2022.'),
            ('Var exakt ska jag mäta midjan?', 'Mitt emellan nedersta revbenet och höftbenskammen, med måttbandet vågrätt mot huden, i slutet av en vanlig utandning. Att mäta vid naveln fungerar också om du gör likadant varje gång.'),
            ('Är midja-längd-kvoten bättre än BMI?', 'För att visa risken för diabetes och hjärtsjukdom, ja, i många studier, eftersom den fångar bukfettet. Bäst är att använda båda tillsammans, som NICE rekommenderar.'),
            ('Vad är skillnaden mellan WHtR och WHR?', 'WHtR delar midjemåttet med längden och har en hälsosam gräns på ungefär 0,5 för alla. WHR delar midjemåttet med höftmåttet, kräver två mätningar och har olika gränser för kvinnor och män.'),
            ('Minskar situps bukfettet?', 'De stärker magmusklerna men bränner inte fett specifikt från magen. Bukfettet minskar med kaloriunderskott, konditions- och styrketräning, bättre sömn och bättre kost.'),
            ('Kan barn använda kalkylatorn?', 'Gränserna här gäller vuxna enligt NICE. Barns vikt och midjemått bedöms av barnhälsovården eller skolhälsovården med åldersanpassade mått.'),
        ],
        'disclaimer': 'Kalkylatorn är ett utbildande screeningverktyg för vuxna. Den ställer ingen diagnos och ska inte användas under graviditet. Är kvoten 0,5 eller mer, ta upp resultatet med din vårdcentral och fråga om lämpliga prover.',
    },
}
