/**
 * WiBo Health - Single URL Language Switcher
 * Changes content language WITHOUT changing URL
 * Version: 5.0.0
 */

(function() {
    'use strict';

    const LanguageSwitcher = {
        currentLang: 'ar', // اللغة الافتراضية

        // الحصول على اللغة المحفوظة
        getSavedLanguage() {
            return localStorage.getItem('wibohealth_language') || 'ar';
        },

        // حفظ اللغة
        saveLanguage(lang) {
            localStorage.setItem('wibohealth_language', lang);
            this.currentLang = lang;
        },

        // تطبيق اللغة على الصفحة
        applyLanguage(lang) {
            const html = document.documentElement;
            
            if (lang === 'en') {
                // إنجليزي
                html.setAttribute('lang', 'en');
                html.setAttribute('dir', 'ltr');
                
                // إخفاء المحتوى العربي
                document.querySelectorAll('[data-lang="ar"]').forEach(el => {
                    el.style.display = 'none';
                });
                
                // إظهار المحتوى الإنجليزي
                document.querySelectorAll('[data-lang="en"]').forEach(el => {
                    el.style.display = '';
                });
                
                // تعديل الفونت
                document.body.style.fontFamily = "'Inter', sans-serif";
                
                // تحديث النصوص الديناميكية
                this.updateDynamicText('en');
                
            } else {
                // عربي
                html.setAttribute('lang', 'ar');
                html.setAttribute('dir', 'rtl');
                
                // إخفاء المحتوى الإنجليزي
                document.querySelectorAll('[data-lang="en"]').forEach(el => {
                    el.style.display = 'none';
                });
                
                // إظهار المحتوى العربي
                document.querySelectorAll('[data-lang="ar"]').forEach(el => {
                    el.style.display = '';
                });
                
                // تعديل الفونت
                document.body.style.fontFamily = "'Cairo', sans-serif";
                
                // تحديث النصوص الديناميكية
                this.updateDynamicText('ar');
            }
            
            // حفظ اللغة
            this.saveLanguage(lang);
            
            // تحديث أزرار اللغة
            this.updateLanguageButtons();
        },

        // تحديث النصوص الديناميكية (data.js, recipes, etc.)
        updateDynamicText(lang) {
            // تحديث عناصر تحتوي على [data-translate]
            document.querySelectorAll('[data-translate]').forEach(el => {
                const key = el.getAttribute('data-translate');
                if (window.t) {
                    el.textContent = window.t(key, lang);
                }
            });
        },

        // تبديل اللغة
        toggleLanguage() {
            const newLang = this.currentLang === 'ar' ? 'en' : 'ar';
            this.applyLanguage(newLang);
        },

        // تحديث أزرار اللغة
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

        // التهيئة
        init() {
            // تحميل اللغة المحفوظة
            const savedLang = this.getSavedLanguage();
            this.currentLang = savedLang;
            
            // تطبيق اللغة عند تحميل الصفحة
            document.addEventListener('DOMContentLoaded', () => {
                this.applyLanguage(savedLang);
                
                // إضافة مستمعي الأحداث لأزرار اللغة
                document.querySelectorAll('[data-lang-toggle]').forEach(button => {
                    button.addEventListener('click', (e) => {
                        e.preventDefault();
                        const targetLang = button.getAttribute('data-lang-toggle');
                        this.applyLanguage(targetLang);
                    });
                });
            });
        }
    };

    // تشغيل تلقائي
    LanguageSwitcher.init();

    // إتاحة عالمياً
    window.LanguageSwitcher = LanguageSwitcher;

})();
