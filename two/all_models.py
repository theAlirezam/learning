class Customer:
    customer_list = list()

    def __init__(self, name, last_name, customer_id):
        self.name = name
        self.lastname = last_name
        self.customer_id = customer_id

    def __str__(self):
        return f"{self.name}\t" + str(self.customer_id)


class Products:

    def __init__(self, upc, product_name, price):
        self.upc = upc
        self.product_name = product_name
        self.price = price

    def is_free(self):
        return self.price == 0
