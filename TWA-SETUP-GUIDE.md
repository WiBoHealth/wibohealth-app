# 🚀 دليل إنشاء Trusted Web Activity لـ WiBo Health

## 📋 الخطوة 1: تجهيز الأيقونات

### الأيقونات المطلوبة:

لازم يكون عندك 4 أيقونات في مجلد `images/`:

1. **icon-192.png** (192x192 بكسل) - أيقونة عادية
2. **icon-512.png** (512x512 بكسل) - أيقونة عادية ✅ (موجودة)
3. **icon-maskable-192.png** (192x192 بكسل) - أيقونة maskable
4. **icon-maskable-512.png** (512x512 بكسل) - أيقونة maskable

---

### ما هي Maskable Icons؟

**أيقونة Maskable** = أيقونة مع مساحة أمان (safe zone) حتى لا يتم قصها على أجهزة Android المختلفة.

**القاعدة الذهبية:**
- الشعار الأساسي يجب أن يكون في **80% من المساحة المركزية**
- الـ 20% الخارجية = منطقة أمان (قد تُقص)

---

### طريقة إنشاء الأيقونات:

#### **الطريقة 1: باستخدام Maskable.app (الأسهل)** ⭐

1. اذهب إلى: https://maskable.app/editor
2. ارفع أيقونتك الحالية: `/images/icon-512.png`
3. ضبط الأيقونة في المنطقة الآمنة (الدائرة الداخلية)
4. حمّل النتيجة بحجمين (192 و 512)
5. سمّها: `icon-maskable-192.png` و `icon-maskable-512.png`

#### **الطريقة 2: باستخدام Photoshop/GIMP**

1. افتح `icon-512.png`
2. أضف مساحة خارجية (padding) 10% من كل جانب
3. احفظ بحجمين: 192x192 و 512x512

#### **الطريقة 3: أداة سريعة أونلاين**

استخدم: https://www.pwabuilder.com/imageGenerator
- ارفع أيقونتك
- ستنشئ لك جميع الأحجام تلقائياً

---

### إنشاء icon-192.png:

لازم تصغّر `icon-512.png` إلى 192x192:

**طريقة سريعة عبر موقع:**
1. اذهب إلى: https://www.iloveimg.com/resize-image
2. ارفع `/images/icon-512.png`
3. اختر 192x192 بكسل
4. حمّل النتيجة وسمّها `icon-192.png`

---

## 📋 الخطوة 2: رفع الأيقونات على Netlify

بعد ما تجهز الأيقونات الأربعة:

1. ارفعها على مجلد `images/` في مشروعك
2. تأكد من الأسماء:
   - `icon-192.png`
   - `icon-512.png` ✅ (موجودة)
   - `icon-maskable-192.png`
   - `icon-maskable-512.png`

3. ارفع المشروع على Netlify
4. تأكد من الروابط تعمل:
   - https://tangerine-smakager-463ba5.netlify.app/images/icon-192.png
   - https://tangerine-smakager-463ba5.netlify.app/images/icon-512.png
   - https://tangerine-smakager-463ba5.netlify.app/images/icon-maskable-192.png
   - https://tangerine-smakager-463ba5.netlify.app/images/icon-maskable-512.png

---

## 📋 الخطوة 3: تثبيت Bubblewrap CLI

### تأكد من المتطلبات مثبتة:

```bash
# تحقق من Node.js (لازم يكون مثبت)
node --version

# تحقق من Java (لازم يكون مثبت)
java -version
```

**إذا مش مثبتة:**
- **Node.js**: حمّل من https://nodejs.org
- **Java JDK 17**: حمّل من https://adoptium.net

---

### ثبّت Bubblewrap:

```bash
npm install -g @bubblewrap/cli
```

### تحقق من التثبيت:

```bash
bubblewrap --version
```

**إذا طلع رقم النسخة** → تمام! ✅

---

## 📋 الخطوة 4: إنشاء التطبيق باستخدام Bubblewrap

### 1. إنشاء المشروع:

```bash
bubblewrap init --manifest https://tangerine-smakager-463ba5.netlify.app/manifest.json
```

**سيطلب منك معلومات:**

```
? Domain being opened in the TWA: 
➡️ أدخل: tangerine-smakager-463ba5.netlify.app

? Application ID (com.example.twa):
➡️ أدخل: com.wibohealth.app

? Application name:
➡️ أدخل: WiBo Health

? Starting URL path:
➡️ اضغط Enter (/) الافتراضي

? Color for the toolbar (hex format):
➡️ أدخل: #667eea

? Color for the splash screen (hex format):
➡️ أدخل: #667eea

? Path to icon file (must be at least 512x512):
➡️ اضغط Enter (سيستخدم من manifest.json)

? Display mode (standalone, fullscreen):
➡️ أدخل: standalone

? Status bar color (for Android M and above):
➡️ أدخل: #667eea

? Enable notifications?
➡️ أدخل: y

? Signing key information - keystore path:
➡️ اضغط Enter (سينشئ تلقائياً)

? Signing key information - key alias:
➡️ أدخل: wibohealth

? Password for the keystore:
➡️ أدخل كلمة سر قوية (احفظها!)

? Password for the key:
➡️ نفس كلمة السر السابقة
```

---

### 2. بناء التطبيق (Build):

```bash
cd twa-project
bubblewrap build
```

**هذا الأمر سيُنشئ:**
- ملف **APK** للتجربة (في مجلد `app/build/outputs/apk/`)
- ملف **AAB** للنشر على Google Play (في مجلد `app/build/outputs/bundle/`)

---

### 3. اختبار التطبيق:

**على جهاز Android حقيقي:**

```bash
# توصيل الجهاز عبر USB
# تفعيل وضع المطور (Developer Mode)
# تفعيل USB Debugging

# تثبيت التطبيق
adb install app/build/outputs/apk/release/app-release-signed.apk
```

**أو انسخ ملف APK على هاتفك وثبّته يدوياً**

---

## 📋 الخطوة 5: رفع التطبيق على Google Play

### متطلبات النشر:

1. **حساب Google Play Console** ($25 رسوم تسجيل لمرة واحدة)
2. **ملف AAB** (من الخطوة 4)
3. **Privacy Policy** (سياسة الخصوصية)
4. **Screenshots** (صور من التطبيق - 2 على الأقل)
5. **App Description** (وصف التطبيق)

---

### خطوات النشر:

1. اذهب إلى: https://play.google.com/console
2. أنشئ "تطبيق جديد"
3. املأ معلومات التطبيق:
   - الاسم: **WiBo Health**
   - الفئة: **الصحة واللياقة**
   - اللغة: **العربية**

4. ارفع ملف AAB:
   ```
   app/build/outputs/bundle/release/app-release.aab
   ```

5. أكمل:
   - الوصف القصير (80 حرف)
   - الوصف الكامل (4000 حرف)
   - Screenshots (على الأقل 2)
   - أيقونة التطبيق (512x512)

6. أضف سياسة الخصوصية (Privacy Policy)
7. اختر الفئة العمرية والمحتوى
8. أرسل للمراجعة!

---

## ⚠️ مهم جداً: Digital Asset Links

بعد ما يوافق Google على التطبيق، لازم تضيف ملف **assetlinks.json** على موقعك عشان التطبيق يفتح بدون شريط المتصفح.

**الخطوات:**

1. اذهب إلى: https://developers.google.com/digital-asset-links/tools/generator

2. أدخل:
   - **Website**: https://tangerine-smakager-463ba5.netlify.app
   - **Package name**: com.wibohealth.app
   - **SHA-256 fingerprint**: (ستحصل عليه من Bubblewrap)

3. احفظ الملف في:
   ```
   /.well-known/assetlinks.json
   ```

4. ارفعه على Netlify

---

## 🎯 الملخص السريع:

```bash
# 1. تثبيت الأدوات
npm install -g @bubblewrap/cli

# 2. إنشاء المشروع
bubblewrap init --manifest https://tangerine-smakager-463ba5.netlify.app/manifest.json

# 3. بناء التطبيق
cd twa-project
bubblewrap build

# 4. ملف AAB جاهز للنشر!
# app/build/outputs/bundle/release/app-release.aab
```

---

## 🆘 إذا واجهت مشاكل:

### خطأ: "SDK location not found"
```bash
# أنشئ ملف local.properties:
echo "sdk.dir=/path/to/Android/sdk" > local.properties
```

### خطأ: "Java not found"
```bash
# ثبّت Java JDK 17
# Windows: https://adoptium.net
# Mac: brew install openjdk@17
```

### خطأ: "Command not found: bubblewrap"
```bash
# تأكد من تثبيت npm بشكل صحيح
npm list -g @bubblewrap/cli
```

---

## 📞 جاهز للبدء؟

**الخطوة التالية:**
1. جهّز الأيقونات الأربعة
2. ارفعها على Netlify
3. قلي "جاهز" وسأعطيك الأوامر الدقيقة!

أنا معك خطوة بخطوة 💪
