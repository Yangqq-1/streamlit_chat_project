import time
# 书籍列表
book_list = [{'name': 'yqq', 'price': 12, 'status': False, 'id': 1789825104 }, {'name': '你好', 'price': 122, 'status': True, 'id': 1789825105 }]
# 公共方法；获取输入的数据
def get_info(type, title):
    try:
        return type(input(title))
    except Exception as e:
        print(e)
        # 输入错误后重新输入
        return get_info(type, title)

# 公共方法：获取所有的书籍id
def get_id_list():
    id_list = []
    for item in book_list:
        id_list.append(item['id'])
    return id_list

# 1、自定义函数 add_info()。
def add_info():
    try:
        name = get_info(str,'请输入书籍名称：')
        price = get_info(float,'请输入价格：')
        status = get_info(str,'是否出租（是/否）：')
    except Exception as e:
        print(e)
    else:
        data = {
            'name': name,
            'price': price,
            'status': True if status == '是' else False,
            'id':int(time.time())
        }
        book_list.append(data)
        print('添加成功!')

# add_info()
# print(book_list)

# 2、自定义函数 delete_info()。
# 功能: 根据编号删除书籍。让用户输入要删除的书籍的编号，并根据编号从存储图书信息的列表中，删除这本书。
def delete_info():
    try:
        id = int(input("请输入要删除的书籍编号："))
    except Exception as e:
        print(e)
        delete_info()
    else:
        # 判断书籍出租状态
        status = False
        for item in book_list:
            if item['id'] == id:
                status = item['status']
        if status == True:
            print("该书籍已出租！无法删除")
        else:
            id_list = get_id_list() # 获取所有id
            if id in id_list:
                for item in book_list:
                    if item['id'] == id:
                        book_list.remove(item)
                        print('删除成功！')
            else:
                print('该书籍信息不存在！')
                delete_info()
# delete_info()
# print(book_list)

# 3、自定义函数 update_info()。
# 功能: 修改书籍信息。让用户输入要修改的书籍的编号，再让用户选择要修改的字段，并输入修改的信息，然后根据编号从存储图书信息的列表中修改这本书的信息。
# 注意事项：
# 根据编号修改, 只能修改: 书籍名，价格，书籍出租状态.
def update_info():
    try:
        id = int(input("请输入要修改的书籍编号："))
    except Exception as e:
        print(e)
    else:
        # 获取所有书籍编号
        id_list = get_id_list() # 获取所有id
        if (id) in id_list:
            operate_type = input("请输入你要修改的类型，输入对应编号即可：\n1.书籍名\n2.价格\n3.书籍出租状态\n")
            if operate_type == '1':
                name = get_info(str, '请输入新的书籍名称：')
                for item in book_list:
                    if item['id'] == id:
                        item['name'] = name
            if operate_type == '2':
                price = get_info(float, '请输入新的价格：')
                for item in book_list:
                    if item['id'] == id:
                        item['price'] = price
            if operate_type == '3':
                status = get_info(str, '请输入是否出租（是/否）：')
                for item in book_list:
                    if item['id'] == id:
                        item['status'] = True if status == '是' else False
            print('修改成功')
        else:
            print('该书籍不存在，请重新输入！')
            update_info()

# update_info()
# print(book_list)

# 4、自定义函数 search_info()。
# 功能: 查询某个书籍信息.
# 注意事项: 根据书籍名查询，使用占位符格式化输出书籍信息
def search_info():
    try:
        name = input("请输入要查询的书籍名称：")
    except Exception as e:
        print(e)
    else:
        for item in book_list:
            if item['name'] == name:
                print("书籍名称：%s， 价格：%.2f， 是否出租：%s"%(item['name'], item['price'], '是' if item['status'] else '否'))

# search_info()
# print(book_list)

# 5、自定义函数 search_all()。
# 功能: 查询所有书籍的信息，并使用占位符格式化分别输出每一本书的书籍信息。
def search_all():
    if len(book_list) > 0:
        for item in book_list:
            print("书籍名称：%s， 价格：%.2f， 是否出租：%s" % (item['name'], item['price'], '是' if item['status'] else '否'))
    else:
        print("暂未录入书籍信息！")
# search_all()
# print(book_list)

# 6、定义函数 print_info() ，打印提示信息。
def print_info():
    try:
        num = int(input("""
        ①输入1: 添加书籍(书籍编号,  书籍名，书籍价格，书籍出租状态【是/否】).
        ②输入2: 删除书籍(根据编号删除）【删除时，需要判断书籍出租状态，如果书籍未出租，则删除书籍；如果书籍已出租，则打印“书籍已出租，暂无法删除”】)
        ③输入3: 修改书籍信息(只能改书籍名，书籍出租状态
        ④输入4：查询单个书籍信息(根据书籍名查)
        ⑤输入5: 查询所有书籍信息
        ⑥输入6: 退出系统
        """))
    except Exception as e:
        print(e)
    else:
        return num
# print_info()

# 7、打印提示界面, 让管理员登录账号和密码。
username = 'yqq'
password = '123'
def sign():
    # info = ['请输入用户名：', '请输入密码：']
    i = 0
    for i in range(3):
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        if name == username and pwd == password:
            print("登录成功！")
            break
        else:
            if i < 2:
                print("用户名或密码错误！请重试")
    else:
        print("错误次数达上限, 已退出系统！")
# sign()

# 8、读取文件“book.txt”。
def read_info():
    list = []
    f = open('book.txt', 'r')
    data = f.readlines()
    for item in data:
        lst = item.rstrip('\n').split(',')
        list.append({
            'name': str(lst[0]),
            'price': float(lst[1]),
            'status': True if int(lst[2]) else False,
        })
    f.close()
    return list
# print(read_info())

# 9、自定义while True循环逻辑， 实现用户录入什么选项, 就进行相应的操作
while True:
    try:
        num = print_info()
    except Exception as e:
        print(e)
    else:
        if num == 1:
            add_info()
            break
        elif num == 2:
            delete_info()
            break
        elif num == 3:
            update_info()
            break
        elif num == 4:
            search_info()
            break
        elif num == 5:
            search_all()
            break
        elif num == 6:
            break
        else:
            break

print(book_list)





