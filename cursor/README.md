# Cursor Adapter

Cursor 的原生入口是项目规则。实际规则文件已放在：

```text
.cursor/rules/
```

打开本仓库时，Cursor 可读取这些规则并把本项目当作七政四余工作流使用。

## 规则文件

- `.cursor/rules/qz-router.mdc`：总体路由、数据流和 Skill 边界。
- `.cursor/rules/qz-data-contract.mdc`：Reader/Core/专题之间的数据契约。
- `.cursor/rules/qz-safety.mdc`：疾病、法律、投资等高风险安全表达。
- `.cursor/rules/qz-platform-files.mdc`：平台目录说明与文件修改边界。

## 使用方式

在 Cursor 中打开项目根目录后，可以直接要求：

- “用 qz-reader 处理这个盘面文本。”
- “基于 qz_structured_data.md 生成 qz_core_report.md。”
- “把这个项目同步到 Codex/Claude Code/ChatGPT 适配目录。”

Cursor 不是 `SKILL.md` 自动安装环境，因此 `.cursor/rules` 是本项目的 Cursor 原生补齐层。
