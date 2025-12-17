/**
 * WiBo Health - Universal Supplements Data Loader
 * يحمل تلقائياً جميع بيانات المكملات من كل الملفات
 */

(function() {
    'use strict';
    
    console.log('🔄 بدء جمع المكملات الثنائية اللغة...');
    
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    function init() {
        // Give more time for all large scripts to load
        window.addEventListener('load', function() {
            setTimeout(collectAndMerge, 3000);
        });
    }
    
    function collectAndMerge() {
        // All possible variable names from batch files
        const batchVariables = [
            'supplementsDataBilingual',      // 1-33
            'supplementsBatch_34_49',        // 34-49
            'supplements_50_65',             // 50-65
            'supplementsData_126_138',       // 126-138
            'supplementsData_139_160',       // 139-160
            'supplementsData_161_181',       // 161-181
            'supplementsData_182_206',       // 182-206
            'supplementsData_207_225',       // 207-225
            'supplementsData_227_246',       // 227-246
            'supplementsData_247_259',       // 247-259
            'supplementsData_260_279',       // 260-279
            'supplementsData_280_300',       // 280-300
            'supplementsData_301_320',       // 301-320 (fixed)
            'supplementsData_321_343',       // 321-343 (fixed)
            'supplementsData_344_366',       // 344-366 (fixed)
            'supplementsData_367_385',       // 367-385 (fixed)
            'supplementsData_386_400',       // 386-400 (fixed)
            'supplementsData_401_426',       // 401-426 (fixed)
            'supplementsData_427_441',       // 427-441 (fixed)
            'supplementsData_442_453'        // 442-453 (fixed)
        ];
        
        const allSupplements = [];
        const seenIds = new Set();
        let loadedBatches = 0;
        
        // Collect from all batch variables
        batchVariables.forEach(varName => {
            if (window[varName] && Array.isArray(window[varName]) && window[varName].length > 0) {
                const batch = window[varName];
                batch.forEach(supp => {
                    if (supp && supp.id && !seenIds.has(supp.id)) {
                        allSupplements.push(supp);
                        seenIds.add(supp.id);
                    }
                });
                loadedBatches++;
                console.log(`✅ ${varName}: ${batch.length} مكملات`);
            }
        });
        
        if (allSupplements.length === 0) {
            console.error('❌ لم يتم العثور على أي بيانات!');
            console.log('🔍 المتغيرات المتاحة:', Object.keys(window).filter(k => k.includes('supplement')));
            return;
        }
        
        // Sort by ID
        allSupplements.sort((a, b) => a.id - b.id);
        
        // Store globally
        window.supplementsData = allSupplements;
        window.supplementsDataMerged = allSupplements;
        
        console.log('═══════════════════════════════════════');
        console.log(`🎉 تم تحميل ${allSupplements.length} مكمل غذائي!`);
        console.log(`📊 من ${loadedBatches} ملف`);
        console.log(`🆔 النطاق: ${allSupplements[0]?.id} - ${allSupplements[allSupplements.length-1]?.id}`);
        console.log('═══════════════════════════════════════');
        
        // Update counter
        const counter = document.getElementById('supplements-total-count');
        if (counter) {
            counter.textContent = allSupplements.length;
            console.log(`📊 تم تحديث العداد: ${allSupplements.length}`);
        }
        
        // Trigger display
        if (typeof displaySupplements === 'function') {
            setTimeout(() => {
                displaySupplements();
                console.log('✅ تم تحديث عرض المكملات');
            }, 300);
        }
        
        // Dispatch event
        document.dispatchEvent(new CustomEvent('supplementsDataLoaded', {
            detail: { total: allSupplements.length, data: allSupplements }
        }));
    }
})();
