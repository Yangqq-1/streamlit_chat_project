# Anaconda 使用指南（macOS Apple Silicon 版）

## 一、Anaconda 是什么？

**Anaconda 就是一个"Python 全家桶"。**

装完之后，电脑上就有了：
- **Python 本身**（不用单独去 python.org 下载）
- **Conda**（一个工具，帮你装包、管理虚拟环境，替代 pip + venv）
- **一大堆常用库**（NumPy、Pandas、Jupyter 等 180+ 个，开箱即用）

打个比方：
- 单独装 Python + pip = 买毛坯房，自己装修
- 装 Anaconda = 买精装房，拎包入住

---

## 二、安装

### 下载地址

推荐国内用户从清华镜像源下载（速度快，无需注册）：

    https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

### 版本选择

| 芯片类型 | 对应文件名 |
| :--- | :--- |
| **Apple Silicon（M1/M2/M3/M4）** | `Anaconda3-xxx-MacOSX-arm64.pkg` |
| Intel 芯片 | `Anaconda3-xxx-MacOSX-x86_64.pkg` |

### .pkg 和 .sh 的区别

| 对比项 | `.pkg` | `.sh` |
| :--- | :--- | :--- |
| 安装方式 | 图形界面，鼠标点击 | 终端命令行，键盘操作 |
| 上手难度 | 简单，适合新手 | 需要会用终端 |
| 安装结果 | 完全一样 | 完全一样 |
| 适用场景 | 日常 Mac 电脑 | 服务器 / 远程机器 / 无图形界面环境 |

两种方式安装出来的 Anaconda 完全一样，唯一区别是安装过程的交互方式不同。新手直接选 `.pkg` 双击安装即可。

### 安装步骤（.pkg）

1. 双击 `.pkg` 文件，点击 Continue
2. 阅读许可协议，点击 Agree
3. 选择安装位置（默认即可，通常安装到 `/opt/anaconda3` 或 `~/opt/anaconda3`）
4. 点击 Install，输入系统密码确认
5. 安装完成后点击 Close

### 验证安装

打开终端，执行：

    # 查看 conda 版本（能输出版本号就说明装好了）
    conda --version

    # 查看 Python 版本
    python --version

    # 查看已安装的包
    conda list

### 常见问题：conda 命令找不到

如果终端提示 `conda: command not found`，执行以下命令初始化：

    conda init zsh

然后**关闭并重新打开终端**即可。

---

## 三、安装后配置（推荐）

### 配置国内镜像源（加速 conda 包下载）

    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
    conda config --set show_channel_urls yes

---

## 四、日常使用

### 1. 创建虚拟环境（每个项目一个）

    # 创建一个叫 myenv 的环境，指定 Python 版本为 3.11
    conda create -n myenv python=3.11

    # 激活环境
    conda activate myenv

    # 用完退出
    conda deactivate

### 2. 在环境里装包

    # 激活环境后装包
    conda activate myenv
    conda install streamlit pandas numpy

    # 或者用 pip 也行（conda 环境里 pip 也能用）
    pip install some-package

### 3. 查看和管理环境

    # 查看所有环境
    conda env list

    # 查看当前环境装了哪些包
    conda list

    # 删除不用的环境
    conda env remove -n myenv

### 4. 跑项目

    conda activate myenv
    python app.py
    # 或者
    streamlit run app.py
### 5. 默认base关闭/打开

    conda config --set auto_activate false
    conda config --set auto_activate true

---

## 五、Conda vs Pip 怎么选？

| 场景 | 用什么 |
| :--- | :--- |
| 装科学计算类库（NumPy、Pandas 等） | `conda install` 优先，兼容性更好 |
| 装 conda 上没有的包 | 用 `pip install`，完全没问题 |
| 两者混用 | 可以，但建议一个环境里尽量统一用一种，避免冲突 |

---

## 六、命令对照表（venv + pip → conda）

| 以前用的（venv + pip） | Anaconda 里对应的 |
| :--- | :--- |
| `python3 -m venv .venv` | `conda create -n myenv python=3.11` |
| `source .venv/bin/activate` | `conda activate myenv` |
| `pip install xxx` | `conda install xxx`（或继续用 pip 也行） |
| `deactivate` | `conda deactivate` |
| `rm -rf .venv` | `conda env remove -n myenv` |

本质上做的事情一模一样，只是命令换了。Conda 把"创建虚拟环境"和"装包"两件事合到一个工具里了，不用再记 `python3 -m venv` 和 `pip` 两套命令。

---

## 七、Anaconda vs Miniconda

| 对比项 | Anaconda | Miniconda |
| :--- | :--- | :--- |
| 体积 | 约 3~5 GB | 约 400~500 MB |
| 预装包 | 180+ 科学计算库 | 仅 Conda + Python |
| 适合人群 | 新手、数据科学从业者 | 追求轻量、有明确需求的老手 |
| 安装后 | 开箱即用 | 需手动 conda install 安装所需包 |