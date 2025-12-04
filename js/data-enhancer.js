/**
 * WiBo Health - Data Enhancer
 * Automatically adds categoryEn to all food items
 * This script runs after data.js loads and enhances the data
 */

(function() {
    'use strict';

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

    /**
     * Enhance foodsDatabase with categoryEn
     */
    function enhanceFoodsDatabase() {
        if (typeof window.foodsDatabase === 'undefined') {
            // Silently exit - Normal for pages that don't use foodsDatabase (like index.html)
            return false;
        }

        let enhanced = 0;
        window.foodsDatabase.forEach(food => {
            if (!food.categoryEn && food.category) {
                food.categoryEn = categoriesMap[food.category] || food.category;
                enhanced++;
            }
        });

        console.log(`✅ Data Enhancer: Added categoryEn to ${enhanced} food items`);
        return true;
    }

    /**
     * Initialize when DOM is ready
     */
    function init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                setTimeout(enhanceFoodsDatabase, 100);
            });
        } else {
            setTimeout(enhanceFoodsDatabase, 100);
        }
    }

    // Auto-initialize
    init();

    // Expose to window for manual use
    window.enhanceFoodsDatabase = enhanceFoodsDatabase;
    window.categoriesMap = categoriesMap;

})();
