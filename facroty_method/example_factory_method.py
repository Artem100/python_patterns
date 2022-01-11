from enum import Enum


class PizzaTypes(Enum):
    """
    Перечисление типы пицц, которые можно приготовить
    """
    MARGARITA = 0,
    MEXICO = 1,
    STELLA = 2

class Pizza:
    """
    Конструктор который возращает цену за пиццу
    """
    def __init__(self, price: float):
        self.__price = price # цена пиццы

    def get_price(self) -> float:
        return self.__price


class PizzaMargarita(Pizza):
    """
    Наследуемся от класса Pizza,
    наследуем конструктор Pizza,
    и задаем цену для этой пиццы
    """
    def __init__(self):
        super().__init__(3.5)

class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)


def create_pizza(pizza_type: PizzaTypes) -> Pizza:
    """
    Factory Method
    :return
    factory_dict[pizza_type]() # Возращаем сформированный словарь[передаем класс вызываемой пиццы и вызываем его конструктор]()
    """
    factory_dict = {
        PizzaTypes.MARGARITA: PizzaMargarita, # Пиццу которую мы будем создавать: передаем класс пиццы
        PizzaTypes.MEXICO: PizzaMexico,
        PizzaTypes.STELLA: PizzaStella
    }
    return factory_dict[pizza_type]()


if __name__ == '__main__':
    for pizza in PizzaTypes:
        my_pizza = create_pizza(pizza) # pizza Отправляется в формате PizzaTypes.MARGARITA, ищем такое значение по ключу и возращаем цену
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')
