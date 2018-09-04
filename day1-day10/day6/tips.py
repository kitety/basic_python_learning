'''
py2
    print 'abs'
    xrang() 生成器
    raw_input()
py3
    print('abs')
    range()
    input()
== 比较值 is比较内存地址

'''
l1 = [1, 2]
l2 = l1
# 指向同一个
print(l1 is l2, id(l1), id(l2))
# 数字 小数据池 -5-256
# 字符串 1 不能有特殊字符
i1 = 3
i2 = 3
print(id(i1), id(i2))
s1 = 'a'
s2 = s1 * 20
s3 = s1 * 30
print(id(s1), id(s2), id(s3))
