-- Summary statistics for reviews and star ratings to support threshold definition for top books

-- 1. Summary statistics for review count
SELECT
    ROUND(AVG(reviews), 1) AS avg_reviews, -- Mean number of reviews
    MIN(reviews) AS min_reviews, -- Minimum number of reviews
    MAX(reviews) AS max_reviews, -- Maximum number of reviews
    APPROX_PERCENTILE(reviews, 0.5) AS median_reviews, -- Median number of reviews
    APPROX_PERCENTILE(reviews, 0.9) AS p90_reviews -- 90th percentile for reviews
FROM books;

-- 2. Summary statistics for star ratings
SELECT
    ROUND(AVG(stars), 2) AS avg_stars, -- Mean star rating
    MIN(stars) AS min_stars, -- Minimum star rating
    MAX(stars) AS max_stars, -- Maximum star rating
    APPROX_PERCENTILE(stars, 0.5) AS median_stars, -- Median star rating
    APPROX_PERCENTILE(stars, 0.9) AS p90_stars -- 90th percentile for star ratings
FROM books;
