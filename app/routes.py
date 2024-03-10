from flask import render_template, request, redirect, url_for
from faker import Faker
from app import app, db
from app.models import Author, Book, Borrow
from app.forms import AuthorForm, BookForm, BorrowForm

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
def base_view():
    if Author.query.first() is None:
        create_fake_data_n_times(12)
    return render_template("base.html")


@app.route('/authors', methods=["GET", "POST"])
def authors_view():
    form=AuthorForm()
    error = ""
    authors = Author.query.all()
    
    if request.method == "POST" and form.validate_on_submit():
        form.data.pop('csrf_token')
        new_author = Author(name=form.data['name'], comment=form.data['comment'])
        db.session.add(new_author)
        db.session.commit()

        return redirect(url_for("authors_view"))

    return render_template("authors.html", authors=authors, form=form)


@app.route('/books', methods=["GET", "POST"])
def books_view():
    form=BookForm()
    error = ""
    books = Book.query.all()

    return render_template("books.html", books=books, form=form)


@app.route('/borrows', methods=["GET", "POST"])
def borrows_view():
    form=BorrowForm()
    error = ""
    borrows = Borrow.query.all()

    return render_template("borrows.html", borrows=borrows, form=form, error=error)