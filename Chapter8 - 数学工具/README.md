# 第8章：SciPy 与金融数值计算

- [课件 PDF](latex/chapter8.pdf)
- [课件源码](latex/chapter8.tex)
- [教学 Notebook](notebooks/08_Math_Tools.ipynb)

在 VS Code 打开 Notebook，选择课程根目录 `.venv` 解释器，按顺序运行。

本章在代码中生成示例数据，无需额外输入文件。

运行生成的文件放在 `outputs/`；供课件引用的插图放在 `latex/figures/`。所需目录按实际内容创建。

编译课件时进入本章 `latex/`，运行两次 `xelatex -interaction=nonstopmode -halt-on-error chapter8.tex`。

## 教学顺序

概率分布与分位点 → 数值求根与债券收益率 → 拟合与插值 → 优化 → 积分 → 结果检查 → SymPy 选学。

章节编号与目录名保持不变；第9章讲模拟与期权定价，第10章深入统计检验与投资组合优化。

Notebook 含实际输出、图形和折叠练习答案。课件插图可用项目 Python 运行 `scripts/export_figures.py` 重新生成；日常运行 Notebook 不写出图片文件。
