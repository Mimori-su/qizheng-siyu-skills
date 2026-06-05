#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
KEYS={'学业':['学','学历','考试','毕业','印'],'工作':['官禄','工作','事业','升职','迁移'],'婚恋':['夫妻','感情','婚','男女','桃花'],'健康':['疾病','相貌','病','身体'],'财务':['财帛','田宅','财库','破财'],'官非':['官非','诉讼','合同','纠纷','官禄']}
def events(path):
    if path.suffix=='.json': return json.loads(path.read_text(encoding='utf-8'))
    return [{'text':l.strip()} for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]
def score(text, evs):
    total=0; notes=[]
    for e in evs:
        body=e.get('text') or ' '.join(map(str,e.values())); hit=[]
        for domain, words in KEYS.items():
            if domain in body or any(w in body for w in words):
                n=sum(1 for w in words if w in text); total+=n; hit.append(f'{domain}+{n}') if n else None
        notes.append(f'{body}: {", ".join(hit) if hit else "未匹配"}')
    return total, notes
def main():
    p=argparse.ArgumentParser(); p.add_argument('--events', required=True, type=Path); p.add_argument('candidates', nargs='+', type=Path); p.add_argument('--out', default=Path('rectification_compare_report.md'), type=Path); a=p.parse_args(); evs=events(a.events)
    rows=[]; detail=[]
    for c in a.candidates:
        s,notes=score(c.read_text(encoding='utf-8'), evs); rows.append((c.name,s)); detail.append('## '+c.name+'\n\n- 匹配分：'+str(s)+'\n'+'\n'.join('- '+n for n in notes))
    rows.sort(key=lambda x:x[1], reverse=True); md='# 候选时辰比较报告\n\n| 候选文件 | 匹配分 |\n|---|---|\n'+''.join(f'| {n} | {s} |\n' for n,s in rows)+'\n说明：脚本只做关键词辅助比较，最终仍需 qz-rectifier 复核。\n\n'+'\n\n'.join(detail)
    a.out.write_text(md, encoding='utf-8'); print(f'wrote {a.out}'); return 0
if __name__ == '__main__': raise SystemExit(main())
