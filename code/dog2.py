# dog2.py

class Dog:
    # Utilizar identación para indicar que un atributo/método pertenece a la clase​
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