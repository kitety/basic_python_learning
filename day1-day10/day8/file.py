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
f = open('testfile', mode='r+b')
content = f.read()
f.write('testtext'.encode('utf-8'))
f.close()
print(content)
