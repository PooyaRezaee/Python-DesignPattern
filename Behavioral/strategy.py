"""
    Strategy
"""
from abc import ABC,abstractmethod

class Context:
    def __init__(self,direction,text):
        self._direction = direction
        self.text = text

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self,dir):
        self._direction = dir

    def sorting(self):
        return self._direction.direct(self.text)

class Direction(ABC):

    @abstractmethod
    def direct(self,data):
        pass

class Right(Direction):
    def direct(self,data):
        print(data[::-1])

class Left(Direction):
    def direct(self,data):
        print(data)


c1 = Context(Right(),'Sample Text ...')
c1.sorting()