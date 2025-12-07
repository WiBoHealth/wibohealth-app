@echo off
chcp 65001 >nul
echo ╔════════════════════════════════════════════════════╗
echo ║         🏥 WiBo Health - دليلك الصحي الشامل       ║
echo ╚════════════════════════════════════════════════════╝
echo.
echo 🔧 جاري تشغيل التطبيق...
echo.

cd /d "%~dp0"

echo [1/2] 📦 التأكد من المكتبات...
if not exist "node_modules\" (
    echo ⚠️  المكتبات غير مثبتة! جاري التثبيت...
    call npm install
    echo ✅ تم تثبيت المكتبات بنجاح!
    echo.
)

echo [2/2] 🚀 تشغيل Expo...
echo.
echo ════════════════════════════════════════════════════
echo  بعد ظهور QR Code:
echo  • اضغط W للفتح في المتصفح
echo  • أو امسح QR Code بتطبيق Expo Go
echo ════════════════════════════════════════════════════
echo.

call npx expo start

pause
