---
kind: build_system
name: 构建系统：基于Docker与Shell脚本的本地/云端环境搭建
category: build_system
scope:
    - '**'
source_files:
    - code/ch02/Docker/Dockerfile
    - code/ch02/Docker/install.sh
    - code/ch02/cloud/install.sh
    - code/ch02/cloud/setup.sh
---

该仓库为《Python for Finance》第二版的配套教学材料，不包含传统意义上的项目构建系统（如Makefile、tox、setup.py、pyproject.toml、CI流水线等）。其“构建”主要体现在通过Docker镜像和Shell脚本快速搭建一致的Python数据分析环境，用于课程演示与实验。

**使用的系统与工具**
- Docker：以Ubuntu为基础镜像，内嵌Miniconda3与常用Python库（pandas、ipython、matplotlib、scikit-learn、jupyter等），容器启动后直接进入IPython交互环境。
- Shell脚本：install.sh负责在Ubuntu中安装系统依赖、下载并静默安装Miniconda、创建conda环境并安装课程所需包；cloud/install.sh在此基础上额外配置Jupyter Notebook服务器及证书；cloud/setup.sh通过scp+ssh远程部署到DigitalOcean Droplet。

**关键文件与位置**
- code/ch02/Docker/Dockerfile：定义基础镜像，ADD install.sh并执行，设置PATH与CMD。
- code/ch02/Docker/install.sh：安装apt包、Miniconda、conda包（pandas、ipython）。
- code/ch02/cloud/install.sh：创建py4fi conda环境，安装jupyter、pytables、pandas、matplotlib、scikit-learn、openpyxl、pyyaml、cufflinks等，并启动Jupyter。
- code/ch02/cloud/setup.sh：将install.sh、证书、Jupyter配置复制到远程主机并执行安装。

**架构与约定**
- 分层设计：Docker镜像仅包含最小运行环境（Ubuntu + Miniconda + pandas + ipython），云端部署则扩展为完整的Jupyter服务环境。
- 幂等性：脚本使用apt-get update/upgrade、conda update确保依赖最新；删除临时安装包（rm Miniconda.sh）保持镜像精简。
- 路径约定：Miniconda安装在/root/miniconda3，Jupyter配置位于/root/.jupyter，notebook工作目录为/root/notebook。
- 环境变量：通过ENV PATH将miniconda3/bin加入PATH，使conda命令在容器/远程会话中可用。

**约束与规范**
- 无版本锁定：Dockerfile使用ubuntu:latest，Miniconda通过Miniconda3-latest-Linux-x86_64.sh动态获取最新版本，可能导致环境不一致。
- 无依赖清单：Python包直接通过conda install逐条安装，未使用requirements.txt或environment.yml集中管理。
- 无测试/发布流程：仓库仅为教学示例代码与笔记，不存在自动化测试、打包发布或CI/CD配置。
- 安全注意：cloud/install.sh以--allow-root启动Jupyter，且setup.sh通过root@${MASTER_IP}直连，适合教学而非生产环境。