# 6. Напишите программу, в которой пользователь будет задавать две строки,
#    а программа - определять количество вхождений одной строки в другой.
#    aaabba   aa -> 2
#    abababbaba  aba -> 3
a = str(input('введите первую строку: '))
a1 = list(a)
aLen = len(a1)
b = str(input('введите вторую строку: '))
b1 = list(b)
bLen = len(b1)
sum = 0
if len(a1) >= len(b1):
    while len(a1) >= len(b1):
        a2 = a1[-bLen:]

        if a2 == b1:
            sum += 1
            a1.pop(-1)
        else:
            a1.pop(-1)
else:
    while len(b1) >= len(a1):
        b2 = b1[-aLen:]

        if b2 == a1:
            sum += 1
            b1.pop(-1)
        else:
            b1.pop(-1)

print(f'количество вхождений одной строки в другую -> {sum}')
