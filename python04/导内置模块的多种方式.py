# import throttle_1
# print(throttle_1.show())
# from throttle_1 import show
# print(show())

# 导入包中的模块
# import __init__.m1 as m1
# print(m1.show_m1())

from __init__ import m1
print(m1.show_m1())

from __init__ import m2
print(m2.show_m2())