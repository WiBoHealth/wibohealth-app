/**
 * WiBo Health - Food master groups (AR / EN / NL)
 * The 10 groups behind the category filter on foods.html (color = the card accent there). Every record in js/data.js
 * carries one of these keys in its `group` field.
 */

const FOOD_GROUPS = [
    { key: 'fruits',             color: '#ef4444', icon: '🍎', ar: 'الفواكه والتوتيات',               en: 'Fruits & Berries',                nl: 'Fruit & Bessen' },
    { key: 'vegetables',         color: '#22c55e', icon: '🥦', ar: 'الخضروات والسلطات',               en: 'Vegetables & Salads',             nl: 'Groenten & Salades' },
    { key: 'grains_bakery',      color: '#d97706', icon: '🍞', ar: 'المخبوزات والحبوب والبدائل',       en: 'Breads, Grains & Alternatives',   nl: 'Bakkerij & Granen' },
    { key: 'proteins_legumes',   color: '#e11d48', icon: '🥩', ar: 'البروتينات واللحوم والبقوليات',     en: 'Proteins, Meats & Legumes',       nl: 'Eiwitten & Peulvruchten' },
    { key: 'dairy_alternatives', color: '#0ea5e9', icon: '🧀', ar: 'الألبان والأجبان والبدائل',        en: 'Dairy, Cheeses & Alternatives',   nl: 'Zuivel & Plantaardig' },
    { key: 'fats_nuts',          color: '#65a30d', icon: '🥑', ar: 'الدهون الصحية والمكسرات والزيوت',   en: 'Healthy Fats, Nuts & Oils',       nl: 'Gezonde Vetten & Noten' },
    { key: 'meals_cuisines',     color: '#f97316', icon: '🍲', ar: 'الأطباق والشوربات والوجبات',        en: 'Meals, Dishes & Soups',           nl: 'Maaltijden & Soepen' },
    { key: 'snacks_desserts',    color: '#db2777', icon: '🍰', ar: 'السناكات والحلويات والمحليات',      en: 'Snacks, Desserts & Sweeteners',   nl: 'Snacks & Desserts' },
    { key: 'beverages',          color: '#8b5cf6', icon: '☕', ar: 'المشروبات الصحية والشاي والقهوة',   en: 'Healthy Beverages & Drinks',      nl: 'Dranken & Thee' },
    { key: 'pantry_spices',      color: '#0d9488', icon: '🧂', ar: 'البهارات والصلصات ومكونات الطهي',   en: 'Spices, Sauces & Pantry',         nl: 'Sauzen & Specerijen' }
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
