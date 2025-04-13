CREATE OR REPLACE VIEW top_selling_categories AS
SELECT
  category_name,
  COUNT(*) AS total_books,
  ROUND(AVG(price), 2) AS avg_price,
  SUM(reviews) AS total_reviews
FROM books
GROUP BY category_name
ORDER BY total_reviews DESC
LIMIT 10;
