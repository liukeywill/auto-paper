# Auto Paper 已合并到 Vibe Research

完整功能现由 [Vibe Research](https://github.com/liukeywill/vibe-research) 统一维护，提供人工核查、自动成稿两种模式。此仓库只保留旧名称兼容入口，不再包含独立引擎。

## 安装统一技能

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo liukeywill/vibe-research \
  --path . \
  --name vibe-research
```

安装后使用：

```text
$vibe-research 模式：自动成稿；选题：城市遗产更新中的居民参与；字数：8000。
```

只给研究方向时默认人工核查。已有 Auto Paper 项目可以直接提供路径恢复，沿用原 profile 与冻结脚本，不重新初始化。已经安装旧版本的用户，先保留项目与原安装备份，再安装统一技能并更新本兼容入口；不要把旧安装中残留的脚本当作当前发布引擎。

`$auto-paper` 仍可作为兼容调用，但要求同级目录中已安装 Vibe Research。新用户只需安装统一技能。历史实现保留在 Git 历史及 [合并前版本](https://github.com/liukeywill/auto-paper/tree/pre-unification-2026-10-16) 中；新维护只在统一仓库进行。
