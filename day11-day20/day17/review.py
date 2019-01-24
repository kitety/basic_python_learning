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
# lambda 三元运算符,列表推导式
ret = filter(fun_even, num)
ret1 = filter(lambda x: x % 2 == 0, num)
ret2 = filter(lambda x: True if x % 2 == 0 else False, num)
# print(list(ret))
# print(list(ret))
# print(list(ret1))
# print(list(ret1))

# 3.随意写一个20行以上的文件
# 运行程序,先将内容读取到内存中,
# 接收用户输入的页码,每页5条,仅输出当页内容
# with open('data.txt', encoding='utf-8') as f:
#     # 转换为数组
#     l = f.readlines()
# page_num = int(input('请输入页码:'))
# # 每一页的大小
# page_size = 5
# # 1 1-5 (n-1)*5 开始 加五个
# # 2 6-10
# # 3 11-15
# # 4 16-20
# # 5 21-...
# # 商余函数
# # 总的页码 和 多的条数
# pages, mod = divmod(len(l), page_size)
# if mod:
#     pages += 1
#
# if page_num > pages or page_num <= 0:
#     print('输入有误')
# elif page_num == pages and mod != 0: # 输入的页码是最后一页,且有剩余行数
#     for i in range(mod):
#         # 输出这一页剩余的行数
#         print(l[(page_num - 1) * 5 + i].strip())
#
# elif page_num > 0 and page_num < pages:
#     for i in range(5):
#         print(l[(page_num - 1) * 5 + i].strip())

# 4.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 4.1 计算购买每只股票的总价
ret_all = map(lambda dic: {dic['name']: round(dic['shares'] * dic['price'], 2)}, portfolio)
print(list(ret_all))
# 4.2 过滤出单价大于100的股票
ret_greater100 = filter(lambda item: item['price'] > 100,portfolio)
print(list(ret_greater100))
