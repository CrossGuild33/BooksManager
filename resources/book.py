from flask_restful import Resource

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
        pass

    def put(self, book_id):
        pass

    def delete(self, book_id):
        pass