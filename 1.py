# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from decimal import Decimal
num = abs(Decimal(input('Введите вещественное число: ')))
while num != int(num):
    num *= 10
my_sum = 0
while num > 0:
    my_sum += int(num % 10)
    num /= 10
print(my_sum)

