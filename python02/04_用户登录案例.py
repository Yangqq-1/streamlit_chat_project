name = 'admin'
pwd = 123

get_name = input('please input your name:')
get_pwd = int(input('please input your password:'))

if get_name == name and get_pwd == pwd:
    print("信息正确，即将跳转！")
else:
    print("用户名或密码错误！")