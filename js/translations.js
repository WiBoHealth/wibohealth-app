/**
 * WiBo Health - Translations Database
 * All text content in Arabic and English
 * Version: 5.0.0
 */

const translations = {
    // Header & Logo
    tagline: {
        ar: 'دليلك الصحي الشامل للتغذية السليمة',
        en: 'Your Complete Guide to Proper Nutrition'
    },
    
    // Language Switcher
    switchToEnglish: {
        ar: 'Switch to English',
        en: 'التبديل للعربية'
    },
    
    // Theme Toggle
    toggleTheme: {
        ar: 'تغيير المظهر',
        en: 'Toggle Dark Mode'
    },
    
    // Navigation
    nav: {
        foods: {
            ar: 'دليل الأطعمة',
            en: 'Foods Guide'
        },
        calculators: {
            ar: 'الحاسبات',
            en: 'Calculators'
        },
        calorieTracker: {
            ar: 'متتبع السعرات',
            en: 'Calorie Tracker'
        },
        recipes: {
            ar: 'الوصفات',
            en: 'Recipes'
        },
        articles: {
            ar: 'المقالات',
            en: 'Articles'
        },
        supplements: {
            ar: 'المكملات الغذائية',
            en: 'Supplements'
        },
        doctor: {
            ar: 'د. وسيم حبيب',
            en: 'Drs. Wassim Habib'
        },
        freeDiet: {
            ar: 'دايت مجاني 🎁',
            en: 'Free Diet Plan 🎁'
        }
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
            title: {
                ar: 'قاعدة بيانات ضخمة للأطعمة',
                en: 'Massive Food Database'
            },
            desc: {
                ar: '1051 عنصر غذائي مع معلومات تفصيلية كاملة',
                en: '1051 food items with complete detailed information'
            }
        },
        calculators: {
            title: {
                ar: 'حاسبات صحية دقيقة',
                en: 'Accurate Health Calculators'
            },
            desc: {
                ar: '5 حاسبات مجانية: BMI، BMR، السعرات، الماء، الدهون',
                en: '5 free calculators: BMI, BMR, Calories, Water, Body Fat'
            }
        },
        recipes: {
            title: {
                ar: '110 وصفة صحية',
                en: '110 Healthy Recipes'
            },
            desc: {
                ar: 'وصفات دايت وحلويات صحية مع القيم الغذائية',
                en: 'Diet recipes and healthy desserts with nutritional values'
            }
        },
        supplements: {
            title: {
                ar: 'دليل المكملات الغذائية',
                en: 'Supplements Guide'
            },
            desc: {
                ar: '442 مكمل غذائي مع الفوائد والجرعات والتحذيرات',
                en: '442 supplements with benefits, dosages, and warnings'
            }
        },
        articles: {
            title: {
                ar: '19 مقالة تغذوية احترافية',
                en: '19 Professional Nutrition Articles'
            },
            desc: {
                ar: 'مقالات متخصصة عن السكري، القولون، القلب، والمزيد',
                en: 'Specialized articles about diabetes, IBS, heart health, and more'
            }
        },
        tracker: {
            title: {
                ar: 'متتبع سعرات احترافي',
                en: 'Professional Calorie Tracker'
            },
            desc: {
                ar: 'تتبع سعراتك اليومية مع رسوم بيانية تفاعلية',
                en: 'Track your daily calories with interactive charts'
            }
        }
    },
    
    // Stats Section
    stats: {
        foods: {
            ar: 'عنصر غذائي',
            en: 'Food Items'
        },
        supplements: {
            ar: 'مكمل غذائي',
            en: 'Supplements'
        },
        recipes: {
            ar: 'وصفة صحية',
            en: 'Healthy Recipes'
        },
        articles: {
            ar: 'مقالة تغذوية',
            en: 'Nutrition Articles'
        }
    },
    
    // Footer
    footer: {
        about: {
            ar: 'عن WiBo Health',
            en: 'About WiBo Health'
        },
        aboutDesc: {
            ar: 'منصتك الصحية الشاملة للتغذية السليمة والحياة الصحية',
            en: 'Your comprehensive health platform for proper nutrition and healthy living'
        },
        quickLinks: {
            ar: 'روابط سريعة',
            en: 'Quick Links'
        },
        contact: {
            ar: 'اتصل بنا',
            en: 'Contact Us'
        },
        privacy: {
            ar: 'سياسة الخصوصية',
            en: 'Privacy Policy'
        },
        terms: {
            ar: 'الشروط والأحكام',
            en: 'Terms & Conditions'
        },
        disclaimer: {
            ar: 'إخلاء المسؤولية',
            en: 'Disclaimer'
        },
        copyright: {
            ar: '© 2025 WiBo Health. جميع الحقوق محفوظة.',
            en: '© 2025 WiBo Health. All rights reserved.'
        }
    }
};

// Helper function to get translation
function t(key, lang = null) {
    if (!lang) {
        lang = window.LanguageSwitcher ? window.LanguageSwitcher.currentLang : 'ar';
    }
    
    // Navigate through nested keys (e.g., 'nav.foods')
    const keys = key.split('.');
    let value = translations;
    
    for (const k of keys) {
        value = value[k];
        if (!value) return key; // Return key if not found
    }
    
    return value[lang] || value['ar'] || key;
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { translations, t };
}
