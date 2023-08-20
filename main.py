"""
Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
Забезпечте методи для доступу до цих властивостей та встановлення їх значень.
"""


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name
        return name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age
        return age

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())
print(person.get_age())

        
