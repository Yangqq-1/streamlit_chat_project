# 定义元组
t1 = ()
t2 = tuple()
print(type(t1), type(t2)) # <class 'tuple'>
# d定义非空元组
t3 = ('hello', 'world', 123)

# 如果元组中只存储一个元素，必须加逗号
t4 = (234,)
t5 = (123) # <class 'int'>
print(type(t4),type(t5)) # <class 'tuple'> <class 'int'>

# 元组也可以嵌套
t5 = (t3, t4)

t6 = (10, 20, 30, [1, 2, 3])
# t6[0] = 11 # 元组不支持修改
# t6[-1] = [2, 3] # 元组不支持修改
t6[-1][0] = 10 # 支持修改 !!! 本质元组中存储的是地址
print(t6)
print(id(t6[-1]))
print(id(t6[-1][0]))
