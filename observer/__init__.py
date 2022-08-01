from shop import Product, Purchase
from notification import EmailNotification
p1 = Product()
p2 = Product()
p3 = Product()
p4 = Product()

purchase = Purchase([p1, p2, p3, p4])
purchase.checkout()
purchase.cancel()

# EmailNotification.send('purchase paid')
