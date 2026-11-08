"""Batch 31: approved Arabic copy (ar_corrected.md) -> merge format ar.md (scripts/batch28/merge.py keys) + foods.json.
Checks per-100 g numbers against js/data.js and the portion GL against what the page computes.
Usage: python -X utf8 -I build_ar.py   (run from scripts/batch31)"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
B = ' | WiBo Health'

SLUG = {910: 'gado-gado', 912: 'loempia-speciaal', 913: 'ajam-ketjap', 914: 'sambal-oelek', 915: 'spekkoek',
        917: 'atjar-tjampoer', 918: 'serundeng', 919: 'vitello-tonnato', 920: 'beef-carpaccio', 921: 'steak-tartare',
        923: 'veal-scaloppine', 924: 'ossobuco', 925: 'chicken-piccata', 927: 'chicken-kiev', 928: 'chanterelles',
        929: 'porcini-rehydrated', 931: 'oyster-mushrooms', 932: 'black-trumpet-mushrooms', 933: 'morels',
        934: 'chestnut-mushrooms', 936: 'white-truffle', 937: 'fried-zucchini-skordalia', 938: 'skordalia',
        939: 'taramosalata', 940: 'saganaki'}
# meta descriptions approved with the correction table (2026-11-08)
DESC = {
910: 'أشهر طبق خضار دافئ في إندونيسيا وهولندا؛ اكتشف سعرات سلطة غادو غادو بصلصة الفول السوداني، وحملها الجلايسيمي المنخفض، وكيف تختار صلصة بلا سكر مضاف.',
912: 'لفة اللومبيا الهولندية الإندونيسية المقرمشة؛ اعرف سعرات القطعة الكبيرة وحملها الجلايسيمي، وكيف تأكلها بذكاء مع السلطة أو من القلاية الهوائية.',
913: 'دجاج الكيتجاب الإندونيسي بالصويا الحلوة والزنجبيل؛ اعرف سعراته وبروتينه وكمية السكر في الصلصة، وكيف تجعله مناسباً للكارب المنخفض.',
914: 'معجون الفلفل الإندونيسي الحار بلا سكر؛ اعرف سعرات ملعقة السامبال وأثرها على سكر الدم، ولماذا يعد بديلاً ذكياً للكاتشب والصلصات المحلاة.',
915: 'الكعكة الإندونيسية الهولندية متعددة الطبقات بالقرفة والهيل؛ اعرف سعرات الشريحة وحملها الجلايسيمي، ولماذا تُعامل كتحلية نادرة محسوبة.',
917: 'مخلل الخضار الإندونيسي الذهبي بالكركم؛ اكتشف كمية السكر المضاف في النسخ الجاهزة، وحمله الجلايسيمي، وكيف تحضّره في البيت بلا سكر.',
918: 'رشة جوز الهند المحمص بالفول السوداني والتوابل؛ اعرف سعرات الملعقة وأليافها، وكيف تضيف القرمشة لأطباقك دون أثر يُذكر على سكر الدم.',
919: 'لحم العجل البارد بصلصة التونة والكبر من بيدمونت؛ اعرف سعراته وبروتينه، ولماذا يناسب الكيتو ومريض السكري.',
920: 'شرائح اللحم البقري النيئة الرقيقة بمايونيز الترفل والبارميزان؛ اعرف سعراتها وبروتينها، ومن يجب أن يتجنب اللحم النيء.',
921: 'اللحم البقري النيء المفروم بالسكين مع صفار البيض والكبر؛ اعرف قيمته الغذائية وسعراته، ومحاذير اللحم والبيض النيئ.',
923: 'شرائح لحم العجل الإيطالية بصلصة الليمون والزبدة؛ اعرف سعراتها وبروتينها، وكيف تقدمها بجانب الخضار بدل المعكرونة.',
924: 'موزات العجل الميلانية المطهوة ببطء مع الغريمولاتا؛ اعرف سعرات الحصة وبروتينها، ولماذا يرتفع السكر فقط مع الريزوتو المرافق.',
925: 'صدور الدجاج الإيطالية بصلصة الليمون والزبدة والكبر؛ اعرف سعراتها وبروتينها، ولماذا تناسب الكيتو والدايت.',
927: 'صدر الدجاج المحشو بزبدة الثوم والمغلف بالبقسماط؛ اعرف سعرات القطعة وحملها الجلايسيمي، وكيف تحضّر نسخة أخف في القلاية الهوائية.',
928: 'فطر الغابات الذهبي بنكهته الفاكهية؛ اعرف سعراته وأليافه، ولماذا يناسب مريض السكري والكيتو، وكيف تنظفه وتطهوه.',
929: 'فطر البورسيني المجفف بعد نقعه، سيد نكهة الأومامي؛ اعرف سعراته وكربوهيدراته شبه المعدومة، وكيف تستخدم ماء النقع كمرق طبيعي.',
931: 'فطر المحار بقوامه اللحمي ونكهته الناعمة؛ اعرف سعراته وبروتينه النباتي، ولماذا يناسب مريض السكري كبديل للحوم في الووك والشوربات.',
932: 'فطر البوق الأسود، كمأة الفقراء الفرنسية بنكهتها الدخانية؛ اعرف سعراته وأليافه، وكيف تنقعه وتضيفه للبيض واليخنات.',
933: 'الفطر الربيعي الأغلى برأسه الشبكي؛ اعرف سعراته وبروتينه، ولماذا يجب طهيه جيداً قبل الأكل، وكيف يناسب مريض السكري.',
934: 'فطر الكستناء البني المحبوب في السوبرماركت؛ اعرف سعراته وكربوهيدراته القليلة، والفرق بينه وبين الفطر الأبيض، وكيف تطهوه دون أن يفقد قوامه.',
936: 'الكمأة البيضاء النادرة من ألبا؛ اعرف قيمتها الغذائية في الرقائق القليلة التي تؤكل منها، وكيف تميز الكمأة الحقيقية من زيوت النكهة.',
937: 'رقائق الكوسا اليونانية المقرمشة مع صلصة الثوم سكورداليا؛ اعرف سعرات الحصة وحملها الجلايسيمي، وكيف تحضرها في القلاية الهوائية.',
938: 'صلصة الثوم اليونانية بالبطاطا وزيت الزيتون؛ اعرف سعرات الملعقتين وحملها الجلايسيمي، وكيف تحضرها بكارب أقل.',
939: 'الغموس اليوناني الكريمي ببطارخ السمك وزيت الزيتون؛ اعرف سعرات الملعقتين وكربوهيدراتها القليلة، وكيف تميز النسخة الطبيعية من الملونة.',
940: 'الجبنة اليونانية الصلبة المقلية بالليمون؛ اعرف سعرات القطعة وبروتينها، ولماذا تناسب الكيتو، وانتبه للملح.',
}
HEAD = {'الاستهلاك': 'توصيات الاستهلاك', 'التحضير': 'أفضل طرق التحضير',
        'ملاحظة هامة': 'ملاحظة غذائية هامة ⚠️', 'ملاحظة أمان سريرية': 'ملاحظة أمان ⚠️'}


def parse(b):
    lines = [l.strip() for l in b.strip().split('\n')]
    m = re.match(r'#(\d+) - (.*?) \| (.*)$', lines[0])
    f = {'id': int(m.group(1)), 'ar': m.group(2).strip(), 'en_short': m.group(3).strip()}
    i = next(k for k, l in enumerate(lines) if l.startswith('العنوان المقترح'))
    f['title'] = lines[i + 1] + B
    f['portion'] = float(re.findall(r'([\d.]+) غ', re.search(r'الحصة المعتادة \(([^)]*)\)', b).group(1))[-1])
    gi = re.search(r'المؤشر الجلايسيمي: (\d+)', b)
    f['gi'] = int(gi.group(1)) if gi else None
    gl = re.search(r'الحمل الجلايسيمي: ([\d.]+)', b)
    f['gl_copy'] = float(gl.group(1)) if gl else None
    for key, label in (('kcal', 'الماكروز \\(لكل 100 غ[^)]*\\): '), ('carbs', 'كارب: '), ('protein', 'بروتين: '),
                       ('fat', 'دهون: '), ('fiber', 'ألياف: ')):
        f[key] = float(re.search(label + r'([\d.]+)', b).group(1))
    k = lines.index('لغة الشارع والنص السريري الدافئ:')
    f['pulse'] = lines[k + 1]
    g = lines.index('الإرشاد الغذائي الذكي:')
    f['tips'] = []
    for l in lines[g + 1:]:
        if l.startswith('3 أسئلة'):
            break
        label, text = l.split(': ', 1)
        f['tips'].append((HEAD[label], text))
    assert len(f['tips']) == 3, f['id']
    f['faq'] = re.findall(r'(?m)^س\d: (.*)\n\s*ج: (.*)$', b)
    assert len(f['faq']) == 3, f['id']
    return f


def main():
    src = (HERE / 'ar_corrected.md').read_text(encoding='utf-8')
    foods = [parse(b) for b in re.split(r'(?m)^(?=#\d+ - )', src)[1:]]
    data = (ROOT / 'js' / 'data.js').read_text(encoding='utf-8')
    out = ['# Batch 31 (8 November 2026): approved Arabic copy for 910-940 (25 foods), generated by build_ar.py\n']
    for f in foods:
        line = re.search(r'\{ id: %d,.*\}' % f['id'], data).group(0)
        nut = dict(re.findall(r'(calories|protein|carbs|fat|fiber): ([\d.]+)', line.split('nutrition:')[1]))
        d = {'kcal': float(nut['calories']), 'protein': float(nut['protein']), 'carbs': float(nut['carbs']),
             'fat': float(nut['fat']), 'fiber': float(nut['fiber'])}
        diff = {k: (f[k], d[k]) for k in d if abs(f[k] - d[k]) > 0.05}
        gl = round(f['gi'] * (d['carbs'] - d['fiber']) * f['portion'] / 10000, 1) if f['gi'] else None
        flag = '' if gl is None or f['gl_copy'] is None or abs(gl - f['gl_copy']) < 0.05 else ' <- GL'
        print(f['id'], 'portion', f['portion'], 'GI', f['gi'], 'GL page', gl, 'copy', f['gl_copy'], 'diff', diff or '-', flag)
        assert len(f['title']) <= 95 and len(f['title']) >= 80 and not re.search(r'\d', f['title'] + DESC[f['id']]), f['id']
        f['desc'] = DESC[f['id']]
        body = [f['pulse']]
        for head, text in f['tips']:
            body += ['', '### ' + head, text]
        faq = '\n\n'.join(f'**{q}**\n{a}' for q, a in f['faq'])
        out.append(f'\n## {f["id"]}\nslug: {SLUG[f["id"]]}\nsugar: غير متوفر\nii: غير مختبر\n'
                   f'title: {f["title"]}\ndesc: {f["desc"]}\n\n' + '\n'.join(body) + '\n\n### FAQ\n' + faq + '\n')
    (HERE / 'ar.md').write_text(''.join(out), encoding='utf-8', newline='\n')
    (HERE / 'foods.json').write_text(json.dumps(foods, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')
    print('ar.md:', len(foods), 'foods')


if __name__ == '__main__':
    main()
