import psycopg2

'''
Postgres4 Credentials are in text file;
Needed for connecting to db!
'''


# First create a table with rows
def create_table():
    # Create a connection
    conn = psycopg2.connect("dbname='pgdb1' user='postgres' password='0212181' host='localhost' port='5432'")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS Mystore (item TEXT , quantity INTEGER, price REAL )")

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
    conn = psycopg2.connect("dbname='pgdb1' user='postgres' password='0212181' host='localhost' port='5432'")
    curs = conn.cursor()
    # curs.execute("INSERT INTO Mystore VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    curs.execute("INSERT INTO Mystore VALUES (%s, %s, %s)", (item, quantity, price))

    # Commit database and data to data source and then close connection
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='pgdb1' user='postgres' password='0212181' host='localhost' port='5432'")
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
    conn = psycopg2.connect("dbname='pgdb1' user='postgres' password='0212181' host='localhost' port='5432'")
    curs = conn.cursor()
    # Delete an item
    curs.execute("DELETE FROM Mystore WHERE item=%s", (item,))  # Need a comma for SQLite after parameter
    conn.commit()
    conn.close()


def update(quantity, price, item):
    """
    Args:
        quantity:
        price:
        item:
    """
    conn = psycopg2.connect("dbname='pgdb1' user='postgres' password='0212181' host='localhost' port='5432'")
    curs = conn.cursor()
    # Update an item
    curs.execute("UPDATE Mystore SET quantity=%s, price=%s WHERE item=%s",
                 (quantity, price, item))  # Need a comma for SQLite after parameter
    conn.commit()
    conn.close()


create_table()
# insert('Apples', 15, 0.99)
# delete('Green Apples')
update(22, 0.95, 'Apples')
print(view())

# # Delete an item
# delete('Wine Glass')
#
# # Update an item
# update(12, 18, 'Waterbottle')
#
# # Select non-duplicated items
# remove_duplicates()
#
# # Print a view of the data in a list format
# print(view())
