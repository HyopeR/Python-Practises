from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class ArticleForm(Form):
    title = StringField("Article Title", validators=[
        DataRequired(message='Article Title cannot be empty.'),
        Length(min=3, max=40, message='The number of characters cannot be less than 3 and greater than 30.')
    ])

    content = TextAreaField("Article Content", validators=[
        DataRequired(message='Article Title cannot be empty.'),
        Length(min=10, max=500, message='The number of characters cannot be less than 10 and greater than 100.')
    ])

