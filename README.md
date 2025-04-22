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
The following Snowflake views were created for downstream consumption and analysis:

- ```top_performing_books```

- ```category_performance_summary```

- ```kindle_unlimited_vs_non_kindle_unlimited_comparison```

- ```label_performance_summary```

- ```publishing_trends_by_month```

## 📈 Tableau Dashboard
The final dashboard was built using the above Snowflake views and exported as CSV to support visual storytelling.
It highlights key performance patterns across books, categories, subscription inclusion, and publishing trends.

### 💡 Key Insights Visualised:
**📚 Top 50 Books** – Most-reviewed and highest-rated titles

**🗂 Performance by Category** – Stars, price, Kindle Unlimited %, and review stats per category

**🔄 Kindle Unlimited vs Non-Kindle Unlimited** – Subscription impact on stars, price, and bestseller rate

**🏷 Performance by Label** – Impact of being a Bestseller, Editor’s Pick, or Goodreads Choice

**📅 Publishing Trends** – Book release volume and average rating over time (2020.09–2023.09)

🔗 View [the Dashboard](https://public.tableau.com/app/profile/soyeon.kim4151/viz/AmazonKindleBookDataDashboard/AmazonKindleBooksDashboard) on Tableau Public




## 💡 Key Takeaways
- Built and tested two ingestion pipelines to compare performance trade-offs.

- Focused on data type consistency, validation, and schema clarity for downstream use.

- Simulated both engineering and analytics use cases, preparing the data for dashboards.

- Completed end-to-end pipeline from ingestion → modelling → visualisation.
