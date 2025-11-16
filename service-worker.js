const CACHE_NAME = 'wibohealth-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/foods.html',
  '/calculators.html',
  '/recipes.html',
  '/doctor.html',
  '/articles.html',
  '/css/style.css',
  '/css/mobile-menu.css',
  '/js/main.js',
  '/js/data.js',
  '/js/mobile-menu.js',
  '/images/logo.png',
  '/images/icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
