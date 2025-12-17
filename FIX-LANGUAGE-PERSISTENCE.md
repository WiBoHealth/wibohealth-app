# 🔧 حل مشكلة تغيير اللغة التلقائي
# Fix Language Persistence Issue

---

## 🔴 المشكلة / Problem

**السيناريو:**
1. الزائر يفتح `index.html` (الصفحة الرئيسية)
2. يختار **English** من زر اللغة
3. ينتقل لصفحة أخرى (مثلاً `supplements.html`)
4. **المشكلة:** الصفحة ترجع عربي تلقائياً! ❌

**المطلوب:**
- لما الزائر يختار إنجليزي → كل الصفحات تصير إنجليزي ✅
- تبقى إنجليزي لحد ما هو يرجعها عربي ✅

---

## ✅ الحل / Solution

### السبب:
نظام اللغة الموحد `unified-language-system.js` **مش مضاف لكل الصفحات!**

### الحل:
**نضيف هذا السطر لكل صفحة HTML:**

```html
<!-- Unified Language System -->
<script src="js/unified-language-system.js"></script>
```

---

## 📝 الخطوات التفصيلية / Detailed Steps

### ✅ الصفحات المطلوب تحديثها:

#### 1. **index.html** ✅ (تم!)
```html
<head>
    ...
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
    ...
</head>
```

#### 2. **supplements.html** ⏳ (محتاج)
أضف السطر قبل `</head>`:
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 3. **foods.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 4. **calculators.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 5. **articles.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 6. **doctor.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 7. **about.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 8. **contact.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 9. **pricing.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 10. **diet-plan.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 11. **calorie-tracker.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 12. **food-details.html** ⏳ (محتاج)
```html
    <!-- Unified Language System -->
    <script src="js/unified-language-system.js"></script>
</head>
```

#### 13. **recipes.html** ✅ (موجود بالفعل!)
```html
<script src="js/unified-language-system.js"></script>
```

---

## 🎯 نقطة مهمة:

**الموقع يجب أن يضيف السكريبت قبل إغلاق `</head>` في كل صفحة!**

---

## 📋 قائمة التحقق / Checklist

- [x] ✅ index.html
- [x] ✅ recipes.html
- [ ] ⏳ supplements.html
- [ ] ⏳ foods.html
- [ ] ⏳ calculators.html
- [ ] ⏳ articles.html
- [ ] ⏳ doctor.html
- [ ] ⏳ about.html
- [ ] ⏳ contact.html
- [ ] ⏳ pricing.html
- [ ] ⏳ diet-plan.html
- [ ] ⏳ calorie-tracker.html
- [ ] ⏳ food-details.html

---

## 🚀 كيف يعمل النظام؟

### 1. **تخزين اللغة:**
```javascript
localStorage.setItem('wibo_language', 'en'); // حفظ الإنجليزية
```

### 2. **قراءة اللغة:**
```javascript
const lang = localStorage.getItem('wibo_language') || 'ar'; // قراءة اللغة المحفوظة
```

### 3. **تطبيق اللغة:**
```javascript
// تغيير اتجاه الصفحة
document.documentElement.setAttribute('lang', lang);
document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
```

---

## 🧪 اختبار الحل:

### بعد إضافة السكريبت لكل الصفحات:

1. **افتح `index.html`** في المتصفح
2. **اضغط على زر "English"**
3. **انتقل إلى صفحة أخرى** (مثلاً `supplements.html`)
4. **تحقق:** هل الصفحة لا تزال بالإنجليزية؟ ✅

---

## ✅ النتيجة المتوقعة:

**بعد الإصلاح:**
- ✅ الزائر يختار إنجليزي مرة واحدة
- ✅ **كل الصفحات** تفتح بالإنجليزي تلقائياً
- ✅ يبقى إنجليزي لحد ما هو يرجعه عربي
- ✅ النظام يحفظ الاختيار في `localStorage`

---

## 📞 ملاحظة:

**النظام الموجود في `unified-language-system.js` يعمل تلقائياً!**

كل اللي محتاجينه:
- نضيف السكريبت لكل صفحة
- وكل شي رح يشتغل تلقائياً! ✨

---

## 🎊 خلصنا!

بعد ما تضيف السكريبت لكل الصفحات، **المشكلة رح تنحل 100%!** 🎉

---

*آخر تحديث: 30 يناير 2025*
