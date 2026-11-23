"""Titles, meta descriptions and structured-data facts of the hand-written root pages, per language.

The Arabic masters keep their own approved <title> and description. The English, Dutch (and, for the food guide,
Swedish) values below are faithful translations of the Arabic meta copy, shortened to fit the search result
(title 40-60 characters, description 120-160). EU-claim adjustments against the Arabic: no "cure/treat"
wording, no "clinically validated" / "approved" claims, the boodi app is "coming soon" (no "download").
generate_root_pages.py checks the lengths.

kind (schema.org): home, about, profile, contact, collection, article, app, webpage.
author: 'doctor' only where the Arabic master already credits Dr. Wassim Habib; otherwise the organisation.
"""

SEO = {
    '/': dict(kind='home', meta={
        'en': ('WiBo Health: Glycemic Index, Insulin Index & Food Guide',
               'Glycemic index and insulin index for 970+ foods, a guide to 174 supplements, healthy recipes and free '
               'health calculators in four languages.'),
        'nl': ('WiBo Health: glykemische index, insuline-index en voeding',
               'Glykemische index en insuline-index van 970+ voedingsmiddelen, een gids voor 174 supplementen, gezonde '
               'recepten en gratis gezondheidscalculators.'),
    }),
    '/about.html': dict(kind='about', meta={
        'en': ('About WiBo Health Group and the boodi App',
               'Meet WiBo Health Group, led by Dr. Wassim Habib: a European platform for the glycemic index, insulin '
               'response and the official boodi food scanner app.'),
        'nl': ('Over WiBo Health Group en de boodi-app',
               'Maak kennis met WiBo Health Group onder leiding van dr. Wassim Habib: een Europees platform voor de '
               'glykemische index, insulinerespons en de boodi-app.'),
    }),
    '/doctor.html': dict(kind='profile', image='dr-wassim.webp', meta={
        'en': ('Dr. Wassim Habib – Founder of WiBo Health',
               'Meet Dr. Wassim Habib, founder of WiBo Health, who reviews its content on metabolic health, the '
               'glycemic index and insulin response.'),
        'nl': ('Dr. Wassim Habib – oprichter van WiBo Health',
               'Maak kennis met dr. Wassim Habib, oprichter van WiBo Health, die de inhoud over metabole gezondheid, '
               'glykemische index en insulinerespons beoordeelt.'),
    }),
    '/methodology.html': dict(kind='webpage', meta={
        'en': ('Methodology & Scientific References | WiBo Health',
               'How we determine glycemic and insulin index values: the Atkinson 2021 tables (ISO 26642), the "not '
               'applicable" rule, the glycemic load formula and sources.'),
        'nl': ('Methodologie & wetenschappelijke bronnen | WiBo Health',
               'Hoe wij glykemische en insuline-indexwaarden bepalen: Atkinson 2021 (ISO 26642), de regel "niet van '
               'toepassing", de formule voor glykemische lading en bronnen.'),
    }),
    '/foods.html': dict(kind='collection', meta={
        'en': ('Food Guide: Glycemic Index, Insulin Index & Calories',
               'Search 970+ foods by glycemic index, insulin index, calories, protein, carbs, fat and fibre: an '
               'informational nutrition database for diabetes and weight.'),
        'nl': ('Voedingswijzer: glykemische index, insuline en calorieën',
               'Zoek in 970+ voedingsmiddelen op glykemische index, insuline-index, calorieën, eiwit, koolhydraten, vet '
               'en vezels. Informatief, voor diabetes en gewicht.'),
        'sv': ('Livsmedelsguide: glykemiskt index, insulin och kalorier',
               'Sök bland 970+ livsmedel efter glykemiskt index, insulinindex, kalorier, protein, kolhydrater, fett och '
               'fibrer. En informativ databas för diabetes och vikt.'),
    }),
    '/supplements.html': dict(kind='collection', meta={
        'en': ('Supplements Guide: Dosage, Timing and Warnings',
               'A guide to 174 supplements – whey protein, creatine, omega-3, vitamins and minerals – with benefits, '
               'dosage, timing and warnings for each one.'),
        'nl': ('Supplementengids: dosering, timing en waarschuwingen',
               'Een gids voor 174 supplementen – wei-eiwit, creatine, omega-3, vitamines en mineralen – met voordelen, '
               'dosering, timing en waarschuwingen per supplement.'),
    }),
    '/boodi.html': dict(kind='app', image='boodi-app-poster.webp', meta={
        'en': ('boodi App: Smart Food and Ingredient Scanner',
               'The official boodi app by WiBo Health, coming soon: scan barcodes, check ingredients against your diet, '
               'see the glycemic index and find lower-sugar swaps.'),
        'nl': ('boodi-app: slimme voedings- en ingrediëntenscanner',
               'De officiële boodi-app van WiBo Health, binnenkort: scan barcodes, check ingrediënten voor je dieet, '
               'zie de glykemische index en vind minder suiker.'),
    }),
    '/recipes.html': dict(kind='collection', meta={
        'en': ('Healthy Low-GI Recipes for Diabetes and Weight Control',
               'Healthy recipes with glycemic and insulin index values: fresh salads, nourishing soups, main dishes and '
               'lighter desserts for diabetes and weight control.'),
    }),
    '/partners.html': dict(kind='webpage', image='boodi-app-poster.webp', meta={
        'en': ('Partnerships & Sponsorships | WiBo Health',
               'Partner with WiBo Health and the boodi app: an audience focused on diabetes, weight and halal products, '
               '970+ foods in four languages and 174 supplements.'),
        'nl': ('Partnerships en sponsoring | WiBo Health',
               'Word partner van WiBo Health en de boodi-app: een publiek gericht op diabetes, gewicht en halal '
               'producten, 970+ voedingsmiddelen en 174 supplementen.'),
    }),
    '/contact.html': dict(kind='contact', meta={
        'en': ('Contact and Support | WiBo Health & boodi App',
               'Contact the WiBo Health team and boodi app support: general questions about the platform, the '
               'ingredient scanner and technical support in the EU.'),
        'nl': ('Contact en klantenservice | WiBo Health & boodi-app',
               'Neem contact op met het WiBo Health-team en de boodi-klantenservice: vragen over het platform, de '
               'ingrediëntenscanner en technische hulp in de EU.'),
    }),
    '/privacy.html': dict(kind='webpage', meta={
        'en': ('Privacy & Data Protection Policy | WiBo Health',
               'Privacy and data protection policy of WiBo Health and the boodi app: how we protect your data in line '
               'with the GDPR (AVG) and the EU MDR rules.'),
        'nl': ('Privacybeleid en gegevensbescherming | WiBo Health',
               'Privacy- en gegevensbeschermingsbeleid van WiBo Health en de boodi-app: hoe wij je gegevens beschermen '
               'volgens de AVG (GDPR) en de Europese MDR.'),
    }),
    '/terms.html': dict(kind='webpage', meta={
        'en': ('Terms of Use and Legal Agreement | WiBo Health',
               'Terms of use for the WiBo Health website and the boodi app: the European legal framework, the medical '
               'disclaimer and the rules of use in the EU.'),
        'nl': ('Gebruiksvoorwaarden en juridische overeenkomst',
               'Gebruiksvoorwaarden van de WiBo Health-website en de boodi-app: het Europese juridische kader, de '
               'medische disclaimer en de gebruiksregels in de EU.'),
    }),
    '/insulin-resistance.html': dict(kind='article', author='doctor', image='card-insulin-resistance.webp', meta={
        'en': ('HbA1c and Insulin Resistance: The Complete Guide',
               'Understand HbA1c, the hidden signs of insulin resistance, and the eating and exercise plan that helps '
               'lower blood sugar and improve insulin sensitivity.'),
        'nl': ('HbA1c en insulineresistentie: de complete gids',
               'Begrijp je HbA1c, de verborgen signalen van insulineresistentie en het voedings- en beweegplan dat je '
               'bloedsuiker en insulinegevoeligheid ondersteunt.'),
    }),
    '/leptin-resistance.html': dict(kind='article', image='card-leptin-resistance.webp', meta={
        'en': ('Always Hungry? The Leptin Resistance Puzzle Explained',
               'Why you stay hungry after eating: leptin resistance, natural fruit sugar versus liquid fructose, and a '
               'practical plan to support your satiety signals.'),
        'nl': ('Altijd honger? Het raadsel van leptineresistentie',
               'Waarom je honger blijft houden na het eten: leptineresistentie, natuurlijke fruitsuiker tegenover '
               'vloeibare fructose en een plan voor je verzadiging.'),
    }),
    '/cortisol-stress.html': dict(kind='article', image='card-cortisol-stress.webp', meta={
        'en': ('Cortisol vs Cortisone: The Stress Hormone and Belly Fat',
               'The difference between cortisol and cortisone, and how a chronically high stress hormone drives belly '
               'fat storage, the stress belly and weight plateaus.'),
        'nl': ('Cortisol of cortison? Het stresshormoon en buikvet',
               'Het verschil tussen cortisol en cortison, en hoe een chronisch hoog stresshormoon bijdraagt aan buikvet, '
               'de stressbuik en een gewicht dat niet daalt.'),
    }),
    '/intermittent-fasting.html': dict(kind='article', image='card-intermittent-fasting.webp', meta={
        'en': ('Intermittent Fasting: Myths vs Science, the Full Guide',
               'Intermittent fasting myths taken apart: insulin, growth hormone and autophagy explained, common '
               'mistakes when breaking a fast, and tips for women.'),
        'nl': ('Periodiek vasten: mythes en wetenschap, de complete gids',
               'Mythes over periodiek vasten ontkracht: insuline, groeihormoon en autofagie uitgelegd, fouten bij het '
               'breken van het vasten en tips voor vrouwen.'),
    }),
    '/magnesium-types.html': dict(kind='article', image='card-magnesium-types.webp', meta={
        'en': ('Magnesium Types: Which One for Sleep, Muscles or Stress?',
               'The difference between magnesium glycinate, citrate and malate, how to choose the right form for your '
               'needs, and which cheap forms are best avoided.'),
        'nl': ('Magnesiumvormen: welke voor slaap, spieren of stress?',
               'Het verschil tussen magnesiumbisglycinaat, -citraat en -malaat, hoe je de juiste vorm voor jouw '
               'behoefte kiest en welke goedkope vormen je overslaat.'),
    }),
    '/bone-health-minerals.html': dict(kind='article', image='card-bone-health.webp', meta={
        'en': ('The Calcium Myth: Bone Health, Minerals and Salt',
               'Why calcium alone is not enough for your bones: trace minerals, Himalayan and sea salt, and the role of '
               'vitamin D, healthy fats and vitamin K2.'),
        'nl': ('De calciummythe: botgezondheid, mineralen en zout',
               'Waarom calcium alleen niet genoeg is voor je botten: sporenmineralen, Himalaya- en zeezout en de rol '
               'van vitamine D, gezonde vetten en vitamine K2.'),
    }),
    '/thyroid-health.html': dict(kind='article', image='card-thyroid-health.webp', meta={
        'en': ('Eating Little but Not Losing Weight? Thyroid Explained',
               'The hidden sluggish thyroid explained: the TSH test and misleading results, converting T4 to T3, and '
               'the role of selenium and zinc in your metabolism.'),
        'nl': ('Weinig eten en toch niet afvallen? De trage schildklier',
               'De verborgen trage schildklier uitgelegd: de TSH-test en misleidende uitslagen, de omzetting van T4 naar '
               'T3 en de rol van selenium en zink in je stofwisseling.'),
    }),
}

# Breadcrumb / Organization labels per language
CRUMB_HOME = {'ar': 'الرئيسية', 'en': 'Home', 'nl': 'Home', 'sv': 'Hem'}
