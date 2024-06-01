"""
Для задачи из блока 1 создать две функции, save_def u load_def, которые позволяют сохранять информацию из экземпляров
класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов
Python в бинарном формате.
"""
import pickle
from PZ_16_1 import Animal


def save_def():
    with open("pickle.bin", "wb") as file:
        pickle.dump(Animal().inform(), file)


def load_def():
    with open("pickle.bin", "rb") as file:
        return pickle.load(file)


save_def()
print(load_def())
