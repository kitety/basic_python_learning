s = '这是一段文本'


def my_len(s):
    i = 0
    for k in s:
        i += 1
    return i


def my_len2():
    return 1, 2, 3


print(my_len(s))
# 直接用元组接收
r = my_len2()
# 分开接收
a, b, c = my_len2()

print(r)
print(a, b, c)


# 其实元组,列表,字典都有解构


def my_sum(a, b):
    return a + b


# 传参设置
print(my_sum(1, 2))
print(my_sum(b=1, a=2))


def classmate(name, sex='男'):
    print('%s,%s' % (name, sex))


classmate('小王')
classmate('小王')
classmate('小王', '女')


def sum(*args):
    n = 0
    for i in args:
        n += i
    return n


print(sum(1, 2, 3))


def func1(**kwargs):
    print(kwargs)


func1(a=1, b=2)


def func2(*args, **kwargs):
    print(args, kwargs)


func2(1, 2, 3, 4, 5, 6, 8, a=1, b=2)


# 定义函数的参数顺序:位置参数 *args,默认参数,**kwargs


# 形参角度,为变量加上*,就是组合所有传来的值
def func3(*args):
    print(args)


l1 = [1, 2, 3323]
# 实参角度,为序列加上*,就是将这个序列按照新顺序打散
func3(*l1)


def func4(**kwargs):
    print(kwargs)


d = {'a': 1}
func4(**d)
