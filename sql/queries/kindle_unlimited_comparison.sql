-- Comparison of book performance between Kindle Unlimited and non Kindle Unlimited books

SELECT
    isKindleUnlimited,
    COUNT(*) AS total_books,
    ROUND(AVG(stars), 2) AS avg_rating, -- Average star rating
    ROUND(AVG(reviews), 1) AS avg_reviews, -- Average number of reviews
    ROUND(AVG(price), 2) AS avg_price, -- Average price
    ROUND(AVG(CASE WHEN isBestSeller THEN 1 ELSE 0 END) * 100, 1) AS bestseller_rate
FROM books
GROUP BY isKindleUnlimited;
