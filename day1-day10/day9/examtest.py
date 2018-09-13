li = ['alex', 'wusir', 'rain']
s1 = ''.join(li)
# print(s1)
s1 = '*'.join(li)
# print(s1)

# range 包头不包尾
# 1-2+3...
s = 0
for i in range(1, 100):
    if i % 2 == 0:
        s -= i
    else:
        s += i
print(s)

# for i in range(100, -1, -1):
#     print(i)

# 求出字符串的的奇数位并且是数字的个数
'''
content = input('>>>')
odd_num = 0
for i in range(0, len(content)):
    if i % 2 == 1 and content[i].isdigit():
        odd_num += 1
print(odd_num)
'''
# 根据输入的内容自动加法
# content = input('请输入内容:').strip()
# li = content.split('+')
# sum = 0
# # 直接遍历数组
# for i in li:
#     sum += int(i)
# print(sum)

# 根据大小放入不同的字典的数组
li = [11, 22, 33, 44, 55, 77, 88, 99]
dict = {}
for i in li:
    if i > 66:
        if 'k1' not in dict:
            dict['k1'] = []
        dict['k1'].append(i)
    else:
        if 'k2' not in dict:
            dict['k2'] = []
        dict['k2'].append(i)
print(dict)

# 别的方法 以下三行为固定
li = [11, 22, 33, 44, 55, 77, 88, 99]
dict = {}
for i in li:
    dict.setdefault('k1', [])
    dict.setdefault('k2', [])
    if i > 66:
        dict['k1'].append(i)
    else:
        dict['k2'].append(i)
print(dict)

# hr管理系统
user_list = [{
    'username': 'barry',
    'password': '1234'
}, {
    'username': 'alex',
    'password': 'asdf'
}]
board = ['张三', '李四', '王二']
while 1:
    username = input('请输入用户名:')
    if username.upper() == 'Q':
        break
    password = input('请输入密码:')
    for i in board:
        if i in username:
            username = username.replace(i, '*' * len(i))
    user_list.append({'username': username, 'password': password})
    print(user_list)
