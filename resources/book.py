from flask_restful import Resource, reqparse

books = [
    {
        'title': 'Hora e a Vez de Augusto Matraga',
        'author': 'Guimarães Rosa',
        'year': 1963
    },
    {
        'title': 'O Tempo e o Vento',
        'author': 'Erico Verissimo',
        'year': 1952
    }

]


class Books(Resource):
    @staticmethod
    def get(self):
        return {'books': books}

class Book(Resource):
    def get(self, book_id):
        for book in books:
            if books['book_id'] == book_id:
                return book
        return {'message': 'Book not found'}, 404

    def post(self, book_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('title')
        argumentos.add_argument('author')
        argumentos.add_argument('year')

        dados = argumentos.parse_args()

        new_book = {
            'book_id': book_id,
            'title': dados['title'],
            'author': dados['author'],
            'year': dados['year']
        }

        books.append(new_book)
        return new_book, 200

    def put(self, book_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('title')
        argumentos.add_argument('author')
        argumentos.add_argument('year')

        dados = argumentos.parse_args()

        new_book = {
            'book_id': book_id,
            'title': dados['title'],
            'author': dados['author'],
            'year': dados['year']
        }

        for book in books:
            if books['book_id'] == book_id:
                return book
        return None
        if book is not None:
            for book in books:
                if book['book_id'] == book_id:
                    book.update(new_book)
                    return new_book, 200
                books.append(book)
                return new_book, 201

    def delete(self, book_id):
        pass