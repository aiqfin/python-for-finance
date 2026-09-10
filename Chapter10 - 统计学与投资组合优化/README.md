# 第10章：统计学与投资组合优化

- [课件 PDF](latex/chapter10.pdf)
- [课件源码](latex/chapter10.tex)
- [教学 Notebook](notebooks/10_Statistics_Portfolio_Optimization.ipynb)

在 VS Code 打开 Notebook，选择课程根目录 `.venv` 解释器，按顺序运行。
路径设置支持从本章 `notebooks/`、本章目录或课程根目录运行；Windows与macOS共用Python路径代码。

输入数据位于 `data/`：

- `tr_eikon_eod_data.csv`：教材配套示例数据。

本章数据复制自 `原书代码/source/tr_eikon_eod_data.csv`，原书资料保留原样。

运行生成的文件放在 `outputs/`；供课件引用的插图放在 `latex/figures/`。所需目录按实际内容创建。

编译课件时进入本章 `latex/`，运行两次 `xelatex -interaction=nonstopmode -halt-on-error chapter10.tex`。
