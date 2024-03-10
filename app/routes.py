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
    for i in range(0, n):
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

    return render_template("authors.html", authors=authors, form=form, error=error)


@app.route('/books', methods=["GET", "POST"])
def books_view():
    error = ""
    books = Book.query.all()
    return render_template("books.html", books=books, error=error)


@app.route('/addbook/<int:author_id>', methods=["GET", "POST"])
def add_book_view(author_id):
    form=BookForm()
    error = ""
    
    if request.method == "POST" and form.validate_on_submit():
        author_id = request.form.get('author_id')
        form.data.pop('csrf_token')
        new_book = Book(title=form.data['title'], comment=form.data['comment'], author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        books = Book.query.all()
        return render_template("books.html", books=books, form=form, error=error)
    
    return render_template("add_book.html", form=form, error=error, author_id=author_id)


@app.route('/borrows', methods=["GET", "POST"])
def borrows_view():
    error = ""
    borrows = Borrow.query.all()
    return render_template("borrows.html", borrows=borrows, error=error)


@app.route('/addborrow/<int:book_id>', methods=["GET", "POST"])
def add_borrow_view(book_id):
    form=BorrowForm()
    error = ""
    
    if request.method == "POST" and form.validate_on_submit():
        book_id = request.form.get('book_id')
        form.data.pop('csrf_token')
        new_borrow = Borrow(borrower=form.data['borrower'], 
                            borrow_date=form.data['borrow_date'], 
                            return_date=form.data['return_date'], 
                            comment=form.data['comment'], 
                            book_id=book_id)
        db.session.add(new_borrow)
        db.session.commit()
        borrows = Borrow.query.all()
        return render_template("borrows.html", borrows=borrows, form=form, error=error)
    
    return render_template("add_borrow.html", form=form, error=error, book_id=book_id)
