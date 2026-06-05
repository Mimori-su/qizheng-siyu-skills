#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path
COURSE_RE=re.compile(r'^(第[一二三四五六七八九十百零〇两]+[课講讲])$'); TITLE_RE=re.compile(r'(.+?)[\.。·\s]*([0-9]{1,3})$')
def classify(t):
    for k,v in [
        ('七政四时论','古文资料'),('女命口诀','古文资料'),('相心赋','古文资料'),('月谈赋','古文资料'),('指金赋','古文资料'),
        ('尽三','看盘流程'),('余奴','看盘流程'),('看盘起手式','看盘流程'),('罗计轮回','看盘流程'),
        ('感情','感情专题'),('桃花','感情专题'),('合盘','感情专题'),
        ('财运','财运专题'),('疾病','疾病专题'),('官非','官非专题'),('子女','子女专题'),
        ('择日','择日'),('占盘','占盘'),('生时','生时校正'),('生肖','生肖'),
        ('运势','运势判断'),('倒限','运势判断'),('太极','太极转换'),
        ('星盘','星盘结构'),('五行','干支五行'),('天干','干支五行'),('地支','干支五行'),
        ('十神','十神神煞'),('神煞','十神神煞')
    ]:
        if k in t: return v
    return '基础概念'
def parse(text_dir):
    text=''
    for n in [1,2]:
        p=text_dir/f'page_{n:03d}.txt'
        if p.exists(): text+='\n'+p.read_text(encoding='utf-8', errors='ignore')
    lines=[l.strip() for l in text.splitlines() if l.strip() and not l.startswith('<!--') and not l.startswith('www.')]
    items=[]; i=0
    while i<len(lines):
        if COURSE_RE.match(lines[i]) and i+1<len(lines):
            m=TITLE_RE.match(lines[i+1])
            if m: items.append((lines[i],m.group(1).strip('. 。·'),int(m.group(2)))); i+=2; continue
        m=TITLE_RE.match(lines[i])
        if m and not lines[i].isdigit() and any(k in m.group(1) for k in ['七政','气象','口诀','相心','月谈','指金']): items.append(('篇目',m.group(1).strip('. 。·'),int(m.group(2))))
        i+=1
    return items
def main():
    p=argparse.ArgumentParser(); p.add_argument('--text-dir', default=Path('build/pdf_text'), type=Path); p.add_argument('--out', default=Path('shared/references/source_map.md'), type=Path); a=p.parse_args(); items=parse(a.text_dir)
    if not items: raise SystemExit(f'no TOC items found in {a.text_dir}')
    rows=[
        '# Source Map',
        '',
        f'文本目录：`{a.text_dir}`',
        '',
        '本文件由提取出的 PDF 目录页自动生成，只保存章节索引，不保存教材正文。',
        '',
        '| ID | 来源 | 页码范围 | 类型 | 自动整理内容 | 人工复核重点 |',
        '|---|---|---|---|---|---|'
    ]
    for i,(label,title,start) in enumerate(items,1):
        end=items[i][2]-1 if i<len(items) else 499; rows.append(f'| S{i:03d} | {label} {title} | {start}-{end} | {classify(title)} | 章节索引与 Skill 路由初稿 | 复核标题、页码、术语和案例边界 |')
    a.out.parent.mkdir(parents=True, exist_ok=True); a.out.write_text('\n'.join(rows)+'\n', encoding='utf-8'); print(f'wrote {a.out} ({len(items)} items)'); return 0
if __name__ == '__main__': raise SystemExit(main())
