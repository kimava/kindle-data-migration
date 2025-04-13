-- Check data has been successfully migrated to Snowflake
-- Run this query in Snowflake or from Python via snowflake-connector

-- Total number of rows in the 'books' table
SELECT COUNT(*) AS total_rows FROM books;

-- Preview a few rows
SELECT *
FROM books
LIMIT 5;

