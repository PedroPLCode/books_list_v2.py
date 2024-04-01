from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Author, Book, Borrow
from app.forms import AuthorOnlyForm, BookOnlyForm, AuthorAndBookForm, BorrowOnlyForm, BorrowAndBookForm
from app.utils import *

@app.route('/')
def home_page_view():
    return render_template("home_page.html")


@app.route('/authors/', methods=["GET", "POST"])
def authors_view():
    search_query = request.args.get('search')
    form = AuthorOnlyForm()
    if search_query:
        authors = Author.query.filter(Author.name.ilike(f"%{search_query}%")).all()
    else:
        authors = Author.query.all()
        search_query = None
    if request.method == "POST" and form.validate_on_submit():
        add_author(form)
        return redirect(url_for("authors_view"))
    return render_template("authors.html", 
                           authors=authors, 
                           search=search_query,
                           form=form)


@app.route('/removeauthor/<int:author_id>', methods=["GET"])
def remove_author(author_id):
    authors = Author.query.all()
    for author in authors:
        if author.id  == int(author_id):
            db.session.delete(author)
            db.session.commit()
            flash(f'Author {author.name.title()} removed from database.')
            break
    return redirect(url_for("authors_view"))


@app.route('/books/', methods=["GET"])
def books_view():
    authors = Author.query.all()
    author_name = request.args.get('author')
    search_query = request.args.get('search')
    form = AuthorAndBookForm(authors, author=author_name, extra_validators=[length_validator])
    author = None
    if author_name:
        author = Author.query.filter_by(name=author_name).first()
        if author:
            books = Book.query.filter_by(author_id=author.id).all()
        else:
            books = []
    elif search_query:
        books = Book.query.filter(Book.title.ilike(f"%{search_query}%")).all()
    else:
        books = Book.query.all()
    return render_template("books.html", 
                           author=author, 
                           form=form, 
                           search=search_query,
                           books=books)


@app.route('/addbook/<int:author_id>', methods=["GET", "POST"])
def add_book_view(author_id):
    form = BookOnlyForm()
    
    if request.method == "POST" and form.validate_on_submit():
        author_id = request.form.get('author_id')
        add_book(form, author_id)
        return redirect(url_for("books_view"))
    
    author = Author.query.filter_by(id=author_id).first()
    return render_template("add_book.html", 
                           form=form,
                           author_name=author.name,
                           author_id=author_id)
    
    
@app.route('/addbook/', methods=["POST"])
def add_book_without_author_id_param():
    authors = Author.query.all()
    form = AuthorAndBookForm(authors, extra_validators=[length_validator])
    author = Author.query.filter_by(name=form.data['author']).first()
    
    if author and form.validate():
        author_id = author.id
        add_book(form, author_id)
    elif not author and form.validate():
        add_author(form)
        author = Author.query.filter_by(name=form.data['author']).first()
        author_id = author.id
        add_book(form, author_id)
    return redirect(url_for("books_view"))


@app.route('/removebook/<int:book_id>', methods=["GET"])
def remove_book(book_id):
    books = Book.query.all()
    for book in books:
        if book.id  == int(book_id):
            db.session.delete(book)
            db.session.commit()
            flash(f'Book {book.title.title()} removed from database.')
            break
    return redirect(url_for("books_view"))


@app.route('/borrows/', methods=["GET"])
def borrows_view():
    books = Book.query.all()
    form = BorrowAndBookForm(books)
    borrower_name = request.args.get('borrower')
    search_query = request.args.get('search')
    if borrower_name:
        borrows = Borrow.query.filter_by(borrower=borrower_name).all()
        search_query = None
    elif search_query:
        borrows = Borrow.query.filter(Borrow.borrower.ilike(f"%{search_query}%")).all()
        borrower_name = None
    else:
        borrows = Borrow.query.all()
        borrower_name = None
        search_query = None
    return render_template("borrows.html", 
                           form=form,
                           borrower=borrower_name, 
                           search=search_query, 
                           borrows=borrows)


@app.route('/addborrow/<int:book_id>', methods=["GET", "POST"])
def add_borrow_view(book_id):
    form = BorrowOnlyForm()
    if request.method == "POST" and form.validate_on_submit():
        book_id = request.form.get('book_id')
        add_borrow(form, book_id)
        return redirect(url_for("borrows_view"))
    book = Book.query.filter_by(id=book_id).first()
    return render_template("add_borrow.html", 
                           form=form, 
                           book_title=book.title,
                           book_id=book_id)
    
    
@app.route('/addborrow/', methods=["POST"])
def add_borrow_without_book_id_param():
    books = Book.query.all()
    form = BorrowAndBookForm(books)
    book = Book.query.filter_by(title=form.data['book']).first()
    book_id = book.id
    
    if form.validate_on_submit():
        add_borrow(form, book_id)
        return redirect(url_for("borrows_view"))


@app.route('/removeborrow/<int:borrow_id>', methods=["GET"])
def remove_borrow(borrow_id):
    borrows = Borrow.query.all()
    for borrow in borrows:
        if borrow.id == int(borrow_id):
            flash(f'{borrow.borrower.title()}s borrow of book {borrow.book.title} ended.')
            db.session.delete(borrow)
            db.session.commit()
            break
    return redirect(url_for("borrows_view"))