import os
from dotenv import load_dotenv
import snowflake.connector

# Load environment variables from .env
load_dotenv()

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)

cursor = conn.cursor()

# Check row count
cursor.execute("SELECT COUNT(*) FROM books")
print("📊 Total rows in 'books':", cursor.fetchone()[0])

# Preview a few rows
cursor.execute("SELECT * FROM books LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
