#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, shutil
from pathlib import Path
TARGETS={
    'claude-code': Path('claude-code/skills'),
    'codex': Path('codex/skills'),
    'chatgpt': Path('chatgpt/skills'),
}
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root', default=Path(__file__).resolve().parents[2], type=Path)
    p.add_argument('--targets', nargs='*', choices=sorted(TARGETS), default=['claude-code'])
    p.add_argument('--yes', action='store_true')
    p.add_argument('--no-backup', action='store_true')
    a=p.parse_args()
    src=a.root/'antigravity'/'skills'
    if not src.exists(): raise SystemExit(f'missing source: {src}')
    total=0
    for target in a.targets:
        dst=a.root/TARGETS[target]
        if dst.exists() and any(dst.iterdir()) and not a.yes: raise SystemExit(f'destination exists: {dst}; rerun with --yes')
        if dst.exists() and any(dst.iterdir()) and not a.no_backup:
            backup=dst.with_name('skills.backup-'+target+'-'+dt.datetime.now().strftime('%Y%m%d%H%M%S')); shutil.copytree(dst, backup); print(f'backup: {backup}')
        if dst.exists(): shutil.rmtree(dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src,dst)
        count=sum(1 for _ in dst.glob("*/SKILL.md")); total+=count
        print(f'synced {count} skills from {src} to {dst}')
    print(f'total synced skill copies: {total}')
    return 0
if __name__ == '__main__': raise SystemExit(main())
