# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input('введите число N: '))
print(f'набор произведений чисел от 1 до {n}: ')
factorial = 1
i = 1
result=[]
while i <= n:
    factorial = factorial*i
    result.append(factorial)
    i += 1   
print(f'{result}')