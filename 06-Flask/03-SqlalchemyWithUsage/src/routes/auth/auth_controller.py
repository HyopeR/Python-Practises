from src.routes.auth.auth_service import AuthService


class AuthController:

    def __init__(self):
        self.AuthService = AuthService()

    def login(self, body):
        email = body.get('email')
        password = body.get('password')

        return self.AuthService.login(email, password)

    def register(self, body):
        return self.AuthService.register(body)
