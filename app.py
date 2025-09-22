from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.book import Books, Book

app = Flask(__name__)
api = Api(app)

api.add_resource(Books, '/books')
api.add_resource(Book, '/books/<string:book_id>')

# Para criar o banco e rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)