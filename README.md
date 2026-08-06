# Python 金融大数据分析 · 课程资源

本仓库为 **"Python金融大数据分析"** 课程的教学资源集合，基于 Yves Hilpisch 所著 *Python for Finance — Mastering Data-Driven Finance*（第2版，O'Reilly）编写。内容涵盖 Python 数据科学生态在金融领域的全流程应用，包括课件幻灯片、课堂 Jupyter Notebook 代码、练习题及参考答案。

## 课程内容

| 章节 | 主题 | 课件 | 课堂代码 |
|------|------|------|----------|
| 第1章 | 课程简介与引言 | `Chapter1 slides - 课程简介与引言/chapter1.pdf` | — |
| 第2章 | Python 基础语法 | `Chapter2 slides - Python基础语法/chapter2.pdf` | `02_Python_Basics.ipynb` |
| 第3章 | NumPy 数组计算 | `Chapter3 slides - NumPy数组计算/chapter3.pdf` | `03_NumPy.ipynb` |
| 第4章 | pandas 数据分析 | `Chapter4 slides - pandas数据分析/chapter4.pdf` | `04_pandas.ipynb` |
| 第5章 | Matplotlib 可视化 | `Chapter5 slides - Matplotlib可视化/chapter5.pdf` | `05_Visualization.ipynb` |
| 第6章 | 金融时间序列 | `Chapter6 slides - 金融时间序列/chapter6.pdf` | `06_Financial_Time_Series.ipynb` |
| 第7章 | 数据输入输出 | `Chapter7 slides - 数据输入输出/chapter7.pdf` | `07_Input_Output.ipynb` |
| 第8章 | 数学工具 | `Chapter8 slides - 数学工具/chapter8.pdf` | `08_Math_Tools.ipynb` |
| 第9章 | 模拟与期权定价 | `Chapter9 slides - 模拟与期权定价/chapter9.pdf` | `09_Monte_Carlo.ipynb` |
| 第10章 | 统计学与投资组合优化 | `Chapter10 slides - 统计学与投资组合优化/chapter10.pdf` | `10_Statistics_Portfolio_Optimization.ipynb` |

## 项目结构

```
.
├── Chapter1~10 slides */    # 各章节 LaTeX 幻灯片（含 PDF）
│   ├── chapterN.tex         #   主 TeX 源文件（xelatex + ctexbeamer 编译）
│   ├── chapterN.pdf         #   编译生成的课件 PDF
│   ├── figures/             #   插图资源
│   ├── logo/                #   校徽 / 主题 logo
│   ├── style/               #   Beamer 主题（shubeamer.sty）、宏包、参考文献样式
│   └── reference.bib        #   参考文献数据库
├── 章节课堂代码/             # 各章节 Jupyter Notebook 及示例数据
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
| 文件 I/O | tables (HDF5), openpyxl (Excel) |
| 交互环境 | jupyterlab, ipykernel |

### 启动 Jupyter Lab

```bash
# 激活虚拟环境（Windows PowerShell）
.\.venv\Scripts\Activate.ps1

# 启动 Jupyter Lab
jupyter lab
```

然后打开 `章节课堂代码/` 目录下的对应 `.ipynb` 文件即可开始学习。

## 课件编译

各章节幻灯片使用 XeLaTeX 编译，依赖 TeX Live 完整发行版。以第1章为例：

```bash
cd "Chapter1 slides - 课程简介与引言"
xelatex chapter1.tex
xelatex chapter1.tex   # 两次编译以生成目录
```

新建章节时，复制 `章节幻灯片模板/` 文件夹并修改 `chapterN.tex` 中的标题信息即可。详细说明见模板文件头部注释。

## 参考教材

- Hilpisch, Yves. *Python for Finance: Mastering Data-Driven Finance*. 2nd ed., O'Reilly Media, 2019.
- 中文译本：《Python金融大数据分析》（第2版），人民邮电出版社。
- 原书配套代码：见 `原书代码/` 目录或 [GitHub 官方仓库](https://github.com/yhilpisch/py4fi2nd)。

## 贡献者

- **主讲人**：王伟冠（上海大学经济学院金融系）

## 许可

本仓库的教学材料仅供课程学习使用。原书代码遵循原书仓库的 [LICENSE](原书代码/LICENSE.txt) 条款。
