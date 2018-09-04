'''
ascii
    A 一个字符一个字节  8位
unicode
    A/中 一个字符4个字节 32位
utf-8
    A 一个字节 8位
    中 三个字节 24位
gbk
    A 一个字节 8位
    中 两个字节 16位
各个编码的二进制互相不能识别,会产生乱码
文件储存传输不为unicode(很大)
py3
    字符串 unicode(占内存)
    bytes 非unicode
    字符串=>bytes=>存储 传输
'''
s1 = 'alex'
s2 = b'alex'
# print(s1, type(s1))
# print(s2, type(s2))
s1 = '中国'
# s2 = b'中国'
# print(s1, type(s1))
# print(s2, type(s2))

# str=>bytes
s1 = 'alex'
s2 = s1.encode()
print(s1, s2)
s1 = '中国'
# s2 = s1.encode('utf-8')
s2 = s1.encode('gbk')
print(s1, s2)
