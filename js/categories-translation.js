/**
 * WiBo Health - Categories Translation Map
 * جدول ترجمة شامل لجميع فئات الأطعمة
 */

const categoriesTranslation = {
    // الفئات الأساسية
    'حبوب': 'Grains',
    'بقوليات': 'Legumes',
    'فواكه': 'Fruits',
    'خضروات': 'Vegetables',
    'ألبان': 'Dairy',
    'مكسرات': 'Nuts',
    'بروتين': 'Protein',
    'سكريات': 'Sweets',
    'مشروبات': 'Beverages',
    
    // مطاعم الوجبات السريعة
    'ماكدونالدز': 'McDonald\'s',
    'كنتاكي': 'KFC',
    'بيتزا هت': 'Pizza Hut',
    'صب واي': 'Subway',
    'برجر كنج': 'Burger King',
    'هارديز': 'Hardee\'s',
    'دومينوز': 'Domino\'s',
    'بابا جونز': 'Papa John\'s',
    'دانكن': 'Dunkin\'',
    'ستاربكس': 'Starbucks',
    
    // فئات إضافية
    'معلبات': 'Canned Foods',
    'سناكس': 'Snacks',
    'زيوت': 'Oils',
    'أطعمة آسيوية': 'Asian Foods',
    'أطعمة عربية': 'Arab Foods',
    'أطعمة إيطالية': 'Italian Foods',
    'أطعمة مكسيكية': 'Mexican Foods',
    'مخبوزات': 'Baked Goods',
    'حلويات': 'Desserts',
    'إفطار': 'Breakfast',
    'سلطات': 'Salads',
    'شوربات': 'Soups',
    'صلصات': 'Sauces',
    'توابل': 'Spices',
    'مقبلات': 'Appetizers',
    'مخللات': 'Pickles',
    'مقليات': 'Fried Foods',
    'مشويات': 'Grilled Foods',
    'بحرية': 'Seafood',
    'لحوم': 'Meats',
    'دواجن': 'Poultry',
    'أعشاب': 'Herbs',
    'بذور': 'Seeds',
    'فطر': 'Mushrooms',
    'حبوب إفطار': 'Breakfast Cereals',
    'معجنات': 'Pastries',
    'أرز': 'Rice',
    'باستا': 'Pasta'
};

/**
 * دالة للحصول على ترجمة الفئة
 */
function getCategoryTranslation(categoryAr, lang = 'en') {
    if (lang === 'ar') return categoryAr;
    return categoriesTranslation[categoryAr] || categoryAr;
}

/**
 * دالة للحصول على الفئة بحسب اللغة الحالية
 */
function getCategoryByLang(categoryAr, categoryEn, lang = 'ar') {
    return lang === 'en' ? categoryEn : categoryAr;
}

// Export for use in other scripts
if (typeof window !== 'undefined') {
    window.categoriesTranslation = categoriesTranslation;
    window.getCategoryTranslation = getCategoryTranslation;
    window.getCategoryByLang = getCategoryByLang;
}
