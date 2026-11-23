"""One registry of the site's page URLs per language, shared by every generator.

Every page has a static, indexable URL per language: Arabic at the root, English in /en/, Dutch in /nl/ and Swedish
in /sv/. There are no ?lang= pages any more; old ?lang= links get a 301 in vercel.json (ROOT_PAGES drives those
rules too, see scripts/generate_root_pages.py).

ROOT_PAGES: the hand-written Arabic pages at the root (the masters) and their language versions.
  'en' / 'nl'  written by scripts/generate_root_pages.py from the master's own translation dictionary
  'sv'         a Swedish page written by another generator (article / site-page / homepage generators) or, for the
               interactive food guide, by generate_root_pages.py
A language that is missing has no version: links in that language open the English page.
"""

SITE = 'https://wibohealth.com'
LANGS = ('ar', 'en', 'nl', 'sv')
X_DEFAULT = 'en'          # hreflang x-default of every page cluster on the site (2026-11-23)


def _mirror(path, sv=None, langs=('en', 'nl')):
    """A root page whose English/Dutch versions mirror its file name: /about.html -> /en/about.html."""
    out = {'ar': path}
    for l in langs:
        out[l] = f'/{l}{path}'
    if sv:
        out['sv'] = sv
    return out


ROOT_PAGES = {
    '/': {'ar': '/', 'en': '/en/index.html', 'nl': '/nl/index.html', 'sv': '/sv/index.html'},
    '/about.html': _mirror('/about.html', '/sv/om-oss.html'),
    '/doctor.html': _mirror('/doctor.html', '/sv/dr-wassim-habib.html'),
    '/methodology.html': _mirror('/methodology.html', '/sv/metodik.html'),
    '/foods.html': _mirror('/foods.html', '/sv/foods.html', langs=('en', 'nl', 'sv')),
    '/supplements.html': _mirror('/supplements.html'),
    '/boodi.html': _mirror('/boodi.html', '/sv/boodi.html'),
    '/calculators.html': _mirror('/calculators.html', '/sv/calculators.html'),
    '/recipes.html': _mirror('/recipes.html', langs=('en',)),
    '/partners.html': _mirror('/partners.html', '/sv/partners.html'),
    '/contact.html': _mirror('/contact.html', '/sv/kontakt.html'),
    '/privacy.html': _mirror('/privacy.html', '/sv/integritetspolicy.html'),
    '/terms.html': _mirror('/terms.html', '/sv/anvandarvillkor.html'),
    '/insulin-resistance.html': _mirror('/insulin-resistance.html', '/sv/articles/insulinresistens-hba1c.html'),
    '/leptin-resistance.html': _mirror('/leptin-resistance.html', '/sv/articles/leptinresistens.html'),
    '/cortisol-stress.html': _mirror('/cortisol-stress.html', '/sv/articles/kortisol-och-stress.html'),
    '/intermittent-fasting.html': _mirror('/intermittent-fasting.html', '/sv/articles/periodisk-fasta.html'),
    '/magnesium-types.html': _mirror('/magnesium-types.html', '/sv/articles/magnesiumformer.html'),
    '/bone-health-minerals.html': _mirror('/bone-health-minerals.html', '/sv/articles/skeletthalsa-och-mineraler.html'),
    '/thyroid-health.html': _mirror('/thyroid-health.html', '/sv/articles/trog-skoldkortel.html'),
}

# pages with static versions written by other generators (calculators, the fatty liver guide, the Diabetes hub);
# the root URL of the fatty liver guide is itself a 301 to /articles/
OTHER_PAGES = {
    **{f'/{c}-calculator.html': {'ar': f'/{c}-calculator.html', **{l: f'/{l}/{c}-calculator.html' for l in ('en', 'nl', 'sv')}}
       for c in ('bmi', 'tdee', 'water', 'whtr')},
    '/fatty-liver.html': {'ar': '/articles/fatty-liver-and-visceral-fat.html',
                          **{l: f'/{l}/articles/fatty-liver-and-visceral-fat.html' for l in ('en', 'nl', 'sv')}},
    '/diabetes.html': {'ar': '/diabetes.html', **{l: f'/{l}/diabetes.html' for l in ('en', 'nl', 'sv')}},
    '/supplements/index.html': {'ar': '/supplements/index.html', **{l: f'/{l}/supplements/index.html' for l in ('en', 'nl', 'sv')}},
    '/foods/index.html': {'ar': '/foods/index.html', **{l: f'/{l}/foods/index.html' for l in ('en', 'nl', 'sv')}},
}

# pages that exist in Arabic only and are kept out of the index (noindex): links in other languages open the Arabic page
ARABIC_ONLY = {'/diet-plan.html', '/calorie-tracker.html', '/delete-account.html', '/disclaimer.html', '/image-credits.html'}


# links only (not hreflang alternates): the closest page for a language that has no version of the page itself
LINK_ONLY = {
    '/supplements.html': {'sv': '/sv/supplements/index.html'},   # no Swedish interactive guide: the Swedish index
}


def versions(path):
    """{lang: path} of a known page, or None."""
    return ROOT_PAGES.get(path) or OTHER_PAGES.get(path)


def url_in(path, lang):
    """The page `path` (an Arabic root path, optionally with #fragment or a legacy ?lang=xx query) in `lang`:
    the static page of that language, else the English one, else the path itself. Never returns a ?lang= URL."""
    bare, hash_, frag = path.partition('#')
    bare = bare.split('?', 1)[0] or '/'
    if bare == '/index.html':
        bare = '/'
    v = versions(bare)
    if lang in LINK_ONLY.get(bare, {}):
        out = LINK_ONLY[bare][lang]
    elif v:
        out = v.get(lang) or v.get('en') or v['ar']
    else:
        out = bare
    return out + (hash_ + frag if frag else '')


def lang_of_url(path):
    """Language of a static path: /en/... -> en, /nl/... -> nl, /sv/... -> sv, everything else Arabic."""
    for l in ('en', 'nl', 'sv'):
        if path == f'/{l}' or path.startswith(f'/{l}/'):
            return l
    return 'ar'


def cluster_of(path):
    """The language cluster ({lang: path}) that contains the static path `path` (any language), or None."""
    for v in list(ROOT_PAGES.values()) + list(OTHER_PAGES.values()):
        if path in v.values():
            return v
    return None
