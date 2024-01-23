"""
Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
и вывести эти элементы в порядке возрастания индексов.
"""

import random

N = random.randrange(-10, 10)
a = []
for i in range(abs(N)):
    a.append(random.randrange(-10, 11))

print('Исходный список: \n', a, '\nРазмер списка: ', abs(N))

suma = 0
a1 = 0
a2 = 0
for i in range(abs(N)):
    try:
        if suma < (a[i]+a[i+1]):
            a1 = a[i]
            a2 = a[i+1]
            suma = (a[i]+a[i+1])
    except IndexError:
        break

print('\nмаксимальная сумма двух соседних элементов списка размером N: ', suma,
      '\nэлементы в порядке возрастания индексов: ', a1, 'и', a2)
