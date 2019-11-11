import sqlite3
import random
import string


# Create a class (as an OOP design) for cleaning up code
class MyDatabase:

    # Create database connection
    def __init__(self, db):
        """
        Args:
            db:
        """
        self.conn = sqlite3.connect(db)
        self.curs = self.conn.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS bookstore ("
                          "id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT )")
        self.conn.commit()

    # Generate random ISBN numbers
    def isbn_generator(self, size=12, chars=string.ascii_lowercase + string.digits):
        """
        Args:
            size:
            chars:
        """
        return ''.join(random.choice(chars) for self.x in range(size))

    # Create function to insert data
    def insert(self, title, author, year, isbn):
        """
        Args:
            title:
            author:
            year:
            isbn:
        """
        self.curs.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    # Create function to delete data (want the ability to search many criteria)
    def delete(self, id):
        """
        Args:
            id:
        """
        self.curs.execute("DELETE FROM bookstore WHERE id=?", (id,))
        self.conn.commit()

    # Allow user's to update an entry
    def update(self, id, title, author, year, isbn):
        # Update an item
        """
        Args:
            id:
            title:
            author:
            year:
            isbn:
        """
        self.curs.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",
                          (title, author, year, isbn, id))  # Need a comma for SQLite after parameter
        self.conn.commit()

    # Create a view function
    def view(self):
        self.curs.execute("SELECT * FROM bookstore")
        rows = self.curs.fetchall()

        return rows

    # Create a search function
    def search(self, title='', author='', year='', isbn=''):
        """
        Args:
            title:
            author:
            year:
            isbn:
        """
        self.curs.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",
                          (title, author, year, isbn))
        rows = self.curs.fetchall()

        return rows

    # Removed close() from __init__ function so need new function
    def __del__(self):
        self.conn.close()

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
