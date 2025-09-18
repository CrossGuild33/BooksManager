# class Section(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#
#
# class Summary(db.Model):
#     id = Column(db.Integer, primary_key=True)
#     content = db.Column(db.text, nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'))