"""Build the static Swedish homepage /sv/index.html from the root index.html.

The root homepage serves ar/en/nl on one URL through its inline `translations` dictionary and ?lang=.
Swedish gets its own indexable file instead: this script copies index.html, swaps the dictionary for the
Swedish one in homepage_sv.py, pre-renders every data-i18n element in Swedish (so the HTML is Swedish
without JavaScript), makes all links absolute (the page lives one folder down) and points pages that have
no Swedish version yet at their English version.

Run after every change to index.html:  python scripts/generate_sv_homepage.py
Every replacement checks that its anchor is still there and stops with an error otherwise.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from homepage_sv import ALT, FOOTER_SOURCES, MEALS, META, T, TIPS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'index.html'
OUT = ROOT / 'sv' / 'index.html'
URL = 'https://wibohealth.com/sv/index.html'
ARABIC = re.compile(r'[؀-ۿ]')


def sub(pattern, repl, text, count=1, flags=0, what=None):
    """re.sub that fails unless the pattern matched exactly `count` times (count=0: at least once)."""
    new, n = re.subn(pattern, repl, text, flags=flags)
    if (count and n != count) or n == 0:
        sys.exit('generate_sv_homepage: %s matched %d times (expected %s)' % (what or pattern[:60], n, count or '1+'))
    return new


def rep(old, new, text, count=1):
    n = text.count(old)
    if n != count:
        sys.exit('generate_sv_homepage: %r found %d times (expected %d)' % (old[:60], n, count))
    return text.replace(old, new)


def attr(value):
    return html.escape(value, quote=True)


def head(t):
    t = rep('<html lang="ar" dir="rtl">', '<html lang="sv" dir="ltr">', t)
    # language boot: this page is always Swedish
    t = sub(r'<script>\s*\(function \(d\) \{\s*var h = d\.documentElement;.*?\}\)\(document\);\s*</script>',
            '<script>document.documentElement.lang = \'sv\'; document.documentElement.dir = \'ltr\'; '
            'window.wiboLangReady = function () {};</script>', t, flags=re.S, what='language boot script')
    t = sub(r'<title>.*?</title>', '<title>%s</title>' % html.escape(META['title']), t, what='title')
    for name in ('title', 'description', 'keywords'):
        t = sub(r'<meta name="%s" content="[^"]*">' % name,
                '<meta name="%s" content="%s">' % (name, attr(META[name])), t, what='meta ' + name)
    t = rep('<link rel="canonical" href="https://wibohealth.com/">', '<link rel="canonical" href="%s">' % URL, t)
    t = rep('    <!-- EN/NL are served on this same URL via ?lang (no hreflang for them); Swedish has its own static page -->\n',
            '', t)
    t = rep('<meta property="og:url" content="https://wibohealth.com/">', '<meta property="og:url" content="%s">' % URL, t)
    t = rep('<meta name="twitter:url" content="https://wibohealth.com/">', '<meta name="twitter:url" content="%s">' % URL, t)
    t = rep('<meta property="og:locale" content="ar_AR">', '<meta property="og:locale" content="sv_SE">', t)
    for prop, key in (('og:title', 'og_title'), ('og:description', 'og_description')):
        t = sub(r'<meta property="%s" content="[^"]*">' % prop,
                '<meta property="%s" content="%s">' % (prop, attr(META[key])), t, what=prop)
    for name, key in (('twitter:title', 'twitter_title'), ('twitter:description', 'twitter_description')):
        t = sub(r'<meta name="%s" content="[^"]*">' % name,
                '<meta name="%s" content="%s">' % (name, attr(META[key])), t, what=name)
    t = rep('<script src="/js/consent.js?v=1" defer></script>', '<script src="/js/consent.js?v=2" defer></script>', t)
    return t


def language_engine(t):
    keys = re.findall(r"^\s*'([a-z0-9_]+)':", t[t.index('const translations = {'):t.index('function detectInitialLang')], re.M)
    missing = sorted(set(keys) - set(T))
    if missing:
        sys.exit('generate_sv_homepage: Swedish copy missing for ' + ', '.join(missing))
    sv = json.dumps(T, ensure_ascii=False, indent=16)[:-1] + '            }'
    t = sub(r'const translations = \{.*?\n        \};\n', 'const translations = {\n            sv: %s\n        };\n' % sv,
            t, flags=re.S, what='translations dictionary')
    t = sub(r'function detectInitialLang\(\) \{.*?\n        \}\n', "function detectInitialLang() {\n            return 'sv';\n        }\n",
            t, flags=re.S, what='detectInitialLang')
    # the other languages live on the root homepage; the choice is stored there as usual
    t = rep("        function changeLanguage(lang) {\n            currentLang = lang;\n            localStorage.setItem('preferred_language', lang);\n            localStorage.setItem('wibo_language', lang);\n",
            "        function changeLanguage(lang) {\n            if (lang !== 'sv') { location.href = '/?lang=' + lang; return; }\n            currentLang = lang;\n", t)
    return t


def switcher(t):
    old = re.search(r'( *)<button class="lang-btn" data-lang-toggle="ar".*?title="Svenska">🇸🇪</a>\n', t, re.S)
    if not old:
        sys.exit('generate_sv_homepage: language switcher not found')
    pad = old.group(1)
    new = ''.join(pad + line + '\n' for line in (
        '<a class="lang-btn" href="/?lang=ar" hreflang="ar" lang="ar" title="العربية">🇪🇬</a>',
        '<a class="lang-btn" href="/?lang=en" hreflang="en" lang="en" title="English">🇬🇧</a>',
        '<a class="lang-btn" href="/?lang=nl" hreflang="nl" lang="nl" title="Nederlands">🇳🇱</a>',
        '<button class="lang-btn active" data-lang-toggle="sv" aria-current="true" title="Svenska">🇸🇪</button>'))
    return t[:old.start()] + new + t[old.end():]


def prerender(t):
    """Write the Swedish text into every data-i18n element, as updatePageLanguage() would."""
    def text(m):
        tag, attrs, key, inner = m.groups()
        if re.search(r'<%s[\s>]' % tag, inner):
            sys.exit('generate_sv_homepage: nested <%s> inside data-i18n="%s"' % (tag, key))
        return '<%s%s>%s</%s>' % (tag, attrs, T[key], tag)
    t = sub(r'<([a-z0-9]+)(\s[^>]*?\bdata-i18n="([a-z0-9_]+)"[^>]*)>(.*?)</\1>', text,
            t, count=0, flags=re.S, what='data-i18n elements')

    def attribute(name, target, also=None):
        def fix(m):
            tag = m.group(0)
            value = attr(T[m.group(1)])
            for a in (target, also) if also else (target,):   # not the data-i18n-* attribute of the same name
                tag = re.sub(r'(?<![-\w])%s="[^"]*"' % a, lambda _: '%s="%s"' % (a, value), tag, count=1)
            return tag
        return lambda s: sub(r'<[a-z]+[^>]*\b%s="([a-z0-9_]+)"[^>]*>' % name, fix, s, count=0, flags=re.S, what=name)
    for name, target, also in (('data-i18n-href', 'href', None), ('data-i18n-alt', 'alt', None),
                               ('data-i18n-placeholder', 'placeholder', 'aria-label')):
        t = attribute(name, target, also)(t)
    return t


def links(t):
    """The page lives in /sv/: absolute URLs everywhere, and pages without a Swedish version open in English."""
    # CSS selector on the doctor link (its href gains ?lang=en below)
    t = rep('html[data-theme="dark"] a[href="doctor.html"]', 'html[data-theme="dark"] a[href^="/doctor.html"]', t)
    body = t.index('<body>')

    def fix(m):
        name, url = m.group(1), m.group(2)
        if re.match(r'(https?:|mailto:|tel:|data:|#|/en/|/nl/|/sv/|//)', url):
            return m.group(0)
        if url == '/':
            return '%s="/sv/index.html"' % name
        if not url.startswith('/'):
            url = '/' + url
        path = url.split('#')[0].split('?')[0]
        if name == 'href' and path.endswith('.html') and m.start() > body:
            url = re.sub(r'^([^#]*?)(\?[^#]*)?(#.*)?$',
                         lambda p: p.group(1) + (p.group(2) + '&' if p.group(2) else '?') + 'lang=en' + (p.group(3) or ''), url)
        return '%s="%s"' % (name, url)
    t = re.sub(r'\b(href|src|srcset)="([^"]+)"', lambda m: fix(m) if ' ' not in m.group(2) else m.group(0), t)
    t = re.sub(r'srcset="([^"]+)"', lambda m: 'srcset="%s"' % ', '.join(
        (p if p.startswith('/') else '/' + p) for p in m.group(1).split(', ')), t)
    # the static directory pages come in ar/en/nl: Swedish readers get the English index
    t = rep("a.href = (l === 'en' || l === 'nl' ? '/' + l : '') + '/'",
            "a.href = (l === 'en' || l === 'nl' ? '/' + l : l === 'sv' ? '/en' : '') + '/'", t)
    # the food search matches English (and Arabic/Dutch) names: open the guide in English
    t = rep('<form class="meals-search" action="/foods.html" method="get" role="search">',
            '<form class="meals-search" action="/foods.html" method="get" role="search">\n'
            '        <input type="hidden" name="lang" value="en">', t)
    return t


def localise_rest(t):
    # floating chat button: one Swedish label
    t = sub(r'<span data-l="ar">[^<]*</span><span data-l="en">[^<]*</span><span data-l="nl">[^<]*</span>',
            '<span data-l="sv">Chatta med oss</span>', t, what='chat labels')
    t = rep('html[lang="nl"] .wibo-chat-btn [data-l="nl"]{display:inline}',
            'html[lang="nl"] .wibo-chat-btn [data-l="nl"],html[lang="sv"] .wibo-chat-btn [data-l="sv"]{display:inline}', t)
    # meal strip: only the Swedish row
    t = sub(r'\n *<div class="meals-track" data-lang="(ar|en|nl)" lang="\1">.*?\n *</div>\n *</div>', '', t,
            count=3, flags=re.S, what='meal tracks')
    pills = '\n'.join(
        '                        <a href="%s" class="meals-pill"><span class="pulse-ico" aria-hidden="true">%s</span>'
        '<span>%s</span><span class="meals-gi">%s%s</span></a>'
        % (href, ico, html.escape(name), band, '' if gi is None else ' <span dir="ltr">≈%d</span>' % gi)
        for href, ico, name, band, gi in MEALS)
    t = rep('            <div class="pulse-viewport">\n            </div>',
            '            <div class="pulse-viewport">\n                <div class="meals-track" data-lang="sv" lang="sv">\n'
            '                    <div class="pulse-set">\n%s\n                    </div>\n                </div>\n            </div>' % pills, t)
    t = rep('html[lang="nl"] .meals-track[data-lang="nl"] { display: flex; }',
            'html[lang="nl"] .meals-track[data-lang="nl"],\n        html[lang="sv"] .meals-track[data-lang="sv"] { display: flex; }', t)
    t = rep("{ ar: ['السابق', 'التالي'], nl: ['Vorige', 'Volgende'], en: ['Previous', 'Next'] }",
            "{ sv: ['Föregående', 'Nästa'], en: ['Previous', 'Next'] }", t)
    # tip of the day
    tips = json.dumps(TIPS, ensure_ascii=False, indent=20)[:-1].rstrip() + '\n                ]'
    t = sub(r'var TIPS = \{\n.*?\n            \};', lambda _: 'var TIPS = {\n                sv: %s\n            };' % tips,
            t, flags=re.S, what='tips')
    t = rep("var NEXT = { ar: 'النصيحة التالية', en: 'Next tip', nl: 'Volgende tip' };", "var NEXT = { sv: 'Nästa tips' };", t)
    t = rep('TIPS[currentLang]) ? currentLang : \'ar\'', 'TIPS[currentLang]) ? currentLang : \'sv\'', t)
    t = rep('id="homeTipNext" aria-label="النصيحة التالية"', 'id="homeTipNext" aria-label="Nästa tips"', t)
    t = rep('title="المظهر"', 'title="Byt tema"', t)
    # diabetes capsule (js/nav-diabetes.js sets the same at runtime)
    t = rep('href="/diabetes.html?lang=en" class="nav-link nav-diabetes"', 'href="/en/diabetes.html" class="nav-link nav-diabetes"', t)
    t = rep('href="/diabetes.html?lang=en" class="mobile-nav-link nav-diabetes"', 'href="/en/diabetes.html" class="mobile-nav-link nav-diabetes"', t)
    t = rep('<span class="nav-diabetes-label">السكري ومتلازمة الأيض</span>', '<span class="nav-diabetes-label">Diabetes</span>', t, count=2)
    # Arabic image alts without an i18n key
    for src, alt in ALT.items():
        t = sub(r'(<img [^>]*src="/%s"[^>]*alt=")[^"]*(")' % re.escape(src), r'\g<1>%s\2' % attr(alt).replace('\\', r'\\'),
                t, flags=re.S, what='alt ' + src)
    t = rep('aria-label="WiBo Health highlights"', 'aria-label="WiBo Health – höjdpunkter"', t)
    t = rep('aria-label="What\'s cooking today"', 'aria-label="Vad blir det till middag"', t)
    # the three long nutrition guides are Arabic-only: not on the Swedish page
    t = sub(r'\n *<h3 class="home-articles-h3" data-i18n="home_articles_guides">.*?\n            </div>\n(?=        </section>)', '\n',
            t, flags=re.S, what='Arabic long guides')
    # footer
    t = sub(r'<h4 style="color: #10b981; margin-bottom: 15px; font-size: 1\.1em;">📚 المصادر العلمية</h4>.*?</p>',
            FOOTER_SOURCES, t, flags=re.S, what='footer sources')
    t = sub(r'💚 مُطور بـ (<span[^>]*>♥</span>) من أجل بودي', r'💚 Utvecklad med \1 för boodi', t, what='footer credit')
    return t


def check(t):
    """No Arabic outside scripts, except the language-switcher label."""
    visible = re.sub(r'<script\b.*?</script>|<!--.*?-->|/\*.*?\*/', '', t, flags=re.S)
    visible = visible.replace('title="العربية"', '')
    left = sorted({line.strip()[:90] for line in visible.split('\n') if ARABIC.search(line)})
    if left:
        sys.exit('generate_sv_homepage: Arabic text left on the Swedish page:\n  ' + '\n  '.join(left))
    if 'data-i18n="' in t and re.search(r'data-i18n="(?!(%s)")' % '|'.join(T), t):
        sys.exit('generate_sv_homepage: data-i18n key without Swedish copy')


def main():
    t = SRC.read_text(encoding='utf-8-sig')
    t = head(t)
    t = language_engine(t)
    t = switcher(t)
    t = prerender(t)
    t = links(t)
    t = localise_rest(t)
    check(t)
    OUT.parent.mkdir(exist_ok=True)
    t = rep('<!DOCTYPE html>\n', '<!DOCTYPE html>\n<!-- Generated by scripts/generate_sv_homepage.py from index.html '
            '+ scripts/homepage_sv.py; edit those, not this file. -->\n', t)
    OUT.write_text(t, encoding='utf-8', newline='\n')
    print('wrote', OUT.relative_to(ROOT), '(%d bytes)' % OUT.stat().st_size)


if __name__ == '__main__':
    main()
