from flask import Response
from json import dumps


class ErrorHandler(Exception):

    def __init__(self, message, key, status_code=400, detail=None):
        self.message = message
        self.key = key
        self.status_code = status_code
        self.detail = detail

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def handle(self):
        error = {
            "success": False,
            "status_code": self.status_code,
            "error": {
                "message": self.message,
                "key": self.key,
                "detail": self.detail
            }
        }

        return Response(dumps(error), status=self.status_code, mimetype='application/json')
