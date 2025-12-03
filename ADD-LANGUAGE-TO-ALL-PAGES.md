# ✅ خطوات إضافة نظام اللغة لجميع الصفحات

## 🎯 التعديلات المطلوبة لكل صفحة:

### 1️⃣ إضافة الفونتات في `<head>`:
```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet">
```

### 2️⃣ استبدال `language-manager.js` بالنظام الجديد:
```html
<!-- القديم -->
<script src="/js/language-manager.js"></script>

<!-- الجديد -->
<script src="/js/unified-language-system.js"></script>
```

### 3️⃣ استبدال زر اللغة القديم:
```html
<!-- القديم -->
<a href="/en/" class="theme-toggle">🇬🇧</a>

<!-- الجديد -->
<button class="theme-toggle" data-lang-toggle="en" data-lang="ar" title="Switch to English">
    🇬🇧 EN
</button>
<button class="theme-toggle" data-lang-toggle="ar" data-lang="en" title="التبديل للعربية" style="display: none;">
    🇸🇦 AR
</button>
```

### 4️⃣ إضافة `data-lang` للنصوص الرئيسية:
```html
<!-- مثال: العنوان -->
<h1 data-lang="ar">دليل الأطعمة</h1>
<h1 data-lang="en" style="display: none;">Foods Guide</h1>

<!-- مثال: الوصف -->
<p data-lang="ar">1051 عنصر غذائي</p>
<p data-lang="en" style="display: none;">1051 Food Items</p>
```

---

## 📋 قائمة الصفحات المطلوب تعديلها:

- [ ] foods.html
- [ ] supplements.html
- [ ] calculators.html
- [ ] recipes.html
- [ ] articles.html
- [ ] doctor.html
- [ ] pricing.html
- [ ] diet-plan.html
- [ ] calorie-tracker.html
- [ ] food-details.html
- [ ] about.html
- [ ] contact.html
- [ ] privacy.html
- [ ] terms.html
- [ ] disclaimer.html

---

## ⚡ نصائح للسرعة:

1. ✅ استخدم Find & Replace لاستبدال `language-manager.js`
2. ✅ ابحث عن `<a href="/en/"` واستبدلها بالأزرار الجديدة
3. ✅ النصوص الديناميكية (data.js, recipes) **لا تحتاج تعديل!**
4. ✅ السكريبت الجديد يترجمها تلقائياً!

---

## 🎯 الأولوية:

**عالية (افعلها أولاً):**
- foods.html ← الأكثر استخداماً
- supplements.html
- recipes.html
- calculators.html

**متوسطة:**
- articles.html
- doctor.html
- pricing.html

**منخفضة:**
- الصفحات القانونية (privacy, terms, etc.)
