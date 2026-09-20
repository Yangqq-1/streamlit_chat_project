"""
类型转换常用格式
str() 任意类型都能转换为字符串
int() 浮点类型转换成整数会丢失精度，字符串转换的时候必须是整数字符串（123）才能转换，浮点数即带小数点的数字字符串转换成整数会报错
float() 整数转浮点会加.0, 字符串必须纯数字才可以转
"""

x = 10.1223

print(int(x), type(int(x)))
print(str(x), type(str(x)))
print(float(x), type(float(x)))
print("===============================>")

# 字符串和浮点数转换成整数
# print(type(int("你好"))) # 报错
print(type(int("123")))
print(type(int(3.23)))
print(int(3.23))
# print(int('3.23'))
print("===============================>")

# 3.字符串和整数转换成浮点数
# print(type(float("你好"))) 报错，因为不是纯数字
print(float("123"), type(float("123"))) #123.0
print(float("123.2"), type(float("123.2")))
print(float(123), type(float(123)))#123.0

