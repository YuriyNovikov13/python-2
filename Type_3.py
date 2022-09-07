# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072
def func(x):
    return (1+(1/x))**x


list = []
n = int(input('введите число: '))
for i in range(1, n + 1):
    list.append(func(i))
print(list)
res = round(sum(list), 3)
print()
print(f'для n = {n} -> {res}')


