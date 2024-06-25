# shapes.py
from abc import ABC, abstractmethod
from math import pi

# clase abstracta: no hay instancias directas​
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass # método abstracto que se debe redefinir en subclase
    @abstractmethod
    def get_perimeter(self):
        pass
    def __str__(self):
        return f"object with area {self.get_area()} and perimeter {self.get_perimeter()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return pi * self.radius ** 2
    def get_perimeter(self):
        return 2 * pi * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def get_area(self):
        return self.side ** 2
    def get_perimeter(self):
        return 4 * self.side

shape_a = Circle(100)
print(shape_a)

    
