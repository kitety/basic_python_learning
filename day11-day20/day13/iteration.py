from collections import Iterable
from collections import Iterator

# 迭代器
list1 = [1, 2, 3]
# 索引 循环 for
# list dic str set tuple f=open() range() enumerate
# print(set(dir([])))
# print(dir({}))
# print(dir(''))
# print(dir(range(5)))
# 集合有交集
ret = set(dir([])) & set(dir({})) & set(dir('')) & set(dir(range(5)))
# print(ret)
# print('__iter__' in dir(int))
# print('__iter__' in dir([]))
# print('__iter__' in dir(''))
# print('__iter__' in dir({}))
# print('__iter__' in dir(bool))
# 集合的差集
print(set(dir([].__iter__())) - set(dir([])))
# 元素个数__length_hint__()
print([1, 2, 3].__iter__().__length_hint__())
# print([1,2,3].__iter__().__next__())
# 从那个开始__setState__()
# print([1, 2].__iter__().__setState__())
list1 = [1, 2, 3]
iterator1 = list1.__iter__()
print(iterator1.__next__())
print(iterator1.__next__())
print(iterator1.__next__())
print(isinstance([], Iterator))
print(isinstance([], Iterable))


# 自己定义
class A:
    def __iter__(self):
        pass

    def __next__(self):
        pass


a = A()
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# 自己的for循环的实现
# l1 = [1, 2, 3, 4]
# iterator = l1.__iter__()
# while 1:
#     print(iterator.__next__())
