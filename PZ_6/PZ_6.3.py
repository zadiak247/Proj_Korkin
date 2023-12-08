"""
Дан список размера N и целое число k (1<K<N). Осуществить сдвиг элементов списка вправо на K позиций
(при этом A₁ перейдет в Aₖ₊₁, A - в Aₖ₋₂, ..., Aₙ₋ₖ - в Aₙ, а исходное значение K последних элементов будет потеряно).
Первые K элементов полученного списка положить, равными 0.
"""

import random

N = random.randrange(-1000, 1001)
a = []
k = random.randint(1, abs(N))

for i in range(abs(N)):
    a.append(random.randrange(-1000, 1001))

print('Исходный список: \n', a, '\nРазмер списка: ', abs(N))

for i in range(k):
    a.insert(0, a.pop())
for i in range(k):
    a[i] = 0

print('\nитоговый список: \n', a)