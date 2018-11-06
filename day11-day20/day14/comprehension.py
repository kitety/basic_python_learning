# 遍历处理
# [每一个相关元素 for 元素 in 可迭代]
# 遍历+筛选
# [满足条件的元素每一个相关元素 for 元素 in 可迭代 if 元素的条件]
ret = [i for i in range(30) if i % 3 == 0]
# 得到一个数组
print(ret)
ret = [i**2 for i in range(30) if i % 3 == 0]
# 得到一个数组
print(ret)

names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
ret = [names for list in names for names in list if names.count('e') > 1]
# 找到数组 找到元素 计算元素的包含
print(ret)

# 字典的key value对调
mcase = {'a': 10, 'b': 34}
# 得到键
# for i in mcase:
#     print(i)
mcase_query = {mcase[i]: i for i in mcase}
print(mcase_query)

# 合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# 得到键
# for i in mcase.keys():
#     print(i)
# 键值对就是键值对,大写小写都模糊处理,直接可以拿到值
mcase_query = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase
}
print(mcase_query)

# 集合推导式
squared = {x**2 for x in [1, -1, 2]}
print(squared)
