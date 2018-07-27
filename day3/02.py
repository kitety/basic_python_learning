# 字符串的索引和切片
s = 'abcdefg'
print(s[0])
print(s[-2])
# 切片 顾头不顾尾
print(s[0:2])
print(s[0:-1])
print(s[0:0])
print(s[0:5:2])
print(s[4:0:-1])
s = 'ABCDLSESRF'  # s[首:尾:步长]
# s10 = s[0:5:2]
# print(s10)
s11 = s[4:0:-1]
print(s11)
s12 = s[3::-1]
print(s12)
s13 = s[3::-2]
print(s13)

s = 'ABCDLSESRF'  # s[首:尾:步长]
s10 = s[0:5:2]
print(s10)
s11 = s[4:0:-1]
print(s11)
s12 = s[3::-1]
print(s12)
s13 = s[3::-2]
print(s13)
s = 'ABCDLSESRF'
s14 = s[-1::-1]
print(s14)
s15 = s[::-1]
print(s15)
