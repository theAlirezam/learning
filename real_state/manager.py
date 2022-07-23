class Manager:

    def __init__(self, _class=None):
        self._class = _class

    def search(self, **kwargs):
        search_list = list()
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    search_list.append(obj)
        return search_list

