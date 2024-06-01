"""
Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год выпуска". От этого класса унаследуйте
класс "Автомобиль" и добавьте в него свойство "тип кузова".
"""


class Transport:

    @property
    def brand(self):
        pass

    @property
    def model(self):
        pass

    @property
    def issue_year(self):
        pass


class Automobile(Transport):
    @property
    def body_type(self):
        pass

