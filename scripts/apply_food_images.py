"""Apply the food photos approved on review/review_images.html.

    python scripts/apply_food_images.py review/approved_images.json

For every approved food: download the original photo, centre-crop it to a 350 x 350 WebP in images/foods/<slug>.webp,
set the food's `image` in js/data.js, and record the licence in data/food_image_credits.json (author, licence, source),
which the attribution of CC BY / CC BY-SA photos needs. Then: thumbnails, the food pages of these foods and the static
food indexes are rebuilt. Only foods whose image is empty in js/data.js are changed unless --replace is given.
"""
import io
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'js' / 'data.js'
CREDITS = ROOT / 'data' / 'food_image_credits.json'
SIZE, QUALITY = 350, 82
UA = {'User-Agent': 'WiBoHealthImageReview/1.0 (food photo review)'}


def download(url):
    """Wikimedia answers 429 when files are fetched too fast: pause between files and back off on 429."""
    for attempt in range(6):
        time.sleep(3)
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(20 * (attempt + 1))
    raise RuntimeError(f'still rate-limited: {url}')


def source_url(c):
    """A 960 px Wikimedia rendition is plenty for a 350 px photo and is not throttled like the originals."""
    thumb = c.get('thumbnail') or ''
    if c.get('source') == 'wikimedia' and '/330px-' in thumb and (c.get('width') or 0) > 960:
        return re.sub(r'^https://thumb\.wikimedia\.org/', 'https://upload.wikimedia.org/', thumb.replace('/330px-', '/960px-'))
    return c['url']


def records(src):
    """(id, start, end) of every food record in data.js."""
    starts = [m.start() for m in re.finditer(r"\{\s*id:\s*\d+,", src)] + [len(src)]
    return [(int(re.match(r"\{\s*id:\s*(\d+)", src[a:b]).group(1)), a, b) for a, b in zip(starts, starts[1:])]


def main():
    approvals = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))['approved']
    replace = '--replace' in sys.argv
    slugs = json.loads(re.search(r'= (\{.*\});', (ROOT / 'js' / 'food-pages.js').read_text(encoding='utf-8')).group(1))
    src = DATA.read_text(encoding='utf-8')
    recs = {fid: (a, b) for fid, a, b in records(src)}
    credits = json.loads(CREDITS.read_text(encoding='utf-8')) if CREDITS.exists() else {}
    done, edits = [], []
    for item in approvals:
        fid, c = int(item['food_id']), item['candidate']
        a, b = recs[fid]
        m = re.search(r"image:\s*'([^']*)'", src[a:b])
        if m.group(1) and not replace:
            print(f'{fid}: has an image already ({m.group(1)}), skipped (use --replace)')
            continue
        rel = f'images/foods/{slugs[str(fid)]}.webp'
        try:
            raw = download(source_url(c))
        except Exception as e:                           # keep going: the others are still applied
            print(f'{fid}: download failed ({e}), not changed')
            continue
        with Image.open(io.BytesIO(raw)) as im:
            ImageOps.fit(ImageOps.exif_transpose(im).convert('RGB'), (SIZE, SIZE), Image.LANCZOS) \
                .save(ROOT / rel, 'WEBP', quality=QUALITY, method=6)
        edits.append((a + m.start(), a + m.end(), f"image: '{rel}'"))
        credits[str(fid)] = {'file': rel, 'title': c.get('title'), 'creator': c.get('creator'),
                             'creator_url': c.get('creator_url'), 'license': c.get('license'),
                             'license_version': c.get('license_version'), 'license_url': c.get('license_url'),
                             'source': c.get('source'), 'landing': c.get('foreign_landing_url'),
                             'original': c.get('url'), 'approved': item.get('approved_at')}
        done.append(fid)
        print(f'{fid}: {rel} ({c.get("license")} {c.get("license_version") or ""}, {c.get("creator")})')
    for s, e, new in sorted(edits, reverse=True):          # back to front, so the offsets stay valid
        src = src[:s] + new + src[e:]
    DATA.write_text(src, encoding='utf-8', newline='')
    CREDITS.parent.mkdir(exist_ok=True)
    CREDITS.write_text(json.dumps(credits, ensure_ascii=False, indent=1, sort_keys=True), encoding='utf-8')
    if not done:
        return
    py = sys.executable
    subprocess.run([py, 'scripts/make_food_thumbs.py'], cwd=ROOT, check=True)
    subprocess.run([py, 'scripts/generate_food_pages.py', '--only', ','.join(map(str, done))], cwd=ROOT, check=True)
    subprocess.run([py, 'scripts/generate_directory_pages.py'], cwd=ROOT, check=True)
    print(f'{len(done)} foods have their new photo: {done}')


if __name__ == '__main__':
    main()
