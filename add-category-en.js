/**
 * Script to add categoryEn field after every category field in data.js
 * This uses regex replacement to add the translation automatically
 */

const fs = require('fs');

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
    'ماكدونالدز': 'McDonald\\\'s',
    'كنتاكي': 'KFC',
    'بيتزا هت': 'Pizza Hut',
    'صب واي': 'Subway',
    'برجر كنج': 'Burger King',
    'هارديز': 'Hardee\\\'s',
    'دومينوز': 'Domino\\\'s',
    'بابا جونز': 'Papa John\\\'s',
    'دانكن': 'Dunkin\\\'',
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

// Read data.js file content
let content = fs.readFileSync('js/data.js', 'utf8');

// For each category in the map, add categoryEn after it
Object.entries(categoriesMap).forEach(([categoryAr, categoryEn]) => {
    // Pattern: category: 'حبوب',
    // Replace with: category: 'حبوب',\n        categoryEn: 'Grains',
    const pattern = new RegExp(`category: '${categoryAr}',`, 'g');
    const replacement = `category: '${categoryAr}',\n        categoryEn: '${categoryEn}',`;
    content = content.replace(pattern, replacement);
});

// Write updated content back to file
fs.writeFileSync('js/data.js', content, 'utf8');

console.log('✅ Successfully added categoryEn to all items in data.js');
console.log('Categories translated:', Object.keys(categoriesMap).length);
