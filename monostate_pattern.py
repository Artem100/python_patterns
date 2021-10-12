class TheadData:
    __common_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = TheadData.__common_attrs


th1 = TheadData()
th2 = TheadData()
th2.id = 3
print(th1.__dict__) # Этот экзепляр тоже увидит что обновили значение атрибута id
th1.attr_new = 'new attr' # Добавляем новый ключ и значение в наш словарь
print(th2.__dict__) # Этот экземпляр тоже увидит новый атрибут