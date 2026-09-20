# 1. 先定义函数
def get_sum(a, b):
    return a + b

# 2. 再调用函数
print(get_sum(2, 3))

def say_hello():
    print('hello')
    return None # 如果没有主动返回数据，默认底层会自动补充

result = say_hello()
print(result) # None
print(type(result)) # <class "NoneType">
