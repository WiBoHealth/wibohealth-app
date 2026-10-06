const fs = require('fs');

console.log('🔄 جاري مزامنة الهيدر والألوان من index.html إلى supplements.html...');

try {
    // 1. قراءة الصفحة الرئيسية
    const indexHtml = fs.readFileSync('index.html', 'utf8');

    // 2. استخراج الهيدر المعتمد من index.html
    const headerMatch = indexHtml.match(/<header[\s\S]*?<\/header>/i);
    if (!headerMatch) {
        console.error('❌ لم يتم العثور على وسم <header> في index.html!');
        process.exit(1);
    }
    const officialHeader = headerMatch[0];

    // 3. قراءة صفحة المكملات
    let suppHtml = fs.readFileSync('supplements.html', 'utf8');

    // 4. استبدال الهيدر في supplements.html
    suppHtml = suppHtml.replace(/<header[\s\S]*?<\/header>/i, officialHeader);

    // 5. استعادة ألوان خلفية الموقع الأصلية (النيلي/البنفسجي الملكي لـ index.html)
    suppHtml = suppHtml.replace(
        /body\s*\{[\s\S]*?background:\s*linear-gradient\([^;]+;/i,
        'body {\n            font-family: \'Cairo\', sans-serif;\n            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'
    );

    // 6. حفظ ملف supplements.html
    fs.writeFileSync('supplements.html', suppHtml, 'utf8');

    console.log('✅ تم نقل الهيدر الرسمي والألوان الملكية إلى supplements.html بنجاح 100%!');
} catch (err) {
    console.error('❌ حدث خطأ:', err.message);
}