# qizheng-siyu-skills

`qizheng-siyu-skills` 是一个七政四余多 Skill AI 辅助项目，用于把七政四余相关学习资料、盘面读取、数据契约、核心分析流程和专题分析拆成可协作的 Skill 体系。项目提供 ChatGPT / Cursor / Codex / Antigravity / Claude Code 五类智能体适配入口。

本项目的架构思想：Reader 负责数据入口，Core 负责核心分析，专题 Skill 继承 Core 结论，Rectifier 独立校时，Report 做最终整合。

## 计算体系

本项目约定盘面计算使用郑案古宿+岁差。Reader 在记录盘面来源时，应优先标注排盘软件、宿界体系、岁差处理方式和可信度。

推荐使用 iOS 应用“七政四余排盘”导出盘面文字。读盘时优先使用软件导出的文字描述或可复制文本，尽量不要依赖截图识别；截图和 OCR 只适合作为补充核对来源。

| 星宿 |    度数 |
| ---- | ------: |
| 娄   |     15° |
| 胃   |   26.5° |
| 昴   |  42.03° |
| 毕   |   53.1° |
| 觜   |  70.16° |
| 参   |  71.08° |
| 井   |  81.02° |
| 鬼   | 113.73° |
| 柳   | 115.94° |
| 星   | 128.96° |
| 张   | 135.15° |
| 翼   | 152.35° |
| 轸   | 170.89° |
| 角   | 188.07° |
| 亢   | 200.03° |
| 氐   | 208.93° |
| 房   | 225.21° |
| 心   |  230.7° |
| 尾   | 236.98° |
| 箕   | 255.74° |
| 斗   | 265.93° |
| 牛   |  290.6° |
| 女   | 297.84° |
| 虚   | 308.89° |
| 危   |  317.7° |
| 室   | 333.06° |
| 壁   | 349.97° |
| 奎   | 358.44° |

## 为什么不是一个 Skill

七政四余的任务天然分层：学习教材、读盘提取、原局分析、专题判断、生时校正和报告整合需要不同的输入、校验和安全边界。把所有内容塞进一个 Skill 会让 Reader 误做解读、专题绕过数据契约、输出口径不一致。本项目用 12 个 Skill 分担职责，确保每一步都有明确上游、下游和限制。

## 项目架构图

```text
用户问题 / 用户盘面 / PDF教材
        |
        v
qz-study：教材学习、术语解释、学习路线
        |
        v
qz-reader：读盘、提取、校验
        |
        v
qz_structured_data.md
        |
        v
qz-core：太极命身、尽三起手、三度/同度复核、宫度星、五行体用喜忌、原局、运势
        |
        v
qz-love / qz-wealth / qz-health / qz-career / qz-children / qz-lawsuit / qz-election / qz-rectifier
        |
        v
qz-report：整合报告
```

## 每个 Skill 的职责

| Skill        | 职责                                                         |
| ------------ | ------------------------------------------------------------ |
| qz-study     | 教材学习、术语解释、章节摘要、记忆卡和学习路线，不正式断盘。 |
| qz-reader    | 从 PDF、截图或文本中提取盘面数据，校验并输出 `qz_structured_data.md`，不解读吉凶。 |
| qz-core      | 基于 Reader 数据做原局核心分析，先定太极命身，再以尽三起手，继而看三度/同度复核，输出 `qz_core_report.md`。 |
| qz-love      | 感情、婚姻、桃花、合盘专题，继承 Core 结论。                 |
| qz-wealth    | 财运、资产、田宅、收入、破财专题，避免投资建议。             |
| qz-health    | 疾病与健康取象专题，只作传统术数参考，不作医学诊断。         |
| qz-career    | 事业、官禄、工作、名望、升迁专题。                           |
| qz-children  | 子女、生育与亲子关系专题，涉及健康时提醒就医。               |
| qz-lawsuit   | 官非、纠纷、合同和法律风险取象，提醒咨询律师。               |
| qz-election  | 择日流程，兼顾现实约束，不保证必吉。                         |
| qz-rectifier | 生时校正，收集事件并比较候选时辰，不强行定时。               |
| qz-report    | 整合 Core 和专题报告，统一口径，不新增无来源结论。           |

## 推荐使用流程

```text
学习教材 → qz-study
读盘提取 → qz-reader
核心分析 → qz-core
专题分析 → qz-love / qz-wealth / qz-health / qz-career / qz-children / qz-lawsuit / qz-election / qz-rectifier
报告整合 → qz-report
```

## 数据流转说明

1. `qz-reader` 生成 `qz_structured_data.md`，字段必须符合 `shared/contracts/qz_structured_data_contract.md`。
2. `qz-core` 读取结构化数据，先检查完整性，再定太极与命身；正式解盘起手先看尽三。尽三是论宫组合，尽三后接着看命度、命主星所在度、身度等度层，按四度相通/同度感应复核尽三结论，再分层分析星曜、神煞、五行、体用、喜忌和运势引动。
3. 专题 Skill 必须读取 `qz_structured_data.md` 与 `qz_core_report.md`，不能绕过 Reader/Core 自行下断语。
4. `qz-report` 只整合既有报告，保留支持因素、制约因素、缺失数据和不确定项。

## 安装方式

根据本地环境调整路径。

### Antigravity

```bash
cp -r qizheng-siyu-skills/antigravity/skills/* ~/.antigravity/skills/
```

部分 Antigravity 工作区也可使用 workspace 级 `.agents/skills/`，请按本地版本文档调整。

### Claude Code

```bash
cp -r qizheng-siyu-skills/claude-code/skills/* ~/.claude/skills/
cp qizheng-siyu-skills/claude-code/CLAUDE.md ./CLAUDE.md
cp -r qizheng-siyu-skills/claude-code/.claude/commands/* ./.claude/commands/
```

### Codex

```bash
cp -r qizheng-siyu-skills/codex/skills/* ~/.codex/skills/
```

### ChatGPT

ChatGPT 有两条路径：

```text
ChatGPT Skills：上传 chatgpt/skills/ 下的 12 个 Skill。
Custom GPT：把 chatgpt/custom-gpt-instructions.md 放入 Instructions，并按 chatgpt/knowledge-files.md 上传 Knowledge。
```

### Cursor

Cursor 原生入口是项目规则。本项目已提供：

```text
.cursor/rules/qz-router.mdc
.cursor/rules/qz-data-contract.mdc
.cursor/rules/qz-safety.mdc
.cursor/rules/qz-platform-files.mdc
```

在 Cursor 中打开本仓库即可读取这些规则。若复制到其他项目，请同步 `.cursor/rules/` 和需要的 shared references/contracts。

## 平台适配差异

| 平台        | 本项目入口                                                   | 原生形态                                | 说明                                                         |
| ----------- | ------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------ |
| Antigravity | `antigravity/skills/`                                        | `SKILL.md` + resources/scripts/examples | 主 Skill 目录。                                              |
| Claude Code | `claude-code/skills/`、`claude-code/CLAUDE.md`、`claude-code/.claude/commands/` | Skill 镜像 + 项目记忆 + slash commands  | 同时支持 Skill 风格和 Claude Code 命令入口。                 |
| Codex       | `codex/skills/`                                              | Agent Skills                            | 与 Antigravity 主目录保持镜像。                              |
| ChatGPT     | `chatgpt/skills/`、`chatgpt/custom-gpt-instructions.md`      | ChatGPT Skills 或 Custom GPT            | Skills 逐个上传；Custom GPT 需手动配置 Instructions/Knowledge。 |
| Cursor      | `.cursor/rules/`、`cursor/README.md`                         | `.mdc` Project Rules                    | Cursor 不以 `SKILL.md` 为主要触发入口，使用规则文件路由。    |

## 测试方式

```bash
python qizheng-siyu-skills/shared/scripts/quality_check.py
python -m pytest qizheng-siyu-skills/shared/tests
```

## 如何添加新专题 Skill

1. 在 `antigravity/skills/` 下创建 `qz-new-topic/`，包含 `SKILL.md`、`resources/` 和 `examples/`。
2. 在 `SKILL.md` 中声明必须读取 `qz_structured_data.md` 和 `qz_core_report.md`。
3. 在 `shared/references/topic_index_full.md` 增加专题入口。
4. 运行 `python qizheng-siyu-skills/shared/scripts/sync_skills.py --targets claude-code codex chatgpt --yes` 同步各 Skill 镜像目录。
5. 运行质量检查和测试。
