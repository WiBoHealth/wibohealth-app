"""Batch 30: replace title/desc lines of one language file from a {id: (title, desc)} table (None keeps the line).
Usage: python -X utf8 -I set_meta.py <lang> <table.py>"""
import re
import sys

lang, table = sys.argv[1], sys.argv[2]
META = {}
exec(open(table, encoding='utf-8').read())
path = f'{lang}.md'
src = open(path, encoding='utf-8').read()
parts = re.split(r'(?m)^(## \d+\s*)$', src)
for i in range(1, len(parts), 2):
    fid = int(parts[i][3:])
    if fid not in META:
        continue
    t, d = META[fid]
    body = parts[i + 1]
    if t:
        body = re.sub(r'(?m)^title: .*$', lambda m: 'title: ' + t, body, count=1)
    if d:
        body = re.sub(r'(?m)^desc: .*$', lambda m: 'desc: ' + d, body, count=1)
    parts[i + 1] = body
open(path, 'w', encoding='utf-8', newline='\n').write(''.join(parts))
print('updated', len(META))
