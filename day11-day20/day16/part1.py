# len 长度
# enumerate 枚举
# all判断是否有bool为false的值 接可迭代的数据
# any判断是否有bool为true的值 接可迭代的数据
print(all([1, 2, 3]))
print(any([1, 0, 2, 3]))

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = (9, 8, [6, 5], 9)
# 字典的话操作的是key
d = {"a": 99, "b": 100}
# 返回一个迭代器
print(zip(l1, l2, l3, d))
for i in zip(l1, l2, l3, d):
    print(i)
'''
# 两边的长度一样，以短的的为准
(1, 1)
(2, 2)
(3, 3)
'''


# filter 过滤函数
def is_odd(number):
    return number % 2 == 1


l = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
for i in l:
    print(i)
