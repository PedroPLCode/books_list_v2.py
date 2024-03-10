from app import app, db
from app.models import Author, Book, Borrow

app.config["SECRET_KEY"] = "sratatata"

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Author": Author,
        "Book": Book,
        "Borrow": Borrow
    }

if __name__ == "__main__":
    app.run(debug=True)