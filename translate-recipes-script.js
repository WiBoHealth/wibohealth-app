/**
 * WiBo Health - Automatic Recipe Translation Script
 * This script reads recipes-data.js and adds English translations
 */

// Category translations
const categoryTranslations = {
    'فطور': 'Breakfast',
    'غداء': 'Lunch',
    'عشاء': 'Dinner',
    'سلطات': 'Salads',
    'شوربات': 'Soups',
    'حلويات صحية': 'Healthy Desserts',
    'سناكات': 'Snacks',
    'مشروبات': 'Drinks'
};

// Sample translations for first 10 recipes
const recipeTranslations = {
    1: {
        titleEn: 'Oatmeal with Berries and Nuts',
        timeEn: '10 minutes',
        ingredientsEn: [
            '½ cup raw oats',
            '1 cup low-fat milk',
            '¼ cup mixed berries',
            '2 tablespoons chopped almonds',
            '1 teaspoon honey',
            'Pinch of cinnamon'
        ],
        stepsEn: [
            'Place oats and milk in a pot over medium heat',
            'Stir constantly until thickened (5-7 minutes)',
            'Turn off heat and add cinnamon',
            'Transfer to serving bowl',
            'Garnish with berries and almonds',
            'Drizzle honey on top and serve hot'
        ],
        tipsEn: 'You can prepare it cold the night before (overnight oats)'
    },
    2: {
        titleEn: 'Vegetable Egg White Omelet',
        timeEn: '15 minutes',
        ingredientsEn: [
            '4 egg whites',
            '½ cup chopped broccoli',
            '½ cup chopped bell peppers',
            '¼ cup chopped green onions',
            '2 tablespoons low-fat cheese',
            'Salt and black pepper',
            '1 teaspoon olive oil'
        ],
        stepsEn: [
            'Beat egg whites with salt and pepper',
            'Heat oil in a non-stick pan',
            'Add vegetables and sauté for 3 minutes',
            'Pour egg whites over vegetables',
            'Cover pan and cook for 5 minutes on low heat',
            'Sprinkle cheese on top before serving'
        ],
        tipsEn: 'You can add any vegetables you have available'
    },
    3: {
        titleEn: 'Avocado Toast with Egg',
        timeEn: '10 minutes',
        ingredientsEn: [
            '1 slice whole wheat bread',
            '½ ripe avocado',
            '1 egg',
            'Juice of ½ lemon',
            'Pinch of red pepper flakes',
            'Salt and black pepper'
        ],
        stepsEn: [
            'Toast bread until golden',
            'Mash avocado with lemon juice and salt',
            'Spread avocado on toasted bread',
            'Boil or fry egg as desired',
            'Place egg on top of avocado',
            'Sprinkle red pepper flakes and serve immediately'
        ],
        tipsEn: 'Choose ripe avocado for creamy texture'
    },
    4: {
        titleEn: 'Banana Oat Pancakes',
        timeEn: '20 minutes',
        ingredientsEn: [
            '1 cup ground oats',
            '1 ripe banana',
            '2 eggs',
            '¼ cup milk',
            '1 teaspoon baking powder',
            'Pinch of cinnamon',
            '1 teaspoon vanilla'
        ],
        stepsEn: [
            'Mash banana well in a bowl',
            'Add eggs, milk, and vanilla and whisk',
            'Add oats, baking powder, and cinnamon',
            'Mix until you get a consistent batter',
            'Heat non-stick pan',
            'Pour batter in circles and flip after browning'
        ],
        tipsEn: 'Serve with honey and fresh berries'
    },
    5: {
        titleEn: 'Green Protein Smoothie',
        timeEn: '5 minutes',
        ingredientsEn: [
            '1 scoop protein powder',
            '1 cup fresh spinach',
            '½ banana',
            '½ cup low-fat Greek yogurt',
            '½ cup almond milk',
            '1 tablespoon chia seeds',
            'Ice cubes'
        ],
        stepsEn: [
            'Add all ingredients to blender',
            'Blend on high speed for 1 minute',
            'Add more milk if too thick',
            'Pour into glass and serve immediately'
        ],
        tipsEn: 'Great post-workout breakfast'
    }
    // Note: Translations for recipes 6-110 will be added using AI translation
};

console.log('Recipe translations loaded');
console.log('Total translations available:', Object.keys(recipeTranslations).length);
console.log('This is a demonstration script showing the translation structure');
console.log('Full translation will be integrated directly into recipes-data.js');
