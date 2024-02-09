from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email

class ExpenseForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    paid = BooleanField('Czy zapłacone?')