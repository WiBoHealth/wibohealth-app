/**
 * WiBo Health - Smart Search for Foods Page
 * Version: 1.0.0
 * Date: 2025-12-04
 * Features: Instant search, auto-suggestions, highlighting, keyboard navigation
 */

class FoodsSmartSearch {
    constructor() {
        this.searchInput = null;
        this.suggestionsContainer = null;
        this.currentFocus = -1;
        this.searchTimeout = null;
        this.minChars = 2;
        
        this.init();
    }

    init() {
        // Wait for DOM and data to be ready
        const initWhenReady = () => {
            const hasSearchInput = !!document.getElementById('searchInput');
            const hasAllFoods = !!(window.allFoods && window.allFoods.length > 0);
            
            if (hasSearchInput && hasAllFoods) {
                this.setup();
            } else {
                setTimeout(initWhenReady, 100);
            }
        };

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initWhenReady);
        } else {
            initWhenReady();
        }
    }

    setup() {
        this.searchInput = document.getElementById('searchInput');
        
        if (!this.searchInput) {
            console.warn('Smart Search: searchInput not found');
            return;
        }

        if (!window.allFoods || window.allFoods.length === 0) {
            console.warn('Smart Search: allFoods not ready');
            return;
        }

        // Create suggestions container
        this.createSuggestionsContainer();
        
        // Attach event listeners
        this.attachEventListeners();
        
        console.log('✅ Smart Search initialized successfully');
    }

    createSuggestionsContainer() {
        // Remove existing suggestions if any
        const existing = document.getElementById('searchSuggestions');
        if (existing) existing.remove();

        // Create new suggestions container
        this.suggestionsContainer = document.createElement('div');
        this.suggestionsContainer.id = 'searchSuggestions';
        this.suggestionsContainer.className = 'search-suggestions';
        
        // Insert after search input
        this.searchInput.parentNode.insertBefore(
            this.suggestionsContainer, 
            this.searchInput.nextSibling
        );
    }

    attachEventListeners() {
        // Input event for instant search
        this.searchInput.addEventListener('input', (e) => {
            clearTimeout(this.searchTimeout);
            this.searchTimeout = setTimeout(() => {
                this.handleSearch(e.target.value);
            }, 150); // Debounce 150ms
        });

        // Keyboard navigation
        this.searchInput.addEventListener('keydown', (e) => {
            this.handleKeyboardNavigation(e);
        });

        // Focus events
        this.searchInput.addEventListener('focus', () => {
            if (this.searchInput.value.length >= this.minChars) {
                this.suggestionsContainer.style.display = 'block';
            }
        });

        // Click outside to close suggestions
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.search-box')) {
                this.closeSuggestions();
            }
        });

        // Language change event - re-render suggestions if visible
        document.addEventListener('languageChanged', () => {
            if (this.suggestionsContainer.style.display === 'block' && this.searchInput.value.length >= this.minChars) {
                this.handleSearch(this.searchInput.value);
            }
        });
    }

    handleSearch(searchTerm) {
        const trimmed = searchTerm.trim();

        // Hide suggestions if less than minimum characters
        if (trimmed.length < this.minChars) {
            this.closeSuggestions();
            
            // Still filter foods (existing functionality)
            if (typeof window.filterFoods === 'function') {
                window.filterFoods();
            }
            return;
        }

        // Detect search term language (Arabic vs English)
        const isSearchArabic = /[\u0600-\u06FF]/.test(trimmed);
        
        // Get suggestions
        const suggestions = this.getSuggestions(trimmed);
        
        // Render suggestions with detected language
        this.renderSuggestions(suggestions, trimmed, isSearchArabic);
        
        // Also trigger existing filter
        if (typeof window.filterFoods === 'function') {
            window.filterFoods();
        }
    }

    getSuggestions(searchTerm) {
        if (!window.allFoods || !Array.isArray(window.allFoods)) {
            return [];
        }

        const term = searchTerm.toLowerCase();
        const matches = [];
        const categories = new Set();

        // Search in foods
        window.allFoods.forEach(food => {
            const nameAr = (food.name || '').toLowerCase();
            const nameEn = (food.nameEn || '').toLowerCase();
            const categoryAr = (food.category || '').toLowerCase();
            const categoryEn = (food.categoryEn || '').toLowerCase();

            // Check if matches
            if (nameAr.includes(term) || nameEn.includes(term)) {
                matches.push({
                    type: 'food',
                    name: food.name,
                    nameEn: food.nameEn,
                    category: food.category,
                    categoryEn: food.categoryEn,
                    calories: food.nutrition?.calories || food.calories || 0,
                    id: food.id
                });
            } else if (categoryAr.includes(term) || categoryEn.includes(term)) {
                categories.add(JSON.stringify({
                    type: 'category',
                    name: food.category,
                    nameEn: food.categoryEn
                }));
            }
        });

        // Convert categories set to array
        const categoryMatches = Array.from(categories).map(str => JSON.parse(str));

        // Combine and limit results
        return {
            foods: matches.slice(0, 8), // Max 8 food suggestions
            categories: categoryMatches.slice(0, 3) // Max 3 category suggestions
        };
    }

    renderSuggestions(suggestions, searchTerm, forceArabic = null) {
        const { foods, categories } = suggestions;
        
        // Store language preference for this render
        this._renderLanguage = forceArabic;
        
        // Clear previous suggestions
        this.suggestionsContainer.innerHTML = '';
        this.currentFocus = -1;

        // No results
        if (foods.length === 0 && categories.length === 0) {
            this.suggestionsContainer.innerHTML = `
                <div class="suggestion-item no-results">
                    <i class="fas fa-search"></i>
                    <span>${this.getTranslation('noResults')}</span>
                </div>
            `;
            this.suggestionsContainer.style.display = 'block';
            return;
        }

        // Render categories first
        if (categories.length > 0) {
            const categoryHeader = document.createElement('div');
            categoryHeader.className = 'suggestion-header';
            categoryHeader.textContent = this.getTranslation('categories');
            this.suggestionsContainer.appendChild(categoryHeader);

            categories.forEach(cat => {
                const item = this.createSuggestionItem(cat, searchTerm, 'category');
                this.suggestionsContainer.appendChild(item);
            });
        }

        // Render foods
        if (foods.length > 0) {
            const foodHeader = document.createElement('div');
            foodHeader.className = 'suggestion-header';
            foodHeader.textContent = this.getTranslation('foods');
            this.suggestionsContainer.appendChild(foodHeader);

            foods.forEach(food => {
                const item = this.createSuggestionItem(food, searchTerm, 'food');
                this.suggestionsContainer.appendChild(item);
            });
        }

        // Show suggestions
        this.suggestionsContainer.style.display = 'block';
    }

    createSuggestionItem(data, searchTerm, type) {
        const item = document.createElement('div');
        item.className = 'suggestion-item';
        item.setAttribute('data-type', type);

        // Use render language if provided, otherwise use system language
        let isArabic;
        if (this._renderLanguage !== null && this._renderLanguage !== undefined) {
            isArabic = this._renderLanguage;
        } else {
            const currentLang = (window.UnifiedLanguageSystem && window.UnifiedLanguageSystem.currentLang) || document.documentElement.lang || 'ar';
            isArabic = currentLang === 'ar';
        }

        if (type === 'category') {
            const displayName = isArabic ? data.name : data.nameEn;
            item.innerHTML = `
                <i class="fas fa-folder"></i>
                <span>${this.highlightMatch(displayName, searchTerm)}</span>
            `;
            item.addEventListener('click', () => {
                this.searchInput.value = displayName;
                this.closeSuggestions();
                if (typeof window.filterFoods === 'function') {
                    window.filterFoods();
                }
            });
        } else {
            const displayName = isArabic ? data.name : data.nameEn;
            const displayCategory = isArabic ? data.category : data.categoryEn;
            
            item.innerHTML = `
                <i class="fas fa-utensils"></i>
                <div class="suggestion-content">
                    <div class="suggestion-name">${this.highlightMatch(displayName, searchTerm)}</div>
                    <div class="suggestion-details">
                        <span class="suggestion-category">${displayCategory}</span>
                        <span class="suggestion-calories">${data.calories} ${this.getTranslation('cal')}</span>
                    </div>
                </div>
            `;
            item.addEventListener('click', () => {
                // Navigate to food details
                window.location.href = `food-details.html?id=${data.id}`;
            });
        }

        return item;
    }

    highlightMatch(text, searchTerm) {
        if (!searchTerm) return text;
        
        const regex = new RegExp(`(${searchTerm})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }

    handleKeyboardNavigation(e) {
        const items = this.suggestionsContainer.querySelectorAll('.suggestion-item:not(.no-results)');
        
        if (items.length === 0) return;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            this.currentFocus++;
            if (this.currentFocus >= items.length) this.currentFocus = 0;
            this.setActive(items);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            this.currentFocus--;
            if (this.currentFocus < 0) this.currentFocus = items.length - 1;
            this.setActive(items);
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (this.currentFocus > -1) {
                items[this.currentFocus].click();
            }
        } else if (e.key === 'Escape') {
            this.closeSuggestions();
            this.searchInput.blur();
        }
    }

    setActive(items) {
        // Remove active class from all
        items.forEach(item => item.classList.remove('active'));
        
        // Add active to current
        if (this.currentFocus >= 0 && this.currentFocus < items.length) {
            items[this.currentFocus].classList.add('active');
            items[this.currentFocus].scrollIntoView({ block: 'nearest' });
        }
    }

    closeSuggestions() {
        this.suggestionsContainer.style.display = 'none';
        this.currentFocus = -1;
    }

    getTranslation(key) {
        const translations = {
            ar: {
                noResults: 'لا توجد نتائج',
                categories: 'التصنيفات',
                foods: 'الأطعمة',
                cal: 'سعرة'
            },
            en: {
                noResults: 'No results found',
                categories: 'Categories',
                foods: 'Foods',
                cal: 'cal'
            }
        };

        const currentLang = (window.UnifiedLanguageSystem && window.UnifiedLanguageSystem.currentLang) || document.documentElement.lang || 'ar';
        return translations[currentLang][key] || translations.ar[key];
    }
}

// Initialize on page load
const smartSearch = new FoodsSmartSearch();
