-- Monthly publishing trends (2020.09 - 2023.09)
-- Includes number of books published and their average star rating per month

SELECT
    TO_CHAR(publishedDate, 'YYYY-MM') AS published_month, -- Convert date to year-month format
    COUNT(*) AS books_published, -- Number of books published that month
    ROUND(AVG(stars), 2) AS avg_rating -- Average rating of books published that month
FROM books
WHERE publishedDate >= '2020-09-01'
  AND publishedDate < '2023-10-01' 
GROUP BY published_month
ORDER BY published_month;
