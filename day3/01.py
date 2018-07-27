# print(6 or 2 > 1)
# 1-99的奇偶和
i = 0
sum = 0
# 第一种
# while i < 101:
#     i += 1
#     if i == 88:
#         continue
#     else:
#         if i % 2 == 0:
#             sum -= i
#         else:
#             sum += i
# print(sum)
#  第二种 符号位
# j = -1
# while i < 101:
#     i += 1
#     # 符号位的变化
#     j = -j
#     if i == 88:
#         continue
#     else:
#         sum += i * j
# print(sum)
# 第二题
username = '1'
password = '2'
i = 3
while i > 0:
    i -= 1
    zh = input('Please input your count:')
    if zh == username:
        mm = input('Please input your password:')
        if mm == password:
            print('Login success!')
            break
        else:
            print('your password is wrong!')
            if i != 0:
                print('your have %s time(s)' % (i))
            else:
                new = input('your have %s time(s),want a go?Y' % (i))
                if new == 'Y':
                    i = 3
    else:
        print('your username is wrong!')
        if i != 0:
            print('your have %s time(s)' % (i))
        else:
            new = input('your have %s time(s),want a go?Y:' % (i))
            if new == 'Y':
                i = 3
else:
    print('这么多次了,还要脸面嘛?')
