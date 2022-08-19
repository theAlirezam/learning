import json
from abc import ABC, abstractmethod


class StorageBase(ABC):

    @abstractmethod
    def store(self, data, *args):
        pass


class MongoStorage(StorageBase):

    def store(self, data, *args):
        pass


class FileStorage(StorageBase):

    def store(self, data, filename, *args):
        with open(f"files/{filename}.json", 'w') as f:
            f.write(json.dumps(data))
            print(f"files/{filename}.json")

    def load(self, filename):
        with open(f"files/{filename}.json, 'r") as f:
            data = json.loads(f.read())

            print('reading ' + filename)
            return data
