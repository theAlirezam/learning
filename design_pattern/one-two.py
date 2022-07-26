# Singleton
from abc import ABC, abstractmethod


class SingleTone:
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


# Abstract Factory

class ProductBase(ABC):

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass


class Fruits(ProductBase):
    def __init__(self, name, price):
        self._name = name
        self.kprice = price

    @property
    def detail(self):
        return FruitsDetail(self)

    @property
    def price(self):
        return FruitsPrice(self)


class FruitsPrice(DetailBase):
    def __init__(self, fruit):
        self.fruit = fruit

    def show(self):
        print(f"price: {self.fruit.kprice}")


class FruitsDetail(DetailBase):
    def __init__(self, fruit):
        self.fruit = fruit

    def show(self):
        print(f"detail = {self.fruit._name}")


f1 = Fruits('apple', 10)
f2 = Fruits('banana', 20)

for f in [f1, f2]:
    print(f.detail.show())
    print(f.price.show())
