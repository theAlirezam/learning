class User:
    def __init__(self, user_name, user_id, password):
        self.user_name = user_name
        self.user_id = user_id
        self.password = password

    def check_password(self, password):
        return self.password == password

    def __str__(self):
        return f"\n{self.user_name}: {str(self.user_id)}"

    @property
    def pswrd(self):
        pass

    @classmethod
    def hi(cls):
        pass

    @staticmethod
    def hello(ji):
        pass


class Customer(User):

    customer_list = list()

    def __init__(self, user_name, customer_id, password):
        super().__init__(user_name, customer_id, password)

        Customer.customer_list.append(self)


class Products:

    def __init__(self, upc, product_name, price):
        self.upc = upc
        self.product_name = product_name
        self.price = price

    def is_free(self):
        return self.price == 0


class Reseller(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
