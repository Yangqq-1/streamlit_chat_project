import random
# f = open('.python.txt', 'r')

# f = open('venv_configuration.py', 'r', encoding='utf-8')

# 打开项目工程路径下的 python.txt，逐行读取并打印
# f = open("python.txt", "r", encoding="utf-8")

# for line in f:
#     print(line, end='')      # line 自带换行符，用 end="" 避免多打一个空行
#
# f.close()

# 请编写一个函数 print_info，接受以下参数：
#
# name：表示一个人的姓名（必须）
# age：表示一个人的年龄（必须）
# city：表示一个人所在的城市（可选，默认值为 "未知"）
# gender：表示一个人的性别（可选，默认值为 "未知"）
# 函数内部根据提供的参数打印人物信息，输出格式如下：
# 姓名：xxx
# 年龄：xxx
# 城市：xxx
# 性别：xxx

# def print_info(name, age, city = "未知", gender = "未知"):
#     print(f"姓名：{name}\n年龄：{age}\n城市：{city}\n性别：{gender}\n")
#
# print_info('yqq', 12)
# =================
# 写一个 lambda 表达式，用于将字符串列表中的字符串都转换为大写
# def transform_func(list):
#     temp_list = []
#     for item in list:
#         str = item.upper()
#         temp_list.append(str)
#     return temp_list
# func = lambda lst: transform_func(lst)
# print(func(['asda', 's']))
#
# def transform_func(str):
#     return str.upper()
# func = lambda str: str.upper()
# temp_list = []
# for item in ['asd', 's']:
#     temp_list.append(func(item))
# print(temp_list)



# ===========================
# 请编写一个程序，接受用户输入一个整数，并进行相应的处理。
#
# 首先，程序需要提示用户输入一个整数。
# 然后，程序尝试将用户输入的内容转换为整数类型，并计算它的平方。
# 如果用户输入的内容无法转换为整数类型，程序将捕获异常，并输出错误信息："输入无效，请输入一个有效的整数！"。
# 否则，在else逻辑块中将程序输出计算得到的平方结果。
# def get_int_num():
#     try:
#         num = input("请输入一个整数：")
#         int_num = int(num)
#     except Exception as e:
#         print('输入无效，请输入一个有效的整数！', e)
#         get_int_num()
#     else:
#         print(int_num ** 2)
# get_int_num()
# ===========================

# 我们需要统计一个源文本文件中每个单词出现的次数，并将结果写入另一个目标文件。
# 源文件input.txt内容如下：
# As your report on White Pollution indicates, regulations on the use of plastic bags have not been implemented effectively in some areas.
# I am writing this letter to express my concern over the abuse of plastic bags and make some suggestions.

# f_in = open('book.txt', 'r', encoding='utf-8')
# data = f_in.read()
# dict = {}
# for word in data.split():
#     if word == ' ' or word == '\n' or word == '.' or word == ',':
#         continue
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
# f_out = open('output.txt', 'w', encoding='utf-8')
# for k,v in dict.items():
#     f_out.write(f"{k}: {v}\n")
# f_in.close()
# f_out.close()

# ==========================
# 定义函数findall，要求返回符合要求的所有位置的起始下标，
# 如字符串"helloworldhellopythonhelloc++hellojava"需要找出里面所有的"hello"的位置，
# 返回的格式是一个元组，即：(0,10,21,29)
# def find_all(str, key):
#     index_list = []
#     current_index = -1
#     while True:
#         index = str.find(key, current_index + 1) # 不能算当次索引，下一次从+1开始
#         if index == -1:
#             break
#         current_index = index
#         index_list.append(index)
#     return tuple(index_list)
# val = find_all('helloworldhellopythonhelloc++hellojava', 'l')
# print(val)
# def find_all(str, key):
#     key_len = len(key)
#     original_str = len(str)
#     res = tuple()
#     for i in range(0, original_str):
#         if str[i:i + key_len] == key:
#             res += (i, ) #元组不能修改，所以追加下
#     return res
# val = find_all('helloworldhellopythonhelloc++hellojava', 'hello')
# print(val)

# ==============================

# 定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果。
# 示例：
# ​ 输入：列表[1,2,3]，字典{'a': 4,'b': 5, 'c': 6},定义一个函数fun，
# ​ 输出：21
# 解释：它们（1+2+3+4+5+6）的累积结果=21
# def fun(lst, dic):
#     sum = 0
#     try:
#         for i in lst:
#             sum += i
#         for v in dic.values():
#             sum += v
#     except Exception as e:
#         print(e)
#     return sum
# print(fun([1,2,3], {"a":1, "b":2, "c":3}))

# =======================================
# 定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
# 编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。
# def get_code():
#     str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     str_len = len(str1)
#     code = ''
#     i = 0
#     while i < 4:
#         random_index = random.randint(0, str_len - 1)
#         code += str1[random_index]
#         i += 1
#     return code
# print(get_code())

# =======================================
# 我们定义，在以下情况时，单词的大写用法是正确的：
# ​ 第一种情况：全部字母都是大写，比如 "USA" 。
# ​ 第二种情况：单词中所有字母都不是大写，比如 "leetcode" 。
# ​ 第三种情况：如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
#
# ​ 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
#
# ​ 示例 1：
# ​ 输入：word = "USA"
# ​ 输出：true
#
# ​ 示例 2：
# ​ 输入：word = "FlaG"
# ​ 输出：false
#
# ​ 提示：
# ​ 1 <= word.length <= 100
# ​ word由小写和大写英文字母组成
# def func(str):
#     if str.isupper():
#         return True
#     elif str.islower():
#         return True
#     elif not str.isupper() and str[0].isupper() and str[1:].islower():
#         return True
#     else:
#         return False
# print(func("JsssS"))




# ============================

# 给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。
# ​ 记录中只含下面三种字符：
#
# ​ 'A'：Absent，缺勤
# ​ 'L'：Late ， 迟到
# ​ 'P'：Present，到场
# ​ 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
#
# ​ 条件一：按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# ​ 条件二：学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
#
# ​ 如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。
#
# ​ 示例 1：
# ​ 输入：s = "PPALLP"
# ​ 输出：true
# ​ 解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。
#
# ​ 示例 2：
# ​ 输入：s = "PPALLL"
# ​ 输出：false
# ​ 解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。
#
# ​ 提示：
# ​ 1 <= s.length <= 1000
# ​ s[i] 为 'A'、'L' 或 'P'

# def func (str):
#     a_len = str.count('A')
#     l_len = str.count('LLL')
#     print(a_len, l_len)
#     # if a_len < 2 and l_len == 0:
#     #     return True
#     # else:
#     #     return False
#     return True if a_len < 2 and l_len == 0 else False
# print(func('APPALLALL'))

# =========================================================
# 将26个英文字母分为了三组。给你一个字符串数组word，判断字符串中的所有字母是否在同一组。只返回所有字母在同一组的字符串。
# ​ 请注意，字符串中的字母 不区分大小写，相同字母的大小写形式都被视为在同一组。
#
# ​ 26个英文字母分组如下：
# ​ 第一组由字符 "qwertyuiop" 组成。
# ​ 第二组由字符 "asdfghjkl" 组成。
# ​ 第三组由字符 "zxcvbnm" 组成。
#
# ​ 示例 1：
# ​ 输入：words = ["Hello","Alaska","Dad","Peace"]
# ​ 输出：["Alaska","Dad"]
# ​ 解释：由于不区分大小写，"a" 和 "A" 都在第二组。
#
# ​ 示例 2：
# ​ 输入：words = ["omk"]
# ​ 输出：[]
#
# ​ 示例 3：
# ​ 输入：words = ["adsdf","sfd"]
# ​ 输出：["adsdf","sfd"]
#
# ​ 提示：
# ​ 1 <= words.length <= 20
# ​ 1 <= words[i].length <= 100
# ​ words[i] 由英文字母（小写和大写字母）组成

# 如果一个单词的字母全在某个分组，返回True，调用方可以依此直接确认该单词符合要求
def is_all_in(ori_w, tar_w):
    is_in = []
    for tw in tar_w:
        if tw.lower() not in ori_w:
            is_in.append(False)
        is_in.append(True)
    # 如果有一个字母不在字符串里，那直接就不用考虑直接返回False，有一个False即代表不满足。
    # 也即全在某个分组的时候返回True，否则False
    return False if is_in.count(False) > 0 else True


def func(word):
    w1 = "qwertyuiop"
    w2 = "asdfghjkl"
    w3 = "zxcvbnm"
    w_arr = [w1, w2, w3]
    temp_arr = []
    for w in word:
        for ori_w in w_arr:
            # 如果True代表全在分组内，这个字符串符合要求
            if is_all_in(ori_w, w):
                if w not in temp_arr:
                    temp_arr.append(w)
    return temp_arr

print(func(["Hello","Alaska","Dad","Peace"]))











