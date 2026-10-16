---
name: auto-paper
description: "原 Auto Paper 的兼容入口，已合并到 Vibe Research；用于明确调用 $auto-paper 或恢复旧 Auto Paper 项目，默认转入统一技能的自动成稿模式，不再维护独立科研引擎。"
---

# Auto Paper 兼容入口

完整科研功能已合并到 Vibe Research。本入口不包含第二套引擎或研究规范。

1. 检查与本技能同级的 `../vibe-research/SKILL.md` 是否存在；可用时读取该入口，并按其选择与恢复模式。
2. 对明确调用 `$auto-paper` 的新项目，默认传递“自动成稿”意图；用户明确要求人工核查时尊重该要求。提供已有项目路径时保留实际模式、profile 和冻结版本，不能重新初始化。
3. 继续旧 Auto Paper 项目时，从项目 runtime-snapshot 运行旧脚本，不需要旧安装目录保留另一套代码。
4. 如果统一技能未安装，说明需要安装 `liukeywill/vibe-research` 的完整根目录；不假装功能已执行，不回落旧引擎，不自动安装、联网读取或上传资料。

统一仓库：https://github.com/liukeywill/vibe-research
