from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = TextAreaField('Author', validators=[DataRequired()])
    lent = BooleanField('Is lent?')