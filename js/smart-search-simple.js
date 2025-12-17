/**
 * WiBo Health - Simple Smart Search
 * Version: 1.0 - Safe & Tested
 */

(function() {
    'use strict';
    
    console.log('🔍 Smart Search Loading...');
    
    // Wait for page to be ready
    function initSmartSearch() {
        const searchInput = document.getElementById('searchInput');
        
        if (!searchInput) {
            console.warn('⚠️ Search input not found, retrying...');
            setTimeout(initSmartSearch, 500);
            return;
        }
        
        console.log('✅ Search input found!');
        
        // Check if data is loaded
        const initialData = window.supplementsData || window.allSupplementsData || (typeof supplementsData !== 'undefined' ? supplementsData : []);
        if (initialData.length > 0) {
            console.log('✅ Found', initialData.length, 'supplements ready!');
        } else {
            console.log('⏳ Waiting for supplements data to load...');
        }
        
        // Create suggestions container
        const searchBox = searchInput.parentElement;
        const suggestionsDiv = document.createElement('div');
        suggestionsDiv.id = 'smartSuggestions';
        suggestionsDiv.className = 'smart-suggestions';
        searchBox.appendChild(suggestionsDiv);
        
        // Add CSS
        addSmartSearchCSS();
        
        let currentIndex = -1;
        let suggestions = [];
        
        // Listen to input
        searchInput.addEventListener('input', function(e) {
            const query = e.target.value.trim().toLowerCase();
            
            if (query.length < 2) {
                hideSuggestions();
                return;
            }
            
            // Get data - try multiple sources
            const data = window.supplementsData || window.allSupplementsData || supplementsData || [];
            if (data.length === 0) {
                console.warn('⚠️ No supplements data yet, waiting...');
                // Retry after delay if data not loaded
                setTimeout(function() {
                    const retryData = window.supplementsData || window.allSupplementsData || supplementsData || [];
                    if (retryData.length > 0) {
                        console.log('✅ Data loaded! Found', retryData.length, 'supplements');
                    }
                }, 2000);
                return;
            }
            
            // Filter supplements
            suggestions = data.filter(function(supp) {
                const nameAr = supp.name.toLowerCase();
                const nameEn = supp.englishName ? supp.englishName.toLowerCase() : '';
                const category = supp.category ? supp.category.toLowerCase() : '';
                
                return nameAr.includes(query) || 
                       nameEn.includes(query) || 
                       category.includes(query);
            }).slice(0, 6); // Max 6 suggestions
            
            if (suggestions.length > 0) {
                showSuggestions(suggestions, query);
            } else {
                hideSuggestions();
            }
        });
        
        // Keyboard navigation
        searchInput.addEventListener('keydown', function(e) {
            const suggestionItems = suggestionsDiv.querySelectorAll('.suggestion-item');
            
            if (suggestionItems.length === 0) return;
            
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                currentIndex = (currentIndex + 1) % suggestionItems.length;
                highlightSuggestion(suggestionItems, currentIndex);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                currentIndex = currentIndex <= 0 ? suggestionItems.length - 1 : currentIndex - 1;
                highlightSuggestion(suggestionItems, currentIndex);
            } else if (e.key === 'Enter' && currentIndex >= 0) {
                e.preventDefault();
                const suppId = suggestions[currentIndex].id;
                selectSupplement(suppId);
            } else if (e.key === 'Escape') {
                hideSuggestions();
            }
        });
        
        // Close on click outside
        document.addEventListener('click', function(e) {
            if (!searchBox.contains(e.target)) {
                hideSuggestions();
            }
        });
        
        function showSuggestions(supps, query) {
            currentIndex = -1;
            
            suggestionsDiv.innerHTML = supps.map(function(supp, index) {
                const nameAr = highlightText(supp.name, query);
                const nameEn = supp.englishName ? highlightText(supp.englishName, query) : '';
                const icon = supp.icon || '💊';
                
                return `
                    <div class="suggestion-item" data-index="${index}" data-id="${supp.id}">
                        <span class="sug-icon">${icon}</span>
                        <div class="sug-content">
                            <div class="sug-name-ar">${nameAr}</div>
                            <div class="sug-name-en">${nameEn}</div>
                        </div>
                        <i class="fas fa-arrow-left sug-arrow"></i>
                    </div>
                `;
            }).join('');
            
            suggestionsDiv.classList.add('show');
            
            // Add click handlers
            suggestionsDiv.querySelectorAll('.suggestion-item').forEach(function(item) {
                item.addEventListener('click', function() {
                    const id = parseInt(this.getAttribute('data-id'));
                    selectSupplement(id);
                });
            });
        }
        
        function hideSuggestions() {
            suggestionsDiv.classList.remove('show');
            currentIndex = -1;
        }
        
        function highlightSuggestion(items, index) {
            items.forEach(function(item, i) {
                if (i === index) {
                    item.classList.add('active');
                } else {
                    item.classList.remove('active');
                }
            });
        }
        
        function highlightText(text, query) {
            if (!query || !text) return text;
            const regex = new RegExp('(' + query + ')', 'gi');
            return text.replace(regex, '<mark>$1</mark>');
        }
        
        function selectSupplement(id) {
            hideSuggestions();
            searchInput.value = '';
            
            // Call existing modal function
            if (typeof openSupplementModal === 'function') {
                openSupplementModal(id);
            } else if (typeof window.openSupplementModal === 'function') {
                window.openSupplementModal(id);
            } else {
                console.error('❌ Modal function not found');
            }
        }
        
        console.log('✅ Smart Search Ready!');
    }
    
    function addSmartSearchCSS() {
        if (document.getElementById('smartSearchCSS')) return;
        
        const style = document.createElement('style');
        style.id = 'smartSearchCSS';
        style.textContent = `
            .smart-suggestions {
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: white;
                border-radius: 0 0 15px 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.3s ease;
                z-index: 1000;
                margin-top: -5px;
            }
            
            .smart-suggestions.show {
                max-height: 400px;
                overflow-y: auto;
            }
            
            .suggestion-item {
                display: flex;
                align-items: center;
                gap: 12px;
                padding: 12px 20px;
                cursor: pointer;
                transition: all 0.2s;
                border-bottom: 1px solid #f0f0f0;
            }
            
            .suggestion-item:last-child {
                border-bottom: none;
            }
            
            .suggestion-item:hover,
            .suggestion-item.active {
                background: linear-gradient(135deg, #f8f9ff, #f0f2ff);
                border-right: 3px solid #667eea;
            }
            
            .sug-icon {
                font-size: 28px;
                flex-shrink: 0;
            }
            
            .sug-content {
                flex: 1;
            }
            
            .sug-name-ar {
                font-weight: 700;
                color: #1f2937;
                font-size: 15px;
                margin-bottom: 3px;
            }
            
            .sug-name-en {
                font-size: 13px;
                color: #6b7280;
            }
            
            .sug-name-ar mark,
            .sug-name-en mark {
                background: #fef08a;
                color: #ca8a04;
                padding: 2px 4px;
                border-radius: 3px;
                font-weight: 800;
            }
            
            .sug-arrow {
                color: #667eea;
                font-size: 14px;
                opacity: 0;
                transition: opacity 0.2s;
            }
            
            .suggestion-item:hover .sug-arrow,
            .suggestion-item.active .sug-arrow {
                opacity: 1;
            }
            
            .search-box {
                position: relative;
            }
            
            /* Scrollbar styling */
            .smart-suggestions::-webkit-scrollbar {
                width: 6px;
            }
            
            .smart-suggestions::-webkit-scrollbar-track {
                background: #f1f1f1;
            }
            
            .smart-suggestions::-webkit-scrollbar-thumb {
                background: #667eea;
                border-radius: 3px;
            }
            
            .smart-suggestions::-webkit-scrollbar-thumb:hover {
                background: #5568d3;
            }
        `;
        document.head.appendChild(style);
    }
    
    // Start when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSmartSearch);
    } else {
        setTimeout(initSmartSearch, 100);
    }
    
})();
