# 工具篇：AI 辅助编程与项目版本管理

目录编号为 `ChapterX`，课件仍称“工具篇”。教学安排在第1章之后、第2章之前，第1—12章编号保持不变。环境配置、VS Code、AI 编程和 Git 内容从第1章迁入；第1章保留课程介绍与学习动机。

- [课件 PDF](latex/tools.pdf)
- [课件源码](latex/tools.tex)

## 学习顺序

1. VS Code 与学习路线：认识文件、编辑区、终端，明确工具分工。
2. 项目环境：在 `py4fi-course` 创建 `.venv`、安装依赖、选择 Notebook 内核，理解如何重建环境。
3. Git 本地版本管理：手写平均值小程序，学习差异、暂存、提交、分支与合并，再区分 Git 和 GitHub。
4. GitHub 同步课程：克隆 `python-for-finance`、重建课程环境、课前拉取更新，用个人分支保存练习。
5. AI 辅助编程：回到 `py4fi-course` 打开 Qoder，从实际任务理解工具调用、`AGENTS.md` 与 Skill，再用 Git 审查和保存 AI 修改。
6. 综合练习：将两期收益率程序扩展到多期，在分支中验证并保存版本。

先学会编辑、运行和版本管理，再获取课程，最后引入 AI；AI 操作沿用前面已经学过的检查与验证方法。

本篇使用 Qoder CN 桌面端，同类工具可沿用相同的任务描述与验证流程。课件中的软件入口以实际版本为准。

## 课堂练习

本篇使用两个并列目录：`py4fi-course` 从空目录建立，用于环境、Git 和 AI 小练习；`python-for-finance` 从 GitHub 克隆，用于课程材料与后续章节。两者各有自己的 `.venv` 和 Git 历史，切换目录时检查终端路径与 Notebook 内核。

Git 入门先运行 `[2,4,6]` 的平均值程序（输出 `4.0`），在分支中增加数字 `8`（输出 `5.0`）并合并。GitHub 同步完成后，切回练习目录，先打开 Qoder 再进行 AI 任务。后续 NumPy、pandas 与可视化练习继续使用本篇的项目工作流程。

完成练习时保留两个可运行的 Git 版本，并能展示差异、运行命令和手算核对结果。两期价格 `[100, 110, 99]` 的累计收益率为 -1%；扩展后的三期价格 `[100, 110, 99, 108.9]` 的累计收益率为 8.9%。

## 编译

在本篇 `latex/` 目录运行两次：

```powershell
xelatex -interaction=nonstopmode -halt-on-error tools.tex
```

## 从 GitHub 获取与同步课程

课程仓库：[aiqfin/python-for-finance](https://github.com/aiqfin/python-for-finance)。2026-09-24 核对为公开仓库，默认分支为 `master`。此前空目录练习的 `main` 与课程分支名不同。

首次获取，在准备保存课程的父目录执行（需先安装 Git、uv）：

```bash
git clone https://github.com/aiqfin/python-for-finance.git
cd python-for-finance
git remote -v
git branch --show-current
uv sync --locked
```

用 VS Code 打开新建的 `python-for-finance` 文件夹，阅读章节 README，打开 Notebook 并选择仓库根目录的 `.venv` 内核。也可用 VS Code 的 `Git: Clone` 命令完成克隆。只接收公开课程无需先 Fork；ZIP 解压目录不能直接用 `git pull`。

每次上课前，先保存编辑器内容并运行 `git status`。确认工作区干净、当前为 `master` 且没有个人提交后：

```bash
git pull --ff-only origin master
uv sync --locked
git log -3 --format="%s"
```

开始写个人练习前，从课程主分支运行 `git switch -c my-work`。之后在该分支编辑、运行并提交指定练习文件；已存在分支时用 `git switch my-work`。Notebook 的输出变化也可能需要处理。自己的修改提交后，确认工作区干净，再接收老师更新：

```bash
git switch master
git pull --ff-only origin master
git switch my-work
git merge master
```

合并成功后执行 `uv sync --locked` 并验证相关例子。遇到历史分叉或 Notebook 冲突，保留现状并请老师协助；不要通过丢弃自己的修改完成同步。老师必须将提交推送到 GitHub，学生才能获取；学生不需要也通常没有权限向老师仓库推送。本地 commit 不等于上传作业。

仓库只传输已跟踪且已推送的文件，`.venv`、生成的课件 PDF 和部分大型数据被忽略；依照章节 README 重建环境、编译课件或获取数据。

参考：[GitHub 克隆指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)、[Git pull](https://git-scm.com/docs/git-pull)、[VS Code 克隆入口](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes)、[uv 环境同步](https://docs.astral.sh/uv/concepts/projects/sync/)。

## Qoder 操作参考

- [Qoder CN 官方下载页](https://qoder.cn/download)
- [Qoder CN 官方快速入门](https://docs.qoder.cn/qoder/quickstart)

核对日期：2026-09-24。环境与 Git 的参考链接保留在对应课件页。

## AI 编程概念与练习

先打开 Qoder 并确认练习目录，再读取 Git 入门中已有的平均值程序，把输入改回 `[2,4,6]`。通过工具调用、项目约定与技能练习（答案通过下一步展开），区分模型生成代码、工具执行命令和 Python 返回结果，再迁移到收益率验证。

- `AGENTS.md`：在练习目录编写项目约定，显式要求读取，并核对实际执行。自动加载与 `/memory` 的说明明确限定为 Qoder CLI；桌面端不假定具有完全相同的加载规则。
- Tool calling：工具名称、参数、执行结果及 Agent 循环。课件中的 `run_command` 是教学接口示意，不是实际 Qoder API。
- Skill：展示自编 `SKILL.md` 示例，以及 Qoder 桌面端的导入、选择和验证步骤。示例仅写入课件，没有安装技能或修改课程根目录的 `AGENTS.md`。

参考资料：

- [Qoder 任务执行原理](https://docs.qoder.cn/cli/how-it-works)
- [Qoder CLI 的 AGENTS.md 与静态记忆](https://docs.qoder.cn/cli/memory)
- [Qoder 桌面端技能指南](https://docs.qoder.cn/qoder/skills)
- [Agent Skills 文件格式规范](https://agentskills.io/specification)

## VS Code 界面图解

课件增加四页图解：界面分区、Notebook 内核选择、暂存与提交、左右差异对照。采用 VS Code 官方文档的五张截图，配合中文解读与平均值版本管理练习。

图片保存在 `latex/figures/`，原始链接与展示方式见[图片来源说明](latex/figures/SOURCES.md)。截图中的项目与版本仅作示例，课堂需核对自己的项目路径及 `.venv` 环境。
