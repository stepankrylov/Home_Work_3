def func_1(x, y):
    if y != 0:
        res = x / y
        return res
    else:
        print('На 0 делить нельзя!')
        return


'''
result = func_1(5, 0)
print(result)
'''


def func_2(first_name, last_name, year_of_birth, city, email, tel):
    form = f'имя: {first_name}, фамилия: {last_name}, год рождения: {year_of_birth}, ' \
           f'город проживания: {city}, e-mail: {email}, номер телефона: {tel}'
    return form


'''
result = func_2(first_name='Mike', last_name='Pirson', year_of_birth='1975',
                city='New York', email='mikep@mail.com', tel='+1(987)6543210')
print(result)
'''


def func_3(x, y, z):
    arg = [x, y, z]
    arg.remove(min(arg))
    res = sum(arg)
    return res


'''
result = func_3(5, 1, 6)
print(result)
'''


def func_4(x: float, y: int):
    res_1 = x ** y
    rez_2 = 1
    for item in range(-y):
        rez_2 = rez_2 * 1 / x

    return res_1, rez_2


'''
result_1, result_2 = func_4(3, -2)
print(f'Первым способом: {result_1} и вторым: {result_2}')
'''
