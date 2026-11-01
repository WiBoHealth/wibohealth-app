/* boodi app waitlist (boodi.html + sv/boodi.html).
 * Saves {email, lang, consent} in the boodi Supabase project (Frankfurt), table public.waitlist.
 * Only the public anon/publishable key belongs here: RLS allows INSERT only, nobody can read,
 * change or delete rows from the browser (SQL: scripts/sql/boodi_waitlist.sql).
 * NEVER put the service_role / secret key in this file.
 * A duplicate email (409 / 23505) shows the same thank-you message (user decision 2026-11-01). */
(function () {
    var SUPABASE_URL = 'https://yfmjhlhxifgcqqtkuzva.supabase.co';
    var SUPABASE_ANON_KEY = 'sb_publishable_UX16vJP6NI41imgfFoSPmw_s-KSjeD2';   // publishable key - public by design, RLS = insert only

    var MSG = {
        ar: { thanks: 'شكراً لك! سنرسل لك رسالة واحدة عند إطلاق تطبيق بودي.',
              invalid: 'يرجى إدخال بريد إلكتروني صحيح.',
              error: 'تعذّر التسجيل الآن. يرجى المحاولة لاحقاً.' },
        en: { thanks: 'Thank you! We’ll send you one email when boodi launches.',
              invalid: 'Please enter a valid email address.',
              error: 'We couldn’t sign you up right now. Please try again later.' },
        nl: { thanks: 'Bedankt! We sturen je één e-mail zodra boodi wordt gelanceerd.',
              invalid: 'Vul een geldig e-mailadres in.',
              error: 'Aanmelden lukt nu niet. Probeer het later opnieuw.' },
        sv: { thanks: 'Tack! Vi skickar ett enda mejl när boodi lanseras.',
              invalid: 'Ange en giltig e-postadress.',
              error: 'Det gick inte att anmäla dig just nu. Försök igen senare.' }
    };
    var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    var loadedAt = Date.now();

    function pageLang(form) {
        var l = (form.getAttribute('data-lang') || document.documentElement.lang || 'ar').slice(0, 2).toLowerCase();
        return MSG[l] ? l : 'en';
    }

    function init(form) {
        var email = form.querySelector('input[type="email"]');
        var consent = form.querySelector('input[type="checkbox"][name="consent"]');
        var trap = form.querySelector('input[name="website"]');
        var btn = form.querySelector('button[type="submit"]');
        var out = form.querySelector('.waitlist-msg');
        var busy = false;

        function sync() { btn.disabled = busy || !consent.checked; }
        function say(kind, text) {
            out.textContent = text;
            out.className = 'waitlist-msg ' + kind;
        }
        function done(m) {
            form.classList.add('is-done');
            say('ok', m.thanks);
        }

        consent.addEventListener('change', sync);
        sync();

        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var lang = pageLang(form), m = MSG[lang];
            if (busy || !consent.checked) return;
            var value = (email.value || '').trim().toLowerCase();
            if (value.length > 254 || !EMAIL_RE.test(value)) { say('err', m.invalid); email.focus(); return; }
            // honeypot filled in, or sent faster than a person can type: act as if it worked, send nothing
            if ((trap && trap.value) || Date.now() - loadedAt < 2000) { done(m); return; }
            if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
                if (window.console) console.warn('boodi waitlist: SUPABASE_URL / SUPABASE_ANON_KEY not set');
                say('err', m.error); return;
            }
            busy = true; sync(); say('', '');
            var headers = { 'Content-Type': 'application/json', 'apikey': SUPABASE_ANON_KEY, 'Prefer': 'return=minimal' };
            if (SUPABASE_ANON_KEY.indexOf('eyJ') === 0) headers.Authorization = 'Bearer ' + SUPABASE_ANON_KEY;
            fetch(SUPABASE_URL.replace(/\/+$/, '') + '/rest/v1/waitlist', {
                method: 'POST', headers: headers,
                body: JSON.stringify({ email: value, lang: lang, consent: true })
            }).then(function (r) {
                if (r.ok || r.status === 409) { done(m); return; }          // 409 = already on the list
                return r.json().catch(function () { return {}; }).then(function (j) {
                    if (j && j.code === '23505') done(m);
                    else if (j && j.code === '23514') say('err', m.invalid);   // database email check
                    else say('err', m.error);
                });
            }).catch(function () { say('err', m.error); })
              .then(function () { busy = false; sync(); });
        });
    }

    function start() {
        var forms = document.querySelectorAll('form.boodi-waitlist');
        for (var i = 0; i < forms.length; i++) init(forms[i]);
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
    else start();
})();
