# ret=input('>>>')
ret = 'select name,age where age>20'
view, condiction = ret.split('where')
# view=view.split(' ')[1]
# print(view, condiction)
view=view.replace('select',' ').strip()
view_list=view.split(',')
print(view_list, condiction)
