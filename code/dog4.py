# dog4.py

class Dog:
    def __init__(self, name, age):
        self._name = name # Private attribute
        self.set_age(age)

    def set_age(self, new_age):
        self._age = new_age  # Private attribute
    
    def get_age(self):
        return self._age

miles = Dog("Miles",4)
miles._age = 6 # Not recommended access
miles._age # Not recommended access
miles.set_age(7) # Recommended access
miles.get_age() # Recommended access
