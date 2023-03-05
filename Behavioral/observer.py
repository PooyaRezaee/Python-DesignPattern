"""
    Observer
        - if Changed data Send Notif to all observers
"""

class Observer:
    def __init__(self):
        self._observers = []

    def attach(self,observer):
        self._observers.append(observer)

    def notiy(self):
        for observer in self._observers:
            observer.update(self)

class Product(Observer):
    def __init__(self,name,count):
        super().__init__()
        self.name = name
        self._count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
        self.notiy()

class Signal1:
    def update(self,subject):
        print(f"signal 1 : {subject.name} Changed !")

class Signal2:
    def update(self,subject):
        print(f"Signal 2 : {subject.name} Changed To {subject.count}")

# Subjects : List Of Products
products = {
    "1": Product('Speacker', 5),
    "2": Product('Monitor', 5),
}

# Observers : List of signals
signals = [Signal1(),Signal2()]

# Register Signals on Products
for product in products.values():
    for signal in signals:
        product.attach(signal)

# Change Count Products
products['1'].count -= 1
# products['2'].count += 2