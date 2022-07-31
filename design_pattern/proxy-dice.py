import random


class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)


class User:
    pass


class Game:
    def __init__(self, u1, u2):
        self.user1 = u1
        self.user2 = u2
        self.turn = u1
        self.dice = Dice

    def change_turn(self):
        self.turn = self.user2 if self.turn == self.user1 else self.user1


def check_turn_and_roll(game, user):
    if game.turn == user:
        game.change_turn()
        return game.dice.roll()
    return 'its not ur turn'


user1 = User()
user2 = User()

game = Game(user1, user2)
"""
print(check_turn_and_roll(game, user2))
print(check_turn_and_roll(game, user2))
print(check_turn_and_roll(game, user1))
print(check_turn_and_roll(game, user1))
print(check_turn_and_roll(game, user2))
print(check_turn_and_roll(game, user1))
"""

##################### LAZY LOADER ########################


from time import sleep


class Lazy:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class A:
    def __init__(self):
        sleep(10)

    # @staticmethod
    def connect(self):
        return "A connecting"


class B:
    def __init__(self):
        sleep(6)

    def show(self):
        return "B showing"


b = Lazy(B)
# b = Lazy(A)
print(b.show())
# print(b.connect())

