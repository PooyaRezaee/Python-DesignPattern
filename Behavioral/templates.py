"""
    Templates Method
        - like Mixins
"""
from abc import  ABC,abstractmethod

class Animal(ABC):
    def detail(self):
        self.live()
        self.sound()
        self.foot()
        self.height()

    def live(self):
        print(f"{self} Is live")

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def foot(self):
        pass

    def height(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Cat Say mu mu ...")

    def foot(self):
        print("Cat have 4 foot")

    def __str__(self):
        return "Cat"


class Bird(Animal):
    def sound(self):
        print("Bird Say jik jik ...")

    def foot(self):
        print("Bird Have Two foot")

    def height(self):
        print("Bird Fly To 50m")

    def __str__(self):
        return "Bird"

cat = Cat()
cat.detail()

# bird = Bird()
# bird.detail()