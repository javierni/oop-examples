# picture.py
from abc import ABC, abstractmethod

# abstract class
class Graphic(ABC):
    @abstractmethod
    def draw(self)->None:
        pass # abstract method

class Circle(Graphic):
    def draw(self)->None:
        print(type(self))

class Line(Graphic):
    def draw(self)->None:
        print(type(self))

class Picture(Graphic):
    def __init__(self):
        self._children = list()

    def add(self, graphic: Graphic)->None:
        self._children.append(graphic)

    def remove(self, graphic: Graphic)->None:
        self._children.remove(graphic)

    def draw(self)->None:
        print(self,": ")
        for graphic in self._children:
            graphic.draw()

c = Circle()
l = Line()
p = Picture()
p.add(c)
p.add(l)
p.draw()
p.remove(c)
p.draw()
p.remove(l)
p.draw()
g = Graphic()


    
