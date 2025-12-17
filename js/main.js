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
    if (foodCounter) {
        foodCounter.textContent = foodsDatabase.length;
    }
    
    // إعداد التنقل
    setupNavigation();
    
    // إعداد التمرير السلس
    setupSmoothScroll();
    
    // إضافة تأثيرات التمرير
    setupScrollAnimations();
}

// ============================================
// إدارة التنقل (Navigation)
// ============================================
function setupNavigation() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // فتح/إغلاق القائمة في الموبايل
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // تغيير الأيقونة
            const icon = this.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // إغلاق القائمة عند النقر على رابط
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // إزالة active من جميع الروابط
            navLinks.forEach(l => l.classList.remove('active'));
            // إضافة active للرابط المنقور
            this.classList.add('active');
            
            // إغلاق القائمة في الموبايل
            if (window.innerWidth <= 768) {
                navMenu.classList.remove('active');
                const icon = menuToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    });
    
    // تفعيل الرابط حسب الموضع في الصفحة
    window.addEventListener('scroll', function() {
        let current = '';
        const sections = document.querySelectorAll('section[id]');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
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
    // تأثير الظهور عند التمرير
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
    
    // إضافة التأثير للعناصر
    const animateElements = document.querySelectorAll('.feature-item, .food-item, .info-card');
    animateElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(element);
    });
    
    // تأثير Auto-hide للقوائم عند التمرير
    const header = document.querySelector('.header');
    const quickNav = document.querySelector('.quick-nav');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        // Auto-hide: إخفاء القوائم عند السحب لأسفل، إظهارها عند السحب لأعلى
        if (currentScroll > lastScroll && currentScroll > 150) {
            // السحب لأسفل - إخفاء القوائم
            if (quickNav) {
                quickNav.style.transform = 'translateY(-120%)';
                quickNav.style.transition = 'transform 0.3s ease';
            }
        } else {
            // السحب لأعلى - إظهار القوائم
            if (quickNav) {
                quickNav.style.transform = 'translateY(0)';
                quickNav.style.transition = 'transform 0.3s ease';
            }
        }
        
        // تأثير تصغير الهيدر
        if (currentScroll > 100) {
            header.style.padding = '0.5rem 0';
            header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
        } else {
            header.style.padding = '1rem 0';
            header.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
        }
        
        lastScroll = currentScroll;
    });
}

// ============================================
// تحميل وعرض الأطعمة
// ============================================
function loadFoodGrid() {
    const foodGrid = document.getElementById('foodGrid');
    if (!foodGrid) return;
    
    // الحصول على جميع الفئات المتاحة
    const categories = getCategories();
    
    // عرض عينات من كل فئة (3-4 أطعمة من كل فئة)
    const foodsToDisplay = [];
    categories.forEach(category => {
        const categoryFoods = foodsDatabase.filter(food => food.category === category);
        // أخذ أول 3 عناصر من كل فئة
        const samples = categoryFoods.slice(0, 3);
        foodsToDisplay.push(...samples);
    });
    
    // خلط العينات بشكل عشوائي لعرض متنوع
    const shuffled = foodsToDisplay.sort(() => Math.random() - 0.5);
    // عرض أول 24 عنصر من العينات المخلوطة
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
    
    const giLevel = getIndexLevel(food.gi);
    const iiLevel = getIndexLevel(food.ii);
    
    // Get current language
    const currentLang = (window.UnifiedLanguageSystem && window.UnifiedLanguageSystem.currentLang) || 'ar';
    
    // Get translated content
    const foodName = currentLang === 'en' ? (food.nameEn || food.name) : food.name;
    const foodCategory = currentLang === 'en' ? (food.categoryEn || food.category) : food.category;
    const indexLevelText = getIndexLevelText(food.gi, currentLang);
    const indexLevelText2 = getIndexLevelText(food.ii, currentLang);
    
    // Translated labels
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
    
    card.innerHTML = `
        <div class="food-header">
            <span class="food-icon">${food.icon}</span>
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
                <span class="nutrition-value">${food.nutrition.calories} ${labels.kcal}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.protein}</span>
                <span class="nutrition-value">${food.nutrition.protein} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.carbs}</span>
                <span class="nutrition-value">${food.nutrition.carbs} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.fats}</span>
                <span class="nutrition-value">${food.nutrition.fat} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.fiber}</span>
                <span class="nutrition-value">${food.nutrition.fiber} ${labels.g}</span>
            </div>
            <div class="nutrition-item">
                <span>${labels.category}</span>
                <span class="nutrition-value">${foodCategory}</span>
            </div>
        </div>
    `;
    
    // إضافة تأثير النقر
    card.addEventListener('click', function() {
        showFoodDetails(food);
    });
    
    return card;
}

/**
 * عرض تفاصيل الطعام في نافذة منبثقة
 */
function showFoodDetails(food) {
    // يمكن إضافة نافذة منبثقة مع تفاصيل أكثر
    console.log('عرض تفاصيل:', food.name);
    // TODO: إضافة modal لتفاصيل الطعام
}

// ============================================
// البحث والفلترة
// ============================================
function filterFoods() {
    const searchInput = document.getElementById('foodSearch');
    const foodGrid = document.getElementById('foodGrid');
    const foodCounter = document.getElementById('foodCounter');
    
    if (!searchInput || !foodGrid) return;
    
    const searchTerm = searchInput.value.toLowerCase().trim();
    
    // إذا كان البحث فارغاً، نعرض العينات
    if (searchTerm === '') {
        loadFoodGrid();
        if (foodCounter) foodCounter.textContent = foodsDatabase.length;
        return;
    }
    
    // تصفية الأطعمة
    const filteredFoods = filterFoodsBySearch(searchTerm);
    
    // تحديث العداد
    if (foodCounter) {
        foodCounter.textContent = filteredFoods.length;
    }
    
    // عرض النتائج
    foodGrid.innerHTML = '';
    
    if (filteredFoods.length === 0) {
        // Get current language
        const currentLang = (window.UnifiedLanguageSystem && window.UnifiedLanguageSystem.currentLang) || 'ar';
        const noResultsText = currentLang === 'en' ? `No results found for "${searchTerm}"` : `لم يتم العثور على نتائج لـ "${searchTerm}"`;
        const tryAgainText = currentLang === 'en' ? 'Try searching with different keywords' : 'جرب البحث بكلمة أخرى';
        const clearButtonText = currentLang === 'en' ? '<i class="fas fa-redo"></i> Clear search and show samples' : '<i class="fas fa-redo"></i> مسح البحث وعرض العينات';
        
        foodGrid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 3rem;">
                <i class="fas fa-search" style="font-size: 4rem; color: var(--gray-300); margin-bottom: 1rem;"></i>
                <p style="font-size: 1.25rem; color: var(--gray-600);">${noResultsText}</p>
                <p style="color: var(--gray-500);">${tryAgainText}</p>
                <button onclick="document.getElementById('foodSearch').value=''; filterFoods();" style="margin-top: 1rem; padding: 0.75rem 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 50px; cursor: pointer; font-size: 1rem; font-weight: 600;">
                    ${clearButtonText}
                </button>
            </div>
        `;
    } else {
        // عرض أول 50 نتيجة لتحسين الأداء
        const resultsToShow = filteredFoods.slice(0, 50);
        resultsToShow.forEach(food => {
            const foodCard = createFoodCard(food);
            foodGrid.appendChild(foodCard);
        });
        
        // إذا كان هناك المزيد من النتائج
        if (filteredFoods.length > 50) {
            const currentLang = (window.UnifiedLanguageSystem && window.UnifiedLanguageSystem.currentLang) || 'ar';
            const showingText = currentLang === 'en' ? `Showing first 50 results of ${filteredFoods.length} items` : `يتم عرض أول 50 نتيجة من ${filteredFoods.length} عنصر`;
            const refineText = currentLang === 'en' ? 'Refine your search for more specific results' : 'حدد كلمات البحث للحصول على نتائج أدق';
            
            const moreDiv = document.createElement('div');
            moreDiv.style.cssText = 'grid-column: 1 / -1; text-align: center; padding: 2rem;';
            moreDiv.innerHTML = `
                <p style="color: var(--gray-600); font-size: 1.1rem;">
                    <i class="fas fa-info-circle"></i> 
                    ${showingText}
                </p>
                <p style="color: var(--gray-500); margin-top: 0.5rem;">${refineText}</p>
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
        
        // إضافة تأثير الظهور
        setTimeout(() => {
            modal.querySelector('.modal-content').style.animation = 'slideDown 0.3s ease';
        }, 10);
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.querySelector('.modal-content').style.animation = 'slideUp 0.3s ease';
        
        setTimeout(() => {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }, 300);
    }
}

// إغلاق النافذة المنبثقة عند النقر خارجها
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            if (event.target === modal) {
                closeModal(modal.id);
            }
        });
    }
}

// إغلاق النافذة المنبثقة بزر ESC
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

// ============================================
// تأثيرات إضافية
// ============================================

// تأثير القلوب المتحركة للإهداء
function createHeartAnimation() {
    const dedication = document.querySelector('.dedication');
    if (!dedication) return;
    
    dedication.addEventListener('mouseenter', function() {
        // إنشاء قلوب متحركة
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                const heart = document.createElement('span');
                heart.innerHTML = '💚';
                heart.style.position = 'absolute';
                heart.style.fontSize = '1.5rem';
                heart.style.animation = 'floatHeart 2s ease-out forwards';
                heart.style.left = `${Math.random() * 100}%`;
                heart.style.pointerEvents = 'none';
                
                this.appendChild(heart);
                
                setTimeout(() => {
                    heart.remove();
                }, 2000);
            }, i * 100);
        }
    });
}

// إضافة أنيميشن للقلوب
const heartAnimationStyle = document.createElement('style');
heartAnimationStyle.textContent = `
    @keyframes floatHeart {
        0% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
        100% {
            opacity: 0;
            transform: translateY(-100px) scale(1.5);
        }
    }
    
    @keyframes slideUp {
        from {
            opacity: 1;
            transform: translateY(0);
        }
        to {
            opacity: 0;
            transform: translateY(-50px);
        }
    }
`;
document.head.appendChild(heartAnimationStyle);

// تفعيل تأثير القلوب
setTimeout(createHeartAnimation, 1000);

// ============================================
// دالة للطباعة (إذا كانت مطلوبة)
// ============================================
function printFoodInfo(foodId) {
    const food = foodsDatabase.find(f => f.id === foodId);
    if (!food) return;
    
    const printWindow = window.open('', '_blank');
    printWindow.document.write(`
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>${food.name} - WiBo Health</title>
            <style>
                body {
                    font-family: 'Cairo', Arial, sans-serif;
                    padding: 2rem;
                    direction: rtl;
                }
                h1 { color: #4ade80; }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 1rem;
                }
                td, th {
                    border: 1px solid #ddd;
                    padding: 0.75rem;
                    text-align: right;
                }
                th { background-color: #f0f0f0; }
            </style>
        </head>
        <body>
            <h1>${food.icon} ${food.name}</h1>
            <h2>المؤشرات الصحية</h2>
            <table>
                <tr>
                    <th>المؤشر</th>
                    <th>القيمة</th>
                    <th>المستوى</th>
                </tr>
                <tr>
                    <td>الجلايسيميك إندكس (GI)</td>
                    <td>${food.gi}</td>
                    <td>${getIndexLevelText(food.gi)}</td>
                </tr>
                <tr>
                    <td>الإنسولين إندكس (II)</td>
                    <td>${food.ii}</td>
                    <td>${getIndexLevelText(food.ii)}</td>
                </tr>
            </table>
            
            <h2>المعلومات الغذائية</h2>
            <table>
                <tr>
                    <th>العنصر</th>
                    <th>القيمة</th>
                </tr>
                <tr>
                    <td>السعرات الحرارية</td>
                    <td>${food.nutrition.calories} كيلو كالوري</td>
                </tr>
                <tr>
                    <td>البروتين</td>
                    <td>${food.nutrition.protein} جرام</td>
                </tr>
                <tr>
                    <td>الكربوهيدرات</td>
                    <td>${food.nutrition.carbs} جرام</td>
                </tr>
                <tr>
                    <td>الدهون</td>
                    <td>${food.nutrition.fat} جرام</td>
                </tr>
                <tr>
                    <td>الألياف</td>
                    <td>${food.nutrition.fiber} جرام</td>
                </tr>
            </table>
            
            <p style="margin-top: 2rem; color: #666; font-size: 0.875rem;">
                مطبوع من WiBo Health - دليلك الصحي الشامل
            </p>
            
            <script>
                window.onload = function() {
                    window.print();
                }
            </script>
        </body>
        </html>
    `);
    printWindow.document.close();
}

// ============================================
// تصدير الدوال للاستخدام العام
// ============================================
window.openModal = openModal;
window.closeModal = closeModal;
window.filterFoods = filterFoods;
window.printFoodInfo = printFoodInfo;