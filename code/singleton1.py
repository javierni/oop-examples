# singleton1.py

class Singleton:
    _instance = None

    def __new__(cls):
        # __new__ method is responsible for creating a new instance
        # we redefine it to control the creation of a unique instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls):
        return cls()

    def doSomething(self):
        print(self)

a = Singleton.getInstance()
b = Singleton()
print (a is b) # Expected value: True
print(a)
print(b)