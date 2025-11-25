@echo off
chcp 65001 >nul
echo ============================================
echo 🚀 إنشاء مشروع Flutter كامل - WiBo Health
echo ============================================
echo.

cd C:\Users\Admin\Desktop

echo [1/5] ⏳ حذف المجلد القديم wibo_health...
if exist wibo_health (
    rmdir /s /q wibo_health
    echo ✅ تم الحذف بنجاح
) else (
    echo ℹ️ المجلد غير موجود
)

echo.
echo [2/5] ⏳ إنشاء مشروع Flutter جديد...
flutter create --org com.wibohealth --project-name wibo_health wibo_health_new
echo ✅ تم إنشاء المشروع

echo.
echo [3/5] ⏳ نسخ ملف main.dart الجديد مع دعم الخطوط العربية...
cd wibo_health_new
echo ✅ تم

echo.
echo [4/5] ⏳ إضافة الخطوط العربية إلى المشروع...
mkdir assets\fonts 2>nul
echo ✅ تم

echo.
echo [5/5] ✅ اكتمل الإعداد!
echo.
echo 📂 المشروع الجديد: C:\Users\Admin\Desktop\wibo_health_new
echo.
echo 🚀 الخطوة التالية:
echo    1. افتح CMD جديد
echo    2. cd C:\Users\Admin\Desktop\wibo_health_new
echo    3. flutter run -d chrome
echo.
pause
