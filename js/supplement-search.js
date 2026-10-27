// Supplement quick search on the static supplement pages and indexes (scripts/generate_supplement_pages.py and
// generate_directory_pages.py). Finds a supplement by its Arabic, English, Dutch or Swedish name and links to its page in
// the reader's language (Swedish: the Swedish page when there is one, else English). On an index it also filters the cards.
// The names (js/supplement-search-data.js) are downloaded on the first focus or keystroke, not with the page.
(function () {
    'use strict';
    var box = document.querySelector('.supp-search');
    if (!box) return;
    var input = box.querySelector('input'), list = box.querySelector('.supp-search-results');
    var lang = box.getAttribute('data-lang') || 'ar', noHits = box.getAttribute('data-none') || '';
    var data = null, loading = null;

    function load() {
        if (!loading) loading = new Promise(function (resolve) {
            var s = document.createElement('script');
            s.src = box.getAttribute('data-src');
            s.onload = s.onerror = function () { data = window.SUPP_SEARCH || []; resolve(); };
            document.head.appendChild(s);
        });
        return loading;
    }

    // lower case, no Arabic diacritics, one form of alef / ya / ta marbuta, Latin accents removed
    function norm(t) {
        return String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ًͯ-ْـ]/g, '')
            .replace(/[أإآ]/g, 'ا').replace(/ى/g, 'ي').replace(/ة/g, 'ه').replace(/\s+/g, ' ').trim();
    }

    function url(it) {                      // it = [slug, ar, en, nl, sv, icon]
        if (lang === 'ar') return '/supplements/' + it[0] + '.html';
        if (lang === 'sv') return (it[4] ? '/sv' : '/en') + '/supplements/' + it[0] + '.html';
        return '/' + lang + '/supplements/' + it[0] + '.html';
    }
    function label(it) {
        return ({ ar: it[1], en: it[2], nl: it[3], sv: it[4] || it[2] })[lang] || it[2];
    }
    function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

    var cards = [].slice.call(document.querySelectorAll('.dir-list li'));      // index pages only
    function slugOf(li) { var m = /\/supplements\/([^\/]+)\.html$/.exec(li.querySelector('a').getAttribute('href')); return m && m[1]; }

    function run() {
        var q = norm(input.value);
        if (!q) { list.hidden = true; list.innerHTML = ''; cards.forEach(function (li) { li.hidden = false; }); return; }
        var hits = data.filter(function (it) { return norm(it.slice(1, 5).join(' | ')).indexOf(q) !== -1; });
        if (cards.length) {
            var keep = {};
            hits.forEach(function (it) { keep[it[0]] = 1; });
            cards.forEach(function (li) { li.hidden = !keep[slugOf(li)]; });
        }
        list.innerHTML = hits.length
            ? hits.slice(0, 8).map(function (it) {
                return '<li><a href="' + url(it) + '"><span aria-hidden="true">' + esc(it[5]) + '</span>' + esc(label(it)) + '</a></li>';
            }).join('')
            : '<li class="none">' + esc(noHits) + '</li>';
        list.hidden = false;
    }

    input.addEventListener('focus', load);
    input.addEventListener('input', function () { load().then(run); });
    input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') { var a = list.querySelector('a'); if (a) { e.preventDefault(); location.href = a.href; } }
        if (e.key === 'Escape') { input.value = ''; run(); }
    });
    document.addEventListener('click', function (e) { if (!box.contains(e.target)) list.hidden = true; });
})();
