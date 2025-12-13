// Emergency Service Worker Disabler
// This file forcefully unregisters ALL service workers

if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then(function(registrations) {
    for(let registration of registrations) {
      console.log('🗑️ Unregistering Service Worker:', registration);
      registration.unregister();
    }
    console.log('✅ All Service Workers removed!');
    
    // Clear all caches
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          console.log('🗑️ Deleting cache:', cacheName);
          return caches.delete(cacheName);
        })
      );
    }).then(function() {
      console.log('✅ All caches cleared!');
      alert('✅ Cache cleared successfully! Please refresh the page.');
    });
  });
}
