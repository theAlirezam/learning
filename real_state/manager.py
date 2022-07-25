class Manager:

    def __init__(self, _class=None):
        self._class = _class

    def search(self, **kwargs):

        search_list = list()

        for key, value in kwargs.items():
            if key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            elif key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            else:
                compare_key = 'equal'

            for obj in self._class.object_list:
                if hasattr(obj, key):

                    if compare_key == 'max':
                        result = getattr(obj, key) <= value
                    elif compare_key == 'min':
                        result = getattr(obj, key) >= value
                    else:
                        result = getattr(obj, key) == value
                    if result:
                        search_list.append(obj)
        return search_list

        # for key, value in kwargs.items():
        #     if key.endswith('__max'):
        #         key = key[:-5]
        #
        #         for obj in self._class.object_list:
        #             print(self._class.object_list)
        #             if hasattr(obj, key):
        #                 result = getattr(obj, key) <= value
        #                 if result:
        #                     search_list.append(obj)
        #
        #     elif key.endswith('__min'):
        #         key = key[:-5]
        #         for obj in self._class.object_list:
        #             if hasattr(obj, key):
        #                 result = getattr(obj, key) >= value
        #
        #                 if result:
        #                     search_list.append(obj)
        #
        #     else:
        #         for obj in self._class.object_list:
        #             if hasattr(obj, key):
        #                 result = getattr(obj, key) == value
        #
        #                 if result:
        #                     search_list.append(obj)
        #
        # return search_list

    def count(self):
        return len(self._class.object_list)
