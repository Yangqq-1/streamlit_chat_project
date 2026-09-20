# c传统必须手动关闭文件对象，with open方式会自动关闭
with open('test.txt', 'w') as f:
    f.write('hello world')