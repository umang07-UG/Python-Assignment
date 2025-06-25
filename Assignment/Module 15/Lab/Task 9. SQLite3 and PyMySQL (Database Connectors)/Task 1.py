# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.


import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')


cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))


conn.commit()


cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()


for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")


conn.close()