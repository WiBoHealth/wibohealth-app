// Service Worker for WiBo Health PWA
// Version 7.1.0 - Language Buttons Removed from Header 🚀✅

const CACHE_NAME = 'wibo-health-v7.1.0-no-lang-buttons';
const RUNTIME_CACHE = 'wibo-health-runtime-v7.1.0';
const IMAGE_CACHE = 'wibo-health-images-v7.1.0';
const API_CACHE = 'wibo-health-api-v7.1.0';
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/foods.html',
  '/food-details.html',
  '/supplements-v6-new.html',
  '/calculators.html',
  '/recipes.html',
  '/articles.html',
  '/doctor.html',
  '/pricing.html',
  '/about.html',
  '/contact.html',
  '/privacy.html',
  '/terms.html',
  '/css/style.css',
  '/css/mobile-menu.css',
  '/js/main.js',
  '/js/data.js',
  '/js/mobile-menu.js',
  '/js/language-manager.js',
  '/manifest.json'
];

// ============================================
// 🔧 INSTALL EVENT - التثبيت الأولي
// ============================================
self.addEventListener('install', event => {
  console.log('✅ Service Worker: Installing v7.1.0 (No Language Buttons)...');
  
  event.waitUntil(
    Promise.all([
      // تخزين الملفات الأساسية
      caches.open(CACHE_NAME)
        .then(cache => {
          console.log('📦 Service Worker: Caching app shell');
          return cache.addAll(PRECACHE_URLS);
        }),
      // تنظيف الـ Runtime cache
      caches.delete(RUNTIME_CACHE),
      caches.delete(IMAGE_CACHE),
      caches.delete(API_CACHE)
    ])
    .then(() => {
      console.log('✅ Service Worker: Installation completed');
      return self.skipWaiting(); // تفعيل فوري
    })
    .catch(error => {
      console.error('❌ Service Worker: Installation failed:', error);
    })
  );
});

// ============================================
// 🔄 ACTIVATE EVENT - التفعيل والتنظيف
// ============================================
self.addEventListener('activate', event => {
  console.log('🔄 Service Worker: Activating v6.0.2 - Console Errors Fixed! ✅');
  
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        console.log('📋 Service Worker: Found caches:', cacheNames);
        
        return Promise.all(
          cacheNames.map(cacheName => {
            // احتفظ بـ Caches الجديدة فقط
            const isCurrentVersion = [
              CACHE_NAME,
              RUNTIME_CACHE,
              IMAGE_CACHE,
              API_CACHE
            ].includes(cacheName);
            
            if (!isCurrentVersion) {
              console.log('🗑️ Service Worker: Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {
        console.log('✅ Service Worker: Activation completed');
        return self.clients.claim(); // التحكم بجميع الصفحات
      })
      .catch(error => {
        console.error('❌ Service Worker: Activation failed:', error);
      })
  );
});

// ============================================
// 📡 FETCH EVENT - استراتيجية المراقبة
// ============================================
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // تجاهل Google Analytics و Google Tag Manager (لا نخزنهم في Cache)
  const excludedDomains = [
    'googletagmanager.com',
    'google-analytics.com',
    'analytics.google.com',
    'www.googletagmanager.com',
    'www.google-analytics.com'
  ];
  
  if (excludedDomains.some(domain => request.url.includes(domain))) {
    return; // دع المتصفح يتعامل معها بشكل طبيعي
  }

  // تجاهل الطلبات الخارجية والبروتوكولات المختلفة
  if (!url.origin.includes(self.location.origin) && 
      !request.url.startsWith('http')) {
    return;
  }

  // تجاهل طلبات غير GET
  if (request.method !== 'GET') {
    return;
  }

  // ============================================
  // استراتيجيات مختلفة حسب نوع الملف
  // ============================================
  
  // 1️⃣ صفحات HTML - Network First
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(networkFirstStrategy(request));
    return;
  }

  // 2️⃣ الصور - Cache First
  if (request.url.match(/\.(png|jpg|jpeg|gif|webp|svg)$/i)) {
    event.respondWith(cacheFirstStrategy(request, IMAGE_CACHE));
    return;
  }

  // 3️⃣ CSS و JavaScript - Cache First
  if (request.url.match(/\.(css|js)$/i)) {
    event.respondWith(cacheFirstStrategy(request, CACHE_NAME));
    return;
  }

  // 4️⃣ APIs والبيانات - Network First مع Cache Fallback
  if (request.url.includes('/api/') || request.url.includes('/data/')) {
    event.respondWith(networkFirstStrategy(request, API_CACHE));
    return;
  }

  // 5️⃣ الملفات الأخرى - Stale While Revalidate
  event.respondWith(staleWhileRevalidateStrategy(request));
});

// ============================================
// 📊 استراتيجيات التخزين المؤقت
// ============================================

/**
 * Network First - جرب الشبكة أولاً ثم استخدم Cache
 */
function networkFirstStrategy(request, cacheName = RUNTIME_CACHE) {
  return fetch(request)
    .then(response => {
      // تخزين النسخة الناجحة
      if (response && response.status === 200) {
        const responseClone = response.clone();
        caches.open(cacheName).then(cache => {
          cache.put(request, responseClone);
        });
      }
      console.log(`🌐 Network First - Fresh: ${request.url}`);
      return response;
    })
    .catch(error => {
      // عند فشل الشبكة، استخدم Cache
      console.log(`💾 Network First - Cache Fallback: ${request.url}`);
      return caches.match(request)
        .then(cachedResponse => {
          if (cachedResponse) {
            return cachedResponse;
          }
          
          // إذا كانت صفحة HTML وغير موجودة، أرجع صفحة الخطأ
          if (request.url.includes('.html') || request.url.endsWith('/')) {
            return caches.match('/index.html');
          }
          
          // إذا كانت صورة، أرجع صورة افتراضية
          if (request.url.match(/\.(png|jpg|jpeg|gif|webp|svg)$/i)) {
            return new Response(
              `<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
                <rect fill="#f0f0f0" width="100" height="100"/>
                <text x="50" y="50" font-family="Arial" font-size="14" fill="#999" text-anchor="middle" dy=".3em">Image</text>
              </svg>`,
              { headers: { 'Content-Type': 'image/svg+xml' } }
            );
          }
          
          throw error;
        });
    });
}

/**
 * Cache First - استخدم Cache أولاً ثم الشبكة
 */
function cacheFirstStrategy(request, cacheName = CACHE_NAME) {
  return caches.match(request)
    .then(cachedResponse => {
      if (cachedResponse) {
        console.log(`💾 Cache First - Cached: ${request.url}`);
        return cachedResponse;
      }

      // إذا لم يكن في Cache، جلبه من الشبكة
      return fetch(request)
        .then(response => {
          if (response && response.status === 200) {
            const responseClone = response.clone();
            caches.open(cacheName).then(cache => {
              cache.put(request, responseClone);
            });
          }
          console.log(`🌐 Cache First - Network: ${request.url}`);
          return response;
        })
        .catch(error => {
          console.error(`❌ Cache First - Failed: ${request.url}`, error);
          throw error;
        });
    });
}

/**
 * Stale While Revalidate - استخدم Cache وحدّث في الخلفية
 */
function staleWhileRevalidateStrategy(request) {
  return caches.match(request)
    .then(cachedResponse => {
      const fetchPromise = fetch(request)
        .then(response => {
          if (response && response.status === 200) {
            const responseClone = response.clone();
            caches.open(RUNTIME_CACHE).then(cache => {
              cache.put(request, responseClone);
            });
          }
          return response;
        })
        .catch(error => {
          console.error(`❌ SWR - Failed: ${request.url}`, error);
          return cachedResponse;
        });

      console.log(`♻️ Stale While Revalidate: ${request.url}`);
      return cachedResponse || fetchPromise;
    });
}

// ============================================
// 🔔 PUSH NOTIFICATIONS
// ============================================
self.addEventListener('push', event => {
  console.log('🔔 Service Worker: Push notification received');
  
  const data = event.data ? event.data.json() : {};
  const options = {
    body: data.body || 'إشعار جديد من WiBo Health',
    icon: '/images/icon-512.png',
    badge: '/images/icon-192.png',
    tag: 'wibo-notification',
    requireInteraction: false,
    vibrate: [200, 100, 200],
    data: {
      dateOfArrival: Date.now(),
      url: data.url || '/'
    },
    actions: [
      {
        action: 'open',
        title: 'عرض',
        icon: '/images/icon-192.png'
      },
      {
        action: 'close',
        title: 'إغلاق',
        icon: '/images/icon-192.png'
      }
    ]
  };

  event.waitUntil(
    self.registration.showNotification(data.title || 'WiBo Health', options)
  );
});

// ============================================
// 🖱️ NOTIFICATION CLICK HANDLER
// ============================================
self.addEventListener('notificationclick', event => {
  console.log('🖱️ Service Worker: Notification clicked');
  
  event.notification.close();

  const urlToOpen = event.notification.data.url || '/';

  if (event.action === 'open' || !event.action) {
    event.waitUntil(
      clients.matchAll({ type: 'window' })
        .then(clientList => {
          // تحقق من وجود نافذة مفتوحة بالفعل
          for (let i = 0; i < clientList.length; i++) {
            if (clientList[i].url === urlToOpen && 'focus' in clientList[i]) {
              return clientList[i].focus();
            }
          }
          // إذا لم تكن مفتوحة، افتح نافذة جديدة
          if (clients.openWindow) {
            return clients.openWindow(urlToOpen);
          }
        })
    );
  }
});

// ============================================
// 📨 MESSAGE HANDLER - التواصل مع الصفحة
// ============================================
self.addEventListener('message', event => {
  console.log('📨 Service Worker: Message received:', event.data.type);

  // تحديث Service Worker
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
    event.ports[0].postMessage({ success: true });
  }

  // الحصول على رقم الإصدار
  if (event.data && event.data.type === 'GET_VERSION') {
    event.ports[0].postMessage({ 
      version: CACHE_NAME,
      caches: [CACHE_NAME, RUNTIME_CACHE, IMAGE_CACHE, API_CACHE]
    });
  }

  // حذف جميع الـ Caches
  if (event.data && event.data.type === 'CLEAR_CACHE') {
    event.waitUntil(
      caches.keys()
        .then(cacheNames => {
          return Promise.all(
            cacheNames.map(cacheName => {
              console.log('🗑️ Deleting cache:', cacheName);
              return caches.delete(cacheName);
            })
          );
        })
        .then(() => {
          console.log('✅ All caches cleared');
          event.ports[0].postMessage({ success: true });
        })
        .catch(error => {
          console.error('❌ Failed to clear caches:', error);
          event.ports[0].postMessage({ success: false, error: error.message });
        })
    );
  }

  // تحديث لغة محددة
  if (event.data && event.data.type === 'LANGUAGE_CHANGED') {
    console.log('🌐 Service Worker: Language changed to', event.data.language);
    // يمكن هنا إضافة منطق إضافي عند تغيير اللغة
    event.ports[0].postMessage({ success: true });
  }

  // حذف Cache معين
  if (event.data && event.data.type === 'DELETE_CACHE') {
    event.waitUntil(
      caches.delete(event.data.cacheName)
        .then(deleted => {
          console.log(`Cache ${event.data.cacheName} deleted:`, deleted);
          event.ports[0].postMessage({ success: deleted });
        })
    );
  }

  // الحصول على حجم الـ Cache
  if (event.data && event.data.type === 'GET_CACHE_SIZE') {
    event.waitUntil(
      caches.keys()
        .then(cacheNames => {
          return Promise.all(
            cacheNames.map(cacheName => {
              return caches.open(cacheName)
                .then(cache => {
                  return cache.keys()
                    .then(requests => ({
                      name: cacheName,
                      size: requests.length
                    }));
                });
            })
          );
        })
        .then(cacheInfo => {
          console.log('📊 Cache information:', cacheInfo);
          event.ports[0].postMessage({ caches: cacheInfo });
        })
    );
  }
});

// ============================================
// 🔄 BACKGROUND SYNC
// ============================================
self.addEventListener('sync', event => {
  console.log('🔄 Service Worker: Background sync triggered:', event.tag);

  if (event.tag === 'sync-health-data') {
    event.waitUntil(
      syncHealthData()
        .then(() => {
          console.log('✅ Background sync completed');
        })
        .catch(error => {
          console.error('❌ Background sync failed:', error);
          throw error; // أعد محاولة
        })
    );
  }
});

/**
 * مزامنة بيانات الصحة
 */
function syncHealthData() {
  return Promise.resolve();
  // يمكن إضافة منطق المزامنة هنا
}

// ============================================
// 🔔 تنبيهات إغلاق الإشعار
// ============================================
self.addEventListener('notificationclose', event => {
  console.log('✖️ Service Worker: Notification closed');
});

// ============================================
// 🚀 تسجيل بدء تشغيل Service Worker
// ============================================
console.log('🚀 Service Worker: Loaded successfully');
console.log('📦 Cache Name:', CACHE_NAME);
console.log('⚙️ Runtime Cache:', RUNTIME_CACHE);
console.log('🖼️ Image Cache:', IMAGE_CACHE);
console.log('📡 API Cache:', API_CACHE);
