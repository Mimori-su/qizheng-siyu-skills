# qizheng-siyu-skills Claude Code Instructions

本目录为 Claude Code 原生适配层。处理七政四余任务时，优先遵守本文件，再读取对应 Skill。

## 核心数据流

```text
qz-study -> qz-reader -> qz-core -> topic skills -> qz-report
```

## 使用规则

- 学习、术语、课程总结：读取 `skills/qz-study/SKILL.md`。
- 读盘、提取、校验：读取 `skills/qz-reader/SKILL.md`，输出 `qz_structured_data.md`，不解读吉凶。
- 原局分析：读取 `skills/qz-core/SKILL.md`，必须先有 `qz_structured_data.md`。
- 专题分析：读取对应专题 Skill，并继承 `qz_core_report.md`。
- 报告整合：读取 `skills/qz-report/SKILL.md`，只整合已有报告。

## 安全规则

所有输出必须包含支持因素、制约因素、缺失数据、不确定项和谨慎结论。疾病、法律、投资、心理危机等高风险问题只能作传统术数取象参考，并提醒咨询现实专业人士。

## 可用 Slash Commands

本目录提供 `.claude/commands/qz-*.md`，可作为 Claude Code 项目命令复制到项目或用户级 `.claude/commands/`。
