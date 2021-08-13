from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    name = StringField("Name", validators=[
        DataRequired(message='Name cannot be empty.'),
        Length(min=3, max=25, message='The number of characters cannot be less than 3 and greater than 25.')
    ])

    surname = StringField("Surname", validators=[
        DataRequired(message='Surname cannot be empty.'),
        Length(min=3, max=25, message='The number of characters cannot be less than 3 and greater than 25.')
    ])

    email = EmailField("Email", validators=[
        DataRequired(message='Email cannot be empty.'),
        Email(message='Incorrect email address.')
    ])

    username = StringField("Username", validators=[
        DataRequired(message='Username cannot be empty.'),
        Length(min=3, max=25, message='The number of characters cannot be less than 3 and greater than 25.')
    ])

    password = PasswordField("Password", validators=[
        DataRequired(message='Password cannot be empty.'),
        EqualTo(fieldname='passwordConfirm', message='Password confirm is incorrect.')
    ])

    passwordConfirm = PasswordField("Password Confirm", validators=[
        DataRequired(message='Password Confirm cannot be empty.'),
        EqualTo(fieldname='password', message='Password confirm is incorrect.')
    ])
