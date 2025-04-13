# 📚 Kindle Book Data Migration to Snowflake

This project simulates a real-world data platform migration from a local relational database (SQLite) to Snowflake, using publicly available Kindle book data. It covers schema restructuring, multiple ingestion methods, and downstream-ready views for analysis.


## 🔄 Migration Summary

- **Source**: SQLite (`kindle_books.db`)
- **Target**: Snowflake Cloud Data Warehouse
- **Data**: Amazon Kindle Books Dataset 2023 (130K Books) (from [Kaggle](https://www.kaggle.com/datasets/asaniczka/amazon-kindle-books-dataset-2023-130k-books))
- **Schema**: Defined in `sql/schema/create_books_table.sql`


## 🧰 Tools & Tech

- **Python** (pandas, sqlite3, snowflake-connector)
- **Snowflake** (Snowsight, Internal Stage, COPY INTO)


## 🚀 Migration Paths

### Option A: Direct Insert from SQLite
```bash
python scripts/upload_from_sqlite_to_snowflake.py
```

### Option B: High-Volume Load via COPY INTO
```bash
python scripts/upload_csv_to_stage.py
python scripts/load_from_csv_to_snowflake.py
```


## ✅ Data Verification
- SQL: ```sql/queries/verify_row_count.sql```

- Python: ```scripts/check_data_in_snowflake.py```


## 📊 Downstream Views (for reporting)
- Top Selling Categories: ```sql/views/top_selling_categories.sql```

- Bestsellers by Review Count: ```sql/views/best_sellers_by_reviews.sql```

These views simulate data marts for analytics and can be visualised in Tableau.


## 💡 Key Takeaways
- Built and tested two ingestion pipelines to compare performance trade-offs.

- Focused on data type consistency, validation, and schema clarity for downstream use.

- Simulated both engineering and analytics use cases, preparing the data for dashboards.
