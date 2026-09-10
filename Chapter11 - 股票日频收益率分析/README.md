# 第11章：股票日频收益率分析

本章是股票收益率数据分析的入门教学材料，包含 A 股市场构成、字段与样本口径、基础指标、描述性统计和图表解释。

- [课件 PDF](latex/chapter11.pdf)：35页，沿用课程上海大学 Beamer 主题。
- [教学 Notebook](notebooks/11_股票日频收益率分析.ipynb)：50个单元格，其中24个代码单元格，已使用课程 `.venv` 从头执行并保存输出。
- [课件源码](latex/chapter11.tex)：可继续修改；图表和统计宏由 Notebook 生成。
- [数据及分析核验](outputs/validation.md)：记录本次范围、检查与解释边界。

## 数据与文件结构

原始来源是本地 CSMAR 授权 ZIP（原包文件名保留），共7个 CSV、27个字段、6,888,585条记录，日期范围为2021-08-16至2026-08-13。原始包包含A股、B股与填充记录，不能直接当成全体A股交易日样本。使用范围以既有机构授权为准；本次未向外部服务上传数据。

```text
data/
  原始授权数据.zip                 # 原始文件保持不变，实际名称见目录
  raw/                            # Notebook从ZIP解压的7个CSV、字段说明和版权说明
  stock_daily.parquet              # 同一全量数据的压缩版本，供快速读取
notebooks/11_股票日频收益率分析.ipynb
outputs/
  analysis_summary.json           # 本次实际统计结果
  tables/                         # 筛选、板块、敏感性、收益率及相关性汇总
  validation.md
latex/
  chapter11.tex / chapter11.pdf
  analysis_numbers.tex            # Notebook生成的统计宏
  figures/                        # Notebook生成的7张图
  style/ / logo/                  # 本课程主题资源
```

原始 ZIP、`data/raw/` 和Parquet文件已配置 Git 忽略。课堂流程不依赖 HDF5、`tables` 或 `source_profile.json`。分块读取时只保留教学年份，避免同时载入全包；解压后的文件另需本地磁盘空间，具体大小由 Notebook 开头显示。

## 打开与运行

把原始 ZIP 放入本章 `data/`，在 VS Code 打开 Notebook，选择课程根目录 `.venv` 解释器，从头运行即可。支持以 Notebook 目录、本章目录或课程根目录为工作目录。

Notebook 第2节完整展示：

1. `ZipFile` 查看包内文件与解压大小。
2. `extract` 解压到 `data/raw/`；已有文件保留，不覆盖手工编辑。
3. `read_csv(nrows=5)` 试读，查看字段说明和类型。
4. `read_csv(chunksize=150_000)` 扫描每个CSV，统计全包覆盖并选取 `YEAR`。
5. 第2.4.1节直接将7个原始CSV分块合并为 `data/stock_daily.parquet`，不生成合并CSV；使用已纳入课程依赖的 `pyarrow`，已有Parquet保留并核对行数。
6. 第2.4.2节展示Parquet按年、按列快速读取。
7. `pd.concat` 合并年度记录，检查行数、重复键与价格关系，再接第3节分析。

每次从头运行都会重新读取CSV；无需事先在终端运行脚本。旧版HDF5转换脚本已移除，Notebook是本章唯一的教学运行入口。Python解压与读取代码在Windows和macOS上相同。

执行 Notebook（Windows，从课程根目录）：

```powershell
.\.venv\Scripts\python.exe -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 "Chapter11 - 股票日频收益率分析/notebooks/11_股票日频收益率分析.ipynb"
```

macOS将上述 Python 路径换为 `./.venv/bin/python`。本次执行验证在 Windows 完成；中文图形字体优先使用微软雅黑，macOS可使用苹方。

编译课件（两系统均先进入本章 `latex/`）：

```text
xelatex -interaction=nonstopmode -halt-on-error chapter11.tex
xelatex -interaction=nonstopmode -halt-on-error chapter11.tex
```

## 读取速度实测

[测试报告](outputs/read_performance.md)记录每轮耗时与复现代码。CSV完整读取中位数7.53秒，Parquet为0.53秒；2025年8列为5.32秒和0.13秒。Parquet首次完整读取曾耗时37.8秒，重复读取更快；测试未清空系统缓存。文件由1.65 GiB缩小到539 MiB。测速用的合并CSV已清理；原始ZIP和7个CSV保留用于原始数据核对。

## 教学口径与对应关系

| 内容 | Notebook | 课件PDF页码 |
|---|---|---|
| A股市场、原始ZIP、解压、读取与合并 | 1–2.5节 | 4–10 |
| 填充记录、筛选、质量检查、样本构成 | 2.6–3节 | 11–14 |
| 价格、收益口径、累计收益、对数收益 | 4–4.1节 | 15–20 |
| 波动率与回撤 | 4.2节 | 21–23 |
| 成交、市值、换手率与范围指标 | 5节 | 24–25 |
| 描述统计、分布、极值、板块比较 | 6节 | 26–30 |
| 股票层面汇总、相关性 | 7节 | 31–32 |
| 导出、核验与解释 | 8–9节 | 33–35 |

2025年主样本为5,500个代码、1,313,872条有成交股票日记录、243个日期。筛选依据 `Markettype`、`Filling`、成交股数、价格和收益可计算性；保留ST与极值。年末图的分母是2025-12-31当日有成交且收益可用的5,458个代码，并非官方上市公司总数。

示例股票代码 `000001`；相关性例子另含 `600000`、`600519`。252只用于近似年化，滚动窗口按有效观测计数。换手率由本包流通市值反推股数，市值先由千元转为元。

修改 `YEAR`、示例代码或筛选规则后，重新执行 Notebook，再核对课件中固定写出的日期、筛选数量与事件案例。宏和图会自动更新，案例文字不会自动改写。
