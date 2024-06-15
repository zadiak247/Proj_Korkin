"""
1. Перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена вложенных подкаталогов выводить не
нужно. перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку test1. В папку test
переместить два файла из П36, а в папку test1 - один файл из П37. Файл из ПЗ7 переименовать в test.txt. Вывести в
консоль информацию о размере файлов в папке test.
2. перейти в папку с P711, найти там файл с самым коротким именем, имя вывести в консоль. Использовать функцию
basename() (os.path.basename()).
3. перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в привязанной к нему программе. Использовать
функцию os.startfile().
4. удалить файл test.txt.
"""
import os

# первое задание:
os.chdir("../PZ_11")
print('Список всех файлов в каталоге PZ_11:', os.listdir())

# второе задание:
os.chdir("..")
if not os.path.isdir("test/test1"):
    os.makedirs("test/test1")
# os.replace("PZ_6/PZ_6.1.py/", "test/PZ_6.1.py")
# os.replace("PZ_6/PZ_6.2.py/", "test/PZ_6.2.py")
# os.replace("PZ_7/PZ_7.1.py/", "test/test1/test.txt")
print(f'Информация о размере файлов в папке test: {os.stat("test/").st_size} байт')

# третье задание:
for i in os.listdir("PZ_11/"):
    s_name = os.path.basename(f'PZ_11/{i}')
    for z in os.listdir("PZ_11/"):
        if s_name > os.path.basename(f'PZ_11/{z}'):
            s_name = os.path.basename(f'PZ_11/{z}')
    break

print('Файл с самым коротким именем в папке PZ11: ', s_name)

# четвертое задание:
# os.startfile('Reports/PZ_17.pdf', 'edit')

# пятое задание:
# os.remove("test/test1/test.txt")
