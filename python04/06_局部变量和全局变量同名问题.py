def show():
    global a
    a = 100
    print(a)

a = 200
show()
print(a)

def show1(age, name):
    print(age, name)
show1(age = 22, name = 'A')
show1(22, name = 'A')
show1(22, 'A')