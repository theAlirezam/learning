from factory import Fruits


class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, p):
        return self.rate * p.kprice


adp = PriceAdapter(30000)

f1 = Fruits('apple', 20)
f2 = Fruits('pineapple', 30)

for f in [f1, f2]:
    print(adp.exchange(f))
