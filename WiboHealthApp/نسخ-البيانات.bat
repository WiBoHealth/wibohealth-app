@echo off
echo ================================================
echo   📦 نسخ بيانات WiBo Health إلى React Native
echo ================================================
echo.

REM الانتقال لمجلد المشروع الأصلي
cd /d "D:\Project_abou\wibohealth-app\"

echo 📁 المجلد الأصلي: %CD%
echo.

echo 📋 نسخ ملف recipes-data.js...
copy "js\recipes-data.js" "%USERPROFILE%\Desktop\WiboHealthApp\src\data\recipesData.js"
if %errorlevel% equ 0 (
    echo ✅ تم نسخ الوصفات بنجاح!
) else (
    echo ❌ فشل نسخ الوصفات
)
echo.

echo 📋 نسخ ملف data.js...
copy "js\data.js" "%USERPROFILE%\Desktop\WiboHealthApp\src\data\foodsData.js"
if %errorlevel% equ 0 (
    echo ✅ تم نسخ الأطعمة بنجاح!
) else (
    echo ❌ فشل نسخ الأطعمة
)
echo.

echo ================================================
echo   ✅ انتهى النسخ!
echo ================================================
echo.
pause
