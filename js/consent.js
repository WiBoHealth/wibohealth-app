/* WiBo Health cookie consent (Google Consent Mode v2).
 * The <head> of every page sets all consent types to 'denied' before gtag.js loads and re-applies a stored 'granted'.
 * This file shows the banner when no choice is stored yet, saves the choice and updates consent.
 * wiboConsent.open() reopens the banner (privacy page "Cookie settings" button). */
(function () {
    'use strict';
    var KEY = 'wibo_consent';
    var TYPES = ['ad_storage', 'ad_user_data', 'ad_personalization', 'analytics_storage'];
    var TEXT = {
        ar: {
            title: 'ملفات تعريف الارتباط (الكوكيز)',
            body: 'نستخدم Google Analytics لقياس الزيارات وتحسين الموقع، وقد تُستخدم كوكيز Google للإعلانات. لن نفعّل هذه الكوكيز إلا بموافقتك، ويمكنك تغيير اختيارك في أي وقت من صفحة الخصوصية.',
            more: 'سياسة الخصوصية',
            accept: 'أوافق',
            reject: 'أرفض'
        },
        en: {
            title: 'Cookies',
            body: 'We use Google Analytics to measure visits and improve the site, and Google may use cookies for advertising. These cookies are only switched on with your consent, and you can change your choice at any time on the privacy page.',
            more: 'Privacy policy',
            accept: 'Accept',
            reject: 'Reject'
        },
        nl: {
            title: 'Cookies',
            body: 'We gebruiken Google Analytics om bezoeken te meten en de site te verbeteren, en Google kan cookies gebruiken voor advertenties. Deze cookies worden alleen geplaatst met jouw toestemming, en je kunt je keuze op elk moment wijzigen op de privacypagina.',
            more: 'Privacybeleid',
            accept: 'Accepteren',
            reject: 'Weigeren'
        }
    };

    function stored() {
        try { return localStorage.getItem(KEY); } catch (e) { return null; }
    }

    function lang() {
        var q = /[?&]lang=(ar|en|nl)\b/.exec(location.search);
        if (q) return q[1];
        var l = (document.documentElement.getAttribute('lang') || 'ar').slice(0, 2).toLowerCase();
        return TEXT[l] ? l : 'ar';
    }

    function apply(value) {
        var update = {};
        TYPES.forEach(function (t) { update[t] = value; });
        if (typeof window.gtag === 'function') window.gtag('consent', 'update', update);
    }

    function save(value) {
        try { localStorage.setItem(KEY, value); } catch (e) { /* private mode: the choice lasts for this page only */ }
        apply(value);
        close();
    }

    function close() {
        var el = document.getElementById('wibo-consent');
        if (el) el.parentNode.removeChild(el);
    }

    var CSS =
        '#wibo-consent{position:fixed;left:16px;right:16px;bottom:16px;z-index:2147483000;margin:0 auto;max-width:560px;' +
        'background:#ffffff;color:#0f172a;border:1px solid rgba(15,23,42,.14);border-radius:16px;padding:16px 18px;' +
        'box-shadow:0 12px 40px rgba(15,23,42,.28);font-size:14px;line-height:1.6;font-family:inherit}' +
        'html[data-theme="dark"] #wibo-consent{background:#1e293b;color:#e2e8f0;border-color:rgba(226,232,240,.18)}' +
        '#wibo-consent h2{margin:0 0 6px;font-size:16px;font-weight:800;color:inherit}' +
        '#wibo-consent p{margin:0 0 12px;color:inherit;opacity:.92}' +
        '#wibo-consent a{color:#059669;font-weight:700;text-decoration:underline}' +
        'html[data-theme="dark"] #wibo-consent a{color:#34d399}' +
        '#wibo-consent .wc-btns{display:flex;gap:10px;flex-wrap:wrap}' +
        '#wibo-consent button{flex:1 1 140px;min-height:44px;border-radius:12px;font:inherit;font-weight:800;cursor:pointer;' +
        'border:2px solid #059669;padding:8px 14px}' +
        '#wibo-consent .wc-accept{background:#059669;color:#ffffff}' +
        '#wibo-consent .wc-reject{background:transparent;color:inherit}' +
        '#wibo-consent button:focus-visible{outline:3px solid #34d399;outline-offset:2px}';

    function open() {
        if (document.getElementById('wibo-consent')) return;
        var l = lang(), t = TEXT[l];
        if (!document.getElementById('wibo-consent-css')) {
            var s = document.createElement('style');
            s.id = 'wibo-consent-css';
            s.textContent = CSS;
            document.head.appendChild(s);
        }
        var box = document.createElement('section');
        box.id = 'wibo-consent';
        box.setAttribute('role', 'dialog');
        box.setAttribute('aria-labelledby', 'wibo-consent-title');
        box.setAttribute('lang', l);
        box.setAttribute('dir', l === 'ar' ? 'rtl' : 'ltr');
        var href = '/privacy.html' + (l === 'ar' ? '' : '?lang=' + l) + '#cookies';
        box.innerHTML =
            '<h2 id="wibo-consent-title">' + t.title + '</h2>' +
            '<p>' + t.body + ' <a href="' + href + '">' + t.more + '</a></p>' +
            '<div class="wc-btns">' +
            '<button type="button" class="wc-accept">' + t.accept + '</button>' +
            '<button type="button" class="wc-reject">' + t.reject + '</button>' +
            '</div>';
        box.querySelector('.wc-accept').addEventListener('click', function () { save('granted'); });
        box.querySelector('.wc-reject').addEventListener('click', function () { save('denied'); });
        document.body.appendChild(box);
    }

    window.wiboConsent = { open: open, get: stored };

    if (stored() !== 'granted' && stored() !== 'denied') {
        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', open);
        else open();
    }
})();
