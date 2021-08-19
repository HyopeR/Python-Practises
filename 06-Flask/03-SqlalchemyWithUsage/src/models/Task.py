from src.services.AlchemyService import AlchemyService

db = AlchemyService().db


class Result(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
