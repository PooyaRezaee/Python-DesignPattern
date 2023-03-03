"""
    Abstract Factory

        Car :
            brand => [ bmw , benz ]
                type => [ Suv , Coupe ]
                    model => [ ... ]
"""

from abc import  ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass
# ==============================
class Benz(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model
class Bmw(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model
# ==============================
class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass

class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass
# ==============================
# === SUVs
# benc
class Gla(Suv, Benz):
    def creating_suv(self):
        print("this is suv benz gla ....")
class Glc(Suv, Benz):
    def creating_suv(self):
        print("this is suv benz glc ....")
# bmw
class X1(Suv, Bmw):
    def creating_suv(self):
        print("this is suv bmw x1 ....")
class X2(Suv, Bmw):
    def creating_suv(self):
        print("this is suv bmw x2 ....")

# === COUPEs
# benz
class Cls(Coupe,Benz):
    def creating_coupe(self):
        print("this is coupe benz cls ....")
class E_Class(Coupe,Benz):
    def creating_coupe(self):
        print("this is coupe benz E-Class ....")
# bwm
class M2(Coupe,Bmw):
    def creating_coupe(self):
        print("this is coupe bmw m2 ....")
class M4(Coupe,Bmw):
    def creating_coupe(self):
        print("this is coupe bmw m4 ....")
# ==============================

def ClientSuv(corp,model):
    if issubclass(model,corp):
        suv = corp().call_suv(model())
        suv.creating_suv()
    else:
        raise NameError()

def ClientCoupe(corp,model):
    if issubclass(model,corp):
        coupe = corp().call_coupe(model())
        coupe.creating_coupe()
    else:
        raise NameError()



try:
    ClientSuv(Bmw,X1)
except:
    print("Model Not Found")

try:
    ClientCoupe(Bmw,M4)
except:
    print("Model Not Found")


























