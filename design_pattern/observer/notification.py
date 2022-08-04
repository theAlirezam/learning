from abc import ABC, abstractmethod


class Observer(ABC):
    @staticmethod
    @abstractmethod
    def send(message=''):
        pass


class EmailNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"Email notif {message}")


class PushNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"Push notif {message}")


class SMSNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"SMS notif {message}")
