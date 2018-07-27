user = '1'
pwd = '2'
i = 0
while i < 3:
    name = input('请输入姓名:')
    password = input('请输入密码:')
    if name == user and password == pwd:
        print('success')
        break
    else:
        print('failed,you have %d times' % (2 - i))
        if 2 - i == 0:
            result = input('do you want more?Y?')
            if result == 'Y':
                i = 0
                continue
    i += 1
else:
    print('last!!!!!!')
