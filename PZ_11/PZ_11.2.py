"""
Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое, количество пробельных символов.
Сформировать новый файл, а который поместить текст в стихотворной форме, предварительно вставив после каждой строки
строку из символов "*".
"""

''' запись данных в исходный файл:
a = open('text18-12.txt', 'w')
a.write('Дана строка-предложение на русскому языке. Вывести самое короткое слово в предложении. \n'
        'Если таких слов несколько, то вывести последнее из них. Словом считать набор символов, не содержащий \n'
        'пробелов, знаков препинания и ограниченный пробелами, знаками препинания или началом/концом строки.\n')
a.close()
'''

a = open('text18-12.txt', 'r')
sod = a.read()
a.close()

sp = 0
for i in sod:
    if i == ' ':
        sp += 1

if len(sod) > 0:
    print('Содержимое предложенного текстового файла: ', sod)
else:
    print('Предложенный текстовый файл пуст')

print('Количество пробельных символов: ', sp)

b = open('text19-13.txt', 'w')
b.write(sod.replace('\n', '\n*****\n'))
b.close()

''' просмотр содержимого файла:
b = open('text19-13.txt', 'r')
z = b.read()
b.close()

print(z)
'''

a = open('text18-12.txt', 'w')
a.seek(0)
a.close()