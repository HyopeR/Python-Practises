from flask import Response
from json import dumps


class DataHandler(object):

    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, indent=4)

    def handle(self):
        error = {
            "success": True,
            "status_code": self.status_code,
            "data": self.data,
        }

        return Response(dumps(error), status=self.status_code, mimetype='application/json')
