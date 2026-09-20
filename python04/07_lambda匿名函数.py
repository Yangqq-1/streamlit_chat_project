# 依次编写四个功能函数，加减乘除
# 原始
def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
print(jia(1, 2))
print(jian(1, 2))
print(cheng(1, 2))
print(chu(1, 2))
print('-----------')
f1 = lambda a, b: a + b
print(f1(1,2))
f2 = lambda a, b: a - b
print(f2(1,2))
f3 = lambda a, b: a * b
print(f3(1,2))
f4 = lambda a, b: a / b
print(f4(1,2))
print('-----------')
print((lambda a, b: a + b)(1, 2))
print((lambda a, b: a - b)(1, 2))
print((lambda a, b: a * b)(1, 2))
print((lambda a, b: a / b)(1, 2))

