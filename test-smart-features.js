// Simple test - paste this DIRECTLY in supplements.html after supplementsData

(function() {
    'use strict';
    
    console.log('🚀 SMART FEATURES TEST STARTED');
    
    // Wait for page load
    setTimeout(function() {
        console.log('⏰ Checking after 2 seconds...');
        
        // Check supplements data
        if (typeof supplementsData !== 'undefined') {
            console.log('✅ Found', supplementsData.length, 'supplements');
        } else if (typeof window.supplementsData !== 'undefined') {
            console.log('✅ Found', window.supplementsData.length, 'supplements (window)');
        } else {
            console.error('❌ No supplements data found!');
        }
        
        // Check search input
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            console.log('✅ Search input found!');
            
            // Add simple live search
            searchInput.addEventListener('input', function(e) {
                const query = e.target.value.toLowerCase();
                if (query.length >= 2) {
                    console.log('🔍 Searching:', query);
                    
                    const results = (window.supplementsData || supplementsData).filter(function(supp) {
                        return supp.name.toLowerCase().includes(query) || 
                               supp.englishName.toLowerCase().includes(query);
                    });
                    
                    console.log('📊 Found', results.length, 'results');
                }
            });
        } else {
            console.error('❌ Search input not found!');
        }
        
        console.log('✅ SMART FEATURES TEST COMPLETE!');
        
    }, 2000);
    
})();
