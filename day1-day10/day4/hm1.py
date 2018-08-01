# s = '1324a5b6c'
# print(s[0]+s[2]+s[1])
# print(s[0:3])
# 循环输出
# s = '123456'
# for 循环
# for i in s:
#     print(i)
# while 循环
# index = 0
# length = len(s)
# while index < length:
#     print(s[index])
#     index += 1
# 加法计算器
inpStr = input('请输入表达式:').strip()
symbol = ['+', '-', '*', '/']
# 操作符
operation = ''
# 索引值
index = 0
for sym in symbol:
    if inpStr.find(sym) != -1:
        operation = sym
        index = inpStr.find(sym)
        break
sum = 0
# 注意类型转换
if operation == '+':
    sum = int(inpStr[0:index]) + int(inpStr[index + 1:])
elif operation == '-':
    sum = int(inpStr[0:index]) - int(inpStr[index + 1:])
elif operation == '*':
    sum = int(inpStr[0:index]) * int(inpStr[index + 1:])
elif operation == '/':
    sum = int(inpStr[0:index]) / int(inpStr[index + 1:])
print(sum)

