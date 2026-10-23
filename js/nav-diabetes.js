// Header link to the Diabetes & Metabolic Health hub on the hand-written root pages.
// The hub is a static page per language (/diabetes.html, /en/diabetes.html, /nl/diabetes.html), so the link and its label
// follow <html lang>, which every page's own language switcher sets.
(function () {
    var HUB = {
        ar: ['/diabetes.html', 'السكري ومتلازمة الأيض'],
        en: ['/en/diabetes.html', 'Diabetes'],
        nl: ['/nl/diabetes.html', 'Diabetes'],
        sv: ['/en/diabetes.html', 'Diabetes']   // English hub until /sv/diabetes.html exists (phase 2)
    };

    function apply() {
        var v = HUB[(document.documentElement.lang || 'ar').slice(0, 2)] || HUB.ar;
        document.querySelectorAll('a.nav-diabetes').forEach(function (a) {
            a.setAttribute('href', v[0]);
            var label = a.querySelector('.nav-diabetes-label');
            if (label && label.textContent !== v[1]) label.textContent = v[1];
        });
    }

    apply();
    document.addEventListener('DOMContentLoaded', apply);
    new MutationObserver(apply).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });
})();
