-- Summary of book performance by category

SELECT
    category_name,
    COUNT(*) AS total_books,
    ROUND(AVG(stars), 2) AS avg_rating, -- Average star rating
    ROUND(AVG(reviews), 1) AS avg_reviews, -- Average number of reviews
    ROUND(AVG(price), 2) AS avg_price, -- Average price
    ROUND(AVG(CASE WHEN isKindleUnlimited THEN 1 ELSE 0 END) * 100, 1) AS kindle_unlimted_percentage -- % of books in Kindle Unlimted
FROM books
GROUP BY category_name
ORDER BY total_books DESC;
