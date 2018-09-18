# 求n个数的和
def sum_func(*args):
    total = 0
    for i in args:
        total += i
    return total


print(sum_func(1, 2, 3, 4, 5, 6))


# 返回参数的奇数位
def func1(l):
    # 切片
    return l[0::2]


print(func1([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 判断传入长度是否大于5
def func2(l):
    return len(l) > 5


print(func2([1, 2, 3, 4, 5, 6, 7]))


# 保留裂变前两位
def chech_func(l):
    # 直接返回,不用判断
    # if len(l) > 2:
    # 包头不包尾
    return l[:2]


print(chech_func([1, 2, 3, 4, 5]))


# 计算传入字符串的数字,字符,空格,其他 的个数
def count(s):
    obj = {'number': 0, 'character': 0, 'blank': 0, 'other': 0}
    for ss in s:
        if ss.isdigit():
            obj['number'] += 1
        elif ss.isalpha():
            obj['character'] += 1
        elif ss.isspace():
            obj['blank'] += 1
        else:
            obj['other'] += 1
    return obj


# input_str = input('请输入:')
# obj = count(input_str)
# print('您输入的字符串有{}个数字,{}个字母,{}个空格,{}个其他字符'.format(
#     obj['number'], obj['character'], obj['blank'], obj['other']))


# 判断用户传入的对象(字符串,列表,元组)每一个元素是不是空内容
# True 有空的,False 没有空的
def func3(l):
    # 是字符串并且非空
    if not l:
        return True
    elif type(l) is str and l:
        for i in l:
            if i == ' ':
                return True
        return False
    elif l and (type(l) is list or type(l) is tuple):
        for i in l:
            if not i:
                return True
        return False
    else:
        return False


print(func3([1, 2]))


# 只保留字典的每个值的前两位
def dict_func(l):
    for k in l:
        if len(l[k]) > 2:
            l[k] = l[k][:2]
    return l


print(dict_func({'k': '112321321', 'v': '2121212'}))


# 返回较大者
# return (a>b的返回) if a > b else 否则的返回
def max_func(a, b):
    return a if a > b else b


print(max_func(1, 2))
