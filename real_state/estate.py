from base import BaseClass
from abc import abstractmethod


class EstateAbstract(BaseClass):
    def __init__(self, user, region, area, floor, address, *args, **kwargs):
        self.user = user
        self.region = region
        self.area = area
        self.floor = floor
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"apartment {self.id} floor:{self.floor}".capitalize())


class House(EstateAbstract):
    def __init__(self, built_year, has_yard, *args, **kwargs):
        self.built_year = built_year
        self.has_yard = has_yard
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"house {self.id}".capitalize())


class Store(EstateAbstract):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"store {self.id}".capitalize())
