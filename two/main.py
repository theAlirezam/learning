from two import all_models

c1 = all_models.Customer('ali', 'karimi', 123)
c2 = all_models.Customer('saeed', 'alavi', 456)

p1 = all_models.Products(1, 'milk', 1000)
p2 = all_models.Products(2, 'tea', 0)

print(c1)

if p2.is_free():
    print(p1.product_name + f' is FREE!')
