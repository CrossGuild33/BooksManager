class BookModel:
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