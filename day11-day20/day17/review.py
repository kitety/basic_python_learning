# 内置函数
# 带key(可接匿名函数) max,min,filter,map,sorted

# 匿名函数
# lambda 参数,参数2:返回值表达式

# 1.用map处理,讲列表中的数据加上'_well'后缀,a变为a_well
# name = ['hello', 'cool', 'usa', 'family']
#
#
# def func(str):
#     return str + '_well'
#
# #迭代器
# new_name=map(func, name)
# # 或者for循环
# # print(list(new_name))
# for i in new_name:
#     print(i)
#
# print(list(new_name)) # [] 取值去完了 是个迭代器
# print(list(i))

# 匿名函数形式
# 迭代器与生成器的区别
name = ['hello', 'cool', 'usa', 'family']
ret = map(lambda s: s + '_well', name)
# print(list(ret))

# 2.filter 筛选偶数

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fun_even(num1):
    return num1 % 2 == 0

# 迭代器
# lambda 三元运算符,列表推倒式
ret = filter(fun_even, num)
ret1 = filter(lambda x:x%2==0, num)
ret2 = filter(lambda x:True if x%2==0 else False, num)
print(list(ret))
print(list(ret))
print(list(ret1))
print(list(ret1))
