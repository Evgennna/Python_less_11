# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance


if __name__ == '__main__':
    s = MyStr('hello', 'qwerty')
    print(s)
    print(s.author)
    s2 = MyStr('si', 'asdfg')
    print(s2.author)
    print(s.upper())
    print(s.time, s2.time)

# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """При первом запуске создает экземпляр класса, при повторном - добавляет в архив прежние данные."""
    instance = None
    counts = []
    texts = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.counts.append(cls.instance.count)
            cls.instance.texts.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text

    def __str__(self):
        c = self.instance.counts if self.instance.counts else "Empty"
        t = self.instance.texts if self.instance.texts else "Empty"
        return f"Value: {self.instance.count}, text: {self.instance.text} " \
    f"value archive: {c}, text archive: {t}"

    def __repr__(self):
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.texts)
    print(f'{d1}')
    print(f'{d1 =}')
    d2 = Archive(2, "b")
    print(d2.text, d2.texts)
    print(f'{d2}')
    print(f'{d2 =}')

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """При первом запуске создает экземпляр класса, при повторном - добавляет в архив прежние данные."""
    instance = None
    counts = []
    texts = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.counts.append(cls.instance.count)
            cls.instance.texts.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text

    def __str__(self):
        c = self.instance.counts if self.instance.counts else "Empty"
        t = self.instance.texts if self.instance.texts else "Empty"
        return f"Value: {self.instance.count}, text: {self.instance.text} " \
    f"value archive: {c}, text archive: {t}"

    def __repr__(self):
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.texts)
    print(f'{d1}')
    print(f'{d1 =}')
    d2 = Archive(2, "b")
    print(d2.text, d2.texts)
    print(f'{d2}')
    print(f'{d2 =}')


# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, height: float, width: float = 0):
        self.height: float = height
        self.width: float = [width, height][width == 0]
        self.__perimetr: (float, None) = None
        self.__area: (float, None) = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: float):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: float):
        self._width = width

    @property
    def perimetr(self) -> float:
        if self.__perimetr is None:
            self.__perimetr = (self.height + self.width) * 2
        return self.__perimetr

    @property
    def area(self) -> float:
        if self.__area is None:
            self.__area = self.height * self.width
        return self.__area

    def __add__(self, other):
        new_perimetr = self.perimetr + other.perimetr
        new_height = self.height + other.height
        new_width = new_perimetr/2 - new_height
        return Rectangle(new_height, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr - other.perimetr)
        new_height = abs(self.height - other.height)
        new_width = new_perimetr/2 - new_height
        return Rectangle(new_height, new_width)

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area


if __name__ == '__main__':
    rectangle1 = Rectangle(2)
    rectangle2 = Rectangle(4, 5)
    new_rec = rectangle1 + rectangle2
    print(new_rec.width, new_rec.height, new_rec.perimetr)
    new_new_rec = rectangle1 - rectangle2
    print(new_new_rec.width, new_new_rec.height, new_new_rec.perimetr)

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, height: float, width: float = 0):
        self.height: float = height
        self.width: float = [width, height][width == 0]
        self.__perimetr: (float, None) = None
        self.__area: (float, None) = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: float):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: float):
        self._width = width

    @property
    def perimetr(self) -> float:
        if self.__perimetr is None:
            self.__perimetr = (self.height + self.width) * 2
        return self.__perimetr

    @property
    def area(self) -> float:
        if self.__area is None:
            self.__area = self.height * self.width
        return self.__area

    def __add__(self, other):
        new_perimetr = self.perimetr + other.perimetr
        new_height = self.height + other.height
        new_width = new_perimetr/2 - new_height
        return Rectangle(new_height, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr - other.perimetr)
        new_height = abs(self.height - other.height)
        new_width = new_perimetr/2 - new_height
        return Rectangle(new_height, new_width)

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area


if __name__ == '__main__':
    rectangle1 = Rectangle(2)
    rectangle2 = Rectangle(4, 5)
    new_rec = rectangle1 + rectangle2
    print(new_rec.width, new_rec.height, new_rec.perimetr)
    new_new_rec = rectangle1 - rectangle2
    print(new_new_rec.width, new_new_rec.height, new_new_rec.perimetr)


# Создайте класс Матрица. Добавьте методы для:
# вывода на печать
# сравнения
# сложения
# *умножения матриц

from functools import total_ordering


@total_ordering
class Matrix:
    def __init__(self, matrix: list[list]):
        self.value = matrix
        self.length = len(matrix)
        self.height = len(matrix[0])

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, matrix: list[list]):
        self._value = matrix

    def __str__(self):
        return "\n".join(str(i) for i in self.value)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.value[i][j] == other.value[i][j])
                return all(result)
        return False

    def __lt__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.value[i][j] < other.value[i][j])
                return all(result)
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = [[] for i in range(self.length)]
                for i in range(self.length):
                    for j in range(self.height):
                        result[i].append(self.value[i][j] + other.value[i][j])
                return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.length:
                result = [[sum(a * b for a, b in zip(self_row, other_col))
                           for other_col in zip(*other.value)]
                          for self_row in self.value]
            elif self.length == other.height:
                result = [[sum(a * b for a, b in zip(self_col, other_row))
                           for self_col in zip(*self.value)]
                          for other_row in other.value]
            return Matrix(result)
        return False


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix_1, matrix_2, sep='\n\n')
    print(matrix_1 == matrix_2)
    print(matrix_1 == matrix_3)
    print(matrix_1 < matrix_2)
    print(matrix_1 > matrix_2)
    add_matrix = matrix_1 + matrix_2
    print(add_matrix)
    mul_matrix = matrix_1 * matrix_2
    print(mul_matrix)