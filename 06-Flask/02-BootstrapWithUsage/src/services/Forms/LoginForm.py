from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField("Username", validators=[
        DataRequired(message='Name cannot be empty.')
    ])

    password = PasswordField("Password", validators=[
        DataRequired(message='Surname cannot be empty.')
    ])
