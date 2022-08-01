from notification import *
from decorator import notify_observer


class Product:
    pass


class Purchase:
    observer = [EmailNotification, SMSNotification, PushNotification]

    def __init__(self, product_list):
        self.product_list = product_list
        self.is_payed = False

    @notify_observer('purchase paid')
    def checkout(self):
        self.is_payed = True

    @notify_observer('purchase cancel')
    def cancel(self):
        self.is_payed = False
