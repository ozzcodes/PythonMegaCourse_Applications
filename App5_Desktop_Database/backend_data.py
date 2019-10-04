import sqlite3
import random
import string


# Generate random ISBN numbers
def isbn_generator(size=12, chars=string.ascii_lowercase + string.digits):
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
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


# Create function to delete data
def delete(title, author, year, isbn):
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("DELETE FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    conn.commit()
    conn.close()


# Allow user's to update an entry
def update(title, author, year, isbn):
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    # Update an item
    curs.execute("UPDATE bookstore SET author=?, year=?, isbn=? WHERE title=?",
                 (author, year, isbn, title))  # Need a comma for SQLite after parameter
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
def search(title, author, year, isbn):
    conn = sqlite3.connect('books.sqlite')
    curs = conn.cursor()
    curs.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = curs.fetchall()
    conn.close()

    return rows


# Close the program
def close():
    return -1


db_connect()

# insert('The Old Man and the Sea', 'Ernest Hemingway', 1952, isbn=isbn_generator())
print(view())
