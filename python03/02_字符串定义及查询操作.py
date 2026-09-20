# 定义空字符串
s1 = ''
s2 = ""
s3 = """"""

# 定义非空字符串
s6 = "你会的 okk"
print(len(s6))
print(s6.index("o")) #4
print(s6.index("okk")) #4
print(s6.index("k")) #5
print(s6.rindex("k")) #6
print(s6.count("o")) #1
print(s6.find("o4")) #-1
print(s6.replace("okk","可以的"))
print(s6.split(' ')) # ['你会的', 'okk'] 按照空格切割

str = "你TMD，TMD，TMD的啊"
print(str.replace("TMD", "***")) # 你***，***，***的啊
print(str.replace("TMD", "***", 2)) # 你***，***，TMD的啊

str1 = "苹果,香蕉,橘子,榴莲"
print(str1.split(",")) # ['苹果', '香蕉', '橘子', '榴莲']
l1 = str1.split(",")
print(l1)
print('-'.join(l1))

print(str1.startswith('苹'))
print(str1.endswith('莲'))

print(str1.encode()) # 二进制