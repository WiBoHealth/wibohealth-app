"""Batch 31 (8 November 2026): js/data.js gets the approved names and GI for 910-940.
Arabic names = the approved copy headings; EN/NL keep data.js except where the approval changed them
(no cooking method in mushroom names, no claim in 931 NL, 920/921 as approved). Nutrition values are unchanged.
Usage: python -X utf8 -I update_data.py   (run from scripts/batch31)"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
foods = {f['id']: f for f in json.loads((Path(__file__).parent / 'foods.json').read_text(encoding='utf-8'))}
EN = {928: 'Golden Chanterelle Wild Mushrooms', 929: 'Dried Porcini Mushrooms (Rehydrated)',
      932: 'Black Trumpet Mushrooms (Dried, Rehydrated)', 933: 'Wild Spring Morel Mushrooms',
      921: 'Steak Tartare: Raw Minced Beef with Egg Yolk, Mustard & Capers'}
NL = {928: 'Wilde cantharellen', 929: 'Geweekt gedroogd eekhoorntjesbrood (porcini)', 931: 'Gestoomde oesterzwammen',
      932: 'Zwarte trompetzwam (gedroogd, geweekt)', 933: 'Wilde morieljes', 934: 'Kastanjechampignons',
      921: 'Steak tartaar: rauw rundvlees met eigeel, mosterd en kappertjes'}


def js(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


path = ROOT / 'js' / 'data.js'
text = path.read_text(encoding='utf-8')
for fid, f in foods.items():
    line = re.search(r'(?m)^    \{ id: %d,.*\},?$' % fid, text).group(0)
    m = re.search(r"name: '((?:[^'\\]|\\.)*)', nameEn: '((?:[^'\\]|\\.)*)', nameNl: '((?:[^'\\]|\\.)*)'", line)
    en = EN.get(fid, m.group(2).replace("\\'", "'"))
    nl = NL.get(fid, m.group(3).replace("\\'", "'"))
    new = line.replace(m.group(0), f"name: {js(f['ar'])}, nameEn: {js(en)}, nameNl: {js(nl)}", 1)
    gi = (f"gi: {f['gi']}, gi_status: 'reviewed', gi_source: 'WiBo Health medical team review'" if f['gi']
          else "gi: null, gi_status: 'not_applicable'")
    new = re.sub(r"gi: [^,]+, gi_status: '[a-z_]+'(?:, gi_source: '[^']*')?", gi, new, count=1)
    text = text.replace(line, new, 1)
path.write_text(text, encoding='utf-8', newline='\n')
print('data.js updated:', len(foods), 'foods')
