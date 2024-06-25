# dog4.py

class Dog:
    def __init__(self, name, age):
        self._name = name # Atributo privado
        self._age = age # Atributo privado

    def set_name(self, new_name):
        self._name = new_name
    
    def get_name(self):
        return self._name
    
    def set_age(self, new_age):
        self._age = new_age
    
    def get_age(self):
        return self._age

miles = Dog("Miles",4)
miles._age = 6 # Acceso no recomendado
miles._age # Acceso no recomendado
miles.set_age(7) # Acceso recomendado
miles.get_age() # Acceso recomendado
