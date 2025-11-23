// Service Worker for WiBo Health PWA
// Version 2.1.0

const CACHE_NAME = 'wibo-health-v2.1.0';
const RUNTIME_CACHE = 'wibo-health-runtime';

// الملفات الأساسية للتخزين المؤقت (Cache)
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/foods.html',
  '/calculators.html',
  '/recipes.html',
  '/articles.html',
  '/doctor.html',
  '/pricing.html',
  '/about.html',
  '/contact.html',
  '/css/style.css',
  '/css/mobile-menu.css',
  '/js/main.js',
  '/js/data.js',
  '/js/mobile-menu.js',
  '/manifest.json'
];

// 🔧 التثبيت: تخزين الملفات الأساسية
self.addEventListener('install', event => {
  console.log('✅ Service Worker: Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('📦 Service Worker: Caching app shell');
        return cache.addAll(PRECACHE_URLS);
      })
      .then(() => {
        console.log('✅ Service Worker: Installed successfully');
        return self.skipWaiting(); // تفعيل فوري
      })
  );
});

// 🔄 التفعيل: تنظيف Cache القديم
self.addEventListener('activate', event => {
  console.log('🔄 Service Worker: Activating...');
  
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME && cacheName !== RUNTIME_CACHE) {
            console.log('🗑️ Service Worker: Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      console.log('✅ Service Worker: Activated successfully');
      return self.clients.claim(); // التحكم بجميع الصفحات
    })
  );
});

// 📡 Fetch: استراتيجية Cache First مع Network Fallback
self.addEventListener('fetch', event => {
  // تجاهل الطلبات الخارجية (CDN, APIs)
  if (!event.request.url.startsWith(self.location.origin)) {
    return;
  }

  // تجاهل طلبات غير GET
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    caches.match(event.request)
      .then(cachedResponse => {
        // إذا موجود في Cache، استخدمه
        if (cachedResponse) {
          console.log('💾 Service Worker: Serving from cache:', event.request.url);
          
          // جلب نسخة جديدة في الخلفية (Update in background)
          fetch(event.request).then(networkResponse => {
            if (networkResponse && networkResponse.status === 200) {
              caches.open(RUNTIME_CACHE).then(cache => {
                cache.put(event.request, networkResponse);
              });
            }
          }).catch(() => {
            // تجاهل أخطاء الشبكة في التحديث الخلفي
          });

          return cachedResponse;
        }

        // إذا مش موجود، جيبه من الشبكة
        console.log('🌐 Service Worker: Fetching from network:', event.request.url);
        return fetch(event.request).then(networkResponse => {
          // تخزين النسخة الجديدة
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(RUNTIME_CACHE).then(cache => {
              cache.put(event.request, responseClone);
            });
          }
          return networkResponse;
        }).catch(error => {
          console.error('❌ Service Worker: Fetch failed:', error);
          
          // صفحة offline بديلة
          if (event.request.destination === 'document') {
            return caches.match('/index.html');
          }
          
          throw error;
        });
      })
  );
});

// 🔔 Push Notifications (للمستقبل)
self.addEventListener('push', event => {
  console.log('🔔 Service Worker: Push notification received');
  
  const options = {
    body: event.data ? event.data.text() : 'إشعار جديد من WiBo Health',
    icon: '/images/icon-512.png',
    badge: '/images/icon-512.png',
    vibrate: [200, 100, 200],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'عرض',
        icon: '/images/icon-512.png'
      },
      {
        action: 'close',
        title: 'إغلاق',
        icon: '/images/icon-512.png'
      }
    ]
  };

  event.waitUntil(
    self.registration.showNotification('WiBo Health', options)
  );
});

// 🖱️ Notification Click Handler
self.addEventListener('notificationclick', event => {
  console.log('🖱️ Service Worker: Notification clicked');
  
  event.notification.close();

  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});

// 🔄 Background Sync (للمستقبل)
self.addEventListener('sync', event => {
  console.log('🔄 Service Worker: Background sync triggered');
  
  if (event.tag === 'sync-data') {
    event.waitUntil(
      // يمكن إضافة كود لمزامنة البيانات هنا
      Promise.resolve()
    );
  }
});

// 📊 Message Handler (للتواصل مع الصفحة)
self.addEventListener('message', event => {
  console.log('📨 Service Worker: Message received:', event.data);
  
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'GET_VERSION') {
    event.ports[0].postMessage({ version: CACHE_NAME });
  }
});

console.log('🚀 Service Worker: Loaded successfully - Version:', CACHE_NAME);
