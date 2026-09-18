/**
 * WiBo Health - Persistent Supplements Compare & Search Fix
 * يحفظ المكملات المختارة في الذاكرة حتى لا تضيع عند استخدام البحث
 */

// ذاكرة الحفظ الذكية للمكملات المختارة
window.selectedSupplements = new Set();

// دالة التبديل لحفظ أو إزالة المكمل في الذاكرة
window.toggleSupplementCompare = function(id, checkbox) {
    id = parseInt(id);
    if (checkbox.checked) {
        if (window.selectedSupplements.size >= 5) {
            checkbox.checked = false;
            alert('يمكنك مقارنة 5 مكملات كحد أقصى');
            return;
        }
        window.selectedSupplements.add(id);
    } else {
        window.selectedSupplements.delete(id);
    }
    window.updateCompareButton();
};

// تحديث زر المقارنة العائم بناءً على عدد المكملات في الذاكرة
window.updateCompareButton = function() {
    const compareBtn = document.getElementById('compareFloatBtn');
    const compareCount = document.getElementById('compareCount');
    if (!compareBtn || !compareCount) return;

    const count = window.selectedSupplements.size;
    if (count >= 2) {
        compareBtn.classList.remove('hidden');
        compareCount.textContent = count;
    } else {
        compareBtn.classList.add('hidden');
    }
};

// إعادة كتابة دالة عرض المكملات لتحافظ على علامة الصح (checked) دائماً
window.displaySupplements = function() {
    const grid = document.getElementById('supplementsGrid');
    const loading = document.querySelector('.loading');
    const noResults = document.getElementById('noResults');
    
    if (loading) loading.classList.remove('show');
    if (typeof supplementsData === 'undefined' || !grid) return;
    
    // تصفية المكملات بناءً على البحث
    const term = (typeof searchTerm !== 'undefined' ? searchTerm : '').toLowerCase().trim();
    
    let filtered = supplementsData.filter(supp => {
        if (!term) return true;
        const nameMatch = supp.name && supp.name.toLowerCase().includes(term);
        const enMatch = supp.englishName && supp.englishName.toLowerCase().includes(term);
        const tagMatch = supp.tags && supp.tags.some(tag => tag.toLowerCase().includes(term));
        return nameMatch || enMatch || tagMatch;
    });
    
    if (filtered.length === 0) {
        if (noResults) noResults.classList.add('show');
        grid.innerHTML = '';
        return;
    } else {
        if (noResults) noResults.classList.remove('show');
    }
    
    // رسم الكروت مع فحص الذاكرة: هل هذا المكمل محدد مسبقاً؟
    grid.innerHTML = filtered.map(supp => {
        const isChecked = window.selectedSupplements.has(supp.id) ? 'checked' : '';
        const catName = typeof getCategoryName === 'function' ? getCategoryName(supp.category) : supp.category;
        
        return `
        <div class="supplement-card">
            <div class="compare-checkbox-wrapper">
                <input type="checkbox" 
                       class="compare-checkbox" 
                       id="compare-${supp.id}" 
                       value="${supp.id}"
                       ${isChecked}
                       onchange="toggleSupplementCompare(${supp.id}, this)">
                <label for="compare-${supp.id}" class="compare-label">
                    <i class="fas fa-check"></i>
                </label>
            </div>
            <div class="card-content" onclick="openModal(${supp.id})">
                <div class="supplement-header">
                    <div class="supplement-icon">${supp.icon || '💊'}</div>
                    <h3>${supp.name}</h3>
                    <p class="english-name">${supp.englishName || ''}</p>
                </div>
                <div class="supplement-body">
                    <span class="supplement-category">${catName}</span>
                    <p class="supplement-summary">${supp.summary || ''}</p>
                    <div class="supplement-tags">
                        ${(supp.tags || []).map(tag => `<span class="tag">${tag}</span>`).join('')}
                    </div>
                    <div class="supplement-footer">
                        <span class="read-more-btn">
                            اقرأ المزيد
                            <i class="fas fa-arrow-left"></i>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        `;
    }).join('');
};

// فتح نافذة المقارنة وجلب كل المكملات المختارة من الذاكرة
window.openCompareModal = function() {
    if (window.selectedSupplements.size < 2) {
        alert('الرجاء اختيار مكملين على الأقل للمقارنة');
        return;
    }

    const selectedIds = Array.from(window.selectedSupplements);
    const supplements = selectedIds.map(id => 
        supplementsData.find(s => s.id === id)
    ).filter(Boolean);

    if (supplements.length < 2) {
        alert('حدث خطأ في تحميل المكملات');
        return;
    }

    if (typeof displayComparisonTable === 'function') {
        displayComparisonTable(supplements);
    }
    
    const compareModal = document.getElementById('compareModal');
    if (compareModal) {
        compareModal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
};

// إغلاق نافذة المقارنة دون مسح اختيارات المستخدم
window.closeCompareModal = function() {
    const compareModal = document.getElementById('compareModal');
    if (compareModal) {
        compareModal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
};

// إعادة تهيئة فورية
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(window.displaySupplements, 200);
});