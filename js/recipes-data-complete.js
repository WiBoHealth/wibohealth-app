/**
 * WiBo Health - Complete Recipes Database Loader
 * قاعدة بيانات الوصفات الكاملة - المحمّل
 * Bilingual: Arabic & English
 * Total: 110 Recipes (IDs: 1-110)
 * 
 * Categories:
 * - Healthy Breakfast (فطور صحي)
 * - Salads (سلطات)
 * - Soups (شوربات)
 * - Main Dishes (أطباق رئيسية)
 * - Healthy Snacks (سناكات صحية)
 * - Healthy Desserts (حلويات صحية)
 * - Arabic Dishes (أطباق عربية)
 * - Snacks/Diet (وجبات خفيفة/دايت)
 * 
 * Last Updated: 2025-01-29
 * 
 * Structure:
 * - Part 1: Recipes 1-20 (20 recipes)
 * - Part 2: Recipes 21-35 (15 recipes)
 * - Part 3: Recipes 36-55 (20 recipes)
 * - Part 4: Recipes 56-70 (15 recipes)
 * - Part 5: Recipes 71-91 (21 recipes)
 * - Part 6: Recipes 92-110 (19 recipes)
 * Total: 110 recipes
 */

// Initialize complete recipes database
let recipesDatabase = [];

// Function to merge all recipe parts
function mergeRecipesParts() {
    // Check if all parts are loaded
    if (typeof recipesDatabase_Part1 === 'undefined' ||
        typeof recipesDatabase_Part2 === 'undefined' ||
        typeof recipesDatabase_Part3 === 'undefined' ||
        typeof recipesDatabase_Part4 === 'undefined' ||
        typeof recipesDatabase_Part5 === 'undefined' ||
        typeof recipesDatabase_Part6 === 'undefined') {
        console.error('❌ Not all recipe parts are loaded!');
        return [];
    }
    
    // Merge all parts in order
    recipesDatabase = [
        ...recipesDatabase_Part1,  // 1-20
        ...recipesDatabase_Part2,  // 21-35
        ...recipesDatabase_Part3,  // 36-55
        ...recipesDatabase_Part4,  // 56-70
        ...recipesDatabase_Part5,  // 71-91
        ...recipesDatabase_Part6   // 92-110
    ];
    
    // Validate merged database
    console.log('✅ Complete WiBo Health Recipes Database loaded: ' + recipesDatabase.length + ' recipes');
    
    // Verify recipe IDs are sequential
    const expectedIds = Array.from({length: 110}, (_, i) => i + 1);
    const actualIds = recipesDatabase.map(r => r.id).sort((a, b) => a - b);
    const allIdsValid = expectedIds.every((id, i) => id === actualIds[i]);
    
    if (allIdsValid) {
        console.log('✅ All recipe IDs are sequential (1-110)');
    } else {
        console.warn('⚠️ Warning: Some recipe IDs might be missing or duplicated');
    }
    
    // Display statistics
    const categoryCounts = recipesDatabase.reduce((acc, recipe) => {
        acc[recipe.category] = (acc[recipe.category] || 0) + 1;
        return acc;
    }, {});
    
    console.log('📊 Recipes by category:', categoryCounts);
    
    return recipesDatabase;
}

// Auto-merge when all parts are loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mergeRecipesParts);
} else {
    // If DOM is already loaded, merge immediately
    setTimeout(mergeRecipesParts, 100);
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { recipesDatabase, mergeRecipesParts };
}
