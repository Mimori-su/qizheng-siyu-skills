#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path
STARS=[('日','七政'),('月','七政'),('金','七政'),('木','七政'),('水','七政'),('火','七政'),('土','七政'),('罗','四余'),('气','四余'),('计','四余'),('孛','四余')]
PALACES=['命宫','财帛','兄弟','田宅','男女','奴仆','夫妻','疾病','迁移','官禄','福德','相貌']
def val(text,key):
    m=re.search(rf'{key}[：:\s]+([^\n，,；;]+)', text); return m.group(1).strip() if m else ''
def star_row(text, star, typ):
    m=re.search(rf'{star}[^\n]{{0,20}}?(子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥|命|财帛|兄弟|田宅|男女|奴仆|夫妻|疾病|迁移|官禄|福德|相貌)[宫]?[^\n]{{0,20}}?([角亢氐房心尾箕斗牛女虚危室璧壁奎娄胃昴毕觜参井鬼柳星张翼轸][日月火水木金土])?', text)
    palace=(m.group(1)+'宫' if m and len(m.group(1))==1 else (m.group(1) if m else ''))
    degree=m.group(2) if m and m.group(2) else ''
    conf='中' if m else '低'
    return f'| {star} | {typ} |  | {palace} | {degree} |  | 自动初提，需复核 | 输入文本 | {conf} |'
def build(text):
    missing=[k for k in ['命宫','命度','命度主','身宫','身度','身度主'] if not val(text,k)]
    out=['# qz_structured_data.md','','## 1. 元信息','','| 字段 | 内容 | 可信度 | 来源 |','|---|---|---|---|']
    for k in ['出生日期','出生时间','出生地点','性别','排盘软件']:
        out.append(f'| {k} | {val(text,k)} | 低 | 输入文本 |')
    out += ['| 数据来源 | 文本 | 中 | 用户粘贴 |','| 读取方式 | 文本提取 | 中 | parse_chart_text.py |','','## 2. 数据完整性',f'- 缺失项：{", ".join(missing) if missing else "待人工复核"}','- 待用户确认项：所有低可信度字段','','## 3. 太极与命身','','| 项目 | 值 | 说明 | 来源 | 可信度 |','|---|---|---|---|---|']
    for k in ['命宫','命度','命度主','身宫','身度','身度主']:
        out.append(f'| {k} | {val(text,k)} | 自动初提 | 输入文本 | 低 |')
    out += ['| 男命/女命取法 |  | 待确认 | 输入文本 | 低 |','','## 4. 七政四余星曜位置','','| 星曜 | 类型 | 五行 | 宫位 | 星宿/度 | 状态 | 备注 | 来源 | 可信度 |','|---|---|---|---|---|---|---|---|---|']
    out += [star_row(text,s,t) for s,t in STARS]
    out += ['','## 5. 十二宫','','| 序号 | 宫名 | 宫位 | 宫五行 | 宫内星曜 | 神煞 | 备注 | 来源 | 可信度 |','|---|---|---|---|---|---|---|---|---|']
    out += [f'| {i} | {name} |  |  |  |  | 自动模板，待补充 | 输入文本 | 低 |' for i,name in enumerate(PALACES,1)]
    out += ['','## 6. 二十八宿','','| 星宿 | 五行 | 所在宫位 | 相关星曜 | 来源 | 可信度 |','|---|---|---|---|---|---|','','## 7. 神煞','','| 神煞 | 位置 | 作用领域 | 备注 | 来源 | 可信度 |','|---|---|---|---|---|---|','','## 8. 原局初步标记','','注意：本部分由 qz-reader 仅做数据标记，不做解读。','','- 五行明显偏性：待 qz-core 复核','- 命身关键星曜：待 qz-core 复核',f'- 明显缺失项：{", ".join(missing) if missing else "待人工复核"}','- 可交给 qz-core 复核的点：自动解析结果可信度偏低','','## 9. 运势资料','','| 类型 | 内容 | 来源 | 可信度 |','|---|---|---|---|','| 流年 |  |  |  |','| 限度 |  |  |  |','| 倒限 |  |  |  |','| 其他 |  |  |  |','','## 10. 校验结果','','- 七政四余完整性：待校验','- 宫度一致性：待校验','- 命身信息一致性：待校验','- OCR 可疑项：无 OCR；文本仍需人工复核','- 需要用户确认的字段：所有低可信度字段']
    return '\n'.join(out)+'\n'
def main():
    p=argparse.ArgumentParser(); p.add_argument('--input', required=True, type=Path); p.add_argument('--out', default=Path('qz_structured_data.md'), type=Path); a=p.parse_args()
    a.out.write_text(build(a.input.read_text(encoding='utf-8')), encoding='utf-8'); print(f'wrote {a.out}'); return 0
if __name__ == '__main__': raise SystemExit(main())
