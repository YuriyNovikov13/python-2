# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.    
#     *Пример:*    
#     - 6782 -> 23
#     - 0,56 -> 11
n=list(input('введите число: '))
print(n)
sum=0
for i in range(len(n)):
    sum+=int(n[i])
    i+=1
print(sum)

