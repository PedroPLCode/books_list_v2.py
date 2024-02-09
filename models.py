import json

class Expenses:
    def __init__(self):
        try:
            with open("expenses.json", "r") as filename:
                self.expenses = json.load(filename)
        except FileNotFoundError:
            self.expenses = []

    def all(self):
        return self.expenses

    def get(self, id):
        return self.expenses[id]

    def create(self, data):
        data.pop('csrf_token')
        self.expenses.append(data)

    def save_all(self):
        with open("expenses.json", "w") as filename:
            json.dump(self.expenses, filename)

    def update(self, id, data):
        data.pop('csrf_token')
        self.expenses[id] = data
        self.save_all()

expenses = Expenses()