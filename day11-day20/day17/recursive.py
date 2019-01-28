# import sys
# sys.setrecursionlimit(10000000)
n = 0


def story():
    global n
    n += 1
    print(n)
    if (n <= 18):
        story()


# story()
def age(n):
    if n==4:
        return 40
    elif n>0 and n<4:
        return age(n+1)+2
print(age(1))
