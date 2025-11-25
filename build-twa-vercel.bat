@echo off
chcp 65001 >nul
cls
echo ============================================
echo Building TWA for WiBo Health (Vercel)
echo ============================================
echo.
echo Website: https://wibohealth-app.vercel.app
echo Package: com.wibohealth.app
echo.
echo ============================================
echo Instructions:
echo ============================================
echo.
echo Option 1: PWABuilder (Recommended - 5 minutes)
echo -----------------------------------------------
echo 1. Go to: https://www.pwabuilder.com
echo 2. Enter: https://wibohealth-app.vercel.app
echo 3. Click "Start"
echo 4. Select "Android" package
echo 5. Download APK/AAB
echo.
echo ============================================
echo Option 2: Bubblewrap CLI (Advanced - 15 minutes)
echo -----------------------------------------------
echo.
echo Step 1: Install Bubblewrap (if not installed)
echo npm install -g @bubblewrap/cli
echo.
echo Step 2: Initialize project
echo bubblewrap init --manifest https://wibohealth-app.vercel.app/manifest.json
echo.
echo When prompted, use these values:
echo - Domain: wibohealth-app.vercel.app
echo - Package ID: com.wibohealth.app
echo - App name: WiBo Health
echo.
echo Step 3: Build APK
echo cd twa-project
echo bubblewrap build
echo.
echo ============================================
echo Output Files:
echo ============================================
echo APK: app-release-signed.apk
echo AAB: app-release.aab
echo.
echo ============================================
echo Next Steps After Building:
echo ============================================
echo 1. Test APK on your phone
echo 2. If Arabic works correctly, proceed to Google Play
echo 3. Upload AAB to Google Play Console
echo.
pause
