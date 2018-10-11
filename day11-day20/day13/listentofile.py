def tail(filename):
    f = open(filename, encoding="utf-8")
    # 不用for readline 都是一次性的
    while 1:
        line = f.readline()
        if line.strip():
            yield line.strip()


g = tail('hhh')
for i in g:
    print(i)
