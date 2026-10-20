/**
 * WiBo Health - Food master groups (AR / EN / NL)
 * The 10 groups behind the category filter on foods.html. Every record in js/data.js
 * carries one of these keys in its `group` field.
 */

const FOOD_GROUPS = [
    { key: 'fruits',             icon: '🍎', ar: 'الفواكه والتوتيات',               en: 'Fruits & Berries',                nl: 'Fruit & Bessen' },
    { key: 'vegetables',         icon: '🥦', ar: 'الخضروات والسلطات',               en: 'Vegetables & Salads',             nl: 'Groenten & Salades' },
    { key: 'grains_bakery',      icon: '🍞', ar: 'المخبوزات والحبوب والبدائل',       en: 'Breads, Grains & Alternatives',   nl: 'Bakkerij & Granen' },
    { key: 'proteins_legumes',   icon: '🥩', ar: 'البروتينات واللحوم والبقوليات',     en: 'Proteins, Meats & Legumes',       nl: 'Eiwitten & Peulvruchten' },
    { key: 'dairy_alternatives', icon: '🧀', ar: 'الألبان والأجبان والبدائل',        en: 'Dairy, Cheeses & Alternatives',   nl: 'Zuivel & Plantaardig' },
    { key: 'fats_nuts',          icon: '🥑', ar: 'الدهون الصحية والمكسرات والزيوت',   en: 'Healthy Fats, Nuts & Oils',       nl: 'Gezonde Vetten & Noten' },
    { key: 'meals_cuisines',     icon: '🍲', ar: 'الأطباق والشوربات والوجبات',        en: 'Meals, Dishes & Soups',           nl: 'Maaltijden & Soepen' },
    { key: 'snacks_desserts',    icon: '🍰', ar: 'السناكات والحلويات والمحليات',      en: 'Snacks, Desserts & Sweeteners',   nl: 'Snacks & Desserts' },
    { key: 'beverages',          icon: '☕', ar: 'المشروبات الصحية والشاي والقهوة',   en: 'Healthy Beverages & Drinks',      nl: 'Dranken & Thee' },
    { key: 'pantry_spices',      icon: '🧂', ar: 'البهارات والصلصات ومكونات الطهي',   en: 'Spices, Sauces & Pantry',         nl: 'Sauzen & Specerijen' }
];

const FOOD_GROUPS_BY_KEY = Object.fromEntries(FOOD_GROUPS.map(g => [g.key, g]));

/**
 * Label of a master group in the given language ('ar' | 'en' | 'nl'); '' for an unknown key.
 */
function getCategoryLabel(groupKey, lang = 'ar') {
    const group = FOOD_GROUPS_BY_KEY[groupKey];
    if (!group) return '';
    return group[lang] || group.en;
}

if (typeof window !== 'undefined') {
    window.FOOD_GROUPS = FOOD_GROUPS;
    window.getCategoryLabel = getCategoryLabel;
}
