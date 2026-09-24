# 第7章：数据输入输出

- [课件 PDF](latex/chapter7.pdf)
- [课件源码](latex/chapter7.tex)
- [教学 Notebook](notebooks/07_Input_Output.ipynb)

本章按“观察小表 → 制作同源文件 → 按格式学习操作 → 往返验证 → 读取计时 → 真实行情应用”组织，只介绍 CSV、Excel 和 Parquet。

在 VS Code 中选择课程根目录 `.venv` 解释器，按顺序运行 Notebook。路径支持从课程根目录、本章目录或本章 `notebooks/` 运行。依赖 numpy、pandas、openpyxl、pyarrow 与 Jupyter；绘图脚本另用 Pillow，不在课堂代码中自动安装。

### 数据直接放在 data 中

```text
data/
├── eod_data.csv            教材原始数据，只读
├── quotes.csv             同一份虚拟行情，20,000 行 × 8 列
├── quotes.xlsx
├── quotes.parquet
└── quotes_by_market/      分区教学示例，不参与单文件计时
    ├── market=模拟市场甲/
    │   └── part-0.parquet
    └── market=模拟市场乙/
        └── part-0.parquet
```

小样本直接取前 6 行，不设额外目录。`quotes_by_market/` 保留目录层级是为了展示分区数据集：目录分区与单个文件内部的行组是两个不同概念。

所有格式示例均使用同一套 `quotes` 数据。Notebook 另将两工作表报告 `report.xlsx`、计时结果 `read_timings.csv` / `read_summary.csv` / `column_timings.csv`、真实行情计算结果 `spy_vol21.parquet` / `spy_vol21.xlsx` 直接保存到 `data/`，不另建输出目录。

### 课前制作数据与图片

Notebook 会生成实验数据，也可从课程根目录运行：

```powershell
.venv\Scripts\python.exe "Chapter7 - 数据输入输出/scripts/prepare_data.py"
.venv\Scripts\python.exe "Chapter7 - 数据输入输出/scripts/make_figures.py"
```

固定随机种子 7；代码保留前导零，市场名包含中文，评分包含缺失值。证券与行情均为模拟数据。脚本可用 `--rows 2000` 改规模；Notebook 使用自己的 `N_ROWS`。运行覆盖同名生成文件，原始 `eod_data.csv` 不修改。

图片放在 `latex/figures/`，同时嵌入课件和 Notebook：

- [三种文件内容预览](latex/figures/formats_preview.png)：文本和读取后的表格。
- [Parquet 文件内部结构](latex/figures/parquet_layout.png)：行组、列块、文件尾部元数据。
- [Parquet 分区目录](latex/figures/parquet_directory.png)：真实目录、文件名、行数、体积和模式。

这些是依据实际文件绘制的教学预览图，不是第三方软件截图。数据规模改变后重新运行绘图脚本；默认使用 Windows 微软雅黑，其他系统用 `--font` 指定中文字体。来源与重制说明见 [SOURCES.md](latex/figures/SOURCES.md)。

### 格式与实验重点

| 格式 | 本章重点 |
|---|---|
| CSV | 编码、代码与日期类型、缺失值、`usecols`、`chunksize` |
| Excel | `sheet_name`、共享 `ExcelWriter` 写多表、避免覆盖 |
| Parquet | 类型、压缩、`columns`、`filters`、文件内部结构与目录分区 |

先检查行列、类型、缺失值与数值一致性，再预读并进行 5 轮随机顺序计时。只计读取到 DataFrame 的耗时，输出中位数、最小值、最大值与文件 KiB；另比较 CSV 选两列、Parquet 选两列及 Parquet 全表后切列。

CSV 不压缩，Excel 使用 xlsx 容器压缩，Parquet 使用 pyarrow + Snappy。这是有缓存条件下的常用配置比较，不是冷启动磁盘测试，不测峰值内存，不预设永久速度排名。分区示例另行验证，不混入速度表。

### 编译

进入本章 `latex/`，运行 `xelatex -interaction=nonstopmode -halt-on-error chapter7.tex`、`bibtex chapter7`，再运行两次 XeLaTeX。

说明参考 [pandas I/O 文档](https://pandas.pydata.org/docs/user_guide/io.html)、[Apache Parquet 文件结构](https://parquet.apache.org/docs/file-format/) 和 [Arrow Parquet 分区数据集](https://arrow.apache.org/docs/python/parquet.html#partitioned-datasets-multiple-files)。
