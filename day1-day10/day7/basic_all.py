# str int
s = '2'
print(s.isspace())
'''
list:
'''
li = [11, 22, 33, 44, 55]
for i in range(len(li) - 1, -1, -1):
    print(i, li)
    # print(li[li.index(i)])
    del li[i]
print(li)
