import sqlite3
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

# Load Snowflake credentials from .env
load_dotenv()

# Load data from SQLite
sqlite_conn = sqlite3.connect("db/kindle_books.db")
df = pd.read_sql_query("SELECT * FROM books", sqlite_conn)
sqlite_conn.close()
print(f"🙆🏻‍♀️ Loaded {len(df)} rows from SQLite.")

# Connect to Snowflake
sf_conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)
cursor = sf_conn.cursor()

# Create table in Snowflake
create_table_sql = """
CREATE OR REPLACE TABLE books (
    asin STRING,
    title STRING,
    author STRING,
    soldBy STRING,
    stars FLOAT,
    reviews INT,
    price FLOAT,
    isKindleUnlimited BOOLEAN,
    category_id INT,
    isBestSeller BOOLEAN,
    isEditorsPick BOOLEAN,
    isGoodReadsChoice BOOLEAN,
    publishedDate DATE,
    category_name STRING
);
"""
cursor.execute(create_table_sql)
print("🙆🏻‍♀️ Created Snowflake table 'books'.")

# Insert data in batches
insert_sql = """
INSERT INTO books (
    asin, title, author, soldBy, stars, reviews, price,
    isKindleUnlimited, category_id, isBestSeller, isEditorsPick, isGoodReadsChoice,
    publishedDate, category_name
)
VALUES (%(asin)s, %(title)s, %(author)s, %(soldBy)s, %(stars)s, %(reviews)s, %(price)s,
        %(isKindleUnlimited)s, %(category_id)s, %(isBestSeller)s, %(isEditorsPick)s, %(isGoodReadsChoice)s,
        %(publishedDate)s, %(category_name)s);
"""

# Insert in batches
batch_size = 1000
rows = df.to_dict(orient="records")

for i in range(0, len(rows), batch_size):
    batch = rows[i:i+batch_size]
    cursor.executemany(insert_sql, batch)
    print(f"🙆🏻‍♀️ Inserted rows {i} to {i+len(batch)-1}")

cursor.close()
sf_conn.close()
print("🎉 Successfully migrated data from SQLite to Snowflake.")
