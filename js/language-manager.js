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
            // Remove leading/trailing slashes and split
            const parts = path.replace(/^\/|\/$/g, '').split('/');
            
            // If path is like /en/ or /en, return index.html
            if (parts.length === 1 && (parts[0] === 'en' || parts[0] === '')) {
                return 'index.html';
            }
            
            // If path is like /en/foods.html, return foods.html
            // If path is like /foods.html, return foods.html
            const pageName = parts[parts.length - 1];
            return pageName || 'index.html';
        },

        // Build URL for target language
        buildLanguageUrl(targetLang) {
            const currentPage = this.getCurrentPageName();
            
            // Clean the page name (remove any 'en' prefix if exists)
            const cleanPage = currentPage === 'en' ? 'index.html' : currentPage;
            
            if (targetLang === 'en') {
                return `/en/${cleanPage}`;
            } else {
                return `/${cleanPage}`;
            }
        },

        // Check and redirect if needed
        checkAndRedirect() {
            const currentPath = window.location.pathname;
            const currentLang = this.getCurrentLanguage();
            const savedLang = this.getSavedLanguage();

            // Don't auto-redirect on homepage - let user choose language
            // Homepage should always be Arabic by default
            if (currentPath === '/' || currentPath === '/index.html') {
                return; // Don't redirect on homepage
            }

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
