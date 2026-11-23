/* Interactive food guide of foods.html (and /en/, /nl/, /sv/foods.html), moved out of the page on 2026-11-23.
   Loaded with defer; the language comes from <html lang>. The copy for every language is in foodsTranslations
   below (scripts/generate_root_pages.py reads it to pre-render the static pages). Food data: data/foods-index.json
   (only the fields the cards, search and filters use), fetched after the first paint. */
const FOODS_INDEX_URL = (document.currentScript && document.currentScript.dataset.index) || '/data/foods-index.json';

// data/foods-index.json is columnar: {f: field names, l: {field: lookup list}, r: rows}; back to one object per food
function decodeIndex(d) {
    return d.r.map(function (row) {
        var o = {};
        d.f.forEach(function (k, i) {
            var v = row[i];
            if (v === undefined || v === null) return;
            o[k] = d.l[k] ? d.l[k][v] : v;
        });
        if (o.categoryAll) { o.category = o.categoryAll[0]; o.categoryNl = o.categoryAll[1]; o.categoryEn = o.categoryAll[2]; delete o.categoryAll; }
        // photo paths in the data are relative to the site root; the guide also runs in /en/, /nl/ and /sv/
        if (o.image && !/^(\/|https?:)/.test(o.image)) o.image = '/' + o.image;
        return o;
    });
}

function loadFoodsIndex() {
    return fetch(FOODS_INDEX_URL, { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error('foods index ' + r.status); return r.json(); })
        .then(decodeIndex)
        .catch(function (e) { console.warn(e); return []; });
}

window.allFoods = [];
let favorites = JSON.parse(localStorage.getItem('wibo_favorites') || '[]').map(String);
// Filters combine: master group (?group=KEY), favourites toggle and the free-text search
let selectedGroup = 'all';
let showFavorites = false;
const groupKeys = (window.FOOD_GROUPS || []).map(g => g.key);

const CHUNK_SIZE = 36;
let visibleCount = CHUNK_SIZE;
let currentFilteredList = [];
let searchDebounceTimer = null;
let scrollObserver = null;

// Fine category label on cards and in the modal (all three fields are set for every record in js/data.js)
function getSafeCategoryName(food, lang) {
    if (!food) return '';
    if (lang === 'nl') return food.categoryNl || food.categoryEn || food.category || '';
    if (lang === 'en') return food.categoryEn || food.categoryNl || food.category || '';
    if (lang === 'sv') return getCategoryLabel(food.group, 'sv') || food.categoryEn || '';
    return food.category || '';
}

// Food name in the reader's language (Swedish: the approved names of scripts/food_sv.py, else English)
function foodName(food, lang) {
    if (lang === 'en') return food.nameEn || food.name;
    if (lang === 'nl') return food.nameNl || food.nameEn || food.name;
    if (lang === 'sv') return (window.FOOD_NAMES_SV || {})[String(food.id)] || food.nameEn || food.name;
    return food.name;
}

const foodsTranslations = {
    ar: {
        "calc_strip_title": "احسب احتياجك ثم اختر طعامك",
        "calc_strip_bmi": "حاسبة مؤشر كتلة الجسم BMI",
        "calc_strip_tdee": "حاسبة السعرات TDEE",
        "calc_strip_water": "حاسبة الماء اليومي",
        "calc_strip_whtr": "نسبة الخصر إلى الطول",
        "meta_title": "دليل الأطعمة الشامل - المؤشر الجلايسيمي، الأنسولين، السعرات | WiBo Health",
        "meta_desc": "دليلك الغذائي الشامل للأطعمة مع المؤشر الجلايسيمي (GI) ومؤشر الأنسولين (II): سعرات حرارية، بروتين، كربوهيدرات، دهون، ألياف - قاعدة بيانات غذائية استرشادية لمرضى السكري والدايت يراجعها فريق ويبو هيلث.",
        "nav_home": "الرئيسية",
        "nav_foods": "دليل الأطعمة",
        "nav_calculators": "الحاسبات",
        "nav_supplements": "المكملات",
        "nav_articles": "المقالات",
        "nav_boodi_app": "بودي 💚",
        "nav_doctor": "من نحن",
        "cat_title": "تصفح الأطعمة حسب القسم",
        "cat_sub": "صنفاً بقيم غذائية كاملة في 10 أقسام",
        "tab_all": "الكل",
        "tab_fav": "أطعمتي المفضلة",
        "category_bar_label": "تصنيفات الأطعمة",
        "search_placeholder": "🔍 ابحث عن أي طعام أو تصنيف...",
        "search_helper": "يمكنك البحث في اسم الطعام أو التصنيف (عربي / English / Nederlands)",
        "no_results": "لم يتم العثور على أي طعام يطابق بحثك",
        "results_clear": "إلغاء التصفية",
        "res_all": "عرض جميع الأصناف ({n})",
        "res_group": "عرض {n} في قسم {g}",
        "res_fav": "عرض {n} من أطعمتك المفضلة",
        "res_fav_group": "عرض {n} من أطعمتك المفضلة في قسم {g}",
        "res_search": " تطابق «{q}»",
        "res_none": "لا توجد نتائج لهذا الاختيار",
        "no_favorites": "لم تضف أي أطعمة إلى المفضلة بعد. اضغط على أيقونة القلب على أي طعام لإضافته هنا!",
        "calories": "سعرات",
        "protein": "بروتين",
        "carbs": "كربوهيدرات",
        "fats": "دهون",
        "loading_more": "جاري تحميل المزيد من الأطعمة...",
        "modal_close": "إغلاق",
        "modal_gi": "المؤشر الجلايسيمي (GI)",
        "modal_ii": "مؤشر الإنسولين (II)",
        "modal_calories": "السعرات الحرارية",
        "modal_kcal": "سعرة",
        "gi_low": "منخفض 🟢",
        "gi_medium": "متوسط 🟡",
        "gi_high": "مرتفع 🔴",
        "ii_low": "منخفض 🟢",
        "ii_medium": "معتدل 🟡",
        "ii_high": "مرتفع 🔴",
        "ii_tested_badge": "مرجع موثق (Holt / Bao) ✅",
        "ii_not_tested": "غير مختبر سريرياً",
        "modal_per_100g": "القيم الغذائية لكل 100 جرام",
        "modal_full_details": "فتح الصفحة المستقلة للصنف",
        "modal_copy_link": "نسخ رابط الصنف المباشر",
        "modal_link_copied": "تم نسخ الرابط",
        "modal_loading": "جاري تحميل التفاصيل الكاملة",
        "modal_load_error": "تعذّر تحميل التفاصيل الكاملة الآن. يمكنك فتح صفحة الصنف من الزر أدناه.",
        "gi_not_applicable": "لا ينطبق",
        "gi_not_available": "غير متوفر",
        "gi_reviewed_badge": "تقدير",
        "methodology_line": "القيم مقاسة أو محسوبة وفق منهجية موثّقة",
        "methodology_link": "المنهجية والمراجع العلمية",
        "gi_sources": "📚 قيم المؤشر الجلايسيمي (GI) المقاسة مستندة إلى الجداول الدولية المعتمدة (Atkinson et al., Am J Clin Nutr 2021) وأبحاث كلية الطب بجامعة هارفارد، أما القيم الموسومة «تقدير» فهي تقديرات راجعها فريق ويبو هيلث الطبي.",
        "clinical_disclaimer": "إخلاء مسؤولية: دليل الأطعمة وتطبيق بودي أدوات استرشادية لنمط الحياة الأيضي وليست أجهزة تشخيصية أو علاجية طبية وفق اللائحة الأوروبية EU MDR 2017/745. استشر طبيبك دائماً قبل تغيير خطتك العلاجية.",
        "boodi_banner_title": "📱 امسح طعام السوبرماركت مباشرة مع تطبيق بودي 💚",
        "boodi_banner_desc": "قراءة الأرقام ممتازة، ولكن فحص الباركود في المتجر أسرع! تطبيق بودي يحلل لك المؤشر الجلايسيمي، يفحص الحلال والتفضيلات الغذائية، ويقترح بدائل صحية أقل سكراً فوراً من نفس الرف.",
        "boodi_banner_btn": "اكتشف تطبيق بودي مجاناً",
        "diet_teaser_title": "جديد في تطبيق بودي: برنامج دايت مخصص لنمط حياتك",
        "diet_teaser_desc": "محتار كيف تنظم هذه الأطعمة في يومك؟ يبني لك بودي خطة وجبات متوازنة لـ 12 أسبوعاً من مطبخك وأطعمتك المفضلة، من إعداد فريق التغذية ونمط الحياة في WiBo Health.",
        "diet_teaser_btn": "اكتشف البرنامج",
        "footer_about": "من نحن",
        "footer_contact": "اتصل بنا",
        "nav_partners": "الشراكات",
        "footer_partners": "الشراكات",
        "footer_food_index": "فهرس الأطعمة",
        "footer_supp_index": "فهرس المكملات",
        "footer_privacy": "سياسة الخصوصية",
        "footer_terms": "شروط الاستخدام",
        "footer_dev_a": "مُطور بـ",
        "footer_dev_b": "من أجل بودي",
        "footer_rights": "© 2026 WiBo Health Group. جميع الحقوق محفوظة | إعداد فريق ويبو هيلث الطبي"
    },
    en: {
        "calc_strip_title": "Work out your needs, then choose your food",
        "calc_strip_bmi": "BMI calculator",
        "calc_strip_tdee": "TDEE calorie calculator",
        "calc_strip_water": "Daily water calculator",
        "calc_strip_whtr": "Waist-to-height ratio",
        "meta_title": "Comprehensive Food Guide - Glycemic Index, Insulin & Calories | WiBo Health",
        "meta_desc": "Nutritional food guide with Glycemic Index (GI), Insulin Index (II), calories, protein, carbs, fats, and fiber for metabolic health and diabetes. WiBo Health Medical Team.",
        "nav_home": "Home",
        "nav_foods": "Food Guide",
        "nav_calculators": "Calculators",
        "nav_supplements": "Supplements",
        "nav_articles": "Articles",
        "nav_boodi_app": "boodi App 💚",
        "nav_doctor": "About Us",
        "cat_title": "Browse foods by section",
        "cat_sub": "foods with full nutrition facts in 10 sections",
        "tab_all": "All",
        "tab_fav": "My Favorites",
        "category_bar_label": "Food categories",
        "search_placeholder": "🔍 Search any food or category...",
        "search_helper": "Search by food name or category (EN / NL / AR)",
        "no_results": "No food found matching your search query",
        "results_clear": "Clear filter",
        "res_all": "Showing all foods ({n})",
        "res_group": "Showing {n} in {g}",
        "res_fav": "Showing {n} from your favourites",
        "res_fav_group": "Showing {n} from your favourites in {g}",
        "res_search": " matching \"{q}\"",
        "res_none": "No results for this selection",
        "no_favorites": "No favorite foods saved yet. Click the heart icon on any card to save it here!",
        "calories": "Calories",
        "protein": "Protein",
        "carbs": "Carbs",
        "fats": "Fat",
        "loading_more": "Loading more foods...",
        "modal_close": "Close",
        "modal_gi": "Glycemic Index (GI)",
        "modal_ii": "Insulin Index (II)",
        "modal_calories": "Calories",
        "modal_kcal": "kcal",
        "gi_low": "Low 🟢",
        "gi_medium": "Medium 🟡",
        "gi_high": "High 🔴",
        "ii_low": "Low 🟢",
        "ii_medium": "Moderate 🟡",
        "ii_high": "High 🔴",
        "ii_tested_badge": "Documented reference (Holt / Bao) ✅",
        "ii_not_tested": "Not tested",
        "modal_per_100g": "Nutritional values per 100 g",
        "modal_full_details": "Open the standalone food page",
        "modal_copy_link": "Copy direct link to this food",
        "modal_link_copied": "Link copied",
        "modal_loading": "Loading full details",
        "modal_load_error": "The full details could not be loaded right now. You can open the food page with the button below.",
        "gi_not_applicable": "Not applicable",
        "gi_not_available": "Not available",
        "gi_reviewed_badge": "Estimate",
        "methodology_line": "Values are measured or calculated using a documented methodology",
        "methodology_link": "Methodology & scientific references",
        "gi_sources": "📚 Measured Glycemic Index (GI) values are referenced from the International Tables (Atkinson et al., Am J Clin Nutr 2021) and Harvard Health Publishing; values labelled “estimate” are estimates reviewed by the WiBo Health medical team.",
        "clinical_disclaimer": "Disclaimer: The WiBo Health food database and boodi app are informational lifestyle guidance tools and do not constitute diagnostic medical devices under EU MDR 2017/745.",
        "boodi_banner_title": "📱 Scan Grocery Foods Live with boodi App 💚",
        "boodi_banner_desc": "Checking charts is great, but scanning in the supermarket aisle is faster! boodi deconstructs Glycemic Index, screens dietary preferences & hidden ingredients, and discovers healthier alternatives on the spot.",
        "boodi_banner_btn": "Discover boodi App Free",
        "diet_teaser_title": "New in the boodi app: a diet programme built around your lifestyle",
        "diet_teaser_desc": "Not sure how to fit these foods into your day? boodi builds you a balanced 12-week meal plan from your favourite cuisine and foods, created by the WiBo Health nutrition and lifestyle team.",
        "diet_teaser_btn": "Explore the programme",
        "footer_about": "About Us",
        "footer_contact": "Contact Us",
        "nav_partners": "Partnerships",
        "footer_partners": "Partnerships",
        "footer_food_index": "Food index",
        "footer_supp_index": "Supplement index",
        "footer_privacy": "Privacy Policy",
        "footer_terms": "Terms of Use",
        "footer_dev_a": "Developed with",
        "footer_dev_b": "for boodi",
        "footer_rights": "© 2026 WiBo Health Group. All rights reserved | WiBo Health Medical Team"
    },
    nl: {
        "calc_strip_title": "Bereken je behoefte en kies dan je eten",
        "calc_strip_bmi": "BMI berekenen",
        "calc_strip_tdee": "Calorieën berekenen (TDEE)",
        "calc_strip_water": "Waterbehoefte berekenen",
        "calc_strip_whtr": "Taille-lengteratio",
        "meta_title": "Uitgebreide Voedingswijzer - Glykemische Index, Insuline & Calorieën | WiBo Health",
        "meta_desc": "Wetenschappelijke voedingswijzer met Glykemische Index (GI), Insuline Index (II), calorieën, eiwitten, koolhydraten en vetten voor diabetes en metabole gezondheid. Medisch Team WiBo Health.",
        "nav_home": "Home",
        "nav_foods": "Voedingswijzer",
        "nav_calculators": "Calculators",
        "nav_supplements": "Supplementen",
        "nav_articles": "Artikelen",
        "nav_boodi_app": "boodi App 💚",
        "nav_doctor": "Over Ons",
        "cat_title": "Voeding per categorie",
        "cat_sub": "voedingsmiddelen met volledige voedingswaarden in 10 categorieën",
        "tab_all": "Alles",
        "tab_fav": "Mijn Favorieten",
        "category_bar_label": "Voedselcategorieën",
        "search_placeholder": "🔍 Zoek een voedingsmiddel of categorie...",
        "search_helper": "Zoek op naam of categorie (Nederlands / EN / AR)",
        "no_results": "Geen voedingsmiddel gevonden dat aan je zoekopdracht voldoet",
        "results_clear": "Filter wissen",
        "res_all": "Alle producten ({n})",
        "res_group": "{n} in {g}",
        "res_fav": "{n} uit je favorieten",
        "res_fav_group": "{n} uit je favorieten in {g}",
        "res_search": " voor \"{q}\"",
        "res_none": "Geen resultaten voor deze keuze",
        "no_favorites": "Nog geen favorieten opgeslagen. Klik op het hartje bij een product om het hier te bewaren!",
        "calories": "Calorieën",
        "protein": "Eiwit",
        "carbs": "Koolhydraten",
        "fats": "Vetten",
        "loading_more": "Meer voedingsmiddelen laden...",
        "modal_close": "Sluiten",
        "modal_gi": "Glykemische Index (GI)",
        "modal_ii": "Insuline-index (II)",
        "modal_calories": "Calorieën",
        "modal_kcal": "kcal",
        "gi_low": "Laag 🟢",
        "gi_medium": "Gemiddeld 🟡",
        "gi_high": "Hoog 🔴",
        "ii_low": "Laag 🟢",
        "ii_medium": "Matig 🟡",
        "ii_high": "Hoog 🔴",
        "ii_tested_badge": "Gedocumenteerde referentie (Holt / Bao) ✅",
        "ii_not_tested": "Niet klinisch getest",
        "modal_per_100g": "Voedingswaarden per 100 g",
        "modal_full_details": "Open de losse pagina van dit voedingsmiddel",
        "modal_copy_link": "Directe link naar dit voedingsmiddel kopiëren",
        "modal_link_copied": "Link gekopieerd",
        "modal_loading": "Volledige details laden",
        "modal_load_error": "De volledige details konden nu niet worden geladen. Open de pagina via de knop hieronder.",
        "gi_not_applicable": "Niet van toepassing",
        "gi_not_available": "Niet beschikbaar",
        "gi_reviewed_badge": "Schatting",
        "methodology_line": "Waarden zijn gemeten of berekend volgens een gedocumenteerde methode",
        "methodology_link": "Methodologie & wetenschappelijke bronnen",
        "gi_sources": "📚 Gemeten GI-waarden zijn gebaseerd op officiële internationale tabellen (Atkinson et al., Am J Clin Nutr 2021) en Harvard Health Publishing; waarden gemarkeerd als “schatting” zijn schattingen beoordeeld door het medisch team van WiBo Health.",
        "clinical_disclaimer": "Algemene disclaimer: Deze voedingswijzer en de boodi-app zijn leefstijl- en educatieve hulpmiddelen en vormen geen medisch hulpmiddel volgens EU MDR 2017/745.",
        "boodi_banner_title": "📱 Scan supermarktvoeding live met de boodi app 💚",
        "boodi_banner_desc": "Tabellen lezen is handig, maar barcodes scannen in het gangpad is sneller! boodi analyseert de glykemische index, controleert voedingsvoorkeuren en verborgen ingrediënten en tipt gezondere alternatieven direct uit hetzelfde schap.",
        "boodi_banner_btn": "Ontdek boodi App Gratis",
        "diet_teaser_title": "Nieuw in de boodi app: een dieetprogramma dat bij jouw leefstijl past",
        "diet_teaser_desc": "Twijfel je hoe je deze voeding in je dag past? boodi stelt een uitgebalanceerd maaltijdplan van 12 weken voor je samen op basis van je favoriete keuken en gerechten, gemaakt door het voedings- en leefstijlteam van WiBo Health.",
        "diet_teaser_btn": "Ontdek het programma",
        "footer_about": "Over Ons",
        "footer_contact": "Contact",
        "nav_partners": "Partners",
        "footer_partners": "Partners",
        "footer_food_index": "Voedingsindex",
        "footer_supp_index": "Supplementenindex",
        "footer_privacy": "Privacybeleid",
        "footer_terms": "Algemene Voorwaarden",
        "footer_dev_a": "Ontwikkeld met",
        "footer_dev_b": "voor boodi",
        "footer_rights": "© 2026 WiBo Health Group. Alle rechten voorbehouden | Medisch Team WiBo Health"
    },
    sv: {
        "calc_strip_title": "Räkna ut ditt behov och välj sedan din mat",
        "calc_strip_bmi": "Kroppsmasseindex (BMI)",
        "calc_strip_tdee": "Dagligt kaloribehov (TDEE)",
        "calc_strip_water": "Dagligt vätskebehov",
        "calc_strip_whtr": "Midja-längd-kvot (WHtR)",
        "meta_title": "Livsmedelsguide: glykemiskt index, insulinindex och kalorier | WiBo Health",
        "meta_desc": "Livsmedelsguide med glykemiskt index (GI), insulinindex (II), kalorier, protein, kolhydrater, fett och kostfiber för metabol hälsa och diabetes. WiBo Healths medicinska team.",
        "nav_home": "Hem",
        "nav_foods": "Livsmedelsguide",
        "nav_calculators": "Kalkylatorer",
        "nav_supplements": "Kosttillskott",
        "nav_articles": "Artiklar",
        "nav_boodi_app": "boodi-appen 💚",
        "nav_doctor": "Om oss",
        "cat_title": "Bläddra bland livsmedel efter grupp",
        "cat_sub": "livsmedel med fullständigt näringsvärde i 10 grupper",
        "tab_all": "Alla",
        "tab_fav": "Mina favoriter",
        "category_bar_label": "Livsmedelsgrupper",
        "search_placeholder": "🔍 Sök efter livsmedel eller grupp...",
        "search_helper": "Sök på livsmedlets namn eller grupp (SV / EN / NL / AR)",
        "no_results": "Inget livsmedel matchar din sökning",
        "results_clear": "Rensa filter",
        "res_all": "Visar alla livsmedel ({n})",
        "res_group": "Visar {n} i {g}",
        "res_fav": "Visar {n} bland dina favoriter",
        "res_fav_group": "Visar {n} bland dina favoriter i {g}",
        "res_search": " som matchar ”{q}”",
        "res_none": "Inga resultat för det här urvalet",
        "no_favorites": "Du har inga sparade favoriter ännu. Klicka på hjärtat på ett kort för att spara det här!",
        "calories": "Kalorier",
        "protein": "Protein",
        "carbs": "Kolhydrater",
        "fats": "Fett",
        "loading_more": "Laddar fler livsmedel...",
        "modal_close": "Stäng",
        "modal_gi": "Glykemiskt index (GI)",
        "modal_ii": "Insulinindex (II)",
        "modal_calories": "Kalorier",
        "modal_kcal": "kcal",
        "gi_low": "Lågt 🟢",
        "gi_medium": "Medelhögt 🟡",
        "gi_high": "Högt 🔴",
        "ii_low": "Lågt 🟢",
        "ii_medium": "Måttligt 🟡",
        "ii_high": "Högt 🔴",
        "ii_tested_badge": "Dokumenterad referens (Holt / Bao) ✅",
        "ii_not_tested": "Inte kliniskt testat",
        "modal_per_100g": "Näringsvärde per 100 g",
        "modal_full_details": "Öppna livsmedlets egen sida",
        "modal_copy_link": "Kopiera direktlänk till livsmedlet",
        "modal_link_copied": "Länken har kopierats",
        "modal_loading": "Laddar fullständiga detaljer",
        "modal_load_error": "De fullständiga detaljerna kunde inte laddas just nu. Du kan öppna livsmedlets sida med knappen nedan.",
        "gi_not_applicable": "Ej tillämpligt",
        "gi_not_available": "Saknas",
        "gi_reviewed_badge": "Uppskattning",
        "methodology_line": "Värdena är uppmätta eller beräknade enligt en dokumenterad metod",
        "methodology_link": "Metod och vetenskapliga källor",
        "gi_sources": "📚 Uppmätta värden för glykemiskt index (GI) kommer från de internationella GI-tabellerna (Atkinson et al., Am J Clin Nutr 2021) och Harvard Health Publishing; värden märkta ”uppskattning” är uppskattningar som granskats av WiBo Healths medicinska team.",
        "clinical_disclaimer": "Ansvarsfriskrivning: WiBo Healths livsmedelsdatabas och boodi-appen är informativa verktyg för vägledning om levnadsvanor och är ingen medicinteknisk produkt för diagnostik enligt EU-förordningen MDR 2017/745.",
        "boodi_banner_title": "📱 Skanna streckkoder i butiken med boodi-appen 💚",
        "boodi_banner_desc": "boodi analyserar förpackade produkter direkt, granskar ingredienserna och föreslår alternativ med mindre socker från samma hylla.",
        "boodi_banner_btn": "Upptäck boodi-appen",
        "diet_teaser_title": "Nytt i boodi-appen: ett kostprogram för din livsstil",
        "diet_teaser_desc": "Osäker på hur du får in de här livsmedlen i vardagen? boodi tar fram en balanserad kostplan på 12 veckor utifrån det kök och den mat du tycker om, framtagen av WiBo Healths team för kost och livsstil.",
        "diet_teaser_btn": "Utforska programmet",
        "footer_about": "Om oss",
        "footer_contact": "Kontakta oss",
        "nav_partners": "Samarbeten",
        "footer_partners": "Samarbeten",
        "footer_food_index": "Livsmedelsregister",
        "footer_supp_index": "Kosttillskottsregister (på engelska)",
        "footer_privacy": "Integritetspolicy",
        "footer_terms": "Användarvillkor",
        "footer_dev_a": "Utvecklad med",
        "footer_dev_b": "för boodi",
        "footer_rights": "© 2026 WiBo Health Group. Alla rättigheter förbehållna."
    }
};

function getInitialLanguage() {
    return document.documentElement.lang || 'ar';   // the page language is fixed by its URL (/, /en/, /nl/, /sv/)
}

let currentLang = getInitialLanguage();

function t(key) {
    return (foodsTranslations[currentLang] && foodsTranslations[currentLang][key]) || key;
}

function changeLanguage(lang) {
    // Swedish: render once the names have arrived (a failed download falls back to the English names)
    if (lang === 'sv' && !window.FOOD_NAMES_SV && !window.svNamesTried) {
        window.loadSvNames().then(() => { window.svNamesTried = true; changeLanguage('sv'); });
        return;
    }
    currentLang = lang;
    localStorage.setItem('preferred_language', lang);
    localStorage.setItem('wibo_language', lang);
    
    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

    // الدرع البرمجي الحاسم: تصفير أي انحراف أفقي في ثانية التبديل
    window.scrollTo({
        left: 0,
        top: window.scrollY,
        behavior: 'instant'
    });
    document.documentElement.scrollLeft = 0;
    document.body.scrollLeft = 0;
    
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const k = el.getAttribute('data-i18n');
        if (foodsTranslations[lang] && foodsTranslations[lang][k]) {
            el.textContent = foodsTranslations[lang][k];
        }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const k = el.getAttribute('data-i18n-placeholder');
        if (foodsTranslations[lang] && foodsTranslations[lang][k]) {
            el.placeholder = foodsTranslations[lang][k];
        }
    });

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang-toggle') === lang);
    });

    // header links that have a Swedish page switch to it in Swedish
    document.querySelectorAll('[data-sv-href]').forEach(a => {
        if (!a.dataset.baseHref) a.dataset.baseHref = a.getAttribute('href');
        a.setAttribute('href', lang === 'sv' ? a.dataset.svHref : a.dataset.baseHref);
    });

    // calculator pages exist per language: /bmi-calculator.html, /en/..., /nl/..., /sv/...
    document.querySelectorAll('[data-calc-page]').forEach(a => {
        a.href = (lang === 'ar' ? '/' : '/' + lang + '/') + a.getAttribute('data-calc-page') + '.html';
    });

    if (foodsTranslations[lang] && foodsTranslations[lang]['meta_title']) {
        /* <title> is static per language URL */
    }
    const descMeta = document.getElementById('metaDescription');
    if (descMeta && foodsTranslations[lang] && foodsTranslations[lang]['meta_desc']) {
        /* meta description is static per language URL */
    }

    // the section cards keep their photos: only labels and counts change with the language
    if (!relabelCategoryBar()) renderCategoryBar();
    visibleCount = CHUNK_SIZE;
    filterFoods();
    updateStructuredDataForSEO();
    restoreListPosition();
}

function toggleFavorite(event, foodId) {
    if (event) {
        event.stopPropagation();
        event.preventDefault();
    }
    foodId = String(foodId);
    const index = favorites.indexOf(foodId);

    if (index > -1) {
        favorites.splice(index, 1);
    } else {
        favorites.push(foodId);
    }

    localStorage.setItem('wibo_favorites', JSON.stringify(favorites));
    updateFavCount();

    if (showFavorites) {
        visibleCount = CHUNK_SIZE;
        filterFoods();
    } else {
        const btn = document.querySelector(`[data-food-id="${foodId}"]`);
        if (btn) {
            const isFav = favorites.includes(foodId);
            btn.classList.toggle('active', isFav);
            btn.innerHTML = `<i class="${isFav ? 'fas' : 'far'} fa-heart"></i>`;
        }
    }
}

function updateFavCount() {
    const count = favorites.length;
    const hCount = document.getElementById('favCount');
    const tabCount = document.getElementById('favFoodsTabCount');
    if (hCount) hCount.textContent = count;
    if (tabCount) tabCount.textContent = count;
}

// A photo that fails to load (a passing network hiccup) is not given up at once: it is asked for again after a
// moment, and only a second failure shows the emoji (section cards and food cards). Returns true while retrying.
function retryImageOnce(img) {
    if (img.dataset.retry) return false;
    img.dataset.retry = '1';
    setTimeout(() => { img.src = img.src.split('?')[0] + '?retry=1'; }, 1500);
    return true;
}

// Chips: "All" + one per master group (count = foods in that group) + the favourites toggle
// "All" and favourites as pills; the 10 master groups as cards (icon, label, item count, accent colour)
function renderCategoryBar() {
    const quick = document.getElementById('categoryQuick');
    const grid = document.getElementById('categoryGrid');
    if (!quick || !grid) return;
    const counts = {};
    allFoods.forEach(f => { counts[f.group] = (counts[f.group] || 0) + 1; });

    quick.setAttribute('aria-label', t('category_bar_label'));
    grid.setAttribute('aria-label', t('category_bar_label'));
    quick.innerHTML = `
        <button class="tab-btn${selectedGroup === 'all' ? ' active' : ''}" type="button" data-group="all" aria-pressed="${selectedGroup === 'all'}">
            <i class="fas fa-utensils"></i><span>${t('tab_all')}</span><span class="tab-count">${allFoods.length}</span>
        </button>
        <button class="tab-btn fav-chip${showFavorites ? ' active' : ''}" type="button" data-fav="1" aria-pressed="${showFavorites}">
            <i class="fas fa-heart"></i><span>${t('tab_fav')}</span><span class="tab-count" id="favFoodsTabCount">${favorites.length}</span>
        </button>`;
    grid.innerHTML = (window.FOOD_GROUPS || []).map(g => `
        <button class="group-card${selectedGroup === g.key ? ' active' : ''}" type="button" data-group="${g.key}" aria-pressed="${selectedGroup === g.key}">
            <span class="gc-icon gc-photo" aria-hidden="true"><img src="/images/categories/${g.key}.webp" alt="" width="66" height="66" loading="lazy" decoding="async"
                onerror="if (retryImageOnce(this)) return; const box=this.parentNode; box.classList.remove('gc-photo'); box.textContent='${g.icon}';"></span>
            <span class="gc-label">${getCategoryLabel(g.key, currentLang)}</span>
            <span class="gc-count">${countLabel(counts[g.key] || 0)}</span>
        </button>`).join('');
}

// Language switch: new labels and counts on the cards already on screen; their <img> elements are left alone.
// Returns false while the bar has not been built yet.
function relabelCategoryBar() {
    const quick = document.getElementById('categoryQuick');
    const grid = document.getElementById('categoryGrid');
    if (!quick || !grid || !grid.querySelector('.group-card')) return false;
    const counts = {};
    allFoods.forEach(f => { counts[f.group] = (counts[f.group] || 0) + 1; });
    quick.setAttribute('aria-label', t('category_bar_label'));
    grid.setAttribute('aria-label', t('category_bar_label'));
    const allLabel = quick.querySelector('[data-group="all"] > span:not(.tab-count)');
    if (allLabel) allLabel.textContent = t('tab_all');
    const favLabel = quick.querySelector('[data-fav] > span:not(.tab-count)');
    if (favLabel) favLabel.textContent = t('tab_fav');
    grid.querySelectorAll('.group-card').forEach(card => {
        const key = card.getAttribute('data-group');
        card.querySelector('.gc-label').textContent = getCategoryLabel(key, currentLang);
        card.querySelector('.gc-count').textContent = countLabel(counts[key] || 0);
    });
    return true;
}

function updateCategoryBarState() {
    document.querySelectorAll('#categoryBar [data-group]').forEach(btn => {
        const on = btn.getAttribute('data-group') === selectedGroup;
        btn.classList.toggle('active', on);
        btn.setAttribute('aria-pressed', on);
    });
    const favBtn = document.querySelector('#categoryBar [data-fav]');
    if (favBtn) {
        favBtn.classList.toggle('active', showFavorites);
        favBtn.setAttribute('aria-pressed', showFavorites);
    }
}

function groupFromUrl() {
    const g = new URLSearchParams(window.location.search).get('group');
    return groupKeys.includes(g) ? g : 'all';
}

// Changes the group; pushState keeps ?lang, ?search and the #food hash, so modal links still work
function selectGroup(group, updateUrl = true) {
    selectedGroup = groupKeys.includes(group) ? group : 'all';
    if (updateUrl) {
        const url = new URL(window.location.href);
        if (selectedGroup === 'all') url.searchParams.delete('group');
        else url.searchParams.set('group', selectedGroup);
        if (url.href !== window.location.href) history.pushState({ group: selectedGroup }, '', url);
    }
    updateCategoryBarState();
    visibleCount = CHUNK_SIZE;
    filterFoods();
}

function toggleFavoritesView() {
    showFavorites = !showFavorites;
    updateCategoryBarState();
    visibleCount = CHUNK_SIZE;
    filterFoods();
}

// After a section is picked, bring the search box and the first results into view
function scrollToResults() {
    const target = document.getElementById('searchBox');
    if (!target) return;
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
}

document.addEventListener('click', function(e) {
    const btn = e.target.closest && e.target.closest('#categoryBar [data-group], #categoryBar [data-fav]');
    if (!btn) return;
    if (btn.hasAttribute('data-fav')) toggleFavoritesView();
    else selectGroup(btn.getAttribute('data-group'));
    scrollToResults();
});

// "Clear filter": back to all foods, no favourites filter, empty search
document.getElementById('resultsClear').addEventListener('click', function() {
    document.getElementById('searchInput').value = '';
    showFavorites = false;
    selectGroup('all');
});

// Arabic count noun agreement follows the last two digits: 1 صنف واحد, 2 صنفان, 3-10 أصناف (also 103-110),
// 11-99 صنفاً (also 111-199...), and 100, 101, 102, 200... صنف
function countLabel(n) {
    if (currentLang === 'ar') {
        if (n === 1) return 'صنف واحد';
        if (n === 2) return 'صنفان';
        const r = n % 100;
        if (r >= 3 && r <= 10) return `${n} أصناف`;
        if (r <= 2) return `${n} صنف`;
        return `${n} صنفاً`;
    }
    if (currentLang === 'nl') return `${n} ${n === 1 ? 'product' : 'producten'}`;
    if (currentLang === 'sv') return `${n} livsmedel`;
    return `${n} ${n === 1 ? 'food' : 'foods'}`;
}

// The line above the grid: what is shown (section / favourites / search) and how many
function updateResultsHeading(term) {
    const heading = document.getElementById('resultsHeading');
    const clear = document.getElementById('resultsClear');
    if (!heading) return;
    const n = currentFilteredList.length;
    const group = selectedGroup !== 'all' ? getCategoryLabel(selectedGroup, currentLang) : '';
    let text;
    if (!n) text = t('res_none');
    else if (showFavorites) text = (group ? t('res_fav_group') : t('res_fav')).replace('{n}', countLabel(n)).replace('{g}', group);
    else if (group) text = t('res_group').replace('{n}', countLabel(n)).replace('{g}', group);
    else text = t('res_all').replace('{n}', n);
    if (n && term) text += t('res_search').replace('{q}', term);
    heading.textContent = text;
    if (clear) clear.hidden = !(selectedGroup !== 'all' || showFavorites || term);
}

// boodi diet programme teaser, shown inside the grid after the first six foods
function dietTeaserHtml() {
    return `
        <aside class="diet-teaser" aria-labelledby="dietTeaserTitle">
            <div class="diet-teaser-icon" aria-hidden="true">👑</div>
            <div class="diet-teaser-text">
                <strong id="dietTeaserTitle">${t('diet_teaser_title')}</strong>
                <span>${t('diet_teaser_desc')}</span>
            </div>
            <a href="boodi.html#diet-program" class="boodi-banner-btn">
                <i class="fas fa-mobile-screen-button" aria-hidden="true"></i>
                <span>${t('diet_teaser_btn')}</span>
            </a>
        </aside>`;
}

window.addEventListener('popstate', function() {
    if (groupFromUrl() !== selectedGroup) selectGroup(groupFromUrl(), false);
});

function onSearchInput() {
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => {
        visibleCount = CHUNK_SIZE;
        filterFoods();
    }, 120);
}

function filterFoods() {
    const term = (document.getElementById('searchInput').value || '').toLowerCase().trim();
    
    let baseList = allFoods;
    if (selectedGroup !== 'all') {
        baseList = baseList.filter(f => f.group === selectedGroup);
    }
    if (showFavorites) {
        baseList = baseList.filter(f => favorites.includes(String(f.id)));
    }

    if (!term) {
        currentFilteredList = baseList;
    } else {
        const has = v => !!v && v.toLowerCase().includes(term);
        currentFilteredList = baseList.filter(f =>
            has(f.name) || has(f.nameEn) || has(f.nameNl) || has((window.FOOD_NAMES_SV || {})[String(f.id)]) ||
            has(f.category) || has(f.categoryEn) || has(f.categoryNl) || has(f.cuisine)
        );
    }

    updateResultsHeading(document.getElementById('searchInput').value.trim());
    renderFoodsIncremental();
}

// Static, crawlable page for pilot foods (generated by scripts/generate_food_pages.py),
// otherwise the dynamic details page.
function foodPageHref(foodId) {
    const slug = (window.FOOD_PAGES || {})[String(foodId)];
    if (!slug) return `/food-details.html?id=${encodeURIComponent(foodId)}`;
    return currentLang === 'ar' ? `/foods/${slug}.html` : `/${currentLang}/foods/${slug}.html`;
}

function renderFoodsIncremental() {
    const grid = document.getElementById('foodGrid');
    const sentinelText = document.getElementById('sentinelText');
    if (!grid) return;

    if (!currentFilteredList || currentFilteredList.length === 0) {
        const msg = showFavorites && favorites.length === 0 ? t('no_favorites') : t('no_results');
        grid.innerHTML = `<div class="results-empty"><i class="fas fa-heart-broken" aria-hidden="true"></i>${msg}</div>`;
        if (sentinelText) sentinelText.textContent = '';
        return;
    }

    const foodsToShow = currentFilteredList.slice(0, visibleCount);
    const unitGram = currentLang === 'ar' ? 'جم' : 'g';

    const cardsHtml = foodsToShow.map(food => {
        const isFav = favorites.includes(String(food.id));
        
        const foodTitle = foodName(food, currentLang);

        const catTitle = getSafeCategoryName(food, currentLang);
        const calVal = Math.round(food.nutrition?.calories || 0);
        const protVal = (food.nutrition?.protein || 0).toFixed(1);
        const carbVal = (food.nutrition?.carbs || 0).toFixed(1);
        const fatVal = ((food.nutrition?.fat !== undefined) ? food.nutrition.fat : (food.nutrition?.fats || 0)).toFixed(1);
        const cardGI = getKnownGI(food);
        const cardGIHtml = cardGI === null ? '' : `
                <div class="card-gi"><span class="gi-num ${getGILevel(cardGI)}">GI ${cardGI}</span>${food.gi_status === 'reviewed' ? `<span class="gi-est">${t('gi_reviewed_badge')}</span>` : ''}</div>`;

        return `
            <a href="${foodPageHref(food.id)}" class="food-card" data-card-id="${food.id}">
                <button class="favorite-btn ${isFav ? 'active' : ''}" 
                        data-food-id="${food.id}" 
                        onclick="toggleFavorite(event, '${food.id}')"
                        title="${t('tab_fav')}"
                        type="button">
                    <i class="${isFav ? 'fas' : 'far'} fa-heart"></i>
                </button>
               ${food.image ? `
    <div style="width: 76px; height: 76px; margin: 0 auto 10px auto; border-radius: 16px; overflow: hidden; box-shadow: 0 2px 8px var(--shadow); border: 1px solid var(--fd-line);">
<img src="${food.image}" alt="${foodTitle}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;" onerror="if (retryImageOnce(this)) return; this.parentElement.style.display='none'; this.parentElement.nextElementSibling.style.display='block';">
    </div>
    <div class="food-icon" style="display: none;">${food.icon || '🍽️'}</div>
` : `
    <div class="food-icon">${food.icon || '🍽️'}</div>
`}
                <h3 class="food-name">${foodTitle}</h3>
                <div style="text-align: center;"><span class="food-category">${catTitle}</span></div>${cardGIHtml}
                <div class="food-stats">
                    <div class="stat-item">
                        <div class="stat-label">${t('calories')}</div>
                        <div class="stat-value">${calVal}</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">${t('protein')}</div>
                        <div class="stat-value">${protVal}${unitGram}</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">${t('carbs')}</div>
                        <div class="stat-value">${carbVal}${unitGram}</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">${t('fats')}</div>
                        <div class="stat-value">${fatVal}${unitGram}</div>
                    </div>
                </div>
            </a>
        `;
    });
    // the diet teaser follows the first six foods (or the last one, if there are fewer)
    cardsHtml.splice(Math.min(6, cardsHtml.length), 0, dietTeaserHtml());
    grid.innerHTML = cardsHtml.join('');

    if (sentinelText) {
        if (visibleCount < currentFilteredList.length) {
            sentinelText.textContent = t('loading_more');
        } else {
            sentinelText.textContent = '';
        }
    }
}

// Food cards and old shared links (foods.html#brown-rice, #food-612): every food opens its own static page
let slugToFoodId = null;

// GI is shown when measured (Atkinson 2021) or an estimate (labelled as such)
function getKnownGI(food) {
    const gi = Number(food.gi);
    if ((food.gi_status === 'measured' || food.gi_status === 'reviewed') && food.gi !== null && food.gi !== undefined && !isNaN(gi)) return gi;
    return null;
}

// GI: <=55 low | 56-69 medium | >=70 high (International GI Tables)
function getGILevel(value) {
    if (value >= 70) return 'high';
    if (value > 55) return 'medium';
    return 'low';
}

// '#brown-rice' or '#food-612' -> food
function foodFromHash(hash) {
    let key = '';
    try { key = decodeURIComponent(String(hash || '').replace(/^#/, '')); } catch (e) { return null; }
    if (!key) return null;
    const byId = /^food-(\d+)$/.exec(key);
    let id = byId ? byId[1] : null;
    if (!id) {
        if (!slugToFoodId) {
            slugToFoodId = {};
            Object.entries(window.FOOD_PAGES || {}).forEach(([fid, slug]) => { slugToFoodId[slug] = fid; });
        }
        id = slugToFoodId[key];
    }
    return id ? (allFoods.find(f => String(f.id) === String(id)) || null) : null;
}

// Back from a food page: the list returns to the same place. A card click saves the scroll position, the food and
// the list state (section, favourites, search, cards shown); the next load of this page that is a step back in
// history (browser back or the page's back button), or that comes from that food's page, restores them once.
document.getElementById('foodGrid').addEventListener('click', function(e) {
    const card = e.target.closest('a.food-card');
    if (!card || e.target.closest('.favorite-btn')) return;
    const id = card.getAttribute('data-card-id');
    try {
        sessionStorage.setItem('foods_scroll_pos', String(Math.round(window.scrollY)));
        sessionStorage.setItem('foods_last_food', (window.FOOD_PAGES || {})[id] || `food-${id}`);
        sessionStorage.setItem('foods_list_state', JSON.stringify({
            id, group: selectedGroup, fav: showFavorites, visible: visibleCount,
            search: document.getElementById('searchInput').value
        }));
    } catch (err) {}
});

function takeSavedListPosition() {
    let pos = null, slug = null, state = null;
    try {
        pos = sessionStorage.getItem('foods_scroll_pos');
        slug = sessionStorage.getItem('foods_last_food');
        state = JSON.parse(sessionStorage.getItem('foods_list_state') || 'null');
        ['foods_scroll_pos', 'foods_last_food', 'foods_list_state'].forEach(k => sessionStorage.removeItem(k));
    } catch (err) { return null; }
    if (pos === null || !slug || !state) return null;
    const nav = (performance.getEntriesByType && performance.getEntriesByType('navigation')[0]) || {};
    let fromFood = false;
    try { fromFood = new URL(document.referrer).pathname.endsWith('/foods/' + slug + '.html'); } catch (err) {}
    if (nav.type !== 'back_forward' && !fromFood) return null;
    return { pos: Number(pos) || 0, state };
}

let pendingListRestore = null;

// Runs after the cards of the restored list are on screen (end of changeLanguage)
function restoreListPosition() {
    const saved = pendingListRestore;
    pendingListRestore = null;
    if (!saved) return;
    if (saved.state.visible > visibleCount) {
        visibleCount = saved.state.visible;
        renderFoodsIncremental();
    }
    const anchor = () => {
        const card = document.querySelector(`#foodGrid a.food-card[data-card-id="${CSS.escape(String(saved.state.id))}"]`);
        if (card) card.scrollIntoView({ block: 'center', behavior: 'instant' });
        else window.scrollTo({ top: saved.pos, behavior: 'instant' });
    };
    anchor();
    // Web fonts and images that finish after this change the card heights above: anchor again on the card,
    // unless the reader has started scrolling
    let moved = false;
    const stop = () => { moved = true; };
    ['wheel', 'touchstart', 'keydown'].forEach(ev => window.addEventListener(ev, stop, { once: true, passive: true }));
    const again = () => { if (!moved) anchor(); };
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(again);
    if (document.readyState !== 'complete') window.addEventListener('load', again, { once: true });
}

// A page kept whole by the browser (back/forward cache) is already in place: drop the saved position
window.addEventListener('pageshow', function(e) {
    if (e.persisted) try { ['foods_scroll_pos', 'foods_last_food', 'foods_list_state'].forEach(k => sessionStorage.removeItem(k)); } catch (err) {}
});

// A #slug typed or pasted later goes to the food's page as well
window.addEventListener('hashchange', function() {
    const food = foodFromHash(location.hash);
    if (food) location.replace(foodPageHref(food.id));
});

function setupInfiniteScroll() {
    const sentinel = document.getElementById('scrollSentinel');
    if (!sentinel) return;

    if (scrollObserver) scrollObserver.disconnect();

    scrollObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            if (visibleCount < currentFilteredList.length) {
                visibleCount += CHUNK_SIZE;
                renderFoodsIncremental();
            }
        }
    }, {
        root: null,
        rootMargin: '400px',
        threshold: 0.1
    });

    scrollObserver.observe(sentinel);
}

function updateStructuredDataForSEO() {
    if (!allFoods || allFoods.length === 0) return;
    // Created here, not in the markup: an empty JSON-LD tag is invalid for crawlers that skip JS
    let schemaEl = document.getElementById('foodsItemListSchema');
    if (!schemaEl) {
        schemaEl = document.createElement('script');
        schemaEl.type = 'application/ld+json';
        schemaEl.id = 'foodsItemListSchema';
        document.head.appendChild(schemaEl);
    }

    // Summary list of the indexable food pages. Never Product: Google requires
    // offers/review/aggregateRating on it, which an information site cannot give.
    const itemsToSchema = allFoods.filter(f => (window.FOOD_PAGES || {})[String(f.id)]).slice(0, 100).map((f, index) => {
        const name = foodName(f, currentLang);
        return {
            "@type": "ListItem",
            "position": index + 1,
            "name": name,
            "url": 'https://wibohealth.com' + foodPageHref(f.id)
        };
    });

    schemaEl.textContent = JSON.stringify({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "numberOfItems": itemsToSchema.length,
        "itemListElement": itemsToSchema
    });
}

window.addEventListener('storage', function(e) {
    if (e.key === 'wibo_theme') {
        if (e.newValue === 'dark') {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    }
});

window.addEventListener('DOMContentLoaded', async function() {
    const savedTheme = localStorage.getItem('wibo_theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        const tIcon = document.querySelector('.theme-toggle i');
        if (tIcon) tIcon.className = 'fas fa-sun';
    }

    // the slim food index (data/foods-index.json, scripts/build_guide_data.py), fetched after the first paint
    const dbCandidates = await loadFoodsIndex();

    if (dbCandidates.length > 0) {
        allFoods = dbCandidates;
        const totalCountEl = document.getElementById('totalCount');
        if (totalCountEl) totalCountEl.textContent = allFoods.length;
    }

    // ?search=VALUE (e.g. from the home page "What did you cook today?" bar) pre-filters the list
    const searchParam = (new URLSearchParams(window.location.search).get('search') || '').trim().slice(0, 80);
    const searchBox = document.getElementById('searchInput');
    if (searchParam && searchBox) searchBox.value = searchParam;

    // ?group=KEY (e.g. foods.html?group=fruits) opens with that category selected
    selectedGroup = groupFromUrl();

    // Back from a food page: the same section, favourites view and search as when the card was followed
    pendingListRestore = takeSavedListPosition();
    if (pendingListRestore) {
        const st = pendingListRestore.state;
        selectedGroup = groupKeys.includes(st.group) ? st.group : 'all';
        showFavorites = !!st.fav;
        if (searchBox) searchBox.value = String(st.search || '').slice(0, 80);
        history.scrollRestoration = 'manual';
    }

    changeLanguage(currentLang);
    updateFavCount();
    setupInfiniteScroll();

    const linkedFood = foodFromHash(location.hash);
    if (linkedFood) location.replace(foodPageHref(linkedFood.id));   // normally done by the early redirect
});

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const icon = document.querySelector('.theme-toggle i');
    if (document.body.classList.contains('dark-mode')) {
        icon.className = 'fas fa-sun';
        localStorage.setItem('wibo_theme', 'dark');
    } else {
        icon.className = 'fas fa-moon';
        localStorage.setItem('wibo_theme', 'light');
    }
}

function toggleMobileMenu() {
    const mobileNav = document.getElementById('mobileNav');
    const overlay = document.querySelector('.mobile-nav-overlay');
    if (mobileNav && overlay) {
        mobileNav.classList.toggle('active');
        overlay.classList.toggle('active');
        document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
    }
}
