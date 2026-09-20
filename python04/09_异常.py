print('开始-------------')

try:
    a = int(input('请输入数字：'))
    print(1 / a)
# except (NameError, ZeroDivisionError) as e:
#     print(e)
except Exception as e:
    print(e)
print('结束-------------')