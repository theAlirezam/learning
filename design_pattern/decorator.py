class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self, address, user=None):
        self.address = address
        self.user = user
        self.basket_list = []

    def add_to_basket(self, basket):
        if not isinstance(basket, list):
            basket = [basket]
        self.basket_list.extend(basket)

    # self.product = product

    def total_price(self):
        t = 0
        for product in self.basket_list:
            t += product.price
        return t


##########proxy########


VAT = {'iran': 9, 'afghanistan': 20}
COUNTRIES = ['iran', 'afghanistan']


########################## DECORATORS ##############################

def calculate_vat(func):
    def wrapped_func(p):
        vat = VAT[p.address]
        total_price = p.total_price()
        return total_price + total_price * vat / 100

    return wrapped_func


def show_price(p):
    return p.total_price()


@calculate_vat
def show_price_and_vat(p):
    return p.total_price()


####################################################################


p1 = Product('mobile', 1000)
p2 = Product('tablet', 1200)

pur = Purchase(COUNTRIES[1])
pur.add_to_basket([p1, p2])
print(show_price(pur))
print(show_price_and_vat(pur))
