from base import BaseClass


class User(BaseClass):
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        super().__init__()

    @property
    def full_name(self):
        return f"{self.first_name} ".capitalize() + f"{self.last_name}".capitalize()
