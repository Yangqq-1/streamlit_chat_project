# 求1-100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    if i == 100:
        print(f"1-100的和为{sum}")
    i += 1

print(f"1-100的和为{sum}")