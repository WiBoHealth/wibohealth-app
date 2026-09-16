/**
 * WiBo Health - Main JavaScript
 * الوظائف التفاعلية الرئيسية للموقع
 */

// ============================================
// التهيئة عند تحميل الصفحة
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // تحميل قائمة الأطعمة
    loadFoodGrid();
    
    // تحديث عداد الأطعمة
    const foodCounter = document.getElementById('foodCounter');
    if (foodCounter && typeof foodsDatabase !== 'undefined') {
        foodCounter.textContent = foodsDatabase.length;
    }
    
    // إعداد التنقل
    setupNavigation();
    
    // إعداد التمرير السلس
    setupSmoothScroll();
    
    // إضافة تأثيرات التمرير
    setupScrollAnimations();

    // تحديث شبكة الأطعمة فوراً وبشكل حي عند تبديل اللغة
    window.addEventListener('languageChanged', function() {
        loadFoodGrid();
    });
}

// ============================================
// إدارة التنقل (Navigation)
// ============================================
function setupNavigation() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // فتح/إغلاق القائمة في الموبايل
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            const icon = this.querySelector('i');
            if (icon) {
                if (navMenu.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }
    
    // إغلاق القائمة عند النقر على رابط
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            
            if (window.innerWidth <= 768 && navMenu && menuToggle) {
                navMenu.classList.remove('active');
                const icon = menuToggle.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    });
    
    // تفعيل الرابط حسب الموضع في الصفحة
    window.addEventListener('scroll', function() {
        let current = '';
        const sections = document.querySelectorAll('section[id]');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}

// ============================================
// التمرير السلس
// ============================================
function setupSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.offsetTop;
                const offsetPosition = elementPosition - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ============================================
// تأثيرات التمرير
// ============================================
function setupScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    const animateElements = document.querySelectorAll('.feature-item, .food-item, .info-card');
    animateElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(element);
    });
    
    const header = document.querySelector('.header');
    const quickNav = document.querySelector('.quick-nav');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > lastScroll && currentScroll > 150) {
            if (quickNav) {
                quickNav.style.transform = 'translateY(-120%)';
                quickNav.style.transition = 'transform 0.3s ease';
            }
        } else {
            if (quickNav) {
                quickNav.style.transform = 'translateY(0)';
                quickNav.style.transition = 'transform 0.3s ease';
            }
        }
        
        if (header) {
            if (currentScroll > 100) {
                header.style.padding = '0.5rem 0';
                header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
            } else {
                header.style.padding = '1rem 0';
                header.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
            }
        }
        
        lastScroll = currentScroll;
    });
}

// ============================================
// تحميل وعرض الأطعمة
// ============================================
function loadFoodGrid() {
    const foodGrid = document.getElementById('foodGrid');
    if (!foodGrid || typeof foodsDatabase === 'undefined') return;
    
    const categories = typeof getCategories === 'function' ? getCategories() : [];
    const foodsToDisplay = [];
    
    if (categories.length > 0) {
        categories.forEach(category => {
            const categoryFoods = foodsDatabase.filter(food => food.category === category);
            const samples = categoryFoods.slice(0, 3);
            foodsToDisplay.push(...samples);
        });
    } else {
        foodsToDisplay.push(...foodsDatabase.slice(0, 24));
    }
    
    const shuffled = foodsToDisplay.sort(() => Math.random() - 0.5);
    const finalDisplay = shuffled.slice(0, 24);
    
    foodGrid.innerHTML = '';
    
    finalDisplay.forEach(food => {
        const foodCard = createFoodCard(food);
        foodGrid.appendChild(foodCard);
    });
}

/**
 * إنشاء بطاقة طعام
 */
function createFoodCard(food) {
    const card = document.createElement('div');
    card.className = 'food-item';
    card.setAttribute('data-food-id', food.id);
    
    const giLevel = typeof getIndexLevel === 'function' ? getIndexLevel(food.gi) : '';
    const iiLevel = typeof getIndexLevel === 'function' ? getIndexLevel(food.ii) : '';
    
    const currentLang = localStorage.getItem('preferred_language') || 'ar';
    
    const foodName = currentLang === 'en' ? (food.nameEn || food.name) : food.name;
    const foodCategory = currentLang === 'en' ? (food.categoryEn || food.category) : food.category;
    
    const indexLevelText = typeof getIndexLevelText === 'function' ? getIndexLevelText(food.gi, currentLang) : '';
    const indexLevelText2 = typeof getIndexLevelText === 'function' ? getIndexLevelText(food.ii, currentLang) : '';
    
    const labels = currentLang === 'en' ? {
        gi: 'GI - Glycemic',
        ii: 'II - Insulin',
        calories: 'Calories',
        protein: 'Protein',
        carbs: 'Carbs',
        fats: 'Fats',
        fiber: 'Fiber',
        category: 'Category',
        kcal: 'kcal',
        g: 'g'
    } : {
        gi: 'GI - جلايسيميك',
        ii: 'II - إنسولين',
        calories: 'سعرات حرارية',
        protein: 'بروتين',
        carbs: 'كربوهيدرات',
        fats: 'دهون',
        fiber: 'ألياف',
        category: 'الفئة',
        kcal: 'كيلو كالوري',
        g: 'جم'
    };
    
    const cal = (food.nutrition && food.nutrition.calories) ? food.nutrition.calories : (food.calories || 0);
    const protein = (food.nutrition && food.nutrition.protein) ? food.nutrition.protein : (food.protein || 0);
    const carbs = (food.nutrition && food.nutrition.carbs) ? food.nutrition.carbs : (food.carbs || 0);
    const fat = (food.nutrition && food.nutrition.fat) ? food.nutrition.fat : (food.fat || 0);
    const fiber = (food.nutrition && food.nutrition.fiber) ? food.nutrition.fiber : (food.fiber || 0);
    
    card.innerHTML = `
        <div class="food-header">
            <span class="food-icon">${food.icon || '🥗'}</span>
            <h3 class="food-name">${foodName}</h3>
        </div>
        
        <div class="food-indexes">
            <div class="index-badge ${giLevel}">
                <small>${labels.gi}</small>
                <span class="index-value">${food.gi}</span>
                <small>${indexLevelText}</small>
            </div>
            <div class="index-badge ${iiLevel}">
                <small>${labels.ii}</small>
                <span class="index-value">${food.ii}</span>
                <small>${indexLevelText2}</small>
            </div>
        </div>
        
        <div class="nutrition-info">
            <div class="nutrition-item">
                <span>${labels.calories}</span>
                <span class="nutrition-value">${cal} ${labels.kcal}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.protein}</span>
                <span class="nutrition-value">${protein} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.carbs}</span>
                <span class="nutrition-value">${carbs} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.fats}</span>
                <span class="nutrition-value">${fat} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.fiber}</span>
                <span class="nutrition-value">${fiber} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.category}</span>
                <span class="nutrition-value">${foodCategory}</span>
            </div>
        </div>
    `;
    
    card.addEventListener('click', function() {
        showFoodDetails(food);
    });
    
    return card;
}

function showFoodDetails(food) {
    console.log('عرض تفاصيل:', food.name);
}

// ============================================
// البحث والفلترة
// ============================================
function filterFoods() {
    const searchInput = document.getElementById('foodSearch');
    const foodGrid = document.getElementById('foodGrid');
    const foodCounter = document.getElementById('foodCounter');
    
    if (!searchInput || !foodGrid || typeof foodsDatabase === 'undefined') return;
    
    const searchTerm = searchInput.value.toLowerCase().trim();
    
    if (searchTerm === '') {
        loadFoodGrid();
        if (foodCounter) foodCounter.textContent = foodsDatabase.length;
        return;
    }
    
    const filteredFoods = typeof filterFoodsBySearch === 'function' ? filterFoodsBySearch(searchTerm) : [];
    
    if (foodCounter) {
        foodCounter.textContent = filteredFoods.length;
    }
    
    foodGrid.innerHTML = '';
    
    if (filteredFoods.length === 0) {
        const currentLang = localStorage.getItem('preferred_language') || 'ar';
        const noResultsText = currentLang === 'en' ? `No results found for "${searchTerm}"` : `لم يتم العثور على نتائج لـ "${searchTerm}"`;
        const tryAgainText = currentLang === 'en' ? 'Try searching with different keywords' : 'جرب البحث بكلمة أخرى';
        const clearButtonText = currentLang === 'en' ? '<i class="fas fa-redo"></i> Clear search and show samples' : '<i class="fas fa-redo"></i> مسح البحث وعرض العينات';
        
        foodGrid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 3rem;">
                <i class="fas fa-search" style="font-size: 4rem; color: #cbd5e1; margin-bottom: 1rem;"></i>
                <p style="font-size: 1.25rem; color: #475569;">${noResultsText}</p>
                <p style="color: #64748b;">${tryAgainText}</p>
                <button onclick="document.getElementById('foodSearch').value=''; filterFoods();" style="margin-top: 1rem; padding: 0.75rem 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 50px; cursor: pointer; font-size: 1rem; font-weight: 600;">
                    ${clearButtonText}
                </button>
            </div>
        `;
    } else {
        const resultsToShow = filteredFoods.slice(0, 50);
        resultsToShow.forEach(food => {
            const foodCard = createFoodCard(food);
            foodGrid.appendChild(foodCard);
        });
        
        if (filteredFoods.length > 50) {
            const currentLang = localStorage.getItem('preferred_language') || 'ar';
            const showingText = currentLang === 'en' ? `Showing first 50 results of ${filteredFoods.length} items` : `يتم عرض أول 50 نتيجة من ${filteredFoods.length} عنصر`;
            const refineText = currentLang === 'en' ? 'Refine your search for more specific results' : 'حدد كلمات البحث للحصول على نتائج أدق';
            
            const moreDiv = document.createElement('div');
            moreDiv.style.cssText = 'grid-column: 1 / -1; text-align: center; padding: 2rem;';
            moreDiv.innerHTML = `
                <p style="color: #475569; font-size: 1.1rem;">
                    <i class="fas fa-info-circle"></i> 
                    ${showingText}
                </p>
                <p style="color: #64748b; margin-top: 0.5rem;">${refineText}</p>
            `;
            foodGrid.appendChild(moreDiv);
        }
    }
}

// ============================================
// إدارة النوافذ المنبثقة (Modals)
// ============================================
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            if (event.target === modal) {
                closeModal(modal.id);
            }
        });
    }
};

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            if (modal.style.display === 'block') {
                closeModal(modal.id);
            }
        });
    }
});

// تصدير الدوال للاستخدام العام
window.openModal = openModal;
window.closeModal = closeModal;
window.filterFoods = filterFoods;