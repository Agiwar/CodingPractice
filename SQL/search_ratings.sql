-- a good research is high rating and low position

-- MySQL
SELECT
    query
    , ROUND(AVG(rating / position), 2) AS avg_rating
FROM
    search_results
GROUP BY
    query


-- PostgreSQL
SELECT
    query
    , ROUND(AVG(rating::NUMERIC / position::NUMERIC), 2) AS avg_rating
FROM
    search_results
GROUP BY
    query