/* Interactive supplements guide of supplements.html (and /en/, /nl/supplements.html), moved out of the page on
   2026-11-23. Loaded with defer; the language comes from <html lang>; the copy for every language is in
   `translations` below (read by scripts/generate_root_pages.py). Data: data/supplements-index.json for the cards and
   search (after the first paint), data/supplements-full.json only when a supplement or the comparison is opened. */
const SUPP_SRC = (document.currentScript && document.currentScript.dataset) || {};
let supplementsData = [];
let supplementsFullPromise = null;

function loadSupplementsJson(url) {
    return fetch(url, { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error('supplements data ' + r.status); return r.json(); });
}

// data/supplements-index.json is columnar: {f: field names, l: {field: lookup list}, r: rows}
function decodeIndex(d) {
    if (Array.isArray(d)) return d;
    return d.r.map(function (row) {
        var o = {};
        d.f.forEach(function (k, i) {
            var v = row[i];
            if (v === undefined || v === null) return;
            o[k] = d.l[k] ? d.l[k][v] : v;
        });
        return o;
    });
}

function ensureFullSupplements() {
    if (!supplementsFullPromise) {
        supplementsFullPromise = loadSupplementsJson(SUPP_SRC.full || '/data/supplements-full.json')
            .then(function (full) { supplementsData = full; })
            .catch(function (e) { supplementsFullPromise = null; console.warn(e); });
    }
    return supplementsFullPromise;
}

const translations = {
    ar: {
        nav_home: "الرئيسية",
        nav_foods: "الأطعمة",
        nav_calculators: "الحاسبات",
        nav_recipes: "الوصفات",
        nav_articles: "المقالات",
        nav_supplements: "المكملات",
        nav_boodi_app: "بودي 💚",
        nav_doctor: "من نحن",
        hero_title: "💊 دليل المكملات الغذائية",
        hero_desc: "دليلك الشامل والموثوق لعالم المكملات الغذائية - اكتشف الفوائد، الجرعات المناسبة، أفضل أوقات الاستخدام، والتحذيرات المهمة لكل مكمل",
        stat_supplements: "مكمل غذائي",
        stat_categories: "تصنيفات رئيسية",
        stat_verified: "معلومات موثوقة",
        search_placeholder: "ابحث بالعربي أو English أو Nederlands أو Svenska...",
        search_helper: "ابحث في اسم المكمل، الفوائد، أو التصنيف (عربي / English / Nederlands / Svenska)",
        compare_hint_title: "💡 ميزة جديدة:",
        compare_hint_text: "علّم على المربعات في زاوية المكملات لمقارنتها جنباً إلى جنب! ⚖️",
        no_results_title: "لم يتم العثور على نتائج",
        no_results_desc: "جرب البحث بكلمات مختلفة",
        compare_btn_text: "قارن المكملات",
        read_more: "اقرأ المزيد",
        modal_benefits: "الفوائد والاستخدامات",
        modal_dosage: "الجرعة والاستخدام",
        modal_dosage_rec: "الجرعة الموصى بها:",
        modal_dosage_timing: "أفضل وقت للاستخدام:",
        modal_dosage_freq: "التكرار:",
        modal_warnings: "تحذيرات مهمة",
        modal_interactions: "التفاعلات الدوائية",
        modal_sources: "المصادر الطبيعية",
        modal_close: "إغلاق",
        modal_refs_title: "المراجع العلمية",
        modal_related: "مكملات ذات صلة",
        modal_forms: "أفضل الأشكال المتوفرة",
        modal_copy_link: "نسخ رابط المكمل المباشر",
        modal_link_copied: "تم نسخ الرابط",
        modal_refs: "📚 المراجع العلمية: الهيئة الأوروبية لسلامة الأغذية (EFSA) • المعاهد الوطنية للصحة (NIH - ODS) • قواعد بيانات PubMed / Cochrane",
        modal_disclaimer: "<strong>⚖️ إخلاء مسؤولية طبي:</strong> المعلومات والبيانات الواردة هنا هي لأغراض التثقيف الصحي والإرشاد الغذائي فقط، ولا تُعتبر تشخيصاً طبياً ولا تُغني بأي حال عن الاستشارة الطبية المباشرة من طبيبك المعالج أو الصيدلي. استشر طبيبك دائماً قبل البدء بأي مكمل، خصوصاً في حالات الحمل والرضاعة أو عند استخدام أدوية مزمنة.",
        compare_title: "مقارنة المكملات",
        compare_subtitle: "مقارنة شاملة للمكملات المختارة",
        cat_muscle: "بناء العضلات",
        cat_health: "صحة عامة",
        cat_weight: "تخسيس",
        cat_sleep: "نوم ونفسية",
        cat_energy: "طاقة وأداء",
        cat_bones: "عظام ومفاصل",
        cat_heart: "صحة القلب",
        cat_diabetes: "سكر الدم والأيض",
        cat_herbs: "أعشاب وزيوت طبيعية",
        warn_title: "تحذير طبي مهم",
        warn_desc: "المعلومات هنا تعليمية عامة فقط وليست استشارة طبية شخصية. استشر طبيبك دائماً.",
        warn_btn: "إخلاء المسؤولية",
        footer_about: "من نحن",
        footer_contact: "اتصل بنا",
        nav_partners: "الشراكات",
        footer_partners: "الشراكات",
        footer_food_index: "فهرس الأطعمة",
        footer_supp_index: "فهرس المكملات",
        footer_privacy: "سياسة الخصوصية",
        footer_terms: "شروط الاستخدام",
        footer_rights: "© 2026 WiBo Health. جميع الحقوق محفوظة.",
        footer_boodi: "مُطور بـ ♥ من أجل بودي"
    },
    en: {
        nav_home: "Home",
        nav_foods: "Foods",
        nav_calculators: "Calculators",
        nav_recipes: "Recipes",
        nav_articles: "Articles",
        nav_supplements: "Supplements",
        nav_boodi_app: "boodi App 💚",
        nav_doctor: "About Us",
        hero_title: "💊 Dietary Supplements Guide",
        hero_desc: "Your comprehensive clinical guide to dietary supplements - explore benefits, optimal dosages, timing, and important warnings.",
        stat_supplements: "Supplements",
        stat_categories: "Main Categories",
        stat_verified: "Verified Info",
        search_placeholder: "Search supplement, benefit or category...",
        search_helper: "Search by supplement name, benefits, or category (EN / NL / AR / SV)",
        compare_hint_title: "💡 New Feature:",
        compare_hint_text: "Tick the checkbox on card corners to compare side-by-side! ⚖️",
        no_results_title: "No Results Found",
        no_results_desc: "Try searching with different keywords",
        compare_btn_text: "Compare Supplements",
        read_more: "Read More",
        modal_benefits: "Benefits & Uses",
        modal_dosage: "Dosage & Usage",
        modal_dosage_rec: "Recommended Dosage:",
        modal_dosage_timing: "Best Time to Take:",
        modal_dosage_freq: "Frequency:",
        modal_warnings: "Important Warnings",
        modal_interactions: "Drug Interactions",
        modal_sources: "Natural Sources",
        modal_close: "Close",
        modal_refs_title: "Scientific references",
        modal_related: "Related supplements",
        modal_forms: "Best forms to choose",
        modal_copy_link: "Copy direct link to this supplement",
        modal_link_copied: "Link copied",
        modal_refs: "📚 Scientific references: European Food Safety Authority (EFSA) • National Institutes of Health (NIH - ODS) • PubMed / Cochrane databases",
        modal_disclaimer: "<strong>⚖️ Medical disclaimer:</strong> The information and data provided here are for health education and nutritional guidance only. They are not a medical diagnosis and never replace a direct consultation with your doctor or pharmacist. Always consult your doctor before starting any supplement, especially during pregnancy or breastfeeding or when taking long-term medication.",
        compare_title: "Supplements Comparison",
        compare_subtitle: "Comprehensive side-by-side comparison",
        cat_muscle: "Muscle Building",
        cat_health: "General Health",
        cat_weight: "Weight Loss",
        cat_sleep: "Sleep & Mood",
        cat_energy: "Energy & Performance",
        cat_bones: "Bones & Joints",
        cat_heart: "Heart Health",
        cat_diabetes: "Blood sugar & metabolism",
        cat_herbs: "Herbs & natural oils",
        warn_title: "Important Medical Warning",
        warn_desc: "This information is educational only and does not constitute medical advice. Always consult your doctor.",
        warn_btn: "Disclaimer",
        footer_about: "About Us",
        footer_contact: "Contact Us",
        nav_partners: "Partnerships",
        footer_partners: "Partnerships",
        footer_food_index: "Food index",
        footer_supp_index: "Supplement index",
        footer_privacy: "Privacy Policy",
        footer_terms: "Terms of Use",
        footer_rights: "© 2026 WiBo Health. All rights reserved.",
        footer_boodi: "Developed with ♥ for boodi"
    },
    nl: {
        nav_home: "Home",
        nav_foods: "Voedingswijzer",
        nav_calculators: "Calculators",
        nav_recipes: "Recepten",
        nav_articles: "Artikelen",
        nav_supplements: "Supplementen",
        nav_boodi_app: "boodi App 💚",
        nav_doctor: "Over Ons",
        hero_title: "💊 Voedingssupplementengids",
        hero_desc: "Uw betrouwbare klinische gids voor supplementen - ontdek voordelen, optimale doseringen, innamemomenten en belangrijke waarschuwingen.",
        stat_supplements: "Supplementen",
        stat_categories: "Hoofdcategorieën",
        stat_verified: "Geverifieerde info",
        search_placeholder: "Zoek supplement, voordeel of categorie...",
        search_helper: "Zoek op supplementnaam, voordelen of categorie (Nederlands / EN / AR / SV)",
        compare_hint_title: "💡 Nieuwe functie:",
        compare_hint_text: "Vink het vakje aan om supplementen naast elkaar te vergelijken! ⚖️",
        no_results_title: "Geen resultaten gevonden",
        no_results_desc: "Probeer te zoeken met andere trefwoorden",
        compare_btn_text: "Vergelijk supplementen",
        read_more: "Lees meer",
        modal_benefits: "Voordelen en toepassingen",
        modal_dosage: "Dosering en inname",
        modal_dosage_rec: "Aanbevolen dosering:",
        modal_dosage_timing: "Beste innamemoment:",
        modal_dosage_freq: "Frequentie:",
        modal_warnings: "Belangrijke waarschuwingen",
        modal_interactions: "Interacties met medicijnen",
        modal_sources: "Natuurlijke bronnen",
        modal_close: "Sluiten",
        modal_refs_title: "Wetenschappelijke bronnen",
        modal_related: "Verwante supplementen",
        modal_forms: "Beste vormen om te kiezen",
        modal_copy_link: "Directe link naar dit supplement kopiëren",
        modal_link_copied: "Link gekopieerd",
        modal_refs: "📚 Wetenschappelijke bronnen: Europese Autoriteit voor Voedselveiligheid (EFSA) • National Institutes of Health (NIH - ODS) • PubMed / Cochrane-databanken",
        modal_disclaimer: "<strong>⚖️ Medische disclaimer:</strong> De informatie en gegevens hier zijn uitsluitend bedoeld voor gezondheidsvoorlichting en voedingsadvies. Ze vormen geen medische diagnose en vervangen nooit een direct consult bij je behandelend arts of apotheker. Overleg altijd met je arts voordat je met een supplement begint, vooral tijdens zwangerschap of borstvoeding of bij langdurig medicijngebruik.",
        compare_title: "Supplementen Vergelijken",
        compare_subtitle: "Volledige vergelijking van geselecteerde supplementen",
        cat_muscle: "Spieropbouw",
        cat_health: "Algemene gezondheid",
        cat_weight: "Gewichtsverlies",
        cat_sleep: "Slaap & Gemoedstoestand",
        cat_energy: "Energie & Prestatie",
        cat_bones: "Botten & Gewrichten",
        cat_heart: "Hart & Bloedvaten",
        cat_diabetes: "Bloedsuiker & stofwisseling",
        cat_herbs: "Kruiden & natuurlijke oliën",
        warn_title: "Belangrijke medische waarschuwing",
        warn_desc: "Deze informatie is uitsluitend educatief en vervangt geen medisch advies. Raadpleeg altijd een arts.",
        warn_btn: "Disclaimer",
        footer_about: "Over Ons",
        footer_contact: "Contact",
        nav_partners: "Partners",
        footer_partners: "Partners",
        footer_food_index: "Voedingsindex",
        footer_supp_index: "Supplementenindex",
        footer_privacy: "Privacybeleid",
        footer_terms: "Gebruiksvoorwaarden",
        footer_rights: "© 2026 WiBo Health. Alle rechten voorbehouden.",
        footer_boodi: "Ontwikkeld met ♥ voor boodi"
    }
};

function smartClinicalTranslate(text, lang) {
    if (!text || lang === 'ar') return text;
    let res = String(text);
    res = res.replace(/جرام|جم/g, 'g').replace(/ملغ|ملغم/g, 'mg').replace(/ميكروجرام/g, 'mcg');
    res = res.replace(/كبسولة/g, 'capsule').replace(/كبسولات/g, 'capsules').replace(/حبة/g, 'tablet');
    
    const dict = {
        nl: {
            'قبل النوم': 'Voor het slapengaan',
            'قبل النوم أو بين الوجبات البعيدة': 'Voor het slapengaan of tussen maaltijden',
            'مرة واحدة يومياً': '1x per dag',
            'مرتين يومياً': '2x per dag',
            '3 مرات يومياً': '3x per dag',
            'يومياً': 'Dagelijks',
            'مع وجبة دسمة': 'Bij een vetrijke maaltijd',
            'مع الوجبة': 'Bij de maaltijd',
            'مع وجبة الإفطار': 'Bij het ontbijt',
            'بعد التمرين': 'Direct na de training',
            'قبل التمرين': 'Voor de training',
            'قبل التمرين بـ 30 دقيقة': '30 minuten voor de training',
            'صباحاً': "'s Ochtends",
            'مساءً': "'s Avonds",
            'عند اللزوم': 'Indien nodig',
            'مع كوب ماء كبير': 'Met een groot glas water',
            'لا توجد تفاعلات خطيرة': 'Geen ernstige interacties bekend',
            'لا توجد': 'Geen bekend'
        },
        en: {
            'قبل النوم': 'Before bedtime',
            'قبل النوم أو بين الوجبات البعيدة': 'Before sleep or between meals',
            'مرة واحدة يومياً': 'Once daily',
            'مرتين يومياً': 'Twice daily',
            '3 مرات يومياً': '3 times daily',
            'يومياً': 'Daily',
            'مع وجبة دسمة': 'With a fatty meal',
            'مع الوجبة': 'With a meal',
            'مع وجبة الإفطار': 'With breakfast',
            'بعد التمرين': 'Post-workout',
            'قبل التمرين': 'Pre-workout',
            'قبل التمرين بـ 30 دقيقة': '30 minutes pre-workout',
            'صباحاً': 'In the morning',
            'مساءً': 'In the evening',
            'عند اللزوم': 'As needed',
            'مع كوب ماء كبير': 'With a large glass of water',
            'لا توجد تفاعلات خطيرة': 'No serious interactions known',
            'لا توجد': 'None known'
        }
    };

    const langDict = dict[lang] || {};
    for (const [arKey, translatedVal] of Object.entries(langDict)) {
        res = res.split(arKey).join(translatedVal);
    }
    return res;
}

function detectInitialLang() {
    return document.documentElement.lang || 'ar';   // the page language is fixed by its URL (/, /en/, /nl/, /sv/)
}

let currentLang = detectInitialLang();

function t(key) {
    return translations[currentLang]?.[key] || translations['ar'][key] || key;
}

function changeLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('preferred_language', lang);
    localStorage.setItem('wibo_language', lang);
    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
    updatePageLanguage();
}

function updatePageLanguage() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (key && translations[currentLang]?.[key]) {
            el.innerHTML = translations[currentLang][key];
        }
    });

    const searchInput = document.getElementById('searchInput');
    if (searchInput) searchInput.placeholder = t('search_placeholder');

    document.querySelectorAll('.lang-btn').forEach(btn => {
        const btnLang = btn.getAttribute('data-lang-toggle');
        if (btnLang === currentLang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // إعادة عرض فورية خفيفة بدون لاغ
    displaySupplements(true);

    if (modalSuppId !== null) {
        const openSupp = supplementsData.find(s => s.id === modalSuppId);
        if (openSupp) renderSupplementModal(openSupp);
    }
}

function initializeTheme() {
    const savedTheme = localStorage.getItem('wibo_theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        const icon = document.querySelector('.theme-toggle i');
        if (icon) icon.className = 'fas fa-sun';
    }
}

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const icon = document.querySelector('.theme-toggle i');
    if (document.body.classList.contains('dark-mode')) {
        if (icon) icon.className = 'fas fa-sun';
        localStorage.setItem('wibo_theme', 'dark');
    } else {
        if (icon) icon.className = 'fas fa-moon';
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

function getCategoryName(category) {
    const catMap = {
        'بناء-عضلات': 'cat_muscle',
        'صحة-عامة': 'cat_health',
        'تخسيس': 'cat_weight',
        'نوم-نفسية': 'cat_sleep',
        'نوم-ومزاج': 'cat_sleep',
        'طاقة': 'cat_energy',
        'طاقة-أداء': 'cat_energy',
        'عظام-مفاصل': 'cat_bones',
        'صحة-العظام': 'cat_bones',
        'صحة-القلب': 'cat_heart',
        'سكر-الدم-والأيض': 'cat_diabetes',
        'أعشاب-وزيوت-طبيعية': 'cat_herbs'
    };
    const key = catMap[category];
    return key ? t(key) : category;
}

// ==========================================
// القاموس السريري الشامل لترجمة وسوم المكملات (Universal Tag Engine)
// ==========================================
const tagTranslations = {
    nl: {
        'بروتين': 'Eiwit', 'بناء عضلات': 'Spieropbouw', 'تعافي': 'Herstel', 'استشفاء': 'Herstel',
        'بطيء الامتصاص': 'Langzame afgifte', 'قبل النوم': 'Voor het slapen', 'قوة': 'Kracht',
        'أداء': 'Prestatie', 'كتلة عضلية': 'Spiermassa', 'أحماض أمينية': 'Aminozuren',
        'منع الهدم': 'Anti-katabool', 'تحمل عضلي': 'Uithoudingsvermogen', 'فيتامينات': 'Vitaminen',
        'معادن': 'Mineralen', 'صحة عامة': 'Algemene Gezondheid', 'أوميغا 3': 'Omega-3',
        'قلب': 'Hart', 'صحة القلب': 'Hartgezondheid', 'دماغ': 'Brein', 'صحة الدماغ': 'Hersenfunctie',
        'مضاد التهاب': 'Ontstekingsremmend', 'فيتامين د': 'Vitamine D', 'عظام': 'Botten',
        'صحة العظام': 'Botgezondheid', 'مناعة': 'Weerstand', 'مزاج': 'Stemming', 'نوم': 'Slaap',
        'عضلات': 'Spieren', 'طاقة': 'Energie', 'نشاط': 'Vitaliteit', 'هرمونات': 'Hormonen',
        'بشرة': 'Huid', 'حرق دهون': 'Vetverbranding', 'أيض': 'Metabolisme', 'تمثيل غذائي': 'Metabolisme',
        'مضاد أكسدة': 'Antioxidant', 'مضادات أكسدة': 'Antioxidanten', 'حفظ عضلات': 'Spierbehoud',
        'تحسين جسم': 'Lichaamssamenstelling', 'تركيب الجسم': 'Lichaamssamenstelling',
        'مفاصل': 'Gewrichten', 'غضاريف': 'Kraakbeen', 'تركيز': 'Focus', 'ذاكرة': 'Geheugen',
        'هضم': 'Spijsvertering', 'صحة الأمعاء': 'Darmgezondheid', 'كبد': 'Lever', 'صحة الكبد': 'Leverfunctie',
        'كلى': 'Nieren', 'توتر': 'Anti-stress', 'قلق': 'Rustgevend', 'استرخاء': 'Ontspanning',
        'حيوية': 'Vitaliteit', 'شعر': 'Haar', 'أظافر': 'Nagels', 'خصوبة': 'Vruchtbaarheid',
        'تستوستيرون': 'Testosteron', 'أستروجين': 'Oestrogeenbalans', 'سكر الدم': 'Bloedsuikerspiegel',
        'حساسية الإنسولين': 'Insulinegevoeligheid', 'كوليسترول': 'Cholesterol', 'ضغط الدم': 'Bloeddruk',
        'دورة دموية': 'Bloedsomloop', 'أداء رياضي': 'Sportprestaties', 'كولاجين': 'Collageen',
        'ألياف': 'Vezels', 'بروبيوتيك': 'Probiotica', 'إنزيمات': 'Enzymen', 'زنك': 'Zink',
        'حديد': 'IJzer', 'مغنيسيوم': 'Magnesium', 'كالسيوم': 'Calcium', 'كبح شهية': 'Eetlustbeheersing',
        'وزن': 'Gewichtsverlies', 'تخسيس': 'Afslanken', 'طبيعي': 'Natuurlijk', 'أعشاب': 'Kruiden'
    },
    en: {
        'بروتين': 'Protein', 'بناء عضلات': 'Muscle Building', 'تعافي': 'Recovery', 'استشفاء': 'Recovery',
        'بطيء الامتصاص': 'Slow Release', 'قبل النوم': 'Bedtime', 'قوة': 'Strength',
        'أداء': 'Performance', 'كتلة عضلية': 'Muscle Mass', 'أحماض أمينية': 'Amino Acids',
        'منع الهدم': 'Anti-catabolic', 'تحمل عضلي': 'Endurance', 'فيتامينات': 'Vitamins',
        'معادن': 'Minerals', 'صحة عامة': 'General Health', 'أوميغا 3': 'Omega-3',
        'قلب': 'Heart', 'صحة القلب': 'Heart Health', 'دماغ': 'Brain', 'صحة الدماغ': 'Brain Function',
        'مضاد التهاب': 'Anti-inflammatory', 'فيتامين د': 'Vitamin D', 'عظام': 'Bones',
        'صحة العظام': 'Bone Health', 'مناعة': 'Immunity', 'مزاج': 'Mood', 'نوم': 'Sleep',
        'عضلات': 'Muscles', 'طاقة': 'Energy', 'نشاط': 'Vitality', 'هرمونات': 'Hormones',
        'بشرة': 'Skin', 'حرق دهون': 'Fat Burn', 'أيض': 'Metabolism', 'تمثيل غذائي': 'Metabolism',
        'مضاد أكسدة': 'Antioxidant', 'مضادات أكسدة': 'Antioxidants', 'حفظ عضلات': 'Muscle Preservation',
        'تحسين جسم': 'Body Composition', 'تركيب الجسم': 'Body Composition',
        'مفاصل': 'Joints', 'غضاريف': 'Cartilage', 'تركيز': 'Focus', 'ذاكرة': 'Memory',
        'هضم': 'Digestion', 'صحة الأمعاء': 'Gut Health', 'كبد': 'Liver', 'صحة الكبد': 'Liver Support',
        'كلى': 'Kidneys', 'توتر': 'Anti-stress', 'قلق': 'Calming', 'استرخاء': 'Relaxation',
        'حيوية': 'Vitality', 'شعر': 'Hair', 'أظافر': 'Nails', 'خصوبة': 'Fertility',
        'تستوستيرون': 'Testosterone', 'أستروجين': 'Estrogen Balance', 'سكر الدم': 'Blood Sugar',
        'حساسية الإنسولين': 'Insulin Sensitivity', 'كوليسترول': 'Cholesterol', 'ضغط الدم': 'Blood Pressure',
        'دورة دموية': 'Circulation', 'أداء رياضي': 'Athletic Performance', 'كولاجين': 'Collageen',
        'ألياف': 'Fiber', 'بروبيوتيك': 'Probiotics', 'إنزيمات': 'Enzymes', 'زنك': 'Zinc',
        'حديد': 'Iron', 'مغنيسيوم': 'Magnesium', 'كالسيوم': 'Calcium', 'كبح شهية': 'Appetite Control',
        'وزن': 'Weight Loss', 'تخسيس': 'Slimming', 'طبيعي': 'Natural', 'أعشاب': 'Herbs'
    }
};

// دالة استخراج وترجمة وتطهير الوسوم ومنع تسريب الحروف العربية
function renderSupplementTags(supp) {
    if (currentLang === 'ar') {
        return (supp.tags || []).map(t => `<span class="tag">${t}</span>`).join('');
    }

    let candidateTags = [];
    if (currentLang === 'nl' && Array.isArray(supp.tagsNl) && supp.tagsNl.length > 0) {
        candidateTags = [...supp.tagsNl];
    } else if (currentLang === 'en' && Array.isArray(supp.tagsEn) && supp.tagsEn.length > 0) {
        candidateTags = [...supp.tagsEn];
    } else {
        candidateTags = [...(supp.tags || [])];
    }

    const arabicRegex = /[\u0600-\u06FF]/;
    const finalizedTags = candidateTags.map(tag => {
        const cleanTag = (tag || '').trim();
        if (arabicRegex.test(cleanTag)) {
            return tagTranslations[currentLang]?.[cleanTag] || tagTranslations['en']?.[cleanTag] || '';
        }
        return cleanTag;
    }).filter(tag => tag && tag.length > 0 && !arabicRegex.test(tag));

    if (finalizedTags.length === 0 && supp.tags && supp.tags.length > 0) {
        supp.tags.forEach(t => {
            const tr = tagTranslations[currentLang]?.[t.trim()] || tagTranslations['en']?.[t.trim()];
            if (tr && !arabicRegex.test(tr)) {
                finalizedTags.push(tr);
            }
        });
    }

    return finalizedTags.map(t => `<span class="tag">${t}</span>`).join('');
}

// ==========================================
// محرك الرندرة فائق السرعة (Chunked Infinite Engine)
// ==========================================
const BATCH_SIZE = 24;
let currentRenderIndex = 0;
let currentFilteredSupplements = [];
let searchTerm = '';
window.selectedSupplements = new Set();
let scrollObserver = null;

function buildCardHtml(supp, arrowIcon) {
    const isChecked = window.selectedSupplements.has(supp.id) ? 'checked' : '';
    
    let title = supp.name;
    let subtitle = supp.englishName || '';
    
    if (currentLang === 'nl') {
        title = supp.nameNl || supp.englishName || supp.name;
        subtitle = (supp.englishName && supp.englishName !== title) ? supp.englishName : '';
    } else if (currentLang === 'en') {
        title = supp.englishName || supp.name;
        subtitle = '';
    }

    const summary = (currentLang === 'nl' && supp.summaryNl) ? supp.summaryNl :
                    (currentLang === 'en' && supp.summaryEn) ? supp.summaryEn :
                    (supp.summary || '');

    const tagsList = renderSupplementTags(supp);
    
    return `
    <div class="supplement-card">
        <div class="compare-checkbox-wrapper">
            <input type="checkbox" 
                   class="compare-checkbox" 
                   id="compare-${supp.id}" 
                   value="${supp.id}"
                   ${isChecked}
                   onchange="toggleSupplementCompare(${supp.id}, this)">
            <label for="compare-${supp.id}" class="compare-label">
                <i class="fas fa-check"></i>
            </label>
        </div>
        <div class="card-content" onclick="openModal(${supp.id})" tabindex="0" role="button" onkeydown="if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openModal(${supp.id}); }" style="cursor: pointer;">
            <div class="supplement-header">
                <div class="supplement-icon">${supp.icon || '💊'}</div>
                <h3>${title}</h3>
                ${subtitle ? `<p class="english-name">${subtitle}</p>` : ''}
            </div>
            <div class="supplement-body">
                <span class="supplement-category">${getCategoryName(supp.category)}</span>
                <p class="supplement-summary">${summary}</p>
                <div class="supplement-tags">
                    ${tagsList}
                </div>
                <div class="supplement-footer">
                    <span class="read-more-btn">
                        ${t('read_more')}
                        <i class="fas ${arrowIcon}"></i>
                    </span>
                </div>
            </div>
        </div>
    </div>
    `;
}

function displaySupplements(reset = true) {
    const grid = document.getElementById('supplementsGrid');
    const loading = document.querySelector('.loading');
    const noResults = document.getElementById('noResults');
    
    if (loading) loading.classList.remove('show');
    if (typeof supplementsData === 'undefined' || !grid) return;

    const totalEl = document.getElementById('supplementsTotalCount');
    if (totalEl) totalEl.textContent = supplementsData.length;

    if (reset) {
        const term = (searchTerm || '').toLowerCase().trim();
        currentFilteredSupplements = supplementsData.filter(supp => {
            if (!term) return true;
            const nameMatch = supp.name && supp.name.toLowerCase().includes(term);
            const enMatch = supp.englishName && supp.englishName.toLowerCase().includes(term);
            const nlMatch = supp.nameNl && supp.nameNl.toLowerCase().includes(term);
            const svName = (window.SUPP_NAMES_SV || {})[supp.slug];
            const svMatch = !!svName && svName.toLowerCase().includes(term);
            const tagMatch = supp.tags && supp.tags.some(tag => tag.toLowerCase().includes(term));
            return nameMatch || enMatch || nlMatch || svMatch || tagMatch;
        });

        grid.innerHTML = '';
        currentRenderIndex = 0;

        if (currentFilteredSupplements.length === 0) {
            if (noResults) noResults.classList.add('show');
            return;
        } else {
            if (noResults) noResults.classList.remove('show');
        }
    }

    renderNextBatch();
}

function renderNextBatch() {
    const grid = document.getElementById('supplementsGrid');
    const scrollLoader = document.getElementById('scrollLoader');
    if (!grid || currentRenderIndex >= currentFilteredSupplements.length) {
        if (scrollLoader) scrollLoader.style.display = 'none';
        return;
    }

    const arrowIcon = currentLang === 'ar' ? 'fa-arrow-left' : 'fa-arrow-right';
    const nextBatch = currentFilteredSupplements.slice(currentRenderIndex, currentRenderIndex + BATCH_SIZE);
    currentRenderIndex += nextBatch.length;

    const batchHtml = nextBatch.map(supp => buildCardHtml(supp, arrowIcon)).join('');
    grid.insertAdjacentHTML('beforeend', batchHtml);

    if (scrollLoader) {
        scrollLoader.style.display = (currentRenderIndex < currentFilteredSupplements.length) ? 'block' : 'none';
    }
}

function initScrollObserver() {
    const sentinel = document.getElementById('infiniteScrollSentinel');
    if (!sentinel) return;

    if (scrollObserver) scrollObserver.disconnect();

    scrollObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            if (currentRenderIndex < currentFilteredSupplements.length) {
                renderNextBatch();
            }
        }
    }, { rootMargin: '400px' });

    scrollObserver.observe(sentinel);
}

// Details Modal Logic
// ==========================================================================
// Supplement modal: opens in place, keeps the exact scroll position, and puts
// #<slug> in the URL so the back button closes it and the link can be shared.
// ==========================================================================
let modalSuppId = null;
let modalScrollY = 0;
let modalReturnFocus = null;
let copyResetTimer = null;

function supplementBySlug(hash) {
    let slug = '';
    try { slug = decodeURIComponent(String(hash || '').replace(/^#/, '')); } catch (e) { return null; }
    return slug ? (supplementsData.find(s => s.slug === slug) || null) : null;
}

function supplementPagePath(supp) {
    if (!(window.SUPP_PAGES || {})[supp.slug]) return null;
    return currentLang === 'ar' ? `/supplements/${supp.slug}.html` : `/${currentLang}/supplements/${supp.slug}.html`;
}

// Direct link to share: the supplement's own indexable page, else the guide with #slug
function supplementUrl(supp) {
    const page = supplementPagePath(supp);
    return page ? 'https://wibohealth.com' + page : 'https://wibohealth.com/supplements.html#' + encodeURIComponent(supp.slug);
}

// Same pick as the generated pages: same group first, then same category; vetted records before the rest
function relatedSupplements(supp, limit = 4) {
    const group = supp.groupLabel && supp.groupLabel.ar;
    const vetted = r => (r.references || []).length > 0;
    const others = supplementsData.filter(r => r.id !== supp.id);
    const picked = [];
    const add = list => list.forEach(r => { if (!picked.includes(r)) picked.push(r); });
    if (group) add(others.filter(r => vetted(r) && r.groupLabel && r.groupLabel.ar === group));
    add(others.filter(r => vetted(r) && r.category === supp.category));
    add(others.filter(r => r.category === supp.category));
    return picked.slice(0, limit);
}

function supplementDisplayName(supp) {
    if (currentLang === 'nl') return supp.nameNl || supp.englishName || supp.name;
    if (currentLang === 'en') return supp.englishName || supp.name;
    return supp.name;
}

// the card data is the slim index; the full record (dosage, warnings, interactions, references) is fetched
// the first time a reader opens a supplement or the comparison
function openModal(id, opts = {}) {
    return ensureFullSupplements().then(() => openModalNow(id, opts));
}

function openModalNow(id, opts = {}) {
    const supp = supplementsData.find(s => s.id === id);
    if (!supp) return;
    const modal = document.getElementById('supplementModal');
    const wasOpen = modal.classList.contains('active');
    if (!wasOpen && !opts.fromHistory) modalReturnFocus = document.activeElement;
    modalSuppId = supp.id;
    renderSupplementModal(supp);

    const hash = '#' + encodeURIComponent(supp.slug);
    if (!wasOpen) {
        modalScrollY = window.scrollY;
        // Push before locking the body so the list entry keeps the real scroll position
        if (!opts.fromHistory && !(history.state && history.state.suppModal)) {
            history.pushState({ suppModal: true }, '', hash);
        }
        document.body.style.top = `-${modalScrollY}px`;
        document.body.classList.add('supp-modal-open');
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
    } else if (!opts.fromHistory && location.hash !== hash) {
        history.replaceState({ suppModal: true }, '', hash);
    }
    modal.scrollTop = 0;
    document.querySelector('#supplementModal .modal-body').scrollTop = 0;
    document.getElementById('supplementClose').focus({ preventScroll: true });
}

function renderSupplementModal(supp) {
    document.getElementById('modalIcon').textContent = supp.icon || '💊';

    if (currentLang === 'ar') {
        document.getElementById('modalTitle').textContent = supp.name;
        document.getElementById('modalSubtitle').textContent = supp.englishName || '';
    } else if (currentLang === 'nl') {
        const titleNl = supp.nameNl || supp.englishName || supp.name;
        document.getElementById('modalTitle').textContent = titleNl;
        document.getElementById('modalSubtitle').textContent = (supp.englishName && supp.englishName !== titleNl) ? supp.englishName : '';
    } else {
        document.getElementById('modalTitle').textContent = supp.englishName || supp.name;
        document.getElementById('modalSubtitle').textContent = '';
    }
    const closeBtn = document.getElementById('supplementClose');
    closeBtn.setAttribute('aria-label', t('modal_close'));
    closeBtn.title = t('modal_close');
    resetCopyButton();

    const benefitsList = (currentLang === 'nl' && supp.benefitsNl) ? supp.benefitsNl :
                         (currentLang === 'en' && supp.benefitsEn) ? supp.benefitsEn :
                         (supp.benefits || []);

    const recVal = (currentLang === 'nl' && supp.dosageNl?.recommended) ? supp.dosageNl.recommended :
                   (currentLang === 'en' && supp.dosageEn?.recommended) ? supp.dosageEn.recommended :
                   smartClinicalTranslate(supp.dosage?.recommended || '-', currentLang);

    const timVal = (currentLang === 'nl' && supp.dosageNl?.timing) ? supp.dosageNl.timing :
                   (currentLang === 'en' && supp.dosageEn?.timing) ? supp.dosageEn.timing :
                   smartClinicalTranslate(supp.dosage?.timing || '-', currentLang);

    const freqVal = (currentLang === 'nl' && supp.dosageNl?.frequency) ? supp.dosageNl.frequency :
                    (currentLang === 'en' && supp.dosageEn?.frequency) ? supp.dosageEn.frequency :
                    smartClinicalTranslate(supp.dosage?.frequency || '-', currentLang);

    const warningsList = (currentLang === 'nl' && supp.warningsNl) ? supp.warningsNl :
                         (currentLang === 'en' && supp.warningsEn) ? supp.warningsEn :
                         (supp.warnings || []);

    const interVal = (currentLang === 'nl' && supp.interactionsNl) ? supp.interactionsNl :
                     (currentLang === 'en' && supp.interactionsEn) ? supp.interactionsEn :
                     smartClinicalTranslate(supp.interactions || '-', currentLang);

    const sourcesVal = (currentLang === 'nl' && supp.naturalSourcesNl) ? supp.naturalSourcesNl :
                       (currentLang === 'en' && supp.naturalSourcesEn) ? supp.naturalSourcesEn :
                       smartClinicalTranslate(supp.naturalSources || '-', currentLang);

    // merged records list several interactions separated by " • ": show them as a list
    const interParts = String(interVal).split(' • ').filter(Boolean);
    const interHtml = interParts.length > 1
        ? `<ul>${interParts.map(x => `<li>${x}</li>`).join('')}</ul>`
        : `<p style="color: var(--text-dark);">${interVal}</p>`;

    const related = relatedSupplements(supp);
    const formsVal = (currentLang === 'nl' && supp.formsNl) ? supp.formsNl :
                     (currentLang === 'en' && supp.formsEn) ? supp.formsEn : (supp.forms || '');

    document.getElementById('modalBody').innerHTML = `
        <div class="info-section span-2">
            <h4><i class="fas fa-star"></i> ${t('modal_benefits')}</h4>
            <ul>
                ${benefitsList.map(b => `<li>${b}</li>`).join('')}
            </ul>
        </div>

        <div class="info-section">
            <h4><i class="fas fa-prescription-bottle"></i> ${t('modal_dosage')}</h4>
            <div class="dosage-box">
                <div class="dosage-item">
                    <span class="dosage-label">${t('modal_dosage_rec')}</span>
                    <span class="dosage-value">${recVal}</span>
                </div>
                <div class="dosage-item">
                    <span class="dosage-label">${t('modal_dosage_timing')}</span>
                    <span class="dosage-value">${timVal}</span>
                </div>
                <div class="dosage-item">
                    <span class="dosage-label">${t('modal_dosage_freq')}</span>
                    <span class="dosage-value">${freqVal}</span>
                </div>
            </div>
        </div>

        ${formsVal ? `
        <div class="info-section">
            <h4><i class="fas fa-capsules"></i> ${t('modal_forms')}</h4>
            <p style="color: var(--text-dark);">${formsVal}</p>
        </div>` : ''}

        <div class="info-section">
            <div class="warning-box">
                <h5><i class="fas fa-triangle-exclamation"></i> ${t('modal_warnings')}</h5>
                <ul>
                    ${warningsList.map(w => `<li>${w}</li>`).join('')}
                </ul>
            </div>
        </div>

        <div class="info-section">
            <h4><i class="fas fa-pills"></i> ${t('modal_interactions')}</h4>
            ${interHtml}
        </div>

        <div class="info-section${formsVal ? ' span-2' : ''}">
            <h4><i class="fas fa-leaf"></i> ${t('modal_sources')}</h4>
            <p style="color: var(--text-dark);">${sourcesVal}</p>
        </div>

        ${related.length ? `
        <div class="info-section span-2">
            <h4><i class="fas fa-layer-group"></i> ${t('modal_related')}</h4>
            <div class="related-list">${related.map(r => `
                <button type="button" class="related-item" onclick="openModal(${r.id})">
                    <span class="related-icon" aria-hidden="true">${r.icon || '💊'}</span>
                    <span class="related-text">
                        <span class="related-name">${supplementDisplayName(r)}</span>
                        <span class="related-group">${(r.groupLabel && r.groupLabel[currentLang]) || getCategoryName(r.category)}</span>
                    </span>
                </button>`).join('')}
            </div>
        </div>` : ''}
        ${(supp.references || []).length ? `
        <div class="info-section span-2">
            <h4><i class="fas fa-book-medical"></i> ${t('modal_refs_title')}</h4>
            <ol class="ref-list">${supp.references.map(r => `<li>${r}</li>`).join('')}</ol>
        </div>` : ''}
        <div class="refs-strip">${t('modal_refs')}</div>
        <div class="medical-disclaimer">${t('modal_disclaimer')}</div>
    `;
}

function hideModal() {
    const modal = document.getElementById('supplementModal');
    if (!modal || !modal.classList.contains('active')) return;
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('supp-modal-open');
    document.body.style.top = '';
    window.scrollTo({ top: modalScrollY, left: 0, behavior: 'instant' });
    modalSuppId = null;
    document.getElementById('supplementModalStatus').textContent = '';
    if (modalReturnFocus && document.body.contains(modalReturnFocus)) modalReturnFocus.focus({ preventScroll: true });
    modalReturnFocus = null;
}

function closeModal() {
    const modal = document.getElementById('supplementModal');
    if (!modal || !modal.classList.contains('active')) return;
    // Drop the history entry added on open; popstate then hides the modal
    if (history.state && history.state.suppModal) {
        history.back();
    } else {
        hideModal();
        if (location.hash) history.replaceState(null, '', location.pathname + location.search);
    }
}

// Opened from a shared link (supplements.html#ashwagandha): put the plain list entry
// under the modal entry, so closing or pressing back shows the list instead of leaving the site.
function openModalFromLink(supp) {
    history.replaceState(null, '', location.pathname + location.search);
    openModal(supp.id);
}

window.addEventListener('popstate', function() {
    const supp = supplementBySlug(location.hash);
    if (!supp) { hideModal(); return; }
    if (history.state && history.state.suppModal) openModal(supp.id, { fromHistory: true });
    else openModalFromLink(supp);   // hash typed or pasted into the address bar
});

// A reload keeps the history state; clear it so closing never leaves the page
if (history.state && history.state.suppModal) history.replaceState(null, '');

function resetCopyButton() {
    clearTimeout(copyResetTimer);
    const btn = document.getElementById('supplementShare');
    btn.classList.remove('copied');
    btn.setAttribute('aria-label', t('modal_copy_link'));
    btn.title = t('modal_copy_link');
    document.getElementById('supplementShareText').textContent = '';
    btn.querySelector('i').className = 'fas fa-link';
}

function legacyCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    let ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    ta.remove();
    return ok;
}

function copySupplementLink() {
    const supp = supplementsData.find(s => s.id === modalSuppId);
    if (!supp) return;
    const url = supplementUrl(supp);
    const done = () => {
        const btn = document.getElementById('supplementShare');
        btn.classList.add('copied');
        btn.querySelector('i').className = 'fas fa-check';
        document.getElementById('supplementShareText').textContent = t('modal_link_copied');
        document.getElementById('supplementModalStatus').textContent = t('modal_link_copied');
        clearTimeout(copyResetTimer);
        copyResetTimer = setTimeout(resetCopyButton, 2200);
    };
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(url).then(done, () => { if (legacyCopy(url)) done(); });
    } else if (legacyCopy(url)) {
        done();
    }
}

document.getElementById('supplementModal').addEventListener('click', function(e) {
    if (e.target === this) closeModal();
});

// Search Input Debouncing
let searchDebounceTimer = null;
document.getElementById('searchInput').addEventListener('input', function(e) {
    const val = e.target.value;
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => {
        searchTerm = val;
        displaySupplements(true);
    }, 180);
});

// Compare Functions
window.toggleSupplementCompare = function(id, checkbox) {
    id = parseInt(id);
    if (checkbox.checked) {
        if (window.selectedSupplements.size >= 5) {
            checkbox.checked = false;
            alert(currentLang === 'nl' ? 'U kunt maximaal 5 supplementen vergelijken' : (currentLang === 'en' ? 'You can compare up to 5 supplements' : 'يمكنك مقارنة 5 مكملات كحد أقصى'));
            return;
        }
        window.selectedSupplements.add(id);
    } else {
        window.selectedSupplements.delete(id);
    }
    updateCompareButton();
};

function updateCompareButton() {
    const compareBtn = document.getElementById('compareFloatBtn');
    const compareCount = document.getElementById('compareCount');
    if (!compareBtn || !compareCount) return;

    const count = window.selectedSupplements.size;
    if (count >= 2) {
        compareBtn.classList.remove('hidden');
        compareCount.textContent = count;
    } else {
        compareBtn.classList.add('hidden');
    }
}

function openCompareModal() {
    return ensureFullSupplements().then(openCompareModalNow);
}

function openCompareModalNow() {
    if (window.selectedSupplements.size < 2) {
        alert(currentLang === 'nl' ? 'Selecteer minimaal 2 supplementen' : (currentLang === 'en' ? 'Please select at least 2 supplements' : 'اختر مكملين على الأقل'));
        return;
    }

    const selectedIds = Array.from(window.selectedSupplements);
    const supplements = selectedIds.map(id => supplementsData.find(s => s.id === id)).filter(Boolean);

    displayComparisonTable(supplements);
    document.getElementById('compareModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeCompareModal() {
    const compareModal = document.getElementById('compareModal');
    if (compareModal) compareModal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function displayComparisonTable(supplements) {
    const body = document.getElementById('compareModalBody');
    const isAr = currentLang === 'ar';
    const isNl = currentLang === 'nl';
    const isEn = currentLang === 'en';
    
    const lbl = {
        crit: isAr ? 'المعيار' : (isNl ? 'Criterium' : 'Criterion'),
        cat: isAr ? 'التصنيف' : (isNl ? 'Categorie' : 'Category'),
        dos: isAr ? 'الجرعة' : (isNl ? 'Dosering' : 'Dosage'),
        tim: isAr ? 'التوقيت' : (isNl ? 'Innamemoment' : 'Timing'),
        warn: isAr ? 'التحذيرات' : (isNl ? 'Waarschuwingen' : 'Warnings')
    };

    body.innerHTML = `
        <div style="overflow-x: auto;">
            <table class="comparison-table">
                <thead>
                    <tr>
                        <th>${lbl.crit}</th>
                        ${supplements.map(s => {
                            let suppTitle = s.name;
                            if (isNl) suppTitle = s.nameNl || s.englishName || s.name;
                            else if (isEn) suppTitle = s.englishName || s.name;

                            return `
                            <th>
                                <div style="font-size: 28px; margin-bottom: 5px;">${s.icon || '💊'}</div>
                                <div style="font-weight: 800; font-size: 15px;">${suppTitle}</div>
                            </th>
                            `;
                        }).join('')}
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><i class="fas fa-tag"></i> ${lbl.cat}</td>
                        ${supplements.map(s => `<td><span class="supplement-category">${getCategoryName(s.category)}</span></td>`).join('')}
                    </tr>
                    <tr>
                        <td><i class="fas fa-prescription-bottle"></i> ${lbl.dos}</td>
                        ${supplements.map(s => {
                            const recVal = (isNl && s.dosageNl?.recommended) ? s.dosageNl.recommended :
                                           (isEn && s.dosageEn?.recommended) ? s.dosageEn.recommended :
                                           (s.dosage?.recommended || '-');
                            return `<td><strong>${recVal}</strong></td>`;
                        }).join('')}
                    </tr>
                    <tr>
                        <td><i class="fas fa-clock"></i> ${lbl.tim}</td>
                        ${supplements.map(s => {
                            const timVal = (isNl && s.dosageNl?.timing) ? s.dosageNl.timing :
                                           (isEn && s.dosageEn?.timing) ? s.dosageEn.timing :
                                           (s.dosage?.timing || '-');
                            return `<td>${timVal}</td>`;
                        }).join('')}
                    </tr>
                    <tr>
                        <td><i class="fas fa-triangle-exclamation"></i> ${lbl.warn}</td>
                        ${supplements.map(s => {
                            const warnList = (isNl && s.warningsNl && s.warningsNl.length > 0) ? s.warningsNl :
                                             (isEn && s.warningsEn && s.warningsEn.length > 0) ? s.warningsEn :
                                             (s.warnings || []);
                            return `<td><ul style="padding-${isAr ? 'right' : 'left'}: 16px; margin: 0; font-size: 13px; line-height: 1.5;">${warnList.slice(0, 2).map(w => `<li>${w}</li>`).join('')}</ul></td>`;
                        }).join('')}
                    </tr>
                </tbody>
            </table>
        </div>
    `;
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        if (modalSuppId !== null) closeModal();
        else closeCompareModal();
    }
});

if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

// Initialize on DOM Ready
window.addEventListener('DOMContentLoaded', async function() {
    window.scrollTo(0, 0);
    supplementsData = await loadSupplementsJson(SUPP_SRC.index || '/data/supplements-index.json').then(decodeIndex).catch(() => []);
    const searchInput = document.getElementById('searchInput');
    if (searchInput) searchInput.value = '';
    searchTerm = '';
    
    initializeTheme();
    initScrollObserver();
    changeLanguage(currentLang);

    const linkedSupp = supplementBySlug(location.hash);
    if (linkedSupp) openModalFromLink(linkedSupp);
});
