username = input('请输入注册的用户名:')
password = input('请输入密码:')
with open('loginFile', mode="w", encoding="utf-8") as f:
    f.write('{}\n{}'.format(username, password))
print('恭喜注册成功')
i = 0
li = []
while i < 3:
    name = input('请输入用户名:').strip()
    pwd = input('请输入密码:').strip()
    with open('loginFile', mode="r+", encoding="utf-8") as f1:
        for line in f1:
            li.append(line.strip())
    if li[0] == name and li[1] == pwd:
        print('登录成功')
        break
    else:
        print('登录失败,请重试')
    i += 1
