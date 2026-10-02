# -*- coding: utf-8 -*-
"""
Validate every prompts/*.json against categories.json and rebuild README.md + dist/all.json.

    python tools/build.py            # validate + build (exit 1 on errors)
    python tools/build.py --check    # validate only (CI)
"""
import json, os, re, sys, glob
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = {'chatgpt', 'claude', 'gemini', 'deepseek', 'perplexity', 'copilot', 'cursor', 'midjourney', 'dalle', 'leonardo', 'flux', 'sora', 'veo', 'runway', 'kling', 'pika'}
SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
FA_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


def load():
    cats = json.load(open(os.path.join(ROOT, 'categories.json'), encoding='utf-8'))['categories']
    items, errors = [], []
    for path in sorted(glob.glob(os.path.join(ROOT, 'prompts', '*.json'))):
        name = os.path.splitext(os.path.basename(path))[0]
        try:
            rows = json.load(open(path, encoding='utf-8'))
        except Exception as e:  # noqa: BLE001
            errors.append(f'{name}.json: invalid JSON — {e}')
            continue
        for i, r in enumerate(rows):
            r['_file'] = name
            r['_i'] = i
            items.append(r)
    return cats, items, errors


def validate(cats, items, errors):
    by_key = {c['key']: c for c in cats}
    seen = Counter(r.get('slug') for r in items)
    for r in items:
        where = f"{r['_file']}.json[{r['_i']}] {r.get('slug', '?')}"
        for f in ('slug', 'category', 'sub', 'title', 'fa', 'en', 'summary', 'tools', 'tags'):
            if not r.get(f):
                errors.append(f'{where}: missing "{f}"')
        s = r.get('slug', '')
        if s and not SLUG.match(s):
            errors.append(f'{where}: slug must be lowercase kebab-case')
        if seen.get(s, 0) > 1:
            errors.append(f'{where}: duplicate slug')
        c = by_key.get(r.get('category'))
        if not c:
            errors.append(f'{where}: unknown category "{r.get("category")}"')
        elif r.get('category') != r['_file']:
            errors.append(f'{where}: category must match file name ({r["_file"]})')
        elif r.get('sub') not in {x['key'] for x in c['subs']}:
            errors.append(f'{where}: unknown sub "{r.get("sub")}" for {c["key"]}')
        bad = set(r.get('tools') or []) - TOOLS
        if bad:
            errors.append(f'{where}: unknown tools {sorted(bad)}')
        for f in ('title_en', 'summary_en', 'ar', 'title_ar', 'summary_ar'):
            if f in r and not r.get(f):
                errors.append(f'{where}: empty "{f}"')
        for f in ('fa', 'en', 'ar'):
            if len(r.get(f) or '') > 600:
                errors.append(f'{where}: "{f}" longer than 600 characters')
    return errors


def build(cats, items):
    clean = [{k: v for k, v in r.items() if not k.startswith('_')} for r in items]
    os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
    json.dump({'categories': cats, 'prompts': clean}, open(os.path.join(ROOT, 'dist', 'all.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))

    per = defaultdict(Counter)
    for r in items:
        per[r['category']][r['sub']] += 1
    total = len(items)
    fa_total = str(total).translate(FA_DIGITS)

    rows = []
    for c in cats:
        n = sum(per[c['key']].values())
        subs = '، '.join(f"{s['fa']} ({str(per[c['key']][s['key']]).translate(FA_DIGITS)})" for s in c['subs'])
        rows.append(f"| [{c['fa']}](prompts/{c['key']}.json) | {c['en']} | {str(n).translate(FA_DIGITS)} | {subs} |")

    sample = []
    for c in cats:
        first = next((r for r in items if r['category'] == c['key']), None)
        if first:
            sample.append(f"**{c['fa']} — {first['title']}**\n\n> {first['fa']}\n>\n> `{first['en']}`\n")

    readme = open(os.path.join(ROOT, 'tools', 'README.template.md'), encoding='utf-8').read()
    readme = readme.replace('{{TOTAL}}', fa_total).replace('{{TOTAL_EN}}', str(total)).replace('{{CATS}}', str(len(cats)).translate(FA_DIGITS)).replace('{{SUBS}}', str(sum(len(c['subs']) for c in cats)).translate(FA_DIGITS))
    readme = readme.replace('{{TABLE}}', '\n'.join(rows)).replace('{{SAMPLES}}', '\n'.join(sample))
    open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n').write(readme)
    return total


if __name__ == '__main__':
    cats, items, errors = load()
    errors = validate(cats, items, errors)
    if errors:
        print('\n'.join(errors[:200]))
        print(f'\n{len(errors)} error(s)')
        sys.exit(1)
    if '--check' in sys.argv:
        print(f'OK: {len(items)} prompts')
        sys.exit(0)
    print(f'OK: {build(cats, items)} prompts → README.md, dist/all.json')
