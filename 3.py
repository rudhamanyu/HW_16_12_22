# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

n = int(input('Введите длину списка: '))
my_list = []
for i in range(n):
    my_list.append(input(f'Введите {i+1} элемент списка: '))
print(my_list)
sec_list = []
for j in range(n):
    rnd = randint(0, n - 1)
    sec_list.append(my_list[rnd])
    del my_list[rnd]
    n -= 1
print(sec_list)
