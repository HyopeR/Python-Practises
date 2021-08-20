from src.core.metaclass.Singleton import Singleton


class ModelService(metaclass=Singleton):
    metadata = None

    def initialize(self, metadata):
        print(metadata)
        self.metadata = metadata

    def getModel(self):
        for i in self.metadata:
            print(i)
