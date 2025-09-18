from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from resources.book import Books

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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



api.add_resource(Books, '/books')

# Para criar o banco e rodar a aplicação
if __name__ == '__main__':
    #with app.app_context():
      #  db.create_all() # Create database in the first run
    app.run(debug=True)