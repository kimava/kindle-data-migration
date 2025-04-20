-- Performance summary of books by label types (Best Seller, Editor's Pick, Goodreads Choice)

SELECT
    'Best Seller' AS label,
    COUNT(*) AS count,
    ROUND(AVG(stars), 2) AS avg_rating,
    ROUND(AVG(reviews), 1) AS avg_reviews,
    ROUND(AVG(CASE WHEN isKindleUnlimited THEN 1 ELSE 0 END) * 100, 1) AS kindle_unlimited_percentage
FROM books
WHERE isBestSeller = TRUE

UNION ALL

SELECT
    'Editor''s Pick',
    COUNT(*),
    ROUND(AVG(stars), 2),
    ROUND(AVG(reviews), 1),
    ROUND(AVG(CASE WHEN isKindleUnlimited THEN 1 ELSE 0 END) * 100, 1)
FROM books
WHERE isEditorsPick = TRUE

UNION ALL

SELECT
    'Goodreads Choice',
    COUNT(*),
    ROUND(AVG(stars), 2),
    ROUND(AVG(reviews), 1),
    ROUND(AVG(CASE WHEN isKindleUnlimited THEN 1 ELSE 0 END) * 100, 1)
FROM books
WHERE isGoodReadsChoice = TRUE;
