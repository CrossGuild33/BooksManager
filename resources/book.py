from flask_restful import Resource

books = [
    {
        'title': 'Hora e a Vez de Augusto Matraga',
        'author': 'Guimarães Rosa',
        'year': 1963
    }
]


class Books(Resource):
    @staticmethod
    def get():
        return {'Books': books}