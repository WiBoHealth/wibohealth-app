/* Crisp callout: a small glass pill above the Crisp launcher (bottom-right).
   - Appears only once Crisp has actually loaded, so it is never a dead button.
   - Click opens the chat; hides while the chat is open and returns when it closes.
   - The x dismisses it for the rest of the browsing session.
   - Text follows <html lang> (ar / nl / en), including live language switches on index.html. */
(function () {
    var TEXT = {
        ar: '💬 هل لديك سؤال؟ دردش معنا',
        nl: '💬 Vragen? Chat met ons',
        en: '💬 Have a question? Chat with us'
    };
    var CLOSE = { ar: 'إغلاق', nl: 'Sluiten', en: 'Close' };
    var KEY = 'wibo_crisp_callout_dismissed';

    var CSS =
        '.wibo-cc{position:fixed;bottom:85px;right:20px;z-index:9999;display:flex;align-items:center;gap:4px;' +
        'padding:6px 6px 6px 14px;border-radius:999px;background:rgba(255,255,255,.78);' +
        '-webkit-backdrop-filter:blur(12px) saturate(160%);backdrop-filter:blur(12px) saturate(160%);' +
        'border:1px solid rgba(16,185,129,.35);box-shadow:0 8px 24px rgba(15,23,42,.14);' +
        'font:600 14px/1.3 "Plus Jakarta Sans","Cairo",system-ui,sans-serif;color:#0f172a;' +
        'opacity:0;transform:translateY(8px);pointer-events:none;transition:opacity .25s ease,transform .25s ease}' +
        '.wibo-cc[dir=rtl]{padding:6px 14px 6px 6px;font-family:"Cairo","Plus Jakarta Sans",system-ui,sans-serif}' +
        '.wibo-cc.is-on{opacity:1;transform:none;pointer-events:auto}' +
        '.wibo-cc::after{content:"";position:absolute;bottom:-6px;right:26px;width:12px;height:12px;' +
        'background:inherit;border-right:inherit;border-bottom:inherit;transform:rotate(45deg);' +
        '-webkit-backdrop-filter:none;backdrop-filter:none}' +
        '.wibo-cc-open{all:unset;cursor:pointer;white-space:nowrap;color:inherit}' +
        '.wibo-cc-open:focus-visible,.wibo-cc-x:focus-visible{outline:2px solid #10b981;outline-offset:3px;border-radius:999px}' +
        '.wibo-cc-x{all:unset;cursor:pointer;display:grid;place-items:center;width:22px;height:22px;border-radius:50%;' +
        'font-size:16px;line-height:1;color:#64748b}' +
        '.wibo-cc-x:hover{background:rgba(100,116,139,.15);color:#0f172a}' +
        'html[data-theme=dark] .wibo-cc{background:rgba(15,23,42,.78);border-color:rgba(52,211,153,.4);' +
        'color:#e2e8f0;box-shadow:0 8px 24px rgba(0,0,0,.45)}' +
        'html[data-theme=dark] .wibo-cc-x{color:#94a3b8}' +
        'html[data-theme=dark] .wibo-cc-x:hover{background:rgba(148,163,184,.2);color:#f1f5f9}' +
        '@media (max-width:480px){.wibo-cc{bottom:80px;right:14px;font-size:13px}}' +
        '@media (prefers-reduced-motion:reduce){.wibo-cc{transition:none}}';

    function dismissed() { try { return sessionStorage.getItem(KEY) === '1'; } catch (e) { return false; } }
    function lang() {
        var l = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2).toLowerCase();
        return TEXT[l] ? l : 'en';
    }

    var el, openBtn, xBtn, ready = false, chatOpen = false;

    function render() {
        var l = lang();
        el.dir = l === 'ar' ? 'rtl' : 'ltr';
        el.lang = l;
        openBtn.textContent = TEXT[l];
        xBtn.setAttribute('aria-label', CLOSE[l]);
    }
    function sync() {
        el.classList.toggle('is-on', ready && !chatOpen && !dismissed());
    }

    function build() {
        var style = document.createElement('style');
        style.textContent = CSS;
        document.head.appendChild(style);

        el = document.createElement('div');
        el.className = 'wibo-cc';
        el.setAttribute('role', 'complementary');
        openBtn = document.createElement('button');
        openBtn.type = 'button';
        openBtn.className = 'wibo-cc-open';
        xBtn = document.createElement('button');
        xBtn.type = 'button';
        xBtn.className = 'wibo-cc-x';
        xBtn.textContent = '×';
        el.appendChild(openBtn);
        el.appendChild(xBtn);
        document.body.appendChild(el);
        render();

        openBtn.addEventListener('click', function () { window.$crisp.push(['do', 'chat:open']); });
        xBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            try { sessionStorage.setItem(KEY, '1'); } catch (err) {}
            sync();
        });
        new MutationObserver(render).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });

        window.$crisp = window.$crisp || [];
        window.$crisp.push(['on', 'session:loaded', function () {
            ready = true;
            try { chatOpen = window.$crisp.is('chat:opened'); } catch (e) {}
            sync();
        }]);
        window.$crisp.push(['on', 'chat:opened', function () { chatOpen = true; sync(); }]);
        window.$crisp.push(['on', 'chat:closed', function () { chatOpen = false; sync(); }]);
    }

    if (dismissed()) return;
    if (document.body) build();
    else document.addEventListener('DOMContentLoaded', build);
})();
