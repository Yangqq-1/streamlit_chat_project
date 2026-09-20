def show():
    return 'success'
if __name__ == '__main__':
    print(__name__)# 只有在当前文件运行才叫__main__，导包那里会打出对应的文件名/模块名
    show()