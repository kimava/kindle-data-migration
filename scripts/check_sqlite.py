"""
This script is used to verify that the cleaned data has been properly stored in the SQLite database.
It prints the total number of rows in the 'books' table and previews the first few entries.
"""

import sqlite3

# Connect to the database
conn = sqlite3.connect("db/kindle_books.db")
cursor = conn.cursor()

# Check number of rows in the 'books' table
cursor.execute("SELECT COUNT(*) FROM books")
row_count = cursor.fetchone()[0]
print(f"Total rows in books table: {row_count}")

# Preview a few rows
cursor.execute("SELECT title, author, publishedDate FROM books LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
