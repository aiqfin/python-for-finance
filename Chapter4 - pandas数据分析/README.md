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

全章使用一份 `04_pandas.ipynb`，按课件12节顺序组织，可分多周学习，不需要切换文件。每次从头运行到当前学习位置；练习答案放在折叠单元格中。

| 单元 | 内容与 Notebook | 学生应完成的任务 |
|---|---|---|
| 一：表与索引 | 第1—5节 | 说明每行含义，选择、筛选、赋值、自动对齐，完成宽长表转换 |
| 二：分组与整理 | 第6—8节 | 区分 agg/transform/filter/apply，处理报价问题，解释连接前后行数 |
| 三：金融应用 | 第9—11节 | 检查报价覆盖与共同样本，计算收益率，理解时间差、下采样及文件读写 |
| 四：综合练习 | 第12节 | 整理成绩登记；选做三股风险统计，解释年化口径与样本范围 |

主线沿用茅台、五粮液和平安的教学合成行情，从3个日期扩充到6个日期；保留课件中的订单合并与成绩清洗案例，避免重复开展订单分组日报。风险统计选做部分使用同三只股票的250期合成价格。教材配套 `eod_data.csv` 在第11节预览，均无需联网下载。

Notebook 已保存代码运行输出，打开即可查看；重新运行会在 `outputs/` 写入 `demo_prices.csv`。需要的库为课程环境已有的 NumPy、pandas、IPython 和 Jupyter 内核。

每节采用“问题—代码—输出—练习”组织，参考答案放在折叠单元格。建议先让学生手算小表，再运行；合并前必须说清粒度、键和预期行数。每单元以独立完成任务为结束条件，不以讲完 API 为结束条件。

本章全部教学页面统一写在 `latex/chapter4.tex`，可直接在主文件中备课与编译。完整 PDF 包含全部单元，可按课堂进度分次讲授。

## 阅读来源

- Wes McKinney, *Python for Data Analysis*, 3rd ed.：[pandas基础](https://wesmckinney.com/book/pandas-basics)、[清洗](https://wesmckinney.com/book/data-cleaning)、[合并与变形](https://wesmckinney.com/book/data-wrangling)、[分组统计](https://wesmckinney.com/book/data-aggregation)。
- [pandas merge 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)：连接关系、validate 与 indicator 参数。

中文说明、教学数据与练习由本课程自行编写，参考上述主题组织而未转载书稿。代码使用课程本地 pandas 环境；不需要为此升级依赖。
