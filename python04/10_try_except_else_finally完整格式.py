try:
    print(1 / 1)
except Exception as e:
    print(e)
else:
    print('没有异常执行的代码')
finally:
    print('最终都会执行')