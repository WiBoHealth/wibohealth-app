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

if __name__ == "__main__":
    process_batch_2()