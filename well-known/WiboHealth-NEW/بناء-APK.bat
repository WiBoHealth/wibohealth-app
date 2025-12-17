@echo off
chcp 65001 >nul
echo ╔════════════════════════════════════════════════════╗
echo ║         📦 بناء APK لتطبيق WiBo Health            ║
echo ╚════════════════════════════════════════════════════╝
echo.
echo 🎯 هذا الملف سيساعدك على بناء APK كامل!
echo.

cd /d "%~dp0"

echo ════════════════════════════════════════════════════
echo  الخطوات المطلوبة:
echo ════════════════════════════════════════════════════
echo.
echo 1️⃣  تثبيت EAS CLI (مرة واحدة فقط)
echo 2️⃣  تسجيل الدخول لحساب Expo
echo 3️⃣  بناء APK (10-15 دقيقة)
echo 4️⃣  تحميل APK على الهاتف
echo.
echo ════════════════════════════════════════════════════
echo.

:MENU
echo.
echo اختر ما تريد فعله:
echo.
echo [1] تثبيت EAS CLI
echo [2] تسجيل الدخول لحساب Expo
echo [3] بناء APK (Preview - للاختبار)
echo [4] بناء APK (Production - نهائي)
echo [5] إنشاء حساب Expo جديد
echo [0] خروج
echo.
set /p choice="اختر رقم (0-5): "

if "%choice%"=="1" goto INSTALL_EAS
if "%choice%"=="2" goto LOGIN
if "%choice%"=="3" goto BUILD_PREVIEW
if "%choice%"=="4" goto BUILD_PRODUCTION
if "%choice%"=="5" goto CREATE_ACCOUNT
if "%choice%"=="0" goto END
goto MENU

:INSTALL_EAS
echo.
echo ════════════════════════════════════════════════════
echo  تثبيت EAS CLI...
echo ════════════════════════════════════════════════════
echo.
call npm install -g eas-cli
echo.
echo ✅ تم التثبيت بنجاح!
pause
goto MENU

:LOGIN
echo.
echo ════════════════════════════════════════════════════
echo  تسجيل الدخول لحساب Expo
echo ════════════════════════════════════════════════════
echo.
echo إذا لم يكن لديك حساب، اختر [5] من القائمة
echo.
call eas login
pause
goto MENU

:BUILD_PREVIEW
echo.
echo ════════════════════════════════════════════════════
echo  بناء APK للاختبار (Preview)
echo ════════════════════════════════════════════════════
echo.
echo ⏱️  سيستغرق البناء: 10-15 دقيقة
echo 📱 ستحصل على رابط التحميل في النهاية
echo.
call eas build --platform android --profile preview
echo.
echo ════════════════════════════════════════════════════
echo ✅ اكتمل البناء!
echo 📥 انسخ رابط التحميل من الأعلى
echo 📱 افتح الرابط على هاتفك وثبّت APK
echo ════════════════════════════════════════════════════
pause
goto MENU

:BUILD_PRODUCTION
echo.
echo ════════════════════════════════════════════════════
echo  بناء APK النهائي (Production)
echo ════════════════════════════════════════════════════
echo.
echo ⏱️  سيستغرق البناء: 10-15 دقيقة
echo 📱 ستحصل على رابط التحميل في النهاية
echo.
call eas build --platform android --profile production
echo.
echo ════════════════════════════════════════════════════
echo ✅ اكتمل البناء!
echo 📥 انسخ رابط التحميل من الأعلى
echo 📱 افتح الرابط على هاتفك وثبّت APK
echo ════════════════════════════════════════════════════
pause
goto MENU

:CREATE_ACCOUNT
echo.
echo ════════════════════════════════════════════════════
echo  إنشاء حساب Expo جديد
echo ════════════════════════════════════════════════════
echo.
echo 🌐 افتح المتصفح واذهب إلى:
echo    https://expo.dev/signup
echo.
echo أو سجّل مباشرة عبر:
call eas register
pause
goto MENU

:END
echo.
echo 👋 مع السلامة!
echo.
pause
exit
