# list = [1,2,3,4,5,6,7,8,9,10]
# list.insert(1, 111) # 插到第一个索引位置
# print(list)

# list.append(100) # 插到最后面，一次只能插一个
# print(list)

# list.extend([9,8,7,6,5,4,3,2,1]) # 插到最后面，一次插多个
# print(list)

# list.pop(2) # 根据索引删除
# print(list)

# list.remove(2) # 删除指定元素，一次只能删除一个，从左到右
# print(list)

# list.clear() # 清空列表
# print(list)

# 列表的遍历
name = ["张三", "李四", "王五", "李六"]

for i in name:
    print(i)

index = 0
while index < len(name):
    print(name[index])
    index += 1
