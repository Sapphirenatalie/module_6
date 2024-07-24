# Наследование классов
# Подробное ТЗ:
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b,
# который проверяет корректность переданных значений перед установкой нового цвета.
# Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color
# на соответствующие значения, предварительно проверив их на корректность.
# Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
# возвращает True если все стороны целые положительные числа
# и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны,
# если их количество не равно sides_count, то не изменять, в противном случае - менять.
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
# Метод get_square возвращает площадь треугольника.
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон,
# если сторон не ровно sides_count, то создать массив с единичными сторонами
# и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

# Код для проверки:
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())

# Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# Проверка объёма (куба):
# print(cube1.get_volume())

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216

# Примечания (рекомендации):
# Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
# Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
# Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
# Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
# Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!


from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__color = color
        self.__sides = [*sides]
        self.filled = filled

    def get_color(self):
        if self.filled is True:
            return self.__color
        if self.filled is False:
            return [*self.__color]

    @staticmethod
    def __is_valid_color(*rgb):
        for item in rgb:
            if 0 <= item <= 255 and isinstance(item, int):
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]
            self.filled = True
        else:
            self.filled = False

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if self.sides_count != len(sides):
            sides = []
        for i in sides:
            if isinstance(i, int) and self.sides_count == len(sides):
                return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sum(self.get_sides()) / 2 * pi

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = (2 * self.get_square()) / (self.get_sides()[0])

    def get_square(self):
        return sqrt((sum(self.get_sides()) / 2) *
                    ((sum(self.get_sides()) / 2) - self.get_sides()[0]) *
                    ((sum(self.get_sides()) / 2) - self.get_sides()[1]) *
                    ((sum(self.get_sides()) / 2) - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
