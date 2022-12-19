# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

num = int(input('Введите число: '))
my_list = []
my_sum = 0
for i in range(num):
    my_list.append(round((1 + (1 / (i + 1))) ** (i + 1), 2))
    my_sum += my_list[i]
print(f'n = {num} -> {my_list}')
print(f'Сумма = {my_sum}')
