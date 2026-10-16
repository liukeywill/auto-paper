# Auto Paper · 连续科研成稿

给定论文主题，在实际材料与工具允许的范围内连续推进检索、精读、综合、设计、分析、写作和自审，交付完整论文与可追溯材料。默认面向教育、社科与文旅，按核心期刊投稿目标准备，不承诺发表。

## 定位与选择

| 你的任务 | 使用入口 | 默认方式 |
|---|---|---|
| 通用文章成稿、改写或表达审查 | [Vibe Writing](https://github.com/liukeywill/vibe-writing) | 内部编辑后直接交稿 |
| 从研究方向逐阶段协作，自己把关关键决定 | [Vibe Research](https://github.com/liukeywill/vibe-research) | 每阶段交付并等待人工核查 |
| 按确定主题连续推进到完整论文及材料包 | [Auto Paper](https://github.com/liukeywill/auto-paper) | 在实际条件允许范围内连续执行 |

默认不逐阶段停等人工批准，必要时保留用户指定的人工交接。自动推进不能补造数据、访问权限、全文阅读或人工确认；无法替代的条件缺失时保存进度并说明未完成项。

## 安装到 Codex

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo liukeywill/auto-paper \
  --path . \
  --name auto-paper
```

需要 Python 3、网络连接及 Codex 的 skill-installer。安装后在下一条消息中调用。已有同名目录不会直接覆盖，更新前先备份并确认现有项目版本。

本仓库包含流水线、schema 和研究基础模块。结构化执行需 `requirements.txt` 中的 jsonschema；数值分析另需相应 Python 库。部分方法、统计和 Word 制作流程还会使用当前环境可用的科研或文档 Skill；这些其他 Skill 不包含在本仓库里。实际缺少能力时交代限制，不将安装本入口说成所有外部能力均已接通。

## 复制即可用

```text
$auto-paper
选题：城市遗产更新中的居民参与
学科：文旅与社会学
字数：8000
语言：中文
请连续检索、整理证据、写作和审查，交付完整论文与材料包。
```

仅主题必填，默认自动判断学科、中文正文约8000字。未指定期刊时核验适配候选与官方要求；质量目标不等于已经达到发表水平。

```text
$auto-paper
选题：AI反馈对大学生写作修改的影响
论文类型：整合性综述
请连续完成中英文文献检索、证据综合、写作与自审。
```

没有真实数据且用户未限定类型时，可以明确选择综述或理论论文。用户指定实证论文而不可替代数据缺失时，保留已完成部分并标记未完成，不暗改类型、不编结果。

## 执行与交付

| 阶段 | 工作 |
|---|---|
| scope | 收敛问题、对象、范围与论文类型 |
| search | 中英文检索、纳排与候选去重 |
| read | 实际精读、原文定位与证据登记 |
| synthesize | 文献矩阵、分歧与研究框架 |
| design | 方法、评价标准、竞争解释与可行性 |
| analyze | 实际数据分析，或明确 planned／not_applicable |
| package | 完整论文、报告与 Word 制作检查 |
| review | 证据、方法、论断、引用与投稿准备度审查 |

默认交付论文 Word、Markdown、JSON，附检索、证据、框架、分析和质量记录。内置数值适配器为 OLS＋HC3，其他方法按实际能力扩展；脚本校验不证明语义正确、创新或可发表性。不会自动投稿或公开发布。

```text
继续 Auto Paper，项目在 /你的项目绝对路径/科研项目/项目名
```

恢复沿用项目 profile、冻结脚本及材料版本；上游材料变化会令受影响阶段失效并要求复核。

## 共用研究基础与版本

与 Vibe Research 共用 [Research Core](https://github.com/liukeywill/research-core) **1.0.0**，统一问题与设计、文献证据、主张审查及版本追溯。逐文件哈希和固定来源提交见 [锁文件](shared/research-core.lock.json)。模块随包内置，无需另装 Research Core 或 Vibe Research。

Auto Paper 继续使用自己的流水线、JSON schema、自动推进和成果验收，不从共用模块继承逐阶段人工等待。新 structured 项目将共用规范与锁文件一并纳入 runtime-snapshot／engine-manifest；旧项目不静默升级。项目格式尚不支持与 Vibe Research 一键互转。

[模块适配和旧项目规则](references/research-core-adapter.md) · [完整 Skill](SKILL.md) · [自动成稿说明](references/autonomous-manuscript.md) · [组件来源与许可](references/components.md)

## 维护与验证

共享规范只在 Research Core 来源仓库更新，通过其 sync_consumers.py 同步并检查本仓库快照；不要单独改 vendored 文件。现有项目保持原冻结版本，更新只作用于新项目或明确承接的新项目。

脚本测试是离线技术验证，不等于真实研究结论或实际论文生成效果测试。各第三方组件许可按原来源维护，不能将整个组合统一称为 MIT。
