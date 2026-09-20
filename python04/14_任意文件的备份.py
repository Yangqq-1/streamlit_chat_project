# 编写一个文件，对任意文件进行备份操作
import os

p = input("请输入路径：")
# todo异常情况
# try:
#     # 打开源文件
#     fin = open(p,'rb')
#     # 先创建备份文件
#     fout = open(f'[备份]{p}','wb')
# except Exception as e:
#     print(e, '操作失败')
# else:
#     # 读取源文件
#     data = fin.read()
#     # 写入源文件到备份文件中
#     fout.write(data)
#     fout.close()
#     fin.close()
if os.path.exists(p):
    with open (p, 'rb') as fin:
        with open(f'{p}【备份】','wb') as fout:
            data = fin.read()
            fout.write(data)
            print(f'{p}【备份】成功')
else:
    print("该备份文件压根不存在！")