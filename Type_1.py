# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11
n = str(input('введите число: '))
lst = list(n)
if ',' in lst:
    lst.remove(',')
if '.' in lst:
    lst.remove('.')
sum = 0
for i in range(len(lst)):
    sum += int(lst[i])
    i += 1
print(f'сумма цифр числа {n} -> {sum}')
