class Animal:
    def __init__(self, name, species):
        self.species = species
        self.name = name

    def display_info(self):
        return print(f"Animal: {self.name}\nSpecies: {self.species}")


class Mammal(Animal):
    def __init__(self, name, species, diet_type):
        super().__init__(name, species)
        self.diet_type = diet_type

    def display_info(self):
        return print(f"Animal: {self.name}\nSpecies: {self.species}\nDiet type: {self.diet_type}")


class Carnivore(Mammal):
    def __init__(self, name, species, diet_type, teeth_count):
        super().__init__(name, species, diet_type)
        self.teeth_count = teeth_count

    def display_info(self):
        return print(
            f"Animal: {self.name}\n"
            f"Species: {self.species}\n"
            f"Diet type: {self.diet_type}\n"
            f"Teeth count: {self.teeth_count}"
                     )


class Lion(Carnivore):
    def __init__(self, name, species, diet_type, teeth_count, mane_size):
        super().__init__(name, species, diet_type, teeth_count)
        self.mane_size = mane_size

    def display_info(self):
        return print(
            f"Animal: {self.name}\n"
            f"Species: {self.species}\n"
            f"Diet type: {self.diet_type}\n"
            f"Teeth count: {self.teeth_count}\n"
            f"Mane size: {self.mane_size}"
                     )


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")
animal = Animal("Cat", "Cat")
animal.display_info()
print(30*"-")
mammal.display_info()
print(30*"-")
carnivore.display_info()
print(30*"-")
lion.display_info()
