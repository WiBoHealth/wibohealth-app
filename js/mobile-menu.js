/* ========================================
   Mobile Menu JavaScript
   ======================================== */

// Toggle Mobile Menu
function toggleMobileMenu() {
    const mobileNav = document.getElementById('mobileNav');
    const overlay = document.querySelector('.mobile-nav-overlay');
    const body = document.body;
    
    if (mobileNav && overlay) {
        mobileNav.classList.toggle('active');
        overlay.classList.toggle('active');
        body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
    }
}

// Close menu when clicking on a link (optional - for better UX)
document.addEventListener('DOMContentLoaded', function() {
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');
    mobileLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Close menu after a short delay to allow navigation
            setTimeout(toggleMobileMenu, 200);
        });
    });
});
