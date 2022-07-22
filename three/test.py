from abc import ABC, abstractmethod


class Oil(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def say_hi(self):
        print('Hi')


class Engine():
    pass


class Car(Engine):

    def run(self):
        print("running...")



class Motorcycle(Oil):

    def run_motor(self):
        print("running...")

    def say_hi(self): pass


class benz(Car, Motorcycle):
    def drive(self):
        print('im driving')


b = benz()
b.drive()
