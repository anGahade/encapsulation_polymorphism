"""
Розробіть клас "Car", який містить такі властивості:
make (марка автомобіля), model (модель автомобіля), year (рік випуску автомобіля) і mileage (пробіг автомобіля).
Забезпечте можливість доступу до цих властивостей через методи, а також зробіть властивості "make" і "model" приватними.
Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане значення.
Перевірте, чи не перевищує пробіг заданий ліміт (наприклад, 300 000 км),
і виведіть повідомлення про досягнення ліміту при спробі здійснити поїздку.
"""


class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, miles_driven):
        self.mileage = self.mileage + miles_driven
        if self.mileage >= 250000:
            print(f"Бобик сдох, далі не поїду, дзвони у сервіс, бо мій пробіг вже: {self.mileage} км")
        else:
            print(f"Загальний пробіг становить: {self.mileage} км")


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make()) # Виведе "Toyota"
print(car.get_model()) # Виведе "Camry"
print(car.get_year()) # Виведе 2020
print(car.get_mileage()) # Виведе 5000
car.drive(100) # Збільшення пробігу на 100
car.drive(300000000) # Виведе повідомлення про досягнення ліміту