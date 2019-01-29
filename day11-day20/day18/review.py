# 递归已经要有结束条件
# 注意递归的return,要看返回操作是在第几层的时候发生的,返回给了对应的谁

# 斐波那契数列
# 对应的位置return
# 1 1 2 3 5 8
def fib(n):
    if (n == 1 or n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(12))

# 一个函数里面嵌套两次递归,不好
# 优化=>一个函数里面嵌套一次递归
# 求某个数的时候已经知道前面两个数是多少
#  a,b=1+1=f(3)
# f(4)=f(3)+f(2)=b+ a+b=1+2  return 2,3
# 一个数的前面两个

def fib2(n, l=[0]):
    l[0] += 1
    # print(l[0], n)
    if (n == 1 or n == 2):
        l[0] -= 1
        if l[0] == 0:
            return 1
        return 1, 1
    else:
        a, b = fib2(n - 1)
        l[0] -= 1
        if l[0] == 0:
            return a + b
        return b, a + b


print(fib2(9))
