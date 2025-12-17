@echo off
echo ========================================
echo Installing expo-font for Arabic support
echo ========================================
echo.

cd /d "%~dp0"
call npm install expo-font

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Now run: npx expo start
echo Then press: w (for web) or scan QR code
echo.
pause
