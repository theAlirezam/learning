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
        return self.gateways[0] if self.purchase.total_price() < 100 else self.gateways[1]

    def pay(self):
        gateway = self.get_gateway()
        print(gateway.name)


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
######################################################################
from abc import ABC, abstractmethod

ALLOWED_EXTENSIONS = ['txt', 'html', 'mp4', 'mp3']


class AbstractRenderer(ABC):
    @abstractmethod
    def render(self):
        pass


class HTMLRenderer(AbstractRenderer):
    def render(self):
        print('rendering from HTML')


class MP4Renderer(AbstractRenderer):
    def render(self):
        print('rendering from mp4')


class MP3Renderer(AbstractRenderer):
    def render(self):
        print('rendering from mp3')


class TXTRenderer(AbstractRenderer):
    def render(self):
        print('rendering from txt')


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    handler_dict = {
        'html': HTMLRenderer,
        'mp4': MP4Renderer,
        'mp3': MP3Renderer,
        'txt': TXTRenderer
    }

    @property
    def extension(self):
        p = self.filename.split('.')[-1]
        return p

    @classmethod
    def create(cls, filename):
        if filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            print(f"error: File extension {filename} not allowed")

        return cls(filename)

    def render(self):

        handler = FileHandler.handler_dict[self.extension]
        return handler().render()


if __name__ == "__main__":
    f1 = FileHandler.create('aasdfa.pdf')
    f11 = FileHandler.create('aasdfa.pdlf')
    f2 = FileHandler.create('acasdfa.html')
    f3 = FileHandler.create('aasddfa.mp3')
    f4 = FileHandler.create('aasdsfa.txt')

    files = [f2, f3, f4]

    for file in files:
        file.render()
