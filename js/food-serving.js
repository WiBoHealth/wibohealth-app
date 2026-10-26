// Food pages (scripts/generate_food_pages.py): portion selector and folded introduction.
// Zero dependencies. Every number marked [data-v100] holds its value per 100 g; picking a portion rewrites it as
// value x grams / 100. The page is complete without this script: the HTML already shows the medium portion.
(function () {
    'use strict';

    // Same output as fmt() in the generator: Python round(x, 1) (exact value, ties to even), no trailing ".0"
    function round1(x) {
        if (Number.isInteger(x * 4) && (x * 4) % 2 === 1) {             // exact tie such as 0.25 or 1.75
            var t = Math.floor(x * 10);
            return (t % 2 === 0 ? t : t + 1) / 10;
        }
        return +x.toFixed(1);
    }
    function round0(x) {                                                  // Python round(x): ties to even
        var f = Math.floor(x);
        if (x - f === 0.5) return f % 2 === 0 ? f : f + 1;
        return Math.round(x);
    }

    var card = document.getElementById('macroCard');
    if (card) {
        var d = card.dataset;
        var dec = d.dec || '.';
        var levels = (d.levels || '').split('|');
        var nums = document.querySelectorAll('[data-v100]');
        var glNum = document.getElementById('glNum'), glBadge = document.getElementById('glBadge'),
            glSub = document.getElementById('glSub'), col = document.getElementById('colServing'),
            live = document.getElementById('servingLive');
        var colDefault = col ? col.textContent : '';
        var fmt = function (x) { return String(round1(x)).replace('.', dec); };

        var apply = function (input) {
            var g = +input.value, factor = g / 100;
            for (var i = 0; i < nums.length; i++) {
                var v = +nums[i].getAttribute('data-v100') * factor;
                nums[i].textContent = nums[i].hasAttribute('data-int') ? round0(v) : fmt(v);
            }
            if (d.gi && glNum) {                                          // GL = GI x available carbs in the portion / 100
                var gl = round1(+d.gi * +d.avail * factor / 100);
                var l = gl <= 10 ? 0 : (gl < 20 ? 1 : 2), cls = ['low', 'medium', 'high'][l];
                glNum.textContent = fmt(gl);
                glNum.className = 'gi-num ' + cls;
                glBadge.textContent = levels[l];
                glBadge.className = 'badge ' + cls;
                glSub.textContent = d.glTpl.replace('{p}', g);
            }
            var label = input.getAttribute('data-label');
            if (col) col.textContent = input.hasAttribute('data-default') ? colDefault : input.getAttribute('data-col');
            if (live) live.textContent = label;
        };
        card.addEventListener('change', function (e) {
            if (e.target && e.target.name === 'serving') apply(e.target);
        });
    }

    // Back to the food guide: a reader who came from foods.html goes back in history, so the browser (or foods.html
    // itself) returns to the same place in the list; anyone else (search engine, shared link) follows the link.
    document.addEventListener('click', function (e) {
        var a = e.target.closest && e.target.closest('a[data-back]');
        if (!a || e.defaultPrevented || e.button || e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
        var ref = null;
        try { ref = new URL(document.referrer); } catch (err) { return; }
        if (ref.origin === location.origin && /^\/foods(\.html)?$/.test(ref.pathname) && history.length > 1) {
            e.preventDefault();
            history.back();
        }
    });

    // Introduction: two lines and a "read more" button; the full text stays in the HTML for readers and search engines
    var fold = document.getElementById('leadFold');
    if (fold) {
        var lead = fold.querySelector('.lead'), btn = fold.querySelector('.more-btn');
        fold.classList.add('clamped');
        if (lead.scrollHeight > lead.clientHeight + 2) {
            btn.hidden = false;
            btn.addEventListener('click', function () {
                var open = fold.classList.toggle('clamped') === false;
                btn.setAttribute('aria-expanded', open ? 'true' : 'false');
                btn.textContent = open ? btn.getAttribute('data-less') : btn.getAttribute('data-more');
            });
        } else {
            fold.classList.remove('clamped');
        }
    }
})();
