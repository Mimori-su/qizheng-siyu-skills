# ChatGPT Adapter

ChatGPT 可通过两种方式使用本项目：

1. ChatGPT Skills：上传或安装 `chatgpt/skills/` 下的 12 个 Skill。
2. Custom GPT：把 `custom-gpt-instructions.md` 放入 Instructions，并把 `knowledge-files.md` 中列出的文件上传为 Knowledge。

## ChatGPT Skills

Skill 目录结构已经按 Agent Skills 风格准备：

```text
chatgpt/skills/qz-reader/SKILL.md
chatgpt/skills/qz-reader/resources/
chatgpt/skills/qz-reader/scripts/
```

如 ChatGPT 工作区要求逐个上传 Skill，请逐个选择 `qz-study`、`qz-reader`、`qz-core` 等目录。

## Custom GPT

Custom GPT 不会自动理解整个仓库目录。建议：

- Instructions：使用 `chatgpt/custom-gpt-instructions.md`。
- Knowledge：优先上传 shared contracts、shared references、shared prompts 和关键 Skill.md。
- Actions：本项目不默认配置外部 API Actions；脚本应在本地 Codex/Cursor/Claude Code 环境执行。

## 安全边界

ChatGPT 输出也必须遵守谨慎表达：不做医学诊断、法律意见、投资建议或确定性命理断语。
