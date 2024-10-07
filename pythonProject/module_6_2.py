class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine):
        self.owner = owner
        self.__model = model
        self.__enginepower = engine
        self.__color = color

    def get_model(self):
        print('Модель: ', self.__model)

    def get_horsepower(self):
        print('Мощность двигателя: ', self.__enginepower)

    def get_color(self):
        print('Цвет: ', self.__color)

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('Владелец: ', self.owner)

    def set_color(self, new_color):
        accept_color = False
        for color in self.__COLOR_VARIANTS:
            if color.lower() == new_color.lower():
                accept_color = True
        if accept_color is True:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на: ', new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
