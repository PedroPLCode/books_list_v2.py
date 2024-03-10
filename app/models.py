from datetime import datetime
from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    comment = db.Column(db.String(100), index=True)
    books = db.relationship("Book", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<User {self.name}>"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    date = db.Column(db.String(100), index=True, default=datetime.today().strftime('%Y-%m-%d'))
    comment = db.Column(db.String(100), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    borrows = db.relationship("Borrow", backref="book", lazy="dynamic")
    
    def __str__(self):
        return f"<Book {self.id} {self.title}>"


class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(100), index=True)
    borrow_date = db.Column(db.String(100), index=True, default=datetime.today().strftime('%Y-%m-%d'))
    return_date = db.Column(db.String(100), index=True)
    comment = db.Column(db.String(100), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Borrow {self.id} {self.borrower}>"