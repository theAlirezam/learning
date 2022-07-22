from base import BaseClass


class Region(BaseClass):
    def __init__(self, name):
        self.name = name
        super().__init__()
