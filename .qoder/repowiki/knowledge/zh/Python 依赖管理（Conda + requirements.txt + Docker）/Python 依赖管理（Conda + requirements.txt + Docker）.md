---
kind: dependency_management
name: Python 依赖管理（Conda + requirements.txt + Docker）
category: dependency_management
scope:
    - '**'
source_files:
    - py4fi2nd-master/py4fi2nd.yml
    - pandas_exercises-master/requirements.txt
    - py4fi2nd-master/code/ch02/Docker/Dockerfile
    - py4fi2nd-master/code/ch02/Docker/install.sh
    - py4fi2nd-master/.gitignore
---

本仓库为《Python金融数据分析》课程资源集合，包含多个独立的 Python 项目片段。依赖管理采用多种工具并存的方式，未形成统一的跨项目规范：

1. **Conda 环境配置**：`py4fi2nd-master/py4fi2nd.yml` 使用 Conda 环境文件声明 Python 3.12 及 numpy==1.26.4、pandas、matplotlib、scikit-learn、statsmodels、tensorflow、numba、cython、sympy 等科学计算库，并指定 prefix 路径。

2. **pip requirements.txt**：`pandas_exercises-master/requirements.txt` 固定了较老版本的依赖（numpy==1.13.1、pandas==0.23.4、matplotlib==2.0.2、seaborn==0.8.1），与 py4fi2nd.yml 中的版本差异较大。

3. **Docker 容器化安装**：`py4fi2nd-master/code/ch02/Docker/Dockerfile` 基于 Ubuntu 镜像，通过 `install.sh` 脚本安装 Miniconda 并 conda install pandas、ipython；cloud 目录下的 `setup.sh` 用于在 DigitalOcean Droplet 上部署 Jupyter Notebook。

4. **无统一包管理器**：仓库中未发现 `requirements.in`、`poetry.lock`、`Pipfile.lock`、`go.mod`、`package.json` 等现代锁定文件；各子项目各自维护依赖清单，版本约束不一致。

5. **虚拟环境隔离**：根目录存在 `.venv` 目录且 `.gitignore` 忽略 `venv/`、`.venv`、`env/` 等虚拟环境目录，表明开发时使用 Python 内置 venv 或第三方虚拟环境工具进行隔离。

6. **代码内直接 import**：所有 .py 和 .ipynb 文件通过标准 import 语句引入第三方库（如 numpy、pandas、scipy、matplotlib、zmq、tensorflow），未见 vendoring 或私有 PyPI 源配置。

由于仓库由多个来源不同的示例代码拼合而成，缺乏统一的依赖声明与版本锁定机制，不同章节/练习集的依赖版本存在显著差异，更新与维护需分别处理各子项目的依赖文件。