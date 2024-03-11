from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Author, Book, Borrow
from app.forms import AuthorForm, BookForm, BorrowForm

@app.route('/')
def home_page_view():
    return render_template("home_page.html")


@app.route('/authors/', methods=["GET", "POST"])
def authors_view():
    form=AuthorForm()
    authors = Author.query.all()
    if request.method == "POST" and form.validate_on_submit():
        form.data.pop('csrf_token')
        new_author = Author(name=form.data['name'], 
                            comment=form.data['comment'])
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for("authors_view"))
    return render_template("authors.html", 
                           authors=authors, 
                           form=form)


@app.route('/removeauthor/<int:author_id>', methods=["GET"])
def remove_author(author_id):
    authors = Author.query.all()
    for author in authors:
        if author.id  == int(author_id):
            db.session.delete(author)
            db.session.commit()
            break
    return redirect(url_for("authors_view"))


@app.route('/books/', methods=["GET"])
def books_view():
    author_name = request.args.get('author')
    
    if author_name:
        author = Author.query.filter_by(name=author_name).first()
        if author:
            books = Book.query.filter_by(author_id=author.id).all()
        else:
            books = []
    else:
        books = Book.query.all()
        author = None
        
    return render_template("books.html", author=author, books=books)


@app.route('/addbook/<int:author_id>', methods=["GET", "POST"])
def add_book_view(author_id):
    form=BookForm()
    if request.method == "POST" and form.validate_on_submit():
        author_id = request.form.get('author_id')
        form.data.pop('csrf_token')
        new_book = Book(title=form.data['title'], 
                        comment=form.data['comment'], 
                        author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("books_view"))
    return render_template("add_book.html", 
                           form=form, 
                           author_id=author_id)


@app.route('/removebook/<int:book_id>', methods=["GET"])
def remove_book(book_id):
    books = Book.query.all()
    for book in books:
        if book.id  == int(book_id):
            db.session.delete(book)
            db.session.commit()
            break
    return redirect(url_for("books_view"))


@app.route('/borrows/', methods=["GET"])
def borrows_view():
    borrows = Borrow.query.all()
    return render_template("borrows.html", 
                           borrows=borrows)


@app.route('/addborrow/<int:book_id>', methods=["GET", "POST"])
def add_borrow_view(book_id):
    form=BorrowForm()
    if request.method == "POST" and form.validate_on_submit():
        book_id = request.form.get('book_id')
        form.data.pop('csrf_token')
        new_borrow = Borrow(borrower=form.data['borrower'], 
                            return_date=form.data['return_date'], 
                            comment=form.data['comment'], 
                            book_id=book_id)
        db.session.add(new_borrow)
        db.session.commit()
        return redirect(url_for("borrows_view"))
    return render_template("add_borrow.html", 
                           form=form, 
                           book_id=book_id)


@app.route('/removeborrow/<int:borrow_id>', methods=["GET"])
def remove_borrow(borrow_id):
    borrows = Borrow.query.all()
    for borrow in borrows:
        if borrow.id == int(borrow_id):
            db.session.delete(borrow)
            db.session.commit()
            break
    return redirect(url_for("borrows_view"))