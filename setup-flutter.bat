@echo off
chcp 65001 >nul
cls
echo ============================================
echo Creating WiBo Health Flutter Project
echo ============================================
echo.
echo [Step 1/5] Removing old project...
cd C:\Users\Admin\Desktop
if exist wibo_health (
    rmdir /s /q wibo_health
    echo Done: Old project removed
) else (
    echo Info: No old project found
)
echo.
echo [Step 2/5] Creating new Flutter project...
echo Please wait 1-2 minutes...
flutter create --org com.wibohealth wibo_health
echo Done: Project created
echo.
echo [Step 3/5] Copying main.dart file...
cd wibo_health\lib
del main.dart
copy C:\Users\Admin\Desktop\WiboHealth-main.dart main.dart
echo Done: main.dart copied
echo.
echo [Step 4/5] Ready to run!
cd ..
echo.
echo ============================================
echo Project is ready!
echo ============================================
echo.
echo Next step: Run the following command:
echo flutter run -d chrome --web-port=8080
echo.
pause
