# dog5.py

class Dog:
    def __init__(self, name, age):
        self.set_name(name) 
        self.set_age(age)
    def set_age(self, new_age):
        self.__age = new_age  # Private attribute
    def get_age(self):
        return self.__age
    def set_name(self, new_name):
        self.__name = new_name # Private attribute
    def get_name(self):
        return self.__name

miles = Dog("Miles",4)
miles.__age
miles._Dog__age
