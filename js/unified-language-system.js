/**
 * WiBo Health - Unified Language System
 * Single URL, Dual Language Support
 * Version: 5.0.0 - Revolutionary Update
 * 
 * Features:
 * - Translates ALL content (UI + Data)
 * - Uses existing translations from data.js, recipes-data.js
 * - No URL changes
 * - Instant language switching
 * - localStorage persistence
 */

(function() {
    'use strict';

    // ==========================================
    // 1. TRANSLATIONS DATABASE
    // ==========================================
    
    const UI_TRANSLATIONS = {
        // Common
        home: { ar: 'الرئيسية', en: 'Home' },
        back: { ar: 'رجوع', en: 'Back' },
        search: { ar: 'بحث', en: 'Search' },
        filter: { ar: 'تصفية', en: 'Filter' },
        save: { ar: 'حفظ', en: 'Save' },
        cancel: { ar: 'إلغاء', en: 'Cancel' },
        close: { ar: 'إغلاق', en: 'Close' },
        loading: { ar: 'جاري التحميل...', en: 'Loading...' },
        
        // Navigation
        nav_foods: { ar: 'دليل الأطعمة', en: 'Foods Guide' },
        nav_calculators: { ar: 'الحاسبات', en: 'Calculators' },
        nav_calorieTracker: { ar: 'متتبع السعرات', en: 'Calorie Tracker' },
        nav_recipes: { ar: 'الوصفات', en: 'Recipes' },
        nav_articles: { ar: 'المقالات', en: 'Articles' },
        nav_supplements: { ar: 'المكملات الغذائية', en: 'Supplements' },
        nav_doctor: { ar: 'د. وسيم حبيب', en: 'Drs. Wassim Habib' },
        nav_freeDiet: { ar: 'دايت مجاني 🎁', en: 'Free Diet Plan 🎁' },
        
        // Foods Page
        foods_title: { ar: 'دليل الأطعمة الشامل', en: 'Complete Foods Guide' },
        foods_subtitle: { ar: '1051 عنصر غذائي مع معلومات تفصيلية كاملة', en: '1051 food items with complete detailed information' },
        foods_searchPlaceholder: { ar: 'ابحث عن طعام...', en: 'Search for food...' },
        foods_calories: { ar: 'سعرات حرارية', en: 'Calories' },
        foods_protein: { ar: 'بروتين', en: 'Protein' },
        foods_carbs: { ar: 'كربوهيدرات', en: 'Carbs' },
        foods_fats: { ar: 'دهون', en: 'Fats' },
        foods_fiber: { ar: 'ألياف', en: 'Fiber' },
        foods_category: { ar: 'الفئة', en: 'Category' },
        foods_gi: { ar: 'مؤشر جلايسيميك', en: 'Glycemic Index' },
        foods_ii: { ar: 'مؤشر أنسولين', en: 'Insulin Index' },
        foods_gi_short: { ar: 'GI - جلايسيميك', en: 'GI - Glycemic' },
        foods_ii_short: { ar: 'II - إنسولين', en: 'II - Insulin' },
        foods_low: { ar: 'منخفض', en: 'Low' },
        foods_medium: { ar: 'متوسط', en: 'Medium' },
        foods_high: { ar: 'مرتفع', en: 'High' },
        foods_kcal: { ar: 'كيلو كالوري', en: 'kcal' },
        foods_gram: { ar: 'جم', en: 'g' },
        foods_noResults: { ar: 'لم يتم العثور على نتائج', en: 'No results found' },
        foods_tryAgain: { ar: 'جرب البحث بكلمة أخرى', en: 'Try searching with different keywords' },
        foods_clearSearch: { ar: 'مسح البحث وعرض العينات', en: 'Clear search and show samples' },
        foods_showingResults: { ar: 'يتم عرض أول 50 نتيجة من', en: 'Showing first 50 results of' },
        foods_refineSearch: { ar: 'حدد كلمات البحث للحصول على نتائج أدق', en: 'Refine your search for more specific results' },
        
        // Supplements Page
        supplements_title: { ar: 'دليل المكملات الغذائية', en: 'Dietary Supplements Guide' },
        supplements_subtitle: { ar: '426 مكمل غذائي مع الفوائد والجرعات والتحذيرات', en: '426 supplements with benefits, dosages, and warnings' },
        supplementsLabel: { ar: 'مكمل غذائي', en: 'Supplements' },
        categoriesLabel: { ar: 'تصنيفات رئيسية', en: 'Main Categories' },
        reliableLabel: { ar: 'معلومات موثوقة', en: 'Reliable Information' },
        aboutLabel: { ar: 'نبذة', en: 'About' },
        benefitsLabel: { ar: 'الفوائد', en: 'Benefits' },
        dosageLabel: { ar: 'الجرعة الموصى بها', en: 'Recommended Dosage' },
        warningsLabel: { ar: 'تحذيرات مهمة', en: 'Important Warnings' },
        interactionsLabel: { ar: 'التداخلات', en: 'Interactions' },
        naturalSourcesLabel: { ar: 'المصادر الطبيعية', en: 'Natural Sources' },
        switchLanguage: { ar: 'English', en: 'العربية' },
        
        // Recipes Page
        recipes_title: { ar: 'وصفات صحية', en: 'Healthy Recipes' },
        recipes_subtitle: { ar: '110 وصفة صحية مع القيم الغذائية الكاملة', en: '110 healthy recipes with complete nutritional values' },
        recipes_ingredients: { ar: 'المقادير', en: 'Ingredients' },
        recipes_instructions: { ar: 'طريقة التحضير', en: 'Instructions' },
        recipes_servings: { ar: 'حصة', en: 'serving' },
        recipes_cookTime: { ar: 'وقت التحضير', en: 'Cook Time' },
        
        // Calculators Page
        calculators_title: { ar: 'الحاسبات الصحية', en: 'Health Calculators' },
        calculators_bmi: { ar: 'حاسبة مؤشر كتلة الجسم', en: 'BMI Calculator' },
        calculators_bmr: { ar: 'حاسبة معدل الأيض الأساسي', en: 'BMR Calculator' },
        calculators_calories: { ar: 'حاسبة السعرات اليومية', en: 'Daily Calorie Calculator' },
        calculators_water: { ar: 'حاسبة احتياج الماء', en: 'Water Intake Calculator' },
        calculators_bodyFat: { ar: 'حاسبة نسبة الدهون', en: 'Body Fat Calculator' },
        calculators_calculate: { ar: 'احسب', en: 'Calculate' },
        calculators_result: { ar: 'النتيجة', en: 'Result' },
        
        // Articles Page
        articles_title: { ar: 'مقالات تغذوية احترافية', en: 'Professional Nutrition Articles' },
        articles_subtitle: { ar: '19 مقالة متخصصة عن التغذية والصحة', en: '19 specialized articles about nutrition and health' },
        articles_readMore: { ar: 'اقرأ المزيد', en: 'Read More' },
        articles_readTime: { ar: 'دقائق قراءة', en: 'min read' },
        
        // Footer
        footer_about: { ar: 'عن WiBo Health', en: 'About WiBo Health' },
        footer_aboutDesc: { ar: 'منصتك الصحية الشاملة للتغذية السليمة', en: 'Your comprehensive health platform' },
        footer_quickLinks: { ar: 'روابط سريعة', en: 'Quick Links' },
        footer_contact: { ar: 'اتصل بنا', en: 'Contact Us' },
        footer_privacy: { ar: 'سياسة الخصوصية', en: 'Privacy Policy' },
        footer_terms: { ar: 'الشروط والأحكام', en: 'Terms & Conditions' },
        footer_disclaimer: { ar: 'إخلاء المسؤولية', en: 'Disclaimer' },
        footer_copyright: { ar: '© 2025 WiBo Health. جميع الحقوق محفوظة.', en: '© 2025 WiBo Health. All rights reserved.' }
    };

    // ==========================================
    // 2. LANGUAGE MANAGER
    // ==========================================
    
    const UnifiedLanguageSystem = {
        currentLang: 'ar',
        
        // Get saved language
        getSavedLanguage() {
            return localStorage.getItem('wibohealth_language') || 'ar';
        },
        
        // Save language
        saveLanguage(lang) {
            localStorage.setItem('wibohealth_language', lang);
            this.currentLang = lang;
        },
        
        // Translate UI text
        t(key) {
            return UI_TRANSLATIONS[key] ? UI_TRANSLATIONS[key][this.currentLang] : key;
        },
        
        // Apply language to page
        applyLanguage(lang) {
            const html = document.documentElement;
            
            // Set HTML attributes
            html.setAttribute('lang', lang);
            html.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
            
            // Set font
            document.body.style.fontFamily = lang === 'ar' ? "'Cairo', sans-serif" : "'Inter', sans-serif";
            
            // Hide/Show language-specific elements
            document.querySelectorAll('[data-lang="ar"]').forEach(el => {
                el.style.display = lang === 'ar' ? '' : 'none';
            });
            
            document.querySelectorAll('[data-lang="en"]').forEach(el => {
                el.style.display = lang === 'en' ? '' : 'none';
            });
            
            // Translate elements with data-translate attribute
            document.querySelectorAll('[data-translate]').forEach(el => {
                const key = el.getAttribute('data-translate');
                const translation = this.t(key);
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = translation;
                } else {
                    el.textContent = translation;
                }
            });
            
            // Save and update buttons
            this.saveLanguage(lang);
            this.updateLanguageButtons();
            
            // Translate dynamic content (foods, recipes, etc.)
            this.translateDynamicContent(lang);
        },
        
        // Translate dynamic content
        translateDynamicContent(lang) {
            // Reload food cards with new language
            if (typeof window.loadFoodGrid === 'function') {
                window.loadFoodGrid();
            }
            
            // Translate food items (legacy support)
            if (typeof window.foodsData !== 'undefined' && window.foodsData.length > 0) {
                this.translateFoods(lang);
            }
            
            // Translate recipes
            if (typeof window.recipesData !== 'undefined' && window.recipesData.length > 0) {
                this.translateRecipes(lang);
            }
            
            // Trigger custom event for other scripts to listen
            window.dispatchEvent(new CustomEvent('languageChanged', { 
                detail: { language: lang } 
            }));
        },
        
        // Translate foods
        translateFoods(lang) {
            const foodCards = document.querySelectorAll('.food-card, .food-item');
            foodCards.forEach((card, index) => {
                const food = window.foodsData[index];
                if (!food) return;
                
                const nameElement = card.querySelector('.food-name, h3');
                if (nameElement && food.nameEn) {
                    nameElement.textContent = lang === 'en' ? food.nameEn : food.name;
                }
            });
        },
        
        // Translate recipes
        translateRecipes(lang) {
            const recipeCards = document.querySelectorAll('.recipe-card, .recipe-item');
            recipeCards.forEach((card, index) => {
                const recipe = window.recipesData[index];
                if (!recipe) return;
                
                const nameElement = card.querySelector('.recipe-name, h3');
                if (nameElement && recipe.nameEn) {
                    nameElement.textContent = lang === 'en' ? recipe.nameEn : recipe.name;
                }
            });
        },
        
        // Update language toggle buttons
        updateLanguageButtons() {
            document.querySelectorAll('[data-lang-toggle]').forEach(button => {
                const targetLang = button.getAttribute('data-lang-toggle');
                if (targetLang === this.currentLang) {
                    button.style.opacity = '0.5';
                    button.style.pointerEvents = 'none';
                } else {
                    button.style.opacity = '1';
                    button.style.pointerEvents = 'auto';
                }
            });
        },
        
        // Initialize
        init() {
            const savedLang = this.getSavedLanguage();
            this.currentLang = savedLang;
            
            // Wait for DOM
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => {
                    this.applyLanguage(savedLang);
                    this.setupEventListeners();
                });
            } else {
                this.applyLanguage(savedLang);
                this.setupEventListeners();
            }
        },
        
        // Setup event listeners
        setupEventListeners() {
            // Language toggle buttons
            document.querySelectorAll('[data-lang-toggle]').forEach(button => {
                button.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetLang = button.getAttribute('data-lang-toggle');
                    this.applyLanguage(targetLang);
                });
            });
            
            console.log('✅ Unified Language System initialized:', this.currentLang);
        }
    };
    
    // ==========================================
    // 3. AUTO-INITIALIZE
    // ==========================================
    
    UnifiedLanguageSystem.init();
    
    // Expose globally
    window.UnifiedLanguageSystem = UnifiedLanguageSystem;
    window.t = (key) => UnifiedLanguageSystem.t(key);
    
})();
