# Python 金融大数据分析 · 课程资源

本仓库为 **"Python金融大数据分析"** 课程的教学资源集合，基于 Yves Hilpisch 所著 *Python for Finance — Mastering Data-Driven Finance*（第2版，O'Reilly）编写。内容涵盖 Python 数据科学生态在金融领域的全流程应用，包括课件幻灯片、课堂 Jupyter Notebook 代码、练习题及参考答案。

## 课程内容

| 章节 | 主题 | 课件 | 课堂代码 |
|------|------|------|----------|
| 第1章 | 课程简介与引言 | `Chapter1 - 课程简介与引言/latex/chapter1.pdf` | — |
| 工具篇 | AI 辅助编程与项目版本管理 | `工具篇 - AI辅助编程与项目版本管理/latex/tools.pdf` | [学习入口](工具篇%20-%20AI辅助编程与项目版本管理/README.md) |
| 第2章 | Python 基础语法 | `Chapter2 - Python基础语法/latex/chapter2.pdf` | `Chapter2 - Python基础语法/notebooks/02_Python_Basics.ipynb` |
| 第3章 | NumPy 数组计算 | `Chapter3 - NumPy数组计算/latex/chapter3.pdf` | `Chapter3 - NumPy数组计算/notebooks/03_NumPy.ipynb` |
| 第4章 | pandas 数据分析 | `Chapter4 - pandas数据分析/latex/chapter4.pdf` | `Chapter4 - pandas数据分析/notebooks/04_pandas.ipynb` |
| 第5章 | Matplotlib 可视化 | `Chapter5 - Matplotlib可视化/latex/chapter5.pdf` | `Chapter5 - Matplotlib可视化/notebooks/05_Visualization.ipynb` |
| 第6章 | 金融时间序列 | `Chapter6 - 金融时间序列/latex/chapter6.pdf` | `Chapter6 - 金融时间序列/notebooks/06_Financial_Time_Series.ipynb` |
| 第7章 | 数据输入输出 | `Chapter7 - 数据输入输出/latex/chapter7.pdf` | `Chapter7 - 数据输入输出/notebooks/07_Input_Output.ipynb` |
| 第8章 | 数学工具 | `Chapter8 - 数学工具/latex/chapter8.pdf` | `Chapter8 - 数学工具/notebooks/08_Math_Tools.ipynb` |
| 第9章 | 模拟与期权定价 | `Chapter9 - 模拟与期权定价/latex/chapter9.pdf` | `Chapter9 - 模拟与期权定价/notebooks/09_Monte_Carlo.ipynb` |
| 第10章 | 统计学与投资组合优化 | `Chapter10 - 统计学与投资组合优化/latex/chapter10.pdf` | `Chapter10 - 统计学与投资组合优化/notebooks/10_Statistics_Portfolio_Optimization.ipynb` |
| 第11章 | 股票日频收益率分析 | `Chapter11 - 股票日频收益率分析/latex/chapter11.pdf` | `Chapter11 - 股票日频收益率分析/notebooks/11_股票日频收益率分析.ipynb` |

工具篇安排在第1章之后，集中讲授环境配置、VS Code、以 Qoder 为例的 AI 编程及 Git 工作流程；第2—12章编号保持不变。

## 前几章扩充与 pandas 多周教学

第2—5章新增基础概念说明、非金融短例子和课堂练习。pandas 作为重点，按“表与索引、数据清洗、合并与变形、分组与应用”四个单元推进，可分多周讲授。

第4章保留原主 Notebook，并增加三个可独立运行的补充 Notebook。具体顺序、学习目标与入口见 [pandas 教学安排](Chapter4%20-%20pandas数据分析/README.md)。新增小数据由课程自行编写，参考 [Python for Data Analysis 在线书](https://wesmckinney.com/book/) 的主题组织。

## 项目结构

```
.
├── ChapterN - 主题/         # 第1–11章统一命名
│   ├── README.md            #   本章入口与运行说明
│   ├── notebooks/           #   教学Notebook（有代码的章节）
│   │   └── *.ipynb
│   ├── data/                #   输入数据（按需）
│   ├── outputs/             #   运行生成的表格、文件（按需）
│   └── latex/               #   LaTeX 源码与构建资源
│       ├── chapterN.tex     #   主 TeX 源文件（xelatex + ctexbeamer 编译）
│       ├── chapterN.pdf     #   编译生成的课件 PDF
│       ├── figures/         #   插图资源
│       ├── logo/            #   校徽 / 主题 logo
│       ├── style/           #   Beamer 主题、宏包、参考文献样式
│       └── reference.bib    #   参考文献数据库
├── 章节幻灯片模板/            # 新建章节时使用的 LaTeX 模板
├── 练习题/                   # 课后练习（含解答）
│   ├── Excercise/           #   精选练习题（Chipotle、US Crime、Auto MPG 等）
│   └── pandas_exercises-master/  # pandas 官方练习集
├── 原书代码/                 # 原书配套代码（Yves Hilpisch 官方仓库）
│   └── code/                #   按章节组织的 Jupyter Notebook
├── pyproject.toml           # 项目元数据与 Python 依赖声明（uv 管理）
└── uv.lock                  # 依赖锁定文件
```

## 环境搭建

### 前置要求

- Python ≥ 3.11
- [uv](https://docs.astral.sh/uv/) 包管理器

### 一键安装

```bash
# 克隆仓库
git clone <repo-url>
cd "Lecture materials"

# 创建虚拟环境并安装所有依赖
uv sync
```

`uv sync` 将自动创建 `.venv` 虚拟环境，并安装以下核心依赖：

| 类别 | 包 |
|------|-----|
| 科学计算 | numpy, pandas, scipy |
| 可视化 | matplotlib, seaborn |
| 机器学习 / 符号计算 | scikit-learn, sympy |
| 金融数据 | pandas-datareader |
| 文件 I/O | tables (HDF5), openpyxl (Excel), pyarrow (Parquet) |
| 交互环境 | jupyterlab, ipykernel |

### 启动 Jupyter Lab

```bash
# 激活虚拟环境（Windows PowerShell）
.\.venv\Scripts\Activate.ps1

# 启动 Jupyter Lab
jupyter lab
```

然后进入对应章节的 `notebooks/` 目录并打开 `.ipynb` 文件即可开始学习。涉及文件读写的Notebook已统一设置 `DATA` 和 `OUTPUTS` 路径，支持从Notebook目录、本章目录或课程根目录运行。例如：

```bash
cd "Chapter4 - pandas数据分析/notebooks"
jupyter lab
```

## 课件编译

各章节幻灯片使用 XeLaTeX 编译，依赖 TeX Live 完整发行版。以第1章为例：

```bash
cd "Chapter1 - 课程简介与引言/latex"
xelatex chapter1.tex
xelatex chapter1.tex   # 两次编译以生成目录
```

新建章节时，建立 `ChapterN - 主题/latex/`，把 `章节幻灯片模板/` 的内容复制到其中，并修改 `chapterN.tex` 中的标题信息即可。详细说明见模板文件头部注释。

## 参考教材

- Hilpisch, Yves. *Python for Finance: Mastering Data-Driven Finance*. 2nd ed., O'Reilly Media, 2019.
- 中文译本：《Python金融大数据分析》（第2版），人民邮电出版社。
- 原书配套代码：见 `原书代码/` 目录或 [GitHub 官方仓库](https://github.com/yhilpisch/py4fi2nd)。

## 贡献者

- **主讲人**：王伟冠, 吕文俊（上海大学经济学院金融系）

## 许可

本仓库的教学材料仅供课程学习使用。原书代码遵循原书仓库的 [LICENSE](原书代码/LICENSE.txt) 条款。
