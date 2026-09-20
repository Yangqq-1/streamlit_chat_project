# 文件打开
f = open('test.txt', 'a')
# 文件写入
# f.write('hello world')
list = ['as', 'sad', 'dasd']
for item in list:
    f.write(item + '\n')
f.close()
# f.read()