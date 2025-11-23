// PWA Service Worker Registration
// نسخة مبسطة للصفحات الأخرى (غير index.html)

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then(registration => {
                console.log('✅ PWA: Service Worker registered');
            })
            .catch(error => {
                console.error('❌ PWA: Service Worker registration failed:', error);
            });
    });
}
