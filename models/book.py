from sql_alchemy import database

class BookModel:
    __tablename__ = 'books'

    book_id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(120))
    author = database.Column(database.String(100))
    year = database.Column(database.Integer)

    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def json(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year
        }