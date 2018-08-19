# 元组
tu = (123, 'alex', [1, 23, 45, 'cool'], 56)
# tu[2][0] = 8989
# print(tu[2][0])
# for i in tu:
#     print(i)
tu[2][3] = tu[2][3].upper()
tu[2].append('testAdd')
# print(tu)

# s = 'alex'
# s1 = '_a_'.join(s)
# print(s1)

# 列表转换为字符串join
# 字符串转换为列表split
tu2 = ('123', 'alex', '56')
# join(可迭代对象)
tu1 = ''.join(tu2)
# print(tu1)

# range
# for i in range(1, 52, 2):
# print(i)
# for i in range(10, 1, -2):
#     print(i)
for i in range(0, 10, -1):
    # 什么都没有
    pass

# for循环嵌套
li = [1, 2, 3, [4, 4, 5, 6], 'alex', 'cool']
for i in li:
    if (type(i) == list) or (type(i) == str):
        for ii in i:
            print(ii)
    else:
        print(i)
