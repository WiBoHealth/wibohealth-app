// Toggle Theme
function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const icon = document.querySelector('.theme-toggle i');
    
    if (document.body.classList.contains('dark-mode')) {
        icon.className = 'fas fa-sun';
        localStorage.setItem('wibo_theme', 'dark');
    } else {
        icon.className = 'fas fa-moon';
        localStorage.setItem('wibo_theme', 'light');
    }
}

// Toggle Mobile Menu
function toggleMobileMenu() {
    const mobileNav = document.getElementById('mobileNav');
    const body = document.body;
    
    mobileNav.classList.toggle('active');
    body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
}

// Load theme on page load
window.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('wibo_theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        document.querySelector('.theme-toggle i').className = 'fas fa-sun';
    }
});

// PWA Install
let deferredPrompt;
const installButton = document.getElementById('install-button');

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    
    if (installButton) {
        installButton.style.display = 'block';
    }
});

if (installButton) {
    installButton.addEventListener('click', async () => {
        if (!deferredPrompt) return;
        
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        
        console.log(`User response: ${outcome}`);
        deferredPrompt = null;
        installButton.style.display = 'none';
    });
}