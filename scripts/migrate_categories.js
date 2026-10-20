/**
 * One-off migration: adds `group` (10 master groups), `categoryEn` and `cuisine` to every record
 * in js/data.js, and fixes the misfiled items found in the category audit.
 *
 * Edits the file line by line (one record per line), so comments and formatting stay as they are.
 * Idempotent: fields written by an earlier run are stripped and rewritten.
 *
 *   node scripts/migrate_categories.js            # write js/data.js
 *   node scripts/migrate_categories.js --dry-run  # print the distribution only
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DATA = path.join(__dirname, '..', 'js', 'data.js');
const DRY = process.argv.includes('--dry-run');

// Fine category (AR) -> NL, EN and default group. Cuisine categories also carry a cuisine tag.
const CATEGORIES = {
    'حبوب':           { nl: 'Granen',                  en: 'Grains & Starches',           group: 'grains_bakery' },
    'مخبوزات':        { nl: 'Bakkerij',                en: 'Bakery & Bread',              group: 'grains_bakery' },
    'فواكه':          { nl: 'Fruit',                   en: 'Fruits',                      group: 'fruits' },
    'خضروات':         { nl: 'Groenten',                en: 'Vegetables',                  group: 'vegetables' },
    'سلطات':          { nl: 'Salades',                 en: 'Salads',                      group: 'vegetables' },
    'معلبات':         { nl: 'Conserven',               en: 'Canned & Preserved',          group: 'vegetables' },
    'بروتين':         { nl: 'Eiwitten',                en: 'Proteins & Meat',             group: 'proteins_legumes' },
    'بقوليات':        { nl: 'Peulvruchten',            en: 'Legumes & Pulses',            group: 'proteins_legumes' },
    'أطعمة نباتية':   { nl: 'Plantaardig',             en: 'Plant-Based',                 group: 'proteins_legumes' },
    'ألبان':          { nl: 'Zuivel',                  en: 'Dairy & Cheese',              group: 'dairy_alternatives' },
    'مكسرات':         { nl: 'Noten & Zaden',           en: 'Nuts & Seeds',                group: 'fats_nuts' },
    'زيوت':           { nl: 'Oliën & Vetten',          en: 'Oils & Fats',                 group: 'fats_nuts' },
    'أطعمة عربية':    { nl: 'Arabische Gerechten',     en: 'Arabic Cuisine',              group: 'meals_cuisines', cuisine: 'Arab' },
    'أطعمة آسيوية':   { nl: 'Aziatische Keuken',       en: 'Asian Cuisine',               group: 'meals_cuisines', cuisine: 'Asian' },
    'أطعمة مكسيكية':  { nl: 'Mexicaanse Keuken',       en: 'Mexican Cuisine',             group: 'meals_cuisines', cuisine: 'Mexican' },
    'أطعمة لاتينية':  { nl: 'Latijns-Amerikaans',      en: 'Latin American Cuisine',      group: 'meals_cuisines', cuisine: 'Latin American' },
    'أطعمة سورينامية وإندونيسية': { nl: 'Surinaams & Indisch', en: 'Surinamese & Indonesian', group: 'meals_cuisines' },
    'أطعمة إيطالية':  { nl: 'Italiaanse Keuken',       en: 'Italian Cuisine',             group: 'meals_cuisines', cuisine: 'Italian' },
    'أطعمة يونانية':  { nl: 'Griekse Keuken',          en: 'Greek Cuisine',               group: 'meals_cuisines', cuisine: 'Greek' },
    'أطعمة تركية':    { nl: 'Turkse Keuken',           en: 'Turkish Cuisine',             group: 'meals_cuisines', cuisine: 'Turkish' },
    'أطعمة مغربية':   { nl: 'Marokkaanse Keuken',      en: 'Moroccan Cuisine',            group: 'meals_cuisines', cuisine: 'Moroccan' },
    'أطعمة إسبانية':  { nl: 'Spaanse Keuken',          en: 'Spanish Cuisine',             group: 'meals_cuisines', cuisine: 'Spanish' },
    'أطعمة فرنسية':   { nl: 'Franse Keuken',           en: 'French Cuisine',              group: 'meals_cuisines', cuisine: 'French' },
    'أطعمة هولندية':  { nl: 'Nederlandse Keuken',      en: 'Dutch Cuisine',               group: 'meals_cuisines', cuisine: 'Dutch' },
    'مطاعم':          { nl: 'Fastfood',                en: 'Fast Food',                   group: 'meals_cuisines', cuisine: 'Fastfood' },
    'وجبات منزلية':   { nl: 'Huisgemaakte Maaltijden', en: 'Home Cooked Meals',           group: 'meals_cuisines', cuisine: 'Home Meals' },
    'سندويشات':       { nl: 'Broodjes',                en: 'Sandwiches & Wraps',          group: 'meals_cuisines' },
    'شوربات':         { nl: 'Soepen',                  en: 'Soups',                       group: 'meals_cuisines' },
    'حلويات':         { nl: 'Desserts',                en: 'Desserts & Sweets',           group: 'snacks_desserts' },
    'وجبات خفيفة':    { nl: 'Snacks',                  en: 'Snacks',                      group: 'snacks_desserts' },
    'سكريات':         { nl: 'Suikers',                 en: 'Sugars & Syrups',             group: 'snacks_desserts' },
    'محليات':         { nl: 'Zoetstoffen',             en: 'Sweeteners',                  group: 'snacks_desserts' },
    'مشروبات':        { nl: 'Dranken',                 en: 'Beverages',                   group: 'beverages' },
    'مشروبات كحولية': { nl: 'Alcoholische Dranken',    en: 'Alcoholic Beverages',         group: 'beverages' },
    'صلصات':          { nl: 'Sauzen',                  en: 'Sauces & Dips',               group: 'pantry_spices' },
    'بهارات':         { nl: 'Specerijen',              en: 'Spices & Herbs',              group: 'pantry_spices' },
    'مكونات الطهي':   { nl: 'Voorraadkast',            en: 'Pantry Staples',              group: 'pantry_spices' },
    'مكملات':         { nl: 'Supplementen',            en: 'Supplements & Superfoods',    group: 'pantry_spices' },
};

// Fine-category corrections: id -> new AR category (NL/EN follow from CATEGORIES).
const SOUPS = [126, 175, 179, 185, 207, 208, 209, 210, 211, 212, 213, 308, 446, 447, 454, 477, 509, 518,
    545, 547, 668, 808, 809, 810, 883, 888, 889, 892, 1035, 1051, 1053, 1056];
const RECATEGORY = {
    244: 'حبوب', 245: 'حبوب',                          // almond / coconut flour were filed as supplements
    285: 'مكونات الطهي', 985: 'مكونات الطهي', 998: 'مكونات الطهي', // vinegar, xanthan gum, gelatin
    600: 'مكونات الطهي',                                 // orange blossom water is a flavouring, not a drink
    796: 'وجبات خفيفة',                                  // oat digestive biscuits were filed as grains
    1025: 'محليات', 1026: 'محليات', 1027: 'محليات', 1028: 'محليات', 1029: 'محليات',
    // AR said "Mexican" while NL said Latin American: split them 1:1
    651: 'أطعمة لاتينية', 652: 'أطعمة لاتينية', 653: 'أطعمة لاتينية', 654: 'أطعمة لاتينية',
    655: 'أطعمة لاتينية', 657: 'أطعمة لاتينية', 658: 'أطعمة لاتينية',
    // NL said Surinaams & Indisch while AR said fast food / Asian
    901: 'أطعمة سورينامية وإندونيسية', 904: 'أطعمة سورينامية وإندونيسية',
    906: 'أطعمة سورينامية وإندونيسية', 907: 'أطعمة سورينامية وإندونيسية',
};
// 656 tamales, 659 quesadilla and 660 chimichanga are Mexican: AR stays, NL goes back to Mexicaanse Keuken.

// Group overrides where the fine category's default group is wrong for the item.
const GROUP = {
    243: 'proteins_legumes', 983: 'proteins_legumes', 999: 'proteins_legumes', 1000: 'proteins_legumes', // protein powders
    186: 'proteins_legumes', 187: 'proteins_legumes',  // tofu, tempeh
    286: 'snacks_desserts',                            // protein bar
    580: 'fats_nuts',                                  // cod liver oil
    135: 'dairy_alternatives',                         // almond milk
    188: 'vegetables',                                 // kimchi
    738: 'pantry_spices',                              // makdous, with the other pickles
    756: 'snacks_desserts',                            // Eid kaak (holiday sweet bread)
    439: 'pantry_spices', 440: 'pantry_spices',        // peeled tomatoes, passata
};

const CUISINE = {
    492: 'Moroccan', 901: 'Surinamese', 904: 'Surinamese', 906: 'Asian', 907: 'Asian',
    651: 'Latin American', 652: 'Latin American', 653: 'Latin American', 654: 'Latin American',
    655: 'Latin American', 657: 'Latin American', 658: 'Latin American',
};
// Soups keep their cuisine from the category they came from.
// Outside cuisine categories, the name's first word may give one (e.g. "Dutch Syrup Waffle").
const NAME_CUISINE = [
    [/^(Dutch|Frisian|Limburg)/, 'Dutch'], [/^(Moroccan)/, 'Moroccan'], [/^(Turkish)/, 'Turkish'],
    [/^(Greek)/, 'Greek'], [/^(Italian|Sicilian)/, 'Italian'], [/^(French)/, 'French'], [/^(Spanish)/, 'Spanish'],
    [/^(Japanese|Korean|Thai|Indian|Indonesian|Chinese|Vietnamese|Malaysian)/, 'Asian'],
    [/^(Levantine|Damascene|Egyptian|Iraqi|Emirati|Gulf|Palestinian|Syrian|Yemeni|Saudi|Arabic|Aleppian)/, 'Arab'],
    [/^(Surinamese)/, 'Surinamese'], [/^(Mexican)/, 'Mexican'], [/^(Argentine|Brazilian|Peruvian|Colombian)/, 'Latin American'],
];

const src = fs.readFileSync(DATA, 'utf8');
const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(src + ';this.__db = foodsDatabase;', ctx);
const byId = new Map(ctx.__db.map(f => [f.id, f]));

function migrate(food) {
    const oldCat = food.category;
    const category = SOUPS.includes(food.id) ? 'شوربات' : (RECATEGORY[food.id] || oldCat);
    const meta = CATEGORIES[category];
    if (!meta) throw new Error(`id ${food.id}: no mapping for category "${category}"`);
    let cuisine = CUISINE[food.id] || meta.cuisine || (CATEGORIES[oldCat] && CATEGORIES[oldCat].cuisine) || '';
    if (!cuisine) {
        const hit = NAME_CUISINE.find(([re]) => re.test(food.nameEn));
        if (hit) cuisine = hit[1];
    }
    return { category, categoryNl: meta.nl, categoryEn: meta.en, group: GROUP[food.id] || meta.group, cuisine };
}

const esc = s => s.replace(/\\/g, '\\\\').replace(/'/g, "\\'");
let touched = 0;
const out = src.split('\n').map(line => {
    const m = line.match(/^\s*\{\s*id:\s*(\d+),/);
    if (!m) return line;
    const food = byId.get(Number(m[1]));
    const r = migrate(food);
    const clean = line.replace(/ categoryEn: '(?:[^'\\]|\\.)*',| group: '(?:[^'\\]|\\.)*',| cuisine: '(?:[^'\\]|\\.)*',/g, '');
    const fields = `category: '${esc(r.category)}', categoryNl: '${esc(r.categoryNl)}', categoryEn: '${esc(r.categoryEn)}', group: '${r.group}',`
        + (r.cuisine ? ` cuisine: '${esc(r.cuisine)}',` : '');
    const next = clean.replace(/category: '(?:[^'\\]|\\.)*', categoryNl: '(?:[^'\\]|\\.)*',/, fields);
    if (next === clean) throw new Error(`id ${food.id}: category fields not found`);
    touched++;
    return next;
}).join('\n');

// Re-parse the result and check it before writing anything.
const check = { window: {} };
vm.createContext(check);
vm.runInContext(out + ';this.__db = foodsDatabase;', check);
const db = check.__db;
const GROUPS = ['fruits', 'vegetables', 'grains_bakery', 'proteins_legumes', 'dairy_alternatives',
    'fats_nuts', 'meals_cuisines', 'snacks_desserts', 'beverages', 'pantry_spices'];
if (touched !== db.length || db.length !== byId.size) throw new Error(`record count changed: ${touched}/${db.length}/${byId.size}`);
for (const f of db) {
    if (!GROUPS.includes(f.group)) throw new Error(`id ${f.id}: bad group ${f.group}`);
    if (!f.categoryEn || !f.categoryNl || !f.category) throw new Error(`id ${f.id}: missing category label`);
    const before = byId.get(f.id);
    for (const k of ['name', 'nameEn', 'nameNl', 'gi', 'ii', 'image'])
        if (before[k] !== f[k]) throw new Error(`id ${f.id}: ${k} changed`);
}
const pairs = new Map();
for (const f of db) {
    const key = f.category;
    const val = f.categoryNl + ' | ' + f.categoryEn;
    if (pairs.has(key) && pairs.get(key) !== val) throw new Error(`category "${key}" maps to two labels`);
    pairs.set(key, val);
}

const count = (k) => db.reduce((m, f) => (m[f[k] || '(none)'] = (m[f[k] || '(none)'] || 0) + 1, m), {});
const sorted = o => Object.entries(o).sort((a, b) => b[1] - a[1]);
console.log(`records: ${db.length}`);
console.log('\ngroups:');
GROUPS.forEach(g => console.log(`  ${String(count('group')[g] || 0).padStart(4)}  ${g}`));
console.log(`\nfine categories: ${pairs.size}`);
sorted(count('category')).forEach(([c, n]) => console.log(`  ${String(n).padStart(4)}  ${c} | ${pairs.get(c)}`));
console.log('\ncuisine:');
sorted(count('cuisine')).forEach(([c, n]) => console.log(`  ${String(n).padStart(4)}  ${c}`));

if (DRY) {
    console.log('\n(dry run, nothing written)');
} else {
    fs.writeFileSync(DATA, out, 'utf8');
    console.log(`\nwrote ${DATA}`);
}
