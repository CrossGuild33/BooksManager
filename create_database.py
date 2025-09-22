import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = " CREATE TABLE IF NOT EXISTS books (book_id text PRIMARY KEY, \
                 title text, author text, year int)"

create_book = " INSERT INTO books VALUES ('Dostoievski', 'Irmãos Karamazovi', 'Fiodor Dostoiévski', 1880)"

cursor.execute(create_table)
cursor.execute(create_book)

connection.commit()
connection.close()