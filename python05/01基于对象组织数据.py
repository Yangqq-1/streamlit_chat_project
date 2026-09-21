# 设计一个表（设计一个类class）
import platform
import subprocess


class Student:
    name = '1111'
    age = None
    addr = None

stu1 = Student()
stu2 = Student()
stu1.name = 'yqq'
stu1.hobby = 'sleep'
stu2.name = 'ymr'

# print(Student.name)
# print(stu1.name, stu1.hobby, stu1)
# print(stu2.name)

class Dog:
    name = None # 成员变量
    age = None # 成员变量

    def get_info(self): # 成员方法，self代表根据类生成的对象
        print(self.name, self.age, self)
dog1 = Dog()
dog1.name = 'yqq'
dog1.age = 12
# dog1.get_info()
# 函数在class外叫函数，在class内叫方法


# 设计类
class Clock:
    id = None
    price = None
    def ring(self):
        # import winsound
        # print(self.id)
        # winsound.Beep(1000, 1000)
        # print(self.price)

        system_name = platform.system()
        if system_name == 'Darwin': # Mac 系统
            print(self.id, system_name)
            subprocess.Popen(["osascript", "-e", "beep"])
            print(self.price)
# 基于类生成对象
clock = Clock()

# 由对象记录数据
clock.id = 1
clock.price = 12
# 由对象执行动作
clock.ring()
# ========================================
# 成员属性和类属性的设置
class NewDog(object):
    color = 'red'
    # 1.init 在创建类对象会自动调用
    # 2.在创建类对象的时候传入的参数，会自动传给init
    def __init__(self, name, age):
        # 设置成员属性
        self.name = name
        self.age = age
new_dog = NewDog('大黄', 12)
print(new_dog.name, new_dog.age) # 大黄 12
# 成员属性和类属性的修改
new_dog.age = 13
new_dog.name = 'yqq'
print(new_dog.name, new_dog.age) # yqq 13

# 修改公共类属性
NewDog.color = 'green'
print(new_dog.name, new_dog.age, new_dog.color) # yqq 13 green
print('='*20)
# 作业
# class NStu(object):
class NStu:
    school = '黑马'
    def __init__(self, name, age):
        self.name = name
        self.age = age
n_stu1 = NStu('yqq', 22)
n_stu2 = NStu('ymr', 21)
print(n_stu1.name, n_stu1.age, n_stu2.name, n_stu2.age, n_stu1.school, n_stu2.school)

NStu.school = '哈哈'
n_stu1.age = 30
n_stu2.age = 30
print(n_stu1.name, n_stu1.age, n_stu2.name, n_stu2.age, n_stu1.school, n_stu2.school)
