"""
Створіть базовий клас "Shape" (фігура), який має властивість color (колір)
і метод display_color() для виведення коліру фігури.
Створіть похідний клас "Rectangle" (прямокутник), який наслідує властивість color
і додає властивості width (ширина) і height (висота).
Забезпечте можливість встановлення значень ширини і висоти прямокутника та виведення їх значень.
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
        # return print(f"Color: {self.color}")

    def width(self):
        return self.width()

    def height(self):
        return self.height()


shape = Shape("Red")
shape.display_color() # Виведе "Color: Red"
rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color() # Виведе "Color: Blue"
print(rectangle.width) # Виведе 10
print(rectangle.height) # Виведе 5


