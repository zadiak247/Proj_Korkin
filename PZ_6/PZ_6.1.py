"""
Дан список A размера N (N - нечетное число). Вывести его элементы с нечетными номерами в порядке убывания номеров:
Aₙ, Aₙ₋₂, Aₙ₋₄, ..., A₁. Условный оператор не использовать.
"""

import random

N = random.randint(-1000, 1000)
while N % 2 == 0:
    N = random.randint(-1000, 1000)

A = []
i = 0
while i < abs(N):
    A.append(random.randint(-1000, 1000))
    i += 1

print('Исходный список: \n', A, '\nРазмер списка: ', abs(N))

_A = []
i = 0
while i <= abs(N):
    try:
        while i % 2 != 0:
            _A.append(A[-i])
            break
    except IndexError:
        break
    i += 1

print('\nэлементы списка A с нечетными номерами (в порядке убывания номеров): \n', _A)
