# 🚀 دليل بناء TWA لـ WiBo Health (Vercel)

---

## ✅ **المعلومات الأساسية:**

| البند | القيمة |
|-------|--------|
| **الموقع** | https://wibohealth-app.vercel.app |
| **Package ID** | com.wibohealth.app |
| **اسم التطبيق** | WiBo Health |
| **النسخة** | 1.0.0 |

---

## 🎯 **الطريقة الموصى بها: PWABuilder**

### **⏱️ المدة: 5 دقائق**

---

### **الخطوات:**

#### **1️⃣ افتح PWABuilder:**
```
https://www.pwabuilder.com
```

#### **2️⃣ أدخل رابط الموقع:**
```
https://wibohealth-app.vercel.app
```

**⚠️ ملاحظة:** لا تضع `/index.html` في النهاية

#### **3️⃣ اضغط "Start"**

#### **4️⃣ انتظر التحليل (10-20 ثانية)**

#### **5️⃣ اختر "Package For Stores"**

#### **6️⃣ اختر "Android"**

#### **7️⃣ املأ المعلومات:**

| الحقل | القيمة |
|-------|--------|
| Package ID | `com.wibohealth.app` |
| App name | `WiBo Health` |
| App version | `1` |
| Version code | `1` |
| Host | `wibohealth-app.vercel.app` |
| Start URL | `/` |

#### **8️⃣ Options (اختياري):**

- ✅ **Enable Notifications**: نعم
- ✅ **Splash screen fade duration**: 300ms
- ✅ **Status bar color**: `#4CAF50`
- ✅ **Navigation bar color**: `#4CAF50`

#### **9️⃣ اضغط "Generate"**

#### **🔟 حمّل الملفات:**

**سيعطيك:**
- ✅ **app-release.aab** (للرفع على Google Play)
- ✅ **app-release.apk** (للاختبار)

---

## 📱 **اختبار APK:**

### **على هاتفك:**

1. **حمّل `app-release.apk`** على هاتفك
2. **ثبّته** (قد تحتاج تفعيل "Unknown Sources")
3. **افتح التطبيق**
4. **تحقق:**
   - ✅ هل العربية تظهر واضحة؟
   - ✅ هل التطبيق يفتح بدون شريط المتصفح؟
   - ✅ هل الأيقونة والاسم صحيحين؟

---

## 🎯 **إذا العربية واضحة:**

### **✅ جاهز للرفع على Google Play!**

---

## 🔄 **الطريقة البديلة: Bubblewrap CLI**

### **⏱️ المدة: 15 دقيقة**

---

### **المتطلبات:**
- ✅ Node.js مثبت
- ✅ JDK 11+ مثبت
- ✅ Android SDK مثبت

---

### **الخطوات:**

#### **1️⃣ تثبيت Bubblewrap:**
```cmd
npm install -g @bubblewrap/cli
```

#### **2️⃣ إنشاء المشروع:**
```cmd
cd C:\Users\Admin\Desktop
bubblewrap init --manifest https://wibohealth-app.vercel.app/manifest.json
```

#### **3️⃣ عند السؤال:**

| السؤال | الجواب |
|--------|--------|
| Domain? | `wibohealth-app.vercel.app` |
| Application ID? | `com.wibohealth.app` |
| Application name? | `WiBo Health` |
| Launcher name? | `WiBo Health` |
| Status bar color? | `#4CAF50` |
| Navigation bar color? | `#4CAF50` |

#### **4️⃣ بناء APK:**
```cmd
cd twa-project
bubblewrap build
```

#### **5️⃣ مكان الملفات:**
```
twa-project/app/build/outputs/bundle/release/app-release.aab
twa-project/app/build/outputs/apk/release/app-release-signed.apk
```

---

## 🔑 **ملاحظات مهمة:**

### **1️⃣ Signing Key:**

**Bubblewrap سينشئ keystore تلقائياً في:**
```
~/.bubblewrap/
```

**⚠️ احفظ هذا الملف!** ستحتاجه لكل تحديث مستقبلي!

---

### **2️⃣ Digital Asset Links:**

**بعد بناء APK، ستحصل على SHA-256 fingerprint**

**مثلاً:**
```
SHA-256: 14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B1:3F:CF:44:E5
```

**حدّث ملف `assetlinks.json` بهذا الـ fingerprint**

**ثم ارفعه على:**
```
https://wibohealth-app.vercel.app/.well-known/assetlinks.json
```

---

## 📤 **الرفع على Google Play:**

### **الملف المطلوب: AAB**

**استخدم:**
```
app-release.aab
```

**⚠️ لا ترفع APK!** Google Play يقبل فقط AAB الآن.

---

## ✅ **Checklist النهائي:**

- [ ] ✅ بنيت APK/AAB من PWABuilder
- [ ] ✅ اختبرت APK على الهاتف
- [ ] ✅ العربية تظهر واضحة
- [ ] ✅ التطبيق يفتح بدون شريط المتصفح
- [ ] ✅ حصلت على SHA-256 fingerprint
- [ ] ✅ حدّثت assetlinks.json
- [ ] ✅ رفعت assetlinks.json على Vercel
- [ ] ✅ جاهز للرفع على Google Play Console

---

## 🎉 **بعد النشر على Google Play:**

**تطبيقك سيكون:**
```
https://play.google.com/store/apps/details?id=com.wibohealth.app
```

---

## 📞 **الدعم:**

إذا واجهت أي مشكلة:
1. راجع ملف `TWA-SETUP-GUIDE.md`
2. راجع ملف `CHECKLIST.md`
3. تأكد من تحديث `assetlinks.json`

---

**WiBo Health - قريباً على Google Play! 🚀**
