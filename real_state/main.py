from sample import creat_sample
from advertisement import *


class Handler:
    ADVERTISEMENT_TYPES = {
        1: ApartmentSale
    }

    SWITCHES = {
        'r': 'report',
        's': 'show'
    }

    def report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            # print(adv, adv.manager.count())
            for obj in adv.object_list:
                print(obj.show_detail())

    def run(self):
        for key in self.SWITCHES:
            print(f"select {key} to {self.SWITCHES[key]}")

        user_input = input(f'Enter your choice:\t'.capitalize())
        switch = self.SWITCHES.get(user_input, None)


        choice = getattr(self, switch, None)
        choice()
        self.run()


creat_sample()
hand = Handler()

hand.run()
