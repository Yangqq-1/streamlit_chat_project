# 使用递归求1-5累加
def get_sum (next, sum):
    if next <= 5:
        sum += next
        next += 1
        return get_sum(next, sum)
    else:
        return sum


print(get_sum(1, 0))

# 递归求阶乘
def jc(n):
    if n == 1:
        return 1
    return n * jc(n - 1)
print(jc(10))