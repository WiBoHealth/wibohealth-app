@echo off
echo ========================================
echo   🔍 فحص بيئة التطوير - WiBo Health
echo ========================================
echo.

echo 📦 فحص Node.js...
node --version
if %errorlevel% neq 0 (
    echo ❌ Node.js غير مثبت!
    echo 📥 حمّله من: https://nodejs.org/
) else (
    echo ✅ Node.js مثبت بنجاح!
)
echo.

echo 📦 فحص npm...
npm --version
if %errorlevel% neq 0 (
    echo ❌ npm غير مثبت!
) else (
    echo ✅ npm مثبت بنجاح!
)
echo.

echo 📦 فحص Git...
git --version
if %errorlevel% neq 0 (
    echo ❌ Git غير مثبت!
) else (
    echo ✅ Git مثبت بنجاح!
)
echo.

echo 📦 فحص Expo CLI...
expo --version
if %errorlevel% neq 0 (
    echo ⚠️ Expo CLI غير مثبت
    echo 💡 سنثبته الآن...
) else (
    echo ✅ Expo CLI مثبت بنجاح!
)
echo.

echo ========================================
echo   📊 ملخص النتائج
echo ========================================
echo.
echo 💻 اضغط على أي مفتاح لإغلاق النافذة...
pause > nul
