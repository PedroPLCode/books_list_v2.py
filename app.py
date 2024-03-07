from flask import Flask, jsonify, abort, make_response, request, render_template, redirect, url_for
from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "sratatata"

@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_v1():
    lent_parameter = request.args.get("lent")
    if lent_parameter:
        lent_filter = True if lent_parameter == 'true' else False
        filtered = books.get_books_filtered_by_lent(lent_filter)
        return jsonify(filtered)
    return jsonify(books.all())


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book_api_v1(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})


@app.route("/api/v1/books/", methods=["POST"])
def create_book_api_v1():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'lent': False
    }
    books.create(book)
    return jsonify({'book': book}), 201


@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_book_api_v1(book_id):
    result = books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_book_api_v1(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),
        'lent' in data and not isinstance(data.get('lent'), bool)
    ]):
        abort(400)
    book = {
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'lent': data.get('lent', book['lent'])
    }
    books.update(book_id, book)
    return jsonify({'book': book})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BookForm()
    error = ""
    if request.method == "POST" and form.validate_on_submit():
        form.data.pop('csrf_token')
        books.create(form.data)
        books.save_all()
        return redirect(url_for("books_list"))

    return render_template("books.html", 
                           form=form, 
                           books=books.all(), 
                           error=error)
    

@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            book = {
            'id': book_id,
            'title': form.data['title'],
            'author': form.data['author'],
            'lent': form.data['lent']
        }
            form.data.pop('csrf_token')
            books.update(book_id, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", 
                           form=form, 
                           book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)