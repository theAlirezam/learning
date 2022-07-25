from random import choice
from user import User
from region import Region
from estate import Apartment, Store
from advertisement import ApartmentSale

firs_names = ['ali', 'hosein', 'amir']
last_names = ['karimi', 'irani', 'movahed']
phone_numbers = ['1234', '5678', '9012', '3456', '7890']


def creat_sample():
    customer_list = list()

    for phone in phone_numbers:
        User(choice(firs_names), choice(last_names), phone_numbers)
        customer_list.append(User)

    for people in User.object_list:
        # print(people.first_name, people.last_name, people.id)
        print(f"{people.full_name}\t " + f"{people.id}".capitalize())

    reg1 = Region(name="Nabard Shomali")
    # apt1 = Apartment(has_elevator=True, has_parking=False, user=customer_list[0],
    #                  region=reg1, area=120, floor=2, address='aslkdjf'
    #                  )
    # apt1.show_description()
    # store = Store(user=customer_list[-1],
    #               region=reg1, area=20, floor=0, address='l;ksasdkj'
    #               )
    # store.show_description()

    apt_sell1 = ApartmentSale(user=customer_list[0], has_elevator=False, has_parking=True,
                              area=20, floor=1, address='jkdsfhkljh', region=reg1,
                              price_per_meter=10, discountable=True, convertable=False
                              )
    apt_sell2 = ApartmentSale(user=customer_list[1], has_elevator=False, has_parking=True,
                              area=25, floor=2, address='jkdsfhkljh', region=reg1,
                              price_per_meter=10, discountable=True, convertable=False
                              )
    apt_sell3 = ApartmentSale(user=customer_list[2], has_elevator=False, has_parking=False,
                              area=30, floor=3, address='jkdsfhkljh', region=reg1,
                              price_per_meter=10, discountable=True, convertable=False
                              )
    apt_sell4 = ApartmentSale(user=customer_list[4], has_elevator=False, has_parking=True,
                              area=40, floor=4, address='jkdsfhkljh', region=reg1,
                              price_per_meter=10, discountable=True, convertable=False
                              )

    search_res = ApartmentSale.manager.search(region=reg1)
    # print(search_res)
