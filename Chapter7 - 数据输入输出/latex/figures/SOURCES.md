# 第7章图片来源

图片均由本项目 `scripts/make_figures.py` 从 `scripts/prepare_data.py` 生成的虚拟行情文件绘制，无第三方软件截图或外部图片素材。配色沿用课程蓝色；界面是教学预览，不冒充实际软件窗口。

| 图片 | 实际数据来源 | 表达边界 |
|---|---|---|
| `formats_preview.png` | `data/quotes.csv`、`quotes.xlsx`、`quotes.parquet` | 三种预览均展示相同前 3 行、全部 8 列及相同列顺序；表格中的缺失值以文字标出 |
| `parquet_layout.png` | `pyarrow.parquet.ParquetFile(...).metadata` | 行组行数、列名和压缩来自文件；方块不按字节比例绘制，未展开页和文件头尾标记 |
| `parquet_directory.png` | `data/quotes_by_market/` 的目录与文件元数据 | 行数、体积、类型来自文件；仅展示教学数据集，不是所有 Parquet 数据必须遵循的目录布局 |

默认图对应 20,000 行 × 8 列、每行组最多 5,000 行、Snappy 压缩。分区文件不重复存储 `market`，读取 Hive 风格数据集时由目录名恢复。

技术说明核对自官方资料（2026-09-24）：

- [Apache Parquet 文件结构](https://parquet.apache.org/docs/file-format/)
- [Apache Arrow：读取与写入 Parquet](https://arrow.apache.org/docs/python/parquet.html)

重制：使用本地 `.venv`，先运行本章 `scripts/prepare_data.py`，再运行 `scripts/make_figures.py`。非 Windows 系统传入 `--font /path/to/chinese-font.ttf`；需要 Pillow 和中文字体。修改数据规模后重新制作图片，以对应新数据。
