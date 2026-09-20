# Python 环境配置与包管理避坑指南

> **核心原则**：严禁全局裸奔安装第三方库，始终坚持"一个项目，一个虚拟环境"。

## 1. 虚拟环境基础操作

### 为什么必须用虚拟环境？
- **隔离依赖**：避免不同项目对同一个库的版本需求冲突（如项目A需要 Pandas 1.0，项目B需要 Pandas 2.0）。
- **保护系统**：macOS 系统自带 Python，全局乱装包可能导致系统工具崩溃。
- **便于部署**：可以生成精确的 `requirements.txt`，方便在服务器或其他电脑上复刻环境。

### 标准操作流程
    # 1. 进入项目文件夹
    cd my_project

    # 2. 创建虚拟环境（.venv 是文件夹名，可自定义）
    python3 -m venv .venv

    # 3. 激活虚拟环境
    source .venv/bin/activate

    # 4. 验证是否激活成功
    # 成功激活后，终端提示符前会出现 (.venv) 标识

### 退出虚拟环境
    deactivate
- **作用**：将终端的 Python 指向从虚拟环境切换回系统全局环境。
- **注意**：如果直接关闭终端窗口，虚拟环境会自动失效；若要在同一终端切换项目，必须手动执行 `deactivate`。

---

## 2. Pip 镜像源配置（加速下载）

在国内网络环境下，建议永久配置国内镜像源以提升下载速度。

### 推荐镜像源
- **阿里云（首选，华东地区速度快）**：`https://mirrors.aliyun.com/pypi/simple/`
- **中国电信（备用，极度稳定）**：`https://mirrors.ctyun.cn/pypi/simple/`

### 永久配置命令（推荐）
使用 `python3 -m pip` 是最规范的写法，能确保配置写入当前用户的配置文件（`~/.pip/pip.conf`），对所有 Python 版本生效。

    # 设置阿里云镜像源
    python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

    # 设置受信任主机
    python3 -m pip config set global.trusted-host mirrors.aliyun.com

### 临时使用（单次生效）
    pip install streamlit -i https://mirrors.aliyun.com/pypi/simple/

---

## 3. Pip 命令规范：pip vs pip3 vs python3 -m pip

### 核心区别
- **pip**：通用名称。在虚拟环境内指向环境内的 Python；在全局环境下可能指向 Python 2 或 Python 3，存在歧义。
- **pip3**：明确指向 Python 3。但在全局环境下，如果安装了多个 Python 3 版本（如 3.11 和 3.12），无法确定具体指向哪一个。
- **python3 -m pip（最推荐）**：**绝对精准**。明确调用当前终端 `python3` 命令对应的解释器来运行 pip 模块。

### 最佳实践速查表

| 场景 | 推荐命令写法 | 原因 |
| :--- | :--- | :--- |
| **虚拟环境内** | `pip install xxx` | 激活后 `pip` 已自动绑定当前环境，简洁且安全 |
| **全局环境** | `python3 -m pip install xxx` | 彻底避免多版本 Python 指向混乱，防止装错位置 |
| **查看已安装包** | `python3 -m pip list` | 确保列出的是目标 Python 环境下的包 |
| **导出依赖清单** | `python3 -m pip freeze > requirements.txt` | 确保导出的依赖与当前 Python 环境一致 |

---

## 4. 包的卸载与管理

### 卸载单个包
    # 确保先激活虚拟环境
    source .venv/bin/activate

    # 卸载指定包（-y 跳过确认提示）
    pip uninstall streamlit -y

### 批量卸载
    # 根据 requirements.txt 批量卸载
    pip uninstall -r requirements.txt -y

### 彻底清空虚拟环境
如果环境依赖混乱，最干净的做法是删除重建：

    # 1. 退出环境
    deactivate

    # 2. 删除虚拟环境文件夹
    rm -rf .venv

    # 3. 重新创建并激活
    python3 -m venv .venv
    source .venv/bin/activate

---

## 5. 常见疑问解答 (FAQ)

### Q1: 为什么 npm 有 -g 全局安装，pip 没有？
- **npm**：默认是局部安装（装到项目的 `node_modules`），加 `-g` 才是全局。
- **pip**：默认就是全局安装（装到系统的 `site-packages`）。Python 没有提供 `-g` 参数，因为它的默认行为就是全局的。要实现局部隔离，必须手动创建虚拟环境。

### Q2: 镜像源配置是只对 Python 3.11 生效吗？
- **不是**。镜像源配置是**用户级别**的（存储在 `~/.pip/pip.conf`）。
- 只要你是在当前用户下操作，本地安装的所有 Python 版本（3.9, 3.11, 3.12 等）都会自动读取这个配置，无需重复设置。

### Q3: 在虚拟环境里，写 `pip` 和 `pip3` 有区别吗？
- **没有区别**。激活虚拟环境后，`.venv/bin/` 目录下的 `pip` 和 `pip3` 是指向同一个文件的符号链接。
- 为了书写简洁，在虚拟环境内推荐直接写 `pip`；在全局环境推荐写 `python3 -m pip`。