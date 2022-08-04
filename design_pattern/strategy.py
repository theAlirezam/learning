class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Gateway:
    def __init__(self, name):
        self.name = name


class Payment:
    gateways = (Gateway('G1'), Gateway('G2'))

    def __init__(self, purchase):
        self.purchase = purchase

    def get_gateway(self):
        return self.gateways[0] if self.purchase.total_price < 100 else self.gateways[1]

    def pay(self):
        gateway = self.get_gateway()
        print(gateway)


class Purchase:
    def __init__(self):
        self.products = list()
        self.payment = Payment(self)

    def add(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def checkout(self):
        self.payment.pay()


if __name__ == "__main__":
    pur = Purchase()
    p1 = Product('p1', 50)

    p2 = Product('p2', 40)

    p3 = Product('p3', 38)

    pur.add(p1)
    print(pur.total_price())
    pur.checkout()
    pur.add(p2)
    print(pur.total_price())
    pur.checkout()

    pur.add(p3)
    print(pur.total_price())
    pur.checkout()
