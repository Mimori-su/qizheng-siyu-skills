#!/usr/bin/env python3
from __future__ import annotations
import json, re
from pathlib import Path
SKILLS=['qz-study','qz-reader','qz-core','qz-love','qz-wealth','qz-health','qz-career','qz-children','qz-lawsuit','qz-election','qz-rectifier','qz-report']; IGNORE={'.git','__pycache__','.pytest_cache','build'}
SKILL_BASES=['antigravity/skills','claude-code/skills','codex/skills','chatgpt/skills']
MIN_RESOURCE_NONBLANK_LINES=8
def skip(p): return bool(set(p.parts)&IGNORE)
def fm(text): return bool(re.match(r'^---\n[\s\S]*?\n---\n', text)) and 'name:' in text and 'description:' in text
def main():
    root=Path(__file__).resolve().parents[2]; errors=[]; warnings=[]
    if not (root/'README.md').exists(): errors.append('missing README.md')
    for base in SKILL_BASES:
        for s in SKILLS:
            d=root/base/s; sf=d/'SKILL.md'; res=d/'resources'
            if not d.exists(): errors.append(f'missing skill dir: {base}/{s}')
            if not sf.exists(): errors.append(f'missing SKILL.md: {base}/{s}')
            elif not fm(sf.read_text(encoding='utf-8')): errors.append(f'invalid front matter: {sf}')
            if not res.exists() or not any(p.is_file() and p.stat().st_size>20 for p in res.rglob('*')): errors.append(f'empty resources: {base}/{s}')
            if res.exists():
                for rp in res.rglob('*.md'):
                    nonblank=[line for line in rp.read_text(encoding='utf-8', errors='ignore').splitlines() if line.strip()]
                    if len(nonblank)<MIN_RESOURCE_NONBLANK_LINES: errors.append(f'resource too thin ({len(nonblank)} lines): {rp}')
    text_dir=root/'build/pdf_text'; index=text_dir/'index.json'; pages=list(text_dir.glob('page_*.txt'))
    if not index.exists(): errors.append('missing PDF extraction index: build/pdf_text/index.json')
    elif len(pages)<400: errors.append(f'PDF extraction appears incomplete: {len(pages)} page files')
    else:
        try:
            data=json.loads(index.read_text(encoding='utf-8'))
            if data.get('pages',0)<400: errors.append(f'PDF extraction index reports too few pages: {data.get("pages")}')
        except Exception as exc: errors.append(f'invalid PDF extraction index: {exc}')
    for ds in root.rglob('.DS_Store'):
        if not skip(ds): errors.append(f'DS_Store file is not allowed: {ds}')
    required_files=[
        'codex/README.md',
        'chatgpt/README.md',
        'chatgpt/custom-gpt-instructions.md',
        'chatgpt/knowledge-files.md',
        'chatgpt/skills-upload-manifest.md',
        'cursor/README.md',
        '.cursor/rules/qz-router.mdc',
        '.cursor/rules/qz-data-contract.mdc',
        '.cursor/rules/qz-safety.mdc',
        '.cursor/rules/qz-platform-files.mdc',
        'claude-code/CLAUDE.md',
    ]
    for f in required_files:
        path=root/f
        if not path.exists() or path.stat().st_size<100: errors.append(f'missing or too small platform adapter file: {f}')
    command_dir=root/'claude-code/.claude/commands'
    if len(list(command_dir.glob('qz-*.md')))<12: errors.append('missing Claude Code qz slash command files')
    for z in root.rglob('*.zip'):
        if not skip(z): errors.append(f'zip file is not allowed: {z}')
    for md in root.rglob('*.md'):
        if skip(md): continue
        text=md.read_text(encoding='utf-8', errors='ignore').strip()
        if not text: errors.append(f'empty markdown: {md}')
        compact=re.sub(r'[#|`\-\s:：/._0-9A-Za-z]', '', text)
        if 'TODO' in text.upper() and len(compact)<8: errors.append(f'TODO-only markdown: {md}')
        if text.count('<!-- PDF page')>3: errors.append(f'raw PDF page text appears in markdown: {md}')
    print('# quality_check report'); print(f'root: {root}')
    if errors:
        print('\n## Errors'); [print('- '+e) for e in errors]
    if warnings:
        print('\n## Warnings'); [print('- '+w) for w in warnings]
    if not errors and not warnings: print('\nOK')
    return 1 if errors else 0
if __name__ == '__main__': raise SystemExit(main())
