"""
    Builder
        - Director
            . set Builder
            . get Object
        - Main Object
            . Set Detail
            . Methods
        - Builder
            . set abstract method for Get each part Object
        - Type Of Main Objects
            . Return each part Object with Get.. method
        - Small Parts of Objects


"""
from abc import ABC,abstractmethod

class Director:
    __builder = None

    def setBuilder(self,builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        wheel = self.__builder.getWheel()
        car.setWheel(wheel)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        return car

class Car:
    def __init__(self):
        self.__body = None
        self.__engine = None
        self.__wheel = None

    def setWheel(self,wheel):
        self.__wheel = wheel

    def setBody(self,body):
        self.__body = body

    def setEngine(self,engine):
        self.__engine = engine

    def detail(self):
        print(f"Shape Body Is {self.__body.shape}")
        print(f"Engine Is {self.__engine.hp} HP")
        print(f"Wheel Is {self.__wheel.size} Inch")


class Builder(ABC):
    @abstractmethod
    def getEngine(self):
        pass

    @abstractmethod
    def getWheel(self):
        pass

    @abstractmethod
    def getBody(self):
        pass

class Benz(Builder):
    def getEngine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getBody(self):
        body = Body()
        body.shape = 'suv'
        return body


class Bmw(Builder):
    def getEngine(self):
        engine = Engine()
        engine.hp = 620
        return engine

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 26
        return wheel

    def getBody(self):
        body = Body()
        body.shape = 'coupe'
        return body


class Body:
    shape = None

class Engine:
    hp = None

class Wheel:
    size = None


car1 = Bmw()
director = Director()
director.setBuilder(car1)
b1 = director.getCar()
b1.detail()