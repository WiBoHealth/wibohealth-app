// Script to extract unique categories from data.js
// Run this in browser console on a page that loads data.js

const extractCategories = () => {
    const categories = [...new Set(foodsDatabase.map(food => food.category))];
    const sortedCategories = categories.sort();
    
    console.log('=== All Categories ===');
    console.log('Total unique categories:', categories.length);
    console.log('');
    
    sortedCategories.forEach((cat, index) => {
        const count = foodsDatabase.filter(f => f.category === cat).length;
        console.log(`${index + 1}. ${cat} (${count} items)`);
    });
    
    return sortedCategories;
};

// Auto-run if foodsDatabase exists
if (typeof foodsDatabase !== 'undefined') {
    extractCategories();
} else {
    console.log('foodsDatabase not found. Please load data.js first.');
}
