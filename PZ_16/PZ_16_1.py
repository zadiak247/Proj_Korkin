"""
Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который выводит информацию о животном
в формате "Имя: имя, Вид: вид"
"""


class Animal:
    def __init__(self, name, kind):
        """
        self.name = input('Ввод имени животного: ')
        self.kind = input('Ввод вида животного: ')
        """
        self.name = name
        self.kind = kind

    def inform(self):
        return f'\nИнформация о животном:\nИмя: {self.name}, Вид: {self.kind}'


anim_1 = Animal('лев', 'Лева').inform()
if __name__ == '__main__':
    print(anim_1)
