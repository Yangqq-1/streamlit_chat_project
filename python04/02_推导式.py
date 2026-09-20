# 快速生成1-10列表

source = []

for i in range(1, 101):
    source.append(i)
# print(source)
# 列表推导式改写
list = [i for i in range(1, 101)]
print(list)

# 把1-100偶数提取出来
for i in range(1, 101):
    if i % 2 == 0:
        source.append(i)
list1 = [i for i in range(1, 101) if i % 2 == 0]
print(list1)

# 集合
a = set()
b = {i for i in range(1, 101) if i % 2 == 0}
print(b)

# 字典
# e = {i: i for i in range(1, 101) if i % 2 == 0}
e = {i: i*i for i in range(1, 101) if i % 2 == 0}
print(e)

# 特殊
nt = (i for i in range(1, 11))
print(nt, type(nt)) # <generator object <genexpr> at 0x1003a02b0> <class 'generator'> 得到一个生成器
# 通过tuple快速转成元组
print(tuple(nt))  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 字符串不行
# str = str(i for i in range(1, 10))
# print(str)