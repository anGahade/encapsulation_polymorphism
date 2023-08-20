"""
Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку.
Зробіть так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120.
При спробі встановити недійсне значення, виведіть повідомлення про помилку.
"""


class Person:

    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
            return name
        else:
            return "І'мя повинно складатись лише з літер!"

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
            return age
        else:
            return "Вкажіть справжній вік"

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())
print(person.get_age())

print(person.set_name("John43"))
print(person.set_age(-9))
