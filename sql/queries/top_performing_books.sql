-- Top books based on high ratings and review count (90th percentile and above)
-- Tip: Thresholds were derived from reviews_stars_summary_stats.sql (90th percentile)

SELECT
  asin,
  title,
  author,
  stars,
  reviews,
  price,
  isKindleUnlimited,
  category_name
FROM books
WHERE stars >= 4.8 -- 90th percentile for star ratings
  AND reviews >= 1700 -- 90th percentile for review count
ORDER BY reviews DESC -- Most reviewed books first
LIMIT 50;