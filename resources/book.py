from flask_restful import Resource, reqparse
from models.book import BookModel


class Books(Resource):
    @staticmethod
    def get(self):
        return {'books': books}

class Book(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('title')
    argumentos.add_argument('author')
    argumentos.add_argument('year')

    def find_book(book_id):
        for book in books:
            if book['book_id'] == book_id:
                return book
            return None

    def get(self, book_id):
        book = Book.find_book(book_id)
        if book:
            return book
        return {'message': 'Book not found'}, 404

    def post(self, book_id):
        dados = Book.argumentos.parse_args()
        book_object = BookModel(book_id, **dados)
        new_book = book_object.json()
        books.append(new_book)
        return new_book, 200

    def put(self, book_id):
        dados = Book.argumentos.parse_args()

        book_object = BookModel(book_id, **dados)
        new_book = book_object.json()

        book = Book.find_book(book_id)
        if book:
            book.update(new_book)
            return new_book, 200 # OK
        books.append(new_book)
        return new_book, 201 # Cria o objeto caso ele não exista

    def delete(self, book_id):
        global books
        books = [book for book in books if book['book_id'] != book_id]
        return {'message': 'Book deleted.'}