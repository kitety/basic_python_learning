# 递归已经要有结束条件
# 注意递归的return,要看返回操作是在第几层的时候发生的,返回给了对应的谁

# 斐波那契数列
# 对应的位置return
# 1 1 2 3 5 8
def fib(n):
    if (n == 1 or n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(12))
