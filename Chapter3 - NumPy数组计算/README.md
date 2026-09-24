# 第3章：NumPy数组计算

- [课件 PDF](latex/chapter3.pdf)
- [课件源码](latex/chapter3.tex)
- [教学 Notebook](notebooks/03_NumPy.ipynb)

在 VS Code 打开 Notebook，选择课程根目录 `.venv` 解释器，按顺序运行。

本章在代码中生成示例数据，无需额外输入文件。

运行生成的文件放在 `outputs/`；供课件引用的插图放在 `latex/figures/`。所需目录按实际内容创建。

编译课件时进入本章 `latex/`，运行两次 `xelatex -interaction=nonstopmode -halt-on-error chapter3.tex`。

## 扩充教学内容

成绩矩阵、axis、切片视图与复制、广播和左右随机走动。新增内容嵌入原有知识点之前或之后，保留原金融案例。先用生活小例子解释概念，再迁移到金融。

新增代码中的数据均为课程自编合成数据。Notebook 含练习及折叠参考答案。本章全部教学页面统一写在 `latex/chapter3.tex`，可直接在主文件中备课与编译。

阅读参考：Wes McKinney, *Python for Data Analysis*, 3rd ed.，https://wesmckinney.com/book/。新增中文说明和练习为本课程自行编写，未转载书稿；使用原书配套代码时应保留其 MIT 许可声明。
