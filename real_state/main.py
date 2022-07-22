from random import choice
from user import User

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
