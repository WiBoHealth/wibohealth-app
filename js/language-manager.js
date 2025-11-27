/**
 * WiBo Health - Language Manager
 * Manages language preference across all pages using localStorage
 */

(function() {
    'use strict';

    const LanguageManager = {
        // Get current language from URL
        getCurrentLanguage() {
            return window.location.pathname.startsWith('/en/') ? 'en' : 'ar';
        },

        // Get saved language preference
        getSavedLanguage() {
            return localStorage.getItem('wibohealth_language') || 'ar';
        },

        // Save language preference
        saveLanguage(lang) {
            localStorage.setItem('wibohealth_language', lang);
        },

        // Get current page name (without language prefix)
        getCurrentPageName() {
            const path = window.location.pathname;
            const pageName = path.split('/').pop() || 'index.html';
            return pageName;
        },

        // Build URL for target language
        buildLanguageUrl(targetLang) {
            const currentPage = this.getCurrentPageName();
            
            if (targetLang === 'en') {
                return `/en/${currentPage}`;
            } else {
                return `/${currentPage}`;
            }
        },

        // Check and redirect if needed
        checkAndRedirect() {
            const currentLang = this.getCurrentLanguage();
            const savedLang = this.getSavedLanguage();

            // Only redirect if saved language is different from current
            if (savedLang !== currentLang) {
                const targetUrl = this.buildLanguageUrl(savedLang);
                window.location.replace(targetUrl);
            }
        },

        // Handle language toggle
        toggleLanguage() {
            const currentLang = this.getCurrentLanguage();
            const newLang = currentLang === 'ar' ? 'en' : 'ar';
            
            // Save preference
            this.saveLanguage(newLang);
            
            // Redirect to new language
            const targetUrl = this.buildLanguageUrl(newLang);
            window.location.href = targetUrl;
        },

        // Initialize
        init() {
            // Check and redirect on page load
            this.checkAndRedirect();

            // Setup language toggle buttons
            document.addEventListener('DOMContentLoaded', () => {
                // Find all language toggle links
                const langLinks = document.querySelectorAll('a[href*="/en/"], a[href^="/"][href$=".html"]');
                
                langLinks.forEach(link => {
                    const href = link.getAttribute('href');
                    
                    // Check if it's a language toggle link
                    if ((href.startsWith('/en/') && this.getCurrentLanguage() === 'ar') ||
                        (href.startsWith('/') && !href.startsWith('/en/') && this.getCurrentLanguage() === 'en')) {
                        
                        link.addEventListener('click', (e) => {
                            e.preventDefault();
                            this.toggleLanguage();
                        });
                    }
                });
            });
        }
    };

    // Auto-initialize
    LanguageManager.init();

    // Expose to global scope for manual usage if needed
    window.LanguageManager = LanguageManager;
})();
