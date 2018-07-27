# print(12)
# a = input('enter a number:')
# print(a)
# 练习题1
# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)
# 练习题2
# count = 1
# while count < 101:
#     if count % 2 == 1:
#         print(count)
#     count += 1
# 练习题3
# sum = 0
# count = 0
# while count <= 100:
#     if count % 2 == 0:
#         sum -= count
#     else:
#         sum += count
#     count += 1
# print(sum)
# 练习题4
i = 0
while i < 3:
    i += 1
    user = input('请输入账号:')
    pwd = input('请输入密码:')
    if user == '1' and pwd == '2':
        print('登陆成功1')
        break
    else:
        print('错误')
