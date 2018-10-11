f = open('hhh', encoding="utf-8")
# 不用for readline 都是一次性的
while 1:
    line = f.readline()
    if line:
        print(line)
