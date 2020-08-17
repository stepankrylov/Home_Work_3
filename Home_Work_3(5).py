def func_5():
    ex = 0
    on = input('введите числа: ').split()
    for item in on:
        if item.isdigit():
            list_1.append(item)
        elif item == 'a':
            ex = 'exit'
    res = sum(list(map(int, list_1)))
    return res, ex


list_1 = []
while True:
    x, y = func_5()
    if y != 'exit':
        print('Итоговая сумма: ', x)
    else:
        print('Итоговая сумма: ', x)
        print('Выход')
        break

