// Supplement comparison on the static supplement indexes (scripts/generate_directory_pages.py). A tick box on each card
// selects it (2 to 5); the comparison shows, side by side, the approved dose, timing, frequency, warnings and interactions
// with medicines of each supplement in the reader's language. Its data (js/supplement-compare-<lang>.js, written by
// generate_supplement_pages.py) is downloaded on the first tick, not with the page.
(function () {
    'use strict';
    var root = document.getElementById('suppCompare');
    if (!root) return;
    var ui = JSON.parse(root.getAttribute('data-ui')), src = root.getAttribute('data-src'), lang = root.getAttribute('data-lang');
    var bar = root.querySelector('.supp-compare-bar'), count = bar.querySelector('.n'), go = bar.querySelector('.go');
    var modal = root.querySelector('.supp-compare-modal'), body = modal.querySelector('.supp-compare-body');
    var picked = [], loading = null, lastFocus = null;

    function load() {
        if (!loading) loading = new Promise(function (resolve) {
            var s = document.createElement('script');
            s.src = src;
            s.onload = s.onerror = function () { resolve(window.SUPP_COMPARE || {}); };
            document.head.appendChild(s);
        });
        return loading;
    }
    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function pageUrl(slug) {
        if (lang === 'ar') return '/supplements/' + slug + '.html';
        return '/' + lang + '/supplements/' + slug + '.html';
    }

    function update() {
        bar.hidden = picked.length === 0;
        count.textContent = picked.length;
        go.disabled = picked.length < 2;
        bar.querySelector('.hint').hidden = picked.length >= 2;
    }

    // the tick boxes sit on the cards: a click on them never opens the supplement page
    document.addEventListener('click', function (e) {
        if (e.target.classList && e.target.classList.contains('supp-pick')) e.stopPropagation();
    }, true);
    document.addEventListener('change', function (e) {
        var box = e.target;
        if (!box.classList || !box.classList.contains('supp-pick')) return;
        e.stopPropagation();
        if (box.checked) {
            if (picked.length >= 5) { box.checked = false; alert(ui.max); return; }
            picked.push(box.value);
            load();
        } else {
            picked = picked.filter(function (s) { return s !== box.value; });
        }
        update();
    });

    bar.querySelector('.clear').addEventListener('click', function () {
        picked = [];
        [].forEach.call(document.querySelectorAll('.supp-pick:checked'), function (b) { b.checked = false; });
        update();
    });

    function list(items) {
        return '<ul>' + items.map(function (w) { return '<li>' + esc(w) + '</li>'; }).join('') + '</ul>';
    }
    function render(data) {
        var rows = picked.map(function (s) { return [s, data[s]]; }).filter(function (r) { return r[1]; });
        var head = rows.map(function (r) {
            var d = r[1];       // [name, icon, area, recommended, timing, frequency, [warnings], interactions]
            return '<th><span class="ic" aria-hidden="true">' + esc(d[1]) + '</span><a href="' + pageUrl(r[0]) + '">' + esc(d[0]) +
                '</a><small>' + esc(d[2]) + '</small></th>';
        }).join('');
        function row(label, icon, cell) {
            return '<tr><th scope="row"><i class="fas ' + icon + '" aria-hidden="true"></i> ' + esc(label) + '</th>' +
                rows.map(function (r) { return '<td>' + cell(r[1]) + '</td>'; }).join('') + '</tr>';
        }
        body.innerHTML = '<div class="supp-compare-scroll"><table><thead><tr><th></th>' + head + '</tr></thead><tbody>' +
            row(ui.rec, 'fa-prescription-bottle', function (d) { return '<strong>' + esc(d[3]) + '</strong>'; }) +
            row(ui.timing, 'fa-clock', function (d) { return esc(d[4]); }) +
            row(ui.freq, 'fa-repeat', function (d) { return esc(d[5]); }) +
            row(ui.inter, 'fa-pills', function (d) { return esc(d[7]); }) +
            row(ui.warnings, 'fa-triangle-exclamation', function (d) { return list(d[6] || []); }) +
            '</tbody></table></div>';
    }

    function open() {
        if (picked.length < 2) return;
        lastFocus = document.activeElement;
        body.innerHTML = '<p class="loading">…</p>';
        modal.hidden = false;
        document.body.style.overflow = 'hidden';
        modal.querySelector('.close').focus();
        load().then(render);
    }
    function close() {
        modal.hidden = true;
        document.body.style.overflow = '';
        if (lastFocus) lastFocus.focus();
    }
    go.addEventListener('click', open);
    modal.querySelector('.close').addEventListener('click', close);
    modal.addEventListener('click', function (e) { if (e.target === modal) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !modal.hidden) close(); });
    update();
})();
