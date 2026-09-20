# 读取本地test文件，展示到控制台
f = open('test.txt', 'rb')
print(f.read())
# data = f.readline()
# print(data)
# data = f.readlines()
# print(data)
# 之前读过的，后面就读不到了，read会读光所有，再调用readline，readlines就没有了