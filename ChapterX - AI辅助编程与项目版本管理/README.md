# 工具篇：AI 辅助编程与项目版本管理

目录编号为 `ChapterX`，课件仍称“工具篇”。教学安排在第1章之后、第2章之前，第1—12章编号保持不变。环境配置、VS Code、AI 编程和 Git 内容从第1章迁入；第1章保留课程介绍与学习动机。

- [课件 PDF](latex/tools.pdf)
- [课件源码](latex/tools.tex)

## 学习顺序

1. 工具分工：VS Code、Python 与 uv、Qoder、Git。
2. 项目环境：创建 `.venv`、安装依赖、选择 Notebook 内核与重建环境。
3. AI 辅助编程：以 Qoder 为统一示例，说明目标、输入、约束和验收要求。
4. Git 版本管理：比较修改、暂存、提交、分支与远程协作。
5. 综合练习：将两期收益率程序扩展到多期，在分支中验证并保存版本。

本篇使用 Qoder CN 桌面端，同类工具可沿用相同的任务描述与验证流程。课件中的软件入口以实际版本为准。

## 课堂练习

在独立的 `py4fi-course` 练习目录操作，按课件从空目录建立项目。后续 NumPy、pandas 与可视化练习继续使用本篇的项目工作流程。

完成练习时保留两个可运行的 Git 版本，并能展示差异、运行命令和手算核对结果。两期价格 `[100, 110, 99]` 的累计收益率为 -1%；扩展后的三期价格 `[100, 110, 99, 108.9]` 的累计收益率为 8.9%。

## 编译

在本篇 `latex/` 目录运行两次：

```powershell
xelatex -interaction=nonstopmode -halt-on-error tools.tex
```

## Qoder 操作参考

- [Qoder CN 官方下载页](https://qoder.cn/download)
- [Qoder CN 官方快速入门](https://docs.qoder.cn/qoder/quickstart)

核对日期：2026-09-24。环境与 Git 的参考链接保留在对应课件页。

## VS Code 界面图解

课件增加四页图解：界面分区、Notebook 内核选择、暂存与提交、左右差异对照。采用 VS Code 官方文档的五张截图，配合中文解读与收益率练习说明。

图片保存在 `latex/figures/`，原始链接与展示方式见[图片来源说明](latex/figures/SOURCES.md)。截图中的项目与版本仅作示例，课堂需核对自己的项目路径及 `.venv` 环境。
