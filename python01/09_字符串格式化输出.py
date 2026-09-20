# 定义三个变量，分别存储姓名、年龄、体重，要求格式化输出：姓名：xx，年龄：xx，体重：xxkg

name = "杨钦强"
year = 31
weight = 60.99

message1 = "我叫:" + name + ",今年：" + str(year) + ",体重：" + str(weight)
message2 = "我叫：%s，今年：%d，体重：%.4f"%(name, year, weight)
message3 = f"我叫：{name},今年：{year}，体重：{weight}"
print(message1)
print(message2)
print(message3)

