from random import choice
from user import User
from region import Region
from estate import Apartment, Store
from advertisement import ApartmentSale

firs_names = ['ali', 'hosein', 'amir']
last_names = ['karimi', 'irani', 'movahed']
phone_numbers = ['1234', '5678', '9012', '3456', '7890']

customer_list = list()

for phone in phone_numbers:
    User(choice(firs_names), choice(last_names), phone_numbers)
    customer_list.append(User)

for people in User.object_list:
    # print(people.first_name, people.last_name, people.id)
    print(f"{people.full_name}\t {people.id}".rjust(20))

reg1 = Region(name="Nabard Shomali")
apt1 = Apartment(has_elevator=True, has_parking=False, user=customer_list[0],
                 region=reg1, area=120, floor=2, address='aslkdjf'
                 )
apt1.show_description()
store = Store(user=customer_list[-1],
              region=reg1, area=20, floor=0, address='l;ksasdkj'
              )
store.show_description()

apt_sell = ApartmentSale(False, True, user=customer_list[-2], region=reg1,
                         area=230, floor=3, address='jkdsfhkljh',
                         price_per_meter=10, discountable=True, convertable=False
                         )

apt_sell.show_detail(str(customer_list[-2]))
