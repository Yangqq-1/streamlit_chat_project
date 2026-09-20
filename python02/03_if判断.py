# age = 19
# if age >= 18:
#     pass
#
# if age >= 18:
#   print("可以") # 二选一
    # print("可以")

age1 = int(input('请您输入年龄：'))
# if 18 <= age1 <= 65:
#     print("可以")
# elif age1 > 65:
#     print("牛逼")
# else:
#     print("回家写作业")

if 0 < age1 < 150:
    if 18 <= age1 <= 65:
        print("年轻人可以")
    elif age1 > 65:
        print("大爷牛逼")
    else:
        print("孩子回家写作业")
else:
    print("神经病啊，哪有这么大年龄的人")