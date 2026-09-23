# 第4章：pandas数据分析

- [课件 PDF](latex/chapter4.pdf)
- [课件源码](latex/chapter4.tex)
- [教学 Notebook](notebooks/04_pandas.ipynb)

在 VS Code 打开 Notebook，选择课程根目录 `.venv` 解释器，按顺序运行。
路径设置支持从本章 `notebooks/`、本章目录或课程根目录运行；Windows与macOS共用Python路径代码。

输入数据位于 `data/`：

- `eod_data.csv`：教材配套示例数据。

运行生成的文件放在 `outputs/`；供课件引用的插图放在 `latex/figures/`。所需目录按实际内容创建。

编译课件时进入本章 `latex/`，运行两次 `xelatex -interaction=nonstopmode -halt-on-error chapter4.tex`。

## 多周教学安排

本章按四个教学单元组织，不要求一周讲完。每单元可用一周；若每周课时少，可把讲解、上机和讲评拆开。

| 单元 | 内容与 Notebook | 学生应完成的任务 |
|---|---|---|
| 一：表与索引 | [04_pandas 第1—5节](notebooks/04_pandas.ipynb) | 说明每行含义，选择、筛选、赋值，解释标签对齐 |
| 二：清洗 | [04_2_Cleaning](notebooks/04_2_Cleaning.ipynb) | 保留原始记录，处理类型、重复、缺失和异常，给出清洗记录 |
| 三：合并与变形 | [04_3_Wrangling](notebooks/04_3_Wrangling.ipynb) | 解释连接前后行数、识别未匹配项，完成长宽表转换 |
| 四：分组与应用 | [04_4_GroupBy](notebooks/04_4_GroupBy.ipynb)，再回到 04_pandas 第6—9节 | 区分 size/count、agg/transform、简单与加权平均，完成订单报表和金融迁移 |

新增三个 Notebook 均可在独立内核中从头运行，不依赖前一单元的文件或变量。返回主 Notebook 时从头运行恢复状态。全部新增小数据为课程自编合成数据，不需联网下载。原有 eod_data.csv 保留。

每节采用“问题—代码—输出—练习”组织，参考答案放在折叠单元格。建议先让学生手算小表，再运行；合并前必须说清粒度、键和预期行数。每单元以独立完成任务为结束条件，不以讲完 API 为结束条件。

课件入口仍为 `latex/chapter4.tex`，扩充页面放在 `latex/supplements/`。完整 PDF 包含全部单元，可按课堂进度分次讲授。

## 阅读来源

- Wes McKinney, *Python for Data Analysis*, 3rd ed.：[pandas基础](https://wesmckinney.com/book/pandas-basics)、[清洗](https://wesmckinney.com/book/data-cleaning)、[合并与变形](https://wesmckinney.com/book/data-wrangling)、[分组统计](https://wesmckinney.com/book/data-aggregation)。
- [pandas merge 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)：连接关系、validate 与 indicator 参数。

新增中文说明、数据与练习由本课程自行编写，参考上述主题组织而未转载书稿。新增代码面向课程本地 pandas 2.x 环境；不要为了使用在线文档默认展示的新版本接口而升级课程环境。
