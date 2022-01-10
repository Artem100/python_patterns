class Point:

    __instance = None # Сслыка на экзмепляр класса, если его нет, то значение None будет, если есть то это будет ссылка на экземпляр класса
    # Чтобы проверять существует или нет ссылка объекта

    # Содание синглтона
    def __new__(cls, *args, **kwargs):
        """
        Волшебный метод перегрузки конструктора
        cls - ссылка на внутрений класс Point

        :param args:
        :param kwargs:
        """
        if cls.__instance is None:
            # если текущий экзменпляр не равняется текущему классу, то мы создаем экзмепляр класса
            cls.__instance = super(Point, cls).__new__(cls) # Здесь создаем класс Point
        return cls.__instance

    def __del__(self):
        Point.__instance = None # снова сделаем None, если объект будет удален

    def __init__(self, _x=0, _y=0 ):
        self.x = _x
        self.y = _y

    def get_attrs1(self):
        print("Created: ", self.x, self.y)

c = Point(1, 5)
c2 = Point(13, 54)
print(id(c), id(c2)) # Айдишники у двух экземлпяров будет одинаковый

c.get_attrs1() # Данные будут использовать последнего экземпляра c2, т.к. с2 переписал данные одного экземлпяра класса
c2.get_attrs1() # Данные будут использовать последнего экземпляра c2