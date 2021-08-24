from src.core.metaclass.Singleton import Singleton
from src.core.parentclass.Service import Service
from src.core.decorators.service_interceptor import service_interceptor
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from dateutil.relativedelta import relativedelta
from datetime import datetime
from src.services.EnvironmentService import EnvironmentService
from typing import Dict
from passlib.hash import sha256_crypt
import jwt


class AuthService(Service, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.User, = self.getModels(["User"])
        self.user_schema, = self.getSchemas(["User"])

    @service_interceptor(ErrorDescriptive.login_error.key)
    def login(self, email, password):
        print(password)
        user = self.User.query.filter_by(email=email).first()

        if user is None:
            raise Exception('Email address not found.')

        if sha256_crypt.verify(password, user.password):
            raise Exception('Password incorrect.')

        date = datetime.now() + relativedelta(years=1)
        token = jwt.encode({"exp": date}, EnvironmentService().get_one('SECRET_KEY'), algorithm="HS256")

        data = self.user_schema.dump(user)
        data["token"] = token
        return data

    @service_interceptor(ErrorDescriptive.register_error.key)
    def register(self, body: Dict):
        password = sha256_crypt.encrypt(body.get('password'))
        body['password'] = password

        user = self.User(**body)
        self.db.session.add(user)
        self.db.session.commit()

        date = datetime.now() + relativedelta(years=1)
        token = jwt.encode({"exp": date}, EnvironmentService().get_one('SECRET_KEY'), algorithm="HS256")

        data = self.user_schema.dump(user)
        data["token"] = token

        return data
