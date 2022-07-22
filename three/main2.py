from _ast import arg
from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, floor, elevator, *args, **kwargs):
        self.floor = floor
        self.elevator = elevator
        super().__init__(*args, **kwargs)  # PASS THE FUNCTION TO THE NEXT FUNCTION

    @abstractmethod
    def apartabs(self):
        pass


class House:
    def __init__(self, age):
        self.age = age


class Rent(ABC):
    def __init__(self, fixed, monthly):
        self.fixed = fixed
        self.monthly = monthly


class Sale(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def permission(self):
        pass


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"floor: {self.floor} price: {self.price}".upper()

    def permission(self):
        pass

    def apartabs(self): pass


class ApartmentRent(Apartment, Rent):
    pass


apartemensale = ApartmentSale(5, True, 12000)
# print(apartemensale.permission())

print(apartemensale)

