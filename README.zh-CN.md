# Zone Memory Skill

`Zone Memory` 是一个可移植的 skill 包，用来给编码项目快速建立一套轻量协作操作系统：

- 规划 / 执行 / 验收 / 维护 四区分工
- `docs/project_notes/` 项目记忆文件
- `AGENTS.md` / `CLAUDE.md` 协作规则
- 短任务卡、低 token 交接

它不是只给 Codex 用的。这个包把真正可迁移的部分抽出来了：规则、模板、文档结构。同时这版也把平台行为定清楚了：

- Codex：自动创建四个分区，并自动发送四段开场白
- 非 Codex：不自动创建分区，但第一次调用时必须返回手动创建步骤和四段可直接复制的开场白

## 目录结构

- `skills/zone-memory`: 真正的 skill 内容
- `install.py`: 安装到 Codex 和/或 Claude
- `build_release.py`: 打 ZIP 发布包
- `tests/test_delivery.py`: 最小交付检查

## 本地安装

```bash
python3 install.py --agent codex
python3 install.py --agent claude
python3 install.py --agent both
```

只预览，不落盘：

```bash
python3 install.py --agent both --dry-run
```

升级已有安装：

```bash
python3 install.py --agent both --upgrade
```

## 从 GitHub Repo 安装

```bash
git clone https://github.com/Jeffrey22444/zone-memory.git
cd zone-memory
python3 install.py --agent both
```

推荐按平台分别安装：

```bash
git clone https://github.com/Jeffrey22444/zone-memory.git
cd zone-memory
python3 install.py --agent codex
```

```bash
git clone https://github.com/Jeffrey22444/zone-memory.git
cd zone-memory
python3 install.py --agent claude
```

如果某个 Agent 不支持本地 skill 目录安装，也可以直接把
`skills/zone-memory` 下的 Markdown 文件复制到对应平台的 prompt/skill
目录，或者手动把模板放进你的项目里使用。

## 使用方式

1. 安装 skill。
2. 在目标项目中调用 `zone-memory`。
3. 让 Agent 检查仓库并初始化：
   - `docs/project_notes/bugs.md`
   - `docs/project_notes/decisions.md`
   - `docs/project_notes/key_facts.md`
   - `docs/project_notes/issues.md`
   - `docs/project_notes/zone_operating_model.md`
4. 把工作流规则合并进项目的 `AGENTS.md` 或 `CLAUDE.md`。
5. 如果你在 Codex 里，Agent 应自动创建这四个分区：
   - `规划区`
   - `执行区`
   - `验收区`
   - `维护区`
6. 如果你不在 Codex 里，就手动创建四个 chat / thread，并把 `skills/zone-memory/references/opening_prompts.md` 里的对应开场白分别贴进去。

## 非 Codex 用户怎么手动创建

1. 新建四个独立的 chat、thread，或者四个长期保留的对话入口。
2. 名字固定为：
   - `规划区`
   - `执行区`
   - `验收区`
   - `维护区`
3. 把 `skills/zone-memory/references/opening_prompts.md` 里对应分区的开场白粘进去。
4. 后续同一个项目持续复用这四个分区，不要每次重新开零散对话。

## 第一次调用时的行为

- 在 Codex 里：第一次调用应自动建四区，并自动把四段开场白发进去。
- 在非 Codex 平台：第一次调用应直接返回四段开场白，供用户手动粘贴。

## 推荐分发方式

直接把 GitHub 仓库本身当成交付物。

- 用户先 `git clone`
- 再运行 `python3 install.py --agent codex` 或 `--agent claude`
- 不需要额外包管理器

## 为什么这样做

- 核心可移植，Codex 额外享受自动建区
- 只用 Python 标准库
- 安装契约简单
- 模板都是纯 Markdown，没工具也能直接复用
