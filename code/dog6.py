# dog6.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__: special method returning a string representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
class BorderCollie(Dog):
    pass    

class Bulldog(Dog):
    pass

robert = BorderCollie("Robert",8)
print(robert)
type(robert)
isinstance(robert,BorderCollie)