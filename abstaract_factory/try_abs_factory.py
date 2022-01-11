from abc import ABC, abstractmethod

"""
Базовые классы графического (базовые фичи)
"""


class StatusBar(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass


class MainMenu(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass


class MainWindow(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass


"""
Для операционной системы Windows создаем классы с основными операциями в программе (образно), 
в конструктор передаем тектовое значение, а именно как ОС (типо ОС) запускает команду (выполняет функцию из абстрактоного класса)
"""
class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created status bar for {self._system}')


class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created main menu for {self._system}')


class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created MainWindow for {self._system}')


"""
Тоже самое для Linux
"""
class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created status bar for {self._system}')


class LinuxMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created main menu for {self._system}')


class LinuxMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created MainWindow for {self._system}')



"""
Базовый класс абстрактной фабрики
"""
class GuiAbstractFactory(ABC):
    @abstractmethod
    def getStatusBar(self) -> StatusBar: pass

    @abstractmethod
    def getMainMenu(self) -> MainMenu: pass

    @abstractmethod
    def getMainWindow(self) -> MainWindow: pass


"""
Создаем классы и методы для Windows и Linux
для работы с абстрактоной фабрикой выше
"""
class WindowsGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()

    def getMainWindow(self) -> MainWindow:
        return WindowsMainWindow()


class LinuxGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return LinuxStatusBar()

    def getMainMenu(self) -> MainMenu:
        return LinuxMainMenu()

    def getMainWindow(self) -> MainWindow:
        return LinuxMainWindow()



"""
Клиентский класс, куда в конструктор передается интерфейс асбтрактной фабрики
В методе create_gui() вызываем интерфейсы наследованой фабрики
"""
class Application:
    def __init__(self, factory: GuiAbstractFactory):
        self._gui_factory = factory

    def create_gui(self):
        mainwindow = self._gui_factory.getMainWindow() # Создаем экземляры классов из методов абстрактной фабрики (т.к. они возращаеют ссылки на классы)
        status_bar = self._gui_factory.getStatusBar()
        main_menu = self._gui_factory.getMainMenu()
        mainwindow.create() # Вызываем метод из класса который нам возращает асбтрактный метод
        main_menu.create()
        status_bar.create()

# Метод который на вход принимает значение ОС, и он возращает методы, который подходят под это значение
def create_factory(system_name: str) -> GuiAbstractFactory:
    factory_dict = {
        "Windows": WindowsGuiFactory,
        "Linux": LinuxGuiFactory
    }
    return factory_dict[system_name]()

if __name__ == '__main__':
    system_name = "Linux" # задаем ОС
    ui = create_factory(system_name) # вызываем фабрику, которая создает нам реализацию асбтрактных методов для опеределнной ОС
    app = Application(ui) # Передаем значения в клиентский класс
    app.create_gui() # Вызываем метод клиентского класса