CREATE OR REPLACE VIEW best_sellers_by_reviews AS
SELECT
  title,
  author,
  stars,
  price,
  reviews,
  category_name
FROM books
WHERE isBestSeller = TRUE
  AND reviews > 0
ORDER BY reviews DESC, stars DESC
LIMIT 20;
