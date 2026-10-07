# abstractFactory.py

from abc import ABC, abstractmethod


class CarPart(ABC):
    pass

class CarEngine(CarPart, ABC):
    pass

class FordEngine(CarEngine):
    pass

class ToyotaEngine(CarEngine):
    pass

class PorscheEngine(CarEngine):
    pass

class CarBody(CarPart, ABC):
    pass

class FordBody(CarBody):
    pass

class ToyotaBody(CarBody):
    pass

class PorscheBody(CarBody):
    pass

class Car(ABC):
    def get_engine(self) -> CarEngine:
        return self._engine
    def set_engine(self, engine: CarEngine) -> None:
        self._engine = engine
    def get_body(self) -> CarBody:
        return self._body
    def set_body(self, body: CarBody) -> None:
        self._body = body

class FordCar(Car):
    pass

class ToyotaCar(Car):
    pass

class PorscheCar(Car):
    pass

class CarPartFactory(ABC):
    @abstractmethod
    def makeCar() -> Car:
        pass
    @abstractmethod
    def makeBody() -> CarBody:
        pass
    @abstractmethod
    def makeEngine() -> CarEngine:
        pass

class ToyotaFactory(CarPartFactory):
    def makeCar() -> Car:
        return ToyotaCar()
    def makeBody() -> CarBody:
        return ToyotaBody()
    def makeEngine() -> CarEngine:
        return ToyotaEngine()

class Client:
    def __init__(self, factory:CarPartFactory):
        self._factory = factory
    def create_car(self) -> Car: # simpler code with abstract factory
        car = self._factory.makeCar()
        car.set_engine(self._factory.makeEngine())
        car.set_body(self._factory.makeBody())
        return car

client = Client(ToyotaFactory)
car = client.create_car()
print(car, type(car), car.get_engine(), car.get_body())