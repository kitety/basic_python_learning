# f = open('D:\老师.txt', mode='r', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# 当前的文件
# f1 = open(
#     'E:\study\python\day1-day10\day8\main.txt', mode='r', encoding='utf-8')
# print(f1.read())
# byte类型
# f1 = open('E:\study\python\day1-day10\day8\main.txt', mode='rb')
# print(f1.read())

# 只写
# 清楚原文件内容再写
# f = open('testfile', mode='wb')
# # 字符串转换为bytes
# f.write('测试覆盖1'.encode('utf-8'))
# f.close()

# 追加
# f = open('testfile', mode='a', encoding='utf-8')
# f.write('test')
# f.close()

# f = open('testfile', mode='ab')
# f.write('test'.encode('utf-8'))
# f.close()

# 可读可写 先读后写
# f = open('testfile', mode='r+', encoding='utf-8')
# content = f.read()
# f.write('python读写')
# f.close()
# print(content)

# 先写后读
# 注意光标的位置
# f = open('testfile', mode='r+', encoding='utf-8')
# f.write('aaa')
# content = f.read()
# f.close()
# print(content)

# 先写后读 bytes
# 注意光标的位置
# f = open('testfile', mode='r+b')
# content = f.read()
# f.write('testtext'.encode('utf-8'))
# f.close()
# print(content)

# 写读
# f = open('testfile', mode='w+', encoding='utf-8')
# f.write('testtext')
# f.seek(0)
# content = f.read()
# f.close()
# print(content)

# 追加
# f = open('testfile', mode='a+', encoding='utf-8')
# f.write('testtext')
# # 注意光标位置
# f.seek(0)
# content = f.read()
# f.close()
# print(content)

# 功能详解
# 光标的位置的移动的个数跟那个存储的编码方式有关 如utf8 一个中文三个字节 所以只能是三的倍数
# seek 设置光标位置 tell 查看光标位置
f = open('testfile', mode='r+', encoding='utf-8')
# f.seek(1)
# 读出来字符 f.read() 可以设置个数
f.write('add113132121312')
count = f.tell()
# 读取后面三个
f.seek(count - 3)
content = f.read()
# print(content)
f.close()


# 其他
# 判断文件是否可读 f.readable()
# 一行一行读 f.readline()
# 每一行当成列表的一个元素 添加到列表 f.readlines()
# 截断文字输出,源文件 f.truncate()
# f = open('testfile', mode='r+', encoding='utf-8')
# print(f.readable())
# print(f.readline())
# print(f.readlines())
# f.seek(0)
# # f.truncate(5)
# print(f.read())
# for i in f:
#     print(i)
# f.close()

# 循环 直接看文件
# f = open('testfile', mode='r+', encoding='utf-8')
# for i in f:
#     print(i)
# f.close()

# 不谢close
with open('testfile', mode='r+', encoding='utf-8') as f:
    print(f.read())
