"""
Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод display_color().
В методі display_color() виведіть повідомлення про колір прямокутника
і додайте також виведення повідомлення про його розміри (ширину і висоту)
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
        # super().display_color()
        return print(f"Color: {self.color}, Width: {self.width}, Height: {self.height}")

    def width(self):
        return self.width()

    def height(self):
        return self.height()


rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color() # Виведе "Color: Blue, Width: 10, Height: 5"


