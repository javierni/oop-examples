# car.py

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


def create_car(brand: str) -> Car:
    if brand == 'ford':
        car = FordCar()
    elif brand == 'toyota':
        car = ToyotaCar()
    else:
        car = PorscheCar();
    if brand == 'ford':
        engine = FordEngine()
    elif brand == 'toyota':
        engine = ToyotaEngine()
    else:
        engine = PorscheEngine()
    car.set_engine(engine)
    if brand == 'ford':
        body = FordBody()
    elif brand == 'toyota':
        body = ToyotaBody()
    else:
        body = PorscheBody()
    car.set_body(body)
    return car

car = create_car('porsche')
print(car, type(car), car.get_engine(), car.get_body())