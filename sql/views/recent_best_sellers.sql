CREATE OR REPLACE VIEW recent_best_sellers AS
SELECT
  title,
  author,
  stars,
  price,
  publishedDate,
  category_name
FROM books
WHERE isBestSeller = TRUE
  AND publishedDate >= DATEADD(YEAR, -1, CURRENT_DATE)
ORDER BY stars DESC, publishedDate DESC
LIMIT 20;
