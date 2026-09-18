/**
 * WiBo Health - Unified Translations & Smart Auto-Language Engine
 * Version: 7.0.0 - Auto-Detect Phone Language (Dutch/Foreign -> English, Arabic -> Arabic)
 */

// ============================================
// 1. الكشف التلقائي الذكي عن لغة هاتف الزائر
// ============================================
function detectInitialLanguage() {
    // 1. إذا كان الزائر قد اختار لغة بنفسه سابقاً، نحترم اختياره فوراً
    const saved = localStorage.getItem('preferred_language');
    if (saved && (saved === 'ar' || saved === 'en')) {
        return saved;
    }

    // 2. إذا كانت أول زيارة، نفحص لغة الهاتف / المتصفح
    const browserLang = (navigator.language || navigator.userLanguage || '').toLowerCase();

    // إذا كانت لغة الهاتف عربية
    if (browserLang.startsWith('ar')) {
        return 'ar';
    }

    // إذا كان هاتف الزائر هولندياً (nl) أو إنجليزياً أو أي لغة أجنبية، يفتح إنجليزي فوراً وبشكل كامل!
    return 'en';
}

// ============================================
// 2. قاموس النصوص والترجمات
// ============================================
const translations = {
    // Header & Logo
    tagline: {
        ar: 'دليلك الصحي الشامل للتغذية السليمة',
        en: 'Your Complete Guide to Proper Nutrition'
    },
    
    // Theme Toggle
    toggleTheme: {
        ar: 'تغيير المظهر',
        en: 'Toggle Dark Mode'
    },
    
    // Navigation
    nav: {
        home: { ar: 'الرئيسية', en: 'Home' },
        foods: { ar: 'دليل الأطعمة', en: 'Foods Guide' },
        calculators: { ar: 'الحاسبات', en: 'Calculators' },
        calorieTracker: { ar: 'متتبع السعرات', en: 'Calorie Tracker' },
        recipes: { ar: 'الوصفات', en: 'Recipes' },
        articles: { ar: 'المقالات', en: 'Articles' },
        supplements: { ar: 'المكملات الغذائية', en: 'Supplements' },
        doctor: { ar: 'د. وسيم حبيب', en: 'Dr. Wassim Habib' },
        freeDiet: { ar: 'دايت مجاني 🎁', en: 'Free Diet Plan 🎁' },
        about: { ar: 'من نحن', en: 'About Us' },
        contact: { ar: 'اتصل بنا', en: 'Contact Us' }
    },
    
    // Homepage Hero
    hero: {
        title: {
            ar: 'دليلك الشامل للتغذية الصحية',
            en: 'Your Complete Guide to Healthy Nutrition'
        },
        subtitle: {
            ar: '1051 عنصر غذائي | 442 مكمل | 110 وصفة | 19 مقالة | 5 حاسبات صحية',
            en: '1051 Food Items | 442 Supplements | 110 Recipes | 19 Articles | 5 Health Calculators'
        },
        cta: {
            ar: 'استكشف الآن',
            en: 'Explore Now'
        }
    },
    
    // Features Section
    features: {
        title: {
            ar: 'ماذا يقدم WiBo Health؟',
            en: 'What Does WiBo Health Offer?'
        },
        foodDatabase: {
            title: { ar: 'قاعدة بيانات ضخمة للأطعمة', en: 'Massive Food Database' },
            desc: { ar: '1051 عنصر غذائي مع معلومات تفصيلية كاملة', en: '1051 food items with complete detailed information' }
        },
        calculators: {
            title: { ar: 'حاسبات صحية دقيقة', en: 'Accurate Health Calculators' },
            desc: { ar: '5 حاسبات مجانية: BMI، BMR، السعرات، الماء، الدهون', en: '5 free calculators: BMI, BMR, Calories, Water, Body Fat' }
        },
        recipes: {
            title: { ar: '110 وصفة صحية', en: '110 Healthy Recipes' },
            desc: { ar: 'وصفات دايت وحلويات صحية مع القيم الغذائية', en: 'Diet recipes and healthy desserts with nutritional values' }
        },
        supplements: {
            title: { ar: 'دليل المكملات الغذائية', en: 'Supplements Guide' },
            desc: { ar: '442 مكمل غذائي مع الفوائد والجرعات والتحذيرات', en: '442 supplements with benefits, dosages, and warnings' }
        },
        articles: {
            title: { ar: '19 مقالة تغذوية احترافية', en: '19 Professional Nutrition Articles' },
            desc: { ar: 'مقالات متخصصة عن السكري، القولون، القلب، والمزيد', en: 'Specialized articles about diabetes, IBS, heart health, and more' }
        },
        tracker: {
            title: { ar: 'متتبع سعرات احترافي', en: 'Professional Calorie Tracker' },
            desc: { ar: 'تتبع سعراتك اليومية مع رسوم بيانية تفاعلية', en: 'Track your daily calories with interactive charts' }
        }
    },
    
    // Stats Section
    stats: {
        foods: { ar: 'عنصر غذائي', en: 'Food Items' },
        supplements: { ar: 'مكمل غذائي', en: 'Supplements' },
        recipes: { ar: 'وصفة صحية', en: 'Healthy Recipes' },
        articles: { ar: 'مقالة تغذوية', en: 'Nutrition Articles' }
    },
    
    // Footer
    footer: {
        about: { ar: 'من نحن', en: 'About Us' },
        aboutDesc: { ar: 'منصتك الصحية الشاملة للتغذية السليمة والحياة الصحية', en: 'Your comprehensive health platform for proper nutrition and healthy living' },
        quickLinks: { ar: 'روابط سريعة', en: 'Quick Links' },
        contact: { ar: 'اتصل بنا', en: 'Contact Us' },
        privacy: { ar: 'سياسة الخصوصية', en: 'Privacy Policy' },
        terms: { ar: 'الشروط والأحكام', en: 'Terms & Conditions' },
        disclaimer: { ar: 'إخلاء المسؤولية', en: 'Disclaimer' },
        copyright: { ar: '© 2026 WiBo Health. جميع الحقوق محفوظة.', en: '© 2026 WiBo Health. All rights reserved.' }
    }
};

// ============================================
// 3. محرك إدارة وتطبيق اللغات الذكي
// ============================================
const LanguageManager = {
    get currentLang() {
        let lang = localStorage.getItem('preferred_language');
        if (!lang) {
            lang = detectInitialLanguage();
            localStorage.setItem('preferred_language', lang);
        }
        return lang;
    },

    set currentLang(lang) {
        localStorage.setItem('preferred_language', lang);
    },

    init() {
        const lang = this.currentLang;
        this.applyLanguage(lang, false);
    },

    applyLanguage(lang, triggerEvent = true) {
        this.currentLang = lang;

        // تحديث اتجاه الصفحة ولغتها (يمين لليسار للعربي، ويسار لليمين للإنجليزي)
        document.documentElement.setAttribute('lang', lang);
        document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

        // ترجمة العناصر الحاملة للخاصية data-i18n
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            const translatedText = t(key, lang);
            if (translatedText && translatedText !== key) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = translatedText;
                } else {
                    el.textContent = translatedText;
                }
            }
        });

        // ترجمة الـ Placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            const translatedText = t(key, lang);
            if (translatedText && translatedText !== key) {
                el.placeholder = translatedText;
            }
        });

        // تحديث مظهر أزرار الأعلام
        document.querySelectorAll('.lang-btn, [data-lang-toggle]').forEach(btn => {
            const btnLang = btn.getAttribute('data-lang-toggle');
            if (btnLang === lang) {
                btn.classList.add('active');
                btn.style.opacity = '1';
                btn.style.fontWeight = 'bold';
            } else {
                btn.classList.remove('active');
                btn.style.opacity = '0.6';
                btn.style.fontWeight = 'normal';
            }
        });

        // إطلاق حدث عام لتحديث كروت الأطعمة فوراً باللغة الجديدة
        if (triggerEvent) {
            window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
        }
    },

    changeLanguage(lang) {
        this.applyLanguage(lang, true);
    }
};

// الدالة العامة لجلب النصوص
function t(key, lang = null) {
    if (!lang) {
        lang = LanguageManager.currentLang;
    }
    
    const keys = key.split('.');
    let value = translations;
    
    for (const k of keys) {
        if (!value || value[k] === undefined) {
            value = null;
            break;
        }
        value = value[k];
    }
    
    if (value && typeof value === 'object') {
        return value[lang] || value['ar'] || key;
    }
    
    return value || key;
}

// دالة التحويل العامة التي تستدعيها الأزرار
function changeLanguage(lang) {
    LanguageManager.changeLanguage(lang);
}

// ضبط اتجاه الصفحة فوراً في أول لحظة لمنع وميض الشاشة
(function applyImmediateDirection() {
    const immediateLang = LanguageManager.currentLang;
    document.documentElement.setAttribute('lang', immediateLang);
    document.documentElement.setAttribute('dir', immediateLang === 'ar' ? 'rtl' : 'ltr');
})();

// توافق كامل مع الكائنات القديمة
window.LanguageSwitcher = LanguageManager;
window.UnifiedLanguageSystem = LanguageManager;
window.LanguageManager = LanguageManager;
window.changeLanguage = changeLanguage;
window.t = t;

// التهيئة التلقائية عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', () => {
    LanguageManager.init();
});

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { translations, t, LanguageManager, changeLanguage };
}