s1 = set()
d1 = {} # 字典
print(type(s1), type(d1)) # <class 'set'> <class 'dict'>

# 定义非空集合
name = {'张三', '李四', '王五', 18, 18, 67, True, (12, 3, 21, 22)}
print(name)
print(len(name))

# 集合中不能存储可变类型
# s2 = {{1,2,3},{1,2,3}} # 不可以

s2 = set()
s2.add('张三')
s2.add('李四')
print(s2) # {'张三', '李四'}
# s2.pop() # pop 随机删除一个
s2.remove('张三')
print(s2)
s2.clear()
print(s2) # set() 而不是{}, {}是字典

# 删除容器
del s2

s3 = {12,13,14,15}
s4 = {12,13,15,16, 17}
# s3差集
s3.difference_update(s4)
print(s3) # {14}
