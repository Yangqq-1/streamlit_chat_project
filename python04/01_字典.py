# 定义空字典
d1 = {}
d2 = dict()
print(type(d1), type(d2)) # <class 'dict'> <class 'dict'>

# 非空字典
d3 = {"a": 1, "b": 2, "c": 3}
print(d3)

d4 = {'a': [1, 2, 3], '列表': [12, 23], (1, 2, 3): (123, 232, 23)} # 元组可以做为key
print(d4)

# 查询
print(d4[(1, 2, 3)]) # 奇葩 支持
print(d4.get('a'))

# 新增
d4[(1, 2)] = [12,233]
print(d4)

# 删除
d4.pop((1, 2))
print(d4)

# 获取所有key
d5 = d4.keys()
print(d5)
for key in d5:
    print(key)

print(len(d5))
print(d4.values())
print(d4.items()) # dict_items([('a', [1, 2, 3]), ('列表', [12, 23]), ((1, 2, 3), (123, 232, 23))])
