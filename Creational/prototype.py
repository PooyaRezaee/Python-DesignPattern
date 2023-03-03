"""
    Prototype
        Clone a objects
            - Common parts in a space
            - diffrend parts in another space
"""

from copy import deepcopy

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class prototype:
    def __init__(self):
        self._objects = {}

    def register(self,name,obj):
        self._objects[name] = obj

    def unregister(self,name):
        del self._objects[name]

    def clone(self,_name,**kwargs):
        clonedObj = deepcopy(self._objects.get(_name))
        clonedObj.__dict__.update(kwargs)
        return clonedObj

p1 = Person('pooya',32)
pro1 = prototype()
pro1.register('p1',p1)
p1_copy = pro1.clone('p1',name='23')

print(p1.name is p1_copy.name)