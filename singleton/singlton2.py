class Point:
    def __new__(cls, *args, **kwargs):
        """
        cls - ссылается на сам класс
        Вызывает до конструктора класса
        :param args: принимает аргументы, которые потом отправятся в конструктор
        :param kwargs:
        """
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls) # Возращаем ссылку на базовый класс, чтобы создавать экземпляр класса


    def __init__(self, x, y):
        """
        self - ссылается на созданный экземпляр класса
        :param x:
        :param y:
        :return:
        """
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y



pt = Point(1,2) # Экземпляр класса не был создан, т.к. __new__ должен возращать адрес созданного объекта
print(pt)