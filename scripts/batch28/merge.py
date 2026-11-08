"""Batches 28 and 29 (31 October 2026) and 30 (8 November 2026): merge the approved copy in scripts/batch28/,
scripts/batch29/ and scripts/batch30/ ({ar,en,nl,sv}.md) into the generator inputs (all batches in one run, so rerunning
never drops another batch). Batch 30 has 3 FAQs per food and long search titles kept whole ("title_full").

ar/en/nl go to scripts/food_pages_overrides.json; the Swedish names, plural flags and copy go to scripts/food_sv.py.
Each food: "## <id>", then key lines (slug, portion, sugar, ii, brand, title, desc, refs [repeatable], ref_gi), then the body
(### sections) and, after "### FAQ", the questions as **question** + answer lines. Safe to rerun: the batch's earlier
entries are removed first. Foods in HELD keep their copy here but get no page (1047: calories to be checked first).
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
BATCH_DIRS = (HERE, SCRIPTS / 'batch29', SCRIPTS / 'batch30', SCRIPTS / 'batch31')
TITLE_FULL = {int(i) for d in ('batch30', 'batch31')   # 3 FAQs + long approved titles kept whole
              for i in re.findall(r'(?m)^## (\d+)\s*$', (SCRIPTS / d / 'ar.md').read_text(encoding='utf-8'))}
LANGS = ('ar', 'en', 'nl', 'sv')
HELD = {1047}
KEYS = {'sugar': 'sugar', 'ii': 'ii_text', 'portion': 'portion_label', 'ref_gi': 'ref_gi', 'brand': 'brand_note', 'title': 'title', 'desc': 'desc'}
SV_NAMES = {   # id: (Swedish display name, name inside sentences)
    1017: ('Yerba mate', 'yerba mate'), 993: ('Kanel- och ingefärste', 'kanel- och ingefärsteet'),
    991: ('Bockhornsklöverte med honung', 'bockhornsklöverteet'), 963: ('Benbuljong på nötben', 'benbuljongen'),
    906: ('Nasi goreng (indonesiskt stekt ris)', 'nasi goreng'), 878: ('Holländskt russinbröd (krentenbrood)', 'krentenbrood'),
    981: ('Glutenfria havregryn', 'glutenfria havregryn'), 987: ('Shiratakinudlar', 'shiratakinudlar'),
    930: ('Grillad portabellosvamp', 'grillad portabellosvamp'), 989: ('Doumpalmfrukt', 'doumpalmfrukt'),
    1025: ('Erytritol (sötningsmedel)', 'erytritol'), 1026: ('Flytande steviadroppar', 'steviadroppar'),
    1028: ('Kokossocker', 'kokossocker'), 972: ('Bredbara osttrianglar (La vache qui rit)', 'osttrianglar'),
    971: ('Färskost med full fetthalt (Philadelphia Original)', 'färskost'), 922: ('Ugnsstekt kalkonbröst', 'ugnsstekt kalkonbröst'),
    908: ('Kycklingsatay med jordnötssås', 'kycklingsatay'), 1047: ('Machboos med lamm', 'machboos med lamm'),
    1049: ('Luqaimat med dadelsirap', 'luqaimat'), 951: ('Grillade arayes (pitabröd fyllt med köttfärs)', 'arayes'),
    881: ('Holländsk äppelpaj (appeltaart)', 'äppelpajen'), 984: ('Psylliumfröskal', 'psylliumfröskal'),
    # batch 29
    952: ('Egyptisk hawawshi med köttfärs', 'hawawshi'), 956: ('Egyptisk mombar med risfyllning', 'mombar'),
    957: ('Egyptisk kishk med kyckling', 'kishk'), 1045: ('Irakisk grillad masgouf (fisk)', 'masgouf'),
    1048: ('Balaleet från Gulfen (söt vermicelli med ägg)', 'balaleet'),
    1050: ('Emiratisk khabeesa med mannagryn och kardemumma', 'khabeesa'), 1032: ('Egyptisk mishost', 'mishost'),
    973: ('Krämiga ostkuber (Kiri)', 'ostkuber'), 880: ('Holländska oliebollen', 'oliebollen'),
    882: ('Holländsk saucijzenbroodje (korv i smördeg)', 'saucijzenbroodje'),
    907: ('Bami goreng (indonesiska stekta nudlar)', 'bami goreng'), 911: ('Holländsk satékroket', 'satékroket'),
    916: ('Räkchips (kroepoek)', 'kroepoek'), 885: ('Salt lakrits (dubbelzout drop)', 'salt lakrits'),
    1009: ('Limburgsk körsbärsvlaai', 'körsbärsvlaai'), 879: ('Stollen med mandelmassa (kerststol)', 'stollen'),
    1013: ('Lindblomste', 'lindblomsteet'), 992: ('Svartkumminte med honung', 'svartkumminteet'),
    1027: ('Munkfrukt (monk fruit) sötningsmedel', 'munkfrukt'), 1029: ('Allulos (sötningsmedel)', 'allulos'),
    999: ('Kollagenpeptider från nöt', 'kollagenpeptider'), 1030: ('Johannesbrödpulver (kakaoersättning)', 'johannesbrödpulver'),
    935: ('Svart sommartryffel', 'svart sommartryffel'), 1053: ('Thailändsk tom kha gai-soppa', 'tom kha gai'),
    926: ('Cordon bleu på kyckling', 'cordon bleu'),
    # batch 30
    876: ('Belgisk fruktsirap från Liège (äpple och päron, utan tillsatt socker)', 'fruktsirapen från Liège'),
    877: ('Holländsk honungs- och kryddkaka (honingkoek)', 'honingkoek'),
    883: ('Indonesisk kycklingsoppa (soto ayam)', 'soto ayam'),
    884: ('Wilhelmina, holländska pepparmyntstabletter', 'pepparmyntstabletterna'),
    886: ('Holländsk mjuk honungslakrits (honingdrop)', 'honungslakritsen'),
    887: ('Rysk bovetegröt (kasja) med smör och mjölk', 'bovetegröten'),
    888: ('Rysk rassolnik, soppa med saltgurka och korn', 'rassolnik'),
    889: ('Polsk vildsvampsoppa med karljohan (zupa grzybowa)', 'vildsvampsoppan'),
    890: ('Polsk bigos, jägargryta med surkål och kött', 'bigos'),
    891: ('Skandinavisk sillsallad med rödbetor och äpple', 'sillsalladen'),
    892: ('Finsk laxsoppa med dill och grädde (lohikeitto)', 'lohikeitto'),
    893: ('Traditionellt finskt rågbröd (ruisleipä)', 'ruisleipä'),
    894: ('Karelska piroger med risgrynsgröt (karjalanpiirakka)', 'karelska piroger'),
    895: ('Ungersk bön- och köttgryta (babgulyás)', 'babgulyás'),
    896: ('Bulgarisk shopskasallad med vit ost (sirene)', 'shopskasalladen'),
    897: ('Traditionell bulgarisk banitsa med ost och ägg', 'banitsa'),
    898: ('Balkansk grillad ćevapi (ćevapčići)', 'ćevapi'),
    899: ('Balkansk ajvar på grillad paprika', 'ajvar'),
    900: ('Balkansk pindjur med grillad paprika och tomat', 'pindjur'),
    901: ('Surinamesisk roti med kyckling, potatis och långbönor', 'roti med kyckling'),
    902: ('Surinamesiskt rotibröd fyllt med gula ärtor (dhalpuri)', 'dhalpuri'),
    903: ('Surinamesiska sparrisbönor med vitlök (kousenband)', 'sparrisbönorna'),
    904: ('Surinamesisk pom med kyckling (pomtajer)', 'pom'),
    905: ('Surinamesiska friterade barakakor med kryddor', 'barakakorna'),
    909: ('Äkta indonesisk rendang på nötkött med kokosmjölk', 'rendang'),
    # batch 31
    910: ('Gado gado, indonesisk grönsakssallad med jordnötssås', 'gado gado'),
    912: ('Loempia speciaal (stor holländsk-indonesisk vårrulle med kyckling)', 'loempian'),
    913: ('Ajam ketjap, indonesisk kyckling i söt sojasås', 'ajam ketjap'),
    914: ('Sambal oelek, indonesisk chilipasta', 'sambal oelek'),
    915: ('Spekkoek, indonesisk kryddig lagerkaka', 'spekkoek'),
    917: ('Atjar tjampoer, indonesiska inlagda grönsaker med gurkmeja', 'atjar tjampoer'),
    918: ('Serundeng, rostad kokos med jordnötter och kryddor', 'serundeng'),
    919: ('Vitello tonnato, kall kalv med tonfisksås', 'vitello tonnato'),
    920: ('Oxcarpaccio med tryffelmajonnäs, parmesan och pinjenötter', 'carpaccion'),
    921: ('Råbiff (steak tartare) med äggula, senap och kapris', 'råbiffen'),
    923: ('Kalvscaloppine med citron och smör', 'kalvscaloppinen'),
    924: ('Ossobuco alla milanese (kalvlägg med märg och gremolata)', 'ossobuco'),
    925: ('Kyckling piccata med citron och kapris', 'kyckling piccata'),
    927: ('Kyckling Kiev med vitlöks- och örtsmör', 'kyckling Kiev'),
    928: ('Vilda kantareller', 'kantarellerna'),
    929: ('Torkad karljohansvamp (porcini), blötlagd', 'karljohansvampen'),
    931: ('Ångade ostronskivlingar', 'ostronskivlingarna'),
    932: ('Svart trumpetsvamp, torkad och blötlagd', 'trumpetsvampen'),
    933: ('Vilda murklor (toppmurklor)', 'murklorna'),
    934: ('Kastanjechampinjoner (cremini)', 'kastanjechampinjonerna'),
    936: ('Vit tryffel från Alba', 'den vita tryffeln'),
    937: ('Friterad zucchini med skordalia (grekisk vitlöksdipp)', 'den friterade zucchinin'),
    938: ('Skordalia, grekisk vitlöks- och potatisdipp', 'skordalia'),
    939: ('Taramosalata, grekisk dipp på fiskrom', 'taramosalata'),
    940: ('Saganaki, stekt grekisk ost med citron', 'saganaki'),
}
SV_PLURAL = {981, 987, 972, 1026, 1049, 951, 984, 973, 880, 916, 999,
             884, 894, 898, 903, 905, 928, 931, 933, 934}
MARK = '    # batch 28 (31 October 2026): translated from the approved Arabic copy'   # also covers batch 29


def parse(lang):
    foods = {}
    blocks = [b for d in BATCH_DIRS for b in
              re.split(r'^## (?=\d+\s*$)', (d / f'{lang}.md').read_text(encoding='utf-8'), flags=re.M)[1:]]
    for block in blocks:
        lines = block.split('\n')
        fid, o, i = int(lines[0]), {}, 1
        while i < len(lines) and not lines[i].startswith('### '):
            m = re.match(r'(\w+): (.*)$', lines[i])
            if m:
                k, v = m.group(1), m.group(2).strip()
                if k == 'refs':
                    o.setdefault('refs_extra', []).append(v)
                elif k == 'ref_gi':
                    o['ref_gi'] = v + ' '            # the ISO citation follows
                elif k in KEYS:
                    o[KEYS[k]] = v
                elif k == 'slug':
                    o['slug'] = v
                else:
                    raise SystemExit(f'{lang} {fid}: unknown key {k}')
            i += 1
        body, faq = '\n'.join(lines[i:]).split('### FAQ', 1)
        o['body'] = body.strip()
        o['faq'] = [dict(q=q.strip(), a=a.strip()) for q, a in
                    re.findall(r'^\*\*(.+?)\*\*\s*\n(.+?)(?=\n\s*\n|\Z)', faq.strip(), re.M | re.S)]
        assert len(o['faq']) == (3 if fid in TITLE_FULL else 4), (lang, fid, len(o['faq']))
        foods[fid] = o
    return foods


def main():
    copy = {l: parse(l) for l in LANGS}
    all_ids = list(copy['ar'])
    assert all(list(copy[l]) == all_ids for l in LANGS), 'the four files must list the same foods'
    for l in LANGS:
        for fid in all_ids:
            assert set(copy[l][fid]) - {'slug'} == set(copy['ar'][fid]) - {'slug'}, (l, fid)
    ids = [i for i in all_ids if i not in HELD]

    path = SCRIPTS / 'food_pages_overrides.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    for fid in all_ids:
        data['foods'].pop(str(fid), None)
    for fid in ids:
        entry = {'slug': copy['ar'][fid]['slug']}
        if fid in TITLE_FULL:                  # batch 30: approved 80-95 character titles, brand kept
            entry['title_full'] = True
        for key in [k for k in copy['ar'][fid] if k != 'slug']:
            entry[key] = {l: copy[l][fid][key] for l in ('ar', 'en', 'nl')}
        data['foods'][str(fid)] = entry
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

    sv = (SCRIPTS / 'food_sv.py').read_text(encoding='utf-8')
    sv = re.sub(re.escape(MARK) + r'\n(?:    \d+: .*\n)+', '', sv)                        # names block
    sv = re.sub(re.escape(MARK) + r' \(body[^\n]*\n(?:    \d+: .*\n)+', '', sv)           # copy block
    sv = re.sub(r'(871, 875),\n          [\d, ]+\}', r'\1}', sv)                          # plural flags
    names = ''.join(f'    {fid}: {SV_NAMES[fid]!r},\n' for fid in ids)
    anchor = "    875: ('Antwerpse handjes (smörkex med mandel)', 'antwerpse handjes'),\n}"
    assert sv.count(anchor) == 1
    sv = sv.replace(anchor, anchor[:-1] + MARK + '\n' + names + '}', 1)
    plural = '801, 802, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 871, 875}'
    assert sv.count(plural) == 1
    sv = sv.replace(plural, plural[:-1] + ',\n          ' + ', '.join(map(str, sorted(SV_PLURAL - HELD))) + '}', 1)
    block = MARK + ' (body, FAQ, table and reference notes)\n'
    for fid in ids:
        block += f'    {fid}: { {k: v for k, v in copy["sv"][fid].items() if k != "slug"}!r},\n'
    assert sv.endswith(')]),\n}\n'), 'unexpected end of food_sv.py'
    sv = sv[:-2] + block + '}\n'
    (SCRIPTS / 'food_sv.py').write_text(sv, encoding='utf-8', newline='\n')
    print('merged', len(ids), 'foods (held:', sorted(HELD), ') into food_pages_overrides.json and food_sv.py')


if __name__ == '__main__':
    main()
