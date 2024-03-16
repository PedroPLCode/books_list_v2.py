from app.models import Author, Book, Borrow
from app import db
from flask import flash

def add_author(form):
    form.data.pop('csrf_token')
    new_author = Author(name=form.data['author'], 
                            comment=form.data['comment'])
    db.session.add(new_author)
    db.session.commit()
    flash(f'Author {new_author.name.title()} added to database.')
        

def add_book(form, author_id):
    form.data.pop('csrf_token')
    new_book = Book(title=form.data['title'], 
                    comment=form.data['comment'], 
                    author_id=author_id)
    db.session.add(new_book)
    db.session.commit()
    flash(f'Book {new_book.title.title()} added to database.')
    
    
def add_borrow(form, book_id):
    form.data.pop('csrf_token')
    new_borrow = Borrow(borrower=form.data['borrower'], 
                        return_date=form.data['return_date'], 
                        comment=form.data['comment'], 
                        book_id=book_id)
    db.session.add(new_borrow)
    db.session.commit()
    flash(f'New borrow to {new_borrow.borrower.title()} reqistered.')
    
    
def length_validator(form):
    if len(form.title.data) < 3:
        form.title.errors.append('Title must be at least 3 characters long.')
        return False
    return True