import pandas as pd
from pathlib import Path

# File paths
RAW_DATA_PATH = Path("data/raw/kindle_data.csv")
CLEANED_DATA_PATH = Path("data/raw/cleaned_kindle_data.csv")

# Load the raw dataset
df = pd.read_csv(RAW_DATA_PATH)

# Drop unnecessary columns (not for analysis)
df = df.drop(columns=["imgUrl", "productURL"])

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Convert 'stars' to float
df['stars'] = pd.to_numeric(df['stars'], errors='coerce').fillna(0.0)

# Convert 'reviews' to int
df['reviews'] = pd.to_numeric(df['reviews'], errors='coerce').fillna(0).astype(int)

# Convert 'price' to float
df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)

# Convert boolean-like columns to actual booleans
bool_cols = ['isKindleUnlimited', 'isBestSeller', 'isEditorsPick', 'isGoodReadsChoice']
for col in bool_cols:
    df[col] = df[col].astype(str).str.lower().map({'true': True, 'false': False})
    df[col] = df[col].fillna(False)

# Convert 'publishedDate' to datetime format (NaT if invalid or empty)
df['publishedDate'] = pd.to_datetime(df['publishedDate'], errors='coerce')

# Clean text columns (strip whitespace, remove quotes, handle special characters if needed)
df['title'] = df['title'].astype(str).str.strip().str.replace('"', '', regex=False)
df['author'] = df['author'].astype(str).str.strip()
df['soldBy'] = df['soldBy'].astype(str).str.strip()
df['category_name'] = df['category_name'].astype(str).str.strip()

# Drop duplicate ASINs
df = df.drop_duplicates(subset='asin')

# Sanity check: check data types, missing values, and boolean conversions
print("Data types:")
print(df.dtypes)

print("Missing values:")
print(df.isnull().sum())

print("Unique values for boolean columns:")
for col in bool_cols:
    print(f"{col}: {df[col].unique()}")

# Save the cleaned data
CLEANED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CLEANED_DATA_PATH, index=False)
print(f"Preprocessing complete! Cleaned file saved to: {CLEANED_DATA_PATH}")
