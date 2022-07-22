from estate import Store, Apartment, House
from deal import Rent, Sell


class ApartmentSale(Apartment, Sell):
    def show_detail(self, username):
        self.show_description()
        print(username)
