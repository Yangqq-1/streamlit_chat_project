# 创建非空容器过程就是打包操作
str = '12321'
list = [12,232,323]
tuple = (12,232,323)
set = {12,232,323}
dict = {'a': 1, 'b': 2, 'c': 3}

# 从容器中把值一个个取出来赋值给对应的变量过程就是拆包
a, b, c, d, e = str
print(a, b, c, d, e)
a, b, c = dict
print(a, b, c, d, e)

items = {'a': 1, 'b': 2, 'c': 3}
print(items.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)]) 元组
for k,v in items.items(): # 拆包元组
    print(k, v)

# 快速交换 a,b
a = 10
b = 20
a,b = b,a # 默认打包成元组
print(a, b)

# max
print(max(str))
print(min(str))
print(max(dict)) # c 最大值对应的key
print(min(dict)) # a 最小值对应的key