'''
Составить функцию, которая выполнит суммирование числового ряда.
'''

def suma():
    b = 0

    while True:
        a = input('ввод целого числа: ')
        try:
            a = int(a)
            b += a
        except ValueError:
            break
    print('сумма чисел: ', b)

suma()
