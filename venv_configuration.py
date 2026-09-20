# 注意：在虚拟环境中，写 pip 和 pip3 其实完全等价

# 创建虚拟环境并安装依赖
    # 进入项目目录
    # cd my_streamlit_app

    # 创建虚拟环境
    # python3 -m venv .venv

    # 激活虚拟环境
    # source .venv/bin/activate

    # 然后才安装依赖
    # pip install streamlit

    # 退出虚拟环境
    # deactivate

# 卸载虚拟环境中的包
    # 激活虚拟环境（已激活忽略）
    # source .venv/bin/activate

    # 卸载指定包（-y 参数可以跳过确认提示，直接卸载）
    # pip uninstall streamlit -y

    # 批量卸载多个包
    # pip uninstall streamlit pandas numpy -y

    # 如果你之前导出过依赖清单（requirements.txt）可以直接根据这个文件批量卸载里面列出的所有包
    # pip uninstall -r requirements.txt -y

# 清空整个虚拟环境
    # 1. 先退出当前虚拟环境
    # deactivate

    # 2. 直接删除虚拟环境文件夹
    # rm -rf .venv

    # 3. 重新创建一个干净的虚拟环境
    # python3 -m venv .venv

    # 4. 重新激活
    # source .venv/bin/activate

