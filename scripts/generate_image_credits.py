"""Write /image-credits.html: author, licence and source of the food photos in data/food_image_credits.json.

    python scripts/generate_image_credits.py

CC BY / CC BY-SA photos must name their author; the food pages link here from the footer (generate_food_pages.py,
needs_credit) instead of printing the names under the photo. noindex, not in the sitemap.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
E = html.escape


def food_names():
    src = (ROOT / 'js' / 'data.js').read_text(encoding='utf-8')
    starts = [m.start() for m in re.finditer(r"\{\s*id:\s*\d+,", src)] + [len(src)]
    names = {}
    for a, b in zip(starts, starts[1:]):
        rec = src[a:b]
        fid = int(re.match(r"\{\s*id:\s*(\d+)", rec).group(1))
        ar = re.search(r"\bname:\s*(['\"])(.*?)(?<!\\)\1", rec)
        en = re.search(r"nameEn:\s*(['\"])(.*?)(?<!\\)\1", rec)
        names[fid] = (ar.group(2) if ar else '', en.group(2).replace("\\'", "'") if en else '')
    return names


def main():
    credits = json.loads((ROOT / 'data' / 'food_image_credits.json').read_text(encoding='utf-8'))
    slugs = json.loads(re.search(r'= (\{.*\});', (ROOT / 'js' / 'food-pages.js').read_text(encoding='utf-8')).group(1))
    names = food_names()
    rows = []
    for key in sorted(credits, key=int):
        c, fid = credits[key], int(key)
        ar, en = names.get(fid, ('', ''))
        lic = E(c.get('license') or '')
        if c.get('license_url'):
            lic = f'<a href="{E(c["license_url"])}" rel="license noopener" target="_blank">{lic}</a>'
        rows.append(f'''      <tr id="f{fid}">
        <td><img src="/images/foods/thumb/{E(Path(c['file']).name)}" alt="" width="48" height="48" loading="lazy"></td>
        <td><a href="/foods/{E(slugs.get(key, ''))}.html">{E(ar)}</a><br><span dir="ltr" lang="en"><a href="/en/foods/{E(slugs.get(key, ''))}.html">{E(en)}</a></span></td>
        <td dir="ltr"><a href="{E(c['landing'])}" rel="noopener" target="_blank">{E(c.get('creator') or 'unknown')}</a></td>
        <td dir="ltr">{lic}</td>
      </tr>''')
    page = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, follow">
<title>مصادر الصور | Image credits | WiBo Health</title>
<link rel="icon" type="image/png" sizes="192x192" href="/images/icon-192.png">
<style>
  :root {{ --bg:#f6f7f5; --card:#fff; --text:#1d2521; --muted:#5d6b64; --line:#dfe5e1; --link:#0f7a55; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --bg:#141816; --card:#1d2320; --text:#e7ece9; --muted:#9db0a6; --line:#2f3833; --link:#5fd0a0; }} }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text); font:15px/1.6 system-ui,"Segoe UI",Tahoma,sans-serif; }}
  main {{ max-width:900px; margin:0 auto; padding:24px 16px 40px; }}
  h1 {{ font-size:22px; margin:0 0 4px; }}
  p {{ color:var(--muted); margin:0 0 16px; }}
  a {{ color:var(--link); }}
  .wrap {{ background:var(--card); border:1px solid var(--line); border-radius:12px; overflow-x:auto; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th, td {{ padding:10px; border-bottom:1px solid var(--line); text-align:start; vertical-align:middle; }}
  th {{ color:var(--muted); font-weight:600; }}
  tr:last-child td {{ border-bottom:0; }}
  tr:target {{ background:color-mix(in srgb, var(--link) 12%, transparent); }}
  img {{ border-radius:6px; display:block; }}
  .home {{ display:inline-block; margin-bottom:16px; }}
</style>
</head>
<body>
<main>
  <a class="home" href="/">WiBo Health</a>
  <h1>مصادر الصور <span dir="ltr" lang="en">· Image credits</span></h1>
  <p>صور الأطعمة التالية من Wikimedia Commons، ونذكر هنا اسم المصوّر ورخصة كل صورة كما تشترط الرخصة.<br>
  <span dir="ltr" lang="en">These food photos are from Wikimedia Commons; each is credited to its author under the licence shown.</span></p>
  <div class="wrap">
    <table>
      <thead><tr><th></th><th>الطعام · Food</th><th>المصوّر · Author</th><th>الرخصة · Licence</th></tr></thead>
      <tbody>
{chr(10).join(rows)}
      </tbody>
    </table>
  </div>
</main>
</body>
</html>
'''
    (ROOT / 'image-credits.html').write_text(page, encoding='utf-8', newline='\n')
    print(f'image-credits.html: {len(rows)} photos')


if __name__ == '__main__':
    main()
