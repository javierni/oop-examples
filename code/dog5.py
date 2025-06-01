# dog5.py

class Dog:
    def __init__(self, name, age):
        self.__name = name # Private attribute
        self.__age = age # Private attribute
    def set_age(self, new_age):
        self.__age = new_age
    def get_age(self):
        return self.__age
    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name

miles = Dog("Miles",4)
miles.__age
miles._Dog__age
