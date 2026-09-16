/**
 * WiBo Health - PWA Registration & Smart Install Banner
 * يدعم هواتف الأندرويد والآيفون تلقائياً
 */

let deferredPrompt = null;

// 1. تسجيل السيرفس وركر
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then(reg => console.log('✅ PWA: Service Worker Registered'))
            .catch(err => console.log('❌ PWA: Registration Failed', err));
    });
}

// 2. التحقق هل التطبيق مثبت مسبقاً
function isAppInstalled() {
    return window.matchMedia('(display-mode: standalone)').matches || 
           window.navigator.standalone === true;
}

// 3. التحقق هل الجهاز آيفون / iOS
function isIos() {
    const userAgent = window.navigator.userAgent.toLowerCase();
    return /iphone|ipad|ipod/.test(userAgent);
}

// 4. بناء شريط اقتراح التثبيت تلقائياً في الصفحة
function createInstallBanner() {
    if (isAppInstalled()) return; // لا تظهر شيء إذا كان التطبيق مثبتاً بالفعل
    if (localStorage.getItem('wibo_pwa_dismissed') === 'true') return; // إذا أغلقه المستخدم مؤخراً

    // تصميم الشريط البرمجي
    const banner = document.createElement('div');
    banner.id = 'pwaInstallBanner';
    banner.style.cssText = `
        position: fixed;
        bottom: 20px;
        left: 20px;
        right: 20px;
        max-width: 480px;
        margin: 0 auto;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 16px 20px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        z-index: 999999;
        direction: rtl;
        font-family: 'Cairo', sans-serif;
        border: 1px solid rgba(255,255,255,0.1);
        animation: pwaSlideUp 0.5s ease;
    `;

    // محتوى الشريط
    banner.innerHTML = `
        <div style="display: flex; align-items: center; gap: 12px;">
            <img src="/images/icon-192.png" alt="WiBo" style="width: 45px; height: 45px; border-radius: 10px;" onerror="this.style.display='none'">
            <div>
                <strong style="display: block; font-size: 15px; color: #4ade80;">تطبيق WiBo Health</strong>
                <span style="font-size: 12px; color: #94a3b8;" id="pwaBannerDesc">ثبّت التطبيق على هاتفك لتصفح أسرع!</span>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <button id="pwaInstallBtn" style="
                background: #22c55e;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: bold;
                cursor: pointer;
                font-family: inherit;
            ">تثبيت</button>
            <button id="pwaCloseBtn" style="
                background: transparent;
                border: none;
                color: #94a3b8;
                font-size: 18px;
                cursor: pointer;
                padding: 4px;
            ">&times;</button>
        </div>
    `;

    // إضافة أنيميشن الظهور
    const style = document.createElement('style');
    style.textContent = `
        @keyframes pwaSlideUp {
            from { transform: translateY(100px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
    document.body.appendChild(banner);

    // زر الإغلاق
    document.getElementById('pwaCloseBtn').addEventListener('click', () => {
        banner.remove();
        // إخفاء الشريط لمدة 3 أيام حتى لا يزعج الزائر
        localStorage.setItem('wibo_pwa_dismissed', 'true');
    });

    // زر التثبيت
    const installBtn = document.getElementById('pwaInstallBtn');

    if (isIos()) {
        // تعليمات خاصة بالآيفون
        installBtn.textContent = 'كيف أثبته؟';
        installBtn.addEventListener('click', () => {
            alert('لتثبيت التطبيق على الآيفون:\n1. اضغط على زر المشاركة (Share ⎋) أسفل المتصفح\n2. مرر للأسفل واختر "إضافة إلى الشاشة الرئيسية (Add to Home Screen ➕)"');
        });
    } else {
        // هواتف الأندرويد
        installBtn.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                console.log(`PWA Prompt choice: ${outcome}`);
                deferredPrompt = null;
                banner.remove();
            } else {
                alert('لتثبيت التطبيق: اضغط على قائمة المتصفح (⋮) ثم اختر "تثبيت التطبيق" أو "إضافة إلى الشاشة الرئيسية".');
            }
        });
    }
}

// 5. التقاط حدث التثبيت الرسمي من أندرويد كروم
window.addEventListener('beforeinstallprompt', (e) => {
    // منع المتصفح من إظهار الشريط الافتراضي القديم
    e.preventDefault();
    deferredPrompt = e;
    
    // إظهار الشريط الخاص بنا
    createInstallBanner();
});

// للمستخدمين عبر الآيفون (إظهار الشريط بعد ثانيتين من فتح الصفحة)
window.addEventListener('DOMContentLoaded', () => {
    if (isIos() && !isAppInstalled()) {
        setTimeout(createInstallBanner, 2500);
    }
});