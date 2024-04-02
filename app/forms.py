from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional

class AuthorOnlyForm(FlaskForm):
    author = StringField('Name', validators=[DataRequired()])
    comment = TextAreaField('Comment')


class BookOnlyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    comment = TextAreaField('Comment')
    
    
class AuthorAndBookForm(FlaskForm):
    author = SelectField('Author', validators=[DataRequired()])
    customauthor = StringField('Custom Author', validators=[Optional()])
    title = StringField('Title', validators=[DataRequired()])
    comment = TextAreaField('Comment')
    
    def __init__(self, authors, extra_validators=None, *args, **kwargs):
        extra_validators = kwargs.pop('extra_validators', None)
        super(AuthorAndBookForm, self).__init__(*args, **kwargs)
        choices =  [author.name for author in authors] + ['custom']
        self.author.choices = choices
        self.authors_names = [author.name for author in authors]
        self.extra_validators = extra_validators


    def validate(self):
        if not super(AuthorAndBookForm, self).validate():
            return False
        
        if self.extra_validators:
            for validator in self.extra_validators:
                if not validator(self):
                    return False

        if self.author.data == 'custom' and not self.customauthor.data:
            self.customauthor.errors.append('Please enter the custom author.')
            return False
        
        if self.author.data == 'custom':
            self.author.data = self.customauthor.data

        if not self.author.data and not self.customauthor.data:
            self.author.errors.append('Please select an author or enter a custom author.')
            return False

        return True


    def is_customauthor_selected(self):
        return self.author.data == 'custom'
    
    
class BorrowOnlyForm(FlaskForm):
    borrower = SelectField('Borrower', validators=[DataRequired()])
    customborrower = StringField('Custom Borrower', validators=[Optional()])
    return_date = StringField('Return date', validators=[DataRequired()])
    comment = TextAreaField('Comment')

    def __init__(self, borrows, extra_validators=None, *args, **kwargs):
        extra_validators = kwargs.pop('extra_validators', None)
        super(BorrowOnlyForm, self).__init__(*args, **kwargs)
        choices = [borrow.borrower for borrow in borrows] + ['custom']
        self.borrower.choices = choices
        self.borrowers_names = [borrow.borrower for borrow in borrows]
        self.extra_validators = extra_validators

    def validate(self):
        if not super(BorrowOnlyForm, self).validate():
            return False
            
        if self.extra_validators:
            for validator in self.extra_validators:
                if not validator(self):
                    return False

        if self.borrower.data == 'custom' and not self.customborrower.data:
            self.customborrower.errors.append('Please enter the custom borrower.')
            return False
            
        if self.borrower.data == 'custom':
            self.borrower.data = self.customborrower.data

        if not self.borrower.data and not self.customborrower.data:
            self.borrower.errors.append('Please select an borrower or enter a custom borrower.')
            return False

        return True


    def is_customborrower_selected(self):
        return self.borrower.data == 'custom' 
    

class BorrowAndBookForm(FlaskForm):
    book = SelectField('Book', validators=[DataRequired()])
    borrower = SelectField('Borrower', validators=[DataRequired()])
    customborrower = StringField('Custom Borrower', validators=[Optional()])
    return_date = StringField('Return date', validators=[DataRequired()])
    comment = TextAreaField('Comment')
    
    def __init__(self, books, borrows, extra_validators=None, *args, **kwargs):
        extra_validators = kwargs.pop('extra_validators', None)
        super(BorrowAndBookForm, self).__init__(*args, **kwargs)
        
        books_choices = [book.title for book in books]
        self.book.choices = books_choices
        self.books_titles = [book.title for book in books]
        
        borrower_choices = [borrow.borrower for borrow in borrows] + ['custom']
        self.borrower.choices = borrower_choices
        self.borrowers_names = [borrow.borrower for borrow in borrows]
        self.extra_validators = extra_validators

    def validate(self):
        if not super(BorrowAndBookForm, self).validate():
            return False
            
        if self.extra_validators:
            for validator in self.extra_validators:
                if not validator(self):
                    return False

        if self.borrower.data == 'custom' and not self.customborrower.data:
            self.customborrower.errors.append('Please enter the custom borrower.')
            return False
            
        if self.borrower.data == 'custom':
            self.borrower.data = self.customborrower.data

        if not self.borrower.data and not self.customborrower.data:
            self.borrower.errors.append('Please select an borrower or enter a custom borrower.')
            return False

        return True


    def is_customborrower_selected(self):
        return self.borrower.data == 'custom' 