import sqlite3


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    """)
    connection.commit()
    connection.close()


initiate_db()

# запустить один раз:
# a = 1
# for i in range(4):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f'Product {a}', f'описание {a}', f'{a*100}'))
#     a += 1

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products
