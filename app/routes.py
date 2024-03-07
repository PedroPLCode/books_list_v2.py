from flask import render_template
from faker import Faker
from app import app, db
from app.models import Author, Book, Borrow

fake = Faker()

def create_fake_data():
    author = Author(name=f"{fake.first_name()} {fake.last_name()}")
    book = Book(title=f"{fake.job()}", 
                date=f"{fake.date_of_birth()}", 
                author_id=author.id)
    borrow = Borrow(borrower=f"{fake.first_name()} {fake.last_name()}", 
                    borrow_date=f"{fake.date_of_birth()}", 
                    return_date=f"{fake.date_of_birth()}",
                    book_id=book.id)
    db.session.add(author)
    db.session.add(book)
    db.session.add(borrow)
    db.session.commit()


def create_fake_data_n_times(n):
    for i in range(1, n):
        create_fake_data()
        

@app.route('/')
def index():
    if Author.query.first() is None:
        create_fake_data_n_times(12)

    authors = Author.query.all()
    books = Book.query.all()
    borrows = Borrow.query.all()

    return render_template("index.html", authors=authors, books=books, borrows=borrows)