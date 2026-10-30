"""Swedish versions of the doctor, about, legal and contact pages (built by generate_article_pages.py).

Each page: `slug` (/sv/<slug>.html), `legacy` = the hand-written ?lang page it translates (hreflang ar/sv/x-default,
SV link and ?lang=sv forwarding are added there), `kind` (structured data), copy and body HTML.
Decisions (2026-10-23): WiBo Health is an educational platform and app - no diagnosis, treatment, medical
consultations or prescriptions; the doctor is presented as "Dr. Wassim Habib – Grundare, WiBo Health" (2026-10-30; was "Grundare och Medicinskt Ansvarig,
WiBo Health Group" with no other titles or registration numbers (Patientsäkerhetslagen: never "läkare");
the Swedish disclaimer is indexed; Crisp is click-to-load and disclosed.
"""

SUPPORT_EMAIL = 'support@wibohealth.com'
WHATSAPP = 'https://wa.me/31645844585?text=Hej%21%20Jag%20har%20en%20fr%C3%A5ga%20om%20WiBo%20Health%20%2F%20boodi-appen'
UPDATED = 'Senast uppdaterad: oktober 2026'
CARE = ('Behöver du sjukvårdsrådgivning? Kontakta din vårdcentral eller ring <strong>1177</strong> (1177 Vårdguiden). '
        'Vid akut fara – ring <strong>112</strong>.')

SITE_PAGES_SV = [
    dict(
        key='doctor', slug='dr-wassim-habib', legacy='/doctor.html', kind='profile', modified='2026-10-23',
        title='Dr. Wassim Habib – Grundare, WiBo Health',
        h1='Dr. Wassim Habib', crumb='Dr. Wassim Habib',
        desc='Dr. Wassim Habib är grundare av WiBo Health och granskar det medicinska innehållet på WiBo Health och i boodi-appen.',
        image='dr-wassim.webp', image_alt='Dr. Wassim Habib – grundare av WiBo Health',
        body='''            <p class="article-byline"><i class="fas fa-user-doctor"></i> Grundare, WiBo Health</p>

            <h2 class="section-title"><i class="fas fa-user"></i> <span>Om Dr. Habib</span></h2>
            <p>Dr. Wassim Habib leder WiBo Health, som grundades för att knyta ihop medicinsk forskning med vardagens matval i Nederländerna, övriga Europa och arabvärlden. Arbetet handlar om metabol hälsa: glykemiskt index, kroppens insulinsvar och livsstilen bakom typ 2-diabetes och fettlever. Han granskar det medicinska innehållet på webbplatsen och i boodi-appen.</p>
            <p><strong>WiBo Health är en plattform för hälsoinformation och utbildning.</strong> Vi ställer inga diagnoser, ger ingen behandling eller individuell medicinsk rådgivning och skriver inte ut läkemedel.</p>

            <h2 class="section-title"><i class="fas fa-microscope"></i> <span>Fokusområden</span></h2>
            <ul class="check-list">
                <li><strong>Glykemiskt index och glykemisk belastning:</strong> hur snabbt livsmedel höjer blodsockret och vad det betyder för energi och aptit.</li>
                <li><strong>Insulinsvar och insulinresistens:</strong> livsmedlens insulinindex och levnadsvanor som minskar risken för typ 2-diabetes.</li>
                <li><strong>Metabol hälsa och vikt:</strong> fettlever, hormonbalans och viktkontroll med kunskapsbaserad kost.</li>
                <li><strong>Kosttillskott utan överdrifter:</strong> doser, interaktioner med läkemedel och varningar, utan vilseledande marknadsföring.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>Så granskar vi innehållet</span></h2>
            <ul class="check-list">
                <li>Värdena för glykemiskt index kommer från de internationella GI-tabellerna (Atkinson m.fl., 2021) och databaser från University of Sydney och Harvard.</li>
                <li>Insulinindex visas bara för livsmedel som har testats kliniskt (Holt m.fl., 1997; Bao m.fl., 2009); otestade livsmedel märks tydligt.</li>
                <li>Hälsokalkylatorerna bygger på validerade formler, som Mifflin-St Jeor och midja-längd-kvoten (WHtR).</li>
                <li>Hälsopåståenden om livsmedel och näringsämnen följer EU:s förordning 1924/2006 och listan över godkända påståenden.</li>
                <li>Innehållet är utbildande, granskas och uppdateras regelbundet och är ingen diagnos eller ersättning för individuell rådgivning från vården.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-book-medical"></i> <span>Artiklar på svenska</span></h2>
            <ul class="check-list">
                <li><a href="/sv/diabetes/prediabetes.html">Prediabetes: så bromsar du utvecklingen och sänker ditt HbA1c</a></li>
                <li><a href="/sv/diabetes/graviditetsdiabetes.html">Graviditetsdiabetes: normala blodsockervärden och vad du kan äta</a></li>
                <li><a href="/sv/articles/insulinresistens-hba1c.html">HbA1c och insulinresistens</a></li>
                <li><a href="/sv/articles/fettlever.html">Fettlever (MASLD)</a></li>
                <li><a href="/sv/articles/leptinresistens.html">Leptin och mättnad</a></li>
                <li><a href="/sv/articles/kortisol-och-stress.html">Kortisol och stress</a></li>
                <li><a href="/sv/articles/periodisk-fasta.html">Periodisk fasta</a></li>
                <li><a href="/sv/articles/magnesiumformer.html">Magnesiumformer</a></li>
                <li><a href="/sv/articles/skeletthalsa-och-mineraler.html">Skeletthälsa och mineraler</a></li>
                <li><a href="/sv/articles/trog-skoldkortel.html">Trög sköldkörtel</a></li>
                <li><a href="/sv/articles/frukostflingor-utan-socker.html">Frukostflingor utan socker</a></li>
            </ul>

            <h2 class="section-title"><i class="fas fa-envelope"></i> <span>Kontakt</span></h2>
            <p>Har du synpunkter på innehållet, ett förslag på samarbete eller hittat ett fel? Skriv till <a href="mailto:support@wibohealth.com">support@wibohealth.com</a>. Vi svarar inte på frågor om enskilda personers hälsa.</p>
''',
        footer_note=CARE,
    ),
    dict(
        key='about', slug='om-oss', legacy='/about.html', kind='about', modified='2026-10-23',
        title='Om oss – WiBo Health Group | WiBo Health',
        h1='Om oss – WiBo Health Group', crumb='Om oss',
        desc='WiBo Health är en plattform för hälsoinformation om blodsocker, glykemiskt index och sund mat, och står bakom boodi-appen som skannar streckkoder och ingredienser.',
        body='''            <p class="lead">WiBo Health är en plattform för hälsoinformation och utbildning om metabol hälsa, kunskapsbaserad kost och smarta digitala verktyg för vardagens matval.</p>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Medicinsk ledning och grundsyn</span></h2>
            <p>WiBo Health grundades under medicinsk ledning av <a href="/sv/dr-wassim-habib.html">Dr. Wassim Habib</a>, grundare av WiBo Health. Vi vill knyta ihop forskning om ämnesomsättning med vardagens inköp i Europa och arabvärlden. Vi tror att kalorier inte berättar hela historien: hur maten påverkar blodsocker och insulin spelar också roll för hälsan på lång sikt.</p>
            <p><strong>Vi är ingen vårdgivare.</strong> Vi ställer inga diagnoser, ger ingen behandling eller individuell medicinsk rådgivning och skriver inte ut läkemedel.</p>

            <h2 class="section-title"><i class="fas fa-mobile-screen-button"></i> <span>boodi 💚 – appen</span></h2>
            <p>boodi är WiBo Health Groups egen app: en hjälpreda i butiken som skannar streckkoder, visar ingredienser och tillsatser och föreslår hälsosammare alternativ från samma hylla. boodi är ett verktyg för information och livsstil och ingen medicinteknisk produkt.</p>

            <h2 class="section-title"><i class="fas fa-eye"></i> <span>Vår vision</span></h2>
            <p>Att vara en pålitlig och tydlig källa till kunskap om glykemiskt index, insulinsvar och öppenhet kring livsmedel.</p>

            <h2 class="section-title"><i class="fas fa-bullseye"></i> <span>Vårt uppdrag</span></h2>
            <p>Att hjälpa människor och familjer att göra välgrundade matval med hjälp av noggranna kalkylatorer, opartiska genomgångar av kosttillskott och smarta verktyg för butiken.</p>

            <h2 class="section-title"><i class="fas fa-landmark"></i> <span>Det här står vi för</span></h2>
            <ul class="check-list">
                <li><strong>Vetenskaplig grund:</strong> vi bygger på publicerad forskning och anger våra källor.</li>
                <li><strong>Tydliga gränser:</strong> vi informerar och utbildar, men ersätter aldrig vården.</li>
                <li><strong>Ärliga påståenden:</strong> hälsopåståenden om livsmedel följer EU:s regler, utan överdrifter.</li>
                <li><strong>Integritet:</strong> vi säljer aldrig dina uppgifter; läs vår <a href="/sv/integritetspolicy.html">integritetspolicy</a>.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-envelope"></i> <span>Kontakt</span></h2>
            <p>Frågor om plattformen, samarbeten eller support för boodi-appen? Se vår <a href="/sv/kontakt.html">kontaktsida</a> eller skriv till <a href="mailto:support@wibohealth.com">support@wibohealth.com</a>.</p>
''',
        footer_note=CARE,
    ),
    dict(
        key='privacy', slug='integritetspolicy', legacy='/privacy.html', kind='webpage', modified='2026-10-23',
        title='Integritetspolicy | WiBo Health och boodi',
        h1='🔒 Integritetspolicy', crumb='Integritetspolicy',
        desc='Hur WiBo Health och boodi-appen behandlar personuppgifter enligt GDPR: vilka uppgifter, varför, cookies och samtycke, mottagare, lagringstid, dina rättigheter och rätten att klaga till IMY.',
        body=f'''            <p class="article-meta"><span><i class="fas fa-calendar"></i> {UPDATED}</span></p>
            <p class="lead">Vi på WiBo Health och boodi 💚 är måna om din integritet. Här beskriver vi hur vi samlar in, använder och skyddar dina personuppgifter enligt EU:s dataskyddsförordning (GDPR).</p>

            <h2 class="section-title"><i class="fas fa-building"></i> <span>1. Personuppgiftsansvarig</span></h2>
            <p>Personuppgiftsansvarig är <strong>WiBo Health Group</strong> i Nederländerna, som driver webbplatsen wibohealth.com och boodi-appen. Kontakt i alla frågor om personuppgifter: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>

            <h2 class="section-title"><i class="fas fa-database"></i> <span>2. Vilka uppgifter vi samlar in</span></h2>
            <ul class="check-list">
                <li><strong>Användningsuppgifter:</strong> vilka sidor du besöker, hur länge, språkinställningar och sammanställd statistik.</li>
                <li><strong>Enhetsuppgifter:</strong> enhetsmodell, operativsystem, webbläsare och tekniska identifierare som behövs för att webbappen ska fungera.</li>
                <li><strong>Kontaktuppgifter:</strong> e-postadress eller telefonnummer bara när du själv kontaktar oss med en fråga eller ett supportärende.</li>
                <li><strong>Kontouppgifter i boodi:</strong> se avsnitt 9.</li>
            </ul>
            <p>Vi behandlar inga hälsouppgifter om dig på våra servrar, och du ska inte skicka sådana uppgifter till oss.</p>

            <h2 class="section-title"><i class="fas fa-bullseye"></i> <span>3. Varför vi behandlar uppgifterna och med vilken rättslig grund</span></h2>
            <ul class="check-list">
                <li><strong>Driva och förbättra webbplatsen och appen</strong> – vårt berättigade intresse (artikel 6.1 f GDPR).</li>
                <li><strong>Besöksstatistik och annonser</strong> – bara med ditt samtycke (artikel 6.1 a).</li>
                <li><strong>Svara på dina frågor och supportärenden</strong> – för att kunna hantera din begäran (artikel 6.1 b och f).</li>
                <li><strong>Ditt boodi-konto och köp i appen</strong> – för att fullgöra avtalet med dig (artikel 6.1 b).</li>
                <li><strong>Nyhetsbrev om kost och hälsa</strong> – bara med ditt uttryckliga samtycke (artikel 6.1 a).</li>
            </ul>

            <h2 class="section-title" id="cookies"><i class="fas fa-cookie-bite"></i> <span>4. Cookies och lokal lagring</span></h2>
            <p>Vi använder lokal lagring och nödvändiga funktionscookies för att komma ihåg dina val, till exempel språk och ljust eller mörkt tema; de kräver inget samtycke. Cookies för statistik och annonser från Google aktiveras bara om du klickar på ”Acceptera” i cookierutan. Du kan när som helst ändra eller återkalla ditt samtycke med knappen nedan eller genom att rensa webbplatsens data i webbläsaren.</p>
            <p><strong>Google Analytics 4:</strong> vi använder Google Analytics från Google Ireland Limited för att se hur många som besöker oss, vilka sidor som läses mest och var besökarna kommer ifrån. Tjänsten körs i Googles samtyckesläge (Consent Mode v2): innan du samtycker är all lagring avstängd, så inga statistik- eller annonscookies sätts, men en sida kan skicka anonyma signaler utan cookies eller identifierare till Google (till exempel att en sida öppnades). Först efter ditt samtycke sätter Google Analytics cookies som _ga och _ga_* (giltiga i upp till två år) för att känna igen återkommande besök. Google Analytics 4 lagrar inte IP-adresser, och vi kopplar inte uppgifterna till din identitet eller använder dem i medicinskt syfte. Google kan behandla uppgifter utanför EU med stöd av EU–US Data Privacy Framework. Om annonser från Google AdSense visas används annonscookies bara med ditt samtycke.</p>
            <p><strong>Livechatt (Crisp):</strong> knappen ”Chatta med oss” på startsidan använder Crisp från Crisp IM SAS i Frankrike (inom EU). Crisp laddas först när du själv klickar på knappen; då behandlas dina meddelanden, ett eventuellt namn eller e-postadress som du skriver in och tekniska uppgifter som IP-adress och webbläsare, och en identifierare sparas på din enhet så att samtalet finns kvar. Den rättsliga grunden är din begäran att kontakta oss och ditt samtycke. Vi sparar samtal bara så länge som behövs för att svara dig. Skriv inte känsliga hälsouppgifter i chatten: plattformen är utbildande och ger ingen medicinsk rådgivning.</p>
            <p><button type="button" class="cookie-settings-btn" onclick="window.wiboConsent && wiboConsent.open()" style="min-height:44px;padding:8px 18px;border-radius:12px;border:2px solid #059669;background:#059669;color:#fff;font:inherit;font-weight:800;cursor:pointer"><i class="fas fa-cookie-bite"></i> Cookieinställningar</button></p>

            <h2 class="section-title"><i class="fas fa-share-nodes"></i> <span>5. Vem vi delar uppgifter med</span></h2>
            <p>Vi säljer, hyr ut eller tjänar aldrig pengar på dina personuppgifter. Uppgifter delas bara med leverantörer som behandlar dem för vår räkning (personuppgiftsbiträden) eller när lagen kräver det:</p>
            <ul class="check-list">
                <li><strong>Supabase</strong> – lagring av boodi-konton på servrar i Frankfurt, Tyskland (EU).</li>
                <li><strong>Google</strong> – Google Analytics och AdSense (med samtycke), Google Gemini för analys av matfoton i appen, Google AdMob för annonser i appen och Google Play Billing för köp.</li>
                <li><strong>RevenueCat</strong> – hantering av prenumerationer i appen, utan att vi lagrar kortuppgifter.</li>
                <li><strong>Crisp</strong> – livechatt (se avsnitt 4).</li>
                <li><strong>Vercel</strong> – webbhotell för webbplatsen; behandlar tekniska uppgifter som IP-adresser i serverloggar.</li>
            </ul>
            <p>Om uppgifter överförs utanför EU/EES sker det med de skyddsåtgärder som GDPR kräver, till exempel EU–US Data Privacy Framework eller EU-kommissionens standardavtalsklausuler.</p>

            <h2 class="section-title"><i class="fas fa-clock-rotate-left"></i> <span>6. Hur länge vi sparar uppgifterna</span></h2>
            <ul class="check-list">
                <li><strong>Statistikcookies:</strong> upp till två år, eller tills du återkallar ditt samtycke eller rensar dem.</li>
                <li><strong>E-post, WhatsApp och chatt:</strong> så länge som behövs för att hantera ditt ärende.</li>
                <li><strong>boodi-konto:</strong> tills du raderar kontot (se <a href="/sv/radera-konto.html">Radera konto</a>).</li>
                <li><strong>Uppgifter vi måste spara enligt lag</strong>, till exempel för bokföring av köp, sparas så länge lagen kräver.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-shield-halved"></i> <span>7. Säkerhet</span></h2>
            <ul class="check-list">
                <li>All trafik krypteras med HTTPS/TLS.</li>
                <li>Kontouppgifter lagras krypterat med automatiska säkerhetskopior hos Supabase i Frankfurt (EU).</li>
                <li>Vi gör regelbundna säkerhetsgenomgångar och samlar bara in de uppgifter vi behöver (dataminimering).</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>8. Dina rättigheter</span></h2>
            <p>Enligt GDPR har du kostnadsfritt rätt att:</p>
            <ul class="check-list">
                <li>få veta vilka uppgifter vi har om dig (registerutdrag),</li>
                <li>få felaktiga eller ofullständiga uppgifter rättade,</li>
                <li>få dina uppgifter raderade (”rätten att bli bortglömd”),</li>
                <li>begränsa behandlingen, invända mot den och få ut dina uppgifter i ett överförbart format (dataportabilitet),</li>
                <li>när som helst återkalla ett samtycke, utan att det påverkar behandlingen innan återkallelsen.</li>
            </ul>
            <p>Kontakta oss på <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> för att använda dina rättigheter. Är du missnöjd med hur vi behandlar dina uppgifter har du rätt att klaga hos <strong>Integritetsskyddsmyndigheten (IMY)</strong>, <a href="https://www.imy.se" rel="noopener">imy.se</a>, eller hos tillsynsmyndigheten i det EU-land där du bor eller arbetar.</p>

            <h2 class="section-title"><i class="fas fa-mobile-screen-button"></i> <span>9. boodi 💚-appen</span></h2>
            <p><strong>Ingen medicinteknisk produkt:</strong> boodi (com.wibohealth.boodi) är ett verktyg för kost- och livsstilsinformation och ingen medicinteknisk produkt enligt EU:s förordning 2017/745 (MDR). Appen ställer inga diagnoser, räknar inte ut insulin- eller läkemedelsdoser och ersätter inte vården. Personer med diabetes eller svåra allergier ska alltid kontrollera förpackningen och följa råd från sin vårdgivare.</p>
            <ul class="check-list">
                <li><strong>Lokal lagring först:</strong> din skanningshistorik, dina granskade livsmedel och dina hälsomål sparas bara lokalt på din telefon och raderas när du loggar ut. På Supabase-servrarna i Tyskland sparas bara kontoprofilen (konto-id och e-post om du registrerar dig), ditt saldo av skanningar och de produktbidrag och foton du laddar upp.</li>
                <li><strong>Kamera:</strong> används för att skanna streckkoder, som avkodas helt på din telefon. Inga foton eller filmer spelas in eller laddas upp för skanningen; bara streckkodens siffror används för att slå upp produkten i Open Food Facts.</li>
                <li><strong>Analys av matfoton (Google Gemini):</strong> om du väljer att fotografera en måltid skickas bara den bilden till Google Gemini för en uppskattning av näringsinnehållet. Bilden kopplas aldrig till ditt namn, din e-post eller din hälsohistorik och sparas inte på våra servrar.</li>
                <li><strong>Köp och annonser:</strong> köp och prenumerationer hanteras av Google Play Billing och RevenueCat utan att vi lagrar kortuppgifter. Annonser i appen visas via Google AdMob.</li>
                <li><strong>Radera konto:</strong> du kan när som helst radera ditt konto och alla uppgifter på Supabase i appen eller via sidan <a href="/sv/radera-konto.html">Radera konto</a>.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-child"></i> <span>10. Barn</span></h2>
            <p>Våra tjänster riktar sig inte till barn. Är du under 13 år får du bara skapa ett konto i boodi med samtycke från din vårdnadshavare.</p>

            <h2 class="section-title"><i class="fas fa-up-right-from-square"></i> <span>11. Länkar till andra webbplatser</span></h2>
            <p>Vi länkar ibland till externa källor, till exempel livsmedelsdatabaser. Vi ansvarar inte för hur andra webbplatser hanterar personuppgifter.</p>

            <h2 class="section-title"><i class="fas fa-rotate"></i> <span>12. Ändringar</span></h2>
            <p>Vi kan uppdatera policyn när lagar eller tjänster förändras. Större ändringar meddelar vi på den här sidan.</p>

            <h2 class="section-title"><i class="fas fa-envelope"></i> <span>13. Kontakt</span></h2>
            <ul class="check-list">
                <li><strong>E-post:</strong> <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> eller <a href="mailto:wibohealth@gmail.com">wibohealth@gmail.com</a></li>
                <li><strong>WhatsApp för allmänna frågor och support:</strong> <a href="{WHATSAPP}" rel="noopener">+31 6 45 84 45 85</a></li>
            </ul>
            <p>Den här svenska versionen är en översättning; vid skillnader gäller den engelska versionen av policyn.</p>
''',
    ),
    dict(
        key='terms', slug='anvandarvillkor', legacy='/terms.html', kind='webpage', modified='2026-10-23',
        title='Användarvillkor | WiBo Health och boodi',
        h1='📜 Användarvillkor', crumb='Användarvillkor',
        desc='Villkoren för att använda WiBo Health och boodi-appen: tjänstens karaktär, medicinsk ansvarsfriskrivning, tillåten användning, ansvarsbegränsning och tillämplig lag.',
        body=f'''            <p class="article-meta"><span><i class="fas fa-calendar"></i> {UPDATED}</span></p>
            <p class="lead">Välkommen till WiBo Health och boodi 💚. Genom att använda webbplatsen eller våra appar godkänner du de här villkoren. Läs dem noga.</p>

            <h2 class="section-title"><i class="fas fa-handshake"></i> <span>1. Godkännande av villkoren</span></h2>
            <p>När du använder WiBo Health godkänner du villkoren. Om du inte godkänner dem ska du sluta använda webbplatsen och apparna. Är du under 18 år ska du använda tjänsterna tillsammans med eller med samtycke från en vårdnadshavare.</p>

            <h2 class="section-title"><i class="fas fa-book-open"></i> <span>2. Tjänsternas karaktär och tillåten användning</span></h2>
            <p>Plattformen erbjuder information och utbildning om kost och hälsa. Du får använda den för personligt, icke-kommersiellt bruk, till exempel för att:</p>
            <ul class="check-list">
                <li>slå upp glykemiskt index, insulinindex och näringsvärden,</li>
                <li>använda de kostnadsfria kalkylatorerna (BMR, TDEE, BMI, WHtR) för att uppskatta ditt behov,</li>
                <li>läsa guider om kosttillskott, artiklar och recept,</li>
                <li>skanna streckkoder i boodi-appen för att granska ingredienser och se hälsosammare alternativ.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>3. Medicinsk ansvarsfriskrivning</span></h2>
            <p>Allt innehåll, alla kalkylatorer och funktioner på WiBo Health och i boodi-appen är verktyg för information och utbildning och är <strong>ingen medicinteknisk produkt</strong> enligt EU:s förordning 2017/745 (MDR). WiBo Health är ingen vårdgivare: vi ställer inga diagnoser, ger ingen behandling eller individuell medicinsk rådgivning och skriver inte ut läkemedel eller doser. Personer med till exempel diabetes, njursjukdom eller svåra allergier ska alltid följa sin vårdgivares råd och kontrollera förpackningen. Läs vår <a href="/sv/medicinsk-ansvarsfriskrivning.html">medicinska ansvarsfriskrivning</a>.</p>

            <h2 class="section-title"><i class="fas fa-mobile-screen-button"></i> <span>4. Särskilt om boodi-appen</span></h2>
            <p>boodi använder öppna databaser och AI-modeller från Google Gemini. Analyser av ingredienser är automatiska uppskattningar utifrån tillverkarnas uppgifter och kan innehålla fel; kontrollera alltid förpackningen. Prenumerationer och skanningspaket hanteras via Google Play Billing och RevenueCat.</p>

            <h2 class="section-title"><i class="fas fa-ban"></i> <span>5. Förbjuden användning</span></h2>
            <ul class="check-list">
                <li>Automatisk insamling eller massnedladdning av våra data utan skriftligt tillstånd.</li>
                <li>Att dekompilera, bakåtkompilera eller fånga upp appens eller webbplatsens tekniska gränssnitt.</li>
                <li>Att använda tjänsterna för obehörig kommersiell verksamhet, skräppost eller bedrägeri.</li>
                <li>Att angripa våra servrar, föra in skadlig kod eller skicka missbrukande skanningsförfrågningar.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-copyright"></i> <span>6. Immateriella rättigheter</span></h2>
            <p>Alla rättigheter till innehåll, varumärken, sammanställningar, design och kod tillhör WiBo Health Group och skyddas av upphovsrättslagstiftning.</p>

            <h2 class="section-title"><i class="fas fa-database"></i> <span>7. Datakällor och rättelser från tillverkare</span></h2>
            <p>Närings- och tillskottsdata kommer från källor som USDA, nederländska Voedingscentrum och Open Food Facts. Enligt EU:s förordning om digitala tjänster (DSA) kan tillverkare skicka rättelser av produktuppgifter till <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>

            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>8. Ansvarsbegränsning</span></h2>
            <p>I den utsträckning lagen tillåter ansvarar WiBo Health Group inte för indirekta skador eller följdskador som uppstår när information från plattformen används utan råd från vården. Begränsningen gäller inte ansvar som inte får begränsas enligt tvingande lag.</p>

            <h2 class="section-title"><i class="fas fa-gavel"></i> <span>9. Tillämplig lag och tvister</span></h2>
            <p>Villkoren regleras av nederländsk lag, och tvister prövas av behörig domstol i Nederländerna. Är du konsument bosatt i Sverige behåller du alltid det skydd du har enligt tvingande svensk konsumentlagstiftning. Vid en tvist med ett företag i ett annat EU-land kan du få kostnadsfri hjälp av Konsument Europa.</p>

            <h2 class="section-title"><i class="fas fa-envelope"></i> <span>10. Kontakt</span></h2>
            <ul class="check-list">
                <li><strong>E-post:</strong> <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> eller <a href="mailto:wibohealth@gmail.com">wibohealth@gmail.com</a></li>
                <li><strong>WhatsApp för allmänna frågor och support:</strong> <a href="{WHATSAPP}" rel="noopener">+31 6 45 84 45 85</a></li>
            </ul>
            <p>Den här svenska versionen är en översättning; vid skillnader gäller den engelska versionen av villkoren.</p>
''',
    ),
    dict(
        # the Arabic disclaimer is noindex: linked from the language switcher only, not as an hreflang alternate
        key='disclaimer', slug='medicinsk-ansvarsfriskrivning', legacy=None, switch_ar='/disclaimer.html', kind='webpage',
        modified='2026-10-23',
        title='Medicinsk ansvarsfriskrivning | WiBo Health',
        h1='⚖️ Medicinsk ansvarsfriskrivning', crumb='Medicinsk ansvarsfriskrivning',
        desc='WiBo Health är en plattform för hälsoinformation och utbildning och ingen vårdgivare. Så ska innehållet användas, och när du ska kontakta vårdcentralen, 1177 eller 112.',
        body=f'''            <p class="article-meta"><span><i class="fas fa-calendar"></i> {UPDATED}</span></p>
            <div class="tip"><h3>Kortfattat</h3><p>Innehållet på WiBo Health och i boodi-appen är avsett som allmän information och utbildning. Det ersätter inte råd, diagnos eller behandling från legitimerad hälso- och sjukvårdspersonal. Kontakta din vårdcentral eller ring <strong>1177</strong> för sjukvårdsrådgivning. Vid akut fara – ring <strong>112</strong>.</p></div>

            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>1. Innehållets karaktär</span></h2>
            <ul class="check-list">
                <li>WiBo Health är en plattform för hälsoinformation och utbildning, <strong>ingen vårdgivare</strong>.</li>
                <li>Vi ställer inga diagnoser, ger ingen behandling eller individuell medicinsk rådgivning och skriver inte ut läkemedel.</li>
                <li>Att läsa innehållet, använda kalkylatorerna eller kontakta oss skapar ingen vårdrelation mellan dig och WiBo Health.</li>
                <li>Innehållet är allmänt och tar inte hänsyn till din hälsa, dina sjukdomar eller dina läkemedel.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>2. När du ska kontakta vården</span></h2>
            <p>Följande kräver en personlig bedömning av din läkare, din vårdcentral eller en legitimerad dietist, inte av den här plattformen:</p>
            <ul class="check-list">
                <li>Du har en sjukdom eller symtom som behöver följas upp.</li>
                <li>Du behöver en kostplan anpassad efter din sjukdom, graviditet eller dina läkemedel.</li>
                <li>Du vill börja med kosttillskott och tar läkemedel, är gravid eller ammar.</li>
                <li>Du funderar på att ändra kosten kraftigt eller börja träna intensivt med en sjukdom.</li>
                <li>Du vill sluta med eller ändra dosen av ett läkemedel – gör det aldrig utan att prata med din läkare.</li>
            </ul>
            <p>Sjukvårdsrådgivning dygnet runt: ring <strong>1177</strong> eller gå till <a href="https://www.1177.se" rel="noopener">1177.se</a>.</p>

            <h2 class="section-title"><i class="fas fa-capsules"></i> <span>3. Kosttillskott</span></h2>
            <ul class="check-list">
                <li>Doser som nämns är allmän information från studier och myndigheters gränsvärden, inga personliga rekommendationer.</li>
                <li>Många kosttillskott kan påverka läkemedel. Fråga din läkare eller på apoteket innan du börjar.</li>
                <li>Kosttillskott ersätter inte en varierad kost och är inte avsedda att behandla eller bota sjukdomar.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-calculator"></i> <span>4. Kalkylatorer och verktyg</span></h2>
            <p>Kalkylatorerna (till exempel BMI, kaloribehov och vätskebehov) ger uppskattningar utifrån allmänna formler. Resultaten är inga diagnoser och kan avvika för dig, till exempel vid graviditet, sjukdom eller hög muskelmassa.</p>

            <h2 class="section-title"><i class="fas fa-book-medical"></i> <span>5. Källor</span></h2>
            <p>Vi bygger innehållet på publicerad forskning och erkända källor och redovisar dem i artiklarna. Forskningen utvecklas, och trots noggrannhet kan innehållet innehålla fel eller vara inaktuellt.</p>

            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>6. Ansvar</span></h2>
            <p>Du ansvarar själv för hur du använder informationen. I den utsträckning lagen tillåter ansvarar WiBo Health inte för skador som uppstår när informationen används i stället för råd från vården. Läs även våra <a href="/sv/anvandarvillkor.html">användarvillkor</a>.</p>

            <h2 class="section-title"><i class="fas fa-truck-medical"></i> <span>7. Akuta lägen</span></h2>
            <div class="allergy-box" role="note">
                <h2>🚨 Vid akut fara – ring 112</h2>
                <ul>
                    <li>Bröstsmärta, andnöd, plötslig förlamning, talsvårigheter eller medvetslöshet: ring <strong>112</strong>.</li>
                    <li>Mycket högt eller lågt blodsocker med förvirring eller medvetandepåverkan: ring <strong>112</strong>.</li>
                    <li>Svår allergisk reaktion: ring <strong>112</strong>.</li>
                    <li>Misstänkt förgiftning, till exempel av för mycket av ett kosttillskott: ring 112 vid akuta symtom, annars Giftinformationscentralen.</li>
                </ul>
            </div>

            <h2 class="section-title"><i class="fas fa-envelope-circle-check"></i> <span>8. Ingen rådgivning via e-post eller chatt</span></h2>
            <p>Vi svarar på allmänna frågor om plattformen och boodi-appen, men inte på frågor om din personliga hälsa, dina provsvar eller dina läkemedel.</p>

            <h2 class="section-title"><i class="fas fa-rotate"></i> <span>9. Uppdateringar</span></h2>
            <p>Vi granskar och uppdaterar innehållet regelbundet och kan ändra den här ansvarsfriskrivningen. Den senaste versionen finns alltid på den här sidan.</p>
''',
    ),
    dict(
        key='contact', slug='kontakt', legacy='/contact.html', kind='contact', modified='2026-10-23',
        title='Kontakt och support | WiBo Health och boodi',
        h1='Kontakt och support', crumb='Kontakt',
        desc='Kontakta WiBo Health med allmänna frågor om plattformen, support för boodi-appen eller förslag på samarbete. Vi ger ingen medicinsk rådgivning.',
        body=f'''            <p class="lead">Vi svarar gärna på allmänna frågor om plattformen och hjälper dig med ditt konto i boodi-appen. WiBo Health är en plattform för information och utbildning och ger ingen diagnos, behandling eller medicinsk rådgivning.</p>
            <div class="tip"><h3>Frågor om din hälsa?</h3><p>{CARE}</p></div>

            <div class="hub-cards">
                <div class="hub-card"><h3><i class="fas fa-mobile-screen-button"></i> Support för boodi-appen</h3><p>Frågor om streckkodsskannern, skanningssaldo, köp i Google Play och förslag på rättelser av produkter.</p><a class="card-link" href="mailto:{SUPPORT_EMAIL}?subject=boodi-support">{SUPPORT_EMAIL}</a></div>
                <div class="hub-card"><h3><i class="fab fa-whatsapp"></i> Allmänna frågor via WhatsApp</h3><p>För allmänna frågor om plattformen och boodi-appen. Skicka inga hälsouppgifter.</p><a class="card-link" href="{WHATSAPP}" rel="noopener">+31 6 45 84 45 85</a></div>
                <div class="hub-card"><h3><i class="fas fa-envelope"></i> Samarbeten och officiella ärenden</h3><p>Samarbeten, forskning, press och övriga ärenden till WiBo Health Group.</p><a class="card-link" href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> <a class="card-link" href="mailto:wibohealth@gmail.com">wibohealth@gmail.com</a></div>
            </div>

            <h2 class="section-title"><i class="fas fa-clock"></i> <span>Öppettider och svarstid</span></h2>
            <p>Vi svarar måndag–fredag kl. 9–18 (svensk tid), och brådskande supportärenden besvaras inom 24 timmar på vardagar. Vi svarar på engelska, arabiska och nederländska.</p>

            <h2 class="section-title"><i class="fas fa-building"></i> <span>Om företaget</span></h2>
            <p>Webbplatsen och boodi-appen drivs av WiBo Health Group i Nederländerna. Läs hur vi hanterar dina uppgifter i vår <a href="/sv/integritetspolicy.html">integritetspolicy</a>.</p>
''',
    ),
    dict(
        key='delete', slug='radera-konto', legacy='/delete-account.html', kind='webpage', modified='2026-10-23',
        title='Radera konto och data i boodi | WiBo Health',
        h1='Radera ditt boodi-konto och dina uppgifter', crumb='Radera konto',
        desc='Så raderar du ditt konto i boodi-appen och alla uppgifter på våra servrar, i appen eller via e-post, enligt GDPR och Google Plays regler.',
        body=f'''            <p class="lead">Vi på WiBo Health respekterar din integritet enligt GDPR och Google Plays regler för utvecklare. Du kan när som helst radera ditt konto i boodi-appen och de uppgifter som hör till det.</p>

            <h2 class="section-title"><i class="fas fa-mobile-screen-button"></i> <span>Radera i appen</span></h2>
            <p>Tryck på ditt saldo i övre fältet ➡️ välj ”Delete my account and data” (radera mitt konto och mina data) ➡️ bekräfta. Alla dina uppgifter raderas direkt.</p>

            <h2 class="section-title"><i class="fas fa-envelope"></i> <span>Begär radering utan appen</span></h2>
            <p>Har du redan avinstallerat appen? Skicka ett mejl till oss från den e-postadress du registrerade dig med, så raderar vi alla dina uppgifter från våra servrar inom 48 timmar.</p>
            <p><a class="boodi-btn" href="mailto:{SUPPORT_EMAIL}?subject=Radera%20mitt%20boodi-konto"><i class="fas fa-trash"></i> Begär radering via e-post</a></p>

            <h2 class="section-title"><i class="fas fa-database"></i> <span>Det här raderas permanent från våra servrar (Supabase, Tyskland)</span></h2>
            <ul class="check-list">
                <li>Din kontoprofil (konto-id och e-postadress om du registrerade dig).</li>
                <li>Ditt saldo av skanningar.</li>
                <li>Dina produktbidrag och uppladdade foton.</li>
            </ul>
            <p><strong>Skanningshistorik:</strong> sparas aldrig på våra servrar. Den finns bara lokalt i telefonens minne och raderas automatiskt när du loggar ut eller raderar kontot.</p>
            <p>Läs mer i vår <a href="/sv/integritetspolicy.html">integritetspolicy</a>.</p>
''',
    ),
    dict(
        key='calculators', slug='calculators', legacy='/calculators.html', kind='collection', modified='2026-10-23',
        title='Hälsokalkylatorer: BMI, kaloribehov, vätskebehov och midja-längd-kvot | WiBo Health',
        h1='Hälsokalkylatorer', crumb='Hälsokalkylatorer',
        desc='Gratis hälsokalkylatorer byggda på riktlinjer från WHO, EFSA och NICE: BMI, dagligt kaloribehov (TDEE), vätskebehov och midja-längd-kvot.',
        body='''            <p class="lead">Verktyg för vardagen, byggda på riktlinjer från Världshälsoorganisationen (WHO), Europeiska livsmedelssäkerhetsmyndigheten (EFSA) och brittiska NICE. Varje kalkylator har en utförlig guide om vad resultatet betyder och vad du kan göra.</p>
            <div class="hub-cards">
                <a class="hub-card" href="/sv/bmi-calculator.html"><h3><i class="fas fa-weight-scale"></i> Kroppsmasseindex (BMI)</h3><p>Klassa din vikt och se det hälsosamma viktintervallet för din längd.</p><span class="card-link">Öppna kalkylatorn →</span></a>
                <a class="hub-card" href="/sv/tdee-calculator.html"><h3><i class="fas fa-fire-flame-curved"></i> Dagligt kaloribehov (TDEE)</h3><p>Basalomsättning, kalorier för att behålla vikten, gå ner i fett eller bygga muskler, och fördelning av protein, fett och kolhydrater.</p><span class="card-link">Öppna kalkylatorn →</span></a>
                <a class="hub-card" href="/sv/water-calculator.html"><h3><i class="fas fa-droplet"></i> Dagligt vätskebehov</h3><p>Rätt mängd vätska för din vikt och aktivitet, jämfört med EFSA:s referensvärden.</p><span class="card-link">Öppna kalkylatorn →</span></a>
                <a class="hub-card" href="/sv/whtr-calculator.html"><h3><i class="fas fa-ruler-combined"></i> Midja-längd-kvot (WHtR)</h3><p>Ett enkelt mått på bukfett och metabol risk: håll midjan under halva din längd.</p><span class="card-link">Öppna kalkylatorn →</span></a>
            </div>

            <div class="boodi-card">
                <div>
                    <h2>boodi 💚 – streckkodsskanner och glykemiskt index</h2>
                    <p>Kalorier berättar inte hela historien: hur maten påverkar blodsocker och insulin spelar också roll. Skanna streckkoder i butiken och se ingredienser, tillsatser och hälsosammare alternativ på några sekunder.</p>
                </div>
                <a class="boodi-btn" href="/sv/boodi.html"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>
''',
        footer_note='Kalkylatorerna är utbildande verktyg för vuxna och ställer inga diagnoser. ' + CARE,
    ),
    dict(
        key='boodi', slug='boodi', legacy='/boodi.html', kind='webpage', modified='2026-10-23',
        title='boodi 💚 – appen som skannar streckkoder, ingredienser och glykemiskt index | WiBo Health',
        h1='Möt boodi 💚 – din smarta hjälp i butiken', crumb='boodi-appen',
        desc='boodi skannar streckkoder och visar näringsvärden, glykemiskt index, ingredienser och tillsatser, och föreslår hälsosammare alternativ från samma hylla. Med ett kostprogram för en hälsosam livsstil.',
        image='boodi-app-logo.jpeg', image_alt='boodi-appens logotyp',
        body='''            <p class="lead">Slut på velandet i butiken! Skanna en streckkod och boodi visar näringsvärden, hur snabbt maten påverkar blodsockret, ingredienser och tillsatser – och föreslår hälsosammare alternativ från samma hylla.</p>
            <p><span class="boodi-btn" aria-disabled="true" style="cursor:default;opacity:.9;white-space:normal;text-align:center"><i class="fab fa-google-play"></i> 🚀 Kommer snart på Google Play</span></p>

            <h2 class="section-title"><i class="fas fa-star"></i> <span>Vad gör boodi?</span></h2>
            <div class="hub-cards">
                <div class="hub-card"><h3><i class="fas fa-barcode"></i> Snabb streckkodsskanning</h3><p>Hämtar uppgifter från stora internationella livsmedelsdatabaser och visar kalorier och dolt socker på några sekunder.</p></div>
                <div class="hub-card"><h3><i class="fas fa-list-check"></i> Ingredienser och tillsatser</h3><p>Visar tillsatser (E-nummer), allergener och ingredienser du själv har valt att undvika, så att du vet vad du äter och kan välja det som passar din kost.</p></div>
                <div class="hub-card"><h3><i class="fas fa-chart-line"></i> Glykemiskt index och insulinsvar</h3><p>Visar hur snabbt ett livsmedel höjer blodsockret – ett stöd för dig som vill ha jämnare blodsocker och en sundare ämnesomsättning.</p></div>
                <div class="hub-card"><h3><i class="fas fa-right-left"></i> Alternativ från samma hylla</h3><p>Inga slumpmässiga förslag: skannar du en vara med mycket socker föreslår boodi ett alternativ med mindre socker inom samma varugrupp.</p></div>
                <div class="hub-card"><h3><i class="fas fa-shield-halved"></i> Integritet enligt GDPR</h3><p>Din skanningshistorik sparas bara på din telefon. Läs mer i vår <a href="/sv/integritetspolicy.html">integritetspolicy</a>.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-leaf"></i> <span>Ett kostprogram för din livsstil</span></h2>
            <p>En balanserad kostplan på 12 veckor, byggd kring din vardag och maten du tycker om, framtagen av WiBo Healths team för kost och livsstil. Ingen svält och inga konstiga livsmedel – bekanta måltider som utvecklas med dig steg för steg.</p>
            <ul class="check-list">
                <li><strong>En ny fas var 14:e dag:</strong> planen förnyas varannan vecka i takt med dina framsteg, så att du kommer förbi viktplatåer utan att tröttna.</li>
                <li><strong>Ditt dagliga behov uträknat:</strong> några snabba frågor om ålder, längd, vikt och aktivitet uppskattar ditt kaloribehov och lägger planen på ett måttligt, säkert underskott.</li>
                <li><strong>Alla världens kök:</strong> boodis personliga kostprogram omfattar alla världens kök – välj fritt det kök du föredrar och få måltider du känner igen och tycker om.</li>
                <li><strong>Välj bort det som inte passar:</strong> markera livsmedel du inte tycker om eller inte tål, så kommer de aldrig med i planen.</li>
                <li><strong>En säkerhetskontroll innan du börjar:</strong> automatiska frågor visar när din hälsa gör att du bör prata med vården innan du följer ett kostprogram.</li>
                <li><strong>Skannern känner till din plan:</strong> skanna en vara och boodi visar direkt ✅ passar din plan, 🟡 med måtta eller ⚠️ innehåller något du valt bort.</li>
            </ul>
            <p class="disclaimer-box">Programmet är en livsstilsguide till hälsosam och balanserad mat. Det är ingen behandling av någon sjukdom och ersätter inte råd från vården. Är du gravid, ammar eller tar läkemedel för en kronisk sjukdom, prata med din vårdcentral innan du börjar.</p>

            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Bra att veta</span></h2>
            <ul class="check-list">
                <li>boodi är ett verktyg för information och livsstil och <strong>ingen medicinteknisk produkt</strong>. Appen ställer inga diagnoser och räknar inte ut insulin- eller läkemedelsdoser.</li>
                <li>Kontrollera alltid förpackningen, särskilt vid allergier, eftersom databasernas uppgifter kan innehålla fel.</li>
                <li>Frågor om appen? Se <a href="/sv/kontakt.html">kontakt och support</a>. Vill du radera ditt konto? Se <a href="/sv/radera-konto.html">Radera konto</a>.</li>
            </ul>
''',
    ),
]
