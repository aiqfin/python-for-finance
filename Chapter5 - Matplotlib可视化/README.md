# 第5章：Matplotlib可视化

- [课件 PDF](latex/chapter5.pdf)
- [课件源码](latex/chapter5.tex)
- [已执行的教学 Notebook](notebooks/05_Visualization.ipynb)
- [数据文件](data/day.csv)与[来源、许可、字段口径](data/SOURCES.md)

## 备课说明

全章只导入一次 UCI Bike Sharing 的 `day.csv`。数据为 Capital Bikeshare 2011—2012 年的 731 天记录、16 列；每行是一天，租车量单位为次数，不是去重人数。数据已保存到本地，上课无需联网。

课堂开头先介绍数据与观察单位。讲到具体分析问题时，再解释所需字段；下表供备课时查看，不放进课件开场。

| 顺序 | 所需字段 | 回答的问题与图形 |
|---|---|---|
| 1 | `cnt` | 一天通常租多少次：直方图、分箱、密度 |
| 2 | `workingday` | 不同日类型的平均水平：柱状图；与直方图并排辨认 |
| 3 | `dteday` | 随时间如何变化：每日折线、月内日均值、线条参数 |
| 4 | `casual`, `registered` | 用户构成有何差别：多曲线、分组柱状图、填充面积 |
| 5 | `temp` | 温度与租车量如何关联：散点图 |
| 6 | `yr` | 两个年份是否呈现不同结构：分组颜色与点形 |
| 练习 | `hum`, `weathersit` | 将相同画图方法用于湿度、天气类别 |

后续的 `monthly`、`user_monthly`、`work_summary` 都从同一个 `bike` 汇总得到。没有另造成绩、饮品、气温或股票数据。金融应用放在章末作为方法迁移说明，不在主线中引入第二套数据。

课件保留“完整代码—实际结果”的相邻页面和参数对照；全部教学页面直接位于 `latex/chapter5.tex`。Notebook 有对应代码、保存的图形输出、数值核对与折叠练习答案。

## 运行与重新生成

在 VS Code 中选择课程根目录 `.venv` 解释器，从头运行 Notebook。路径设置支持从本章 `notebooks/`、本章目录或课程根目录运行。

依赖为现有环境中的 NumPy、pandas、Matplotlib；无需安装新的数据下载包。Notebook 会根据本机字体选择中文字体，Windows 优先使用微软雅黑，macOS 优先使用苹方。

在课程根目录执行：

```powershell
.\.venv\Scripts\python.exe "Chapter5 - Matplotlib可视化/scripts/build_figures.py"
```

脚本执行 Notebook 中的代码，核对对应课件页的代码一致性，生成 17 张 `latex/figures/bike/` 插图，并导出 `outputs/bike_report.png` 与 `outputs/bike_report.pdf`。它不会改写 Notebook。修改教学代码后，应同步修改 Notebook 与课件中的对应代码，再运行此命令。

进入本章 `latex/` 编译；参考文献改变时需要 BibTeX：

```powershell
xelatex -interaction=nonstopmode -halt-on-error chapter5.tex
bibtex chapter5
xelatex -interaction=nonstopmode -halt-on-error chapter5.tex
xelatex -interaction=nonstopmode -halt-on-error chapter5.tex
```

## 数据与解释口径

- 日表经核对无缺失、无重复日期；日期连续，`casual + registered == cnt`。
- 直方图的纵轴是天数；工作日柱状图的纵轴是平均租车量（次/日）。两种柱子的含义不同。
- 工作日与非工作日分别为 500、231 天；均值比较配合各组样本量，不把样本期总量当成典型日水平。
- 月均线有 24 个点，表示月内日均值，不是月度总租车次数。
- 来源对温度还原、季节编码的说明有差异；本章保留标准化 `temp`、不标成摄氏度，不解码 `season`。
- 本章只描述这两年的历史样本。散点图、分组差异不直接支持因果判断。

原数据作者 Hadi Fanaee-T；UCI 标明 CC BY 4.0。完整署名与原始说明见 `data/SOURCES.md`、`data/UCI_Readme.txt`。中文讲解、图形与练习由本课程编写。
