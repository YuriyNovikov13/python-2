# 5. Реализуйте алгоритм перемешивания списка.

n = list(input('введите список: '))
print(n)
l = int(len(n))
import random
for i in range(l):
    j = random.randint(0, l-1)
    element = n.pop(j)
    n.append(element)
print(n)
