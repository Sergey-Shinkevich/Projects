class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        self.__sides = list(sides)
        if len(self.__sides) != self.sides_count:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)



    def __is_valid_color(self, r, g, b):
        result = False
        count = 0
        new_color = [r, g, b]
        for i in range(0, 3):
            if new_color[i] >= 0 and new_color[i] <= 255 and isinstance(new_color[i], int):
                count += 1
        if count == 3:
            result = True
        return result

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, sides):
        result = False
        count = 0
        count_sides = len(sides)
        if self.sides_count != count_sides:
            return result
        else:
            for i in range(0, count_sides):
                if sides[i] >= 0 and isinstance(sides[i], int):
                    count += 1
        if count_sides == count:
            result = True
        return result

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)
        self.radius = (super().get_sides())[0] / 6.28

    def get_square(self):
        return 3.14 * (self.radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self.get_sides())/2
        s = (p * (p - (self.get_sides()[0])) * (p - (self.get_sides()[1])) * (p - (self.get_sides()[2]))) ** 0.5
        return s

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        Figure.__init__(self, color)
        self.__sides = [side, side, side, side, side, side, side, side, side, side, side, side]

    def get_sides(self):
        return self.__sides

    def set_sides(self, new_side):
        for i in range(0, 12):
            self.__sides[i] = new_side

    def get_volume(self):
        return (self.__sides)[0] ** 3





#------------------------------------------------------------
# Проверка круга

#Проверка на не корректное количество сторон
circle_0 = Circle([100, 100, 100], 100, 100)
print(circle_0.get_sides())

# Создание экземпляра круга
circle_1 = Circle([255,255,255], 10)

# Проверка исходного цвета круга
print(circle_1.get_color())

# Проверка исходной длины стороны
print(circle_1.get_sides())

# Проверка подсчета радиуса
print(circle_1.radius)

# Не корректное изменение цвета
circle_1.set_color(100,200,300)
print(circle_1.get_color())

# Корректное изменение цвета
circle_1.set_color(10,20,30)
print(circle_1.get_color())

# Корректное изменение размера стороны
circle_1.set_sides(20)
print(circle_1.get_sides())

# Подсчет площади круга
print(circle_1.get_square())
#------------------------------------------------------------
# Проверка треугольника
#Проверка на не корректное количество сторон
triangle_0 = Triangle((100,100,100), 10,19,19,20)
print(triangle_0.get_sides())

# Создание экземпляра треугольника
triangle_1 = Triangle([255,255,255],10,20,30)

# Проверка исходного цвета круга
print(triangle_1.get_color())

# Проверка исходной длины сторон
print(triangle_1.get_sides())

# Не корректное изменение цвета
triangle_1.set_color(100,200,300)
print(triangle_1.get_color())

# Корректное изменение цвета
triangle_1.set_color(10,20,30)
print(triangle_1.get_color())

# Корректное изменение размера стороны
triangle_1.set_sides(10,20,20)
print(triangle_1.get_sides())

# Подсчет площади треугольника
print(triangle_1.get_square())
#------------------------------------------------------------
# Проверка куба.
# Создание экземпляра куба
cube_1 = Cube([100,100,100],10)

# Проверка исходного цвета
print(cube_1.get_color())

# Проверка исходной длины сторон
print(cube_1.get_sides())

# Не корректное изменение цвета
cube_1.set_color(100, 200, 300)
print(cube_1.get_color())

# Корректное изменение цвета
cube_1.set_color(10,20,30)
print(cube_1.get_color())

# Корректное изменение размера стороны
cube_1.set_sides(20)
print(cube_1.get_sides())

# Подсчет объема куба
print(cube_1.get_volume())
