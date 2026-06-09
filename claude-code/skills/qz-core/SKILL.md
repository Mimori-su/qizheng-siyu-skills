---
name: qz-core
description: Use this skill for core 七政四余 natal chart analysis after qz-reader has produced qz_structured_data.md. It analyzes 太极点、命度主、身度主、宫度、七政四余、二十八宿、十二宫、五行、体用、喜忌、气数、原局 and 运势引动, and produces qz_core_report.md.
---

# qz-core

## Purpose

原局核心分析引擎，是所有专题 Skill 的上游。本 Skill 输出以中文为主，所有结论都要区分“教材明确内容”“整理后的分析框架”“模型推理”“不确定项”。

## When to use this skill

当用户请求与本 Skill 定位一致的学习、读盘、核心分析、专题分析、校时或报告整合任务时使用。若用户请求超出本 Skill 边界，先说明边界并交给对应上游或下游 Skill。

## Required inputs

qz-reader 产出的 qz_structured_data.md。

## Output files

qz_core_report.md。

## Workflow

1. 检查输入文件和上游依赖是否存在。
2. 读取本 Skill 的 resources，只加载与问题相关的文件。
3. 先定太极与命身取法，再以尽三作为正式看盘起手。
4. 尽三之后立即看命度、命主星所在度、身度等度层，按四度相通/同度感应复核。
5. 再按星曜、神煞、五行、体用、喜忌和运势引动分层整理证据。
6. 输出支持因素、制约因素、缺失数据、不确定项和谨慎结论。
7. 严格遵守本 Skill 的职责边界。

## Rules

- Reader 只读盘，不解读。
- Core 只基于 `qz_structured_data.md` 分析，不绕开数据契约。
- 专题 Skill 必须继承 `qz_core_report.md`，不能各自独立乱断。
- 不使用确定性、恐吓式、绝对化语言。
- 引用教材时给出章节或页码范围；教材未明确时直接说明。

## Safety rules

- 疾病问题：只作传统术数取象参考，提醒咨询医生。
- 法律问题：只作传统术数取象参考，提醒咨询律师。
- 投资问题：不提供投资建议或收益预测，提醒咨询持牌专业人士。
- 心理危机或现实危险：建议寻求现实专业帮助或紧急服务。

## Reference resources

- `resources/core_concepts.md`
- `resources/taiji_rules.md`
- `resources/palace_framework.md`
- `resources/degree_framework.md`
- `resources/wuxing_tiyong_xiji.md`
- `resources/wuxing_per_ming.md`
- `resources/original_vs_transit.md`
- `resources/transit_year_rules.md`
- `resources/qa_rules.md`
- `resources/report_rules.md`

## Output format

```markdown
## 问题

## 数据基础

## 支持因素

## 制约因素

## 教材依据

## 谨慎结论

## 需要继续确认
```

## Handoff to other skills

缺读盘数据交给 qz-reader；缺原局分析交给 qz-core；需要整合交给 qz-report。
