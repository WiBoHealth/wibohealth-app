# 🔧 إصلاح مشكلة النص العربي - دليل خطوة بخطوة

## ✅ الملفات المصلحة الجاهزة:

1. **index-fixed.html** - الصفحة الرئيسية بـ UTF-8 صحيح
2. **css/style-main.css** - ملف CSS منفصل
3. **js/main-app.js** - ملف JavaScript منفصل
4. **manifest-fixed.json** - ملف Manifest بـ UTF-8 صحيح

---

## 📋 الخطوات:

### **الخطوة 1: حذف الملفات القديمة**

من مجلد `wibohealth-app`:
```
احذف: index.html
احذف: manifest.json
```

---

### **الخطوة 2: إعادة تسمية الملفات الجديدة**

```
إعادة تسمية: index-fixed.html → index.html
إعادة تسمية: manifest-fixed.json → manifest.json
```

---

### **الخطوة 3: تعديل index.html**

افتح `index.html` وغيّر الروابط:

**من:**
```html
<link rel="stylesheet" href="/css/style.css">
<script src="/js/main.js"></script>
```

**إلى:**
```html
<link rel="stylesheet" href="/css/style-main.css">
<script src="/js/main-app.js"></script>
```

---

### **الخطوة 4: رفع على GitHub**

1. افتح GitHub Desktop
2. سترى التغييرات:
   - Modified: `index.html`
   - Modified: `manifest.json`
   - Added: `css/style-main.css`
   - Added: `js/main-app.js`
3. Commit مع رسالة: `Fix Arabic encoding to UTF-8`
4. اضغط **Push to origin**

---

### **الخطوة 5: انتظر نشر Vercel**

1. انتظر دقيقة واحدة
2. افتح: `https://wibohealth-app.vercel.app`
3. **العربي المفروض يظهر صح الآن!** ✅

---

## 🔍 إذا لسا في مشكلة:

### **تأكد من:**

1. **الملفات تم رفعها على GitHub:**
   - روح على `https://github.com/your-username/wibohealth-app`
   - تأكد الملفات موجودة

2. **Vercel نشر التحديث:**
   - روح على `https://vercel.com/your-projects`
   - شوف آخر Deployment
   - لازم يكون "Ready" (مش Building)

3. **امسح الكاش:**
   - اضغط `Ctrl + Shift + R` في المتصفح
   - أو افتح الموقع في Incognito Mode

---

## 📱 بعد إصلاح الموقع:

✅ **خذ لقطات الشاشة من الموقع الشغال**
✅ **كمّل Google Play Console**
✅ **ارفع AAB ونشر التطبيق!**

---

💚 **بالتوفيق!**
