from src.core.metaclass.Singleton import Singleton
from src.helpers.error.ErrorDescriptive import ErrorDescriptive


class ErrorService(ErrorDescriptive, metaclass=Singleton):
    def __init__(self):
        super(ErrorService, self).__init__()

    def initialize(self):
        return ErrorService()