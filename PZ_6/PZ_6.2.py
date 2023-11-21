"""
Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
и вывести эти элементы в порядке возрастания индексов.
"""

import random

N = random.randrange(-1000, 1001)
a = []
for i in range(abs(N)):
    a.append(random.randrange(-1000, 1001))

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

print('максимальная сумма двух соседних элементов списка размером N: ', suma, '\n',
      'элементы в порядке возрастания индексов: ', a1, 'и', a2)
