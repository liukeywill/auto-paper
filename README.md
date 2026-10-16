# Auto Paper

面向教育、社科与文旅的一句话科研成稿 agent。从主题连续检索、精读、分析、写作和修订，默认以北大核心期刊投稿要求为目标，交付完整论文 Word、Markdown、证据附件及投稿准备度审查。用于自动科研、自动写论文或继续 Auto Paper项目；单项润色或作图用对应技能。

## 安装到 Codex

需要 Python 3、网络连接及 Codex 自带的 skill-installer。安装完整目录及其参考文件：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo liukeywill/auto-paper \
  --path . \
  --name auto-paper
```

安装后在下一条消息中调用 `$auto-paper`。已有同名目录时安装器不会覆盖，请先备份并确认更新方式。

## 使用示例

```text
$auto-paper 选题：城市遗产更新；学科：文旅与社会学；字数：8000；语言：中文。
```

连续推进检索、证据整理、分析、写作与修订。缺少真实数据或来源受阻时保留限制，不编造文献、结果或完成状态。Python 运行时依赖见 requirements.txt。

完整指令、材料要求及核查规则见 [SKILL.md](SKILL.md)。只按实际材料和工具结果报告完成情况，生成内容不自动授权对外发布或提交。

## 仓库结构

本仓库根目录即技能目录，保留原有 `SKILL.md`、`agents/` 及随附参考资料；存在的脚本、配置和依赖清单也一并保留。
