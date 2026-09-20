import random
# dishu = random.randint(1, 10)
# i = 0
# while i < 5:
#     get_num = int(input("请输入1-10数字:"))
#     if get_num < 1 or get_num > 10:
#         print("请输入1-10")
#     elif get_num > dishu:
#         print("猜大了")
#     elif get_num < dishu:
#         print("猜小了")
#     else:
#         print("猜对了")
#         # i = 5
#         break
#     i += 1

# 猜数字游戏，允许无限次但是统计猜对次数
dishu = random.randint(1, 100)
i = 0
while True:
    get_num = int(input("请输入1-100数字:"))
    if get_num < 1 or get_num > 100:
        print("请输入1-100")
        i += 1
    elif get_num > dishu:
        print("猜大了")
        i += 1
    elif get_num < dishu:
        print("猜小了")
        i += 1
    else:
        print("猜对了")
        i += 1
        print(f"总共猜了{i}次")
        break


