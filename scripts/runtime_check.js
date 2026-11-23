/* Runtime check of the interactive pages in a real (headless) Chrome: JS exceptions, console errors, failed requests,
   and the main interactions (search, sections, cards, modal, comparison, language links).

     python -m http.server 8765 --bind 127.0.0.1      (from the site root, in another terminal)
     node scripts/runtime_check.js [http://127.0.0.1:8765]

   Uses the Chrome DevTools Protocol over Node's built-in WebSocket (Node 22+); no npm packages.
   Exit code 1 when any page has an error or a failed step. */
'use strict';
const { spawn } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

const BASE = process.argv[2] || 'http://127.0.0.1:8765';
const CHROME = process.env.CHROME || [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    '/usr/bin/google-chrome', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find(p => fs.existsSync(p));
const PORT = 9333;
const sleep = ms => new Promise(r => setTimeout(r, ms));

// ---------------------------------------------------------------------------------------------------------------
// interaction steps: JS evaluated in the page; each returns a string (ok) or throws (failure)
const waitFor = (expr, ms = 8000) => `(async () => { const t = Date.now(); while (Date.now() - t < ${ms}) {
    const v = (${expr}); if (v) return v; await new Promise(r => setTimeout(r, 100)); } throw new Error('timeout: ' + ${JSON.stringify(expr)}); })()`;
const FOODS = [
    ['cards render', waitFor(`document.querySelectorAll('a.food-card').length >= 20 && document.querySelectorAll('a.food-card').length`)],
    ['card links a food page', `(() => { const h = document.querySelector('a.food-card').getAttribute('href'); if (!/\\/foods\\/[a-z0-9-]+\\.html$/.test(h)) throw new Error(h); return h; })()`],
    ['search filters', `(async () => { const i = document.getElementById('searchInput'); const before = document.getElementById('resultsCount') ? document.getElementById('resultsCount').textContent : '';
        i.value = 'rice'; i.dispatchEvent(new Event('input', { bubbles: true })); await new Promise(r => setTimeout(r, 900));
        const n = document.querySelectorAll('a.food-card').length; if (!n) throw new Error('no result for rice'); i.value = ''; i.dispatchEvent(new Event('input', { bubbles: true }));
        await new Promise(r => setTimeout(r, 600)); return n + ' cards for "rice"'; })()`],
    ['section switch', `(async () => { const g = document.querySelector('.group-card[data-group="fruits"]'); if (!g) throw new Error('no fruits tile'); g.click();
        await new Promise(r => setTimeout(r, 900)); const n = document.querySelectorAll('a.food-card').length; if (!n) throw new Error('no fruit cards');
        return n + ' fruit cards'; })()`],
    ['static hub links present', `(() => { const n = document.querySelectorAll('.hub-static a').length; if (n < 40) throw new Error(n); return n + ' links'; })()`],
];
const SUPPS = [
    ['cards render', waitFor(`document.querySelectorAll('.supplement-card').length >= 12 && document.querySelectorAll('.supplement-card').length`)],
    ['search filters', `(async () => { const i = document.getElementById('searchInput'); i.value = 'magnes'; i.dispatchEvent(new Event('input', { bubbles: true }));
        await new Promise(r => setTimeout(r, 900)); const n = document.querySelectorAll('.supplement-card').length; if (!n) throw new Error('no result');
        i.value = ''; i.dispatchEvent(new Event('input', { bubbles: true })); await new Promise(r => setTimeout(r, 600)); return n + ' cards for "magnes"'; })()`],
    ['modal opens with full data', `(async () => { document.querySelector('.supplement-card .card-content').click();
        const t = Date.now(); while (Date.now() - t < 8000) { const m = document.getElementById('supplementModal');
        if (m.classList.contains('active') && document.getElementById('modalTitle').textContent.trim() && m.querySelectorAll('li').length) break;
        await new Promise(r => setTimeout(r, 100)); }
        const m = document.getElementById('supplementModal'); if (!m.classList.contains('active')) throw new Error('modal not open');
        const items = m.querySelectorAll('li').length; if (!items) throw new Error('modal without details');
        closeModal(); await new Promise(r => setTimeout(r, 400)); return document.getElementById('modalTitle').textContent.trim().slice(0, 40) + ' / ' + items + ' list items'; })()`],
    ['comparison of 2', `(async () => { const c = document.querySelectorAll('.compare-checkbox'); c[0].click(); c[1].click();
        await new Promise(r => setTimeout(r, 300)); document.getElementById('compareFloatBtn').click();
        const t = Date.now(); while (Date.now() - t < 8000) { if (document.querySelector('#compareModalBody table')) break; await new Promise(r => setTimeout(r, 100)); }
        const rows = document.querySelectorAll('#compareModalBody table tr').length; if (!rows) throw new Error('no comparison table'); return rows + ' rows'; })()`],
];
const HOME = [
    ['language links', `(() => { const a = [...document.querySelectorAll('a.lang-btn')].map(x => x.getAttribute('href')); if (a.length < 3) throw new Error(a); return a.join(' '); })()`],
    ['copy pre-rendered', `(() => { const h = document.querySelector('[data-i18n]'); if (!h || !h.textContent.trim()) throw new Error('empty'); return h.textContent.trim().slice(0, 30); })()`],
    ['tip of the day', `(() => { const b = document.getElementById('homeTipNext'); if (b) b.click(); return 'ok'; })()`],
];
const HUB = [
    ['tool cards link their pages', `(() => { const a = [...document.querySelectorAll('a.hub-card')].map(x => x.getAttribute('href')); if (a.length < 4) throw new Error(a.length); return a.join(' '); })()`],
    ['section tabs', `(() => { const t = document.querySelectorAll('.hub-tabs a').length; if (!t) throw new Error('no tabs'); return t + ' tab(s)'; })()`],
];
const PAGES = [
    ['/calculators.html', HUB], ['/en/calculators.html', HUB], ['/nl/calculators.html', HUB], ['/sv/calculators.html', HUB],
    ['/foods.html', FOODS], ['/en/foods.html', FOODS], ['/nl/foods.html', FOODS], ['/sv/foods.html', FOODS],
    ['/supplements.html', SUPPS], ['/en/supplements.html', SUPPS], ['/nl/supplements.html', SUPPS],
    ['/', HOME], ['/en/index.html', HOME], ['/nl/index.html', HOME], ['/sv/index.html', HOME],
    ['/about.html', []], ['/en/about.html', []], ['/nl/doctor.html', []], ['/en/methodology.html', []], 
    ['/en/contact.html', []], ['/nl/privacy.html', []], ['/en/terms.html', []], ['/en/partners.html', []], ['/en/boodi.html', []],
    ['/en/recipes.html', []], ['/en/insulin-resistance.html', []], ['/nl/thyroid-health.html', []],
    ['/en/foods/apple.html', []], ['/food-details.html?id=1000', [['charts drawn', waitFor("document.querySelectorAll('canvas').length && [...document.querySelectorAll('canvas')].every(c => c.width > 0) && document.querySelectorAll('canvas').length")]]], ['/sv/foods/apple.html', []], ['/nl/supplements/5-htp.html', []], ['/en/articles/fructose-fruit-vs-processed-sugar.html', []],
];

// ---------------------------------------------------------------------------------------------------------------
async function main() {
    if (!CHROME) { console.error('Chrome not found (set CHROME)'); process.exit(2); }
    const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'wibo-rt-'));
    const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
        '--window-size=1280,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
    let target;
    for (let i = 0; i < 50 && !target; i++) {
        try { target = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json(); } catch (e) { await sleep(200); }
    }
    const ws = new WebSocket(target.webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r));
    let id = 0; const pending = new Map(); const listeners = [];
    ws.addEventListener('message', ev => {
        const msg = JSON.parse(ev.data);
        if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg); pending.delete(msg.id); }
        else listeners.forEach(fn => fn(msg));
    });
    const send = (method, params = {}) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
    await send('Runtime.enable'); await send('Log.enable'); await send('Network.enable'); await send('Page.enable');
    // the consent banner and analytics are not part of the test
    await send('Network.setBlockedURLs', { urls: ['*googletagmanager.com*', '*google-analytics.com*', '*googlesyndication.com*', '*/api/geo*'] });

    let failed = 0;
    const report = [];
    for (const [url, steps] of PAGES) {
        const errors = [];
        const onEvent = msg => {
            if (msg.method === 'Runtime.exceptionThrown') errors.push('exception: ' + (msg.params.exceptionDetails.exception?.description || msg.params.exceptionDetails.text).split('\n')[0]);
            if (msg.method === 'Runtime.consoleAPICalled' && msg.params.type === 'error') errors.push('console.error: ' + msg.params.args.map(a => a.value || a.description).join(' ').slice(0, 160));
            if (msg.method === 'Log.entryAdded' && msg.params.entry.level === 'error' && !/blocked|ERR_BLOCKED/i.test(msg.params.entry.text)) errors.push('log: ' + msg.params.entry.text.slice(0, 160) + (msg.params.entry.url ? ' ' + msg.params.entry.url : ''));
            if (msg.method === 'Network.responseReceived' && msg.params.response.status >= 400 && msg.params.response.url.startsWith(BASE)) errors.push(`HTTP ${msg.params.response.status} ${msg.params.response.url}`);
        };
        listeners.push(onEvent);
        const loaded = new Promise(r => { const fn = m => { if (m.method === 'Page.loadEventFired') { listeners.splice(listeners.indexOf(fn), 1); r(); } }; listeners.push(fn); });
        await send('Page.navigate', { url: BASE + url });
        await Promise.race([loaded, sleep(15000)]);
        await sleep(800);
        const results = [];
        for (const [name, expr] of steps) {
            const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
            const ex = r.result?.exceptionDetails;
            if (ex) { results.push(`FAIL ${name}: ${(ex.exception?.description || ex.text).split('\n')[0]}`); failed++; }
            else results.push(`ok   ${name}: ${r.result?.result?.value}`);
        }
        await sleep(300);
        listeners.splice(listeners.indexOf(onEvent), 1);
        if (errors.length) failed++;
        report.push(`${errors.length ? 'FAIL' : 'ok  '} ${url}${errors.length ? '\n       ' + [...new Set(errors)].join('\n       ') : ''}` +
                    (results.length ? '\n       ' + results.join('\n       ') : ''));
    }
    console.log(report.join('\n'));
    console.log(`\nRUNTIME: ${failed ? 'FAILED (' + failed + ')' : 'PASSED'} - ${PAGES.length} pages`);
    ws.close(); chrome.kill();
    try { fs.rmSync(profile, { recursive: true, force: true }); } catch (e) { /* Chrome may still hold files */ }
    process.exit(failed ? 1 : 0);
}
main().catch(e => { console.error(e); process.exit(2); });
