# Codex Adapter

本目录提供 Codex 可直接复用的 Agent Skills 镜像。

## 安装

根据本地环境调整路径：

```bash
cp -r codex/skills/* ~/.codex/skills/
```

## 使用原则

- `qz-reader` 只读盘、提取、校验，不做解读。
- `qz-core` 必须读取 `qz_structured_data.md` 后再做原局分析。
- 所有专题 Skill 必须继承 `qz_core_report.md`。
- 涉及疾病、法律、投资、心理危机时，只能作为传统术数取象参考，并提醒咨询现实专业人士。

## 更新方式

运行：

```bash
python shared/scripts/sync_skills.py --targets codex --yes --no-backup
```
