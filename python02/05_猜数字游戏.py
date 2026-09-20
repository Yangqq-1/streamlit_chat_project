import random
# random生成随机数，注意：[x, y] 左闭右必
num = random.randint(1, 10)
get_num = int(input("请输入一个数字："))
if 1 <= get_num <= 10:
    if get_num > num:
        print("猜大了")
    elif get_num < num:
        print("猜小了")
    else:
        print("猜对了")
else:
    print("只能猜1-10")