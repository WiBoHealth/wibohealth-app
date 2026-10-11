"""
WiBo Health - Batch Asset Pipeline (Batch 2: Items 51 to 150)
Target: 100 Foods (Public Domain / Wikimedia Cached Thumbnails)
Format: WebP (350x350) + Auto Update data.js
"""

import os
import re
import json
import time
import urllib.request
import urllib.error
import urllib.parse
from PIL import Image

OUTPUT_DIR = os.path.join("images", "foods")
os.makedirs(OUTPUT_DIR, exist_ok=True)
DATA_FILE = os.path.join("js", "data.js")

# تصحيح ذكي لمصطلحات الأطعمة الأكثر شيوعاً لتحسين دقة الصور
CULINARY_ALIASES = {
    'mandarin': 'Mandarin orange',
    'clementine': 'Clementine',
    'grapefruit': 'Grapefruit',
    'lemon': 'Lemon',
    'lime': 'Lime (fruit)',
    'strawberries': 'Strawberry',
    'blueberries': 'Blueberry',
    'raspberries': 'Raspberry',
    'blackberries': 'Blackberry',
    'cherries': 'Cherry',
    'grapes': 'Grape',
    'watermelon': 'Watermelon',
    'cantaloupe': 'Cantaloupe',
    'melon': 'Melon',
    'peach': 'Peach',
    'nectarine': 'Nectarine',
    'apricot': 'Apricot',
    'plum': 'Plum',
    'pear': 'Pear',
    'kiwi': 'Kiwifruit',
    'mango': 'Mango',
    'pineapple': 'Pineapple',
    'papaya': 'Papaya',
    'pomegranate': 'Pomegranate',
    'figs': 'Common fig',
    'dates': 'Date palm',
    'avocado': 'Avocado',
    'boiled egg': 'Boiled egg',
    'fried egg': 'Fried egg',
    'chicken breast': 'Chicken breast',
    'grilled chicken': 'Roast chicken',
    'beef': 'Beef',
    'steak': 'Steak',
    'salmon': 'Salmon as food',
    'tuna': 'Tuna',
    'sardines': 'Sardines as food',
    'shrimp': 'Shrimp as food',
    'milk': 'Milk',
    'cheddar cheese': 'Cheddar cheese',
    'mozzarella': 'Mozzarella',
    'feta cheese': 'Feta',
    'greek yogurt': 'Strained yogurt',
    'olive oil': 'Olive oil'
}

def make_slug(name):
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', name).strip().lower()
    return re.sub(r'\s+', '-', clean)

def fetch_authentic_food_image(food_name_en):
    clean_name = food_name_en.split('(')[0].strip().lower()
    search_term = CULINARY_ALIASES.get(clean_name, food_name_en.split('(')[0].strip())
    
    encoded = urllib.parse.quote(search_term.replace(' ', '_'))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    
    headers = {
        'User-Agent': 'WiBoHealthBot/2.0 (Clinical Diet Guide; support@wibohealth.com)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode())
            if "thumbnail" in data and "source" in data["thumbnail"]:
                return data["thumbnail"]["source"]
            elif "originalimage" in data and "source" in data["originalimage"]:
                return data["originalimage"]["source"]
    except Exception:
        pass
    return None

def process_batch_2():
    if not os.path.exists(DATA_FILE):
        print(f"[!] ملف {DATA_FILE} غير موجود!")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"\{\s*id:\s*(\d+).*?nameEn:\s*['\"]([^'\"]+)['\"].*?\}", re.DOTALL)
    matches = list(pattern.finditer(content))

    total_items = len(matches)
    batch_start = 50   # يبدأ من العنصر رقم 51 (فهرس 50)
    batch_end = min(150, total_items) # حتى العنصر 150

    print(f"[*] جاري معالجة الدفعة الثانية: من الصنف {batch_start + 1} إلى الصنف {batch_end} (إجمالي: {batch_end - batch_start} صنفاً)...")
    
    count_updated = 0
    for match in matches[batch_start:batch_end]:
        food_id = int(match.group(1))
        name_en = match.group(2).strip()
        slug = make_slug(name_en)
        dest_filename = f"{slug}.webp"
        dest_path = os.path.join(OUTPUT_DIR, dest_filename)
        rel_path = f"images/foods/{dest_filename}"

        # إذا كانت الصورة موجودة مسبقاً، نربطها فقط إذا لم تكن مربوطة
        if os.path.exists(dest_path):
            old_block = match.group(0)
            if "image:" not in old_block:
                new_block = re.sub(r"(nameNl:\s*['\"][^'\"]+['\"],)", rf"\1 image: '{rel_path}',", old_block)
                content = content.replace(old_block, new_block)
                count_updated += 1
            continue

        time.sleep(1.2)  # حماية السيرفر من الحظر
        img_url = fetch_authentic_food_image(name_en)

        if img_url:
            try:
                temp_file = os.path.join(OUTPUT_DIR, f"temp_{slug}.jpg")
                req = urllib.request.Request(img_url, headers={'User-Agent': 'WiBoHealthBot/2.0'})
                with urllib.request.urlopen(req, timeout=15) as resp, open(temp_file, 'wb') as out_f:
                    out_f.write(resp.read())
                
                with Image.open(temp_file) as im:
                    im = im.convert("RGB")
                    width, height = im.size
                    min_dim = min(width, height)
                    left = (width - min_dim) / 2
                    top = (height - min_dim) / 2
                    im_cropped = im.crop((left, top, left + min_dim, top + min_dim))
                    im_resized = im_cropped.resize((350, 350), Image.Resampling.LANCZOS)
                    im_resized.save(dest_path, "WEBP", quality=82)

                if os.path.exists(temp_file):
                    os.remove(temp_file)

                # تحديث السطر داخل ملف data.js
                old_block = match.group(0)
                if "image:" not in old_block:
                    new_block = re.sub(r"(nameNl:\s*['\"][^'\"]+['\"],)", rf"\1 image: '{rel_path}',", old_block)
                    content = content.replace(old_block, new_block)
                    count_updated += 1
                
                print(f"  [✓] الصنف {food_id} ({name_en}) -> تم حفظ {dest_filename}")

            except Exception as e:
                print(f"  [-] الصنف {food_id} ({name_en}) -> خطأ تنزيل: {e}")
        else:
            print(f"  [-] الصنف {food_id} ({name_en}) -> سيبقى بالإيموجي")

    # حفظ ملف data.js المحدث
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n[🎉] اكتملت الدفعة الثانية بنجاح! تم تحديث الأصناف وحفظ الصور في {OUTPUT_DIR}.")

# عناوين ويكيبيديا الدقيقة للأصناف الناقصة في الدفعة الأولى (1-150)
# كل صنف له عنوان أساسي وعناوين بديلة تُجرَّب بالترتيب
MISSING_FOOD_TITLES = {
    42: ['Asparagus'],
    62: ['Medjool', 'Date palm'],
    63: ['Deglet Nour', 'Date palm'],
    70: ['Skimmed milk', 'Milk'],
    71: ['Strained yogurt'],
    75: ['Gouda cheese'],
    77: ['Halloumi'],
    80: ['Almond'],
    85: ['Chia seed'],
    86: ['Flax'],
    87: ['Pumpkin seed'],
    88: ['Sunflower seed'],
    90: ['Peanut butter'],
    91: ['Chicken as food'],
    92: ['Steak'],
    93: ['Lamb and mutton'],
    94: ['Salmon as food'],
    98: ['Canned tuna', 'Canned fish'],
    99: ['Sardines as food'],
    100: ['Shrimp and prawn as food'],
    102: ['Omelette'],
    103: ['Liver (food)'],
    104: ['Hummus'],
    110: ['Mulukhiyah'],
    112: ['Shawarma'],
    113: ['Shish taouk'],
    114: ['Kofta'],
    115: ['Kibbeh'],
    116: ['Kibbeh nayyeh', 'Kibbeh'],
    118: ['Mahshi', 'Dolma'],
    119: ['Mansaf'],
    122: ['Fatteh'],
    123: ['Sayadieh'],
    124: ['Musakhan'],
    126: ['Lentil soup'],
    127: ['Kushari'],
    129: ['Ghee', 'Clarified butter'],
    130: ['Coconut oil'],
    131: ['Tahini'],
    132: ['Espresso'],
    134: ['Matcha'],
    135: ['Almond milk'],
    137: ['Coconut water'],
    138: ['Orange juice'],
    139: ['Pomegranate juice'],
    144: ['Pizza Margherita'],
    145: ['Pepperoni'],
    146: ['Submarine sandwich'],
    149: ['Knafeh'],
}

def fetch_wiki_summary(title):
    """يجلب ملخص صفحة ويكيبيديا مع إعادة محاولة متزايدة عند 429"""
    encoded = urllib.parse.quote(title.replace(' ', '_'))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'WiBoHealthBot/2.0 (Clinical Diet Guide; support@wibohealth.com)'
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 3:
                return None
            time.sleep(10 * (attempt + 1))
        except Exception:
            return None
    return None

def wiki_thumb_url(data):
    # نستخدم المصغّرة بمقاس 500px القياسي (ويكيميديا تحظر تنزيل الأصل بكثرة)
    if not data or data.get("type") == "disambiguation":
        return None
    thumb = data.get("thumbnail", {}).get("source")
    orig_w = data.get("originalimage", {}).get("width", 0)
    if thumb and "/thumb/" in thumb and orig_w >= 500:
        return re.sub(r"/\d+px-", "/500px-", thumb)
    return thumb

def fetch_wiki_image_by_title(title):
    return wiki_thumb_url(fetch_wiki_summary(title))

def save_square_webp(src_path, dest_path):
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        width, height = im.size
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        im_cropped = im.crop((left, top, left + min_dim, top + min_dim))
        im_resized = im_cropped.resize((350, 350), Image.Resampling.LANCZOS)
        im_resized.save(dest_path, "WEBP", quality=82)

def download_to_webp(img_url, slug, dest_path):
    temp_file = os.path.join(OUTPUT_DIR, f"temp_{slug}")
    req = urllib.request.Request(img_url, headers={'User-Agent': 'WiBoHealthBot/2.0'})
    try:
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp, open(temp_file, 'wb') as out_f:
                    out_f.write(resp.read())
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or attempt == 3:
                    raise
                time.sleep(10 * (attempt + 1))  # انتظار متزايد عند تجاوز حد الطلبات
        save_square_webp(temp_file, dest_path)
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def link_image_by_id(content, food_id, rel_path):
    """يضيف حقل image قبل icon في سطر الصنف المحدد بالـ id"""
    pattern = re.compile(rf"(\{{\s*id:\s*{food_id},(?:(?!image:)[^\n])*?)(icon:)")
    new_content, n = pattern.subn(rf"\1image: '{rel_path}', \2", content, count=1)
    return new_content, n == 1

def process_missing_titles():
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    ok, failed = [], []
    for food_id, titles in MISSING_FOOD_TITLES.items():
        m = re.search(rf"\{{\s*id:\s*{food_id},[^\n]*?nameEn:\s*'((?:[^'\\]|\\.)*)'", content)
        if not m:
            failed.append((food_id, '?', 'not found in data.js'))
            continue
        name_en = m.group(1)
        slug = make_slug(name_en)
        dest_filename = f"{slug}.webp"
        dest_path = os.path.join(OUTPUT_DIR, dest_filename)
        rel_path = f"images/foods/{dest_filename}"

        used_title = None
        if not os.path.exists(dest_path):
            for title in titles:
                time.sleep(1.2)  # حماية السيرفر من الحظر
                img_url = fetch_wiki_image_by_title(title)
                if not img_url:
                    continue
                try:
                    download_to_webp(img_url, slug, dest_path)
                    used_title = title
                    break
                except Exception as e:
                    print(f"  [-] {food_id} ({title}) -> خطأ تنزيل: {e}")
            if not used_title:
                failed.append((food_id, name_en, 'no image on Wikipedia'))
                print(f"  [-] الصنف {food_id} ({name_en}) -> سيبقى بالإيموجي")
                continue

        content, linked = link_image_by_id(content, food_id, rel_path)
        ok.append((food_id, name_en, used_title or 'existing file', dest_filename))
        print(f"  [✓] الصنف {food_id} ({name_en}) <- {used_title or 'ملف موجود'} -> {dest_filename}")

    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(content)

    print(f"\n[🎉] نجح: {len(ok)} | فشل: {len(failed)}")
    for food_id, name_en, reason in failed:
        print(f"  [x] {food_id} {name_en}: {reason}")

def fix_white_rice():
    """إعادة حفظ white-rice.webp (كان AVIF بامتداد webp) كـ WebP حقيقي 350x350"""
    path = os.path.join(OUTPUT_DIR, "white-rice.webp")
    temp_file = path + ".src"
    os.replace(path, temp_file)
    try:
        save_square_webp(temp_file, path)
        os.remove(temp_file)
        print("[✓] white-rice.webp -> WebP 350x350")
    except Exception as e:
        os.replace(temp_file, path)
        print(f"[-] white-rice.webp: {e}")

# ===== الدفعة الكبرى: البحث التلقائي بالاسم الإنجليزي بعد تنظيفه =====

# كلمات وصفية لا تفيد البحث في ويكيبيديا
SEARCH_STOPWORDS = {
    'fresh', 'grilled', 'cooked', 'raw', 'organic', 'natural', 'pure', 'warm', 'cold', 'hot',
    'crispy', 'mild', 'unsweetened', 'sweetened', 'ripe', 'homemade', 'traditional', 'classic',
    'authentic', 'lean', 'skinless', 'marinated', 'spiced', 'steamed', 'boiled', 'baked',
    'roasted', 'toasted', 'fried', 'deep', 'pan', 'stir', 'smoked', 'canned', 'dried', 'frozen',
    'light', 'low', 'fat', 'free', 'whole', 'plain', 'simple', 'style', 'slice', 'slices',
    'healthy', 'mixed', 'creamy', 'seasoned', 'stuffed', 'small', 'large', 'medium',
    'dutch', 'turkish', 'moroccan', 'thai', 'chinese', 'korean', 'japanese', 'italian',
    'spanish', 'french', 'german', 'greek', 'british', 'portuguese', 'vietnamese', 'indian',
    'icelandic', 'sicilian', 'aleppian', 'arctic', 'persian', 'pacific', 'atlantic', 'syrian',
    'lebanese', 'egyptian', 'palestinian', 'jordanian', 'iraqi', 'saudi', 'emirati', 'gulf',
    'levantine', 'arabic', 'arab', 'mexican', 'american', 'austrian', 'swiss', 'belgian',
    'scandinavian', 'nordic', 'russian', 'polish', 'hungarian', 'ukrainian', 'yemeni',
    'maghrebi', 'tunisian', 'algerian', 'libyan', 'sudanese', 'kuwaiti', 'omani', 'bahraini',
    'qatari', 'norwegian', 'swedish', 'danish', 'finnish', 'irish', 'scottish', 'english',
}
# كلمات عامة جداً لا نقبلها وحدها كعنوان (تعطي صورة غير دقيقة)
GENERIC_SINGLE_WORDS = {
    'salad', 'soup', 'cake', 'bread', 'drink', 'sauce', 'cheese', 'pie', 'tea', 'juice',
    'stew', 'dip', 'meat', 'fish', 'rice', 'pasta', 'cream', 'oil', 'powder', 'butter',
    'seeds', 'seed', 'flour', 'milk', 'water', 'chicken', 'beef', 'lamb', 'vegetables',
    'fruit', 'sandwich', 'roll', 'rolls', 'bar', 'snack', 'dish', 'mix', 'paste', 'spread',
    'pudding', 'dessert', 'cookies', 'biscuits', 'sweets', 'pastry', 'sausage', 'eggs', 'egg',
    'breast', 'brains', 'fillet', 'wings', 'thighs', 'leg', 'liver', 'onions', 'delight',
}

def build_search_candidates(name_en):
    """يولّد عناوين بحث مرتبة من الأدق إلى الأقصر: [(العنوان, هل هو مطابقة دقيقة)]"""
    name = name_en.replace("\\'", "'")
    paren = re.findall(r"\(([^)]*)\)", name)
    base = re.sub(r"\([^)]*\)", " ", name)
    # حذف الملحقات الوصفية: "with ..." و "in ..." و "on ..."
    base = re.split(r"\s+(?:with|in|on|served)\s+", base, maxsplit=1)[0]
    words = [w for w in re.split(r"[\s/,]+", base) if w and w not in ("&", "-")]
    cleaned = [w for w in words if w.lower().strip("-") not in SEARCH_STOPWORDS]
    if not cleaned:
        cleaned = words

    candidates = []
    def add(t, exact):
        t = re.sub(r"\s+", " ", t).strip(" -&")
        if not t or t.lower() in (c.lower() for c, _ in candidates):
            return
        if " " not in t and t.lower() in GENERIC_SINGLE_WORDS:
            return
        # عناوين ويكيبيديا بصيغة الجملة: الحرف الأول فقط كبير (Turkish delight)
        candidates.append((t[0].upper() + t[1:].lower(), exact))

    # الاسم كما هو أولاً (يحفظ أسماء مثل Turkish Delight و Black Seed)، ثم بعد التنظيف
    add(" ".join(words), True)
    add(" ".join(cleaned), True)
    # محتوى الأقواس غالباً هو الاسم المحلي الدقيق (Vla, Hagelslag, Lokum...)
    for p in paren:
        p_words = [w for w in re.split(r"[\s/,]+", p) if w and w != "&" and w.lower() not in SEARCH_STOPWORDS]
        add(" ".join(p_words), True)
    # اختصار تدريجي (يحتاج مراجعة): آخر كلمتين ثم آخر كلمة غير عامة
    if len(cleaned) > 2:
        add(" ".join(cleaned[-2:]), False)
    if len(cleaned) > 1:
        add(cleaned[-1], False)
    return candidates[:5]

def process_range(start_id, end_id, report_path=None):
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    items = [(int(i), n) for i, n in re.findall(
        r"\{\s*id:\s*(\d+),[^\n]*?nameEn:\s*'((?:[^'\\]|\\.)*)'", content)]
    items = [(i, n) for i, n in items if start_id <= i <= end_id]
    print(f"[*] معالجة {len(items)} صنفاً من {start_id} إلى {end_id}...", flush=True)

    rows = []  # (id, nameEn, status, wiki_title, matched_by, file)
    for idx, (food_id, name_en) in enumerate(items, 1):
        line = re.search(rf"\{{\s*id:\s*{food_id},[^\n]*", content).group(0)
        if "image:" in line:
            rows.append((food_id, name_en, 'already', '', '', ''))
            continue
        slug = make_slug(name_en.replace("\\'", ""))
        dest_filename = f"{slug}.webp"
        dest_path = os.path.join(OUTPUT_DIR, dest_filename)
        rel_path = f"images/foods/{dest_filename}"

        status, wiki_title, matched_by = 'failed', '', ''
        if os.path.exists(dest_path):
            status, matched_by = 'ok', 'existing file'
        else:
            candidates = build_search_candidates(name_en)
            for title, exact in candidates:
                time.sleep(1.2)  # حماية السيرفر من الحظر
                data = fetch_wiki_summary(title)
                img_url = wiki_thumb_url(data)
                if not img_url:
                    continue
                try:
                    download_to_webp(img_url, slug, dest_path)
                except Exception as e:
                    print(f"  [-] {food_id} ({title}) -> خطأ تنزيل: {e}", flush=True)
                    continue
                status = 'ok' if exact else 'review'
                wiki_title, matched_by = data.get("title", title), title
                break

        if status != 'failed':
            content, _ = link_image_by_id(content, food_id, rel_path)
            print(f"  [{'✓' if status == 'ok' else '?'}] {idx}/{len(items)} id {food_id} ({name_en}) <- {wiki_title or matched_by}", flush=True)
        else:
            print(f"  [x] {idx}/{len(items)} id {food_id} ({name_en}) -> يحتاج تسمية مخصصة", flush=True)
        rows.append((food_id, name_en, status, wiki_title, matched_by, dest_filename if status != 'failed' else ''))

        # حفظ دوري حتى لا تضيع الروابط عند أي انقطاع
        if idx % 25 == 0:
            with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
                f.write(content)

    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(content)

    if report_path:
        import csv
        with open(report_path, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id", "nameEn", "status", "wiki_title", "search_term", "file"])
            w.writerows(rows)

    counts = {s: sum(1 for r in rows if r[2] == s) for s in ('ok', 'review', 'failed', 'already')}
    print(f"\n[🎉] مطابقة مباشرة: {counts['ok']} | بعنوان مختصر (للمراجعة): {counts['review']} | "
          f"يحتاج تسمية مخصصة: {counts['failed']} | مربوط مسبقاً: {counts['already']}")

# ===== الجولة الأخيرة: محرك بحث ويكيبيديا + Wikimedia Commons للأصناف بلا صور =====

WIKI_API = "https://en.wikipedia.org/w/api.php"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"

# كلمات لاحقة عامة تُحذف للوصول إلى اسم الأكلة الأساسي (Focaccia bread -> Focaccia)
DISH_SUFFIX_WORDS = GENERIC_SINGLE_WORDS | {
    'gateau', 'infusion', 'decoction', 'brew', 'sticks', 'stick', 'sheets', 'granules',
    'slices', 'pieces', 'nuts', 'drink', 'beverage', 'platter', 'bowl', 'cup', 'shot',
    'noodles', 'patties', 'skewers', 'balls', 'bites', 'wedges', 'fillets', 'cubes',
    'hearts', 'leaves', 'root', 'bulb', 'tart', 'biscuit', 'cutlet', 'casserole', 'naturel',
    # صفات وصفية تشوش البحث
    'aged', 'crumbly', 'dry', 'melting', 'alpine', 'slow-roasted', 'braised', 'glazed', 'spicy',
    'cold-pressed', 'shelled', 'kernels', 'soluble', 'fiber', 'concentrated', 'extract',
    'ceremonial', 'grade', 'soothing', 'festive', 'unflavored', 'halal', 'bovine', 'sweet',
    'molten', 'ribbon', 'clay', 'pot', 'parchment', 'detox', 'premium', 'certified',
}

def api_get(base, params):
    """طلب API مع إعادة محاولة متزايدة عند 429"""
    url = base + "?" + urllib.parse.urlencode({**params, "format": "json", "formatversion": 2})
    req = urllib.request.Request(url, headers={
        'User-Agent': 'WiBoHealthBot/2.0 (Clinical Diet Guide; support@wibohealth.com)'
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 3:
                return None
            time.sleep(10 * (attempt + 1))
        except Exception:
            return None
    return None

def _norm(text):
    import unicodedata
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z]{3,}", text)

def key_tokens(query):
    return {w for w in _norm(query) if w not in SEARCH_STOPWORDS and w not in DISH_SUFFIX_WORDS}

def is_relevant(result_title, query):
    """يقبل النتيجة فقط إذا شاركت الاستعلام كلمة أساسية واحدة على الأقل (يمنع النتائج العشوائية)"""
    q = key_tokens(query)
    if not q:
        return False
    title_words = set(_norm(result_title))
    # مطابقة مرنة للجمع والمفرد (Dates/Date, Mulberries/Mulberry)
    return any(any(t.startswith(w[:5]) or w.startswith(t[:5]) for t in title_words) for w in q)

def build_core_queries(name_en):
    """استعلامات بحث: الاسم الأساسي بدون الوصف واللواحق العامة، ثم محتوى الأقواس، ثم الاسم المنظف"""
    name = name_en.replace("\\'", "'")
    paren = re.findall(r"\(([^)]*)\)", name)
    base = re.sub(r"\([^)]*\)", " ", name)
    base = re.split(r"\s+(?:with|in|on|served)\s+", base, maxsplit=1)[0]
    words = [w for w in re.split(r"[\s/,]+", base) if w and w not in ("&", "-")]
    cleaned = [w for w in words if w.lower().strip("-") not in SEARCH_STOPWORDS]
    core = [w for w in cleaned if w.lower() not in DISH_SUFFIX_WORDS] or cleaned

    queries = []
    def add(q):
        q = re.sub(r"\s+", " ", q).strip(" -&")
        if q and q.lower() not in (x.lower() for x in queries):
            queries.append(q)
    add(" ".join(core))
    for p in paren:
        add(" ".join(w for w in re.split(r"[\s/,]+", p) if w.lower() not in SEARCH_STOPWORDS))
    add(" ".join(cleaned))
    if len(core) > 2:
        add(" ".join(core[:2]))
    return queries[:4]

def wiki_search_image(query):
    """يبحث في محرك ويكيبيديا ويعيد (عنوان المقال, رابط الصورة) لأول نتيجة ذات صلة تملك صورة"""
    data = api_get(WIKI_API, {"action": "query", "list": "search", "srsearch": query,
                              "srlimit": 3, "srnamespace": 0})
    for hit in (data or {}).get("query", {}).get("search", []):
        title = hit["title"]
        if not is_relevant(title, query) or title.lower().startswith("list of"):
            continue
        time.sleep(1.2)
        summary = fetch_wiki_summary(title)
        img = wiki_thumb_url(summary)
        if img:
            return summary.get("title", title), img
    return None, None

def commons_search_image(query):
    """بديل: صورة حرة من Wikimedia Commons (رخص CC / ملك عام) بمقاس 500px"""
    data = api_get(COMMONS_API, {
        "action": "query", "generator": "search", "gsrsearch": f"{query} food filetype:bitmap",
        "gsrnamespace": 6, "gsrlimit": 5, "prop": "imageinfo",
        "iiprop": "url|mime", "iiurlwidth": 500,
    })
    pages = sorted((data or {}).get("query", {}).get("pages", []), key=lambda p: p.get("index", 99))
    for page in pages:
        info = (page.get("imageinfo") or [{}])[0]
        if info.get("mime") not in ("image/jpeg", "image/png", "image/webp"):
            continue
        if not is_relevant(page["title"].replace("File:", ""), query):
            continue
        return page["title"], info.get("thumburl") or info.get("url")
    return None, None

def process_remaining(report_path=None):
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    lines = re.findall(r"\{\s*id:\s*\d+,[^\n]*", content)
    items = []
    for line in lines:
        if "image:" in line:
            continue
        m = re.search(r"id:\s*(\d+),[^\n]*?nameEn:\s*'((?:[^'\\]|\\.)*)'", line)
        if m:
            items.append((int(m.group(1)), m.group(2)))
    print(f"[*] أصناف بلا صور: {len(items)}", flush=True)

    rows = []  # (id, nameEn, status, source, matched_title, query, file)
    for idx, (food_id, name_en) in enumerate(items, 1):
        slug = make_slug(name_en.replace("\\'", ""))
        dest_filename = f"{slug}.webp"
        dest_path = os.path.join(OUTPUT_DIR, dest_filename)
        rel_path = f"images/foods/{dest_filename}"

        status, source, matched, used_query = 'failed', '', '', ''
        for query in build_core_queries(name_en):
            for source_name, finder in (("wikipedia", wiki_search_image), ("commons", commons_search_image)):
                time.sleep(1.2)  # حماية السيرفر من الحظر
                title, img_url = finder(query)
                if not img_url:
                    continue
                try:
                    download_to_webp(img_url, slug, dest_path)
                except Exception as e:
                    print(f"  [-] {food_id} ({title}) -> خطأ تنزيل: {e}", flush=True)
                    continue
                status, source, matched, used_query = 'ok', source_name, title, query
                break
            if status == 'ok':
                break

        if status == 'ok':
            content, _ = link_image_by_id(content, food_id, rel_path)
            print(f"  [✓] {idx}/{len(items)} id {food_id} ({name_en}) <- {source}: {matched}", flush=True)
        else:
            print(f"  [x] {idx}/{len(items)} id {food_id} ({name_en})", flush=True)
        rows.append((food_id, name_en, status, source, matched, used_query, dest_filename if status == 'ok' else ''))

        if idx % 25 == 0:
            with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
                f.write(content)

    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(content)

    if report_path:
        import csv
        with open(report_path, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id", "nameEn", "status", "source", "matched_title", "query", "file"])
            w.writerows(rows)

    ok = [r for r in rows if r[2] == 'ok']
    print(f"\n[🎉] نجح: {len(ok)} (ويكيبيديا: {sum(r[3] == 'wikipedia' for r in ok)} | "
          f"Commons: {sum(r[3] == 'commons' for r in ok)}) | متبقٍ: {len(rows) - len(ok)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "remaining":
        # مثال: python get_50_foods.py remaining batch_remaining.csv
        process_remaining(sys.argv[2] if len(sys.argv) > 2 else None)
    elif len(sys.argv) >= 3:
        # مثال: python get_50_foods.py 151 650 report.csv
        process_range(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        process_missing_titles()
        # fix_white_rice()  # تمت المعالجة