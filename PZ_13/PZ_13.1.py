"""
В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры).
"""
import random
import functools

matrix = [[x for x in range(1, 11)] for y in range(1, 11)]
# N = input('Ввод N: ')
N = random.randint(0, 9)


def func():
    summa = 0
    proizv = 1
    for i in range(len(matrix)):
        summa = (functools.reduce(lambda a, b: a + b, [matrix[i][N] for i in range(len(matrix))]))
        proizv = (functools.reduce(lambda a, b: a * b, [matrix[i][N] for i in range(len(matrix))]))
    yield f'Сумма элементов столбца N: {summa}\nПроизведение элементов столбца N: {proizv}'


[print(f'Исходная матрица: \n{matrix}\nN задано значение "{N}"\n', i) for i in func()]
