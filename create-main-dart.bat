@echo off
chcp 65001 >nul
cls
echo ============================================
echo Creating main.dart for WiBo Health
echo ============================================
echo.

cd C:\Users\Admin\Desktop\wibo_health\lib

echo Creating main.dart file...

(
echo import 'package:flutter/material.dart';
echo.
echo void main^(^) {
echo   runApp^(const WiBoHealthApp^(^)^);
echo }
echo.
echo class WiBoHealthApp extends StatelessWidget {
echo   const WiBoHealthApp^({super.key}^);
echo.
echo   @override
echo   Widget build^(BuildContext context^) {
echo     return MaterialApp^(
echo       title: 'WiBo Health',
echo       debugShowCheckedModeBanner: false,
echo       theme: ThemeData^(
echo         primarySwatch: Colors.green,
echo         useMaterial3: true,
echo       ^),
echo       home: const HomeScreen^(^),
echo     ^);
echo   }
echo }
echo.
echo class HomeScreen extends StatefulWidget {
echo   const HomeScreen^({super.key}^);
echo.
echo   @override
echo   State^<HomeScreen^> createState^(^) =^> _HomeScreenState^(^);
echo }
echo.
echo class _HomeScreenState extends State^<HomeScreen^> {
echo   bool isDarkMode = false;
echo.
echo   @override
echo   Widget build^(BuildContext context^) {
echo     return Directionality^(
echo       textDirection: TextDirection.rtl,
echo       child: Scaffold^(
echo         backgroundColor: isDarkMode ? const Color^(0xFF1a1a1a^) : const Color^(0xFFF5F5F5^),
echo         body: SafeArea^(
echo           child: SingleChildScrollView^(
echo             padding: const EdgeInsets.all^(20^),
echo             child: Column^(
echo               children: [
echo                 Text^(
echo                   '🏥 WiBo Health',
echo                   style: TextStyle^(fontSize: 32, fontWeight: FontWeight.bold^),
echo                 ^),
echo                 const SizedBox^(height: 8^),
echo                 Text^('دليلك الصحي الشامل', style: TextStyle^(fontSize: 18^)^),
echo                 const SizedBox^(height: 20^),
echo                 ElevatedButton^(
echo                   onPressed: ^(^) { setState^(^(^) { isDarkMode = !isDarkMode; }^); },
echo                   child: Text^(isDarkMode ? '☀️ وضع النهار' : '🌙 الوضع الليلي'^),
echo                 ^),
echo                 const SizedBox^(height: 30^),
echo                 Text^('✅ التطبيق يعمل!', style: TextStyle^(fontSize: 24, color: Colors.green^)^),
echo               ],
echo             ^),
echo           ^),
echo         ^),
echo       ^),
echo     ^);
echo   }
echo }
) > main.dart

echo.
echo ============================================
echo Done! main.dart created successfully!
echo ============================================
echo.
echo File location: C:\Users\Admin\Desktop\wibo_health\lib\main.dart
echo.
echo Next step: Run this command:
echo flutter run -d chrome --web-port=8080
echo.
pause
