from abc import ABC
from base import BaseClass


class Sell(ABC):
    def __init__(self, price_per_meter, discountable, convertable, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price per meter: {self.price_per_meter}\t convertable: {self.convertable}")


class Rent(ABC):
    def __init__(self, initial_price, monthly_price):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        super().__init__()
