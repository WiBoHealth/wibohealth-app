/**
 * WiBo Health - Smart Supplements Features
 * Version: 2.0.0
 * 
 * Features:
 * 1. Smart Search with Suggestions
 * 2. Drug Interactions Warnings
 * 3. Smart Recommendations System
 * 4. Enhanced Comparison
 * 5. Fast Loading Optimization
 */

console.log('🚀 Smart Features Script Loaded Successfully!');

// ============================================
// 1. SMART SEARCH WITH AUTO-SUGGESTIONS
// ============================================

let searchSuggestions = [];
let currentSuggestionIndex = -1;

function initSmartSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) {
        console.warn('⚠️ Search input not found, retrying...');
        setTimeout(initSmartSearch, 1000);
        return;
    }
    
    // Create suggestions dropdown
    const suggestionsDiv = document.createElement('div');
    suggestionsDiv.id = 'searchSuggestions';
    suggestionsDiv.className = 'search-suggestions hidden';
    searchInput.parentElement.appendChild(suggestionsDiv);
    
    // Add CSS for suggestions
    addSearchSuggestionsCSS();
    
    // Input event for live suggestions
    searchInput.addEventListener('input', handleSearchInput);
    
    // Keyboard navigation
    searchInput.addEventListener('keydown', handleSearchKeyboard);
    
    // Close suggestions when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !suggestionsDiv.contains(e.target)) {
            hideSuggestions();
        }
    });
}

function handleSearchInput(e) {
    const query = e.target.value.trim().toLowerCase();
    
    if (query.length < 2) {
        hideSuggestions();
        return;
    }
    
    // Get matching supplements
    const matches = window.supplementsData.filter(supp => {
        const nameAr = supp.name.toLowerCase();
        const nameEn = supp.englishName.toLowerCase();
        const category = supp.category.toLowerCase();
        const tags = supp.tags.join(' ').toLowerCase();
        
        return nameAr.includes(query) || 
               nameEn.includes(query) || 
               category.includes(query) ||
               tags.includes(query);
    }).slice(0, 8); // Limit to 8 suggestions
    
    if (matches.length > 0) {
        showSuggestions(matches, query);
    } else {
        hideSuggestions();
    }
}

function showSuggestions(matches, query) {
    const suggestionsDiv = document.getElementById('searchSuggestions');
    searchSuggestions = matches;
    currentSuggestionIndex = -1;
    
    suggestionsDiv.innerHTML = matches.map((supp, index) => `
        <div class="suggestion-item" data-index="${index}" onclick="selectSuggestion(${supp.id})">
            <span class="suggestion-icon">${supp.icon}</span>
            <div class="suggestion-text">
                <div class="suggestion-name">
                    ${highlightMatch(supp.name, query)} 
                    <span class="suggestion-name-en">${highlightMatch(supp.englishName, query)}</span>
                </div>
                <div class="suggestion-category">${getCategoryName(supp.category)}</div>
            </div>
            <i class="fas fa-arrow-left suggestion-arrow"></i>
        </div>
    `).join('');
    
    suggestionsDiv.classList.remove('hidden');
}

function hideSuggestions() {
    const suggestionsDiv = document.getElementById('searchSuggestions');
    if (suggestionsDiv) {
        suggestionsDiv.classList.add('hidden');
        currentSuggestionIndex = -1;
    }
}

function highlightMatch(text, query) {
    if (!query) return text;
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function handleSearchKeyboard(e) {
    const suggestionsDiv = document.getElementById('searchSuggestions');
    if (suggestionsDiv.classList.contains('hidden')) return;
    
    const items = suggestionsDiv.querySelectorAll('.suggestion-item');
    
    if (e.key === 'ArrowDown') {
        e.preventDefault();
        currentSuggestionIndex = (currentSuggestionIndex + 1) % items.length;
        updateSuggestionHighlight(items);
    } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        currentSuggestionIndex = currentSuggestionIndex <= 0 ? items.length - 1 : currentSuggestionIndex - 1;
        updateSuggestionHighlight(items);
    } else if (e.key === 'Enter' && currentSuggestionIndex >= 0) {
        e.preventDefault();
        const suppId = searchSuggestions[currentSuggestionIndex].id;
        selectSuggestion(suppId);
    } else if (e.key === 'Escape') {
        hideSuggestions();
    }
}

function updateSuggestionHighlight(items) {
    items.forEach((item, index) => {
        if (index === currentSuggestionIndex) {
            item.classList.add('active');
            item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        } else {
            item.classList.remove('active');
        }
    });
}

function selectSuggestion(suppId) {
    hideSuggestions();
    openSupplementModal(suppId);
    document.getElementById('searchInput').value = '';
}

function addSearchSuggestionsCSS() {
    if (document.getElementById('smartSearchCSS')) return;
    
    const style = document.createElement('style');
    style.id = 'smartSearchCSS';
    style.textContent = `
        .search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border-radius: 0 0 15px 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            max-height: 400px;
            overflow-y: auto;
            z-index: 1000;
            margin-top: -10px;
            padding-top: 10px;
        }
        
        .search-suggestions.hidden {
            display: none;
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
        
        .suggestion-item:hover,
        .suggestion-item.active {
            background: linear-gradient(135deg, #f8f9ff, #f0f2ff);
            border-right: 3px solid #667eea;
        }
        
        .suggestion-icon {
            font-size: 24px;
            flex-shrink: 0;
        }
        
        .suggestion-text {
            flex: 1;
        }
        
        .suggestion-name {
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 4px;
        }
        
        .suggestion-name mark {
            background: #fef08a;
            color: #ca8a04;
            padding: 2px 4px;
            border-radius: 3px;
            font-weight: 800;
        }
        
        .suggestion-name-en {
            font-size: 13px;
            color: #6b7280;
            margin-right: 8px;
        }
        
        .suggestion-category {
            font-size: 12px;
            color: #9ca3af;
        }
        
        .suggestion-arrow {
            color: #667eea;
            font-size: 16px;
            opacity: 0;
            transition: opacity 0.2s;
        }
        
        .suggestion-item:hover .suggestion-arrow,
        .suggestion-item.active .suggestion-arrow {
            opacity: 1;
        }
        
        .search-box {
            position: relative;
        }
    `;
    document.head.appendChild(style);
}

// ============================================
// 2. DRUG INTERACTIONS WARNINGS (CRITICAL)
// ============================================

function showDrugInteractionWarning(supplement) {
    if (!supplement.interactions || supplement.interactions.length === 0) return '';
    
    const criticalInteractions = supplement.interactions.filter(interaction => {
        const lower = interaction.toLowerCase();
        return lower.includes('خطير') || lower.includes('يمنع') || lower.includes('dangerous') || 
               lower.includes('avoid') || lower.includes('أدوية') || lower.includes('medication');
    });
    
    if (criticalInteractions.length === 0) return '';
    
    return `
        <div class="critical-warning-box" style="
            background: linear-gradient(135deg, #fee2e2, #fecaca);
            border: 2px solid #dc2626;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 15px rgba(220, 38, 38, 0.2);
            animation: pulse-warning 2s infinite;
        ">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <div style="
                    width: 50px;
                    height: 50px;
                    background: #dc2626;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 24px;
                    animation: shake 0.5s infinite;
                ">⚠️</div>
                <div>
                    <h3 style="color: #dc2626; margin: 0; font-size: 20px; font-weight: 800;">
                        تحذير هام - تفاعلات دوائية خطيرة!
                    </h3>
                    <p style="color: #7f1d1d; margin: 5px 0 0 0; font-size: 14px;">
                        استشر طبيبك قبل الاستخدام إذا كنت تتناول أدوية
                    </p>
                </div>
            </div>
            <ul style="margin: 0; padding-right: 20px; color: #7f1d1d;">
                ${criticalInteractions.map(interaction => `
                    <li style="margin-bottom: 8px; font-weight: 600;">
                        <i class="fas fa-exclamation-triangle" style="color: #dc2626; margin-left: 8px;"></i>
                        ${interaction}
                    </li>
                `).join('')}
            </ul>
            <div style="
                margin-top: 15px;
                padding: 12px;
                background: white;
                border-radius: 8px;
                border-right: 3px solid #dc2626;
            ">
                <i class="fas fa-user-md" style="color: #dc2626; margin-left: 8px;"></i>
                <strong style="color: #dc2626;">مهم جداً:</strong>
                <span style="color: #7f1d1d;">
                    لا تبدأ أو توقف هذا المكمل دون استشارة طبيبك إذا كنت تتناول أي أدوية موصوفة.
                </span>
            </div>
        </div>
        
        <style>
            @keyframes pulse-warning {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.02); }
            }
            
            @keyframes shake {
                0%, 100% { transform: rotate(0deg); }
                25% { transform: rotate(-5deg); }
                75% { transform: rotate(5deg); }
            }
        </style>
    `;
}

// ============================================
// 3. SMART RECOMMENDATIONS SYSTEM
// ============================================

function getSmartRecommendations(currentSupplement) {
    if (!window.supplementsData || !currentSupplement) return '';
    
    // Find similar supplements based on category and benefits
    const recommendations = window.supplementsData
        .filter(supp => supp.id !== currentSupplement.id)
        .map(supp => {
            let score = 0;
            
            // Same category = high priority
            if (supp.category === currentSupplement.category) score += 50;
            
            // Shared tags
            const sharedTags = supp.tags.filter(tag => 
                currentSupplement.tags.includes(tag)
            );
            score += sharedTags.length * 10;
            
            // Complementary supplements (works well together)
            if (isComplementary(currentSupplement, supp)) score += 30;
            
            return { ...supp, score };
        })
        .filter(supp => supp.score > 0)
        .sort((a, b) => b.score - a.score)
        .slice(0, 4); // Top 4 recommendations
    
    if (recommendations.length === 0) return '';
    
    return `
        <div class="recommendations-section" style="
            background: linear-gradient(135deg, #f0fdf4, #dcfce7);
            border-radius: 15px;
            padding: 25px;
            margin-top: 30px;
            border-right: 4px solid #10b981;
        ">
            <h3 style="color: #065f46; margin: 0 0 20px 0; display: flex; align-items: center; gap: 10px;">
                <i class="fas fa-lightbulb" style="color: #10b981;"></i>
                توصيات ذكية - مكملات مشابهة أو مكملة
            </h3>
            <div class="recommendations-grid" style="
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
            ">
                ${recommendations.map(supp => `
                    <div class="recommendation-card" onclick="openSupplementModal(${supp.id})" style="
                        background: white;
                        padding: 15px;
                        border-radius: 12px;
                        cursor: pointer;
                        transition: all 0.3s;
                        border: 2px solid transparent;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    " onmouseover="this.style.transform='translateY(-5px)'; this.style.borderColor='#10b981';" 
                       onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='transparent';">
                        <div style="font-size: 32px; text-align: center; margin-bottom: 10px;">
                            ${supp.icon}
                        </div>
                        <h4 style="color: #1f2937; margin: 0 0 5px 0; text-align: center; font-size: 16px;">
                            ${supp.name}
                        </h4>
                        <p style="color: #6b7280; font-size: 12px; text-align: center; margin: 0;">
                            ${supp.englishName}
                        </p>
                        <div style="
                            margin-top: 10px;
                            padding: 8px;
                            background: #f0fdf4;
                            border-radius: 8px;
                            text-align: center;
                        ">
                            <span style="color: #10b981; font-size: 12px; font-weight: 600;">
                                <i class="fas fa-check-circle"></i> ${getMatchReason(currentSupplement, supp)}
                            </span>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function isComplementary(supp1, supp2) {
    const complementaryPairs = {
        'بروتين': ['كرياتين', 'bcaa', 'فيتامينات'],
        'أوميغا': ['فيتامين د', 'كالسيوم'],
        'كرياتين': ['بروتين', 'bcaa'],
        'فيتامين د': ['كالسيوم', 'مغنيسيوم', 'أوميغا'],
        'كالسيوم': ['فيتامين د', 'مغنيسيوم'],
        'حديد': ['فيتامين سي'],
        'مغنيسيوم': ['فيتامين د', 'كالسيوم']
    };
    
    for (const [key, values] of Object.entries(complementaryPairs)) {
        if (supp1.name.includes(key) && values.some(v => supp2.name.toLowerCase().includes(v))) {
            return true;
        }
    }
    return false;
}

function getMatchReason(currentSupp, recommendedSupp) {
    if (currentSupp.category === recommendedSupp.category) {
        return 'نفس التصنيف';
    }
    if (isComplementary(currentSupp, recommendedSupp)) {
        return 'يعمل بشكل جيد معاً';
    }
    return 'مشابه في الفوائد';
}

// ============================================
// 4. ENHANCED COMPARISON
// ============================================

function enhanceComparisonModal(selectedSupplements) {
    if (!selectedSupplements || selectedSupplements.length < 2) return;
    
    const compareBody = document.getElementById('compareModalBody');
    
    // Add quick comparison summary
    const summary = `
        <div class="comparison-summary" style="
            background: linear-gradient(135deg, #eff6ff, #dbeafe);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 25px;
            border-right: 4px solid #3b82f6;
        ">
            <h3 style="color: #1e40af; margin: 0 0 15px 0;">
                <i class="fas fa-chart-line"></i> ملخص المقارنة السريع
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                ${selectedSupplements.map(supp => `
                    <div style="background: white; padding: 15px; border-radius: 10px; text-align: center;">
                        <div style="font-size: 36px; margin-bottom: 10px;">${supp.icon}</div>
                        <h4 style="color: #1f2937; margin: 0 0 10px 0;">${supp.name}</h4>
                        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
                            <div style="background: #f0fdf4; padding: 8px; border-radius: 6px; color: #065f46;">
                                <strong>الفوائد:</strong> ${supp.benefits.length}
                            </div>
                            <div style="background: #fef3c7; padding: 8px; border-radius: 6px; color: #92400e;">
                                <strong>التحذيرات:</strong> ${supp.warnings.length}
                            </div>
                            ${supp.interactions ? `
                                <div style="background: #fee2e2; padding: 8px; border-radius: 6px; color: #7f1d1d;">
                                    <strong>التفاعلات:</strong> ${supp.interactions.length}
                                </div>
                            ` : ''}
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
    
    // Find best choice indicator
    const bestChoice = findBestChoice(selectedSupplements);
    const bestChoiceHTML = bestChoice ? `
        <div style="
            background: linear-gradient(135deg, #fef3c7, #fde68a);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-right: 4px solid #f59e0b;
            display: flex;
            align-items: center;
            gap: 12px;
        ">
            <span style="font-size: 32px;">🏆</span>
            <div>
                <strong style="color: #92400e;">الخيار الأفضل للمبتدئين:</strong>
                <span style="color: #78350f;"> ${bestChoice.name} - ${bestChoice.reason}</span>
            </div>
        </div>
    ` : '';
    
    // Prepend to existing comparison
    compareBody.insertAdjacentHTML('afterbegin', summary + bestChoiceHTML);
}

function findBestChoice(supplements) {
    // Simple logic: fewest warnings + most benefits
    const scored = supplements.map(supp => ({
        ...supp,
        safetyScore: (supp.benefits.length * 2) - supp.warnings.length
    }));
    
    const best = scored.sort((a, b) => b.safetyScore - a.safetyScore)[0];
    
    return {
        name: best.name,
        reason: 'أقل تحذيرات وأكثر فوائد'
    };
}

// ============================================
// 5. FAST LOADING OPTIMIZATION
// ============================================

// Lazy load images and heavy content
function optimizeLoadingSpeed() {
    // Show supplements in batches for faster initial render
    if (typeof displaySupplements === 'function') {
        const originalDisplay = window.displaySupplements;
        
        window.displaySupplements = function() {
            const grid = document.getElementById('supplementsGrid');
            if (!grid || !window.supplementsData) return;
            
            // Clear loading
            const loading = document.querySelector('.loading');
            if (loading) loading.classList.remove('show');
            
            // Display in batches of 20 for smooth rendering
            let currentBatch = 0;
            const batchSize = 20;
            const totalSupplements = window.supplementsData.length;
            
            function displayBatch() {
                const start = currentBatch * batchSize;
                const end = Math.min(start + batchSize, totalSupplements);
                const batch = window.supplementsData.slice(start, end);
                
                batch.forEach(supp => {
                    const card = createSupplementCard(supp);
                    grid.appendChild(card);
                });
                
                currentBatch++;
                
                if (end < totalSupplements) {
                    requestAnimationFrame(displayBatch);
                }
            }
            
            displayBatch();
        };
    }
}

function createSupplementCard(supp) {
    const card = document.createElement('div');
    card.className = 'supplement-card';
    card.onclick = () => openSupplementModal(supp.id);
    card.innerHTML = `
        <div class="supplement-checkbox">
            <input type="checkbox" id="compare-${supp.id}" onchange="toggleCompare(${supp.id})" onclick="event.stopPropagation()">
            <label for="compare-${supp.id}"></label>
        </div>
        <div class="supplement-icon">${supp.icon}</div>
        <h3 class="supplement-name">${supp.name}</h3>
        <p class="supplement-name-en">${supp.englishName}</p>
        <p class="supplement-summary">${supp.summary}</p>
        <div class="supplement-tags">
            ${supp.tags.slice(0, 3).map(tag => `<span class="tag">${tag}</span>`).join('')}
        </div>
    `;
    return card;
}

// Performance monitoring
function monitorPerformance() {
    if ('performance' in window && 'measure' in window.performance) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                const perfData = performance.getEntriesByType('navigation')[0];
                if (perfData) {
                    console.log('⚡ Page Load Time:', Math.round(perfData.loadEventEnd - perfData.fetchStart), 'ms');
                }
            }, 0);
        });
    }
}

// ============================================
// INITIALIZATION
// ============================================

function initSmartFeatures() {
    console.log('🚀 Initializing Smart Features...');
    
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(initializeFeatures, 100);
        });
    } else {
        setTimeout(initializeFeatures, 100);
    }
}

function initializeFeatures() {
    console.log('🎯 Starting feature initialization...');
    
    try {
        initSmartSearch();
        console.log('✅ Smart Search initialized');
    } catch (e) {
        console.warn('⚠️ Smart Search failed:', e.message);
    }
    
    try {
        optimizeLoadingSpeed();
        console.log('✅ Loading optimization initialized');
    } catch (e) {
        console.warn('⚠️ Loading optimization failed:', e.message);
    }
    
    try {
        monitorPerformance();
        console.log('✅ Performance monitoring initialized');
    } catch (e) {
        console.warn('⚠️ Performance monitoring failed:', e.message);
    }
    
    // Override modal opening to add warnings and recommendations
    if (typeof openSupplementModal === 'function') {
        const originalOpenModal = window.openSupplementModal;
        
        window.openSupplementModal = function(id) {
            originalOpenModal(id);
            
            // Add enhancements after modal opens
            setTimeout(() => {
                const supplement = window.supplementsData.find(s => s.id === id);
                if (!supplement) return;
                
                const modalBody = document.getElementById('modalBody');
                if (!modalBody) return;
                
                // Add drug interaction warning at the top
                const warningHTML = showDrugInteractionWarning(supplement);
                if (warningHTML) {
                    modalBody.insertAdjacentHTML('afterbegin', warningHTML);
                }
                
                // Add recommendations at the bottom
                const recommendationsHTML = getSmartRecommendations(supplement);
                if (recommendationsHTML) {
                    modalBody.insertAdjacentHTML('beforeend', recommendationsHTML);
                }
            }, 50);
        };
    }
    
    // Override compare modal to add enhancements
    if (typeof openCompareModal === 'function') {
        const originalCompareModal = window.openCompareModal;
        
        window.openCompareModal = function() {
            originalCompareModal();
            
            setTimeout(() => {
                const selectedSupplements = window.supplementsData.filter(s => 
                    window.comparedSupplements && window.comparedSupplements.includes(s.id)
                );
                enhanceComparisonModal(selectedSupplements);
            }, 50);
        };
    }
    
    console.log('✅ Smart Features Initialized!');
}

// Helper function for category names
function getCategoryName(category) {
    const categories = {
        'بناء-عضلات': 'بناء العضلات',
        'صحة-عامة': 'صحة عامة',
        'تخسيس': 'إنقاص الوزن',
        'طاقة-وأداء': 'طاقة وأداء',
        'فيتامينات': 'فيتامينات ومعادن',
        'صحة-خاصة': 'صحة متخصصة'
    };
    return categories[category] || category;
}

// Auto-initialize with error protection
try {
    initSmartFeatures();
} catch (error) {
    console.error('❌ Smart Features Error:', error);
    // Retry after delay
    setTimeout(() => {
        try {
            initSmartFeatures();
        } catch (e) {
            console.warn('⚠️ Smart Features could not initialize');
        }
    }, 2000);
}
