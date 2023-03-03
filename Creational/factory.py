"""
    Factory method
        We Have 3 Method
            1. Product
            2. Client
            3. Creator
"""
from abc import  ABC,abstractmethod

class Creator(ABC): # Main Creator
    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        resualt = product.edit()
        return  resualt

class JsonCreator(Creator): # Special Creator
    def make(self):
        return Json()

class XmlCreator(Creator): # Special Creator
    def make(self):
        return Xml()

class Product(ABC): # Main Product
    @abstractmethod
    def edit(self):
        pass

class Json(Product): # Special Produc
    def edit(self):
        return 'Editing Json File ...'

class Xml(Product): # Special Produc
    def edit(self):
        return 'Editing Xml File ...'

def client(format): # Client
    return  format.call_edit()

print(client(XmlCreator()))