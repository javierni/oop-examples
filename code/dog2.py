# dog2.py

class Dog:
    # Identation to indicate that an attribute/method belongs to the class
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
miles.name
buddy.name
buddy.species
Dog.species = "Perro"
buddy.species