from estate import Store, Apartment, House
from deal import Rent, Sell
from base import BaseClass


class ApartmentSale(BaseClass, Apartment, Sell):

    def show_detail(self):
        self.show_description()
        self.show_price()
