/**
 * Script to add categoryEn to all food items in data.js
 * This script will be used to generate the updated data.js file
 */

// Categories Translation Map
const categoriesMap = {
    'حبوب': 'Grains',
    'بقوليات': 'Legumes',
    'فواكه': 'Fruits',
    'خضروات': 'Vegetables',
    'ألبان': 'Dairy',
    'مكسرات': 'Nuts',
    'بروتين': 'Protein',
    'سكريات': 'Sweets',
    'مشروبات': 'Beverages',
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

// Function to add categoryEn to a food item
function addCategoryEn(foodItem) {
    const categoryAr = foodItem.category;
    const categoryEn = categoriesMap[categoryAr] || categoryAr;
    return {
        ...foodItem,
        categoryEn: categoryEn
    };
}

// Usage instructions:
console.log('=== Instructions ===');
console.log('1. Load data.js in browser console');
console.log('2. Run: const updatedData = foodsDatabase.map(addCategoryEn);');
console.log('3. Copy output and save to data.js');
console.log('');
console.log('Categories Map:', categoriesMap);
