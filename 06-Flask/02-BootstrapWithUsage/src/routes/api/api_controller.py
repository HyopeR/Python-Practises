from src.core.handlers.DataHandler import DataHandler

class ApiController:

    def __init__(self):
        pass

    def get(self):
        return DataHandler({"app": "Flask"}).handle()

    def post(self, data):
        return DataHandler(data).handle()