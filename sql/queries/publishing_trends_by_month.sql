-- Monthly publishing trends (recent 3 years only)
-- Includes number of books published and their average star rating per month

SELECT
    TO_CHAR(publishedDate, 'YYYY-MM') AS published_month, -- Convert date to year-month format
    COUNT(*) AS books_published, -- Number of books published that month
    ROUND(AVG(stars), 2) AS avg_rating -- Average rating of books published that month
FROM books
WHERE publishedDate >= DATEADD(year, -3, CURRENT_DATE) -- Limit to recent 3 years
GROUP BY published_month
ORDER BY published_month;
