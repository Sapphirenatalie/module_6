# Доступ к свойствам родителя. Переопределение свойств
# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт,
# а Sedan(седан) - наследник класса Vehicle.
# Каждый объект Vehicle должен содержать следующие атрибуты объекта:
# Атрибут owner(str) - владелец транспорта. (владелец может меняться)
# Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
# Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
# Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
# Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
# Каждый объект Vehicle должен содержать следующий методы:
# Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
# Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
# Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
# Метод print_info - распечатывает результаты методов (в том же порядке):
# get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
# Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
# если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
# "Нельзя сменить цвет на <новый цвет>".

# Взаимосвязь методов и скрытых атрибутов:
# Методы get_model, get_horsepower, get_color находятся в одном классе
# с соответствующими им атрибутами: __model, __engine_power, __color.
# Поэтому атрибуты будут доступны для методов.
# Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают все его методы,
# взяты из класса Vehicle.

# Пример результата выполнения программы:
# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
# vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
# vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
# vehicle1.print_info()

# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Невозможно покрасить в Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok


class Vehicle:  # любой транспорт
    __COLOR_VARIANTS = ['dark_blue', 'red', 'metallic', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __engine_power: str, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        print(f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\nЦвет: {self.__color}\n'
              f'Владелец: {self.owner}\n')

    def set_color(self, new_color: str):
        self.__color = new_color

        if self.__color.isupper():
            return new_color.islower()
        if new_color in self.__COLOR_VARIANTS:
            return new_color
        else:
            print('Нельзя сменить цвет на ', new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle2 = Sedan('Vasyok', 'Toyota Mark II', 500, 'black')


print('Изначальные свойства vehicle1\n')
vehicle1.print_info()

print('Меняем свойства (в т.ч. вызывая методы)')
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

print('\nПроверяем что поменялось')
vehicle1.print_info()

print('Изначальные свойства vehicle2\n')
vehicle2.print_info()

print('Меняем свойства (в т.ч. вызывая методы)')
vehicle2.set_color('AQUA')
vehicle2.set_color('RED')
vehicle2.owner = 'Alex'

print('\nПроверяем что поменялось')
vehicle2.print_info()
