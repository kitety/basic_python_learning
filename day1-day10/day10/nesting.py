def max(a, b):
    i = 0
    if a > b:
        i = a
    else:
        i = b
    return i


# 函数嵌套-调用
def max2(a, b, c):
    d = max(a, b)
    return max(c, d)


print(max(1, 2))
print(max2(1, 2, 0.5))


# 函数嵌套-定义
# nonlocal 声明了一个上层局部变量(最近的一个,只能用于局部变量)
def outer():
    a = 1

    def inner():
        nonlocal a
        a += 1
        print('inner')

        def inner2():
            nonlocal a
            a += 10
            print(a)

        inner2()

    inner()


outer()
# 函数名就是内存地址,可以放入列表中.
