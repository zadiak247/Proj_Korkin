"""
Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год выпуска". От этого класса унаследуйте
класс "Автомобиль" и добавьте в него свойство "тип кузова".
"""


class Transport:

    def __init__(self, mark, model, release_year):
        self.mark = mark
        self.model = model
        self.release_year = release_year


class Automobile(Transport):

    def __init__(self, mark, model, release_year, body_type):
        super().__init__(mark, model, release_year)
        self.body_type = body_type
