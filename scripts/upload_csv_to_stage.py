import os
from dotenv import load_dotenv
import snowflake.connector

# Load environment variables
load_dotenv()

# Absolute path to the CSV file
csv_path = os.path.abspath("data/raw/cleaned_kindle_data.csv")

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

# Upload file to internal stage
put_sql = f"""
PUT file://{csv_path} @kindle_stage 
AUTO_COMPRESS=TRUE 
OVERWRITE=TRUE;
"""
cursor.execute(put_sql)
print("🙆🏻‍♀️ CSV file uploaded to Snowflake stage 'kindle_stage'.")

cursor.close()
conn.close()
