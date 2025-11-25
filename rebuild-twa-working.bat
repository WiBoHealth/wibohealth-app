@echo off
chcp 65001 >nul
cls
echo ============================================
echo Rebuilding TWA for WiBo Health (Tested Method)
echo ============================================
echo.
echo This uses the SAME method that worked before!
echo Arabic text worked perfectly in the previous APK.
echo.
echo ============================================
echo Requirements:
echo ============================================
echo [x] Node.js installed
echo [x] JDK 11+ installed
echo [x] Android SDK installed
echo [x] Bubblewrap CLI installed
echo.
echo ============================================
echo Step 1: Install/Update Bubblewrap CLI
echo ============================================
echo.
npm install -g @bubblewrap/cli
echo.
echo ============================================
echo Step 2: Go to project directory
echo ============================================
echo.
cd C:\Users\Admin\Desktop
echo.
echo ============================================
echo Step 3: Initialize TWA Project
echo ============================================
echo.
echo Option A: Use existing twa-manifest.json
echo ------------------------------------------
echo If you have the old project folder with twa-manifest.json:
echo 1. Copy twa-manifest.json to Desktop
echo 2. Run: bubblewrap init --manifest twa-manifest.json
echo.
echo Option B: Create new project from website
echo ------------------------------------------
echo bubblewrap init --manifest https://wibohealth-app.vercel.app/manifest.json
echo.
echo When prompted, use these EXACT values (same as before):
echo - Domain: wibohealth-app.vercel.app
echo - Package ID: com.wibohealth.app
echo - App name: wibo health
echo - Launcher name: WiBo Health
echo - Theme color: #667EEA
echo - Navigation color: #000000
echo - Background color: #667EEA
echo.
echo ============================================
echo Step 4: Build APK
echo ============================================
echo cd twa-project
echo bubblewrap build
echo.
echo ============================================
echo Expected Output:
echo ============================================
echo APK: twa-project\app\build\outputs\apk\release\app-release-signed.apk
echo AAB: twa-project\app\build\outputs\bundle\release\app-release.aab
echo.
echo ============================================
echo Important Notes:
echo ============================================
echo 1. Use the SAME keystore: wibohealth-new.keystore
echo 2. Keystore password: (you should know it)
echo 3. Alias: wibohealth
echo.
echo If you lost the keystore password, you'll need to:
echo - Create a NEW package ID (e.g., com.wibohealth.app2)
echo - Generate a NEW keystore
echo.
pause
