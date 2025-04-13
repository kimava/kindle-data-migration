-- Schema for Kindle books table

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
