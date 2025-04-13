import pandas as pd
import sqlite3

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_kindle_data.csv")

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("db/kindle_books.db")

# Save the DataFrame to a new table, 'books'
df.to_sql("books", conn, if_exists="replace", index=False)

# Close the connection
conn.close()

print("✅ Data saved to SQLite database!")
