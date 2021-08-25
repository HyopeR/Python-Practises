from src.core.metaclass.Singleton import Singleton
from src.core.parentclass.Service import Service
from src.utils.decorators.service_interceptor import service_interceptor
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from passlib.hash import sha256_crypt
from typing import Dict


class UserService(Service, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.User, = self.getModels(["User"])
        self.user_schema, self.users_schema = self.getSchemas(["User", "Users"])

    @service_interceptor(ErrorDescriptive.user_get.key)
    def get(self):
        data = self.User.query.all()

        return self.users_schema.dump(data)

    @service_interceptor(ErrorDescriptive.user_get_one.key)
    def get_one(self, id):
        find_user = self.User.query.filter_by(id=id).first()

        return self.user_schema.dump(find_user)

    @service_interceptor(ErrorDescriptive.user_update.key)
    def put(self, id, body: Dict):
        password = body.get('password')

        if password:
            password = sha256_crypt.encrypt(password)
            body['password'] = password

        update = self.User.query.filter_by(id=id).update(body, synchronize_session='fetch')
        updated_user = self.User.query.filter_by(id=id).first()
        self.db.session.commit()

        return self.user_schema.dump(updated_user)

    @service_interceptor(ErrorDescriptive.user_delete.key)
    def delete(self, id):

        user = self.User.query.filter_by(id=id).first()
        self.db.session.delete(user)
        self.db.session.commit()

        return self.user_schema.dump(user)
