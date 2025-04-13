import os
from dotenv import load_dotenv
import snowflake.connector

# Load env variables
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

# Truncate the table
cursor.execute("TRUNCATE TABLE books;")
print("Table 'books' truncated.")

# COPY INTO from stage
copy_sql = """
COPY INTO books
FROM @kindle_stage
FILE_FORMAT = (
  TYPE = 'CSV'
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  SKIP_HEADER = 1
)
ON_ERROR = 'CONTINUE';
"""
cursor.execute(copy_sql)
print("🙆🏻‍♀️ Completed COPY INTO. Data loaded from CSV.")

# Row count check
cursor.execute("SELECT COUNT(*) FROM books")
print("📊 Total rows after COPY INTO:", cursor.fetchone()[0])

cursor.close()
conn.close()
