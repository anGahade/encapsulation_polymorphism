from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    @abstractmethod
    def display_info(self):
        pass


class Sedan(Car):
    def __init__(self, model, brand, doors_count):
        super().__init__(model, brand)
        self.doors_count = doors_count

    def display_info(self):
        return print(f"Car: {self.model} {self.brand}\n"
                     f"Doors: {self.doors_count}")


class SUV(Car):
    def __init__(self, model, brand, passenger_seats):
        super().__init__(model, brand)
        self.passenger_seats = passenger_seats

    def display_info(self):
        return print(f"Car: {self.model} {self.brand}\n"
                     f"Seats: {self.passenger_seats}")


class SportsCar(Car):
    def __init__(self, model, brand, max_speed):
        super().__init__(model, brand)
        self.max_speed = max_speed

    def display_info(self):
        return print(f"Car: {self.model} {self.brand}\n"
                     f"Max Speed: {self.max_speed} km/h")


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

sedan.display_info()
print(35*"-")
suv.display_info()
print(35*"-")
sports_car.display_info()
print(35*"-")
