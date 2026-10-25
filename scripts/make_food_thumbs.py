"""Make 96 x 96 WebP thumbnails of the food photos for the lists (foods.html cards, the static food indexes).

    python scripts/make_food_thumbs.py

images/foods/<name>.webp (350 x 350) -> images/foods/thumb/<name>.webp (96 x 96, about 2 KB). A thumbnail is only
rebuilt when its photo is newer, so the script can run after every batch of new photos. Thumbnails whose photo is gone
are removed.
"""
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'images' / 'foods'
OUT = SRC / 'thumb'
SIZE = 96
QUALITY = 72


def main():
    OUT.mkdir(exist_ok=True)
    photos = sorted(SRC.glob('*.webp'))
    made = 0
    for photo in photos:
        thumb = OUT / photo.name
        if thumb.exists() and thumb.stat().st_mtime >= photo.stat().st_mtime:
            continue
        with Image.open(photo) as im:
            im = ImageOps.fit(im.convert('RGB'), (SIZE, SIZE), Image.LANCZOS)   # centre crop if a photo is not square
            im.save(thumb, 'WEBP', quality=QUALITY, method=6)
        made += 1
    names = {p.name for p in photos}
    removed = [t for t in OUT.glob('*.webp') if t.name not in names]
    for t in removed:
        t.unlink()
    total = sum(t.stat().st_size for t in OUT.glob('*.webp'))
    print(f'thumbnails: {len(photos)} photos, {made} made, {len(removed)} removed, '
          f'{total / 1024:.0f} KB in total ({total / max(len(photos), 1) / 1024:.1f} KB each)')


if __name__ == '__main__':
    main()
