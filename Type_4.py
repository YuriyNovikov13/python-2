#  [-4 -3 -2 -1 0 1 2 3 4] 3 8
#                             -2 * 3 = -6
# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции (начиная с 1) пользователь вводит с клавиатуры.

n = int(input('введите число N: '))
array = []
for i in range(-n, n+1):
    array.append(i)
print(array)
length = len(array)
a = int(input('введите первую позицию: '))
b = int(input('введите вторую позицию: '))
if 1 > a or a > length or 1 > b or b > length or a >= b:
    print('введены не корректные данные')
else:
    result = array[a-1]*array[b-1]
    print(f'произведение указанных элементов = {result}')



