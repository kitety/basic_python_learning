def qqxing(l1=[]):
    '''
    共享数据类型
    如果默认参数值是一个可变的数据类型,那么没一次调用函数的时候,如果不传值就公用这个数据类型的资源
    '''
    l1.append(1)
    print(l1)


qqxing()
qqxing([])
qqxing()
qqxing()


def qqxing2(k, l2={}):
    l2[k] = 'haha'
    print(l2)


qqxing2(1)
qqxing2(2)
qqxing2(3)
qqxing2(4)
