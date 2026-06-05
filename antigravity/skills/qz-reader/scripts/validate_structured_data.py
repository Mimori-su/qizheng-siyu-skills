#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path
HEADINGS=['## 1. 元信息','## 2. 数据完整性','## 3. 太极与命身','## 4. 七政四余星曜位置','## 5. 十二宫','## 6. 二十八宿','## 7. 神煞','## 8. 原局初步标记','## 9. 运势资料','## 10. 校验结果']
STARS=['日','月','金','木','水','火','土','罗','气','计','孛']
def main():
    p=argparse.ArgumentParser(); p.add_argument('file', type=Path); a=p.parse_args(); text=a.file.read_text(encoding='utf-8')
    errors=[]
    for h in HEADINGS:
        if h not in text: errors.append(f'missing heading: {h}')
    for s in STARS:
        if not re.search(rf'^\|\s*{s}\s*\|', text, re.M): errors.append(f'missing star row: {s}')
    for key in ['命宫','命度','命度主','身宫','身度','身度主','可信度','来源']:
        if key not in text: errors.append(f'missing field: {key}')
    print('# qz_structured_data validation report')
    if errors:
        print('\n## Errors'); [print('- '+e) for e in errors]
    else: print('\nOK')
    return 1 if errors else 0
if __name__ == '__main__': raise SystemExit(main())
