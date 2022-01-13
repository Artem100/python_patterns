from abc import ABC, abstractmethod


class IPizzaBase(ABC):
    """Интерфейс декорируемого объекта
        В нем метод для добавления цены стоимости именно основы пиццы
    """
    @abstractmethod
    def cost(self) -> float:
        pass

class PizzaBase(IPizzaBase):
    """Класс декорируемого объекта
    Передаем класс себестоимость для пиццы
    """
    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost

class IDecorator(IPizzaBase):
    """Интерфейс декоратора
        Возращает имя пиццы
    """
    @abstractmethod
    def name(self) -> str:
        pass

class PizzaMargarita(IDecorator):
    """На основе PizzaBase получаем
    пиццу 'Маргарита'"""
    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost # доп. наценка для приговления пиццы
        self.__name = "Маргарита"

    def cost(self) -> float:
        """Метод для подсчета цены пиццы, который находится в классе IPizzaBase"""
        return self.__cost+self.__wrapped.cost() # доп наценку суммируем с основой пиццы

    def name(self) -> str:
        return self.__name

class PizzaSalami(IDecorator):
    """На основе PizzaBase получаем
    пиццу 'Салями'"""
    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Салями"

    def cost(self) -> float:
        """Таже идея что и для пиццы маргариты, но другая сумма
        для подсчета пиццы
        """
        return (self.__cost+self.__wrapped.cost())*2

    def name(self) -> str:
        return self.__name



if __name__ == "__main__":
    def print_pizza(pizza: IDecorator) -> None:
        print(f"Стоимость пиццы '{pizza.name()}' = {pizza.cost()}")

    pizza_base = PizzaBase(3.4)
    print(f"Стоимость основы пиццы = {pizza_base.cost()}")
    margarita = PizzaMargarita(pizza_base, 10)
    print_pizza(margarita)
    salami = PizzaSalami(pizza_base, 7)
    print_pizza(salami)