def func_6(x):
    y = x.capitalize()
    return y


print(func_6('run'))

text = 'run boy run'.split()
list_el = []
for item in text:
    el = func_6(item)
    list_el.append(el)
res = ' '.join(list_el)
print(res)
