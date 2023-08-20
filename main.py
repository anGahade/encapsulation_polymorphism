"""
Розробіть клас "Square", який успадковує властивості і методи з класу "Rectangle".
Додайте властивість side_length (довжина сторони) і перевизначте методи,
які використовують властивості width і height класу "Rectangle",
щоб вони використовували властивість side_length класу "Square".
Виведіть значення ширини, висоти і довжини сторони для об'єкта класу "Square".
"""


class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        return print(f"Color: {self.color}")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_color(self):
        super().display_color()
        # return print(f"Color: {self.color}, Width: {self.width}, Height: {self.height}")

    def width(self):
        return self.width()

    def height(self):
        return self.height()


class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.side_length = side_length

    def get_side_length(self):
        return self.side_length


square = Square("Green", 8)
square.display_color() # Виведе "Color: Green"
print(square.width) # Виведе 8
print(square.height) # Виведе 8
print(square.side_length) # Виведе 8



