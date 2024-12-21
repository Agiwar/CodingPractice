-- You’re given a table that represents search results from searches on Facebook.
-- The query column is the search term, position column represents each position the search result came in,
-- and the rating column represents the human rating of the result from 1 to 5 where 5 is high relevance and 1 is low relevance.

-- Write a query to get the percentage of search queries where all of the ratings for the query results are less than a rating of 3.
-- Please round your answer to two decimal points.

-- search_results table

-- result_id	INTEGER (primary key)
-- query	    TEXT
-- position	    INTEGER
-- rating	    INTEGER

-- Output:
-- percentage_less_than_3	FLOAT



-- Main idea: Find out each query's all ratings which are all less than three, and count it's percentage.

-- solution 1
WITH rating_each_query AS (
    SELECT
        query,
        COUNT(ratings) AS total_ratings,
        SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) AS total_less_than_3_ratings
    FROM
        search_results
    GROUP BY
        query
)
SELECT
    ROUND(COUNT(query)::NUMERIC / (SELECT COUNT(query) FROM ratings_each_query)::NUMERIC, 2) AS percentage_less_than_3
From
    rating_each_query
WHERE
    total_ratings = total_less_than_3_ratings;


-- solution 2:
WITH rating_each_query AS (
    SELECT
        query,
        COUNT(rating) AS total_ratings,
        SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) AS total_less_than_3_ratings
    FROM
        search_results
    GROUP BY
        query
)
SELECT
    ROUND(AVG((total_ratings = total_less_than_3_ratings)::INT), 2) AS percentage_less_than_3
FROM
    rating_each_query