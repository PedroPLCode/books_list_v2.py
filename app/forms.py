from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email

class AuthorForm(FlaskForm):
    name = StringField('Author', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    
class BorrowForm(FlaskForm):
    borrower = StringField('Borrower', validators=[DataRequired()])
    borrow_date = StringField('Borrow date', validators=[DataRequired()])
    return_date = StringField('Return date', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])