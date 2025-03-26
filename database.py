import sqlite3

# Connect to the SQLite3 database
conn = sqlite3.connect('form.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store form data
cursor.execute('''
CREATE TABLE IF NOT EXISTS form_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()