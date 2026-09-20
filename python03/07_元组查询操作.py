# 定义元组
info = (('as', 'asd'), (123,23,23),45)

print(len(info))
print(info[1].count(23))
# print(info)
# print(info)
ages = info[1]
print(ages.index(23))

# 元组遍历
tup = (12,21,2132,23,233,3)
for index in tup:
    print(index)

index = 0
while index < len(tup):
    print(tup[index])
    index += 1