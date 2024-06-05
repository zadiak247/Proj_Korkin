"""
Для задачи из блока 1 создать две функции, save_def u load_def, которые позволяют сохранять информацию из экземпляров
класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов
Python в бинарном формате.
"""
import pickle
from PZ_16_1 import Animal


def save_def(anim_n):
    with open("pickle.bin", "wb") as file:
        pickle.dump(anim_n, file)


def load_def():
    with open("pickle.bin", "rb") as file:
        return pickle.load(file)


anim_1 = Animal('лев', 'Лева').inform()
anim_2 = Animal('слон', 'Богдан').inform()
anim_3 = Animal('собака', 'Боблин').inform()

save_def(anim_1)
print(load_def())
save_def(anim_2)
print(load_def())
save_def(anim_3)
print(load_def())
