@echo off
chcp 65001 >nul
cls
echo ============================================
echo 🚀 إنشاء مشروع Flutter كامل - WiBo Health
echo ============================================
echo.
echo [الخطوة 1/4] حذف المشروع القديم...
cd C:\Users\Admin\Desktop
if exist wibo_health (
    rmdir /s /q wibo_health
    echo ✅ تم حذف المشروع القديم
) else (
    echo ℹ️  المشروع غير موجود
)
echo.
echo [الخطوة 2/4] إنشاء مشروع Flutter جديد...
echo ⏳ هذا قد يستغرق 1-2 دقيقة...
flutter create --org com.wibohealth wibo_health
echo ✅ تم إنشاء المشروع
echo.
echo [الخطوة 3/4] الانتقال إلى مجلد المشروع...
cd wibo_health
echo ✅ تم
echo.
echo [الخطوة 4/4] جاهز للتشغيل!
echo.
echo ============================================
echo 🎉 المشروع جاهز!
echo ============================================
echo.
echo 📂 مسار المشروع: C:\Users\Admin\Desktop\wibo_health
echo.
echo 🚀 الخطوة التالية:
echo    سأرسل لك ملف main.dart الصحيح الآن
echo    ثم نفذ: flutter run -d chrome --web-port=8080
echo.
pause
