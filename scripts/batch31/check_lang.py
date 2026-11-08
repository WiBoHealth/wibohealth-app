"""Batch 30: title 80-95 chars, no digits in title/desc, desc <= 170 chars, 3 FAQs, every FAQ3 ends with the Boodi link."""
import re, sys
for lang in sys.argv[1:]:
    src = open(f'{lang}.md', encoding='utf-8').read()
    for b in re.split(r'(?m)^## (?=\d+\s*$)', src)[1:]:
        fid = b.split('\n', 1)[0].strip()
        t = re.search(r'(?m)^title: (.*)$', b).group(1); d = re.search(r'(?m)^desc: (.*)$', b).group(1)
        faq = b.split('### FAQ', 1)[1]
        n = len(re.findall(r'(?m)^\*\*', faq))
        bad = []
        if not 80 <= len(t) <= 95: bad.append(f'title {len(t)}')
        if re.search(r'\d', t + d): bad.append('digits')
        if len(d) > 170: bad.append(f'desc {len(d)}')
        if n != 3: bad.append(f'faq {n}')
        if faq.count('(/boodi.html)') != 1: bad.append('cta')
        if bad: print(lang, fid, bad, '|', t)
    print(lang, 'checked')
