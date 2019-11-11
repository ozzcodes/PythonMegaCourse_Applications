import sqlite3
import random
import string


# Generate random ISBN numbers
def isbn_generator(size=12, chars=string.ascii_lowercase + string.digits):
    """
    Args:
        size:
        chars:
    """
    return ''.join(random.choice(chars) for x in range(size))


# Create database connection
def db_connect():
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS bookstore ("
                 "id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT )")
    conn.commit()
    conn.close()


# Create function to insert data
def insert(title, author, year, isbn):
    """
    Args:
        title:
        author:
        year:
        isbn:
    """
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


# Create function to delete data (want the ability to search many criteria)
def delete(id):
    """
    Args:
        id:
    """
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("DELETE FROM bookstore WHERE id=?", (id,))
    conn.commit()
    conn.close()


# Allow user's to update an entry
def update(id, title, author, year, isbn):
    """
    Args:
        id:
        title:
        author:
        year:
        isbn:
    """
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    # Update an item
    curs.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",
                 (title, author, year, isbn, id))  # Need a comma for SQLite after parameter
    conn.commit()
    conn.close()


# Create a view function
def view():
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("SELECT * FROM bookstore")
    rows = curs.fetchall()
    conn.close()

    return rows


# Create a search function
def search(title='', author='', year='', isbn=''):
    """
    Args:
        title:
        author:
        year:
        isbn:
    """
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = curs.fetchall()
    conn.close()

    return rows


# Make connection to database
db_connect()

'''
Test out the functions for correctness
'''
# insert('The Old Man and the Sea', 'Ernest Hemingway', 1952, isbn=isbn_generator())
# insert('A Random Book', 'Random Dude', 2018, isbn=isbn_generator())
# delete(3)
# update(2, 'Island in the Stream', 'Ernest Hemingway', 1970, isbn=isbn_generator())
# print(view())
# print('\n')
# print(search(author='Ernest Hemingway'))
