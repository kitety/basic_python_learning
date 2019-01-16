# len 长度
# enumerate 枚举
# all判断是否有bool为false的值 接可迭代的数据
# any判断是否有bool为true的值 接可迭代的数据
# print(all([1, 2, 3]))
# print(any([1, 0, 2, 3]))

from math import sqrt
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = (9, 8, [6, 5], 9)
# 字典的话操作的是key
d = {"a": 99, "b": 100}
# 返回一个迭代器
# print(zip(l1, l2, l3, d))
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


# 返回迭代器,节省内存
# 结果为真才会留下
# 第一个参数为一个函数,验证true就留下,反之
# l = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
# for i in l:
#     print(i)

def is_str(s):
    return type(s) == str


l1 = filter(is_str, ['1', '2', 3, 4, 5, 6, 'hello'])
for i in l1:
    print(i)

# print('去除空数据')
# # def is_not_empty(s):
# #     return s and str(s).strip()
# #
# # l = filter(is_not_empty, [1,'hello','','  ',6,7,[],'world'])
# # for i in l:
# #     print(i)

# 开平方


def is_sqrt_int(num):
    return sqrt(num) % 1 == 0


all_sqrt_int = filter(is_sqrt_int, range(1, 101))
for i in all_sqrt_int:
    print(i)

# map 循环  类似于for循环
ret = map(sqrt, [1, 4, 5, 6])
for i in ret:
    print(i)
'''
filter 是过滤,值可能变化
map 是循环遍历,个数不变
'''

# sorted排序方法(可迭代,函数名,是否reverse)
l3 = [1, -2, 3, -6, 89]
# 在原基础上排序
l3.sort(key=abs)
print(l3)

# 返回一个新的列表,不改变原列表,占内存
# 注意内存,在不大,数据小的情况下用,排序算法比较好用(c语言,多机制)
# 可以接reverse
l4 = [1, -2, 3, -6, 89]
print(sorted(l4, key=abs, reverse=True))

# 按照长度排序
l5 = ['1', '565656', '23']
print(sorted(l5, key=len))
