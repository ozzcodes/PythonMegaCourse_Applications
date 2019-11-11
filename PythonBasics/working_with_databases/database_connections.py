import sqlite3


# First create a table with rows
def create_table():
    # Create a connection
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS Mystore (item MESSAGE_TEXT , quantity INTEGER, price REAL )")

    # Commit database and data to data source and then close connection
    conn.commit()
    conn.close()


# Enter some data
def insert(item, quantity, price):
    """
    Args:
        item:
        quantity:
        price:
    """
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    curs.execute("INSERT INTO Mystore VALUES (?, ?, ?)", (item, quantity, price))

    # Commit database and data to data source and then close connection
    conn.commit()
    conn.close()


# Insert some random data
# insert('Waterbottle', 15, 5)
# insert('Coffee mug', 12, 8)


def view():
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    curs.execute("SELECT * FROM Mystore")
    rows = curs.fetchall()
    conn.commit()
    conn.close()

    return rows


def delete(item):
    """
    Args:
        item:
    """
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    # Delete an item
    curs.execute("DELETE FROM Mystore WHERE item=?", (item,))  # Need a comma for SQLite after parameter
    conn.commit()
    conn.close()


def update(quantity, price, item):
    """
    Args:
        quantity:
        price:
        item:
    """
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    # Update an item
    curs.execute("UPDATE Mystore SET quantity=?, price=? WHERE item=?",
                 (quantity, price, item))  # Need a comma for SQLite after parameter
    conn.commit()
    conn.close()


def remove_duplicates():
    conn = sqlite3.connect('db.sqlite')
    curs = conn.cursor()
    curs.execute("DELETE FROM Mystore WHERE item NOT IN (SELECT min(item) FROM Mystore GROUP BY item, quantity)")


# Delete an item
delete('Wine Glass')

# Update an item
update(12, 18, 'Waterbottle')

# Select non-duplicated items
remove_duplicates()

# Print a view of the data in a list format
print(view())
