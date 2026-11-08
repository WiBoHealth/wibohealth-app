"""Batch 30 (8 November 2026): js/data.js gets the approved names (ar/en/nl, from the copy) and the approved GI
(`reviewed`; 893 = published value; `not_applicable` where the copy says so; 886 stays without a value, GI_UNAVAILABLE).
Nutrition values are unchanged (they already match the copy). Safe to rerun.
Usage: python -X utf8 -I update_data.py   (run from scripts/batch30)"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
foods = {f['id']: f for f in json.loads((Path(__file__).parent / 'foods.json').read_text(encoding='utf-8'))}
NOT_APPLICABLE = {890, 896, 898, 903, 909}
NO_VALUE = {886}
PUBLISHED = {893}
# Dutch display names in sentence case, as elsewhere in data.js (words and brands as approved)
NL = {877: 'Honingontbijtkoek (kruidkoek)', 883: 'Indonesische soto ayam kippensoep',
      886: 'Zachte honingdrop (met zoethout)', 887: 'Russische boekweitkasha met boter en melk',
      888: 'Russische rassolnik soep met augurk en gerst', 889: 'Poolse romige bospaddenstoelensoep',
      890: 'Poolse bigos jagersstoofpot met zuurkool en vlees', 891: 'Scandinavische haringsalade met rode biet',
      892: 'Finse romige zalmsoep met dille (lohikeitto)', 893: 'Traditioneel Fins roggebrood (ruisleipä)',
      894: 'Karelische rijstpasteitjes (karjalanpiirakka)', 895: 'Hongaarse bonengoulash (babgulyás)',
      896: 'Bulgaarse shopska salade met witte kaas', 897: 'Traditionele Bulgaarse banitsa met kaas en ei',
      899: 'Balkan ajvar van geroosterde paprika', 900: 'Balkan pindjur van paprika en tomaat',
      901: 'Surinaamse roti met kip, aardappel en kousenband', 902: 'Surinaamse rotiplaat met gele erwten (dhalpuri)',
      903: 'Surinaamse kousenband met knoflook', 904: 'Traditionele Surinaamse pom met kip en pomtajer',
      905: 'Surinaamse gefrituurde bara met chutney', 909: 'Authentieke Indonesische rendang van rundvlees'}


def js(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


path = ROOT / 'js' / 'data.js'
text = path.read_text(encoding='utf-8')
for fid, f in foods.items():
    m = re.search(r'(?m)^    \{ id: %d,.*\},?$' % fid, text)
    line = m.group(0)
    new = re.sub(r"name: '(?:[^'\\]|\\.)*', nameEn: '(?:[^'\\]|\\.)*', nameNl: '(?:[^'\\]|\\.)*'",
                 lambda _: f"name: {js(f['ar'])}, nameEn: {js(f['en'])}, nameNl: {js(NL.get(fid, f['nl']))}", line, count=1)
    if fid in NOT_APPLICABLE:
        gi = "gi: null, gi_status: 'not_applicable'"
    elif fid in NO_VALUE:
        gi = "gi: null, gi_status: 'estimated'"
    else:
        src = 'Published measurement (see page references)' if fid in PUBLISHED else 'WiBo Health medical team review'
        gi = f"gi: {f['gi']}, gi_status: 'reviewed', gi_source: '{src}'"
    new = re.sub(r"gi: [^,]+, gi_status: '[a-z_]+'(?:, gi_source: '[^']*')?", gi, new, count=1)
    assert new.count('name: ') == 1 and 'gi_status' in new, fid
    text = text.replace(line, new, 1)
path.write_text(text, encoding='utf-8', newline='\n')
print('data.js updated:', len(foods), 'foods')
