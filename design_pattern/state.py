from abc import ABC, abstractmethod


class Message:
    def __init__(self, subject, message, sender):
        self.subject = subject
        self.message = message
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_user):
        if to_user.__class__ not in self.current.allowed:
            print(f"{self.current.__class__} is not allowed to send msg to {to_user.__class__}")
        else:
            self.flow.append(to_user)
            print(f"msg send to {to_user}")


class AbstractUser(ABC):
    @property
    @abstractmethod
    def allowed(self):
        pass


class Manager(AbstractUser):
    allowed = []


class Superviser(AbstractUser):
    allowed = [Manager]


class Client(AbstractUser):
    allowed = [Superviser]


if __name__ == "__main__":
    mng = Manager()
    sp = Superviser()
    cl = Client()

    msg = Message('issue', 'Hi', cl)

    msg.send(sp)
    msg.send(mng)
    msg.send(sp)
