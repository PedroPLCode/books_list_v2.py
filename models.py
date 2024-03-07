import json

class Books:
    def __init__(self):
        try:
            with open("books.json", "r") as filename:
                self.books = json.load(filename)
        except FileNotFoundError:
            self.books = []

    def all(self):
        return self.books
    
    def get(self, id):
        book = [book for book in self.all() if book['id'] == id]
        if book:
            return book[0]
        return []
    
    def get_books_filtered_by_lent(self, is_lent):
        filtered = [book for book in self.all() if book['lent'] == is_lent]
        if filtered:
            return filtered
        return []
    
    def create(self, data):
        data['id'] = books.all()[-1]['id'] + 1
        self.books.append(data)
        self.save_all()
        
    def delete(self, id):
        book = self.get(id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False

    def save_all(self):
        with open("books.json", "w") as filename:
            json.dump(self.books, filename)

    def update(self, id, data):
        book = self.get(id)
        if book:
            data['id'] = id
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False

books = Books()