"""
В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива.
"""
import random

matrix = [[random.randint(-20, 20) for x in range(-10, 10)] for y in range(1, 6)]


def func():
    mas = []
    for i in range(len(matrix)):
        for z in range(len(matrix[i])):
            if matrix[i][z] < 0:
                mas.append(matrix[i][z])
    yield f'Новый массив, содержащий отрицательные элементы матрицы: {mas}'


[print(f'Исходная матрица: {matrix}\n', i) for i in func()]
